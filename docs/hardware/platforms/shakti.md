---
title: "Shakti"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The Shakti development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

# Shakti

**Registry:** [https://registry.platformio.org/platforms/platformio/shakti](https://registry.platformio.org/platforms/platformio/shakti)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/shakti`

Shakti is an open-source initiative by the RISE group at IIT-Madras, which is not only building open source, production grade processors, but also associated components like interconnect fabrics, verification tools, storage controllers, peripheral IPs and SOC tools.

Vendor website: [shakti.org.in](https://shakti.org.in/?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [Shakti platform repository](https://github.com/platformio/platform-shakti/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [shakti-sdk_gpio-keypad](https://github.com/platformio/platform-shakti/tree/master/examples/shakti-sdk_gpio-keypad?utm_source=platformio.org&utm_medium=docs)
- [shakti-sdk_i2c-lm75](https://github.com/platformio/platform-shakti/tree/master/examples/shakti-sdk_i2c-lm75?utm_source=platformio.org&utm_medium=docs)
- [shakti-sdk_uart-hello](https://github.com/platformio/platform-shakti/tree/master/examples/shakti-sdk_uart-hello?utm_source=platformio.org&utm_medium=docs)
- [shakti-sdk_weatherstation](https://github.com/platformio/platform-shakti/tree/master/examples/shakti-sdk_weatherstation?utm_source=platformio.org&utm_medium=docs)

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
| [Artix-7 35T Arty FPGA Evaluation Kit](../boards/shakti/artix7-35t.md) | E-CLASS | 50MHz | 0B | 128KB |
| [Arty A7-100: Artix-7 FPGA Development Board](../boards/shakti/artix7-100t.md) | C-CLASS | 50MHz | 0B | 128MB |
| [Parashu on Artix-7 100T Arty FPGA Evaluation Kit](../boards/shakti/parashu.md) | E-CLASS | 50MHz | 0B | 128KB |
| [Pinaka on Artix-7 35T Arty FPGA Evaluation Kit](../boards/shakti/pinaka.md) | E-CLASS | 50MHz | 0B | 128KB |
| [Vajra on Arty A7-100: Artix-7 FPGA Development Board](../boards/shakti/vajra.md) | C-CLASS | 50MHz | 0B | 128MB |

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-shakti/releases) of the Shakti platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = shakti
board = ...

; Specific version
[env:custom_stable]
platform = shakti@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-shakti.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [framework-shakti-sdk](https://registry.platformio.org/tools/platformio/framework-shakti-sdk) | A software development kit for developing applications on Shakti class of processors |
| [tool-jlink](https://registry.platformio.org/tools/platformio/tool-jlink) | Software and Documentation Pack for SEGGER J-Link debug probes |
| [tool-openocd-riscv](https://registry.platformio.org/tools/platformio/tool-openocd-riscv) | Fork of Open On-Chip Debugger that has RISC-V support |
| [tool-qemu-riscv](https://registry.platformio.org/tools/platformio/tool-qemu-riscv) | QEMU is a generic and open source machine emulator and virtualizer |
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
| [Shakti SDK](../frameworks/shakti-sdk.md) | A software development kit for developing applications on Shakti class of processors |

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### Xilinx

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Artix-7 35T Arty FPGA Evaluation Kit](../boards/shakti/artix7-35t.md) | On-board | E-CLASS | 50MHz | 0B | 128KB |
| [Arty A7-100: Artix-7 FPGA Development Board](../boards/shakti/artix7-100t.md) | On-board | C-CLASS | 50MHz | 0B | 128MB |
| [Parashu on Artix-7 100T Arty FPGA Evaluation Kit](../boards/shakti/parashu.md) | On-board | E-CLASS | 50MHz | 0B | 128KB |
| [Pinaka on Artix-7 35T Arty FPGA Evaluation Kit](../boards/shakti/pinaka.md) | On-board | E-CLASS | 50MHz | 0B | 128KB |
| [Vajra on Arty A7-100: Artix-7 FPGA Development Board](../boards/shakti/vajra.md) | On-board | C-CLASS | 50MHz | 0B | 128MB |
