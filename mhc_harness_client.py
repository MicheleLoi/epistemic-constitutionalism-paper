"""
mhc_harness_client — MHC-W-backed adapter (shim) for the MHC harness interface.

Implements the harness contract expected by the harness-aware MHC-C skills
(mhc-place -> placement_log, mhc-reconcile -> reconcile_check) with a MHC-W
backend: an append-only ledger (_org/harness_log.jsonl) for agent-registered
artifacts, cross-checked against the DETERMINISTIC session record
(session_topology.yaml `artifacts_produced`, written by the SessionEnd hook
record_artifacts_produced.py) and against files on disk.

Grade: discipline / provenance-grade. NOT adversarial — no cryptographic
tamper-evidence, no third-party-demonstrable chain, no cross-machine. Those
remain MHC-H's domain; the crypto functions below are declared stubs that
refuse rather than fake a guarantee.

Continuity of function: the harness-aware skills depend on this interface, not
on a specific backend. Today it routes to MHC-W; if MHC-H arrives, the same
contract can point to the server without changing the skills.

The module lives in the project root; ROOT is derived from __file__, so it works
regardless of the current working directory. To import it, the project root must
be on sys.path (run python from the project root, or set PYTHONPATH).
"""
import os
import json
import hashlib
import datetime

SCHEMA_VERSION = "1"
ROOT = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(ROOT, ".mhc-config.json")
LEDGER = os.path.join(ROOT, "_org", "harness_log.jsonl")
TOPOLOGY = os.path.join(ROOT, "session_topology.yaml")


# --- helpers ---------------------------------------------------------------

def _now_iso():
    return datetime.datetime.now().isoformat(timespec="seconds")


def _entry_id(*parts):
    blob = "|".join(str(p) for p in parts).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:16]


def _load_config():
    with open(CONFIG, encoding="utf-8") as fh:
        return json.load(fh)


def _append_ledger(record):
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def _read_ledger():
    if not os.path.exists(LEDGER):
        return []
    out = []
    with open(LEDGER, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except ValueError:
                continue
    return out


def _deterministic_observed():
    """Artifacts seen by the SessionEnd hook (independent, machine-generated
    ground truth). Reads session_topology.yaml via pyyaml, plus the sidecar
    JSON files the hook writes when pyyaml is absent."""
    observed = set()
    try:
        import yaml  # type: ignore
        if os.path.exists(TOPOLOGY):
            with open(TOPOLOGY, encoding="utf-8") as fh:
                data = yaml.safe_load(fh) or {}
            for sess in (data.get("sessions") or {}).values():
                for p in (sess.get("artifacts_produced") or []):
                    observed.add(p)
    except Exception:
        pass
    try:
        for fn in os.listdir(ROOT):
            if fn.startswith("artifacts_produced_") and fn.endswith(".json"):
                try:
                    with open(os.path.join(ROOT, fn), encoding="utf-8") as fh:
                        for p in (json.load(fh).get("artifacts_produced") or []):
                            observed.add(p)
                except Exception:
                    continue
    except Exception:
        pass
    return observed


# --- session ---------------------------------------------------------------

def get_session():
    """Current session coordinates from MHC-W config, or None."""
    try:
        cur = _load_config().get("current_session", {})
        sid = cur.get("id") or cur.get("sid")
        if not sid:
            return None
        return {"sid": sid, "started": cur.get("started") or cur.get("started_at")}
    except Exception:
        return None


# --- register / placement --------------------------------------------------

def register(artifact, type, sid=None):
    """Append an artifact registration to the MHC-W ledger. discipline-grade."""
    try:
        sid = sid or (get_session() or {}).get("sid")
        eid = _entry_id("register", type, artifact, sid, _now_iso())
        _append_ledger({"entry_id": eid, "type": type, "artifact": artifact,
                        "sid": sid, "created": _now_iso()})
        return {"schema_version": SCHEMA_VERSION, "entry_id": eid, "status": "ok"}
    except Exception as exc:
        return {"schema_version": SCHEMA_VERSION, "entry_id": None,
                "status": "unreachable", "fallback_reason": str(exc)}


def placement_log(artifact_description, proposed_path, predicted_tier, session_id):
    """Harness endpoint consumed by /mhc-place Step 6. discipline-grade.

    Records the placement prediction in the MHC-W ledger. Returns the contract
    dict the skill expects: status 'ok' on a successful local append.
    """
    try:
        eid = _entry_id("placement", artifact_description, proposed_path,
                        session_id, _now_iso())
        _append_ledger({"entry_id": eid, "type": "placement",
                        "description": artifact_description, "path": proposed_path,
                        "tier": predicted_tier, "sid": session_id,
                        "created": _now_iso()})
        return {"schema_version": SCHEMA_VERSION, "entry_id": eid, "status": "ok"}
    except Exception as exc:
        return {"schema_version": SCHEMA_VERSION, "entry_id": None,
                "status": "unreachable", "fallback_reason": str(exc)}


def list_artifacts(sid=None):
    """List ledger entries, optionally filtered by session id."""
    entries = _read_ledger()
    if sid:
        entries = [e for e in entries if e.get("sid") == sid]
    return entries


# --- reconcile -------------------------------------------------------------

def reconcile_check(diff, last_session_iso):
    """Harness endpoint consumed by /mhc-reconcile Step 5. discipline-grade.

    Cross-checks agent-registered placements (ledger) since last_session_iso
    against files on disk. `server_entries_count` is anchored to the DETERMINISTIC
    record (artifacts_produced from the SessionEnd hook) when available — the
    independent, machine-generated source. A registered path absent from disk is
    flagged as drift (a claim with no ground-truth backing).

    Catches agent drift; does NOT provide adversarial tamper-evidence (MHC-H).
    The `diff` argument is accepted for contract compatibility (the skill's
    filesystem diff); semantic matching against it is a future enrichment.
    """
    try:
        observed = _deterministic_observed()
        drift_details = []
        considered = 0
        for entry in _read_ledger():
            created = entry.get("created", "")
            if last_session_iso and created and created < last_session_iso:
                continue
            path = entry.get("path")
            if not path:
                continue
            considered += 1
            if not os.path.exists(os.path.join(ROOT, path)):
                drift_details.append(
                    "registrato %s -> %s : assente su disco (claim senza ground truth)"
                    % (entry.get("entry_id"), path))
        return {
            "schema_version": SCHEMA_VERSION,
            "server_entries_count": len(observed) if observed else considered,
            "drift_detected": bool(drift_details),
            "drift_details": drift_details,
            "status": "ok",
        }
    except Exception as exc:
        return {
            "schema_version": SCHEMA_VERSION,
            "server_entries_count": 0,
            "drift_detected": False,
            "drift_details": [],
            "status": "unreachable",
            "fallback_reason": str(exc),
        }


# --- crypto: MHC-H only (declared stubs, never faked) ----------------------

class HarnessNotAvailable(RuntimeError):
    """Raised by adversarial-grade operations that the MHC-W backend cannot honour."""


def _requires_mhc_h(name):
    raise HarnessNotAvailable(
        "%s requires MHC-H (blind encrypted custodian). The MHC-W adapter is "
        "discipline-grade and does not provide cryptographic guarantees." % name)


def encrypt(content, key):
    _requires_mhc_h("encrypt")


def decrypt(ciphertext, key):
    _requires_mhc_h("decrypt")


def derive_key(passphrase, salt):
    _requires_mhc_h("derive_key")


def verify_signature(ciphertext, signature):
    _requires_mhc_h("verify_signature")
