---
description: Open a serial monitor to a board or a network serial port, with filters for decoding and logging.
---

<a id="cmd-device-monitor"></a>

# pio device monitor {#pio-device-monitor}

Open a serial monitor: show what the device sends and send what you type.

## Usage {#usage}

```bash
pio device monitor [OPTIONS]
```

## Description {#description}

The monitor is based on pySerial's
[Miniterm](https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm).
Terminal features such as colors and cursor control come from the terminal
you run it in.

Run it in a project directory to use the project's
[monitor options](../../platformio-ini/env/monitor-options.md) from
`platformio.ini`. Command-line options take precedence.

Besides local serial ports, the monitor can open
[RFC 2217](https://tools.ietf.org/html/rfc2217) network serial ports and raw
TCP sockets: pass `rfc2217://<host>:<port>` or `socket://<host>:<port>` as the
port. See pySerial's [URL handlers](https://pyserial.readthedocs.io/en/latest/url_handlers.html).

| Key | Action |
| --- | --- |
| <kbd>Ctrl</kbd>+<kbd>C</kbd> | Quit (change with [`--exit-char`](#cmdoption-pio-device-monitor-exit-char)) |
| <kbd>Ctrl</kbd>+<kbd>T</kbd> | Menu (change with [`--menu-char`](#cmdoption-pio-device-monitor-menu-char)) |
| <kbd>Ctrl</kbd>+<kbd>T</kbd>, then <kbd>Ctrl</kbd>+<kbd>H</kbd> | Help: all menu keys, such as toggling RTS/DTR or changing the baud rate |

If the connection drops, for example while the board resets, the monitor
reconnects automatically.

## Options {#options}

<a id="cmdoption-pio-device-monitor-port"></a>

### `-p, --port` {#cmdoption-pio-device-monitor-p}

The serial port: a device name such as `/dev/ttyUSB0` or `COM3`, a URL, or a
pattern. The values are the same as for [`monitor_port`](../../platformio-ini/env/monitor-port.md).
If you omit it, PlatformIO detects the port.

<a id="cmdoption-pio-device-monitor-baud"></a>

### `-b, --baud` {#cmdoption-pio-device-monitor-b}

The baud rate. Default: `9600`.

In [`platformio.ini`](../../platformio-ini/index.md): [`monitor_speed`](../../platformio-ini/env/monitor-speed.md).

### `--parity` {#cmdoption-pio-device-monitor-parity}

The parity: `N` (none), `E` (even), `O` (odd), `S` (space) or `M` (mark).
Default: `N`.

In [`platformio.ini`](../../platformio-ini/index.md): [`monitor_parity`](../../platformio-ini/env/monitor-parity.md).

### `--rtscts` {#cmdoption-pio-device-monitor-rtscts}

Enable RTS/CTS hardware flow control.

### `--xonxoff` {#cmdoption-pio-device-monitor-xonxoff}

Enable XON/XOFF software flow control.

### `--rts` {#cmdoption-pio-device-monitor-rts}

The initial state of the RTS line: `0` or `1`.

In [`platformio.ini`](../../platformio-ini/index.md): [`monitor_rts`](../../platformio-ini/env/monitor-rts.md).

### `--dtr` {#cmdoption-pio-device-monitor-dtr}

The initial state of the DTR line: `0` or `1`.

In [`platformio.ini`](../../platformio-ini/index.md): [`monitor_dtr`](../../platformio-ini/env/monitor-dtr.md).

### `--echo` {#cmdoption-pio-device-monitor-echo}

Show what you type (local echo).

In [`platformio.ini`](../../platformio-ini/index.md): [`monitor_echo`](../../platformio-ini/env/monitor-echo.md).

### `--encoding` {#cmdoption-pio-device-monitor-encoding}

The encoding of the serial data, for example `UTF-8`, `Latin-1` or
`hexlify`. See the [supported encodings](https://docs.python.org/3/library/codecs.html#standard-encodings).
Default: `UTF-8`.

In [`platformio.ini`](../../platformio-ini/index.md): [`monitor_encoding`](../../platformio-ini/env/monitor-encoding.md).

<a id="cmdoption-pio-device-monitor-filter"></a>

### `-f, --filter` {#cmdoption-pio-device-monitor-f}

Apply a [filter](#cmd-device-monitor-filters) to the data. Repeat the
option to apply several filters.

In [`platformio.ini`](../../platformio-ini/index.md): [`monitor_filters`](../../platformio-ini/env/monitor-filters.md).

### `--eol` {#cmdoption-pio-device-monitor-eol}

The line ending sent when you press <kbd>Enter</kbd>: `CR`, `LF` or `CRLF`.
Default: `CRLF`.

In [`platformio.ini`](../../platformio-ini/index.md): [`monitor_eol`](../../platformio-ini/env/monitor-eol.md).

### `--raw` {#cmdoption-pio-device-monitor-raw}

Show the data as received, without encodings or filters.

In [`platformio.ini`](../../platformio-ini/index.md): [`monitor_raw`](../../platformio-ini/env/monitor-raw.md).

### `--exit-char` {#cmdoption-pio-device-monitor-exit-char}

The ASCII code of the key that quits the monitor. Default: `3`
(<kbd>Ctrl</kbd>+<kbd>C</kbd>). For example, `--exit-char 29` makes
<kbd>Ctrl</kbd>+<kbd>]</kbd> quit.

### `--menu-char` {#cmdoption-pio-device-monitor-menu-char}

The ASCII code of the key that opens the menu. Default: `20`
(<kbd>Ctrl</kbd>+<kbd>T</kbd>). It must differ from `--exit-char`.

### `--quiet` {#cmdoption-pio-device-monitor-quiet}

Show only error messages from the monitor itself.

### `--no-reconnect` {#cmdoption-pio-device-monitor-no-reconnect}

Do not reconnect automatically when the connection fails.

<a id="cmdoption-pio-device-monitor-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-device-monitor-d}

The project directory. Default: the current working directory.

<a id="cmdoption-pio-device-monitor-environment"></a>

### `-e, --environment` {#cmdoption-pio-device-monitor-e}

The [project environment](../../platformio-ini/env/index.md) whose monitor
options to use. Default: the first of
[`default_envs`](../../platformio-ini/platformio/default-envs.md), or the first
environment in `platformio.ini`.

<a id="cmd-device-monitor-filters"></a>

## Filters {#filters}

Filters transform the data shown or sent by the monitor. Apply them with
[`--filter`](#cmdoption-pio-device-monitor-f) or the
[`monitor_filters`](../../platformio-ini/env/monitor-filters.md) option.

### Built-in filters {#built-in-filters}

| Name | Description |
| --- | --- |
| `default` | Remove typical terminal control codes from the input |
| `direct` | Pass all data unchanged. Use it when the data already contains ANSI escape codes, such as colors. |
| `nocontrol` | Remove all control codes, including CR and LF |
| `printable` | Show the decimal code of non-ASCII characters and replace most control codes |
| `debug` | Print what is sent and received |
| `hexlify` | Show the hexadecimal code of each character |
| `time` | Add a timestamp, with milliseconds, to each line |
| `send_on_enter` | Send what you type only when you press <kbd>Enter</kbd> |
| `log2file` | Also write the output to `logs/device-monitor-<date>-<time>.log` in the project directory |

Development platforms can add filters. For example,
[Espressif 32](/hardware/platforms/espressif32) and
[Espressif 8266](/hardware/platforms/espressif8266) provide
`esp32_exception_decoder` and `esp8266_exception_decoder`, which turn crash
backtraces into source file names and line numbers.

### Community filters {#community-filters}

These filters are maintained by the community and installed separately. See
each filter's documentation.

| Name | Description |
| --- | --- |
| [arduplot](https://github.com/yhur/arduplot) | A serial plotter compatible with the Arduino syntax |

<a id="cmd-device-monitor-custom-filters"></a>

### Custom filters {#custom-filters}

A custom filter is a Python file whose name starts with `filter_`. It defines
a class derived from `DeviceMonitorFilterBase`, with a unique `NAME` and the
`rx()` (received data) and `tx()` (sent data) methods. Each method returns the
transformed text.

PlatformIO loads custom filters from:

- the project's [`monitor_dir`](../../platformio-ini/platformio/monitor-dir.md);
- `monitor/` in the folder of the project's development platform
  ([`platforms_dir`](../../platformio-ini/platformio/platforms-dir.md)`/<platform>/monitor`);
- `monitor/` in the folder of each installed package
  ([`packages_dir`](../../platformio-ini/platformio/packages-dir.md)`/<package>/monitor`).

`filter_demo.py`:

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

More examples:

- [Built-in filters](https://github.com/platformio/platformio-core/tree/develop/platformio/device/monitor/filters)
- [Espressif 32 filters](https://github.com/platformio/platform-espressif32/tree/develop/monitor)
- [Espressif 8266 filters](https://github.com/platformio/platform-espressif8266/tree/develop/monitor)

### Save the output to a file {#capture-output-to-a-file}

Apply the `log2file` filter. The log file is created in the `logs` folder of
the project directory:

```bash
pio device monitor -f default -f log2file
```

Or in `platformio.ini`:

```ini
[env:log_output_to_file]
...
platform = ...
monitor_filters = default, log2file
```

## Examples {#examples}

Open the monitor; when there is more than one serial port, choose one:

```bash
pio device monitor
```

```text
--- Available ports:
--- /dev/cu.Bluetooth-Incoming-Port n/a
--- /dev/cu.SLAB_USBtoUART CP2102 USB to UART Bridge Controller
Enter port name:/dev/cu.SLAB_USBtoUART
--- Miniterm on /dev/cu.SLAB_USBtoUART: 9600,8,N,1 ---
--- Quit: Ctrl+C  |  Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---
Hello PlatformIO!
```

Open the monitor at 115200 baud with timestamps:

```bash
pio device monitor -b 115200 -f time
```
