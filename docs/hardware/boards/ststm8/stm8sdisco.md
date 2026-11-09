---
title: "ST STM8S-DISCOVERY"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ST STM8S-DISCOVERY (STM8S105C6T6, 16MHz, 32KB flash, 2KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-ststm8-stm8sdisco"></a>

# ST STM8S-DISCOVERY

## Hardware

Platform [ST STM8](../../platforms/ststm8.md): The STM8 is an 8-bit microcontroller family by STMicroelectronics an extended variant of the ST7 microcontroller architecture. STM8 microcontrollers are particularly low cost for a full-featured 8-bit microcontroller.

| Specification | Value |
|---|---|
| **Microcontroller** | STM8S105C6T6 |
| **Frequency** | 16MHz |
| **Flash** | 32KB |
| **RAM** | 2KB |
| **Vendor** | [ST](https://www.st.com/en/evaluation-tools/stm8s-discovery.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `stm8sdisco` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:stm8sdisco]
platform = ststm8
board = stm8sdisco
```

To override a setting of the board manifest [stm8sdisco.json](https://github.com/platformio/platform-ststm8/blob/master/boards/stm8sdisco.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:stm8sdisco]
platform = ststm8
board = stm8sdisco

; change microcontroller
board_build.mcu = stm8s105c6t6

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Uploading

ST STM8S-DISCOVERY supports these upload protocols:

- `serial`
- `stlink`
- `stlinkv2`

The default is `stlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:stm8sdisco]
platform = ststm8
board = stm8sdisco

upload_protocol = stlink
```

## Debugging

The ST STM8S-DISCOVERY has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [ST-LINK](../../debug-probes/stlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Standard Peripheral Library](../../frameworks/spl.mdx) | Standard Peripheral Library for ST STM32 microcontrollers |
