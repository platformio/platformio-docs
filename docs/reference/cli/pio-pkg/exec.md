<a id="cmd-pkg-exec"></a>

# pio pkg exec {#pio-pkg-exec}

## Usage {#usage}

```bash
pio pkg exec [OPTIONS] [ARGS]
pio pkg exec -- <CMD> [ARGS]
pio pkg exec --package <SPECIFICATION> -- <CMD> [ARGS]
pio pkg exec --call '<cmd> [args]'
```

## Description {#description}

Run command from a PlatformIO package.

:::note

A double-hyphen `--` flag is required before a command when passing its options.

:::

## Options {#options}

<a id="cmdoption-pio-pkg-exec-package"></a>

### `-p, --package` {#cmdoption-pio-pkg-exec-p}

Run a command from the specified package using [Package Specifications](./install.md#cmd-pkg-install-specifications). If a package has not been installed yet, PlatformIO will install it from the [PlatformIO Registry](https://registry.platformio.org).

If a package is not provided, run an arbitrary command from the first matched installed package.

<a id="cmdoption-pio-pkg-exec-call"></a>

### `-c, --call` {#cmdoption-pio-pkg-exec-c}

Run a command and its arguments specified as a string.

## Examples {#examples}

1. Run an arbitrary command from the first matched installed package

```text
> pio pkg exec -- openocd --help

OpenOCD x86_64 Open On-Chip Debugger 0.11.0+dev (2021-10-17-00:18)
Licensed under GNU GPL v2
For bug reports, read
    http://openocd.org/doc/doxygen/bugs.html
Open On-Chip Debugger
Licensed under GNU GPL v2
--help       | -h   display this help
--version    | -v   display OpenOCD version
--file       | -f   use configuration file <name>
--search     | -s   dir to search for config files and scripts
--debug      | -d   set debug level to 3
             | -d<n>    set debug level to <level>
--log_output | -l   redirect log output to file <name>
--command    | -c   run <command>
```

2. Install JLink package and run GDB server

```text
> pio pkg exec -p tool-jlink -- JLinkGDBServer -singlerun -if JTAG -select USB -jtagconf -1,-1 -device EFR32BG22CxxxF512 -port 2331
```
