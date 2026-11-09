---
title: "NUCLEO-8S207K8"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "NUCLEO-8S207K8 (STM8S207K8T6, 16MHz, 64KB flash, 6KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-ststm8-nucleo-8s207k8"></a>

# NUCLEO-8S207K8

## Hardware

Platform [ST STM8](../../platforms/ststm8.md): The STM8 is an 8-bit microcontroller family by STMicroelectronics an extended variant of the ST7 microcontroller architecture. STM8 microcontrollers are particularly low cost for a full-featured 8-bit microcontroller.

| Specification | Value |
|---|---|
| **Microcontroller** | STM8S207K8T6 |
| **Frequency** | 16MHz |
| **Flash** | 64KB |
| **RAM** | 6KB |
| **Vendor** | [STMicroelectronics](https://www.st.com/en/evaluation-tools/nucleo-8s207k8.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `nucleo_8s207k8` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:nucleo_8s207k8]
platform = ststm8
board = nucleo_8s207k8
```

To override a setting of the board manifest [nucleo_8s207k8.json](https://github.com/platformio/platform-ststm8/blob/master/boards/nucleo_8s207k8.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:nucleo_8s207k8]
platform = ststm8
board = nucleo_8s207k8

; change microcontroller
board_build.mcu = stm8s207k8t6

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Uploading

NUCLEO-8S207K8 supports these upload protocols:

- `serial`
- `stlinkv21`

The default is `stlinkv21`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:nucleo_8s207k8]
platform = ststm8
board = nucleo_8s207k8

upload_protocol = stlinkv21
```

## Debugging

The NUCLEO-8S207K8 has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

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
| [Standard Peripheral Library](../../frameworks/spl.mdx) | Standard Peripheral Library for ST STM32 microcontrollers |
