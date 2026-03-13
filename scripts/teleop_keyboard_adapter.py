#!/usr/bin/env python3
"""
Bridge legacy keyboard inputs into the unified action schema.

This file is intentionally small. The goal is to keep keyboard input as an adapter,
not as the place where robot control logic lives.
"""


def pressed_keys_to_action(pressed_keys: set[str]) -> dict | None:
    if "i" in pressed_keys:
        return {"action_type": "move_base", "parameters": {"direction": "forward", "duration": 0.1, "speed": 0.15}}
    if "k" in pressed_keys:
        return {"action_type": "move_base", "parameters": {"direction": "backward", "duration": 0.1, "speed": 0.15}}
    if "j" in pressed_keys:
        return {"action_type": "move_base", "parameters": {"direction": "left", "duration": 0.1, "speed": 0.15}}
    if "l" in pressed_keys:
        return {"action_type": "move_base", "parameters": {"direction": "right", "duration": 0.1, "speed": 0.15}}
    if "u" in pressed_keys:
        return {"action_type": "move_base", "parameters": {"direction": "rotate_left", "duration": 0.1, "speed": 0.30}}
    if "o" in pressed_keys:
        return {"action_type": "move_base", "parameters": {"direction": "rotate_right", "duration": 0.1, "speed": 0.30}}
    return None
