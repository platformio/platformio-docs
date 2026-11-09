---
description: "Install the project dependencies or custom packages from the PlatformIO Registry or external sources."
---

# pio pkg install

## Usage {#usage}

```bash
pio pkg install [OPTIONS]
```

## Description {#description}

Install the project dependencies or custom packages from the [PlatformIO Registry](https://registry.platformio.org) or external sources.

If no custom packages (`--library`, `--platform`, or `--tool`) are specified, the command will install the following project dependencies based on [`platformio.ini`](../../platformio-ini/index.md):

- Library dependencies declared using the [lib_deps](../../platformio-ini/env/lib-deps.md) option
- Development platform declared using the [platform](../../platformio-ini/env/platform.md) option and its dependencies (toolchain, framework, SDKs, debugging server, etc)
- Custom tools declared using the [platform_packages](../../platformio-ini/env/platform-packages.md) option.

## Options {#options}

<a id="cmdoption-pio-pkg-install-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-pkg-install-d}

The project directory. Default: the current working directory.

<a id="cmdoption-pio-pkg-install-environment"></a>

### `-e, --environment` {#cmdoption-pio-pkg-install-e}

Install project dependencies only for the specified environments. Repeat the option for several environments.

<a id="cmdoption-pio-pkg-install-platform"></a>

### `-p, --platform` {#cmdoption-pio-pkg-install-p}

Install specified development platform using [Package Specifications](#cmd-pkg-install-specifications). Repeat the option for several packages.

**Examples**

```bash
pio pkg install -p "platformio/espressif32@^6" -p "platformio/atmelavr"
pio pkg install --platform "https://github.com/platformio/platform-sifive.git"
```

<a id="cmdoption-pio-pkg-install-tool"></a>

### `-t, --tool` {#cmdoption-pio-pkg-install-t}

Install specified tool using [Package Specifications](#cmd-pkg-install-specifications). Repeat the option for several packages.

**Examples**

```bash
pio pkg install -t "platformio/tool-openocd"
pio pkg install --tool https://github.com/platformio/platform-sifive.git
```

<a id="cmdoption-pio-pkg-install-library"></a>

### `-l, --library` {#cmdoption-pio-pkg-install-l}

Install specified library using [Package Specifications](#cmd-pkg-install-specifications). Repeat the option for several packages.

**Examples**

```bash
pio pkg install -l "bblanchon/ArduinoJson@^6.19.2" -l "milesburton/DallasTemperature@^3.9.1"
pio pkg install --library https://github.com/Makuna/NeoPixelBus.git
```

### `--no-save` {#cmdoption-pio-pkg-install-no-save}

Prevent saving specified packages to [`platformio.ini`](../../platformio-ini/index.md).

### `--skip-dependencies` {#cmdoption-pio-pkg-install-skip-dependencies}

Install a package but skip its dependencies declared in the manifest [dependencies](../../library-json/dependencies.md) field.

<a id="cmdoption-pio-pkg-install-global"></a>

### `-g, --global` {#cmdoption-pio-pkg-install-g}

:::warning

We **DO NOT recommend installing** libraries in the global storage. Use the [lib_deps](../../platformio-ini/env/lib-deps.md) option and declare library dependencies per project.

:::

Install packages to the global storage:

- [platforms_dir](../../platformio-ini/platformio/platforms-dir.md) - development platforms
- [packages_dir](../../platformio-ini/platformio/packages-dir.md) - tools
- [globallib_dir](../../platformio-ini/platformio/globallib-dir.md) - libraries.

A package installed to the global storage will be available for any PlatformIO project.

### `--storage-dir` {#cmdoption-pio-pkg-install-storage-dir}

Specify a custom Package Manager storage for global packages.

<a id="cmdoption-pio-pkg-install-force"></a>

### `-f, --force` {#cmdoption-pio-pkg-install-f}

Reinstall a package if exists. The existing package will be removed and the latest compatible version will be installed.

<a id="cmdoption-pio-pkg-install-silent"></a>

### `-s, --silent` {#cmdoption-pio-pkg-install-s}

Suppress progress reporting.

<a id="cmd-pkg-install-types"></a>

## Package Types {#package-types}

PlatformIO supports the next package types:

<dl>

<dt>

`library`

</dt>

<dd>

The Assembly/C/C++ files that can extend project functionality

</dd>

<dt>

`platform`

</dt>

<dd>

See [Development Platforms](../../../hardware/platforms/index.md) for details

</dd>

<dt>

`tool`

</dt>

<dd>

A specialized program, toolchain, or source of auxiliary files (framework, SDK) that are used to build a project, debug it or upload firmware to the target device.

</dd>

</dl>

Browse over 10,000 packages in the [PlatformIO Registry](https://registry.platformio.org).

<a id="cmd-pkg-install-specifications"></a>

## Package Specifications {#package-specifications}

PlatformIO supports different package sources which you can specify for pio pkg install command or configure project dependencies using [`platformio.ini`](../../platformio-ini/index.md) options:

- [platform](../../platformio-ini/env/platform.md) - development platform
- [platform_packages](../../platformio-ini/env/platform-packages.md) - custom tools/packages
- [lib_deps](../../platformio-ini/env/lib-deps.md) - libraries.

A `package` is:

1. A folder containing manifest file ([library.json](../../library-json/index.md), `platform.json` or `package.json`)
2. TAR or ZIP archive containing (a)
3. A URL that resolves to (b)
4. An `<owner>/<name>@<version requirements>` that is published on the [PlatformIO Registry](https://registry.platformio.org)
5. A \<git/hg/svn remote url> that resolves to (a).

### Registry: Latest Version {#registry-latest-version}

**Specification:** `<owner>/<name>`

Install the latest package version from the [PlatformIO Registry](https://registry.platformio.org).

:::tip

We highly recommend pinning a package to a [Registry: Specific Version](#cmd-pkg-install-specific-version) and to prefix the version with the `^` (caret) symbol. This will instruct PlatformIO to install the latest compatible version avoiding breaking changes in the future. See [Version Requirements](#cmd-pkg-install-requirements) for details.

:::

**Examples**

1. Install [ArduinoJson](https://registry.platformio.org/libraries/bblanchon/ArduinoJson) and [Embedded Template](https://registry.platformio.org/libraries/etlcpp/Embedded%20Template%20Library) libraries, and add them to the project dependencies ([lib_deps](../../platformio-ini/env/lib-deps.md)):

   ```bash
   pio pkg install --library "bblanchon/ArduinoJson" --library "etlcpp/Embedded Template Library"
   ```

2. Declare [ArduinoJson](https://registry.platformio.org/libraries/bblanchon/ArduinoJson) and [Embedded Template](https://registry.platformio.org/libraries/etlcpp/Embedded%20Template%20Library) libraries as the project dependencies using [lib_deps](../../platformio-ini/env/lib-deps.md) configuration option:

   ```ini
   [env:myenv]
   lib_deps =
       bblanchon/ArduinoJson
       etlcpp/Embedded Template Library
   ```

3. Install [SEGGER J-Link Software](https://registry.platformio.org/tools/platformio/tool-jlink) for debug probes:

   ```bash
   pio pkg install --tool "platformio/tool-jlink"
   ```

<a id="cmd-pkg-install-specific-version"></a>

### Registry: Specific Version {#registry-specific-version}

**Specification:** `<owner>/<name>@<version>`

Install the specified version of a package from the [PlatformIO Registry](https://registry.platformio.org). This will fail if the version has not been published to the registry.

**Example**

```bash
bblanchon/ArduinoJson@6.9.12
```

### Registry: Version Requirements {#registry-version-requirements}

**Specification:** `<owner>/<name>@<version requirements>`

Install the latest version of a package from the [PlatformIO Registry](https://registry.platformio.org) matching the specified version requirements. See [Version Requirements](#cmd-pkg-install-requirements) for details.

**Example**

```bash
bblanchon/ArduinoJson@>=6,!=6.13.0
```

### Repository (git, hg, svn) {#repository-git-hg-svn}

**Specification:** `[<name>=][<scheme>://][<user>[:<password>]@]<hostname>[:<port>][:][/]<path>[#<commit-ish|branch|tag>]`

Install the package at the specified URL by attempting to clone it. If the repository makes use of submodules, those submodules will be cloned as well.

The supported schemes are:

- `http`
- `https`
- `git`
- `git+http`
- `git+https`
- `git+ssh`
- `hg+http`
- `hg+https`
- `hg+ssh`
- `svn+http`
- `svn+https`
- `svn+ssh`

You can override a package folder name in the Package Manager storage using the `<name>=` syntax. See the example below.

**Examples**

1. Clone default branch of Github repository using HTTPS

   ```bash
   https://github.com/platformio/platform-espressif32.git
   ```

2. Clone default branch of Github repository using SSH

   ```bash
   git@github.com:platformio/platform-espressif32.git

   # or

   git+username@github.com:platformio/platform-espressif32.git
   ```

3. Clone Git repository using SSH and custom username

   ```bash
   git+ssh://git.server.org/my-platform

   # or

   git+ssh://user@git.server.org/my-platform
   ```

4. Clone "master" branch of Git repository

   ```bash
   https://github.com/platformio/platform-espressif32.git#master
   ```

5. Clone "v3.3.0" tag of Git repository

   ```bash
   https://github.com/platformio/platform-espressif32.git#v3.3.0
   ```

6. Clone specified commit of Git repository

   ```bash
   https://github.com/platformio/platform-espressif32.git#084131f6634c818485781651d76818cd1f13a461
   ```

7. Clone specified commit of Git repository and set custom package folder name to "ESP32"

   ```bash
   ESP32=https://github.com/platformio/platform-espressif32.git#084131f6634c818485781651d76818cd1f13a461
   ```

8. Clone Mercurial repository

   ```bash
   hg+hg://hg.server.org/my-package
   hg+https://hg.server.org/my-package
   hg+ssh://hg.server.org/my-package
   ```

<a id="cmd-pkg-install-local-folder"></a>

### Local Folder {#local-folder}

| Specification | Description |
|---|---|
| `[<name>=]file://<folder>` | Copy all files from the local folder to the Package Manager. Making changes in the source folder **WILL NOT** affect the installed package. |
| `[<name>=]symlink://<folder>` | Create a symbolic link pointing the local source folder to the Package Manager. Making changes in the source folder **WILL** affect the installed package. |

Install a package and its [dependencies](../../library-json/dependencies.md) from a local folder. A path should start with `file://` or `symlink://` prefix and the package folder must contain a manifest file ([library.json](../../library-json/index.md), `platform.json`, or `package.json`) with name and version properties.

You can override a package folder name in the Package Manager storage using the `<name>=` syntax. See the example below.

**Examples**

```bash
# Unix, hard copying
file:///local/path/to/the/package/dir

# Windows, symbolic link
symlink://C:/local/path/to/the/package/dir

# Custom package folder name "SomeLib" in the storage
SomeLib=file:///local/path/to/the/package/dir
```

### Local TAR or ZIP archive {#local-tar-or-zip-archive}

**Specification:** `[<name>=]file://<tar or zip file>`

Install a package and its [dependencies](../../library-json/dependencies.md) from a local TAR or ZIP archive.

Archive requirements:

- the filename must use `.tar.gz`, `.tar`, `.tgz`, or `.zip` as the extension
- the package must contain a manifest file ([library.json](../../library-json/index.md), `platform.json`, or `package.json`) with `name` and `version` properties.

You can override a package folder name in the Package Manager storage using the `<name>=` syntax. See the example below.

**Examples**

```bash
# tar.gz
file:///local/path/to/the/archive.tar.gz

# zip
file:///local/path/to/the/archive.zip

# Custom package folder name "SomeLib" in the storage
SomeLib=file:///local/path/to/the/archive.tar.gz
```

### Remote TAR or ZIP archive {#remote-tar-or-zip-archive}

**Specification:** `[<name>=]<archive url>`

Fetch the archive URL, and then install a package and its [dependencies](../../library-json/dependencies.md). The URL must start with `http://` or `https://`.

You can override a package folder name in the Package Manager storage using the `<name>=` syntax. See the example below.

**Examples**

```bash
# TAR archive
https://github.com/bblanchon/ArduinoJson/archive/refs/heads/6.x.tar.gz

# ZIP archive
https://github.com/bblanchon/ArduinoJson/archive/refs/heads/6.x.zip

# Custom package folder name "JSON" in the storage
JSON=https://github.com/bblanchon/ArduinoJson/archive/refs/heads/6.x.tar.gz
```

<a id="cmd-pkg-install-requirements"></a>

## Version Requirements {#version-requirements}

:::note

PlatformIO uses [python-semanticversion](https://github.com/rbarrois/python-semanticversion) library to handle SemVer versions and specifications.

:::

The `@<version requirements>` specification supports [Semantic Versioning](https://semver.org/) ( `<MAJOR>.<MINOR>.<PATCH>`):

- `MAJOR` - incompatible API changes
- `MINOR` - add functionality (backwards-compatible)
- `PATCH` - bug fixes (backwards-compatible).

The version requirements can take any of the following forms (see [Semver cheatsheet](https://devhints.io/semver)):

- `^1.2.3` - any compatible version (new functionality in a backwards compatible manner and patches are allowed, 1.x.x). **RECOMMENDED**
- `~1.2.3` - any version with the same major and minor versions, and an equal or greater patch version
- `>1.2.3` - any version greater than `1.2.3`. `>=`, `<`, and `<=` are also possible
- `>0.1.0,!=0.2.0,<0.3.0` - any version greater than `0.1.0`, not equal to `0.2.0` and less than `0.3.0`
- `1.2.3` - an exact version number. Use only this exact version.

To list available package versions and installation instructions, please visit the [PlatformIO Registry](https://registry.platformio.org).

**Example:**

Depend on the [platformio/espressif32](https://registry.platformio.org/platforms/platformio/espressif32) development platform with the next requirements:

- version is `>=3.5.0`
- version is `<4.0.0`
- version is not `3.2.0`

```bash
platformio/espressif32@>=3.5.0,<4,!=3.2.0

# or short form
platformio/espressif32@^3.5.0,!=3.2.0
```

## See also {#see-also}

- [pio pkg uninstall](./uninstall.md)
- [pio pkg outdated](./outdated.md)
- [library.json](../../library-json/index.md)
