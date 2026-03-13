# Teleop mapping

Legacy keyboard mappings become structured actions.

## Base
- `i` -> `move_base(direction="forward")`
- `k` -> `move_base(direction="backward")`
- `j` -> `move_base(direction="left")`
- `l` -> `move_base(direction="right")`
- `u` -> `move_base(direction="rotate_left")`
- `o` -> `move_base(direction="rotate_right")`
- emergency stop key or stop request -> `stop_all()`

## Head
Head key presses become `set_head(...)` deltas or `reset_head()`.

## Arms
Reset keys become `reset_arm(side=...)`.
