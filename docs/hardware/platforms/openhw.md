---
title: "OpenHW Group"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The OpenHW Group development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

# OpenHW Group

**Registry:** [https://registry.platformio.org/platforms/platformio/openhw](https://registry.platformio.org/platforms/platformio/openhw)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/openhw`

OpenHW Group is a not-for-profit, global organization that provides an infrastructure for hosting high quality open-source HW developments in line with industry best practices. The OpenHW CV32E40P RISC-V core is the first open-source core for high-volume chips verified with the state-of-the-art process required for high-integrity, commercial SoCs.

Vendor website: [www.openhwgroup.org](https://www.openhwgroup.org/?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [OpenHW Group platform repository](https://github.com/platformio/platform-openhw/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [pulp-sdk-asm](https://github.com/platformio/platform-openhw/tree/master/examples/pulp-sdk-asm?utm_source=platformio.org&utm_medium=docs)
- [pulp-runtime-sort](https://github.com/platformio/platform-openhw/tree/master/examples/pulp-runtime-sort?utm_source=platformio.org&utm_medium=docs)
- [pulp-sdk-sort](https://github.com/platformio/platform-openhw/tree/master/examples/pulp-sdk-sort?utm_source=platformio.org&utm_medium=docs)
- [native-sort](https://github.com/platformio/platform-openhw/tree/master/examples/native-sort?utm_source=platformio.org&utm_medium=docs)
- [native-asm](https://github.com/platformio/platform-openhw/tree/master/examples/native-asm?utm_source=platformio.org&utm_medium=docs)

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
| [Digilent Nexys A7](../boards/openhw/nexys-a7.md) |  | 320MHz | 16MB | 1.16MB |

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-openhw/releases) of the OpenHW Group platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = openhw
board = ...

; Specific version
[env:custom_stable]
platform = openhw@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-openhw.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [framework-pulp-runtime](https://registry.platformio.org/tools/platformio/framework-pulp-runtime) | Runtime Environment for Parallel Ultra Low Power platform |
| [framework-pulp-sdk](https://registry.platformio.org/tools/platformio/framework-pulp-sdk) | Software Development Kit for Parallel Ultra Low Power platform |
| [tool-openocd-riscv-pulp](https://registry.platformio.org/tools/platformio/tool-openocd-riscv-pulp) | Fork of Open On-Chip Debugger that has RISC-V support for PULP platform |
| [tool-ovpsim-corev](https://registry.platformio.org/tools/platformio/tool-ovpsim-corev) | Imperas RISC-V OVPsim CORE-V simulator provides a reference of the OpenHW Group CORE-V processor cores. The riscvOVPsim familiy of simulators implement the full and complete functionality of the RISC-V Foundation's public User and Privilege specifications. |
| [tool-renode](https://registry.platformio.org/tools/platformio/tool-renode) | Renode is a development framework which accelerates IoT and embedded systems development by letting you simulate physical hardware systems |
| [toolchain-riscv-pulp](https://registry.platformio.org/tools/platformio/toolchain-riscv-pulp) | GNU toolchain for RISC-V (PULP platform) |

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
| [PULP Runtime Environment](../frameworks/pulp-runtime.md) | Runtime Environment for Parallel Ultra Low Power platform |
| [PULP SDK](../frameworks/pulp-sdk.md) | Software Development Kit for Parallel Ultra Low Power platform |

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### Digilent

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Digilent Nexys A7](../boards/openhw/nexys-a7.md) | On-board |  | 320MHz | 16MB | 1.16MB |
