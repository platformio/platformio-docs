<a id="debugging-tool-avr-stub"></a>

# avr-stub {#avr-stub}

avr-stub is a source level debugger based on GDB stub mechanism. It works with ATmega328 and Arduino Mega microcontrollers without an external programmer. The official reference can be found [here](https://github.com/jdolinay/avr_debug/?utm_source=platformio&utm_medium=docs).

## Configuration {#configuration}

In a nutshell, avr-stub is a piece of software (stub) that is added to your application and communicates with PlatformIO when a debug session is running. It requires several additional configuration steps in order to use it as a debug tool. To use avr-stub, the following settings in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md):

```ini
[env:myenv]
platform = atmelavr
board = ...

debug_tool = avr-stub
debug_port = SERIAL_PORT

; GDB stub implementation
lib_deps =
    jdolinay/avr-debugger @ ~1.4
```

Where the value in [debug_port](../../reference/platformio-ini/env/debug-port.md) is a serial port connected to your board and `jdolinay/avr-debugger` is a special library that implements the GDB stub.

In order to enable the GDB stub in your application, a call to the special function `debug_init` must be added at the beginning of your application. For example, with the Arduino framework it might look like this:

```cpp
#include "Arduino.h"
#include "avr8-stub.h"
#include "app_api.h" // only needed with flash breakpoints

void setup()
{
  // initialize GDB stub
  debug_init();
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

:::warning

If your program doesn't stop on a breakpoint, try specifying an explicit breakpoint directly in the code using the `breakpoint` function:

```cpp
...

void loop()
{
  breakpoint();
  digitalWrite(LED_BUILTIN, HIGH);
  delay(300);
  digitalWrite(LED_BUILTIN, LOW);
  delay(100);
}

...
```

:::

## Breakpoint modes {#breakpoint-modes}

The avr-stub tool supports the following three breakpoint modes:

| Description | AVR8_BREAKPOINT_MODE |
|---|---|
| FLASH breakpoint mode, which works only with atmega328 based boards and requires a special bootloader | `0` |
| RAM breakpoint mode, the default mode which works out of the box with all atmega328, atmega1280, and atmega2560 based boards | `1` |
| FLASH breakpoint mode through Optiboot, which works with all atmega328, atmega1280, and atmega2560 based boards and requires the version 8 of the bootloader. | `2` |

To switch between modes, specify a special macro definition `AVR8_BREAKPOINT_MODE` with the appropriate value from the table above, for example:

```ini
[env:myenv]
platform = atmelavr
board = uno

; Set breakpoint mode
build_flags =
  -DAVR8_BREAKPOINT_MODE=2

debug_tool = avr-stub
debug_port = SERIAL_PORT

lib_deps =
    jdolinay/avr-debugger @ ~1.4
