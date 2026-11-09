---
sidebar_label: "Integrate into your application"
description: Install PlatformIO Core automatically from your IDE extension, plugin or application with the installer script.
---

# Integrate PlatformIO Core into your application {#integration-with-custom-applications-extensions-plugins}

This page is for developers of IDE extensions, plugins and other applications
that need PlatformIO Core on the user's computer. Use the
[installer script](https://github.com/platformio/platformio-core-installer) to
check for an existing installation and install PlatformIO Core when it is
missing. PlatformIO IDE for VS Code works this way, through
[platformio-node-helpers](https://github.com/platformio/platformio-node-helpers).

## Prerequisites {#prerequisite}

### Python {#python-interpreter}

The installer script runs on Python 2.7 or later, but PlatformIO Core needs
Python 3.9 or later, so make sure a recent Python 3 is available. macOS and most Linux distributions include Python; check with
`python3 --version`. If the user's computer has no Python, either:

- ask the user to [install Python](../../resources/faq/install-python.md), or
- download a portable Python from the
  [PlatformIO Registry](https://api.registry.platformio.org/v3/packages/platformio/tool/python-portable),
  unpack it into your application's cache folder, and run the installer script
  with its `python.exe`.

### The installer script {#installer-script}

Get [get-platformio.py](https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py)
onto the user's computer, for example into a cache or temporary folder. You
can bundle it with your application or download it on demand.

To list its commands and options:

```bash
python get-platformio.py --help
```

## Workflow {#workflow}

### 1. Check for an existing installation {#step-1-where-is-platformio-core-installed}

Each time your application starts, check whether PlatformIO Core is installed
and ready:

```bash
python get-platformio.py check core
```

Exit code `0` means it is ready. Any other exit code means you need to
[install it](#step-2-install-platformio-core).

To get the details of the installation, write them to a JSON file with
`--dump-state`:

```bash
python get-platformio.py check core --dump-state tmpdir/pioinstaller-state.json
```

Example output on macOS:

```json
{
  "cache_dir": "/Users/Freedom/.platformio/.cache",
  "core_dir": "/Users/Freedom/.platformio",
  "core_version": "4.3.1",
  "installer_version": "0.2.0",
  "is_develop_core": false,
  "penv_bin_dir": "/Users/Freedom/.platformio/penv/bin",
  "penv_dir": "/Users/Freedom/.platformio/penv",
  "platformio_exe": "/Users/Freedom/.platformio/penv/bin/platformio",
  "python_exe": "/Users/Freedom/.platformio/penv/bin/python",
  "system": "darwin_x86_64"
}
```

Run PlatformIO Core with the `platformio_exe` path, or add `penv_bin_dir` to
the `PATH` of the processes you start so that `pio` is found by name.

### 2. Install PlatformIO Core {#step-2-install-platformio-core}

Run the installer script without arguments:

```bash
python get-platformio.py
```

It installs PlatformIO Core into a virtual environment and returns exit code
`0` on success, or a non-zero code and an error message on failure. Useful
options:

| Option | Description |
| --- | --- |
| `--verbose` | Print detailed output |
| `--dev` | Install the [development version](./development-version.md) |
| `--ignore-python` | A Python interpreter to skip; accepts Unix wildcards and can be repeated |

After installation, continue with [step 1](#step-1-where-is-platformio-core-installed)
on every start.

## Examples {#examples}

- [platformio-node-helpers](https://github.com/platformio/platformio-node-helpers),
  used by [PlatformIO IDE for VS Code](https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide).
