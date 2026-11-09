---
description: The development platforms PlatformIO supports - microcontroller architectures with their toolchains, build scripts and boards.
---

<a id="platforms"></a>

# Development platforms {#development-platforms}

A development platform is PlatformIO's integration of a microcontroller or
processor architecture. Each platform provides:

- the toolchain and the upload and debug tools for the architecture;
- the build scripts for the [frameworks](../frameworks/index.md) it supports;
- the definitions of its [boards](/hardware/boards).

A project environment selects a platform with the
[`platform`](../../reference/platformio-ini/env/platform.md) option, optionally
with a version requirement. A board always belongs to one platform. All
platforms build on Windows, macOS and Linux hosts; some also on ARM Linux
hosts such as the Raspberry Pi.

For an architecture that is not listed, you can create a
[custom development platform](../../guides/custom-platforms-and-boards/creating-platform.md).
All published platforms, including community ones, are in the
[PlatformIO Registry](https://registry.platformio.org/search?t=platform).

## Embedded {#embedded}

Platforms for microcontrollers and embedded processors:

- [Atmel AVR](/hardware/platforms/atmelavr)
- [Atmel megaAVR](/hardware/platforms/atmelmegaavr)
- [Atmel SAM](/hardware/platforms/atmelsam)
- [CHIPS Alliance](/hardware/platforms/chipsalliance)
- [Espressif 32](/hardware/platforms/espressif32)
- [Espressif 8266](/hardware/platforms/espressif8266)
- [Freescale Kinetis](/hardware/platforms/freescalekinetis)
- [Intel ARC32](/hardware/platforms/intel-arc32)
- [Intel MCS-51 (8051)](/hardware/platforms/intel-mcs51)
- [Lattice iCE40](/hardware/platforms/lattice-ice40)
- [Maxim 32](/hardware/platforms/maxim32)
- [Microchip PIC32](/hardware/platforms/microchippic32)
- [Nordic nRF51](/hardware/platforms/nordicnrf51)
- [Nordic nRF52](/hardware/platforms/nordicnrf52)
- [NXP i.MX RT](/hardware/platforms/nxpimxrt)
- [NXP LPC](/hardware/platforms/nxplpc)
- [OpenHW Group](/hardware/platforms/openhw)
- [Raspberry Pi RP2040](/hardware/platforms/raspberrypi)
- [Renesas RA](/hardware/platforms/renesas-ra)
- [RISC-V GAP](/hardware/platforms/riscv-gap)
- [Shakti](/hardware/platforms/shakti)
- [SiFive](/hardware/platforms/sifive)
- [Silicon Labs EFM32](/hardware/platforms/siliconlabsefm32)
- [ST STM32](/hardware/platforms/ststm32)
- [ST STM8](/hardware/platforms/ststm8)
- [Teensy](/hardware/platforms/teensy)
- [TI MSP430](/hardware/platforms/timsp430)
- [TI TIVA](/hardware/platforms/titiva)

## Desktop {#desktop}

Platforms that build programs for your computer, for example to [run unit tests on the host](../../guides/unit-testing/runner.md#native):

- [Native](/hardware/platforms/native)
- [Linux ARM](/hardware/platforms/linux-arm)
- [Linux i686](/hardware/platforms/linux-i686)
- [Linux x86_64](/hardware/platforms/linux-x86-64)
- [Windows x86](/hardware/platforms/windows-x86)
