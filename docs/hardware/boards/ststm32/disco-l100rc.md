---
title: "ST 32L100DISCOVERY"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm32-disco-l100rc"></a>

# ST 32L100DISCOVERY

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32L100RCT6 |
| **Frequency** | 32MHz |
| **Flash** | 256KB |
| **RAM** | 16KB |
| **Vendor** | [ST](https://www.st.com/en/evaluation-tools/32l100cdiscovery.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `disco_l100rc` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:disco_l100rc]
platform = ststm32
board = disco_l100rc
```

You can override default ST 32L100DISCOVERY settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [disco_l100rc.json](https://github.com/platformio/platform-ststm32/blob/master/boards/disco_l100rc.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:disco_l100rc]
platform = ststm32
board = disco_l100rc

; change microcontroller
board_build.mcu = stm32l100rct6

; change MCU frequency
board_build.f_cpu = 32000000L
```

## Uploading

ST 32L100DISCOVERY supports the following uploading protocols:

- `blackmagic`
- `jlink`
- `stlink`

Default protocol is `stlink`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:disco_l100rc]
platform = ststm32
board = disco_l100rc

upload_protocol = stlink
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

ST 32L100DISCOVERY has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [LibOpenCM3](../../frameworks/libopencm3.md) | The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers. |
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
