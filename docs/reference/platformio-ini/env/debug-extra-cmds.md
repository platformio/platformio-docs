---
description: "An extra commands to be passed to a back-end debugger (platformio.ini option debug_extra_cmds)."
---

# `debug_extra_cmds`

- **Type:** String
- **Multiple values:** Yes

Extra commands that will be passed to back-end debugger after [debug_init_cmds](./debug-init-cmds.md). For example, add custom breakpoint and load `.gdbinit` from a project directory for GDB:

```ini
[env:debug]
platform = ...
board = ...
debug_extra_cmds =
  break main.cpp:13
  break foo.cpp:100
  source .gdbinit
```

:::note

**Initial Project Breakpoints**: Use `break path/to/file:LINE_NUMBER` to define initial breakpoints for debug environment. Multiple breakpoints are allowed.

To save session breakpoints, please use `save breakpoints [filename]` command in Debug Console. For example, `save breakpoints .gdbinit`. Later, this file could be loaded via `source [filename]` command. See above.

:::
