#!/usr/bin/env python3
"""
record_artifacts_produced.py — deterministic SessionEnd hook (project-local).

Records, into session_topology.yaml under the current SID, the artifact files
created or modified during the session. The list is DERIVED FROM THE FILESYSTEM
(file mtime >= session start), NOT from any agent self-report — provenance-
independent ground truth (cf. decision_log: "il git diff e' evidenza, il
self-report di un agente no").

Wired in .claude/settings.local.json under hooks.SessionEnd (additive; runs
alongside mhc_end.py and relocate_conversation.py).

Discipline-grade, not adversarial: it records what changed, deterministically.
It does not provide cryptographic tamper-evidence (that is MHC-H's domain).

Never raises: any failure degrades to a JSON sidecar so session close is never
blocked.
"""
import json
import os
import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))

# Artifact types to capture. Conversations are excluded on purpose: the
# transcript is the INDEPENDENT source we check against, not a produced artifact.
CAPTURE_KEYS = ["notes", "traces", "modlogs", "pdl", "prompts"]


def main():
    cfg_path = os.path.join(ROOT, ".mhc-config.json")
    topo_path = os.path.join(ROOT, "session_topology.yaml")
    try:
        with open(cfg_path, encoding="utf-8") as fh:
            cfg = json.load(fh)
    except Exception:
        return

    cur = cfg.get("current_session", {})
    sid = cur.get("id") or cur.get("sid")
    started = cur.get("started") or cur.get("started_at")
    if not sid or not started:
        return
    try:
        start_ts = datetime.datetime.fromisoformat(started).timestamp()
    except Exception:
        return

    folders = cfg.get("folders", {})
    produced = []
    for key in CAPTURE_KEYS:
        rel = folders.get(key)
        if not rel:
            continue
        base = os.path.join(ROOT, rel)
        if not os.path.isdir(base):
            continue
        for dirpath, _dirs, files in os.walk(base):
            for fn in files:
                if not fn.endswith(".md"):
                    continue
                fp = os.path.join(dirpath, fn)
                try:
                    if os.path.getmtime(fp) >= start_ts:
                        produced.append(os.path.relpath(fp, ROOT).replace("\\", "/"))
                except OSError:
                    continue
    produced = sorted(set(produced))

    _write_topology(topo_path, sid, produced)


def _write_topology(topo_path, sid, produced):
    """Idempotent, dependency-light update. Prefer pyyaml; fall back to sidecar."""
    try:
        import yaml  # type: ignore
        data = {}
        if os.path.exists(topo_path):
            with open(topo_path, encoding="utf-8") as fh:
                data = yaml.safe_load(fh) or {}
        sessions = data.setdefault("sessions", {})
        entry = sessions.setdefault(sid, {})
        entry["artifacts_produced"] = produced
        with open(topo_path, "w", encoding="utf-8") as fh:
            yaml.safe_dump(data, fh, allow_unicode=True, sort_keys=False)
    except Exception:
        sidecar = os.path.join(os.path.dirname(topo_path),
                               "artifacts_produced_%s.json" % sid)
        try:
            with open(sidecar, "w", encoding="utf-8") as fh:
                json.dump({"sid": sid, "artifacts_produced": produced},
                          fh, ensure_ascii=False, indent=2)
        except Exception:
            pass


if __name__ == "__main__":
    main()
