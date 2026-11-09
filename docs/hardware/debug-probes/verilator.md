---
description: "Use the Verilator debug probe with PlatformIO: configuration, drivers, wiring and supported boards."
---

# Verilator

[![](./img/verilator.png)](https://www.veripool.org/wiki/verilator/?utm_source=platformio&utm_medium=docs)

Verilator is a free and open-source software tool which converts Verilog to a cycle-accurate behavioral model in C++ or SystemC. See the [official documentation](https://www.veripool.org/wiki/verilator/?utm_source=platformio&utm_medium=docs).

## Configuration {#configuration}

Select this probe with the [`debug_tool`](../../reference/platformio-ini/env/debug-tool.md) option in [`platformio.ini`](../../reference/platformio-ini/index.md):

```ini
[env:myenv]
platform = ...
board = ...
debug_tool = verilator
```

See also:

- [Debugging options](../../reference/platformio-ini/env/debug-options.md)

<!-- begin_platforms -->

## Platforms

| Name | Description |
|---|---|
| [CHIPS Alliance](../platforms/chipsalliance.md) | The CHIPS Alliance develops high-quality, open source hardware designs relevant to silicon devices and FPGAs. |

## Frameworks

| Name | Description |
|---|---|
| [FreeRTOS](../frameworks/freertos.md) | FreeRTOS is a real-time operating system kernel for embedded devices that has been ported to 40 microcontroller platforms. |
| [WD-Firmware](../frameworks/wd-riscv-sdk.md) | The WD Firmware package contains Firmware applications and Processor Support Package (PSP) for various cores, alongside demos which support all features. |

## Boards

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [RVfpga: Digilent Nexys A7](../boards/chipsalliance/swervolf-nexys.md) | [CHIPS Alliance](../platforms/chipsalliance.md) | On-board |  | 320MHz | 16MB | 1.16MB |
