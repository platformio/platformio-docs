---
description: What PlatformIO is, what it is made of, and how a PlatformIO project works.
---

<a id="what-is-pio"></a>

# What is PlatformIO? {#what-is-platformio}

PlatformIO is an open-source toolset for building, uploading, debugging and
testing firmware for embedded systems. One project format and one set of
commands work across many microcontroller architectures, frameworks and
development hosts, so you do not have to install and learn a different vendor
toolchain and IDE for each board.

PlatformIO runs on Windows, macOS, Linux and FreeBSD, including ARM-based
single-board computers such as the Raspberry Pi.

## The problem it solves {#the-problem-it-solves}

Embedded development usually starts with setup work that has nothing to do
with your application:

- Each microcontroller family needs its own toolchain, flashing tool and,
  often, a vendor IDE that runs only on some operating systems.
- Switching to another chip means learning another environment.
- Libraries for sensors and peripherals are scattered and versioned
  inconsistently.
- Sharing a project with a team, or building it on a CI server, requires
  every machine to be set up the same way.

PlatformIO replaces this with a declarative project file. You state which
board and framework a project targets; PlatformIO installs the matching
toolchain, framework and libraries, then builds and uploads the firmware the
same way on every machine.

## Components {#components}

| Component | What it does |
| --- | --- |
| [PlatformIO Core (CLI)](./platformio-core.md) | The command-line tool (`pio`) and build system. Everything else is built on it. |
| [PlatformIO IDE](./platformio-ide.md) | Extensions for Visual Studio Code and CLion that add a toolbar, project wizard, debugger and terminal on top of PlatformIO Core. |
| [PlatformIO Home](./platformio-home.md) | A browser-based UI for projects, libraries, platforms, boards and devices. |
| [PlatformIO Registry](https://registry.platformio.org) | The package registry for development platforms, toolchains and libraries. |

PlatformIO Core is free, open source and permissively licensed (Apache 2.0).

## How a project works {#how-does-it-work}

1. You describe the hardware in [`platformio.ini`](../reference/platformio-ini/index.md):
   one or more [project environments](../reference/platformio-ini/env/index.md),
   each naming a [development platform](../hardware/platforms/index.md), a
   [board](/hardware/boards) and, optionally, a
   [framework](../hardware/frameworks/index.md):

   ```ini
   [env:esp32dev]
   platform = espressif32
   board = esp32dev
   framework = arduino
   ```

2. On the first build, PlatformIO downloads the development platform, the
   toolchain, the framework and the
   [libraries](../guides/libraries/index.md) the project depends on.
3. The build system compiles and links the firmware, and can
   [upload](../reference/cli/pio-run.md) it to the board,
   [debug](../guides/debugging/index.md) it,
   [run unit tests](../guides/unit-testing/index.md) on the host or the
   target, and [analyze the code](../guides/static-code-analysis/index.md).

The same project builds identically in an IDE, in a terminal and on a
[CI server](../guides/ci/index.md).

## Next steps {#next-steps}

- [Install PlatformIO IDE](./platformio-ide.md) to start in Visual Studio Code.
- Prefer the terminal? [Install PlatformIO Core](./install/index.md) and
  follow the [Quick start](./quick-start.md).
