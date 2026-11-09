---
description: Debug options of the platformio.ini [env] section.
---

# Debug options

Configure debugging with `pio debug` and PlatformIO IDE.

| Option | Description |
| --- | --- |
| [`debug_tool`](./debug-tool.md) | A name of debugging tool |
| [`debug_build_flags`](./debug-build-flags.md) | Custom debug flags/options for preprocessing, compilation, assembly, and linking processes |
| [`debug_init_break`](./debug-init-break.md) | An initial breakpoint that makes program stop whenever a certain point in the program is reached |
| [`debug_init_cmds`](./debug-init-cmds.md) | Initial commands to be passed to a back-end debugger |
| [`debug_extra_cmds`](./debug-extra-cmds.md) | An extra commands to be passed to a back-end debugger |
| [`debug_load_cmds`](./debug-load-cmds.md) | A list of commands to be used to load program/firmware to a target device |
| [`debug_load_mode`](./debug-load-mode.md) | Allows one to control when PlatformIO should load debugging firmware to the end target |
| [`debug_server`](./debug-server.md) | Allows one to setup a custom debugging server |
| [`debug_port`](./debug-port.md) | A debugging port of a remote target (a serial device or network address) |
| [`debug_speed`](./debug-speed.md) | A debug adapter speed (JTAG speed) |
| [`debug_svd_path`](./debug-svd-path.md) | A custom path to SVD file which contains information about device peripherals |
| [`debug_server_ready_pattern`](./debug-server-ready-pattern.md) | A pattern to determine when debugging server is ready for an incoming connection |
| [`debug_test`](./debug-test.md) | A name of a unit test to be debugged |
