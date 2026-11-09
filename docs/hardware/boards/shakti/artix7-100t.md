---
title: "Arty A7-100: Artix-7 FPGA Development Board"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-shakti-artix7-100t"></a>

# Arty A7-100: Artix-7 FPGA Development Board

## Hardware

Platform [Shakti](../../platforms/shakti.md): Shakti is an open-source initiative by the RISE group at IIT-Madras, which is not only building open source, production grade processors, but also associated components like interconnect fabrics, verification tools, storage controllers, peripheral IPs and SOC tools.

| Specification | Value |
|---|---|
| **Microcontroller** | C-CLASS |
| **Frequency** | 50MHz |
| **Flash** | 0B |
| **RAM** | 128MB |
| **Vendor** | [Xilinx](https://www.xilinx.com/products/boards-and-kits/1-w51quh.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `artix7_100t` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:artix7_100t]
platform = shakti
board = artix7_100t
```

You can override default Arty A7-100: Artix-7 FPGA Development Board settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [artix7_100t.json](https://github.com/platformio/platform-shakti/blob/master/boards/artix7_100t.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:artix7_100t]
platform = shakti
board = artix7_100t

; change microcontroller
board_build.mcu = C-Class

; change MCU frequency
board_build.f_cpu = 50000000L
```

## Uploading

Arty A7-100: Artix-7 FPGA Development Board supports the following uploading protocols:

- `ftdi`
- `ftdi`
- `jlink`
- `jlink`

Default protocol is `ftdi`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:artix7_100t]
platform = shakti
board = artix7_100t

upload_protocol = ftdi
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Arty A7-100: Artix-7 FPGA Development Board has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [FTDI Chip](../../debug-probes/ftdi.md) | Yes | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Shakti SDK](../../frameworks/shakti-sdk.md) | A software development kit for developing applications on Shakti class of processors |
