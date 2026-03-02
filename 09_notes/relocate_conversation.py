#!/usr/bin/env python3
"""
MHC project hook: relocate 06_conversations/exported/ -> 00_conversations_full/exported/

Runs as a SessionEnd hook AFTER extract_conversation.py.
Receives the same Claude Code hook payload on stdin (JSON with cwd, transcript_path, session_id).

Moves any .md files deposited by the prototype script into 06_conversations/exported/
to the canonical project archive at 00_conversations_full/exported/.
The 06_conversations/ folder is left in place (gitignored, harmless).

Decision note: folder is not deleted because the prototype script recreates it every
session anyway; deletion adds a step that solves nothing.
"""

import json
import sys
import shutil
from pathlib import Path


def main():
    project_cwd = None

    if not sys.stdin.isatty():
        try:
            payload = json.loads(sys.stdin.read())
            project_cwd = payload.get("cwd")
        except json.JSONDecodeError as e:
            print(f"Warning: could not parse hook payload: {e}", file=sys.stderr)

    if not project_cwd:
        # Fallback: script lives in 09_notes/ -> parent is project root
        project_cwd = str(Path(__file__).resolve().parent.parent)
        print(f"Warning: no cwd in payload, using script-derived path: {project_cwd}",
              file=sys.stderr)

    project = Path(project_cwd)
    src = project / "06_conversations" / "exported"
    dst = project / "00_conversations_full" / "exported"

    if not src.exists():
        print("relocate_conversation: nothing to do (06_conversations/exported/ not found).")
        return

    dst.mkdir(parents=True, exist_ok=True)

    moved = 0
    for f in src.glob("*.md"):
        dest_file = dst / f.name
        shutil.move(str(f), dest_file)
        print(f"relocate_conversation: {f.name} -> 00_conversations_full/exported/")
        moved += 1

    if moved == 0:
        print("relocate_conversation: no .md files to relocate.")
    else:
        print(f"relocate_conversation: {moved} file(s) relocated.")


if __name__ == "__main__":
    main()
