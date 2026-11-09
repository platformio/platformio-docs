---
title: "P-Nucleo WB55RG"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm32-nucleo-wb55rg-p"></a>

# P-Nucleo WB55RG

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32WB55RG |
| **Frequency** | 64MHz |
| **Flash** | 512KB |
| **RAM** | 192KB |
| **Vendor** | [ST](https://www.st.com/en/evaluation-tools/p-nucleo-wb55.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `nucleo_wb55rg_p` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:nucleo_wb55rg_p]
platform = ststm32
board = nucleo_wb55rg_p
```

You can override default P-Nucleo WB55RG settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [nucleo_wb55rg_p.json](https://github.com/platformio/platform-ststm32/blob/master/boards/nucleo_wb55rg_p.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:nucleo_wb55rg_p]
platform = ststm32
board = nucleo_wb55rg_p

; change microcontroller
board_build.mcu = stm32wb55rg

; change MCU frequency
board_build.f_cpu = 64000000L
```

## Uploading

P-Nucleo WB55RG supports the following uploading protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `stlink`

Default protocol is `stlink`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:nucleo_wb55rg_p]
platform = ststm32
board = nucleo_wb55rg_p

upload_protocol = stlink
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

P-Nucleo WB55RG has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  |  |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
