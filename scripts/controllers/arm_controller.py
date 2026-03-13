class ArmController:
    def __init__(self, adapter):
        self.adapter = adapter

    def reset_arm(self) -> dict:
        self.adapter.reset_arm()
        return {"executed": "reset_arm"}
