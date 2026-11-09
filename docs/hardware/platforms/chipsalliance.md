---
title: "CHIPS Alliance"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-chipsalliance"></a>

# CHIPS Alliance

**Registry:** [https://registry.platformio.org/platforms/platformio/chipsalliance](https://registry.platformio.org/platforms/platformio/chipsalliance)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/chipsalliance`

The CHIPS Alliance develops high-quality, open source hardware designs relevant to silicon devices and FPGAs.

For more detailed information please visit [vendor site](https://chipsalliance.org?utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [CHIPS Alliance development platform repository](https://github.com/platformio/platform-chipsalliance/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [native-bare_c](https://github.com/platformio/platform-chipsalliance/tree/master/examples/native-bare_c?utm_source=platformio.org&utm_medium=docs)
- [rtosal-freertos](https://github.com/platformio/platform-chipsalliance/tree/master/examples/rtosal-freertos?utm_source=platformio.org&utm_medium=docs)
- [native-asm](https://github.com/platformio/platform-chipsalliance/tree/master/examples/native-asm?utm_source=platformio.org&utm_medium=docs)
- [psp-hello-world](https://github.com/platformio/platform-chipsalliance/tree/master/examples/psp-hello-world?utm_source=platformio.org&utm_medium=docs)

## Debugging

[Debugging](../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

### Tools & Debug Probes

Supported debugging tools are listed in "Debug" column. For more detailed information, please scroll table by horizontal. You can switch between debugging [Tools & Debug Probes](../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md).

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions.

:::

#### On-Board Debug Tools

Boards listed below have on-board debug probe and **ARE READY** for debugging! You do not need to use/buy external debug probe.

| Name | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|
| [RVfpga: Digilent Nexys A7](../boards/chipsalliance/swervolf-nexys.md) |  | 320MHz | 16MB | 1.16MB |

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-chipsalliance/releases) of CHIPS Alliance development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

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

**Linux Users**:

- Install "udev" rules [99-platformio-udev.rules](../../get-started/install/udev-rules.md)
- Raspberry Pi users, please read this article [Enable serial port on Raspberry Pi](https://hallard.me/enable-serial-port-on-raspberry-pi/).

**Windows Users:**

Please check that you have a correctly installed USB driver from board manufacturer

:::

## Frameworks

| Name | Description |
|---|---|
| [FreeRTOS](../frameworks/freertos.md) | FreeRTOS is a real-time operating system kernel for embedded devices that has been ported to 40 microcontroller platforms. |
| [WD-Firmware](../frameworks/wd-riscv-sdk.md) | The WD Firmware package contains Firmware applications and Processor Support Package (PSP) for various cores, alongside demos which support all features. |

## Boards

:::note

- You can list pre-configured boards by [pio boards](../../reference/cli/pio-boards.md) command
- For more detailed `board` information please scroll the tables below by horizontally.

:::

### Digilent

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [RVfpga: Digilent Nexys A7](../boards/chipsalliance/swervolf-nexys.md) | On-board |  | 320MHz | 16MB | 1.16MB |
