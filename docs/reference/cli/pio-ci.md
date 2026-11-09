---
description: "pio ci command is conceived of as 'hot key' for building project with arbitrary source code structure."
---

# pio ci

## Usage {#usage}

```bash
pio ci [OPTIONS] [SRC]
```

## Description {#description}

pio ci command is conceived of as "hot key" for building project with arbitrary source code structure. In a nutshell, using `SRC` and [`pio ci --lib`](#cmdoption-pio-ci-l) contents PlatformIO initializes via [pio project init](./pio-project/init.md) new project in [`pio ci --build-dir`](#cmdoption-pio-ci-build-dir) with the build environments (using [`pio ci --board`](#cmdoption-pio-ci-b) or [`pio ci --project-conf`](#cmdoption-pio-ci-c)) and processes them via [pio run](./pio-run.md) command.

pio ci command accepts **multiple** `SRC` arguments, [`pio ci --lib`](#cmdoption-pio-ci-l) and [`pio ci --exclude`](#cmdoption-pio-ci-exclude) options which can be a path to directory, file or [Glob Pattern](http://en.wikipedia.org/wiki/Glob_%28programming%29). You can also omit `SRC` and set the paths in the [`PLATFORMIO_CI_SRC`](../environment-variables.md#envvar-PLATFORMIO_CI_SRC) environment variable, separated by `:` on macOS and Linux or `;` on Windows

For more details as for integration with the popular Continuous Integration Systems see [Continuous Integration](../../guides/ci/index.md) page.

:::note

pio ci command is useful for library developers. It allows one to build different examples without creating own project per them.

:::

## Options {#options}

<a id="cmdoption-pio-ci-lib"></a>

### `-l, --lib` {#cmdoption-pio-ci-l}

Source code which will be copied to `<BUILD_DIR>/lib` directly.

If [`pio ci --lib`](#cmdoption-pio-ci-l) is a path to file (not to directory), then PlatformIO will create temporary directory within `<BUILD_DIR>/lib` and copy the rest files into it.

### `--exclude` {#cmdoption-pio-ci-exclude}

Exclude directories and/-or files from [`pio ci --build-dir`](#cmdoption-pio-ci-build-dir). The path must be relative to PlatformIO project within [`pio ci --build-dir`](#cmdoption-pio-ci-build-dir).

For example, exclude from project `src` directory:

- `examples` folder
- `*.h` files from `foo` folder

```bash
pio ci --exclude=src/examples --exclude=src/foo/*.h [SRC]
```

<a id="cmdoption-pio-ci-board"></a>

### `-b, --board` {#cmdoption-pio-ci-b}

Build project with automatically pre-generated environments based on board settings.

For more details please look into [`pio project init --board`](./pio-project/init.md#cmdoption-pio-project-init-b).

### `--build-dir` {#cmdoption-pio-ci-build-dir}

Path to directory where PlatformIO will initialise new project. By default it's temporary directory within your operating system.

:::note

This directory will be removed at the end of build process. If you want to keep it, please use [`pio ci --keep-build-dir`](#cmdoption-pio-ci-keep-build-dir).

:::

### `--keep-build-dir` {#cmdoption-pio-ci-keep-build-dir}

Don't remove [`pio ci --build-dir`](#cmdoption-pio-ci-build-dir) after build process.

<a id="cmdoption-pio-ci-project-conf"></a>

### `-c, --project-conf` {#cmdoption-pio-ci-c}

Build project using pre-configured [`platformio.ini`](../platformio-ini/index.md).

<a id="cmdoption-pio-ci-project-option"></a>

### `-O, --project-option` {#cmdoption-pio-ci-O}

Pass additional options from [`platformio.ini`](../platformio-ini/index.md) to [pio project init](./pio-project/init.md) command. For example, automatically install dependent libraries `pio ci --project-option="lib_deps=ArduinoJSON"` or ignore specific library `pio ci --project-option="lib_ignore=SomeLib"`.

:::note

Use multiple `--project-option` to pass multiple options to [`platformio.ini`](../platformio-ini/index.md). One option per one argument. For example, `pio ci --project-option="build_unflags = -std=gnu++11" --project-option="build_flags = -std=c++14"`

:::

<a id="cmdoption-pio-ci-environment"></a>

### `-e, --environment` {#cmdoption-pio-ci-e}

Process specified environments declared in [`pio ci --project-conf`](#cmdoption-pio-ci-c). Repeat the option for several environments.

<a id="cmdoption-pio-ci-verbose"></a>

### `-v, --verbose` {#cmdoption-pio-ci-v}

Print detailed information while processing environments.

This option can also be set globally using [force_verbose](./pio-settings.md#setting-force-verbose) setting or by environment variable [`PLATFORMIO_SETTING_FORCE_VERBOSE`](../environment-variables.md#envvar-PLATFORMIO_SETTING_FORCE_VERBOSE).

## Examples {#examples}

For the others examples see [Continuous Integration](../../guides/ci/index.md) page.
