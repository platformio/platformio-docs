---
description: "Run project targets over environments declared in platformio.ini."
---

<a id="cmd-run"></a>

# pio run {#pio-run}

## Usage {#usage}

```bash
pio run [OPTIONS]
```

## Description {#description}

Run project targets over environments declared in [`platformio.ini`](../platformio-ini/index.md).

## Options {#options}

<a id="cmdoption-pio-run-environment"></a>

### `-e, --environment` {#cmdoption-pio-run-e}

Process specified environments. Repeat the option for several environments.

You can also specify which environments should be processed by default using [default_envs](../platformio-ini/platformio/default-envs.md) option from [`platformio.ini`](../platformio-ini/index.md).

<a id="cmdoption-pio-run-target"></a>

### `-t, --target` {#cmdoption-pio-run-t}

Process specified targets. Multiple targets are allowed.

You can configure default targets per project environment using [targets](../platformio-ini/env/targets.md) option in [`platformio.ini`](../platformio-ini/index.md).

### `--list-targets` {#cmdoption-pio-run-list-targets}

List available project targets. It's also possible to list targets per project environment using [`pio run --environment`](#cmdoption-pio-run-e) option.

There are also built-in system targets:

- Device

  - `monitor` automatically start [pio device monitor](./pio-device/monitor.md) after successful build operation. You can configure monitor using [Monitor options](../platformio-ini/env/monitor-options.md).

- System

  - `envdump` dump current build environment

<a id="cmdoption-pio-run-port"></a>

### `-p, --port` {#cmdoption-pio-run-p}

