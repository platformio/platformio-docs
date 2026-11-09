---
title: "ItsyBitsy nRF52840 Express"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-nordicnrf52-adafruit-itsybitsy-nrf52840"></a>

# ItsyBitsy nRF52840 Express

## Hardware

Platform [Nordic nRF52](../../platforms/nordicnrf52.mdx): The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor which makes them quite capable Bluetooth Smart SoCs.

| Specification | Value |
|---|---|
| **Microcontroller** | NRF52840 |
| **Frequency** | 64MHz |
| **Flash** | 796KB |
| **RAM** | 243KB |
| **Vendor** | [Adafruit](https://www.adafruit.com/product/4062?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `adafruit_itsybitsy_nrf52840` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:adafruit_itsybitsy_nrf52840]
platform = nordicnrf52
board = adafruit_itsybitsy_nrf52840
```

You can override default ItsyBitsy nRF52840 Express settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [adafruit_itsybitsy_nrf52840.json](https://github.com/platformio/platform-nordicnrf52/blob/master/boards/adafruit_itsybitsy_nrf52840.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:adafruit_itsybitsy_nrf52840]
platform = nordicnrf52
board = adafruit_itsybitsy_nrf52840

; change microcontroller
board_build.mcu = nrf52840

; change MCU frequency
board_build.f_cpu = 64000000L
```

## Uploading

ItsyBitsy nRF52840 Express supports the following uploading protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `nrfjprog`
- `nrfutil`
- `stlink`

Default protocol is `nrfutil`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:adafruit_itsybitsy_nrf52840]
platform = nordicnrf52
board = adafruit_itsybitsy_nrf52840

upload_protocol = nrfutil
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

ItsyBitsy nRF52840 Express does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

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
