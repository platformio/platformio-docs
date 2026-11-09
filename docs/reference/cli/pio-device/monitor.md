<a id="cmd-device-monitor"></a>

# pio device monitor {#pio-device-monitor}

## Usage {#usage}

```bash
pio device monitor [OPTIONS]
```

## Description {#description}

This is a console application that provides a small terminal application. It is based on [Miniterm](https://pythonhosted.org/pyserial/examples.html#miniterm) and itself does not implement any terminal features such as *VT102* compatibility. However it inherits these features from the terminal it is run. For example on GNU/Linux running from an *xterm* it will support the escape sequences of the *xterm*. On *Windows* the typical console window is dumb and does not support any escapes. When *ANSI.sys* is loaded it supports some escapes.

Miniterm supports [RFC 2217](https://tools.ietf.org/html/rfc2217.html) remote serial ports and raw sockets using [URL Handlers](https://pyserial.readthedocs.io/en/latest/url_handlers.html#urls) such as `rfc2217://<host>:<port>` respectively `socket://<host>:<port>` as port argument when invoking.

To control *monitor* please use these "hot keys":

- `Ctrl+C` Quit
- `Ctrl+T` Menu
- `Ctrl+T followed by Ctrl+H` Help

## Options {#options}

<a id="cmdoption-pio-device-monitor-port"></a>

### `-p, --port` {#cmdoption-pio-device-monitor-p}

The possible values are the same as documented for [monitor_port](../../platformio-ini/env/monitor-port.md) option.

<a id="cmdoption-pio-device-monitor-baud"></a>

### `-b, --baud` {#cmdoption-pio-device-monitor-b}

Set baud rate, default `9600`.

Can be customized in ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md) using [monitor_speed](../../platformio-ini/env/monitor-speed.md) option.

### `--parity` {#cmdoption-pio-device-monitor-parity}

Set parity (*None, Even, Odd, Space, Mark*), one of \[`N`, `E`, `O`, `S`, `M`\], default is `N`.

Can be customized in ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md) using [monitor_parity](../../platformio-ini/env/monitor-parity.md) option.

### `--rtscts` {#cmdoption-pio-device-monitor-rtscts}

Enable `RTS/CTS` flow control.

### `--xonxoff` {#cmdoption-pio-device-monitor-xonxoff}

Enable software flow control.

### `--rts` {#cmdoption-pio-device-monitor-rts}

Set initial `RTS` line state (`0` or `1`).

Can be customized in ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md) using [monitor_rts](../../platformio-ini/env/monitor-rts.md) option.

### `--dtr` {#cmdoption-pio-device-monitor-dtr}

Set initial `DTR` line state (`0` or `1`).

Can be customized in ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md) using [monitor_dtr](../../platformio-ini/env/monitor-dtr.md) option.

### `--echo` {#cmdoption-pio-device-monitor-echo}

Enable local echo.

Can be customized in ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md) using [monitor_echo](../../platformio-ini/env/monitor-echo.md) option.

### `--encoding` {#cmdoption-pio-device-monitor-encoding}

Set the encoding for the serial port (e.g. `hexlify`, `Latin-1`, `UTF-8`), default `UTF-8`. See the full list of [supported encodings](https://docs.python.org/3/library/codecs.html#standard-encodings).

Can be customized in ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md) using [monitor_encoding](../../platformio-ini/env/monitor-encoding.md) option.

<a id="cmdoption-pio-device-monitor-filter"></a>

### `-f, --filter` {#cmdoption-pio-device-monitor-f}

Add text transformation. See available filters at [Filters](#cmd-device-monitor-filters).

### `--eol` {#cmdoption-pio-device-monitor-eol}

End of line mode (`CR`, `LF` or `CRLF`), default `CRLF`.

Can be customized in ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md) using [monitor_eol](../../platformio-ini/env/monitor-eol.md) option.

### `--raw` {#cmdoption-pio-device-monitor-raw}

