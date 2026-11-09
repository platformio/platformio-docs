---
description: "Allows one to setup a custom debugging server (platformio.ini option debug_server)."
---

<a id="projectconf-debug-server"></a>

# `debug_server` {#debug-server}

- **Type:** String
- **Multiple values:** Yes

Allows one to setup a custom debugging server. By default, boards are pre-configured with a debugging server that is compatible with "on-board" debugging tool (adapter, probe). Also, this option is useful for a [Custom](../../../hardware/debug-probes/custom.md) debugging tool.

**Option format (multi-line)**:

- First line is an executable path of debugging server
- 2-nd and the next lines are arguments for executable file

**Examples:**

```ini
[env:debug]
platform = ...
board = ...
debug_server =
  /path/to/debugging/server
  arg1
  arg2
  ...
  argN

[env:debug_openocd]
platform = ...
board = ...
debug_tool = custom
debug_server =
    ${platformio.packages_dir}/tool-openocd/openocd
    -f
    ${platformio.packages_dir}/tool-openocd/scripts/board/stm32f103zet6_warship.cfg
```