Set both [`pio run --upload-port`](#cmdoption-pio-run-upload-port) and [`pio run --monitor-port`](#cmdoption-pio-run-monitor-port) options simultaneously. This option is a convenient way to specify the same port for both uploading firmware and monitoring device output, streamlining the workflow for users who want to use the same port for both operations.

### `--upload-port` {#cmdoption-pio-run-upload-port}

Custom upload port of embedded board. To print all available ports use [pio device list](./pio-device/list.md) command.

If upload port is not specified, PlatformIO will try to detect it automatically.

### `--monitor-port` {#cmdoption-pio-run-monitor-port}

Specify a custom port to be passed to the [`pio device monitor --port`](./pio-device/monitor.md#cmdoption-pio-device-monitor-p) command. To list all available ports, use the [pio device list](./pio-device/list.md) command.

If the monitor port is not specified, PlatformIO will attempt to detect it automatically.

<a id="cmdoption-pio-run-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-run-d}

The project directory. Default: the current working directory.

<a id="cmdoption-pio-run-project-conf"></a>

### `-c, --project-conf` {#cmdoption-pio-run-c}

Process project with a custom [`platformio.ini`](../platformio-ini/index.md).

<a id="cmdoption-pio-run-jobs"></a>

### `-j, --jobs` {#cmdoption-pio-run-j}

Control the number of parallel build jobs. The default is the number of CPUs in the system.

This option can also be set globally using the environment variable [`PLATFORMIO_RUN_JOBS`](../environment-variables.md#envvar-PLATFORMIO_RUN_JOBS).

### `--disable-auto-clean` {#cmdoption-pio-run-disable-auto-clean}

Disable auto-clean of [build_dir](../platformio-ini/platformio/build-dir.md) when [`platformio.ini`](../platformio-ini/index.md) or [src_dir](../platformio-ini/platformio/src-dir.md) (project structure) have been modified.

<a id="cmdoption-pio-run-program-arg"></a>

### `-a, --program-arg` {#cmdoption-pio-run-a}

Pass an extra argument to the [Native](/hardware/platforms/native) program. Multiple arguments are allowed.

**Example**

```bash
> pio run -t exec --program-arg "arg1" --program-arg="--option1=value1"
# or short format
> pio run -t exec -a "arg1" -a "--option1=value1"
```

<a id="cmdoption-pio-run-silent"></a>

### `-s, --silent` {#cmdoption-pio-run-s}

Suppress progress reporting

<a id="cmdoption-pio-run-verbose"></a>

### `-v, --verbose` {#cmdoption-pio-run-v}

Print detailed information while processing environments.

This option can also be set globally using [force_verbose](./pio-settings.md#setting-force-verbose) setting or by environment variable [`PLATFORMIO_SETTING_FORCE_VERBOSE`](../environment-variables.md#envvar-PLATFORMIO_SETTING_FORCE_VERBOSE).

## Examples {#examples}

Process [Wiring Blink Example](https://github.com/platformio/platformio-examples/tree/develop/wiring-blink):

```bash
pio run
```

```text
[Wed Sep  7 15:48:58 2016] Processing uno (platform: atmelavr, board: uno, framework: arduino)
-----------------------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
Collected 36 compatible libraries
Looking for dependencies...
Project does not have dependencies
Compiling .pio/build/uno/src/main.o
Archiving .pio/build/uno/libFrameworkArduinoVariant.a
Indexing .pio/build/uno/libFrameworkArduinoVariant.a
Compiling .pio/build/uno/FrameworkArduino/CDC.o
...
Compiling .pio/build/uno/FrameworkArduino/wiring_shift.o
Archiving .pio/build/uno/libFrameworkArduino.a
Indexing .pio/build/uno/libFrameworkArduino.a
Linking .pio/build/uno/firmware.elf
Building .pio/build/uno/firmware.hex
Calculating size .pio/build/uno/firmware.elf
AVR Memory Usage
----------------
Device: atmega328p

Program:    1034 bytes (3.2% Full)
(.text + .data + .bootloader)

Data:          9 bytes (0.4% Full)
(.data + .bss + .noinit)


=========================== [SUCCESS] Took 2.47 seconds ===========================

[Wed Sep  7 15:49:01 2016] Processing nodemcu (platform: espressif8266, board: nodemcu, framework: arduino)
-----------------------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
Collected 34 compatible libraries
Looking for dependencies...
Project does not have dependencies
Compiling .pio/build/nodemcu/src/main.o
Archiving .pio/build/nodemcu/libFrameworkArduinoVariant.a
Indexing .pio/build/nodemcu/libFrameworkArduinoVariant.a
Compiling .pio/build/nodemcu/FrameworkArduino/Esp.o
Compiling .pio/build/nodemcu/FrameworkArduino/FS.o
Compiling .pio/build/nodemcu/FrameworkArduino/HardwareSerial.o
...
Archiving .pio/build/nodemcu/libFrameworkArduino.a
Indexing .pio/build/nodemcu/libFrameworkArduino.a
Linking .pio/build/nodemcu/firmware.elf
Calculating size .pio/build/nodemcu/firmware.elf
text       data     bss     dec     hex filename
221240      888   29400  251528   3d688 .pio/build/nodemcu/firmware.elf
Building .pio/build/nodemcu/firmware.bin
=========================== [SUCCESS] Took 6.43 seconds ===========================

[Wed Sep  7 15:49:07 2016] Processing teensy31 (platform: teensy, board: teensy31, framework: arduino)
-----------------------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
Collected 96 compatible libraries
Looking for dependencies...
Project does not have dependencies
Compiling .pio/build/teensy31/src/main.o
Compiling .pio/build/teensy31/FrameworkArduino/AudioStream.o
Compiling .pio/build/teensy31/FrameworkArduino/DMAChannel.o
...
Compiling .pio/build/teensy31/FrameworkArduino/yield.o
Archiving .pio/build/teensy31/libFrameworkArduino.a
Indexing .pio/build/teensy31/libFrameworkArduino.a
Linking .pio/build/teensy31/firmware.elf
Calculating size .pio/build/teensy31/firmware.elf
text       data     bss     dec     hex filename
11288       168    2288   13744    35b0 .pio/build/teensy31/firmware.elf
Building .pio/build/teensy31/firmware.hex
=========================== [SUCCESS] Took 5.36 seconds ===========================

[Wed Sep  7 15:49:12 2016] Processing lpmsp430g2553 (platform: timsp430, build_flags: -D LED_BUILTIN=RED_LED, board: lpmsp430g2553, framework: arduino)
-----------------------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
Collected 29 compatible libraries
Looking for dependencies...
Project does not have dependencies
Compiling .pio/build/lpmsp430g2553/src/main.o
Compiling .pio/build/lpmsp430g2553/FrameworkAnergia/HardwareSerial.o
Compiling .pio/build/lpmsp430g2553/FrameworkAnergia/IPAddress.o
...
Compiling .pio/build/lpmsp430g2553/FrameworkAnergia/wiring_digital.o
Compiling .pio/build/lpmsp430g2553/FrameworkAnergia/wiring_pulse.o
Compiling .pio/build/lpmsp430g2553/FrameworkAnergia/wiring_shift.o
Archiving .pio/build/lpmsp430g2553/libFrameworkAnergia.a
Indexing .pio/build/lpmsp430g2553/libFrameworkAnergia.a
Linking .pio/build/lpmsp430g2553/firmware.elf
Calculating size .pio/build/lpmsp430g2553/firmware.elf
text       data     bss     dec     hex filename
820           0      20     840     348 .pio/build/lpmsp430g2553/firmware.elf
Building .pio/build/lpmsp430g2553/firmware.hex
=========================== [SUCCESS] Took 2.34 seconds ===========================
```

Process specific environment:

```bash
pio run -e nodemcu -e teensy31
```

```text
[Wed Sep  7 15:49:01 2016] Processing nodemcu (platform: espressif8266, board: nodemcu, framework: arduino)
-----------------------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
Collected 34 compatible libraries
Looking for dependencies...
Project does not have dependencies
Compiling .pio/build/nodemcu/src/main.o
Archiving .pio/build/nodemcu/libFrameworkArduinoVariant.a
Indexing .pio/build/nodemcu/libFrameworkArduinoVariant.a
Compiling .pio/build/nodemcu/FrameworkArduino/Esp.o
Compiling .pio/build/nodemcu/FrameworkArduino/FS.o
Compiling .pio/build/nodemcu/FrameworkArduino/HardwareSerial.o
...
Archiving .pio/build/nodemcu/libFrameworkArduino.a
Indexing .pio/build/nodemcu/libFrameworkArduino.a
Linking .pio/build/nodemcu/firmware.elf
Calculating size .pio/build/nodemcu/firmware.elf
text       data     bss     dec     hex filename
221240      888   29400  251528   3d688 .pio/build/nodemcu/firmware.elf
Building .pio/build/nodemcu/firmware.bin
=========================== [SUCCESS] Took 6.43 seconds ===========================

[Wed Sep  7 15:49:07 2016] Processing teensy31 (platform: teensy, board: teensy31, framework: arduino)
-----------------------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
Collected 96 compatible libraries
Looking for dependencies...
Project does not have dependencies
Compiling .pio/build/teensy31/src/main.o
Compiling .pio/build/teensy31/FrameworkArduino/AudioStream.o
Compiling .pio/build/teensy31/FrameworkArduino/DMAChannel.o
...
Compiling .pio/build/teensy31/FrameworkArduino/yield.o
Archiving .pio/build/teensy31/libFrameworkArduino.a
Indexing .pio/build/teensy31/libFrameworkArduino.a
Linking .pio/build/teensy31/firmware.elf
Calculating size .pio/build/teensy31/firmware.elf
text       data     bss     dec     hex filename
11288       168    2288   13744    35b0 .pio/build/teensy31/firmware.elf
Building .pio/build/teensy31/firmware.hex
=========================== [SUCCESS] Took 5.36 seconds ===========================
```

Process specific target (clean project):

```bash
pio run -t clean
```

```text
[Wed Sep  7 15:53:26 2016] Processing uno (platform: atmelavr, board: uno, framework: arduino)
-----------------------------------------------------------------------------------------------------
Removed .pio/build/uno/firmware.elf
Removed .pio/build/uno/firmware.hex
Removed .pio/build/uno/libFrameworkArduino.a
Removed .pio/build/uno/libFrameworkArduinoVariant.a
Removed .pio/build/uno/FrameworkArduino/_wiring_pulse.o
Removed .pio/build/uno/FrameworkArduino/abi.o
Removed .pio/build/uno/FrameworkArduino/CDC.o
Removed .pio/build/uno/FrameworkArduino/HardwareSerial.o
Removed .pio/build/uno/FrameworkArduino/HardwareSerial0.o
Removed .pio/build/uno/FrameworkArduino/HardwareSerial1.o
Removed .pio/build/uno/FrameworkArduino/HardwareSerial2.o
Removed .pio/build/uno/FrameworkArduino/HardwareSerial3.o
Removed .pio/build/uno/FrameworkArduino/hooks.o
Removed .pio/build/uno/FrameworkArduino/IPAddress.o
Removed .pio/build/uno/FrameworkArduino/main.o
Removed .pio/build/uno/FrameworkArduino/new.o
Removed .pio/build/uno/FrameworkArduino/PluggableUSB.o
Removed .pio/build/uno/FrameworkArduino/Print.o
Removed .pio/build/uno/FrameworkArduino/Stream.o
Removed .pio/build/uno/FrameworkArduino/Tone.o
Removed .pio/build/uno/FrameworkArduino/USBCore.o
Removed .pio/build/uno/FrameworkArduino/WInterrupts.o
Removed .pio/build/uno/FrameworkArduino/wiring.o
Removed .pio/build/uno/FrameworkArduino/wiring_analog.o
Removed .pio/build/uno/FrameworkArduino/wiring_digital.o
Removed .pio/build/uno/FrameworkArduino/wiring_pulse.o
Removed .pio/build/uno/FrameworkArduino/wiring_shift.o
Removed .pio/build/uno/FrameworkArduino/WMath.o
Removed .pio/build/uno/FrameworkArduino/WString.o
Removed .pio/build/uno/src/main.o
Done cleaning
======================= [SUCCESS] Took 0.49 seconds =======================

[Wed Sep  7 15:53:27 2016] Processing nodemcu (platform: espressif8266, board: nodemcu, framework: arduino)
-----------------------------------------------------------------------------------------------------
Removed .pio/build/nodemcu/firmware.bin
Removed .pio/build/nodemcu/firmware.elf
Removed .pio/build/nodemcu/libFrameworkArduino.a
Removed .pio/build/nodemcu/libFrameworkArduinoVariant.a
...
Removed .pio/build/nodemcu/FrameworkArduino/spiffs/spiffs_nucleus.o
Removed .pio/build/nodemcu/FrameworkArduino/umm_malloc/umm_malloc.o
Removed .pio/build/nodemcu/src/main.o
Done cleaning
======================= [SUCCESS] Took 0.50 seconds =======================

[Wed Sep  7 15:53:27 2016] Processing teensy31 (platform: teensy, board: teensy31, framework: arduino)
-----------------------------------------------------------------------------------------------------
Removed .pio/build/teensy31/firmware.elf
Removed .pio/build/teensy31/firmware.hex
Removed .pio/build/teensy31/libFrameworkArduino.a
Removed .pio/build/teensy31/FrameworkArduino/analog.o
Removed .pio/build/teensy31/FrameworkArduino/AudioStream.o
...
Removed .pio/build/teensy31/FrameworkArduino/WString.o
Removed .pio/build/teensy31/FrameworkArduino/yield.o
Removed .pio/build/teensy31/src/main.o
Done cleaning
======================= [SUCCESS] Took 0.50 seconds =======================

[Wed Sep  7 15:53:28 2016] Processing lpmsp430g2553 (platform: timsp430, build_flags: -D LED_BUILTIN=RED_LED, board: lpmsp430g2553, framework: energia)
-----------------------------------------------------------------------------------------------------
Removed .pio/build/lpmsp430g2553/firmware.elf
Removed .pio/build/lpmsp430g2553/firmware.hex
Removed .pio/build/lpmsp430g2553/libFrameworkAnergia.a
Removed .pio/build/lpmsp430g2553/FrameworkAnergia/atof.o
...
Removed .pio/build/lpmsp430g2553/FrameworkAnergia/avr/dtostrf.o
Removed .pio/build/lpmsp430g2553/src/main.o
Done cleaning
======================= [SUCCESS] Took 0.49 seconds =======================
```

Mix environments and targets:

```bash
pio run -e uno -t upload
```

```text
[Wed Sep  7 15:55:11 2016] Processing uno (platform: atmelavr, board: uno, framework: arduino)
--------------------------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
Collected 36 compatible libraries
Looking for dependencies...
Project does not have dependencies
Compiling .pio/build/uno/src/main.o
Archiving .pio/build/uno/libFrameworkArduinoVariant.a
Indexing .pio/build/uno/libFrameworkArduinoVariant.a
Compiling .pio/build/uno/FrameworkArduino/CDC.o
...
Compiling .pio/build/uno/FrameworkArduino/wiring_shift.o
Archiving .pio/build/uno/libFrameworkArduino.a
Indexing .pio/build/uno/libFrameworkArduino.a
Linking .pio/build/uno/firmware.elf
Checking program size .pio/build/uno/firmware.elf
text       data     bss     dec     hex filename
1034          0       9    1043     413 .pio/build/uno/firmware.elf
Building .pio/build/uno/firmware.hex
Looking for upload port...
Auto-detected: /dev/cu.usbmodemFA141
Uploading .pio/build/uno/firmware.hex

avrdude: AVR device initialized and ready to accept instructions

Reading | ################################################## | 100% 0.01s

avrdude: Device signature = 0x1e950f
avrdude: reading input file ".pio/build/uno/firmware.hex"
avrdude: writing flash (1034 bytes):

Writing | ################################################## | 100% 0.18s

avrdude: 1034 bytes of flash written
avrdude: verifying flash memory against .pio/build/uno/firmware.hex:
avrdude: load data flash data from input file .pio/build/uno/firmware.hex:
avrdude: input file .pio/build/uno/firmware.hex contains 1034 bytes
avrdude: reading on-chip flash data:

Reading | ################################################## | 100% 0.15s

avrdude: verifying ...
avrdude: 1034 bytes of flash verified

avrdude: safemode: Fuses OK (H:00, E:00, L:00)

avrdude done.  Thank you.

======================== [SUCCESS] Took 4.14 seconds ========================
```
