---
description: List serial ports, logical drives and multicast DNS services visible to PlatformIO.
---

<a id="cmd-device-list"></a>

# pio device list {#pio-device-list}

List the devices PlatformIO can see: serial ports (the default), logical
drives and multicast DNS services. Use it to find the port for
[`upload_port`](../../platformio-ini/env/upload-port.md) or
[`monitor_port`](../../platformio-ini/env/monitor-port.md), and the USB
vendor and product IDs of a board.

## Usage {#usage}

```bash
pio device list [OPTIONS]
```

## Options {#options}

Without options, the command lists serial ports. Combine options to list
several kinds of devices.

### `--serial` {#cmdoption-pio-device-list-serial}

List [serial ports](https://en.wikipedia.org/wiki/Serial_port).

### `--logical` {#cmdoption-pio-device-list-logical}

List logical devices (mounted drives).

### `--mdns` {#cmdoption-pio-device-list-mdns}

List multicast DNS (mDNS) services on the local network.

### `--json-output` {#cmdoption-pio-device-list-json-output}

Print the result in [JSON](https://en.wikipedia.org/wiki/JSON) format.

## Examples {#examples}

List serial ports on macOS or Linux:

```bash
pio device list
```

```text
/dev/cu.SLAB_USBtoUART
----------
Hardware ID: USB VID:PID=10c4:ea60 SNR=0001
Description: CP2102 USB to UART Bridge Controller

/dev/cu.uart-1CFF4676258F4543
----------
Hardware ID: USB VID:PID=451:f432 SNR=1CFF4676258F4543
Description: Texas Instruments MSP-FET430UIF
```

List serial ports on Windows:

```bash
pio device list
```

```text
COM4
----------
Hardware ID: USB VID:PID=0451:F432
Description: MSP430 Application UART (COM4)

COM3
----------
Hardware ID: USB VID:PID=10C4:EA60 SNR=0001
Description: Silicon Labs CP210x USB to UART Bridge (COM3)
```

List multicast DNS services and logical devices:

```bash
pio device list --mdns --logical
```

```text
Multicast DNS Services
======================

PlatformIO._bttremote._tcp.local.
------------------------------
Type: _bttremote._tcp.local.
IP: ...
Port: 62941
Properties: ...

Time for PlatformIO._adisk._tcp.local.
---------------------------------
Type: _adisk._tcp.local.
IP: 192.168.0.1
Port: 9
Properties: ...

PlatformIO._ssh._tcp.local.
------------------------
Type: _ssh._tcp.local.
IP: ...
Port: 22

PlatformIO._sftp-ssh._tcp.local.
-----------------------------
Type: _sftp-ssh._tcp.local.
IP: ...
Port: 22


Logical Devices
===============
/
-
Name:

/Volumes/PIO
-------------
Name: PIO

/Volumes/PLUS
--------------
Name: PLUS
```
