---
description: "Prepare PlatformIO project for debugging or launch debug server."
---

<a id="cmd-debug"></a>

# pio debug {#pio-debug}

Helper command for [Debugging](../../guides/debugging/index.md).

## Usage {#usage}

```bash
pio debug [OPTIONS]

# A binary shortcut for "pio debug --interface=gdb" command
piodebuggdb [GDB OPTIONS]
```

## Description {#description}

Prepare PlatformIO project for debugging or launch debug server.

## Options {#options}

<a id="cmdoption-pio-debug-environment"></a>

### `-e, --environment` {#cmdoption-pio-debug-e}

Debug specified environments.

You can also specify which environments should be used for debugging by default using [default_envs](../platformio-ini/platformio/default-envs.md) option from [`platformio.ini`](../platformio-ini/index.md).

<a id="cmdoption-pio-debug-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-debug-d}

The project directory. Default: the current working directory.

<a id="cmdoption-pio-debug-project-conf"></a>

### `-c, --project-conf` {#cmdoption-pio-debug-c}

Process project with a custom [`platformio.ini`](../platformio-ini/index.md).

### `--load-mode` {#cmdoption-pio-debug-load-mode}

Override [debug_load_mode](../platformio-ini/env/debug-load-mode.md) option.

### `--interface` {#cmdoption-pio-debug-interface}

PlatformIO Debugging Interface. Valid values:

- `gdb` - GDB: The GNU Project Debugger

<a id="cmdoption-pio-debug-verbose"></a>

### `-v, --verbose` {#cmdoption-pio-debug-v}

Print detailed information while processing environments.

This option can also be set globally using [force_verbose](./pio-settings.md#setting-force-verbose) setting or by environment variable [`PLATFORMIO_SETTING_FORCE_VERBOSE`](../environment-variables.md#envvar-PLATFORMIO_SETTING_FORCE_VERBOSE).

## Examples {#examples}

Prepare a project for debugging:

```bash
pio debug
```

```text
[Sun Apr 30 01:34:01 2017] Processing mzeropro (platform: atmelsam; debug_extra_cmds: b main.cpp:26; board: mzeropro; framework: arduino)
-----------------------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
Collected 26 compatible libraries
Looking for dependencies...
Project does not have dependencies
Compiling .pio/build/mzeropro/src/main.o
Compiling .pio/build/mzeropro/FrameworkArduinoVariant/variant.o
Compiling .pio/build/mzeropro/FrameworkArduino/IPAddress.o
Compiling .pio/build/mzeropro/FrameworkArduino/Print.o
Archiving .pio/build/mzeropro/libFrameworkArduinoVariant.a
Indexing .pio/build/mzeropro/libFrameworkArduinoVariant.a
...
Compiling .pio/build/mzeropro/FrameworkArduino/wiring_analog.o
Compiling .pio/build/mzeropro/FrameworkArduino/wiring_digital.o
Compiling .pio/build/mzeropro/FrameworkArduino/wiring_private.o
Compiling .pio/build/mzeropro/FrameworkArduino/wiring_shift.o
Archiving .pio/build/mzeropro/libFrameworkArduino.a
Indexing .pio/build/mzeropro/libFrameworkArduino.a
Linking .pio/build/mzeropro/firmware.elf
Calculating size .pio/build/mzeropro/firmware.elf
Building .pio/build/mzeropro/firmware.bin
text       data     bss     dec     hex filename
11512       256    1788   13556    34f4 .pio/build/mzeropro/firmware.elf
=========================== [SUCCESS] Took 7.82 seconds ===========================
```

Launch GDB instance and load initial configuration per project. A double hyphen is used to skip the parsing of extra GDB options.:

```bash
pio debug --interface=gdb -- -x .pioinit
```

```text
...
Loading section .text, size 0x2c98 lma 0x4000
Loading section .ramfunc, size 0x60 lma 0x6c98
Loading section .data, size 0x100 lma 0x6cf8
Start address 0x47b0, load size 11768
Transfer rate: 4 KB/sec, 3922 bytes/write.
target halted due to debug-request, current mode: Thread
xPSR: 0x81000000 pc: 0x000028f4 msp: 0x20002c00
target halted due to debug-request, current mode: Thread
xPSR: 0x81000000 pc: 0x000028f4 msp: 0x20002c00
Breakpoint 2 at 0x413a: file src/main.cpp, line 26.
```
