---
title: "Shakti"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-shakti"></a>

# Shakti

**Registry:** [https://registry.platformio.org/platforms/platformio/shakti](https://registry.platformio.org/platforms/platformio/shakti)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/shakti`

Shakti is an open-source initiative by the RISE group at IIT-Madras, which is not only building open source, production grade processors, but also associated components like interconnect fabrics, verification tools, storage controllers, peripheral IPs and SOC tools.

For more detailed information please visit [vendor site](https://shakti.org.in/?utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [Shakti development platform repository](https://github.com/platformio/platform-shakti/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [shakti-sdk_gpio-keypad](https://github.com/platformio/platform-shakti/tree/master/examples/shakti-sdk_gpio-keypad?utm_source=platformio.org&utm_medium=docs)
- [shakti-sdk_i2c-lm75](https://github.com/platformio/platform-shakti/tree/master/examples/shakti-sdk_i2c-lm75?utm_source=platformio.org&utm_medium=docs)
- [shakti-sdk_uart-hello](https://github.com/platformio/platform-shakti/tree/master/examples/shakti-sdk_uart-hello?utm_source=platformio.org&utm_medium=docs)
- [shakti-sdk_weatherstation](https://github.com/platformio/platform-shakti/tree/master/examples/shakti-sdk_weatherstation?utm_source=platformio.org&utm_medium=docs)

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
| [Artix-7 35T Arty FPGA Evaluation Kit](../boards/shakti/artix7-35t.md) | E-CLASS | 50MHz | 0B | 128KB |
| [Arty A7-100: Artix-7 FPGA Development Board](../boards/shakti/artix7-100t.md) | C-CLASS | 50MHz | 0B | 128MB |
| [Parashu on Artix-7 100T Arty FPGA Evaluation Kit](../boards/shakti/parashu.md) | E-CLASS | 50MHz | 0B | 128KB |
| [Pinaka on Artix-7 35T Arty FPGA Evaluation Kit](../boards/shakti/pinaka.md) | E-CLASS | 50MHz | 0B | 128KB |
| [Vajra on Arty A7-100: Artix-7 FPGA Development Board](../boards/shakti/vajra.md) | C-CLASS | 50MHz | 0B | 128MB |

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-shakti/releases) of Shakti development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

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

**Linux Users**:

- Install "udev" rules [99-platformio-udev.rules](../../get-started/install/udev-rules.md)
- Raspberry Pi users, please read this article [Enable serial port on Raspberry Pi](https://hallard.me/enable-serial-port-on-raspberry-pi/).

**Windows Users:**

Please check that you have a correctly installed USB driver from board manufacturer

:::

## Frameworks

| Name | Description |
|---|---|
| [Shakti SDK](../frameworks/shakti-sdk.md) | A software development kit for developing applications on Shakti class of processors |

## Boards

:::note

- You can list pre-configured boards by [pio boards](../../reference/cli/pio-boards.md) command
- For more detailed `board` information please scroll the tables below by horizontally.

:::

### Xilinx

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Artix-7 35T Arty FPGA Evaluation Kit](../boards/shakti/artix7-35t.md) | On-board | E-CLASS | 50MHz | 0B | 128KB |
| [Arty A7-100: Artix-7 FPGA Development Board](../boards/shakti/artix7-100t.md) | On-board | C-CLASS | 50MHz | 0B | 128MB |
| [Parashu on Artix-7 100T Arty FPGA Evaluation Kit](../boards/shakti/parashu.md) | On-board | E-CLASS | 50MHz | 0B | 128KB |
| [Pinaka on Artix-7 35T Arty FPGA Evaluation Kit](../boards/shakti/pinaka.md) | On-board | E-CLASS | 50MHz | 0B | 128KB |
| [Vajra on Arty A7-100: Artix-7 FPGA Development Board](../boards/shakti/vajra.md) | On-board | C-CLASS | 50MHz | 0B | 128MB |
