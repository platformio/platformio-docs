<a id="pioremote"></a>

# Remote Development {#remote-development}

**Your devices are always with you!**

**PlatformIO Remote Development Solution** allows you to work remotely with devices from *Anywhere In The World*. No matter where are you now! Run a small and cross-platform [PlatformIO Remote Agent](../reference/cli/pio-remote/agent.md) on a remote machine and you are able to list active devices (wireless + wired), to upload firmware (program), to process remote unit tests, or to start remote debugging session via **Remote Serial Port Monitor**.

Using **PlatformIO Remote Development Solution** you can share your devices with colleagues across your organization or friends. In combination with [Cloud IDEs](./ide/index.md#ide-cloud), you can create awesome things at any time when inspiration comes to you.

You must have an [PlatformIO Account](../get-started/platformio-account.md) to use **PlatformIO Remote Development Solution**. A registration is **FREE**.

## Features {#features}

- [Remote Device Manager](../reference/cli/pio-remote/device.md)
- [Remote Serial Port Monitor](../reference/cli/pio-remote/device.md#cmd-remote-device-monitor)
- [Remote Firmware Updates](../reference/cli/pio-remote/run.md)
- Share devices with your team members
- Continuous Deployment
- Continuous Delivery
- Remote Unit Testing

## Use Cases {#use-cases}

<dl>

<dt>

Cloud IDE

</dt>

<dd>

Program your devices from anywhere in the world using the most popular [Cloud IDEs](./ide/index.md#ide-cloud). You do not need to install any extra software, no need to have static IP or open network ports. Everything works out of the box.

</dd>

<dt>

Devices behind card sized PC

</dt>

<dd>

Work with your favorite development environment and program devices connected to card-sized PC (Raspberry Pi, Cubie Board, etc.). You do not need to open SSH ports, install any extra Linux packages, toolchains.

</dd>

<dt>

Remote Unit Testing

</dt>

<dd>

Instruct any of [Continuous Integration](./ci/index.md) services to run remote tests on a physical device. See the documentation for [Remote Test Runner](./unit-testing/runner.md#unit-testing-runner-remote).

How does it work?

- You commit new changes to your source code repository
- [Continuous Integration](./ci/index.md) service deploys unit tests to a remote agent
- [Unit Testing](./unit-testing/index.md) engine runs tests on a physical device, process them, and send results
- [Continuous Integration](./ci/index.md) service prints results in human readable format
- If one test fails, current CI build will fail too.

</dd>

<dt>

Board Farm

</dt>

<dd>

A similar concept as described in "Remote Unit Testing" above. Let's imagine that you need to test some logic on the unlimited number of target devices. Very often it can be the same hardware prototype but with different factory revisions.

You connect these devices via USB hub to PC and instruct **PlatformIO Remote Development Solution** to process your test on ALL targets connected to a specific agent. See documentation below.

</dd>

<dt>

Remote Serial Monitor

</dt>

<dd>

Sometimes you don't have physical access to a target device but you need to read data from some serial port. **PlatformIO Remote Development Solution** allows you to connect to a remote agent and list connected devices with their serial ports. See [pio remote device monitor](../reference/cli/pio-remote/device.md#cmd-remote-device-monitor) command for details.

</dd>

</dl>

## Technology {#technology}

![](./img/pio-remote-architecture.png)

**PlatformIO Remote Development Solution** is an own PlatformIO technology for remote solutions without external dependencies to operating system or its software based on [client-server architecture](https://en.wikipedia.org/wiki/Client–server_model). The Server component (PlatformIO Cloud) plays a role of coupling link between [PlatformIO Remote Agent](../reference/cli/pio-remote/agent.md) and Client ([PlatformIO Remote CLI](../reference/cli/pio-remote/index.md), [Cloud IDEs](./ide/index.md#ide-cloud), [Continuous Integration](./ci/index.md), SDKs, etc.). When you start [PlatformIO Remote Agent](../reference/cli/pio-remote/agent.md), it connects over the Internet with PlatformIO Cloud and listen for the actions/commands which you can send in Client role from anywhere in the world.

**PlatformIO Remote Development Solution** is multi-agents and multi-clients system. A single agent can be shared with multiple clients, where different clients can use the same agent. This approach allows one to work with distributed hardware located in the different places, networks, etc.

This technology allows one to work with remote devices in generic form as you do that with local devices using PlatformIO ecosystem. The only one difference is a prefix "remote" before each generic PlatformIO command. For example, listing of local and remote devices will look like [pio device list](../reference/cli/pio-device/list.md) and [pio remote device list](../reference/cli/pio-remote/device.md#cmd-remote-device-list).

## Installation {#installation}

**PlatformIO Remote Development Solution** is built into [PlatformIO IDE](../get-started/platformio-ide.md). Please open PlatformIO IDE Terminal and run `pio remote --help` command for usage (see [PlatformIO Remote CLI](../reference/cli/pio-remote/index.md)).

If you do not have [PlatformIO IDE](../get-started/platformio-ide.md), or use [Cloud IDEs](./ide/index.md#ide-cloud) or a card-sized PC (Raspberry Pi, BeagleBoard, etc.), please install [PlatformIO Core (CLI)](../get-started/platformio-core.md).

<a id="pio-remote-quickstart"></a>

## Quick Start {#quick-start}

1. Start **PlatformIO Remote Development Solution** Agent using [pio remote agent start](../reference/cli/pio-remote/agent.md#cmd-remote-agent-start) command on a **remote machine** where devices are connected physically or are accessible via network. **PlatformIO Remote Development Solution** **Agent works on Windows, macOS, Linux and Linux ARMv6+**. It means that you can use desktop machine, laptop or credit card sized PC (Raspberry Pi, BeagleBoard, etc).

   You can share own devices/hardware with friends, team or other developers using [`pio remote agent start --share`](../reference/cli/pio-remote/agent.md#cmdoption-pio-remote-agent-start-s) option.

2. Using **host machine** ([PlatformIO Remote CLI](../reference/cli/pio-remote/index.md), [Cloud IDEs](./ide/index.md#ide-cloud) Terminal in a browser, SDKs, etc.), please authorize via [pio account login](../reference/cli/pio-account/login.md) command with the same credentials that you used on the previous step. Now, you can use [PlatformIO Remote CLI](../reference/cli/pio-remote/index.md) commands to work with **remote machine** and its devices.

   You don't need to have networking or other access to **remote machine** where **PlatformIO Remote Development Solution** Agent is started.

   If you use **PlatformIO Remote Development Solution** in pair with [Continuous Integration](./ci/index.md) or want automatically authorize, please set [`PLATFORMIO_AUTH_TOKEN`](../reference/environment-variables.md#envvar-PLATFORMIO_AUTH_TOKEN) system environment variable instead of using [pio account login](../reference/cli/pio-account/login.md) command.

:::note

In case with [Cloud IDEs](./ide/index.md#ide-cloud), your browser with Cloud IDE's VM is a "host machine". The machine where devices are connected physically (your real PC) is called "remote machine" in this case. You should run **PlatformIO Remote Development Solution** Agent here (not in Cloud IDE's Terminal).

:::

:::note

Please use local IP as "upload port" when device is not connected directly to a remote machine where **PlatformIO Remote Development Solution** Agent is started but supports natively Over-the-Air (OTA) updates. For example, [Espressif 8266](/hardware/platforms/espressif8266) and [Over-the-Air (OTA) update](/hardware/platforms/espressif8266#platform-espressif-ota). In this case, the final command for remote OTA update will look as `pio remote run -t upload --upload-port 192.168.0.255` or `pio remote run -t upload --upload-port myesp8266.local`.

:::

## CLI Guide {#cli-guide}

- [PlatformIO Remote CLI](../reference/cli/pio-remote/index.md)

  - [PlatformIO Remote Agent](../reference/cli/pio-remote/agent.md)

    - [pio remote agent list](../reference/cli/pio-remote/agent.md#pio-remote-agent-list)
    - [pio remote agent start](../reference/cli/pio-remote/agent.md#pio-remote-agent-start)

  - [pio remote device](../reference/cli/pio-remote/device.md)

    - [pio remote device list](../reference/cli/pio-remote/device.md#pio-remote-device-list)
    - [pio remote device monitor](../reference/cli/pio-remote/device.md#pio-remote-device-monitor)

  - [pio remote run](../reference/cli/pio-remote/run.md)

    - [Usage](../reference/cli/pio-remote/run.md#usage)
    - [Description](../reference/cli/pio-remote/run.md#description)
    - [Options](../reference/cli/pio-remote/run.md#options)
    - [Example](../reference/cli/pio-remote/run.md#example)

  - [pio remote test](../reference/cli/pio-remote/test.md)

    - [Usage](../reference/cli/pio-remote/test.md#usage)
    - [Description](../reference/cli/pio-remote/test.md#description)
    - [Options](../reference/cli/pio-remote/test.md#options)
    - [Examples](../reference/cli/pio-remote/test.md#examples)

  - [pio remote update](../reference/cli/pio-remote/update.md)

    - [Usage](../reference/cli/pio-remote/update.md#usage)
    - [Description](../reference/cli/pio-remote/update.md#description)
    - [Options](../reference/cli/pio-remote/update.md#options)
    - [Examples](../reference/cli/pio-remote/update.md#examples)
