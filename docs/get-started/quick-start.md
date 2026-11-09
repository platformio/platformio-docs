<a id="core-quickstart"></a>

# Quick Start {#quick-start}

This tutorial introduces you to the basics of [PlatformIO Core (CLI)](./platformio-core.md) Command Line Interface (CLI) workflow and shows you a creation process of a simple cross-platform “Blink” Project. After finishing you will have a general understanding of how to work with the multiple development platforms and embedded boards.

## Setting Up the Project {#setting-up-the-project}

[PlatformIO Core (CLI)](./platformio-core.md) provides special [pio project init](../reference/cli/pio-project/init.md) command for configuring your projects. It allows one to initialize new empty project or update existing with the new data.

What is more, [pio project init](../reference/cli/pio-project/init.md) can be used for [Cloud & Desktop IDEs](../guides/ide/index.md). It means that you will be able to import pre-generated PlatformIO project using favorite IDE and extend it with the professional instruments for IoT development.

This tutorial is based on the next popular embedded boards and development platforms using [Arduino](/hardware/frameworks/arduino):

| Platform | Board | Framework |
|---|---|---|
| [Atmel AVR](/hardware/platforms/atmelavr) | [Arduino Uno](/hardware/boards/atmelavr/uno) | [Arduino](/hardware/frameworks/arduino) |
| [Espressif 8266](/hardware/platforms/espressif8266) | [NodeMCU 1.0 (ESP-12E Module)](/hardware/boards/espressif8266/nodemcuv2) | [Arduino](/hardware/frameworks/arduino) |
| [Teensy](/hardware/platforms/teensy) | [Teensy 3.1 / 3.2](/hardware/boards/teensy/teensy31) | [Arduino](/hardware/frameworks/arduino) |

## Board Identifier {#board-identifier}

[pio project init](../reference/cli/pio-project/init.md) command requires to specify board identifier ID. It can be found using [Boards](/hardware/boards) catalog, [Boards Explorer](https://platformio.org/boards) or [pio boards](../reference/cli/pio-boards.md) command. For example, using [pio boards](../reference/cli/pio-boards.md) let's try to find Teensy boards:

```bash
> pio boards teensy

Platform: teensy
---------------------------------------------------------------------------
ID                    MCU            Frequency  Flash   RAM    Name
---------------------------------------------------------------------------
teensy20              atmega32u4     16MHz     31K    2.5K  Teensy 2.0
teensy30              mk20dx128      48MHz     128K   16K   Teensy 3.0
teensy31              mk20dx256      72MHz     256K   64K   Teensy 3.1 / 3.2
teensylc              mkl26z64       48MHz     62K    8K    Teensy LC
teensy20pp            at90usb1286    16MHz     127K   8K    Teensy++ 2.0
```

According to the table above the ID for [Teensy 3.1 / 3.2](/hardware/boards/teensy/teensy31) is `teensy31`. Also, the ID for [Arduino Uno](/hardware/boards/atmelavr/uno) is `uno` and for [NodeMCU 1.0 (ESP-12E Module)](/hardware/boards/espressif8266/nodemcuv2) is `nodemcuv2`.

## Initialize Project {#initialize-project}

PlatformIO ecosystem contains big database with pre-configured settings for the most popular embedded boards. It helps you to forget about installing toolchains, writing build scripts or configuring uploading process. Just tell PlatformIO the Board ID and you will receive full working project with pre-installed instruments for the professional development.

1. Create empty folder where you are going to initialize new PlatformIO project. Then open system Terminal and change directory to it:

   ```bash
   # create new directory
   > mkdir path_to_the_new_directory

   # go to it
   > cd path_to_the_new_directory
   ```

2. Initialize project for the boards mentioned above (you can specify more than one board at time):

   ```bash
   > pio project init --board uno --board nodemcuv2 --board teensy31

   The current working directory *** will be used for the new project.
   You can specify another project directory via
   `pio project init -d %PATH_TO_THE_PROJECT_DIR%` command.

   The following files/directories will be created in ***
   platformio.ini - Project Configuration File. |-> PLEASE EDIT ME <-|
   src - Put your source files here
   lib - Put here project specific (private) libraries
   Do you want to continue? [y/N]: y
   Project has been successfully initialized!
   Useful commands:
   `pio run` - process/build project from the current directory
   `pio run --target upload` or `pio run -t upload` - upload firmware to embedded board
   `pio run --target clean` - clean project (remove compiled files)
   ```

Congrats! You have just created the first PlatformIO based Project with the next structure:

- ["platformio.ini" (Project Configuration File)](../reference/platformio-ini/index.md)
- `src` directory where you should place source code (`*.h, *.c, *.cpp, *.S, *.ino, etc.`)
- `lib` directory can be used for the project specific (private) libraries. More details are located in `lib/README` file.
- Miscellaneous files for VCS and [Continuous Integration](../guides/ci/index.md) support.

:::note

If you need to add new board to the existing project please use [pio project init](../reference/cli/pio-project/init.md) again.

:::

The result of just generated `platformio.ini`:

```ini
; PlatformIO Project Configuration File
;
;   Build options: build flags, source filter, extra scripting
;   Upload options: custom port, speed and extra flags
;   Library options: dependencies, extra library storages
;
; Please visit documentation for the other options and examples
; https://docs.platformio.org/en/latest/projectconf/index.html

[env:uno]
platform = atmelavr
framework = arduino
board = uno

[env:nodemcuv2]
platform = espressif8266
framework = arduino
board = nodemcuv2

[env:teensy31]
platform = teensy
framework = arduino
board = teensy31
```

Now, we need to create `main.cpp` file and place it to `src` folder of our newly created project. The contents of `src/main.cpp`:

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

The final Project structure:

```bash
project_dir
├── lib
│   └── README
├── platformio.ini
└── src
    └── main.cpp
```

## Process Project {#process-project}

[PlatformIO Core (CLI)](./platformio-core.md) provides special [pio run](../reference/cli/pio-run.md) command to process project. If you call it without any arguments, PlatformIO Build System will process all project environments (which were created per each board specified above). Here are a few useful commands:

- `pio run`. Process (build) all environments specified in ["platformio.ini" (Project Configuration File)](../reference/platformio-ini/index.md)
- `pio run --target upload`. Build project and upload firmware to the all devices specified in ["platformio.ini" (Project Configuration File)](../reference/platformio-ini/index.md)
- `pio run --target clean`. Clean project (delete compiled objects)
- `pio run -e uno`. Process only `uno` environment
- `pio run -e uno -t upload`. Build project only for `uno` and upload firmware.

Please follow to [`pio run --list-targets`](../reference/cli/pio-run.md#cmdoption-pio-run-list-targets) documentation for the other targets.

## Further Reading {#further-reading}

- [Project examples](https://github.com/platformio/platformio-examples/tree/develop)
- [CLI Guide](../reference/cli/index.md) for [PlatformIO Core (CLI)](./platformio-core.md) commands