Do not apply any encodings/transformations.

Can be customized in ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md) using [monitor_raw](../../platformio-ini/env/monitor-raw.md) option.

### `--exit-char` {#cmdoption-pio-device-monitor-exit-char}

ASCII code of special character that is used to exit the application, default `3` (DEC, `Ctrl+C`).

For example, to use `Ctrl+]` run `pio device monitor --exit-char 29`.

### `--menu-char` {#cmdoption-pio-device-monitor-menu-char}

ASCII code of special character that is used to control miniterm (menu), default `20` (DEC)

### `---quiet` {#cmdoption-pio-device-monitor-quiet}

Diagnostics: suppress non-error messages, default `Off`.

### `--no-reconnect` {#cmdoption-pio-device-monitor-no-reconnect}

Disable automatic reconnection if the established connection fails.

<a id="cmdoption-pio-device-monitor-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-device-monitor-d}

Specify the path to project directory. By default, `--project-dir` is equal to current working directory (`CWD`).

<a id="cmdoption-pio-device-monitor-environment"></a>

### `-e, --environment` {#cmdoption-pio-device-monitor-e}

Process specified environments.

You can also specify which environments should be processed by default using [default_envs](../../platformio-ini/platformio/default-envs.md) option from ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md).

<a id="cmd-device-monitor-filters"></a>

## Filters {#filters}

