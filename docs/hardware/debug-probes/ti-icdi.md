<a id="debugging-tool-ti-icdi"></a>

# TI-ICDI {#ti-icdi}

Tiva™ C Series evaluation and reference design kits provide an integrated In-Circuit Debug Interface (ICDI) which allows programming and debugging of the onboard C Series microcontroller. Official reference can be found [here](http://www.ti.com/tool/stellaris_icdi_drivers?utm_source=platformio&utm_medium=docs).

## Configuration {#configuration}

You can configure debugging tool using [debug_tool](../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md):

```ini
[env:myenv]
platform = ...
board = ...
debug_tool = ti-icdi
```

If you would like to use this tool for firmware uploading, please change upload protocol:

```ini
[env:myenv]
platform = ...
board = ...
debug_tool = ti-icdi
upload_protocol = ti-icdi
```

More options:

- [Debugging options](../../reference/platformio-ini/env/debug-options.md)
- [Upload options](../../reference/platformio-ini/env/upload-options.md)

## Drivers {#drivers}

<dl>

<dt>

Windows

</dt>

<dd>

Please "USB Driver Installation" guide for your board.

</dd>

<dt>

Mac

</dt>

<dd>

Not required.

</dd>

<dt>

Linux

</dt>

<dd>

Please install "udev" rules [99-platformio-udev.rules](../../get-started/install/udev-rules.md). If you already installed them before, please check that your rules are up-to-date or repeat steps.

</dd>

</dl>

<!-- begin_platforms -->

## Platforms

| Name | Description |
|---|---|
| [TI TIVA](../platforms/titiva.md) | Texas Instruments TM4C12x MCUs offer the industrys most popular ARM Cortex-M4 core with scalable memory and package options, unparalleled connectivity peripherals, advanced application functions, industry-leading analog integration, and extensive software solutions. |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [LibOpenCM3](../frameworks/libopencm3.md) | The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers. |

## Boards

:::note

For more detailed `board` information please scroll tables below by horizontal.

:::

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [TI LaunchPad (Stellaris) w/ lm4f120 (80MHz)](../boards/titiva/lplm4f120h5qr.md) | [TI TIVA](../platforms/titiva.md) | On-board | LPLM4F120H5QR | 80MHz | 256KB | 32KB |
| [TI LaunchPad (Tiva C) w/ tm4c123 (80MHz)](../boards/titiva/lptm4c123gh6pm.md) | [TI TIVA](../platforms/titiva.md) | On-board | LPTM4C123GH6PM | 80MHz | 256KB | 32KB |
| [TI LaunchPad (Tiva C) w/ tm4c129 (120MHz)](../boards/titiva/lptm4c1294ncpdt.md) | [TI TIVA](../platforms/titiva.md) | On-board | LPTM4C1294NCPDT | 120MHz | 1MB | 256KB |
