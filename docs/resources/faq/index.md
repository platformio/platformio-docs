---
description: Answers to frequently asked questions about PlatformIO.
---

<a id="faq"></a>

# Frequently asked questions {#frequently-asked-questions}

More answers are in the [FAQ category](https://community.platformio.org/c/faq)
of the PlatformIO Community forum.

<a id="general"></a>

## General {#faq-general}

<a id="what-is-platformio"></a>

**What is PlatformIO?** See [What is PlatformIO?](../../get-started/what-is-platformio.md)

<a id="what-is-pio-directory"></a>

**What is the `.pio` folder?** It is the project's build and dependency folder,
the [`workspace_dir`](../../reference/platformio-ini/platformio/workspace-dir.md).
PlatformIO recreates it as needed; do not commit it to version control.

<a id="command-completion-in-terminal"></a>

**How do I enable tab completion of `pio` commands?** See
[`pio system completion`](../../reference/cli/pio-system/completion/index.md).

<a id="platformio-udev-rules"></a>

**Linux cannot access my board.** Install the
[udev rules](../../get-started/install/udev-rules.md).

<a id="multiple-platformio-cores-in-a-system"></a>

**I have several PlatformIO Core installations.** See
[More than one PlatformIO Core is installed](../../get-started/install/troubleshooting.md#multiple-pio-cores-issue).

## Topics {#topics}

| Question | |
| --- | --- |
| [Arduino IDE or PlatformIO IDE?](./arduino-vs-platformio.md) | Which one fits your project |
| [How do I install Python?](./install-python.md) | Notes for Linux, macOS and Windows |
| [Is there a serial monitor with a graphical UI?](./advanced-serial-monitor.md) | Using CoolTerm with PlatformIO |
| [How is program memory usage calculated?](./program-memory-usage.md) | `.text`, `.data` and `.bss` |
| [How do I convert an `.ino` file to C++?](./ino-to-cpp.md) | For editors without Arduino support |
| [How do I pass options to SCons?](./custom-scons-cli-options.md) | The `SCONSFLAGS` environment variable |
| [Troubleshooting](./troubleshooting.md) | Package manager and build problems |
