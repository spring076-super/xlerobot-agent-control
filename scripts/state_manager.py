class StateManager:
    def __init__(self):
        self.last_observation = {}
        self.busy = False
        self.estop = False
        self.last_error = None

    def snapshot(self) -> dict:
        return {
            "busy": self.busy,
            "estop": self.estop,
            "last_error": self.last_error,
            "last_observation": self.last_observation,
        }
