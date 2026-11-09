---
description: "List Serial Ports on remote machines where PlatformIO Remote Agent is started."
---

<a id="cmd-remote-device"></a>

# pio remote device {#pio-remote-device}

**Remote Device: monitor remote device or list existing.**

<a id="cmd-remote-device-list"></a>

## pio remote device list {#pio-remote-device-list}

### Usage {#usage}

```bash
pio remote device list [OPTIONS]

# List devices from the specified agents. Multiple agents are allowed.
pio remote --agent NAME device list [OPTIONS]
```

### Description {#description}

List [Serial Ports](http://en.wikipedia.org/wiki/Serial_port) on remote machines where [PlatformIO Remote Agent](./agent.md) is started.

You can list devices from the specified remote machines using `--agent NAME` option between "remote" & "device" sub-commands. For example, you have run [`pio remote agent start --name`](./agent.md#cmdoption-pio-remote-agent-start-n) command with "home" and "office" options:

- `pio remote agent start --name home`
- `pio remote agent start --name office`

Now, to list devices from office machine please use `pio remote --agent office device list`.

Multiple agents are allowed ( `pio remote --agent lab1 --agent lab3 device ...`).

### Options {#options}

#### `--json-output` {#cmdoption-pio-remote-device-list-json-output}

Print the result in [JSON](https://en.wikipedia.org/wiki/JSON) format.

### Example {#example}

```bash
pio remote device list
```

```text
Agent innomac.local
===================
/dev/cu.Bluetooth-Incoming-Port
-------------------------------
Hardware ID: n/a
Description: n/a
/dev/cu.obd2ecu-SPPDev
----------------------
Hardware ID: n/a
Description: n/a
/dev/cu.usbmodemFA1431
----------------------
Hardware ID: USB VID:PID=2A03:0043 SER=75435353038351015271 LOCATION=250-1.4.3
Description: Arduino Uno
/dev/cu.usbserial-A6004003
--------------------------
Hardware ID: USB VID:PID=0403:6001 SER=A6004003 LOCATION=253-1.3.1
Description: FT232R USB UART - FT232R USB UART
/dev/cu.SLAB_USBtoUART
----------------------
Hardware ID: USB VID:PID=10C4:EA60 SER=0001 LOCATION=253-1.3.2
Description: CP2102 USB to UART Bridge Controller - CP2102 USB to UART Bridge Controller
/dev/cu.usbmodem589561
----------------------
Hardware ID: USB VID:PID=16C0:0483 SER=589560 LOCATION=250-1.4.1
Description: USB Serial
```

<a id="cmd-remote-device-monitor"></a>

## pio remote device monitor {#pio-remote-device-monitor}

**Remote Serial Port Monitor**

### Usage

```bash
pio remote device monitor [OPTIONS]

# Connect to a specified agent
pio remote --agent NAME device monitor [OPTIONS]
pio remote -a NAME device monitor [OPTIONS]
```

### Description

Connect to Serial Port of remote device and receive or send data in real time. [PlatformIO Remote Agent](./agent.md) should be started before on a remote machine.

To control *monitor* please use these "hot keys":

- `Ctrl+C` Quit
- `Ctrl+T` Menu
- `Ctrl+T followed by Ctrl+H` Help

### Options

<a id="cmdoption-pio-remote-device-monitor-port"></a>

#### `-p, --port` {#cmdoption-pio-remote-device-monitor-p}

Port, a number or a device name

<a id="cmdoption-pio-remote-device-monitor-baud"></a>

#### `-b, --baud` {#cmdoption-pio-remote-device-monitor-b}

Set baud rate, default `9600`

#### `--parity` {#cmdoption-pio-remote-device-monitor-parity}

Set parity (*None, Even, Odd, Space, Mark*), one of \[`N`, `E`, `O`, `S`, `M`\], default `N`

#### `--rtscts` {#cmdoption-pio-remote-device-monitor-rtscts}

Enable `RTS/CTS` flow control, default `Off`

#### `--xonxoff` {#cmdoption-pio-remote-device-monitor-xonxoff}

Enable software flow control, default `Off`

#### `--rts` {#cmdoption-pio-remote-device-monitor-rts}

Set initial `RTS` line state, default `0`

#### `--dtr` {#cmdoption-pio-remote-device-monitor-dtr}

Set initial `DTR` line state, default `0`

#### `--echo` {#cmdoption-pio-remote-device-monitor-echo}

Enable local echo, default `Off`

#### `--encoding` {#cmdoption-pio-remote-device-monitor-encoding}

Set the encoding for the serial port (e.g. `hexlify`, `Latin1`, `UTF-8`), default `UTF-8`.

<a id="cmdoption-pio-remote-device-monitor-filter"></a>

#### `-f, --filter` {#cmdoption-pio-remote-device-monitor-f}

Add text transformation. Available filters:

- `colorize` Apply different colors for received and echo
- `debug` Print what is sent and received
- `default` Remove typical terminal control codes from input
- `direct` Do-nothing: forward all data unchanged
- `nocontrol` Remove all control codes, incl. CR+LF
- `printable` Show decimal code for all non-ASCII characters and replace most control codes

#### `--eol` {#cmdoption-pio-remote-device-monitor-eol}

End of line mode (`CR`, `LF` or `CRLF`), default `CRLF`

#### `--raw` {#cmdoption-pio-remote-device-monitor-raw}

Do not apply any encodings/transformations

#### `--exit-char` {#cmdoption-pio-remote-device-monitor-exit-char}

ASCII code of special character that is used to exit the application, default `3` (DEC, `Ctrl+C`).

For example, to use `Ctrl+]` run `pio remote device monitor --exit-char 29`.

#### `--menu-char` {#cmdoption-pio-remote-device-monitor-menu-char}

ASCII code of special character that is used to control miniterm (menu), default `20` (DEC)

#### `--quiet` {#cmdoption-pio-remote-device-monitor-quiet}

Diagnostics: suppress non-error messages, default `Off`

<a id="cmdoption-pio-remote-device-monitor-project-dir"></a>

#### `-d, --project-dir` {#cmdoption-pio-remote-device-monitor-d}

The project directory. Default: the current working directory.

<a id="cmdoption-pio-remote-device-monitor-environment"></a>

#### `-e, --environment` {#cmdoption-pio-remote-device-monitor-e}

Process specified environments.

You can also specify which environments should be processed by default using [default_envs](../../platformio-ini/platformio/default-envs.md) option from [`platformio.ini`](../../platformio-ini/index.md).

### Examples {#examples}

Open a serial monitor to a device on a remote agent; when there is more than
one port, choose one:

```bash
pio remote device monitor
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

For the monitor keys, see [`pio device monitor`](../pio-device/monitor.md#description).
