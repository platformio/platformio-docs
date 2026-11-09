---
description: "Initial commands to be passed to a back-end debugger (platformio.ini option debug_init_cmds)."
---

# `debug_init_cmds`

- **Type:** String
- **Multiple values:** Yes

Initial commands that will be passed to back-end debugger.

PlatformIO dynamically configures back-end debugger depending on a debug environment. Here is [a list with default initial commands](https://github.com/platformio/platformio-core/tree/develop/platformio/debug/config) for the popular [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools).

For example, the custom initial commands for GDB:

```ini
[env:debug]
platform = ...
board = ...
debug_init_cmds =
  target extended-remote $DEBUG_PORT
  $INIT_BREAK
  monitor reset halt
  $LOAD_CMDS
  monitor init
  monitor reset halt
```
