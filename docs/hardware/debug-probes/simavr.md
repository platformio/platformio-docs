---
description: "Use the simavr debug probe with PlatformIO: configuration, drivers, wiring and supported boards."
---

# simavr

simavr is a lean, mean and hackable AVR simulator. See the [official documentation](https://github.com/buserror/simavr/?utm_source=platformio&utm_medium=docs).

## Configuration {#configuration}

Select this probe with the [`debug_tool`](../../reference/platformio-ini/env/debug-tool.md) option in [`platformio.ini`](../../reference/platformio-ini/index.md):

```ini
[env:myenv]
platform = ...
board = ...
debug_tool = simavr
```

See also:

- [Debugging options](../../reference/platformio-ini/env/debug-options.md)

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

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [ATmega128/A](../boards/atmelavr/atmega128.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA128 | 16MHz | 128KB | 4KB |
| [ATmega1280](../boards/atmelavr/atmega1280.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1280 | 16MHz | 128KB | 8KB |
| [ATmega1281](../boards/atmelavr/atmega1281.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1281 | 16MHz | 128KB | 8KB |
| [ATmega1284](../boards/atmelavr/atmega1284.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1284 | 16MHz | 128KB | 16KB |
| [ATmega1284P](../boards/atmelavr/atmega1284p.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1284P | 16MHz | 128KB | 16KB |
| [ATmega16](../boards/atmelavr/atmega16.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA16 | 16MHz | 16KB | 1KB |
| [ATmega164P/PA](../boards/atmelavr/atmega164p.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA164P | 16MHz | 16KB | 1KB |
| [ATmega168/A](../boards/atmelavr/atmega168.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA168 | 16MHz | 16KB | 1KB |
| [ATmega168P/PA](../boards/atmelavr/atmega168p.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA168P | 16MHz | 16KB | 1KB |
| [ATmega2560](../boards/atmelavr/atmega2560.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 256KB | 8KB |
| [ATmega324A](../boards/atmelavr/atmega324a.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA324A | 16MHz | 32KB | 2KB |
| [ATmega324P](../boards/atmelavr/atmega324p.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA324P | 16MHz | 32KB | 2KB |
| [ATmega324PA](../boards/atmelavr/atmega324pa.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA324PA | 16MHz | 32KB | 2KB |
| [ATmega328](../boards/atmelavr/atmega328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328 | 16MHz | 32KB | 2KB |
| [ATmega328P/PA](../boards/atmelavr/atmega328p.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 32KB | 2KB |
| [ATmega48/A](../boards/atmelavr/atmega48.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA48 | 16MHz | 4KB | 512B |
| [ATmega48P/PA](../boards/atmelavr/atmega48p.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA48P | 16MHz | 4KB | 512B |
| [ATmega644P/PA](../boards/atmelavr/atmega644p.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA644P | 16MHz | 64KB | 4KB |
| [ATmega8/A](../boards/atmelavr/atmega8.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA8 | 16MHz | 8KB | 1KB |
| [ATmega88/A](../boards/atmelavr/atmega88.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA88 | 16MHz | 8KB | 1KB |
| [ATmega88P/PA](../boards/atmelavr/atmega88p.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA88P | 16MHz | 8KB | 1KB |
| [ATtiny13](../boards/atmelavr/attiny13.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATTINY13 | 9MHz | 1KB | 64B |
| [ATtiny13A](../boards/atmelavr/attiny13a.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATTINY13A | 9MHz | 1KB | 64B |
| [Adafruit Bluefruit Micro](../boards/atmelavr/bluefruitmicro.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 8MHz | 28KB | 2.50KB |
| [Adafruit Circuit Playground Classic](../boards/atmelavr/circuitplay-classic.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 8MHz | 28KB | 2.50KB |
| [Adafruit Feather 328P](../boards/atmelavr/feather328p.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 31.50KB | 2KB |
| [Adafruit Feather 32u4](../boards/atmelavr/feather32u4.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 8MHz | 28KB | 2.50KB |
| [Adafruit Flora](../boards/atmelavr/flora8.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 8MHz | 28KB | 2.50KB |
| [Adafruit Gemma](../boards/atmelavr/gemma.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATTINY85 | 8MHz | 8KB | 512B |
| [Adafruit ItsyBitsy 3V/8MHz](../boards/atmelavr/itsybitsy32u4-3v.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 8MHz | 28KB | 2.50KB |
| [Adafruit ItsyBitsy 5V/16MHz](../boards/atmelavr/itsybitsy32u4-5v.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [Adafruit Metro](../boards/atmelavr/metro.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Adafruit Pro Trinket 3V/12MHz (FTDI)](../boards/atmelavr/protrinket3ftdi.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 12MHz | 28KB | 2KB |
| [Adafruit Pro Trinket 3V/12MHz (USB)](../boards/atmelavr/protrinket3.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 12MHz | 28KB | 2KB |
| [Adafruit Pro Trinket 5V/16MHz (FTDI)](../boards/atmelavr/protrinket5ftdi.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 28KB | 2KB |
| [Adafruit Pro Trinket 5V/16MHz (USB)](../boards/atmelavr/protrinket5.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 28KB | 2KB |
| [Adafruit Trinket 3V/8MHz](../boards/atmelavr/trinket3.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATTINY85 | 8MHz | 8KB | 512B |
| [Adafruit Trinket 5V/16MHz](../boards/atmelavr/trinket5.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATTINY85 | 16MHz | 8KB | 512B |
| [Alorium Hinj](../boards/atmelavr/alorium-hinj.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Alorium Sno](../boards/atmelavr/alorium-sno.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Alorium XLR8](../boards/atmelavr/alorium-xlr8.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Anarduino MiniWireless](../boards/atmelavr/miniwireless.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Arduboy](../boards/atmelavr/arduboy.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [Arduboy DevKit](../boards/atmelavr/arduboy-devkit.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [Arduino BT ATmega168](../boards/atmelavr/btatmega168.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA168 | 16MHz | 14KB | 1KB |
| [Arduino BT ATmega328](../boards/atmelavr/btatmega328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 28KB | 2KB |
| [Arduino Duemilanove or Diecimila ATmega168](../boards/atmelavr/diecimilaatmega168.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA168 | 16MHz | 14KB | 1KB |
| [Arduino Duemilanove or Diecimila ATmega328](../boards/atmelavr/diecimilaatmega328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 30KB | 2KB |
| [Arduino Esplora](../boards/atmelavr/esplora.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [Arduino Ethernet](../boards/atmelavr/ethernet.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Arduino Fio](../boards/atmelavr/fio.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 30KB | 2KB |
| [Arduino Industrial 101](../boards/atmelavr/chiwawa.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [Arduino Leonardo](../boards/atmelavr/leonardo.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [Arduino Leonardo ETH](../boards/atmelavr/leonardoeth.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [Arduino LilyPad ATmega168](../boards/atmelavr/lilypadatmega168.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA168 | 8MHz | 14KB | 1KB |
| [Arduino LilyPad ATmega328](../boards/atmelavr/lilypadatmega328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 30KB | 2KB |
| [Arduino LilyPad USB](../boards/atmelavr/lilypadusb.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 8MHz | 28KB | 2.50KB |
| [Arduino Mega ADK](../boards/atmelavr/megaadk.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 248KB | 8KB |
| [Arduino Mega or Mega 2560 ATmega1280](../boards/atmelavr/megaatmega1280.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1280 | 16MHz | 124KB | 8KB |
| [Arduino Mega or Mega 2560 ATmega2560 (Mega 2560)](../boards/atmelavr/megaatmega2560.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 248KB | 8KB |
| [Arduino Micro](../boards/atmelavr/micro.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [Arduino Mini ATmega168](../boards/atmelavr/miniatmega168.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA168 | 16MHz | 14KB | 1KB |
| [Arduino Mini ATmega328](../boards/atmelavr/miniatmega328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 28KB | 2KB |
| [Arduino NG or older ATmega168](../boards/atmelavr/atmegangatmega168.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA168 | 16MHz | 14KB | 1KB |
| [Arduino NG or older ATmega8](../boards/atmelavr/atmegangatmega8.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA8 | 16MHz | 7KB | 1KB |
| [Arduino Nano ATmega168](../boards/atmelavr/nanoatmega168.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA168 | 16MHz | 14KB | 1KB |
| [Arduino Nano ATmega328](../boards/atmelavr/nanoatmega328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 30KB | 2KB |
| [Arduino Nano ATmega328 (New Bootloader)](../boards/atmelavr/nanoatmega328new.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 30KB | 2KB |
| [Arduino Pro or Pro Mini ATmega168 (3.3V, 8 MHz)](../boards/atmelavr/pro8mhzatmega168.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA168 | 8MHz | 14KB | 1KB |
| [Arduino Pro or Pro Mini ATmega168 (5V, 16 MHz)](../boards/atmelavr/pro16mhzatmega168.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA168 | 16MHz | 14KB | 1KB |
| [Arduino Pro or Pro Mini ATmega328 (3.3V, 8 MHz)](../boards/atmelavr/pro8mhzatmega328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 30KB | 2KB |
| [Arduino Pro or Pro Mini ATmega328 (5V, 16 MHz)](../boards/atmelavr/pro16mhzatmega328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 30KB | 2KB |
| [Arduino Robot Control](../boards/atmelavr/robotcontrol.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [Arduino Robot Motor](../boards/atmelavr/robotmotor.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [Arduino Uno](../boards/atmelavr/uno.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Arduino Uno Mini](../boards/atmelavr/uno-mini.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Arduino Yun](../boards/atmelavr/yun.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [Arduino Yun Mini](../boards/atmelavr/yunmini.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [BQ ZUM BT-328](../boards/atmelavr/zumbt328.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 28KB | 2KB |
| [BitWizard Raspduino](../boards/atmelavr/raspduino.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 30KB | 2KB |
| [Controllino Maxi](../boards/atmelavr/controllino-maxi.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 248KB | 8KB |
| [Controllino Maxi Automation](../boards/atmelavr/controllino-maxi-automation.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 248KB | 8KB |
| [Controllino Mega](../boards/atmelavr/controllino-mega.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 248KB | 8KB |
| [Controllino Mini](../boards/atmelavr/controllino-mini.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Digispark USB](../boards/atmelavr/digispark-tiny.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATTINY85 | 16MHz | 5.87KB | 512B |
| [Engduino 3](../boards/atmelavr/engduinov3.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 8MHz | 28KB | 2.50KB |
| [EnviroDIY Mayfly](../boards/atmelavr/mayfly.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1284P | 8MHz | 127KB | 16KB |
| [FYSETC F6 V1.3](../boards/atmelavr/fysetc-f6-13.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 252KB | 8KB |
| [Generic ATtiny2313](../boards/atmelavr/attiny2313.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATTINY2313 | 8MHz | 2KB | 128B |
| [Generic ATtiny24](../boards/atmelavr/attiny24.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATTINY24 | 8MHz | 2KB | 128B |
| [Generic ATtiny25](../boards/atmelavr/attiny25.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATTINY25 | 8MHz | 2KB | 128B |
| [Generic ATtiny4313](../boards/atmelavr/attiny4313.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATTINY4313 | 8MHz | 4KB | 256B |
| [Generic ATtiny44](../boards/atmelavr/attiny44.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATTINY44 | 8MHz | 4KB | 256B |
| [Generic ATtiny45](../boards/atmelavr/attiny45.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATTINY45 | 8MHz | 4KB | 256B |
| [Generic ATtiny84](../boards/atmelavr/attiny84.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATTINY84 | 8MHz | 8KB | 512B |
| [Generic ATtiny85](../boards/atmelavr/attiny85.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATTINY85 | 8MHz | 8KB | 512B |
| [LightBlue Bean](../boards/atmelavr/lightblue-bean.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 31.50KB | 2KB |
| [LightBlue Bean+](../boards/atmelavr/lightblue-beanplus.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [LightUp](../boards/atmelavr/lightup.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 8MHz | 28KB | 2.50KB |
| [Linino One](../boards/atmelavr/one.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [LinkIt Smart 7688 Duo](../boards/atmelavr/smart7688.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 8MHz | 28KB | 2.50KB |
| [LoRa32u4II (868-915MHz)](../boards/atmelavr/lora32u4ii.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 8MHz | 28KB | 2.50KB |
| [LowPowerLab MightyHat](../boards/atmelavr/mightyhat.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31KB | 2KB |
| [LowPowerLab Moteino](../boards/atmelavr/moteino.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [LowPowerLab Moteino (8Mhz)](../boards/atmelavr/moteino8mhz.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 31.50KB | 2KB |
| [LowPowerLab MoteinoMEGA](../boards/atmelavr/moteinomega.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1284P | 16MHz | 127KB | 16KB |
| [Microduino Core (Atmega168PA@16M,5V)](../boards/atmelavr/168pa16m.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA168P | 16MHz | 15.50KB | 1KB |
| [Microduino Core (Atmega168PA@8M,3.3V)](../boards/atmelavr/168pa8m.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA168P | 8MHz | 15.50KB | 1KB |
| [Microduino Core (Atmega328P@16M,5V)](../boards/atmelavr/328p16m.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [Microduino Core (Atmega328P@8M,3.3V)](../boards/atmelavr/328p8m.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 31.50KB | 2KB |
| [Microduino Core USB (ATmega32U4@16M,5V)](../boards/atmelavr/32u416m.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [Microduino Core+ (ATmega1284P@16M,5V)](../boards/atmelavr/1284p16m.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1284P | 16MHz | 127KB | 16KB |
| [Microduino Core+ (ATmega1284P@8M,3.3V)](../boards/atmelavr/1284p8m.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1284P | 8MHz | 127KB | 16KB |
| [Microduino Core+ (Atmega644PA@16M,5V)](../boards/atmelavr/644pa16m.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA644P | 16MHz | 63KB | 4KB |
| [Microduino Core+ (Atmega644PA@8M,3.3V)](../boards/atmelavr/644pa8m.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA644P | 8MHz | 63KB | 4KB |
| [OpenEnergyMonitor emonPi](../boards/atmelavr/emonpi.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 30KB | 2KB |
| [Original Prusa i3 MK3 Multi Material 2.0 Upgrade](../boards/atmelavr/prusa-mm-control.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [PanStamp AVR](../boards/atmelavr/panstampavr.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 31.50KB | 2KB |
| [Pololu A-Star 32U4](../boards/atmelavr/a-star32u4.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [Prusa RAMBo](../boards/atmelavr/prusa-rambo.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 252KB | 8KB |
| [Quirkbot](../boards/atmelavr/quirkbot.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 8MHz | 28KB | 2.50KB |
| [RedBearLab Blend](../boards/atmelavr/blend.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [RedBearLab Blend Micro 3.3V/16MHz (overclock)](../boards/atmelavr/blendmicro16.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [RedBearLab Blend Micro 3.3V/8MHz](../boards/atmelavr/blendmicro8.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 8MHz | 28KB | 2.50KB |
| [RepRap RAMBo](../boards/atmelavr/reprap-rambo.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 252KB | 8KB |
| [SODAQ GaLoRa](../boards/atmelavr/sodaq-galora.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1284P | 8MHz | 127KB | 16KB |
| [SODAQ Mbili](../boards/atmelavr/sodaq-mbili.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1284P | 8MHz | 127KB | 16KB |
| [SODAQ Moja](../boards/atmelavr/sodaq-moja.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 31.50KB | 2KB |
| [SODAQ Ndogo](../boards/atmelavr/sodaq-ndogo.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1284P | 8MHz | 127KB | 16KB |
| [SODAQ Tatu](../boards/atmelavr/sodaq-tatu.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1284P | 8MHz | 127KB | 16KB |
| [Sanguino ATmega1284p (16MHz)](../boards/atmelavr/sanguino-atmega1284p.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1284P | 16MHz | 127KB | 16KB |
| [Sanguino ATmega1284p (8MHz)](../boards/atmelavr/sanguino-atmega1284-8m.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1284P | 8MHz | 127KB | 16KB |
| [Sanguino ATmega644 or ATmega644A (16 MHz)](../boards/atmelavr/sanguino-atmega644.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA644 | 16MHz | 63KB | 4KB |
| [Sanguino ATmega644 or ATmega644A (8 MHz)](../boards/atmelavr/sanguino-atmega644-8m.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA644 | 8MHz | 63KB | 4KB |
| [Sanguino ATmega644P or ATmega644PA (16 MHz)](../boards/atmelavr/sanguino-atmega644p.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA644P | 16MHz | 63KB | 4KB |
| [Sanguino ATmega644P or ATmega644PA (8 MHz)](../boards/atmelavr/sanguino-atmega644p-8m.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA644P | 8MHz | 63KB | 4KB |
| [Seeeduino](../boards/atmelavr/seeeduino.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [SparkFun ATmega128RFA1 Dev Board](../boards/atmelavr/sparkfun-satmega128rfa1.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA128RFA1 | 16MHz | 124KB | 16KB |
| [SparkFun Digital Sandbox](../boards/atmelavr/sparkfun-digitalsandbox.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 31.50KB | 2KB |
| [SparkFun Fio V3 3.3V/8MHz](../boards/atmelavr/sparkfun-fiov3.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 8MHz | 28KB | 2.50KB |
| [SparkFun Makey Makey](../boards/atmelavr/sparkfun-makeymakey.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [SparkFun Mega Pro 3.3V/8MHz](../boards/atmelavr/sparkfun-megapro8mhz.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 8MHz | 252KB | 8KB |
| [SparkFun Mega Pro 5V/16MHz](../boards/atmelavr/sparkfun-megapro16mhz.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 16MHz | 248KB | 8KB |
| [SparkFun Mega Pro Mini 3.3V](../boards/atmelavr/sparkfun-megamini.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA2560 | 8MHz | 252KB | 8KB |
| [SparkFun MicroView](../boards/atmelavr/uview.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [SparkFun Pro Micro 3.3V/8MHz](../boards/atmelavr/sparkfun-promicro8.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 8MHz | 28KB | 2.50KB |
| [SparkFun Pro Micro 5V/16MHz](../boards/atmelavr/sparkfun-promicro16.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [SparkFun Qduino Mini](../boards/atmelavr/sparkfun-qduinomini.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 8MHz | 28KB | 2.50KB |
| [SparkFun RedBoard](../boards/atmelavr/sparkfun-redboard.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [SparkFun Serial 7-Segment Display](../boards/atmelavr/sparkfun-serial7seg.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 31.50KB | 2KB |
| [SpellFoundry Sleepy Pi 2](../boards/atmelavr/sleepypi.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 30KB | 2KB |
| [Talk2 Whisper Node](../boards/atmelavr/whispernode.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
| [The Things Uno](../boards/atmelavr/the-things-uno.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [TinyCircuits TinyDuino Processor Board](../boards/atmelavr/tinyduino.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 30KB | 2KB |
| [TinyCircuits TinyLily Mini Processor](../boards/atmelavr/tinylily.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 8MHz | 30KB | 2KB |
| [USBasp stick](../boards/atmelavr/usbasp.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA8 | 12MHz | 8KB | 1KB |
| [Wicked Device WildFire V2](../boards/atmelavr/wildfirev2.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1284P | 16MHz | 120.00KB | 16KB |
| [Wicked Device WildFire V3](../boards/atmelavr/wildfirev3.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1284P | 16MHz | 127KB | 16KB |
| [ftDuino](../boards/atmelavr/ftduino.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA32U4 | 16MHz | 28KB | 2.50KB |
| [nicai-systems BOB3 coding bot](../boards/atmelavr/bob3.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA88 | 8MHz | 8KB | 1KB |
| [nicai-systems NIBO 2 robot](../boards/atmelavr/nibo2.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA128 | 16MHz | 128KB | 4KB |
| [nicai-systems NIBO burger robot](../boards/atmelavr/niboburger.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA16 | 15MHz | 16KB | 1KB |
| [nicai-systems NIBO burger robot with Tuning Kit](../boards/atmelavr/niboburger-1284.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1284P | 20MHz | 128KB | 16KB |
| [nicai-systems NIBObee robot](../boards/atmelavr/nibobee.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA16 | 15MHz | 16KB | 1KB |
| [nicai-systems NIBObee robot with Tuning Kit](../boards/atmelavr/nibobee-1284.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA1284P | 20MHz | 128KB | 16KB |
| [ubIQio Ardhat](../boards/atmelavr/ardhat.md) | [Atmel AVR](../platforms/atmelavr.mdx) | External | ATMEGA328P | 16MHz | 31.50KB | 2KB |
