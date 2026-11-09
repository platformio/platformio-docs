<a id="piocore"></a>

# PlatformIO Core (CLI) {#platformio-core-cli}

**PlatformIO Core** (CLI tool) is the heart of the entire PlatformIO ecosystem and consists of

- Multi-platform Build System
- Unified Package Manager
- [Library Management](../guides/libraries/index.md)
- [Library Dependency Finder (LDF)](../guides/libraries/ldf.md)
- [Serial Port Monitor](../reference/cli/pio-device/monitor.md)
- Integration components ([Cloud & Desktop IDEs](../guides/ide/index.md) and [Continuous Integration](../guides/ci/index.md)).

**PlatformIO Core** is written in [Python](https://www.python.org/downloads/) and works on Windows, macOS, Linux, FreeBSD and *ARM*-based credit-card sized computers ([Raspberry Pi](http://www.raspberrypi.org), [BeagleBone](http://beagleboard.org), [CubieBoard](http://cubieboard.org), [Samsung ARTIK](https://www.artik.io), etc.).

**PlatformIO Core** provides a rich and documented Command Line Interface (CLI). The other PlatformIO-based software and IDEs are based on **PlatformIO Core CLI**, such as [PlatformIO IDE](./platformio-ide.md). In other words, they wrap **PlatformIO Core** with own GUI.

:::note

Please note that you do not need to install **PlatformIO Core** if you are going to use [PlatformIO IDE](./platformio-ide.md). **PlatformIO Core** is built into PlatformIO IDE and you will be able to use it within PlatformIO IDE Terminal.

If you need **PlatformIO Core** commands outside PlatformIO IDE, please [Install Shell Commands](./install/shell-commands.md).

:::

- [Installation](./install/index.md)

  - [System Requirements](./install/requirements.md)
  - [Installation Methods](./install/methods/index.md)
  - [Development Version](./install/development-version.md)
  - [Install Shell Commands](./install/shell-commands.md)
  - [99-platformio-udev.rules](./install/udev-rules.md)
  - [Integration with custom applications (extensions, plugins)](./install/integration.md)
  - [Proxy Configuration](./install/proxy-configuration.md)
  - [Troubleshooting](./install/troubleshooting.md)
  - [Uninstall PlatformIO Core and dependent packages](./install/uninstall.md)

- [Quick Start](./quick-start.md)

  - [Setting Up the Project](./quick-start.md#setting-up-the-project)
  - [Board Identifier](./quick-start.md#board-identifier)
  - [Initialize Project](./quick-start.md#initialize-project)
  - [Process Project](./quick-start.md#process-project)
  - [Further Reading](./quick-start.md#further-reading)

- [CLI Guide](../reference/cli/index.md)

  - [Usage](../reference/cli/index.md#usage)
  - [Options](../reference/cli/index.md#options)
  - [Commands](../reference/cli/index.md#commands)
