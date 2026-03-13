XLerobot Agent Control
Unified control skill and server for XLerobot on NVIDIA Jetson.
基于 NVIDIA Jetson 的 XLerobot 统一控制技能与服务器。

Overview / 项目概览
This project provides a structured interface to control the XLerobot's body (base, head, and arms) through a single local server. It is specifically designed for integration with LLM agents, ensuring that hardware connections are managed safely and commands follow strict physical constraints.

本项目提供了一个结构化接口，通过单一本地服务器控制 XLerobot 的躯体（底盘、头部和机械臂）。它专为大语言模型（LLM）智能体集成而设计，确保硬件连接的安全管理，并使指令遵循严格的物理约束。

Key Features / 核心功能
Centralized Arbitration: A single robot server owns the hardware port to prevent serial conflicts.
集中仲裁：单一机器人服务器占用硬件端口，防止串口冲突。

Safety Guards: Automatic clamping of motion duration (0.1s - 3.0s) and speed limits.
安全防护：自动限制动作持续时间（0.1s - 3.0s）及速度上限。

Unified Schema: Simple JSON API for all body parts: move_base, set_head, reset_arm, etc.
统一模式：底盘、头部、机械臂共用简单的 JSON API：move_base, set_head, reset_arm 等。

State Management: Real-time observation caching and robot status queries.
状态管理：实时观测值缓存及机器人状态查询。

Architecture / 架构设计
scripts/robot_server.py: The persistent process that talks to the hardware.
与硬件通信的常驻进程。

scripts/execute_action.py: The entry point for the LLM skill to send commands.
LLM 技能发送指令的入口点。

scripts/core/robot_orchestrator.py: Coordinates controllers and state.
协调控制器与状态的核心逻辑。

scripts/safety_guard.py: Validates every request against safety rules.
根据安全规则校验每一项请求。

Usage / 使用方法
1. Start the Server / 启动服务器
On the Jetson device, run:
在 Jetson 设备上运行：
python scripts/robot_server.py

2. Execute an Action / 执行动作
Use the client script to send a JSON payload:
使用客户端脚本发送 JSON 载荷：
python scripts/execute_action.py '{"action_type":"move_base","parameters":{"direction":"forward","duration":1.0,"speed":0.15}}'

License / 许可协议
This project is licensed under the Apache License 2.0.
本项目采用 Apache License 2.0 许可协议。
