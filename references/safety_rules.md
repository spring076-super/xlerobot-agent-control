# Safety rules

- Use one local robot server as the only process that owns `robot.connect()`.
- Clamp all base durations to `0.1` to `3.0` seconds.
- Clamp base speed to conservative values. The default implementation uses `0.15` for translation and `0.30` for rotation unless the robot team changes limits.
- Always stop the base after timed motion.
- Use `stop_all` for emergency language, collision risk, or uncertainty about current execution state.
- Prefer a query with `get_robot_state` before larger motions.
- Do not send arbitrary raw joint or wheel commands from the skill interface.
