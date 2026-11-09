---
description: "Use the Whisper debug probe with PlatformIO: configuration, drivers, wiring and supported boards."
---

<a id="debugging-tool-whisper"></a>

# Whisper {#whisper}

Whisper is a RISCV instruction set simulator (ISS) developed for the verification of the Swerv micro-controller. It allows the user to run RISCV code without RISCV hardware. It has an interactive mode where the user can single step the target RISCV code and inspect/modify the RISCV registers or the simulated system memory. It can also run in lock step with a Verilog simulator serving as a "golden model" against which an implementation is checked after each instruction of a test program. See the [official documentation](https://github.com/westerndigitalcorporation/swerv-ISS/?utm_source=platformio&utm_medium=docs).

## Configuration {#configuration}

Select this probe with the [`debug_tool`](../../reference/platformio-ini/env/debug-tool.md) option in [`platformio.ini`](../../reference/platformio-ini/index.md):

```ini
[env:myenv]
platform = ...
board = ...
debug_tool = whisper
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
