<a id="debugging-tool-renode"></a>

# Renode {#renode}

[![](./img/renode.png)](https://renode.io/?utm_source=platformio&utm_medium=docs)

Renode is a development framework which accelerates IoT and embedded systems development by letting you simulate physical hardware systems - including both the CPU, peripherals, sensors, environment and wired or wireless medium between nodes. For more information, see [Renode's official website](https://renode.io/?utm_source=platformio&utm_medium=docs).

## Configuration {#configuration}

You can configure Renode as a debugging tool using [debug_tool](../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md):

```ini
[env:myenv]
platform = ...
board = ...
debug_tool = renode
```

More options:

- [Debugging options](../../reference/platformio-ini/env/debug-options.md)

## Installation {#installation}

We will automatically install for you the latest Renode package using PlatformIO package manager. The only requirement is to install Mono/.NET framework.

<dl>

<dt>

Windows

</dt>

<dd>

On Windows 7, download and install [.NET Framework 4.7](https://www.microsoft.com/net/download/dotnet-framework-runtime). Windows 10 ships with .NET by default, so no action is required there.

</dd>

<dt>

Mac

</dt>

<dd>

Install [Homebrew](https://brew.sh/) and the `mono` package using `brew install mono`.

</dd>

<dt>

Linux

</dt>

<dd>

Install the `mono-complete` package as per the installation instructions for various Linux distributions which can be found on [the Mono project website](https://www.mono-project.com/download/stable/#download-lin).

</dd>

</dl>

Check the [official Renode installation guide](https://github.com/renode/renode/blob/master/README.rst) for more details.

## Custom Settings {#custom-settings}

If the default Renode configuration is not suitable for your project, it's possible to override the default Renode flags in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md). The following sections describe typical use cases where custom settings might be useful.

### Additional Analyzers {#additional-analyzers}

Additional analyzers might be handy in cases when an application prints output to a peripheral which is not visible by default. For example, to open an additional UART window while using Renode as the upload tool, a special command `showAnalyzer` should be added to `upload_flags` option, e.g.:

```ini
[env:hifive1-revb]
platform = sifive
framework = zephyr
board = hifive1-revb
; Override the default upload settings
upload_command = renode $UPLOAD_FLAGS
upload_flags =
    -e include @scripts/single-node/sifive_fe310.resc
    -e showAnalyzer uart1
    -e sysbus LoadELF @$SOURCE
    -e start
```

### Redirecting peripherals output {#redirecting-peripherals-output}

It might be useful to redirect output from device peripherals to a more convenient communication channel. A typical example is redirecting UART output to a socket which can be opened by [pio device monitor](../../reference/cli/pio-device/monitor.md) while using Renode as the debug tool. The default debug flags can be overridden using the `debug_server` option. For example, the following configuration can be used to redirect output from the `UART0` port on the `hifive1-revb` board:

```ini
[env:hifive1-revb]
platform = sifive
framework = zephyr
board = hifive1-revb
; Override the default debug settings
debug_tool = custom
debug_port = localhost:3333
debug_server = renode
  --hide-log
  -e machine StartGdbServer 3333 True
  -e emulation CreateServerSocketTerminal 4321 "externalUART" false
  -e connector Connect uart0 externalUART
debug_extra_cmds =
    monitor start

# Monitor port for Renode integration
monitor_port = socket://localhost:4321
```

## Examples {#examples}

- [Pre-configured projects for Zephyr RTOS, FreeRTOS, and Arduino](https://github.com/carlosedp/PlatformIO-Renode-Demos/) by Carlos Eduardo

<!-- begin_platforms -->

## Platforms

| Name | Description |
|---|---|
| [OpenHW Group](../platforms/openhw.md) | OpenHW Group is a not-for-profit, global organization that provides an infrastructure for hosting high quality open-source HW developments in line with industry best practices. The OpenHW CV32E40P RISC-V core is the first open-source core for high-volume chips verified with the state-of-the-art process required for high-integrity, commercial SoCs. |
| [SiFive](../platforms/sifive.md) | SiFive brings the power of open source and software automation to the semiconductor industry, making it possible to develop new hardware faster and more affordably than ever before. |

## Frameworks

| Name | Description |
|---|---|
| [Freedom E SDK](../frameworks/freedom-e-sdk.mdx) | Open Source Software for Developing on the SiFive Freedom E Platform |
| [FreeRTOS](../frameworks/freertos.md) | FreeRTOS is a real-time operating system kernel for embedded devices that has been ported to 40 microcontroller platforms. |
| [PULP Runtime Environment](../frameworks/pulp-runtime.md) | Runtime Environment for Parallel Ultra Low Power platform |
| [PULP SDK](../frameworks/pulp-sdk.md) | Software Development Kit for Parallel Ultra Low Power platform |
| [Zephyr](../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |

## Boards

:::note

For more detailed `board` information please scroll tables below by horizontal.

:::

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [Arty FPGA Dev Kit](../boards/sifive/e310-arty.md) | [SiFive](../platforms/sifive.md) | On-board | FE310 | 450MHz | 16MB | 256MB |
| [Digilent Nexys A7](../boards/openhw/nexys-a7.md) | [OpenHW Group](../platforms/openhw.md) | On-board |  | 320MHz | 16MB | 1.16MB |
| [HiFive Unleashed](../boards/sifive/hifive-unleashed.md) | [SiFive](../platforms/sifive.md) | On-board | FU540 | 1500MHz | 32MB | 8GB |
| [HiFive1](../boards/sifive/hifive1.md) | [SiFive](../platforms/sifive.md) | On-board | FE310 | 320MHz | 16MB | 16KB |
| [HiFive1 Rev B](../boards/sifive/hifive1-revb.md) | [SiFive](../platforms/sifive.md) | On-board | FE310 | 320MHz | 16MB | 16KB |
| [SparkFun RED-V RedBoard](../boards/sifive/sparkfun-redboard-v.md) | [SiFive](../platforms/sifive.md) | On-board | FE310 | 320MHz | 16MB | 16KB |
| [SparkFun RED-V Thing Plus](../boards/sifive/sparkfun-thing-plus-v.md) | [SiFive](../platforms/sifive.md) | On-board | FE310 | 320MHz | 16MB | 16KB |
