---
description: "Use the QEMU debug probe with PlatformIO: configuration, drivers, wiring and supported boards."
---

# QEMU

[![](./img/qemu.png)](https://www.qemu.org/?utm_source=platformio&utm_medium=docs)

QEMU is a free and open-source emulator that performs hardware virtualization. See the [official documentation](https://www.qemu.org/?utm_source=platformio&utm_medium=docs).

## Configuration {#configuration}

Select this probe with the [`debug_tool`](../../reference/platformio-ini/env/debug-tool.md) option in [`platformio.ini`](../../reference/platformio-ini/index.md):

```ini
[env:myenv]
platform = ...
board = ...
debug_tool = qemu
```

See also:

- [Debugging options](../../reference/platformio-ini/env/debug-options.md)

<!-- begin_platforms -->

## Platforms

| Name | Description |
|---|---|
| [SiFive](../platforms/sifive.md) | SiFive brings the power of open source and software automation to the semiconductor industry, making it possible to develop new hardware faster and more affordably than ever before. |

## Frameworks

| Name | Description |
|---|---|
| [Freedom E SDK](../frameworks/freedom-e-sdk.mdx) | Open Source Software for Developing on the SiFive Freedom E Platform |
| [FreeRTOS](../frameworks/freertos.md) | FreeRTOS is a real-time operating system kernel for embedded devices that has been ported to 40 microcontroller platforms. |
| [Zephyr](../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |

## Boards

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [Arty FPGA Dev Kit](../boards/sifive/e310-arty.md) | [SiFive](../platforms/sifive.md) | On-board | FE310 | 450MHz | 16MB | 256MB |
| [HiFive Unleashed](../boards/sifive/hifive-unleashed.md) | [SiFive](../platforms/sifive.md) | On-board | FU540 | 1500MHz | 32MB | 8GB |
| [HiFive1](../boards/sifive/hifive1.md) | [SiFive](../platforms/sifive.md) | On-board | FE310 | 320MHz | 16MB | 16KB |
