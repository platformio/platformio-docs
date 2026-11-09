---
description: "Process environments which are defined in platformio.ini file remotely."
---

<a id="cmd-remote-run"></a>

# pio remote run {#pio-remote-run}

**Remote Firmware Updates**

## Usage {#usage}

```bash
pio remote run [OPTIONS]

# process environments using specified PlatformIO Remote Agent
pio remote --agent NAME run [OPTIONS]
```

## Description {#description}

Process environments which are defined in [`platformio.ini`](../../platformio-ini/index.md) file remotely. By default, [Remote Development](../../../guides/remote-development.md) builds project on a host machine and deploy final firmware (program) to a remote device (embedded board).

If you need to process project on a remote machine, please use [`pio remote run --force-remote`](#cmdoption-pio-remote-run-r) option. In this case, [Remote Development](../../../guides/remote-development.md) will automatically synchronize your project with remote machine, install required toolchains, frameworks, SDKs, etc., and process project.

## Options {#options}

<a id="cmdoption-pio-remote-run-environment"></a>

### `-e, --environment` {#cmdoption-pio-remote-run-e}

Process specified environments.

You can also specify which environments should be processed by default using [default_envs](../../platformio-ini/platformio/default-envs.md) option from [`platformio.ini`](../../platformio-ini/index.md).

<a id="cmdoption-pio-remote-run-target"></a>

### `-t, --target` {#cmdoption-pio-remote-run-t}

Process specified targets. See [`pio run --list-targets`](../pio-run.md#cmdoption-pio-run-list-targets) documentation for available targets.

### `--upload-port` {#cmdoption-pio-remote-run-upload-port}

Custom upload port of embedded board. To print all available ports use [pio remote device](./device.md) command.

If upload port is not specified, PlatformIO will try to detect it automatically.

<a id="cmdoption-pio-remote-run-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-remote-run-d}

The project directory. Default: the current working directory.

<a id="cmdoption-pio-remote-run-silent"></a>

### `-s, --silent` {#cmdoption-pio-remote-run-s}

Print only errors.

<a id="cmdoption-pio-remote-run-verbose"></a>

### `-v, --verbose` {#cmdoption-pio-remote-run-v}

Print detailed information while processing environments.

This option can also be set globally using [force_verbose](../pio-settings.md#setting-force-verbose) setting or by environment variable [`PLATFORMIO_SETTING_FORCE_VERBOSE`](../../environment-variables.md#envvar-PLATFORMIO_SETTING_FORCE_VERBOSE).

### `--disable-auto-clean` {#cmdoption-pio-remote-run-disable-auto-clean}

Disable auto-clean of [build_dir](../../platformio-ini/platformio/build-dir.md) when [`platformio.ini`](../../platformio-ini/index.md) or [src_dir](../../platformio-ini/platformio/src-dir.md) (project structure) have been modified.

<a id="cmdoption-pio-remote-run-force-remote"></a>

### `-r, --force-remote` {#cmdoption-pio-remote-run-r}

By default, [Remote Development](../../../guides/remote-development.md) builds project on a host machine and deploy final firmware (program) to remote device (embedded board).

If you need to process project on remote machine, please use [`pio remote run --force-remote`](#cmdoption-pio-remote-run-r) option. In this case, [Remote Development](../../../guides/remote-development.md) will automatically synchronize your project with remote machine, install required toolchains, frameworks, SDKs, etc., and process project.

## Example {#example}

```bash
pio remote run --environment uno --target upload
```

```text
Building project locally
[Wed Oct 26 16:35:09 2016] Processing uno (platform: atmelavr, board: uno, framework: arduino)
--------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
Collected 25 compatible libraries
Looking for dependencies...
Project does not have dependencies
Compiling .pio/build/uno/src/main.o
Archiving .pio/build/uno/libFrameworkArduinoVariant.a
Indexing .pio/build/uno/libFrameworkArduinoVariant.a
Compiling .pio/build/uno/FrameworkArduino/CDC.o
Compiling .pio/build/uno/FrameworkArduino/HardwareSerial.o
Compiling .pio/build/uno/FrameworkArduino/HardwareSerial0.o
Compiling .pio/build/uno/FrameworkArduino/HardwareSerial1.o
Compiling .pio/build/uno/FrameworkArduino/HardwareSerial2.o
Compiling .pio/build/uno/FrameworkArduino/HardwareSerial3.o
Compiling .pio/build/uno/FrameworkArduino/IPAddress.o
Compiling .pio/build/uno/FrameworkArduino/PluggableUSB.o
Compiling .pio/build/uno/FrameworkArduino/Print.o
Compiling .pio/build/uno/FrameworkArduino/Stream.o
Compiling .pio/build/uno/FrameworkArduino/Tone.o
Compiling .pio/build/uno/FrameworkArduino/USBCore.o
Compiling .pio/build/uno/FrameworkArduino/WInterrupts.o
Compiling .pio/build/uno/FrameworkArduino/WMath.o
Compiling .pio/build/uno/FrameworkArduino/WString.o
Compiling .pio/build/uno/FrameworkArduino/_wiring_pulse.o
Compiling .pio/build/uno/FrameworkArduino/abi.o
Compiling .pio/build/uno/FrameworkArduino/hooks.o
Compiling .pio/build/uno/FrameworkArduino/main.o
Compiling .pio/build/uno/FrameworkArduino/new.o
Compiling .pio/build/uno/FrameworkArduino/wiring.o
Compiling .pio/build/uno/FrameworkArduino/wiring_analog.o
Compiling .pio/build/uno/FrameworkArduino/wiring_digital.o
Compiling .pio/build/uno/FrameworkArduino/wiring_pulse.o
Compiling .pio/build/uno/FrameworkArduino/wiring_shift.o
Archiving .pio/build/uno/libFrameworkArduino.a
Indexing .pio/build/uno/libFrameworkArduino.a
Linking .pio/build/uno/firmware.elf
Checking program size
Building .pio/build/uno/firmware.hex
text       data     bss     dec     hex filename
2574         48     168    2790     ae6 .pio/build/uno/firmware.elf
========================= [SUCCESS] Took 10.01 seconds =======================
================================== [SUMMARY] =================================
Environment nodemcuv2   [SKIP]
Environment uno_pic32   [SKIP]
Environment teensy31    [SKIP]
Environment uno         [SUCCESS]
========================= [SUCCESS] Took 10.01 seconds ========================
Uploading firmware remotely
[Wed Oct 26 19:35:20 2016] Processing uno (platform: atmelavr, board: uno, framework: arduino)
----------------------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
Looking for upload port...
Auto-detected: /dev/cu.usbmodemFA1431
Uploading .pio/build/uno/firmware.hex
avrdude: AVR device initialized and ready to accept instructions
Reading | ################################################## | 100% 0.00s
avrdude: Device signature = 0x1e950f
avrdude: reading input file ".pio/build/uno/firmware.hex"
avrdude: writing flash (2622 bytes):
Writing | ################################################## | 100% 0.43s
avrdude: 2622 bytes of flash written
avrdude: verifying flash memory against .pio/build/uno/firmware.hex:
avrdude: load data flash data from input file .pio/build/uno/firmware.hex:
avrdude: input file .pio/build/uno/firmware.hex contains 2622 bytes
avrdude: reading on-chip flash data:
Reading | ################################################## | 100% 0.34s
avrdude: verifying ...
avrdude: 2622 bytes of flash verified
avrdude done.  Thank you.
========================= [SUCCESS] Took 3.04 seconds =======================
========================= [SUMMARY] =========================================
Environment nodemcuv2   [SKIP]
Environment uno_pic32   [SKIP]
Environment teensy31    [SKIP]
Environment uno         [SUCCESS]
========================= [SUCCESS] Took 3.04 seconds ========================
```
