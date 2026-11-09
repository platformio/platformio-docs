---
title: "NXP i.MX RT1015 Evaluation Kit"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-nxpimxrt-mimxrt1015-evk"></a>

# NXP i.MX RT1015 Evaluation Kit

## Hardware

Platform [NXP i.MX RT](../../platforms/nxpimxrt.md): The i.MX RT series of crossover processors features the Arm Cortex-M core, real-time functionality and MCU usability at a cost-effective price.

| Specification | Value |
|---|---|
| **Microcontroller** | MIMXRT1015DAF5A |
| **Frequency** | 500MHz |
| **Flash** | 96KB |
| **RAM** | 128KB |
| **Vendor** | [NXP](https://www.nxp.com/design/development-boards/i.mx-evaluation-and-development-boards/i.mx-rt1015-evaluation-kit:MIMXRT1015-EVK?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `mimxrt1015_evk` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:mimxrt1015_evk]
platform = nxpimxrt
board = mimxrt1015_evk
```

You can override default NXP i.MX RT1015 Evaluation Kit settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [mimxrt1015_evk.json](https://github.com/platformio/platform-nxpimxrt/blob/master/boards/mimxrt1015_evk.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:mimxrt1015_evk]
platform = nxpimxrt
board = mimxrt1015_evk

; change microcontroller
board_build.mcu = mimxrt1015daf5a

; change MCU frequency
board_build.f_cpu = 500000000L
```

## Uploading

NXP i.MX RT1015 Evaluation Kit supports the following uploading protocols:

- `blackmagic`
- `jlink`
- `mbed`

Default protocol is `mbed`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:mimxrt1015_evk]
platform = nxpimxrt
board = mimxrt1015_evk

upload_protocol = mbed
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

NXP i.MX RT1015 Evaluation Kit has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
