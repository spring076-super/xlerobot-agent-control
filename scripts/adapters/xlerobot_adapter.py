import logging
import numpy as np
from lerobot.robots.lekiwi.lekiwi import LeKiwi
from lerobot.robots.lekiwi.config_lekiwi import LeKiwiConfig

class XLerobotAdapter:
    def __init__(self):
        self._connected = False
        
        self.config = LeKiwiConfig(
            port="/dev/ttyACM0",  # Linux 默认端口，Mac 可能是 /dev/tty.usbmodemXXX
            use_degrees=True      # 统一使用角度 (degrees) 作为关节单位
        )
        self.robot = LeKiwi(self.config)

    def connect(self):
        if not self._connected:
            self.robot.connect(calibrate=False)
            self._connected = True

    def disconnect(self):
        if self._connected:
            self.robot.disconnect()
            self._connected = False

    def get_observation(self) -> dict:
        if not self._connected:
            return {"connected": False, "error": "Robot not connected."}
        
        raw_obs = self.robot.get_observation()
        safe_obs = {"connected": self._connected}
        
        # 剥离/转换图像数据，防止 JSON 序列化崩溃
        # LLM 决策通常只需要位置和速度等本体感受 (Proprioception)
        for key, value in raw_obs.items():
            if isinstance(value, (int, float, bool, str)):
                safe_obs[key] = value
            elif isinstance(value, np.ndarray) and value.ndim == 1:
                safe_obs[key] = value.tolist()
            elif hasattr(value, "item"):  # 处理标量 tensor 或 numpy float
                try:
                    safe_obs[key] = value.item()
                except ValueError:
                    pass # 忽略高维图像张量
                    
        return safe_obs

    def send_base(self, vx: float, vy: float, wz: float):
        if not self._connected:
            return
        
        # LeKiwi 要求 theta.vel 的单位是度/秒 (deg/s)。
        # 如果你的 LLM Agent 发送的是 rad/s，需要在这里转换 wz = wz * (180 / np.pi)
        action = {
            "x.vel": vx,          # m/s
            "y.vel": vy,          # m/s
            "theta.vel": wz       # deg/s 
        }
        self.robot.send_action(action)

    def reset_arm(self, side: str = "right"):
        if not self._connected:
            return
            
        # 3. 提供真实的 SO101 安全重置姿态 (全部归零或归中)
        reset_action = {
            "arm_shoulder_pan.pos": 0.0,
            "arm_shoulder_lift.pos": 0.0,
            "arm_elbow_flex.pos": 0.0,
            "arm_wrist_flex.pos": 0.0,
            "arm_wrist_roll.pos": 0.0,
            "arm_gripper.pos": 100.0,  # 100通常代表张开
        }
        self.robot.send_action(reset_action)

    def stop_all(self):
        if self._connected:
            self.robot.stop_base()
            # 可以发送当前位置指令让手臂定住，此处底盘停止最重要