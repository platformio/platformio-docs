# Integration with custom applications (extensions, plugins) {#integration-with-custom-applications-extensions-plugins}

We recommend using PlatformIO Core **Installer Script** when you integrate PlatformIO Core into an application, such as an extension or plugin for IDE.

## Prerequisite {#prerequisite}

### Python Interpreter {#python-interpreter}

PlatformIO Core Installer Script is written in Python and is compatible with Python 2.7+ and Python 3.9+. **We highly recommend using the latest Python 3**.

Python is installed by default on the most popular Unix OS (macOS, Linux, FreeBSD). If there is no Python on a user machine (you can check running `python --version`), we have 2 options:

1. Ask the user to install Python 3 using our guide [Install Python Interpreter](../../resources/faq/install-python.md)
2. You can automatically [Download Portable Python 3 (API)](https://api.registry.platformio.org/v3/packages/platformio/tool/python-portable) and unpack it in a cache folder of your application. Later, you can use `unpacked_protable_python_dir/python.exe` for the installer script.

### Installer Script {#installer-script}

There are 2 options on how to work with PlatformIO Core Installer Script:

1. Bundle [get-platformio.py](https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py) file into your application
2. Download [get-platformio.py](https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py) file on demand.

In both cases, you will need to have `get-platformio.py` script on the end-user machine. You can copy or download it to a cache/temporary folder.

A list of arguments and options for the installer script is available via

```bash
python get-platformio.py --help
```

## Workflow {#workflow}

We will describe a simple workflow on how to automatically install [PlatformIO Core (CLI)](../platformio-core.md) for end-user of your application/extension. We assume that `get-platformio.py` script is already copied/downloaded and exists on the end-user machine. See above for how to get it.

### Step 1. Where is PlatformIO Core installed? {#step-1-where-is-platformio-core-installed}

You should check the PlatformIO Core installation state **each time** when the user starts your application. You need to call the Installer Script with `check core` arguments:

```bash
python get-platformio.py check core
```

This command returns `0` "exit code" when PlatformIO Core is already installed and is ready for use, otherwise, the non-zero code of the subprocess will be returned and you need to install PlatformIO Core (see **Step #2** below).

If you need to have full information about the PlatformIO Core installation state, please run with `--dump-state` option and specify a folder or a full path where to save data in JSON format:

```bash
get-platformio.py check core --dump-state tmpdir/pioinstaller-state.json
```

Now, read JSON file and use `platformio_exe` binary to call PlatforIO Core using CLI (see [CLI Guide](../../reference/cli/index.md)). You can also export `penv_bin_dir` into the system environment `PATH` variable and the `platformio` command will be available without a full path.

Example of `pioinstaller-state.json` run on macOS:

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

### Step 2. Install PlatformIO Core {#step-2-install-platformio-core}

To install PlatformIO Core into the virtual environment in an automatic mode, please call the installer script without any arguments:

```bash
python get-platformio.py
```

Available options:

- `--verbose`, verbose output
- `--dev`, install the latest development version of PlatformIO Core
- `--ignore-python`, a path to Python to be ignored (multiple options and Unix wildcards are allowed)

More options are available at `python get-platformio.py --help`.

Installer Script will return exit code `0` on success, otherwise non-zero code and error explanation.

Next time just use again `python get-platformio.py check core` as described in Step #1 (see above).

## Examples {#examples}

Examples that use this installer are:

- [platformio-node-helpers](https://github.com/platformio/platformio-node-helpers), is used by [PlatformIO IDE for VSCode](https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide)
