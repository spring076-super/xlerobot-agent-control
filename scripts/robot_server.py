#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from core.robot_orchestrator import RobotOrchestrator
from safety_guard import validate_request

ORCH = RobotOrchestrator()


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/action":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)
        try:
            payload = json.loads(body.decode("utf-8"))
            request = validate_request(payload)
            action_type = request["action_type"]
            params = request["parameters"]

            if action_type == "move_base":
                result = ORCH.move_base(**params)
            elif action_type == "stop_base":
                result = ORCH.stop_base()
            elif action_type == "set_head":
                result = ORCH.set_head(**params)
            elif action_type == "reset_head":
                result = ORCH.reset_head()
            elif action_type == "reset_arm":
                result = ORCH.reset_arm(**params)
            elif action_type == "get_robot_state":
                result = ORCH.get_robot_state()
            elif action_type == "stop_all":
                result = ORCH.stop_all()
            else:
                raise ValueError(f"unsupported action_type: {action_type}")

            self._send_json(200, {"ok": True, "result": result})
        except Exception as exc:
            self._send_json(400, {"ok": False, "error": str(exc)})

    def log_message(self, format, *args):
        return

    def _send_json(self, status: int, payload: dict):
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main():
    server = HTTPServer(("127.0.0.1", 8765), Handler)
    print("XLerobot robot_server listening on http://127.0.0.1:8765/action")
    server.serve_forever()


if __name__ == "__main__":
    main()
