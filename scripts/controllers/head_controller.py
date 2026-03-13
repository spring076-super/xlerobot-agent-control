class HeadController:
    def __init__(self, adapter):
        self.adapter = adapter

    def set_head(self, head_motor_1: float, head_motor_2: float) -> dict:
        self.adapter.send_head(head_motor_1=head_motor_1, head_motor_2=head_motor_2)
        return {
            "executed": "set_head",
            "head_motor_1": head_motor_1,
            "head_motor_2": head_motor_2,
        }

    def reset(self) -> dict:
        self.adapter.send_head(head_motor_1=0.0, head_motor_2=0.0)
        return {"executed": "reset_head"}
