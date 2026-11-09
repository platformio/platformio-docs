---
description: Create a PlatformIO project, or add boards, options and IDE project files to an existing one.
---

# pio project init

Create a PlatformIO project, or update an existing one: add boards, set
options, or generate project files for an IDE.

## Usage {#usage}

```bash
pio project init [OPTIONS]
```

## Description {#description}

In a directory that is not yet a project, the command creates:

| Path | Purpose |
| --- | --- |
| [`platformio.ini`](../../platformio-ini/index.md) | The project configuration file |
| [`include`](../../platformio-ini/platformio/include-dir.md) | Project header files |
| [`src`](../../platformio-ini/platformio/src-dir.md) | Project source files (`.c`, `.cpp`, `.S`, `.ino`, ...) |
| [`lib`](../../platformio-ini/platformio/lib-dir.md) | Project-specific (private) libraries; see [Library Dependency Finder](../../../guides/libraries/ldf.md) |
| [`test`](../../platformio-ini/platformio/test-dir.md) | [Unit tests](../../../guides/unit-testing/index.md) |
| `.gitignore` | Excludes the build output from version control |

In an existing project, it keeps your files and only adds what you ask for.
Unless you pass `--no-install-dependencies`, it then installs the development
platforms, toolchains, frameworks and libraries the project needs.

## Options {#options}

<a id="cmdoption-pio-project-init-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-project-init-d}

The project directory. Default: the current working directory.

<a id="cmdoption-pio-project-init-board"></a>

### `-b, --board` {#cmdoption-pio-project-init-b}

Add a [project environment](../../platformio-ini/env/index.md) for a board ID.
Repeat the option to add several boards. The new environment, `[env:<board_id>]`,
sets [`platform`](../../platformio-ini/env/platform.md),
[`board`](../../platformio-ini/env/board.md) and, if the board supports any,
the board's first [`framework`](../../platformio-ini/env/framework.md).
Boards that already have an environment are skipped. Find board IDs with
[`pio boards`](../pio-boards.md).

### `--ide` {#cmdoption-pio-project-init-ide}

Generate project files for an IDE: `clion`, `codeblocks`, `eclipse`, `emacs`,
`netbeans`, `qtcreator`, `sublimetext`, `vim`, `visualstudio` or `vscode`. Then
open or import the project in that IDE. See
[IDE integrations](../../../guides/ide/index.md).

<a id="cmdoption-pio-project-init-environment"></a>

### `-e, --environment` {#cmdoption-pio-project-init-e}

The environment to update with `--project-option`, to use for `--ide` and
`--sample-code`, and whose dependencies to install. If you pass options for an
environment that does not exist, it is created. With `--environment`, the
`--board` options are ignored.

<a id="cmdoption-pio-project-init-project-option"></a>

### `-O, --project-option` {#cmdoption-pio-project-init-O}

A `platformio.ini` option as `name=value`, for example
`-O "lib_deps=bblanchon/ArduinoJson"`. Repeat it to set several options. The
options go to every environment added with `--board`, or to the environment
given with `--environment`; in the latter case, options of the
[`[platformio]` section](../../platformio-ini/platformio/index.md) go to that
section.

### `--env-prefix` {#cmdoption-pio-project-init-env-prefix}

A prefix for the names of environments added with `--board`. For example,
`--env-prefix dev_ --board uno` adds `[env:dev_uno]`.

### `--no-install-dependencies` {#cmdoption-pio-project-init-no-install-dependencies}

Do not install the packages and libraries the project needs.

### `--sample-code` {#cmdoption-pio-project-init-sample-code}

Add a sample `main` source file to `src` if the environment's development
platform or framework provides one. Added in PlatformIO Core 6.1.7.

<a id="cmdoption-pio-project-init-silent"></a>

### `-s, --silent` {#cmdoption-pio-project-init-s}

Do not print progress messages.

## Examples {#examples}

Create a project for Arduino Uno in the current directory:

```bash
pio project init --board uno
```

```text
The following files/directories have been created in /home/user/blink
include - Put project header files here
lib - Put project specific (private) libraries here
src - Put project source files here
platformio.ini - Project Configuration File
...
Project has been successfully initialized!
```

Create a project in another directory:

```bash
pio project init -d path/to/project --board uno
```

Create a project for Teensy 3.1 with the [Mbed](/hardware/frameworks/mbed)
framework instead of the board's default:

```bash
pio project init --board teensy31 --project-option "framework=mbed"
```

Add an environment named `native` with custom options:

```bash
pio project init --environment native --project-option="platform=native" --project-option="build_flags=-DRELEASE=1"
```

Generate VS Code project files for an existing project:

```bash
pio project init --ide vscode
```
