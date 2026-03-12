class XLerobotAdapter:
    """
    Replace the placeholder methods with real XLerobot integration.

    Intended real wiring:
    - construct XLerobotConfig / XLerobot
    - connect once in the server process
    - use robot.get_observation() and robot.send_action(...)
    - translate structured base/head/arm commands into the action dict expected by XLerobot
    """

    def __init__(self):
        self._connected = False
        self._last_action = {}

    def connect(self):
        self._connected = True

    def disconnect(self):
        self._connected = False

    def get_observation(self) -> dict:
        return {
            "connected": self._connected,
            "last_action": self._last_action,
        }

    def send_base(self, vx: float, vy: float, wz: float):
        self._last_action = {"base.vx": vx, "base.vy": vy, "base.wz": wz}

    def send_head(self, head_motor_1: float, head_motor_2: float):
        self._last_action = {
            "head_motor_1.pos": head_motor_1,
            "head_motor_2.pos": head_motor_2,
        }

    def reset_arm(self, side: str):
        self._last_action = {"reset_arm": side}

    def stop_all(self):
        self._last_action = {
            "base.vx": 0.0,
            "base.vy": 0.0,
            "base.wz": 0.0,
            "stop_all": True,
        }
