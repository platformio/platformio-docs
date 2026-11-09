---
title: "Original Prusa i3 MK3 Multi Material 2.0 Upgrade"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Original Prusa i3 MK3 Multi Material 2.0 Upgrade (ATMEGA32U4, 16MHz, 28KB flash, 2.50KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-prusa-mm-control"></a>

# Original Prusa i3 MK3 Multi Material 2.0 Upgrade

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA32U4 |
| **Frequency** | 16MHz |
| **Flash** | 28KB |
| **RAM** | 2.50KB |
| **Vendor** | [Prusa 3D](https://shop.prusa3d.com/en/upgrades/183-original-prusa-i3-mk25smk3s-multi-material-2s-upgrade-kit-mmu2s.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `prusa_mm_control` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:prusa_mm_control]
platform = atmelavr
board = prusa_mm_control
```

To override a setting of the board manifest [prusa_mm_control.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/prusa_mm_control.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:prusa_mm_control]
platform = atmelavr
board = prusa_mm_control

; change microcontroller
board_build.mcu = atmega32u4

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

The Original Prusa i3 MK3 Multi Material 2.0 Upgrade has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [simavr](../../debug-probes/simavr.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
