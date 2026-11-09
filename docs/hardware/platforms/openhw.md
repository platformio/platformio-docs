---
title: "OpenHW Group"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-openhw"></a>

# OpenHW Group

**Registry:** [https://registry.platformio.org/platforms/platformio/openhw](https://registry.platformio.org/platforms/platformio/openhw)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/openhw`

OpenHW Group is a not-for-profit, global organization that provides an infrastructure for hosting high quality open-source HW developments in line with industry best practices. The OpenHW CV32E40P RISC-V core is the first open-source core for high-volume chips verified with the state-of-the-art process required for high-integrity, commercial SoCs.

For more detailed information please visit [vendor site](https://www.openhwgroup.org/?utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [OpenHW Group development platform repository](https://github.com/platformio/platform-openhw/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [pulp-sdk-asm](https://github.com/platformio/platform-openhw/tree/master/examples/pulp-sdk-asm?utm_source=platformio.org&utm_medium=docs)
- [pulp-runtime-sort](https://github.com/platformio/platform-openhw/tree/master/examples/pulp-runtime-sort?utm_source=platformio.org&utm_medium=docs)
- [pulp-sdk-sort](https://github.com/platformio/platform-openhw/tree/master/examples/pulp-sdk-sort?utm_source=platformio.org&utm_medium=docs)
- [native-sort](https://github.com/platformio/platform-openhw/tree/master/examples/native-sort?utm_source=platformio.org&utm_medium=docs)
- [native-asm](https://github.com/platformio/platform-openhw/tree/master/examples/native-asm?utm_source=platformio.org&utm_medium=docs)

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
| [Digilent Nexys A7](../boards/openhw/nexys-a7.md) |  | 320MHz | 16MB | 1.16MB |

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-openhw/releases) of OpenHW Group development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

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

**Linux Users**:

- Install "udev" rules [99-platformio-udev.rules](../../get-started/install/udev-rules.md)
- Raspberry Pi users, please read this article [Enable serial port on Raspberry Pi](https://hallard.me/enable-serial-port-on-raspberry-pi/).

**Windows Users:**

Please check that you have a correctly installed USB driver from board manufacturer

:::

## Frameworks

| Name | Description |
|---|---|
| [PULP Runtime Environment](../frameworks/pulp-runtime.md) | Runtime Environment for Parallel Ultra Low Power platform |
| [PULP SDK](../frameworks/pulp-sdk.md) | Software Development Kit for Parallel Ultra Low Power platform |

## Boards

:::note

- You can list pre-configured boards by [pio boards](../../reference/cli/pio-boards.md) command
- For more detailed `board` information please scroll the tables below by horizontally.

:::

### Digilent

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Digilent Nexys A7](../boards/openhw/nexys-a7.md) | On-board |  | 320MHz | 16MB | 1.16MB |
