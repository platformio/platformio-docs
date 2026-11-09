---
title: "VNG VBLUNO51"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "VNG VBLUNO51 (NRF51822, 16MHz, 128KB flash, 32KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# VNG VBLUNO51

## Hardware

Platform [Nordic nRF51](../../platforms/nordicnrf51.md): The Nordic nRF51 Series is a family of highly flexible, multi-protocol, system-on-chip (SoC) devices for ultra-low power wireless applications. nRF51 Series devices support a range of protocol stacks including Bluetooth Smart (previously called Bluetooth low energy), ANT and proprietary 2.4GHz protocols such as Gazell.

| Specification | Value |
|---|---|
| **Microcontroller** | NRF51822 |
| **Frequency** | 16MHz |
| **Flash** | 128KB |
| **RAM** | 32KB |
| **Vendor** | [VNG](https://vngiotlab.github.io/vbluno/mydoc_introduction.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `vbluno51` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:vbluno51]
platform = nordicnrf51
board = vbluno51
```

To override a setting of the board manifest [vbluno51.json](https://github.com/platformio/platform-nordicnrf51/blob/master/boards/vbluno51.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:vbluno51]
platform = nordicnrf51
board = vbluno51

; change microcontroller
board_build.mcu = nrf51822

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

The VNG VBLUNO51 has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
