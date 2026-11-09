---
title: "Raspberry Pi Pico"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Raspberry Pi Pico (RP2040, 133MHz, 2MB flash, 264KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Raspberry Pi Pico

## Hardware

Platform [Raspberry Pi RP2040](../../platforms/raspberrypi.md): RP2040 is a low-cost, high-performance microcontroller device with a large on-chip memory, symmetric dual-core processor complex, and rich peripheral.

| Specification | Value |
|---|---|
| **Microcontroller** | RP2040 |
| **Frequency** | 133MHz |
| **Flash** | 2MB |
| **RAM** | 264KB |
| **Vendor** | [Raspberry Pi](https://www.raspberrypi.org/products/raspberry-pi-pico/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `pico` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:pico]
platform = raspberrypi
board = pico
```

To override a setting of the board manifest [pico.json](https://github.com/platformio/platform-raspberrypi/blob/master/boards/pico.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:pico]
platform = raspberrypi
board = pico

; change microcontroller
board_build.mcu = rp2040

; change MCU frequency
board_build.f_cpu = 133000000L
```

## Uploading

Raspberry Pi Pico supports these upload protocols:

- `cmsis-dap`
- `jlink`
- `picotool`
- `raspberrypi-swd`

The default is `picotool`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:pico]
platform = raspberrypi
board = pico

upload_protocol = picotool
```

## Debugging

The Raspberry Pi Pico has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [Raspberry pi SWD](../../debug-probes/raspberrypi-swd.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
