---
title: "SiFive"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-sifive"></a>

# SiFive

**Registry:** [https://registry.platformio.org/platforms/platformio/sifive](https://registry.platformio.org/platforms/platformio/sifive)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/sifive`

SiFive brings the power of open source and software automation to the semiconductor industry, making it possible to develop new hardware faster and more affordably than ever before.

For more detailed information please visit [vendor site](https://sifive.com?utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [SiFive development platform repository](https://github.com/platformio/platform-sifive/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [freedom-e-sdk_freertos-blinky-system-view](https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_freertos-blinky-system-view?utm_source=platformio.org&utm_medium=docs)
- [zephyr-blink](https://github.com/platformio/platform-sifive/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs)
- [native-blink_asm](https://github.com/platformio/platform-sifive/tree/master/examples/native-blink_asm?utm_source=platformio.org&utm_medium=docs)
- [freedom-e-sdk_hello](https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_hello?utm_source=platformio.org&utm_medium=docs)
- [freedom-e-sdk_test-coreip](https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_test-coreip?utm_source=platformio.org&utm_medium=docs)
- [freedom-e-sdk_sifive-welcome](https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_sifive-welcome?utm_source=platformio.org&utm_medium=docs)
- [freedom-e-sdk_timer-interrupt](https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_timer-interrupt?utm_source=platformio.org&utm_medium=docs)
- [freedom-e-sdk_freertos-blinky](https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_freertos-blinky?utm_source=platformio.org&utm_medium=docs)
- [freedom-e-sdk_multicore-hello](https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_multicore-hello?utm_source=platformio.org&utm_medium=docs)
- [freedom-e-sdk_user-syscall](https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_user-syscall?utm_source=platformio.org&utm_medium=docs)
- [freedom-e-sdk_spi](https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_spi?utm_source=platformio.org&utm_medium=docs)
- [freedom-e-sdk_freertos-pmp-blinky](https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_freertos-pmp-blinky?utm_source=platformio.org&utm_medium=docs)
- [freedom-e-sdk_user-mode](https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_user-mode?utm_source=platformio.org&utm_medium=docs)
- [zephyr-synchronization](https://github.com/platformio/platform-sifive/tree/master/examples/zephyr-synchronization?utm_source=platformio.org&utm_medium=docs)
- [zephyr-hello-world](https://github.com/platformio/platform-sifive/tree/master/examples/zephyr-hello-world?utm_source=platformio.org&utm_medium=docs)

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
| [Arty FPGA Dev Kit](../boards/sifive/e310-arty.md) | FE310 | 450MHz | 16MB | 256MB |
| [HiFive Unleashed](../boards/sifive/hifive-unleashed.md) | FU540 | 1500MHz | 32MB | 8GB |
| [HiFive1](../boards/sifive/hifive1.md) | FE310 | 320MHz | 16MB | 16KB |
| [HiFive1 Rev B](../boards/sifive/hifive1-revb.md) | FE310 | 320MHz | 16MB | 16KB |
| [SparkFun RED-V RedBoard](../boards/sifive/sparkfun-redboard-v.md) | FE310 | 320MHz | 16MB | 16KB |
| [SparkFun RED-V Thing Plus](../boards/sifive/sparkfun-thing-plus-v.md) | FE310 | 320MHz | 16MB | 16KB |

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-sifive/releases) of SiFive development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = sifive
board = ...

; Specific version
[env:custom_stable]
platform = sifive@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-sifive.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [framework-freedom-e-sdk](https://registry.platformio.org/tools/platformio/framework-freedom-e-sdk) | Open Source Software for Developing on the SiFive Freedom E Platform |
| [framework-zephyr](https://registry.platformio.org/tools/platformio/framework-zephyr) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
| [tool-cmake](https://registry.platformio.org/tools/platformio/tool-cmake) | CMake is an open-source, cross-platform family of tools designed to build, test and package software |
| [tool-dtc](https://registry.platformio.org/tools/platformio/tool-dtc) | Device tree compiler |
| [tool-gperf](https://registry.platformio.org/tools/platformio/tool-gperf) | GNU gperf is a perfect hash function generator |
| [tool-jlink](https://registry.platformio.org/tools/platformio/tool-jlink) | Software and Documentation Pack for SEGGER J-Link debug probes |
| [tool-ninja](https://registry.platformio.org/tools/platformio/tool-ninja) | Ninja is a small build system with a focus on speed |
| [tool-openocd-riscv](https://registry.platformio.org/tools/platformio/tool-openocd-riscv) | Fork of Open On-Chip Debugger that has RISC-V support |
| [tool-qemu-riscv](https://registry.platformio.org/tools/platformio/tool-qemu-riscv) | QEMU is a generic and open source machine emulator and virtualizer |
| [tool-renode](https://registry.platformio.org/tools/platformio/tool-renode) | Renode is a development framework which accelerates IoT and embedded systems development by letting you simulate physical hardware systems |
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
| [Freedom E SDK](../frameworks/freedom-e-sdk.mdx) | Open Source Software for Developing on the SiFive Freedom E Platform |
| [FreeRTOS](../frameworks/freertos.md) | FreeRTOS is a real-time operating system kernel for embedded devices that has been ported to 40 microcontroller platforms. |
| [Zephyr](../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |

## Boards

:::note

- You can list pre-configured boards by [pio boards](../../reference/cli/pio-boards.md) command
- For more detailed `board` information please scroll the tables below by horizontally.

:::

### SiFive

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [HiFive Unleashed](../boards/sifive/hifive-unleashed.md) | On-board | FU540 | 1500MHz | 32MB | 8GB |
| [HiFive1](../boards/sifive/hifive1.md) | On-board | FE310 | 320MHz | 16MB | 16KB |
| [HiFive1 Rev B](../boards/sifive/hifive1-revb.md) | On-board | FE310 | 320MHz | 16MB | 16KB |

### SparkFun

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [SparkFun RED-V RedBoard](../boards/sifive/sparkfun-redboard-v.md) | On-board | FE310 | 320MHz | 16MB | 16KB |
| [SparkFun RED-V Thing Plus](../boards/sifive/sparkfun-thing-plus-v.md) | On-board | FE310 | 320MHz | 16MB | 16KB |

### Xilinx

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Arty FPGA Dev Kit](../boards/sifive/e310-arty.md) | On-board | FE310 | 450MHz | 16MB | 256MB |
