<a id="cmd-project-init"></a>

# pio project init {#pio-project-init}

## Usage {#usage}

```bash
pio project init [OPTIONS]
```

## Description {#description}

Initialize a new PlatformIO based project or update existing with new data.

This command will create:

- ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md)
- [include_dir](../../platformio-ini/platformio/include-dir.md), put project header files here
- [src_dir](../../platformio-ini/platformio/src-dir.md), put project source files here (`*.h, *.c, *.cpp, *.S, *.ino, etc.`)
- [lib_dir](../../platformio-ini/platformio/lib-dir.md), put project specific (private) libraries here. See also [Library Dependency Finder (LDF)](../../../guides/libraries/ldf.md)
- [test_dir](../../platformio-ini/platformio/test-dir.md), put project tests here. More details [Unit Testing](../../../guides/unit-testing/index.md)
- Miscellaneous files for VCS and [Continuous Integration](../../../guides/ci/index.md) support.

## Options {#options}

<a id="cmdoption-pio-project-init-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-project-init-d}

A path to a directory where *PlatformIO* will initialize new project.

<a id="cmdoption-pio-project-init-board"></a>

### `-b, --board` {#cmdoption-pio-project-init-b}

If you specify board `ID` (you can pass multiple `--board` options), then *PlatformIO* will automatically generate environment for ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md) and pre-fill these data:

- [platform](../../platformio-ini/env/platform.md)
- [framework](../../platformio-ini/env/framework.md)
- [board](../../platformio-ini/env/board.md)

The full list with pre-configured boards is available here [Development Platforms](../../../hardware/platforms/index.md).

### `--ide` {#cmdoption-pio-project-init-ide}

Initialize PlatformIO project for the specified IDE which can be imported later via "Import Project" functionality.

A list with supported IDE is available within `pio project init --help` command. Also, please take a look at [Cloud & Desktop IDEs](../../../guides/ide/index.md) page.

<a id="cmdoption-pio-project-init-environment"></a>

### `-e, --environment` {#cmdoption-pio-project-init-e}

Update project using existing environment.

<a id="cmdoption-pio-project-init-project-option"></a>

### `-O, --project-option` {#cmdoption-pio-project-init-O}

Initialize project with additional options from ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md). For example, `pio project init --project-option="lib_deps=ArduinoJSON"`. Multiple options are allowed.

### `--env-prefix` {#cmdoption-pio-project-init-env-prefix}

An environment prefix which will be used with pair in [board](../../platformio-ini/env/board.md) ID. For example, the default environment name for [Teensy 3.1 / 3.2](/hardware/boards/teensy/teensy31) board will be `[env:teensy31]`.

### `--no-install-dependencies` {#cmdoption-pio-project-init-no-install-dependencies}

Do not resolve project dependencies and do not install missed packages.

### `--sample-code` {#cmdoption-pio-project-init-sample-code}

:::info

Added in version 6.1.7.

:::

Include sample code in the newly created project. The availability of sample code depends on the [Development Platforms](../../../hardware/platforms/index.md) being used.

<a id="cmdoption-pio-project-init-silent"></a>

### `-s, --silent` {#cmdoption-pio-project-init-s}

Suppress progress reporting.

## Examples {#examples}

1. Initialize new project in a current working directory

```text
> pio project init

The current working directory *** will be used for the new project.
You can specify another project directory via
`pio project init -d %PATH_TO_THE_PROJECT_DIR%` command.

The following files/directories will be created in ***
platformio.ini - Project Configuration File. |-> PLEASE EDIT ME <-|
src - Put your source files here
lib - Put here project specific (private) libraries
Project has been successfully initialized!
Useful commands:
`pio run` - process/build project from the current directory
`pio run --target upload` or `pio run -t upload` - upload firmware to embedded board
`pio run --target clean` - clean project (remove compiled files)
```

2. Initialize new project in a specified directory

```text
> pio project init -d %PATH_TO_DIR%

The following files/directories will be created in ***
 platformio.ini - Project Configuration File. |-> PLEASE EDIT ME <-|
...
```

3. Initialize project for Arduino Uno

```text
> pio project init --board uno

The current working directory *** will be used for the new project.
You can specify another project directory via
`pio project init -d %PATH_TO_THE_PROJECT_DIR%` command.
...
```

4. Initialize project for Teensy 3.1 board with custom [Mbed](/hardware/frameworks/mbed)

```text
> pio project init --board teensy31 --project-option "framework=mbed"

The current working directory *** will be used for the new project.
You can specify another project directory via
`pio project init -d %PATH_TO_THE_PROJECT_DIR%` command.

...
```

5. Initialize a new project passing working environment name and its options

```text
> pio project init --environment native --project-option="platform=native" --project-option="build_flags=-DRELEASE=1"

The current working directory *** will be used for the new project.
...
```
