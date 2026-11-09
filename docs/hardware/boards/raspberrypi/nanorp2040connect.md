---
title: "Arduino Nano RP2040 Connect"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-raspberrypi-nanorp2040connect"></a>

# Arduino Nano RP2040 Connect

## Hardware

Platform [Raspberry Pi RP2040](../../platforms/raspberrypi.md): RP2040 is a low-cost, high-performance microcontroller device with a large on-chip memory, symmetric dual-core processor complex, and rich peripheral.

| Specification | Value |
|---|---|
| **Microcontroller** | RP2040 |
| **Frequency** | 133MHz |
| **Flash** | 2MB |
| **RAM** | 264KB |
| **Vendor** | [Arduino](https://blog.arduino.cc/2021/01/20/welcome-raspberry-pi-to-the-world-of-microcontrollers/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `nanorp2040connect` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:nanorp2040connect]
platform = raspberrypi
board = nanorp2040connect
```

You can override default Arduino Nano RP2040 Connect settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [nanorp2040connect.json](https://github.com/platformio/platform-raspberrypi/blob/master/boards/nanorp2040connect.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:nanorp2040connect]
platform = raspberrypi
board = nanorp2040connect

; change microcontroller
board_build.mcu = rp2040

; change MCU frequency
board_build.f_cpu = 133000000L
```

## Uploading

Arduino Nano RP2040 Connect supports the following uploading protocols:

- `cmsis-dap`
- `jlink`
- `picotool`
- `raspberrypi-swd`

Default protocol is `picotool`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:nanorp2040connect]
platform = raspberrypi
board = nanorp2040connect

upload_protocol = picotool
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Arduino Nano RP2040 Connect does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [Raspberry Pi SWD](../../debug-probes/raspberrypi-swd.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