```

## Debugger limitations {#debugger-limitations}

- One external interrupt pin must be reserved for the debugger.
- Any part of your application that uses the UART module (e.g. Arduino Serial class) cannot be used in your program together with the debugger.
- When using flash breakpoints the watchdog cannot be used.

More detailed information can be found in the `Important limitations of the debugger` section in [the official documentation](https://github.com/jdolinay/avr_debug/blob/master/doc/avr_debug.pdf).

<!-- begin_platforms -->

## Platforms

| Name | Description |
|---|---|
| [Atmel AVR](../platforms/atmelavr.mdx) | Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |

## Boards

:::note

For more detailed `board` information please scroll tables below by horizontal.

:::

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [ATmega1280](../boards/atmelavr/atmega1280.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1280 | 16MHz | 128KB | 8KB |
| [ATmega2560](../boards/atmelavr/atmega2560.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 256KB | 8KB |
| [ATmega328](../boards/atmelavr/atmega328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328 | 16MHz | 32KB | 2KB |
| [ATmega328P/PA](../boards/atmelavr/atmega328p.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 32KB | 2KB |
| [Adafruit Feather 328P](../boards/atmelavr/feather328p.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 31.50KB | 2KB |
| [Adafruit Metro](../boards/atmelavr/metro.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Adafruit Pro Trinket 3V/12MHz (FTDI)](../boards/atmelavr/protrinket3ftdi.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 12MHz | 28KB | 2KB |
| [Adafruit Pro Trinket 5V/16MHz (FTDI)](../boards/atmelavr/protrinket5ftdi.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 28KB | 2KB |
| [Alorium Hinj](../boards/atmelavr/alorium-hinj.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Alorium Sno](../boards/atmelavr/alorium-sno.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Alorium XLR8](../boards/atmelavr/alorium-xlr8.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Anarduino MiniWireless](../boards/atmelavr/miniwireless.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Arduino BT ATmega328](../boards/atmelavr/btatmega328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 28KB | 2KB |
| [Arduino Duemilanove or Diecimila ATmega328](../boards/atmelavr/diecimilaatmega328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 30KB | 2KB |
| [Arduino Ethernet](../boards/atmelavr/ethernet.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Arduino Fio](../boards/atmelavr/fio.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 30KB | 2KB |
| [Arduino LilyPad ATmega328](../boards/atmelavr/lilypadatmega328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 30KB | 2KB |
| [Arduino Mega ADK](../boards/atmelavr/megaadk.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 248KB | 8KB |
| [Arduino Mega or Mega 2560 ATmega1280](../boards/atmelavr/megaatmega1280.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1280 | 16MHz | 124KB | 8KB |
| [Arduino Mega or Mega 2560 ATmega2560 (Mega 2560)](../boards/atmelavr/megaatmega2560.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 248KB | 8KB |
| [Arduino Mini ATmega328](../boards/atmelavr/miniatmega328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 28KB | 2KB |
| [Arduino Nano ATmega328](../boards/atmelavr/nanoatmega328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 30KB | 2KB |
| [Arduino Nano ATmega328 (New Bootloader)](../boards/atmelavr/nanoatmega328new.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 30KB | 2KB |
| [Arduino Pro or Pro Mini ATmega328 (3.3V, 8 MHz)](../boards/atmelavr/pro8mhzatmega328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 30KB | 2KB |
| [Arduino Pro or Pro Mini ATmega328 (5V, 16 MHz)](../boards/atmelavr/pro16mhzatmega328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 30KB | 2KB |
| [Arduino Uno](../boards/atmelavr/uno.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Arduino Uno Mini](../boards/atmelavr/uno-mini.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [BQ ZUM BT-328](../boards/atmelavr/zumbt328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 28KB | 2KB |
| [BitWizard Raspduino](../boards/atmelavr/raspduino.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 30KB | 2KB |
| [Controllino Maxi](../boards/atmelavr/controllino-maxi.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 248KB | 8KB |
| [Controllino Maxi Automation](../boards/atmelavr/controllino-maxi-automation.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 248KB | 8KB |
| [Controllino Mega](../boards/atmelavr/controllino-mega.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 248KB | 8KB |
| [Controllino Mini](../boards/atmelavr/controllino-mini.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [FYSETC F6 V1.3](../boards/atmelavr/fysetc-f6-13.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 252KB | 8KB |
| [LightBlue Bean](../boards/atmelavr/lightblue-bean.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 31.50KB | 2KB |
| [LightBlue Bean+](../boards/atmelavr/lightblue-beanplus.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [LowPowerLab MightyHat](../boards/atmelavr/mightyhat.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31KB | 2KB |
| [LowPowerLab Moteino](../boards/atmelavr/moteino.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [LowPowerLab Moteino (8Mhz)](../boards/atmelavr/moteino8mhz.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 31.50KB | 2KB |
| [Microduino Core (Atmega328P@16M,5V)](../boards/atmelavr/328p16m.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Microduino Core (Atmega328P@8M,3.3V)](../boards/atmelavr/328p8m.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 31.50KB | 2KB |
| [OpenEnergyMonitor emonPi](../boards/atmelavr/emonpi.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 30KB | 2KB |
| [PanStamp AVR](../boards/atmelavr/panstampavr.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 31.50KB | 2KB |
| [Prusa RAMBo](../boards/atmelavr/prusa-rambo.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 252KB | 8KB |
| [RepRap RAMBo](../boards/atmelavr/reprap-rambo.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 252KB | 8KB |
| [SODAQ Moja](../boards/atmelavr/sodaq-moja.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 31.50KB | 2KB |
| [Seeeduino](../boards/atmelavr/seeeduino.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [SparkFun Digital Sandbox](../boards/atmelavr/sparkfun-digitalsandbox.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 31.50KB | 2KB |
| [SparkFun Mega Pro 3.3V/8MHz](../boards/atmelavr/sparkfun-megapro8mhz.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 8MHz | 252KB | 8KB |
| [SparkFun Mega Pro 5V/16MHz](../boards/atmelavr/sparkfun-megapro16mhz.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 248KB | 8KB |
| [SparkFun Mega Pro Mini 3.3V](../boards/atmelavr/sparkfun-megamini.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 8MHz | 252KB | 8KB |
| [SparkFun MicroView](../boards/atmelavr/uview.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [SparkFun RedBoard](../boards/atmelavr/sparkfun-redboard.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [SparkFun Serial 7-Segment Display](../boards/atmelavr/sparkfun-serial7seg.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 31.50KB | 2KB |
| [SpellFoundry Sleepy Pi 2](../boards/atmelavr/sleepypi.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 30KB | 2KB |
| [Talk2 Whisper Node](../boards/atmelavr/whispernode.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [TinyCircuits TinyDuino Processor Board](../boards/atmelavr/tinyduino.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 30KB | 2KB |
| [TinyCircuits TinyLily Mini Processor](../boards/atmelavr/tinylily.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 30KB | 2KB |
| [ubIQio Ardhat](../boards/atmelavr/ardhat.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
