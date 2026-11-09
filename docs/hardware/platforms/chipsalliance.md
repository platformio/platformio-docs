---
title: "CHIPS Alliance"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The CHIPS Alliance development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

# CHIPS Alliance

**Registry:** [https://registry.platformio.org/platforms/platformio/chipsalliance](https://registry.platformio.org/platforms/platformio/chipsalliance)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/chipsalliance`

The CHIPS Alliance develops high-quality, open source hardware designs relevant to silicon devices and FPGAs.

Vendor website: [chipsalliance.org](https://chipsalliance.org?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [CHIPS Alliance platform repository](https://github.com/platformio/platform-chipsalliance/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [native-bare_c](https://github.com/platformio/platform-chipsalliance/tree/master/examples/native-bare_c?utm_source=platformio.org&utm_medium=docs)
- [rtosal-freertos](https://github.com/platformio/platform-chipsalliance/tree/master/examples/rtosal-freertos?utm_source=platformio.org&utm_medium=docs)
- [native-asm](https://github.com/platformio/platform-chipsalliance/tree/master/examples/native-asm?utm_source=platformio.org&utm_medium=docs)
- [psp-hello-world](https://github.com/platformio/platform-chipsalliance/tree/master/examples/psp-hello-world?utm_source=platformio.org&utm_medium=docs)

## Debugging

[Debugging](../../guides/debugging/index.md) works with the boards below without extra configuration.

### Debug probes

Select a [debug probe](../../guides/debugging/index.md#debugging-tools) with the [debug_tool](../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../reference/platformio-ini/index.md). Each board's page lists its compatible probes.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

#### Boards with an on-board debug probe

These boards are ready for debugging; no external probe is needed.

| Name | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|
| [RVfpga: Digilent Nexys A7](../boards/chipsalliance/swervolf-nexys.md) |  | 320MHz | 16MB | 1.16MB |

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-chipsalliance/releases) of the CHIPS Alliance platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = chipsalliance
board = ...

; Specific version
[env:custom_stable]
platform = chipsalliance@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-chipsalliance.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [framework-wd-riscv-sdk](https://registry.platformio.org/tools/platformio/framework-wd-riscv-sdk) | The WD Firmware package contains Firmware applications and Processor Support Package (PSP) for various cores, alongside demos which support all features. |
| [tool-openocd-riscv-chipsalliance](https://registry.platformio.org/tools/platformio/tool-openocd-riscv-chipsalliance) | Fork of Open On-Chip Debugger that has RISC-V support and enabled VPI JTAG |
| [tool-verilator-swervolf](https://registry.platformio.org/tools/platformio/tool-verilator-swervolf) | Verilator is an open-source SystemVerilog simulator and lint system |
| [tool-whisper](https://registry.platformio.org/tools/platformio/tool-whisper) | Whisper is a RISCV instruction set simulator (ISS) developed for the verification of the Swerv micro-controller. It allows the user to run RISC-V code without RISC-V hardware |
| [toolchain-riscv](https://registry.platformio.org/tools/platformio/toolchain-riscv) | GNU toolchain for RISC-V, including GCC |

:::warning

**Linux:**

- Install the [udev rules](../../get-started/install/udev-rules.md).
- On a Raspberry Pi, [enable the serial port](https://hallard.me/enable-serial-port-on-raspberry-pi/).

**Windows:**

Install the USB driver from the board manufacturer, if needed.

:::

## Frameworks

| Name | Description |
|---|---|
| [FreeRTOS](../frameworks/freertos.md) | FreeRTOS is a real-time operating system kernel for embedded devices that has been ported to 40 microcontroller platforms. |
| [WD-Firmware](../frameworks/wd-riscv-sdk.md) | The WD Firmware package contains Firmware applications and Processor Support Package (PSP) for various cores, alongside demos which support all features. |

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### Digilent

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [RVfpga: Digilent Nexys A7](../boards/chipsalliance/swervolf-nexys.md) | On-board |  | 320MHz | 16MB | 1.16MB |
