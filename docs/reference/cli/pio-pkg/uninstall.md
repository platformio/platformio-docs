---
description: "Uninstall the project dependencies or custom packages from the PlatformIO Registry or external sources."
---

<a id="cmd-pkg-uninstall"></a>

# pio pkg uninstall {#pio-pkg-uninstall}

## Usage {#usage}

```bash
pio pkg uninstall [OPTIONS]
```

## Description {#description}

Uninstall the project dependencies or custom packages from the [PlatformIO Registry](https://registry.platformio.org) or external sources.

If no custom packages (`--library`, `--platform`, or `--tool`) are specified, the command will uninstall the following project dependencies based on [`platformio.ini`](../../platformio-ini/index.md):

- Library dependencies declared using the [lib_deps](../../platformio-ini/env/lib-deps.md) option
- Development platform declared using the [platform](../../platformio-ini/env/platform.md) option and its dependencies (toolchain, framework, SDKs, debugging server, etc)
- Custom tools declared using the [platform_packages](../../platformio-ini/env/platform-packages.md) option.

See [pio pkg install](./install.md) command for package specification.

## Options {#options}

<a id="cmdoption-pio-pkg-uninstall-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-pkg-uninstall-d}

The project directory. Default: the current working directory.

<a id="cmdoption-pio-pkg-uninstall-environment"></a>

### `-e, --environment` {#cmdoption-pio-pkg-uninstall-e}

Uninstall project dependencies only for the specified environments. Repeat the option for several environments.

<a id="cmdoption-pio-pkg-uninstall-platform"></a>

### `-p, --platform` {#cmdoption-pio-pkg-uninstall-p}

Uninstall specified development platform using [Package Specifications](./install.md#cmd-pkg-install-specifications). Repeat the option for several packages.

**Examples**

```bash
pio pkg uninstall -p "platformio/espressif32@^6" -p "platformio/atmelavr"
pio pkg uninstall --platform "https://github.com/platformio/platform-sifive.git"
```

<a id="cmdoption-pio-pkg-uninstall-tool"></a>

### `-t, --tool` {#cmdoption-pio-pkg-uninstall-t}

Uninstall specified tool using [Package Specifications](./install.md#cmd-pkg-install-specifications). Repeat the option for several packages.

**Examples**

```bash
pio pkg uninstall -t "platformio/tool-openocd"
pio pkg uninstall --tool https://github.com/platformio/platform-sifive.git
```

<a id="cmdoption-pio-pkg-uninstall-library"></a>

### `-l, --library` {#cmdoption-pio-pkg-uninstall-l}

Uninstall specified library using [Package Specifications](./install.md#cmd-pkg-install-specifications). Repeat the option for several packages.

**Examples**

```bash
pio pkg uninstall -l "bblanchon/ArduinoJson@^6.19.2" -l "milesburton/DallasTemperature@^3.9.1"
pio pkg uninstall --library https://github.com/Makuna/NeoPixelBus.git
```

### `--no-save` {#cmdoption-pio-pkg-uninstall-no-save}

Prevent removing specified packages from [`platformio.ini`](../../platformio-ini/index.md).

### `--skip-dependencies` {#cmdoption-pio-pkg-uninstall-skip-dependencies}

Uninstall a package and keep its dependencies declared in the manifest [dependencies](../../library-json/dependencies.md) field.

<a id="cmdoption-pio-pkg-uninstall-global"></a>

### `-g, --global` {#cmdoption-pio-pkg-uninstall-g}

Uninstall packages from the global storage:

- [platforms_dir](../../platformio-ini/platformio/platforms-dir.md) - development platforms
- [packages_dir](../../platformio-ini/platformio/packages-dir.md) - tools
- [globallib_dir](../../platformio-ini/platformio/globallib-dir.md) - libraries.

### `--storage-dir` {#cmdoption-pio-pkg-uninstall-storage-dir}

Specify a custom Package Manager storage for global packages.

<a id="cmdoption-pio-pkg-uninstall-silent"></a>

### `-s, --silent` {#cmdoption-pio-pkg-uninstall-s}

Suppress progress reporting.

## See also {#see-also}

- [pio pkg install](./install.md)
- [pio pkg outdated](./outdated.md)
- [library.json](../../library-json/index.md)
