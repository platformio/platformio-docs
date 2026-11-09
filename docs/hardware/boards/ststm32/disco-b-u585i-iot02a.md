---
title: "ST B-U585I-IOT02A Discovery"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm32-disco-b-u585i-iot02a"></a>

# ST B-U585I-IOT02A Discovery

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32U585AII6Q |
| **Frequency** | 160MHz |
| **Flash** | 2MB |
| **RAM** | 256KB |
| **Vendor** | [ST](https://www.st.com/en/evaluation-tools/b-u585i-iot02a.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `disco_b_u585i_iot02a` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:disco_b_u585i_iot02a]
platform = ststm32
board = disco_b_u585i_iot02a
```

You can override default ST B-U585I-IOT02A Discovery settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [disco_b_u585i_iot02a.json](https://github.com/platformio/platform-ststm32/blob/master/boards/disco_b_u585i_iot02a.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:disco_b_u585i_iot02a]
platform = ststm32
board = disco_b_u585i_iot02a

; change microcontroller
board_build.mcu = stm32u585aii6q

; change MCU frequency
board_build.f_cpu = 160000000L
```

## Uploading

ST B-U585I-IOT02A Discovery supports the following uploading protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `mbed`
- `stlink`

Default protocol is `stlink`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:disco_b_u585i_iot02a]
platform = ststm32
board = disco_b_u585i_iot02a

upload_protocol = stlink
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

ST B-U585I-IOT02A Discovery has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

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
