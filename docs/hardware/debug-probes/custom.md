---
description: "Use the Custom debug probe with PlatformIO: configuration, drivers, wiring and supported boards."
---

# Custom

<dl>

<dt>

Configuration

</dt>

<dd>

[debug_tool](../../reference/platformio-ini/env/debug-tool.md) = `custom`

</dd>

</dl>

**PLatformIO Debugging Solution** can be configured using [`platformio.ini`](../../reference/platformio-ini/index.md):

- [Debugging options](../../reference/platformio-ini/env/debug-options.md)

  - [`debug_tool`](../../reference/platformio-ini/env/debug-tool.md)
  - [`debug_build_flags`](../../reference/platformio-ini/env/debug-build-flags.md)
  - [`debug_init_break`](../../reference/platformio-ini/env/debug-init-break.md)
  - [`debug_init_cmds`](../../reference/platformio-ini/env/debug-init-cmds.md)
  - [`debug_extra_cmds`](../../reference/platformio-ini/env/debug-extra-cmds.md)
  - [`debug_load_cmds`](../../reference/platformio-ini/env/debug-load-cmds.md)
  - [`debug_load_mode`](../../reference/platformio-ini/env/debug-load-mode.md)
  - [`debug_server`](../../reference/platformio-ini/env/debug-server.md)
  - [`debug_port`](../../reference/platformio-ini/env/debug-port.md)
  - [`debug_speed`](../../reference/platformio-ini/env/debug-speed.md)
  - [`debug_svd_path`](../../reference/platformio-ini/env/debug-svd-path.md)
  - [`debug_server_ready_pattern`](../../reference/platformio-ini/env/debug-server-ready-pattern.md)
  - [`debug_test`](../../reference/platformio-ini/env/debug-test.md)

## Examples {#examples}

### J-Link and ST nucleo {#j-link-and-st-nucleo}

Segger J-Link probe and ST Nucleo F446RE board in pair with J-Link GDB Server:

- Install [J-Link GDB Server](https://www.segger.com/products/debug-probes/j-link/tools/j-link-gdb-server/about-j-link-gdb-server/?utm_source=platformio&utm_medium=docs)
- [Convert ST-LINK On-Board Into a J-Link](https://www.segger.com/products/debug-probes/j-link/models/other-j-links/st-link-on-board/?utm_source=platformio&utm_medium=docs)

:::note

You can use configuration below in pair with other boards, not only with ST Nucleo F446RE. In this case, please replace `STM32F446RE` with your own device name in `debug_server` option.

See full list with [J-Link Supported Devices](https://www.segger.com/downloads/supported_devices_jlink.php?utm_source=platformio&utm_medium=docs).

:::

```ini
[env:debug_jlink]
platform = ststm32
framework = mbed
board = nucleo_f446re

debug_tool = custom
debug_port = :2331

debug_server =
  /full/path/to/JLinkGDBServerCL
  -singlerun
  -if
  SWD
  -select
  USB
  -port
  2331
  -device
  STM32F446RE

debug_init_cmds =
  define pio_reset_halt_target
      monitor reset
      monitor halt
  end
  define pio_reset_run_target
      monitor clrbp
      monitor reset
      monitor go
  end
  target extended-remote $DEBUG_PORT
  monitor clrbp
  monitor speed auto
  pio_reset_halt_target
  $LOAD_CMDS
  $INIT_BREAK
```

### J-Link as debugger and uploader {#j-link-as-debugger-and-uploader}

Segger J-Link probe as debugger and uploader for a custom board. If you plan to use with other board, please change device `MK20DX256xxx7` to a valid identifier. See supported J-Link devices at [J-LINK](./jlink.md).

- Install [J-Link GDB Server](https://www.segger.com/products/debug-probes/j-link/tools/j-link-gdb-server/about-j-link-gdb-server/?utm_source=platformio&utm_medium=docs)

```ini
[env:jlink_debug_and_upload]
platform = teensy
framework = arduino
board = teensy31
extra_scripts = extra_script.py
upload_protocol = custom
debug_tool = jlink
debug_server =
  /full/path/to/JLinkGDBServerCL
  -singlerun
  -if
  SWD
  -select
  USB
  -port
  2331
  -device
  MK20DX256xxx7
```

**extra_script.py**

Place this file on the same level as [`platformio.ini`](../../reference/platformio-ini/index.md).

```py
from os import makedirs
from os.path import isdir, join
Import('env')

def _jlink_cmd_script(env, source):
    build_dir = env.subst("$BUILD_DIR")
    if not isdir(build_dir):
        makedirs(build_dir)
    script_path = join(build_dir, "upload.jlink")
    commands = ["h", "loadbin %s,0x0" % source, "r", "q"]
    with open(script_path, "w") as fp:
        fp.write("\n".join(commands))
    return script_path

env.Replace(
    __jlink_cmd_script=_jlink_cmd_script,
    UPLOADER="/full/path/to/JLink",
    UPLOADERFLAGS=[
        "-device", "MK20DX256xxx7",
        "-speed", "4000",
        "-if", "swd",
        "-autoconnect", "1"
    ],
    UPLOADCMD='"$UPLOADER" $UPLOADERFLAGS -CommanderScript ${__jlink_cmd_script(__env__, SOURCE)}'
)
```

### ST-Util and ST-Link {#st-util-and-st-link}

On-board ST-Link V2/V2-1 in pair with [ST-Util GDB Server](https://github.com/texane/stlink):

```ini
[env:debug]
platform = ststm32
framework = mbed
board = ...
debug_tool = custom
debug_port = :4242
debug_server = $PLATFORMIO_CORE_DIR/packages/tool-stlink/bin/st-util
debug_init_cmds =
  define pio_reset_halt_target
      monitor reset
      monitor halt
  end
  define pio_reset_run_target
      monitor reset
  end
  target extended-remote $DEBUG_PORT
  $LOAD_CMDS
  pio_reset_halt_target
  $INIT_BREAK
```

### OpenOCD and ST-Link {#openocd-and-st-link}

On-board ST-Link V2/V2-1 in pair with [OpenOCD GDB Server](http://openocd.org):

```ini
[env:debug]
platform = ststm32
framework = mbed
board = ...
debug_tool = custom
debug_server =
  $PLATFORMIO_CORE_DIR/packages/tool-openocd/bin/openocd
  -f
  $PLATFORMIO_CORE_DIR/packages/tool-openocd/scripts/board/st_nucleo_f4.cfg
```

### pyOCD and CMSIS-DAP {#pyocd-and-cmsis-dap}

Using pyOCD for CMSIS-DAP based boards

Firstly, please install [pyOCD](https://github.com/mbedmicro/pyOCD) and check that `pyocd-gdbserver --version` command works.

```ini
[env:debug]
platform = ...
board = ...
framework = mbed
debug_tool = custom
debug_server = pyocd-gdbserver
```
