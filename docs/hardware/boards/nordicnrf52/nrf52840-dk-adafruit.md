---
title: "Nordic nRF52840-DK (Adafruit BSP)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-nordicnrf52-nrf52840-dk-adafruit"></a>

# Nordic nRF52840-DK (Adafruit BSP)

## Hardware

Platform [Nordic nRF52](../../platforms/nordicnrf52.mdx): The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor which makes them quite capable Bluetooth Smart SoCs.

| Specification | Value |
|---|---|
| **Microcontroller** | NRF52840 |
| **Frequency** | 64MHz |
| **Flash** | 796KB |
| **RAM** | 243KB |
| **Vendor** | [Nordic](https://os.mbed.com/platforms/Nordic-nRF52840-DK/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `nrf52840_dk_adafruit` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:nrf52840_dk_adafruit]
platform = nordicnrf52
board = nrf52840_dk_adafruit
```

You can override default Nordic nRF52840-DK (Adafruit BSP) settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [nrf52840_dk_adafruit.json](https://github.com/platformio/platform-nordicnrf52/blob/master/boards/nrf52840_dk_adafruit.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:nrf52840_dk_adafruit]
platform = nordicnrf52
board = nrf52840_dk_adafruit

; change microcontroller
board_build.mcu = nrf52840

; change MCU frequency
board_build.f_cpu = 64000000L
```

## Uploading

Nordic nRF52840-DK (Adafruit BSP) supports the following uploading protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `nrfjprog`
- `stlink`

Default protocol is `jlink`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:nrf52840_dk_adafruit]
platform = nordicnrf52
board = nrf52840_dk_adafruit

upload_protocol = jlink
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Nordic nRF52840-DK (Adafruit BSP) has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  |  |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) | Yes | Yes |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
