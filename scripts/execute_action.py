#!/usr/bin/env python3
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from action_router import route_action
from safety_guard import validate_request


def main() -> int:
    if len(sys.argv) != 2:
        print(json.dumps({
            "ok": False,
            "error": "usage: python scripts/execute_action.py '{\"action_type\":\"...\",\"parameters\":{}}'"
        }))
        return 2

    try:
        request = json.loads(sys.argv[1])
    except json.JSONDecodeError as exc:
        print(json.dumps({"ok": False, "error": f"invalid json: {exc}"}))
        return 2

    try:
        normalized = validate_request(request)
        result = route_action(normalized)
        print(json.dumps({"ok": True, "result": result}, ensure_ascii=False))
        return 0
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
