---
description: "# or short format."
---

## Installation {#installation}

PlatformIO does not install automatically any toolchains for the **native** development platform. It depends on the system `GCC` toolchain that must be added to the `PATH` system environment variable.

Open the system terminal and type `gcc --version`. If the `gcc` command is not found, you have to install the GCC toolchain manually depending on your operating system:

- **Windows** - follow the [MSYS2](https://www.msys2.org/) installation guide and add the following paths to the `PATH` system environment variable:

  ```text
  C:\msys64\mingw64\bin
  C:\msys64\ucrt64\bin
  C:\msys64\usr\bin
  ```

- **Linux** - open the system terminal and run the following commands:

  ```bash
  sudo apt update
  sudo apt install build-essential
  ```

- **macOS** - open the system terminal and install Xcode Command Line Tools

  ```bash
  xcode-select --install
  ```

## Running of program {#running-of-program}

To execute a native program, you need to use `exec` target for the [`pio run --target`](../../reference/cli/pio-run.md#cmdoption-pio-run-t) command. Extra program arguments can be passed using the [`pio run --program-arg`](../../reference/cli/pio-run.md#cmdoption-pio-run-a) option.

**Example**

```bash
> pio run -t exec

# extra args
> pio run -t exec --program-arg "arg1" --program-arg="--option1=value1"

# or short format
> pio run -t exec -a "arg1" -a "--option1=value1"
```
