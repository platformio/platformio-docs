<a id="cmd-pkg-update"></a>

# pio pkg update {#pio-pkg-update}

## Usage {#usage}

```bash
pio pkg update [OPTIONS]
```

## Description {#description}

Update the project dependencies, custom packages from the [PlatformIO Registry](https://registry.platformio.org), or external sources.

If no custom packages (`--library`, `--platform`, or `--tool`) are specified, the command will update the following project dependencies based on ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md):

- Library dependencies declared using the [lib_deps](../../platformio-ini/env/lib-deps.md) option
- Development platform declared using the [platform](../../platformio-ini/env/platform.md) option and its dependencies (toolchain, framework, SDKs, debugging server, etc)
- Custom tools declared using the [platform_packages](../../platformio-ini/env/platform-packages.md) option.

See [pio pkg install](./install.md) command for package specification.

## Options {#options}

<a id="cmdoption-pio-pkg-update-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-pkg-update-d}

Specify the path to project directory. By default, `--project-dir` is equal to current working directory (`CWD`).

<a id="cmdoption-pio-pkg-update-environment"></a>

### `-e, --environment` {#cmdoption-pio-pkg-update-e}

Update project dependencies only for the specified environments. Multiple environments are allowed.

<a id="cmdoption-pio-pkg-update-platform"></a>

### `-p, --platform` {#cmdoption-pio-pkg-update-p}

Update specified development platform. Multiple items are allowed.

**Examples**

```bash
pio pkg update -p "aceinna/aceinna_imu@^1.3.8" -p "platformio/atmelavr"
pio pkg update --platform "https://github.com/platformio/platform-sifive.git"
```

<a id="cmdoption-pio-pkg-update-tool"></a>

### `-t, --tool` {#cmdoption-pio-pkg-update-t}

Update specified tool. Multiple items are allowed.

**Examples**

```bash
pio pkg update -t "platformio/tool-openocd"
pio pkg update --tool https://github.com/platformio/platform-sifive.git
```

<a id="cmdoption-pio-pkg-update-library"></a>

### `-l, --library` {#cmdoption-pio-pkg-update-l}

Update specified library. Multiple items are allowed.

**Examples**

```bash
pio pkg update -l "bblanchon/ArduinoJson@^6.19.2" -l "milesburton/DallasTemperature@^3.9.1"
pio pkg update --library https://github.com/Makuna/NeoPixelBus.git
```

### `--no-save` {#cmdoption-pio-pkg-update-no-save}

Prevent saving specified packages to ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md).

### `--skip-dependencies` {#cmdoption-pio-pkg-update-skip-dependencies}

Update a package but skip its dependencies declared in the manifest [dependencies](../../library-json/dependencies.md) field.

<a id="cmdoption-pio-pkg-update-global"></a>

### `-g, --global` {#cmdoption-pio-pkg-update-g}

Update packages from the global storage:

- [platforms_dir](../../platformio-ini/platformio/platforms-dir.md) - development platforms
- [packages_dir](../../platformio-ini/platformio/packages-dir.md) - tools
- [globallib_dir](../../platformio-ini/platformio/globallib-dir.md) - libraries.

### `--storage-dir` {#cmdoption-pio-pkg-update-storage-dir}

Specify a custom Package Manager storage for global packages.

<a id="cmdoption-pio-pkg-update-silent"></a>

### `-s, --silent` {#cmdoption-pio-pkg-update-s}

Suppress progress reporting.

## See Also {#see-also}

- [pio pkg outdated](./outdated.md)
- [pio pkg install](./install.md)
- [pio pkg uninstall](./uninstall.md)
- [library.json](../../library-json/index.md)
