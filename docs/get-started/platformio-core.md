---
description: PlatformIO Core is the command-line tool and build system behind every PlatformIO product.
---

<a id="piocore"></a>

# PlatformIO Core (CLI) {#platformio-core-cli}

PlatformIO Core is the command-line tool and build system at the center of
PlatformIO. [PlatformIO IDE](./platformio-ide.md) and
[PlatformIO Home](./platformio-home.md) are graphical front ends to it, so
anything you can do in them you can also do, or automate, with the `pio`
command.

It includes:

- A multi-platform build system.
- A package manager for development platforms, toolchains, frameworks and
  [libraries](../guides/libraries/index.md), including the
  [Library Dependency Finder](../guides/libraries/ldf.md).
- Tools to [upload](../reference/cli/pio-run.md),
  [debug](../guides/debugging/index.md),
  [test](../guides/unit-testing/index.md) and
  [analyze](../guides/static-code-analysis/index.md) firmware.
- A [serial port monitor](../reference/cli/pio-device/monitor.md).
- Project generators for [IDEs](../guides/ide/index.md) and integration with
  [CI services](../guides/ci/index.md).

PlatformIO Core is written in Python and runs on Windows, macOS, Linux and
FreeBSD, including ARM-based single-board computers. See
[System requirements](./install/requirements.md).

## Do you need to install it? {#do-you-need-to-install-it}

Not if you use PlatformIO IDE: it includes PlatformIO Core, and its terminal
has the `pio` command ready to use. To use that same installation from other
terminals, [install the shell commands](./install/shell-commands.md).

Install PlatformIO Core on its own when you work only from the command line,
use another editor, or build on a CI server. See
[Install PlatformIO Core](./install/index.md).

## Next steps {#next-steps}

- [Quick start](./quick-start.md): create, build and upload your first project.
- [CLI reference](../reference/cli/index.md): every `pio` command and option.
