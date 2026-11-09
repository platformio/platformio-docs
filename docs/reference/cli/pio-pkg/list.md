<a id="cmd-pkg-list"></a>

# pio pkg list {#pio-pkg-list}

## Usage {#usage}

```bash
pio pkg list [OPTIONS]
```

## Description {#description}

Print to stdout installed packages and their dependencies in a tree structure based on project dependencies declared in ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md):

- Library dependencies declared using the [lib_deps](../../platformio-ini/env/lib-deps.md) option
- Development platform declared using the [platform](../../platformio-ini/env/platform.md) option and its dependencies (toolchain, framework, SDKs, debugging server, etc)
- Custom tools declared using the [platform_packages](../../platformio-ini/env/platform-packages.md) option.

Globally installed packages can be listed using the [`pio pkg list --global`](#cmdoption-pio-pkg-list-g) option.

## Options {#options}

<a id="cmdoption-pio-pkg-list-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-pkg-list-d}

Specify the path to project directory. By default, `--project-dir` is equal to current working directory (`CWD`).

<a id="cmdoption-pio-pkg-list-environment"></a>

### `-e, --environment` {#cmdoption-pio-pkg-list-e}

List installed packages only for the specified environments. Multiple environments are allowed.

<a id="cmdoption-pio-pkg-list-platform"></a>

### `-p, --platform` {#cmdoption-pio-pkg-list-p}

Filter installed platform package using [Package Specifications](./install.md#cmd-pkg-install-specifications). Multiple items are allowed.

<a id="cmdoption-pio-pkg-list-tool"></a>

### `-t, --tool` {#cmdoption-pio-pkg-list-t}

Filter installed tool package using [Package Specifications](./install.md#cmd-pkg-install-specifications). Multiple items are allowed.

<a id="cmdoption-pio-pkg-list-library"></a>

### `-l, --library` {#cmdoption-pio-pkg-list-l}

Filter installed library package using [Package Specifications](./install.md#cmd-pkg-install-specifications). Multiple items are allowed.

<a id="cmdoption-pio-pkg-list-global"></a>

### `-g, --global` {#cmdoption-pio-pkg-list-g}

List installed packages from the global storage:

- [platforms_dir](../../platformio-ini/platformio/platforms-dir.md) - development platforms
- [packages_dir](../../platformio-ini/platformio/packages-dir.md) - tools
- [globallib_dir](../../platformio-ini/platformio/globallib-dir.md) - libraries.

### `--storage-dir` {#cmdoption-pio-pkg-list-storage-dir}

Specify a custom Package Manager storage for global packages.

### `--only-platforms` {#cmdoption-pio-pkg-list-only-platforms}

Print only installed platform packages.

### `--only-tools` {#cmdoption-pio-pkg-list-only-tools}

Print only installed tool packages.

### `--only-libraries` {#cmdoption-pio-pkg-list-only-libraries}

Print only installed library packages.

<a id="cmdoption-pio-pkg-list-verbose"></a>

### `-v, --verbose` {#cmdoption-pio-pkg-list-v}

Print additional package information.

## See Also {#see-also}

- [pio pkg outdated](./outdated.md)
- [pio pkg install](./install.md)
- [pio pkg update](./update.md)
- [pio pkg uninstall](./uninstall.md)
- [library.json](../../library-json/index.md)
