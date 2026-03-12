class ArmController:
    def __init__(self, adapter):
        self.adapter = adapter

    def reset_arm(self, side: str) -> dict:
        self.adapter.reset_arm(side)
        return {"executed": "reset_arm", "side": side}
