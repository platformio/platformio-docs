---
title: "Artix-7 35T Arty FPGA Evaluation Kit"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-shakti-artix7-35t"></a>

# Artix-7 35T Arty FPGA Evaluation Kit

## Hardware

Platform [Shakti](../../platforms/shakti.md): Shakti is an open-source initiative by the RISE group at IIT-Madras, which is not only building open source, production grade processors, but also associated components like interconnect fabrics, verification tools, storage controllers, peripheral IPs and SOC tools.

| Specification | Value |
|---|---|
| **Microcontroller** | E-CLASS |
| **Frequency** | 50MHz |
| **Flash** | 0B |
| **RAM** | 128KB |
| **Vendor** | [Xilinx](https://www.xilinx.com/products/boards-and-kits/arty.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `artix7_35t` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:artix7_35t]
platform = shakti
board = artix7_35t
```

You can override default Artix-7 35T Arty FPGA Evaluation Kit settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [artix7_35t.json](https://github.com/platformio/platform-shakti/blob/master/boards/artix7_35t.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:artix7_35t]
platform = shakti
board = artix7_35t

; change microcontroller
board_build.mcu = E-Class

; change MCU frequency
board_build.f_cpu = 50000000L
```

## Uploading

Artix-7 35T Arty FPGA Evaluation Kit supports the following uploading protocols:

- `ftdi`
- `ftdi`
- `jlink`
- `jlink`

Default protocol is `ftdi`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:artix7_35t]
platform = shakti
board = artix7_35t

upload_protocol = ftdi
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Artix-7 35T Arty FPGA Evaluation Kit has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [FTDI Chip](../../debug-probes/ftdi.md) | Yes | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Shakti SDK](../../frameworks/shakti-sdk.md) | A software development kit for developing applications on Shakti class of processors |
