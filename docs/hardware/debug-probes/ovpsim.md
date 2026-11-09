---
description: "Use the OVPsim debug probe with PlatformIO: configuration, drivers, wiring and supported boards."
---

# OVPsim

[![](./img/renode.png)](https://www.ovpworld.org/?utm_source=platformio&utm_medium=docs)

OVPsim is a multiprocessor platform emulator (often called a full-system simulator) used to run unchanged production binaries of the target hardware. It has public APIs allowing users to create their own processor, peripheral and platform models. Various models are available as open source. For more information, see [OVPsim's official website](https://www.ovpworld.org/?utm_source=platformio&utm_medium=docs).

<!-- begin_platforms -->

## Platforms

| Name | Description |
|---|---|
| [OpenHW Group](../platforms/openhw.md) | OpenHW Group is a not-for-profit, global organization that provides an infrastructure for hosting high quality open-source HW developments in line with industry best practices. The OpenHW CV32E40P RISC-V core is the first open-source core for high-volume chips verified with the state-of-the-art process required for high-integrity, commercial SoCs. |

## Frameworks

| Name | Description |
|---|---|
| [PULP Runtime Environment](../frameworks/pulp-runtime.md) | Runtime Environment for Parallel Ultra Low Power platform |
| [PULP SDK](../frameworks/pulp-sdk.md) | Software Development Kit for Parallel Ultra Low Power platform |

## Boards

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [Digilent Nexys A7](../boards/openhw/nexys-a7.md) | [OpenHW Group](../platforms/openhw.md) | On-board |  | 320MHz | 16MB | 1.16MB |