PlatformIO allows you to apply multiple filters to the device monitor INPUT & OUTPUT streams using the [`pio device monitor --filter`](#cmdoption-pio-device-monitor-f) command or [monitor_filters](../../platformio-ini/env/monitor-filters.md) option.

### Built-in Filters {#built-in-filters}

| Name | Description |
|---|---|
| `direct` | Do-nothing: forward all data unchanged. Useful if data already contains ANSI escape codes (colors) |
| `default` | Remove typical terminal control codes from input |
| `debug` | Print what is sent and received |
| `hexlify` | Show a hexadecimal representation of the data (code point of each character) |
| `log2file` | Log data to a file "platformio-device-monitor-%date%.log" located in the current working directory |
| `nocontrol` | Remove all control codes, incl. CR+LF |
| `printable` | Show decimal code for all non-ASCII characters and replace most control codes |
| `time` | Add timestamp with milliseconds for each new line |
| `send_on_enter` | Send a text to device on ENTER |
| `esp32_exception_decoder` | Custom filter for [Espressif 32](/hardware/platforms/espressif32) which decodes crash exception |
| `esp8266_exception_decoder` | Custom filter for [Espressif 8266](/hardware/platforms/espressif8266) which decodes crash exception |

### Community Filters {#community-filters}

The Community Filters are not a part of PlatformIO Core installation. You need to install them manually. Please visit an official filter's documentation on how to use it.

| Name | Description |
|---|---|
| [arduplot](https://github.com/yhur/arduplot) | **Serial Plotter** compatible with Arduino syntax (output) |

<a id="cmd-device-monitor-custom-filters"></a>

### Custom Filters {#custom-filters}

[PlatformIO Core (CLI)](../../../get-started/platformio-core.md) provides an API to extend device monitor with custom filters. Each filter is a Python-based file and its name should have the `filter_` prefix. In a Python code, you need to extend `DeviceMonitorFilterBase` class to get access to the `rx()` and `tx()` methods/callbacks.

[PlatformIO Core (CLI)](../../../get-started/platformio-core.md) looks for the custom filters in the next locations:

- Project [monitor_dir](../../platformio-ini/platformio/monitor-dir.md)
- [platforms_dir](../../platformio-ini/platformio/platforms-dir.md)/\<platform>/monitor
- [packages_dir](../../platformio-ini/platformio/packages-dir.md)/\<package>/monitor

See the base API below:

**filter_demo.py**

```python
from platformio.public import DeviceMonitorFilterBase


class Demo(DeviceMonitorFilterBase):
    NAME = "demo"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Demo filter is loaded")

    def rx(self, text):
        return f"Received: {text}\n"

    def tx(self, text):
        print(f"Sent: {text}\n")
        return text
```

**Examples**

- [https://github.com/platformio/platformio-core/tree/develop/platformio/device/monitor/filters](https://github.com/platformio/platformio-core/tree/develop/platformio/device/monitor/filters)
- [https://github.com/platformio/platform-espressif32/tree/develop/monitor](https://github.com/platformio/platform-espressif32/tree/develop/monitor)
- [https://github.com/platformio/platform-espressif8266/tree/develop/monitor](https://github.com/platformio/platform-espressif8266/tree/develop/monitor)

### Capture output to a file {#capture-output-to-a-file}

To capture the output of the device monitor in a file, you can use the `log2file` filter from [Filters](#cmd-device-monitor-filters). By default, the log file will be saved in the `logs` folder located in the project root directory.

```bash
> pio device monitor -f default -f log2file
```

Or using ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md) and [monitor_filters](../../platformio-ini/env/monitor-filters.md)

```ini
[env:log_output_to_file]
...
platform = ...
monitor_filters = default, log2file
```

## Examples {#examples}

1. Show available options for *monitor*

```bash
> pio device monitor --help
Usage: pio device monitor [OPTIONS]

Options:
  -p, --port TEXT       Port, a number or a device name
  -b, --baud INTEGER    Set baud rate, default=9600
  --parity [N|E|O|S|M]  Set parity, default=N
  --rtscts              Enable RTS/CTS flow control, default=Off
  --xonxoff             Enable software flow control, default=Off
  --rts [0|1]           Set initial RTS line state, default=0
  --dtr [0|1]           Set initial DTR line state, default=0
  --echo                Enable local echo, default=Off
  --encoding TEXT       Set the encoding for the serial port (e.g. hexlify,
                        Latin1, UTF-8), default: UTF-8
  -f, --filter TEXT     Add filters / text transformation
  --eol [CR|LF|CRLF]    End of line mode, default=CRLF
  --raw                 Do not apply any encodings/transformations
  --exit-char INTEGER   ASCII code of special character that is used to exit
                        the application, default=29 (DEC)
  --menu-char INTEGER   ASCII code of special character that is used to
                        control miniterm (menu), default=20 (DEC)
  --quiet               Diagnostics: suppress non-error messages, default=Off
  -h, --help            Show this message and exit.
```

2. Communicate with serial device and print help inside terminal

```bash
> pio device monitor

--- Available ports:
--- /dev/cu.Bluetooth-Incoming-Port n/a
--- /dev/cu.Bluetooth-Modem n/a
--- /dev/cu.SLAB_USBtoUART CP2102 USB to UART Bridge Controller
--- /dev/cu.obd2ecu-SPPDev n/a
Enter port name:/dev/cu.SLAB_USBtoUART
--- Miniterm on /dev/cu.SLAB_USBtoUART: 9600,8,N,1 ---
--- Quit: Ctrl+C  |  Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---
Hello PlatformIO!
---
--- Ctrl+]   Exit program
--- Ctrl+T   Menu escape key, followed by:
--- Menu keys:
---    Ctrl+T  Send the menu character itself to remote
---    Ctrl+]  Send the exit character itself to remote
---    Ctrl+I  Show info
---    Ctrl+U  Upload file (prompt will be shown)
--- Toggles:
---    Ctrl+R  RTS          Ctrl+E  local echo
---    Ctrl+D  DTR          Ctrl+B  BREAK
---    Ctrl+L  line feed    Ctrl+A  Cycle repr mode
---
--- Port settings (Ctrl+T followed by the following):
---    p          change port
---    7 8        set data bits
---    n e o s m  change parity (None, Even, Odd, Space, Mark)
---    1 2 3      set stop bits (1, 2, 1.5)
---    b          change baud rate
---    x X        disable/enable software flow control
---    r R        disable/enable hardware flow control
--- exit ---
```
