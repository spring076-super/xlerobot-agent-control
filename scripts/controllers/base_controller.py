import time


class BaseController:
    def __init__(self, adapter, control_hz: int = 20):
        self.adapter = adapter
        self.control_hz = control_hz

    def move(self, direction: str, duration: float, speed: float) -> dict:
        vx = vy = wz = 0.0
        if direction == "forward":
            vx = speed
        elif direction == "backward":
            vx = -speed
        elif direction == "left":
            vy = speed
        elif direction == "right":
            vy = -speed
        elif direction == "rotate_left":
            wz = speed
        elif direction == "rotate_right":
            wz = -speed
        else:
            raise ValueError(f"unsupported direction: {direction}")

        dt = 1.0 / self.control_hz
        end_time = time.time() + duration
        while time.time() < end_time:
            self.adapter.send_base(vx=vx, vy=vy, wz=wz)
            time.sleep(dt)
        self.stop()
        return {
            "executed": "move_base",
            "direction": direction,
            "duration": duration,
            "speed": speed,
        }

    def stop(self) -> dict:
        self.adapter.send_base(vx=0.0, vy=0.0, wz=0.0)
        return {"executed": "stop_base"}
