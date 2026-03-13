# Hardware notes

This skill assumes XLerobot uses one shared hardware connection for base, arms, and head.

Rationale:
- One serial or motor bus may be shared across body parts.
- Independent processes can fight over the same port and fail with `device busy` or permission errors.
- A single server can keep one observation cache for all body parts.
- Safety actions such as `stop_all` must be global and atomic.
