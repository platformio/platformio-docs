---
title: "Raytac MDBT50Q-RX Dongle"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-nordicnrf52-raytac-mdbt50q-rx"></a>

# Raytac MDBT50Q-RX Dongle

## Hardware

Platform [Nordic nRF52](../../platforms/nordicnrf52.mdx): The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor which makes them quite capable Bluetooth Smart SoCs.

| Specification | Value |
|---|---|
| **Microcontroller** | NRF52840 |
| **Frequency** | 64MHz |
| **Flash** | 796KB |
| **RAM** | 243KB |
| **Vendor** | [Raytac](https://www.raytac.com/product/ins.php?index_id=89&utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `raytac_mdbt50q_rx` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:raytac_mdbt50q_rx]
platform = nordicnrf52
board = raytac_mdbt50q_rx
```

You can override default Raytac MDBT50Q-RX Dongle settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [raytac_mdbt50q_rx.json](https://github.com/platformio/platform-nordicnrf52/blob/master/boards/raytac_mdbt50q_rx.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:raytac_mdbt50q_rx]
platform = nordicnrf52
board = raytac_mdbt50q_rx

; change microcontroller
board_build.mcu = nrf52840

; change MCU frequency
board_build.f_cpu = 64000000L
```

## Uploading

Raytac MDBT50Q-RX Dongle supports the following uploading protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `nrfjprog`
- `nrfutil`
- `stlink`

Default protocol is `nrfutil`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:raytac_mdbt50q_rx]
platform = nordicnrf52
board = raytac_mdbt50q_rx

upload_protocol = nrfutil
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Raytac MDBT50Q-RX Dongle does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  | Yes |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
