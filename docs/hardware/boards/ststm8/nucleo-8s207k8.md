---
title: "NUCLEO-8S207K8"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
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

Please use `nucleo_8s207k8` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:nucleo_8s207k8]
platform = ststm8
board = nucleo_8s207k8
```

You can override default NUCLEO-8S207K8 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [nucleo_8s207k8.json](https://github.com/platformio/platform-ststm8/blob/master/boards/nucleo_8s207k8.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

NUCLEO-8S207K8 supports the following uploading protocols:

- `serial`
- `stlinkv21`

Default protocol is `stlinkv21`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:nucleo_8s207k8]
platform = ststm8
board = nucleo_8s207k8

upload_protocol = stlinkv21
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

NUCLEO-8S207K8 has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [ST-LINK](../../debug-probes/stlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Standard Peripheral Library](../../frameworks/spl.mdx) | Standard Peripheral Library for ST STM32 microcontrollers |
