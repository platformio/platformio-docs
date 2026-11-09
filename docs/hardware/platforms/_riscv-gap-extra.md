## Configuration {#configuration}

### Drivers {#drivers}

See "Drivers" section for [FTDI Chip](../debug-probes/ftdi.md) debug probe.

### AutoTiler {#autotiler}

You need GAP8 AutoTiler library, please request it via [support@greenwaves-technologies.com](mailto:support@greenwaves-technologies.com)

Put a library somewhere on a disk and add this folder to library path using [build_flags](../../reference/platformio-ini/env/build-flags.md) in [`platformio.ini`](../../reference/platformio-ini/index.md). For example,

```ini
[env:gapuino]
platform = riscv_gap
board = gapuino
framework = ...
build_flags = -L/path/to/libtile/folder
```

### Running modes {#running-modes}

GAPuino supports 2 main modes:

1. Running from RAM, `boot_mode=jtag`
2. Running from HyperFlash, `boot_mode=jtag_hyper`

A running process can be controlled through the internal upload commands:

- `load`, @TODO
- `reqloop`, @TODO
- `ioloop`, @TODO
- `start`, @TODO
- `wait`, @TODO

You can configure "boot mode" and list of upload commands using [`platformio.ini`](../../reference/platformio-ini/index.md). Default values are:

- `board_upload.boot_mode = jtag`
- `board_upload.commands = load reqloop ioloop start wait`

#### Run from RAM {#run-from-ram}

This is a default behavior when you run "Upload" task in [PlatformIO IDE](../../get-started/platformio-ide.md) or use [PlatformIO Core (CLI)](../../get-started/platformio-core.md) and [`pio run --target`](../../reference/cli/pio-run.md#cmdoption-pio-run-t) command with `upload` target.

#### Run from RAM (without any bridge interaction) {#run-from-ram-without-any-bridge-interaction}

- Configure build environment using [`platformio.ini`](../../reference/platformio-ini/index.md) as described below

  ```ini
  [env:gapuino]
  platform = riscv_gap
  board = gapuino
  framework = ...
  board_upload.commands = load start
  ```

- Run "Upload" task in [PlatformIO IDE](../../get-started/platformio-ide.md) or use [PlatformIO Core (CLI)](../../get-started/platformio-core.md) and [`pio run --target`](../../reference/cli/pio-run.md#cmdoption-pio-run-t) command with `upload` target.

#### Flash and run from RAM {#flash-and-run-from-ram}

The same as [Uploading files to HyperFlash](/hardware/platforms/riscv-gap#platform-riscv-gap-uploadfs).

#### Flash and run from flash {#flash-and-run-from-flash}

- Configure build environment using [`platformio.ini`](../../reference/platformio-ini/index.md) as described below

  ```ini
  [env:gapuino]
  platform = riscv_gap
  board = gapuino
  framework = ...
  board_upload.boot_mode = jtag_hyper
  board_upload.commands = reqloop ioloop start wait
  ```

- Perform [Uploading files to HyperFlash](/hardware/platforms/riscv-gap#platform-riscv-gap-uploadfs).

#### Run from flash {#run-from-flash}

:::note

You have to perform [Uploading files to HyperFlash](/hardware/platforms/riscv-gap#platform-riscv-gap-uploadfs) before.

:::

- Configure build environment using [`platformio.ini`](../../reference/platformio-ini/index.md) as described below

  ```ini
  [env:gapuino]
  platform = riscv_gap
  board = gapuino
  framework = ...
  board_upload.boot_mode = jtag_hyper
  board_upload.commands = reqloop ioloop start wait
  ```

- Run "Upload" task in [PlatformIO IDE](../../get-started/platformio-ide.md) or use [PlatformIO Core (CLI)](../../get-started/platformio-core.md) and [`pio run --target`](../../reference/cli/pio-run.md#cmdoption-pio-run-t) command with `upload` target.

#### Run from flash (without any bridge interaction) {#run-from-flash-without-any-bridge-interaction}

:::note

You have to perform [Uploading files to HyperFlash](/hardware/platforms/riscv-gap#platform-riscv-gap-uploadfs) before.

:::

- Configure build environment using [`platformio.ini`](../../reference/platformio-ini/index.md) as described below

  ```ini
  [env:gapuino]
  platform = riscv_gap
  board = gapuino
  framework = ...
  board_upload.boot_mode = jtag_hyper
  board_upload.commands = start
  ```

- Run "Upload" task in [PlatformIO IDE](../../get-started/platformio-ide.md) or use [PlatformIO Core (CLI)](../../get-started/platformio-core.md) and [`pio run --target`](../../reference/cli/pio-run.md#cmdoption-pio-run-t) command with `upload` target.

<a id="platform-riscv-gap-uploadfs"></a>

### Uploading files to HyperFlash {#uploading-files-to-hyperflash}

1. Create new project using [PlatformIO IDE](../../get-started/platformio-ide.md) or initialize project using [PlatformIO Core (CLI)](../../get-started/platformio-core.md) and [pio project init](../../reference/cli/pio-project/init.md) (if you have not initialized it yet)
2. Create `data` folder (it should be on the same level as `src` folder) and put files here. Also, you can specify own location for [data_dir](../../reference/platformio-ini/platformio/data-dir.md)
3. Run "Upload File System image" task in [PlatformIO IDE](../../get-started/platformio-ide.md) or use [PlatformIO Core (CLI)](../../get-started/platformio-core.md) and [`pio run --target`](../../reference/cli/pio-run.md#cmdoption-pio-run-t) command with `uploadfs` target.

Examples:

- [PULP OS File System](https://github.com/pioplus/platform-riscv_gap/tree/develop/examples/gapuino-pulp-os-filesystem)
