<a id="platforms"></a>

# Development Platforms {#development-platforms}

The PlatformIO ecosystem has a decentralized architecture, allowing development for a range of *development platforms*. A development platform (or just "platform" for short) is usually a particular microcontroller or processor architecture that PlatformIO projects can be compiled to run on. (A few platforms, for example Teensy, use different target architectures for different boards.)

Each of the three supported host systems Mac OS X, Linux and Windows support compiling for all platforms listed below. Some platforms are also supported under ARM Linux hosts such as Raspberry Pi. For each development platform, PlatformIO defines:

- The **PlatformIO Build System** build scripts for the supported frameworks and SDKs
- Pre-configured presets for embedded circuit boards
- Pre-compiled toolchains and related tools for the architecture(s)

Each project must specify the platform name using the [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md). A specific platform version can optionally be specified as well. As embedded boards are equipped with a particular microcontroller, each embedded board specifies what development platform it uses and this can not be changed.

If a new board uses an architecture not in this list, a custom development platform can be created; see [Custom Development Platforms](../../guides/custom-platforms-and-boards/creating-platform.md).

The full list of supported development platforms is accessible on the [PlatformIO Registry](https://registry.platformio.org/search?t=platform).

## Embedded {#embedded}

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

- [Native](/hardware/platforms/native)
- [Linux ARM](/hardware/platforms/linux-arm)
- [Linux i686](/hardware/platforms/linux-i686)
- [Linux x86_64](/hardware/platforms/linux-x86-64)
- [Windows x86](/hardware/platforms/windows-x86)
