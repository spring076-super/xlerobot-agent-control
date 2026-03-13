from robot_client import send_request


def handle_global_action(request: dict) -> dict:
    return send_request(request)
