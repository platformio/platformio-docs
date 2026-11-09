---
description: Create, build and upload a "Blink" project for three different boards with the PlatformIO Core CLI.
---

# Quick start

In this tutorial you create a "Blink" project from the command line, build it
for three boards with different architectures, and upload it to a board. It
takes about 15 minutes and introduces the PlatformIO workflow you will use for
any project.

You will use these boards, all with the [Arduino](/hardware/frameworks/arduino)
framework. You do not need all three; any one of them, or another board
supported by the Arduino framework, is enough.

| Board | Board ID | Development platform |
| --- | --- | --- |
| [Arduino Uno](/hardware/boards/atmelavr/uno) | `uno` | [Atmel AVR](/hardware/platforms/atmelavr) |
| [NodeMCU 1.0 (ESP-12E Module)](/hardware/boards/espressif8266/nodemcuv2) | `nodemcuv2` | [Espressif 8266](/hardware/platforms/espressif8266) |
| [Teensy 4.1](/hardware/boards/teensy/teensy41) | `teensy41` | [Teensy](/hardware/platforms/teensy) |

## Before you begin {#before-you-begin}

- [Install PlatformIO Core](./install/index.md). If you use
  [PlatformIO IDE](./platformio-ide.md), you already have it: run the commands
  below in the IDE's terminal.
- On Linux, install the [udev rules](./install/udev-rules.md) so that you can
  upload without root privileges.

<a id="setting-up-the-project"></a>

## Find the board ID {#board-identifier}

Every board has an ID that you use in commands and in
[`platformio.ini`](../reference/platformio-ini/index.md). Find it in the
[boards catalog](/hardware/boards) or with
[`pio boards`](../reference/cli/pio-boards.md), which filters by any text.
For example, to list the Teensy boards:

```bash
pio boards teensy
```

```text
Platform: teensy
================================================================================
ID         MCU          Frequency    Flash    RAM       Name
---------  -----------  -----------  -------  --------  ------------------------
teensymm   IMXRT1062    600MHz       7.75MB   512KB     SparkFun MicroMod Teensy
teensy2    ATMEGA32U4   16MHz        31.50KB  2.50KB    Teensy 2.0
teensy30   MK20DX128    48MHz        128KB    16KB      Teensy 3.0
teensy31   MK20DX256    72MHz        256KB    64KB      Teensy 3.1 / 3.2
teensy35   MK64FX512    120MHz       512KB    255.99KB  Teensy 3.5
teensy36   MK66FX1M0    180MHz       1MB      256KB     Teensy 3.6
teensy40   IMXRT1062    600MHz       1.94MB   512KB     Teensy 4.0
teensy41   IMXRT1062    600MHz       7.75MB   512KB     Teensy 4.1
teensylc   MKL26Z64     48MHz        62KB     8KB       Teensy LC
teensy2pp  AT90USB1286  16MHz        127KB    8KB       Teensy++ 2.0
```

The ID of the Teensy 4.1 is `teensy41`.

## Create the project {#initialize-project}

1. Create an empty directory for the project and change to it:

   ```bash
   mkdir blink
   cd blink
   ```

2. Initialize the project with
   [`pio project init`](../reference/cli/pio-project/init.md), passing one
   `--board` option per board:

   ```bash
   pio project init --board uno --board nodemcuv2 --board teensy41
   ```

   PlatformIO creates the project and installs the development platforms,
   toolchains and frameworks the boards need. The first run can take a few
   minutes. It ends with:

   ```text
   Project has been successfully initialized!
   ```

The project now contains:

| Path | Purpose |
| --- | --- |
| `platformio.ini` | The [project configuration file](../reference/platformio-ini/index.md) |
| `src/` | Your source files (`.c`, `.cpp`, `.S`, `.ino`, ...) |
| `include/` | Your project header files |
| `lib/` | Project-specific (private) [libraries](../guides/libraries/index.md) |
| `test/` | [Unit tests](../guides/unit-testing/index.md) |
| `.gitignore` | Excludes the `.pio` build directory from version control |

`platformio.ini` has one [project environment](../reference/platformio-ini/env/index.md)
per board:

```ini
[env:uno]
platform = atmelavr
board = uno
framework = arduino

[env:nodemcuv2]
platform = espressif8266
board = nodemcuv2
framework = arduino

[env:teensy41]
platform = teensy
board = teensy41
framework = arduino
```

:::tip

To add a board to an existing project later, run `pio project init --board <board_id>`
in the project directory again.

:::

## Add the code {#add-the-code}

Create `src/main.cpp` with the following content:

```cpp
/**
 * Blink
 *
 * Turns on an LED on for one second,
 * then off for one second, repeatedly.
 */
#include "Arduino.h"

#ifndef LED_BUILTIN
#define LED_BUILTIN 13
#endif

void setup()
{
  // initialize LED digital pin as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  // turn the LED on (HIGH is the voltage level)
  digitalWrite(LED_BUILTIN, HIGH);

  // wait for a second
  delay(1000);

  // turn the LED off by making the voltage LOW
  digitalWrite(LED_BUILTIN, LOW);

   // wait for a second
  delay(1000);
}
```

## Build and upload {#process-project}

Use [`pio run`](../reference/cli/pio-run.md) from the project directory.
Without options it builds every environment in `platformio.ini`:

```bash
pio run
```

To build one environment only, pass its name with `-e`:

```bash
pio run -e uno
```

To build and upload, connect the board over USB and add the `upload` target
(`-t`). PlatformIO detects the serial port automatically; to choose one, add
[`--upload-port`](../reference/cli/pio-run.md#cmdoption-pio-run-upload-port).

```bash
pio run -e uno -t upload
```

The board's LED now blinks once per second.

Other useful commands:

| Command | What it does |
| --- | --- |
| `pio run -t clean` | Deletes the build output |
| `pio run --list-targets` | Lists the [project targets](../reference/cli/pio-run.md#cmdoption-pio-run-list-targets) you can run |
| `pio device monitor` | Opens the [serial monitor](../reference/cli/pio-device/monitor.md) |

## Next steps {#further-reading}

- Configure your project: [`platformio.ini` reference](../reference/platformio-ini/index.md).
- Add libraries: [Library management](../guides/libraries/index.md).
- Debug on hardware: [Debugging](../guides/debugging/index.md).
- Browse all commands: [CLI reference](../reference/cli/index.md).
- Browse [project examples](https://github.com/platformio/platformio-examples).
