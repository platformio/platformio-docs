---
description: List the boards PlatformIO supports, filtered by ID, name, MCU, vendor, platform or framework.
---

<a id="cmd-boards"></a>

# pio boards {#pio-boards}

List the boards PlatformIO supports, with their board IDs. Use a board ID in
the [`board`](../platformio-ini/env/board.md) option of `platformio.ini` and in
[`pio project init --board`](./pio-project/init.md).

## Usage {#usage}

```bash
pio boards [OPTIONS] [QUERY]
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `QUERY` | Optional. Show only the boards whose ID, name, MCU, vendor, development platform or frameworks contain this text (case-insensitive). |

Boards are grouped by development platform. You can also browse them in the
[boards catalog](/hardware/boards).

## Options {#options}

### `--installed` {#cmdoption-pio-boards-installed}

List only the boards of installed development platforms.

### `--json-output` {#cmdoption-pio-boards-json-output}

Print the result in [JSON](https://en.wikipedia.org/wiki/JSON) format.

## Examples {#examples}

List the boards with an ATmega168 MCU:

```bash
pio boards atmega168
```

```text
Platform: atmelavr
================================================================================
ID                  MCU          Frequency    Flash    RAM    Name
------------------  -----------  -----------  -------  -----  -----------------------------------------------
ATmega168           ATMEGA168    16MHz        16KB     1KB    ATmega168/A
ATmega168P          ATMEGA168P   16MHz        16KB     1KB    ATmega168P/PA
ATmega168PB         ATMEGA168PB  16MHz        16KB     1KB    ATmega168PB
btatmega168         ATMEGA168    16MHz        14KB     1KB    Arduino BT ATmega168
diecimilaatmega168  ATMEGA168    16MHz        14KB     1KB    Arduino Duemilanove or Diecimila ATmega168
lilypadatmega168    ATMEGA168    8MHz         14KB     1KB    Arduino LilyPad ATmega168
miniatmega168       ATMEGA168    16MHz        14KB     1KB    Arduino Mini ATmega168
...
```

List the boards of the [TI MSP430](/hardware/platforms/timsp430) development
platform:

```bash
pio boards timsp430
```

```text
Platform: timsp430
================================================================================
ID              MCU           Frequency    Flash    RAM    Name
--------------  ------------  -----------  -------  -----  ----------------------------------------
lpmsp430fr5739  MSP430FR5739  16MHz        15.37KB  1KB    TI FraunchPad MSP-EXP430FR5739LP
lpmsp430f5529   MSP430F5529   25MHz        47KB     8KB    TI LaunchPad MSP-EXP430F5529LP
lpmsp430fr2311  MSP430FR2311  16MHz        3.75KB   1KB    TI LaunchPad MSP-EXP430FR2311LP
lpmsp430fr2355  MSP430FR2355  16MHz        32KB     4KB    TI LaunchPad MSP-EXP430FR2355LP
...
```

List every board that supports the Mbed framework, across all platforms:

```bash
pio boards mbed
```
