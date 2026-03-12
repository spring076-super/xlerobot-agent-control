from robot_client import send_request


def handle_head_action(request: dict) -> dict:
    return send_request(request)
