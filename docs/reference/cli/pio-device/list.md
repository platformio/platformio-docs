<a id="cmd-device-list"></a>

# pio device list {#pio-device-list}

## Usage {#usage}

```bash
pio device list [OPTIONS]
```

## Description {#description}

List available devices. Default is set to `--serial` and all available [Serial Ports](http://en.wikipedia.org/wiki/Serial_port) will be shown.

## Options {#options}

### `--serial` {#cmdoption-pio-device-list-serial}

List available [Serial Ports](http://en.wikipedia.org/wiki/Serial_port), default.

### `--logical` {#cmdoption-pio-device-list-logical}

List available logical devices.

### `--mdns` {#cmdoption-pio-device-list-mdns}

List multicast DNS services.

### `--json-output` {#cmdoption-pio-device-list-json-output}

Return the output in [JSON](http://en.wikipedia.org/wiki/JSON) format.

## Examples {#examples}

1. Unix OS

```bash
> pio device list
/dev/cu.SLAB_USBtoUART
----------
Hardware ID: USB VID:PID=10c4:ea60 SNR=0001
Description: CP2102 USB to UART Bridge Controller

/dev/cu.uart-1CFF4676258F4543
----------
Hardware ID: USB VID:PID=451:f432 SNR=1CFF4676258F4543
Description: Texas Instruments MSP-FET430UIF
```

2. Windows OS

```bash
> pio device list
COM4
----------
Hardware ID: USB VID:PID=0451:F432
Description: MSP430 Application UART (COM4)

COM3
----------
Hardware ID: USB VID:PID=10C4:EA60 SNR=0001
Description: Silicon Labs CP210x USB to UART Bridge (COM3)
```

3. List multicast DNS services and logical devices

```bash
> pio device list --mdns --logical
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
