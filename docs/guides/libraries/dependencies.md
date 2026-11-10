---
description: Declare library dependencies in platformio.ini, pin versions, and install and update them.
---

# Dependency management

Declare the libraries your project uses in `platformio.ini`. PlatformIO
installs them automatically when you build, test or debug, separately for each
[project environment](../../reference/platformio-ini/env/index.md), so updating
a library in one project cannot break another.

## Find libraries {#library-registry}

Search the [PlatformIO Registry](https://registry.platformio.org), the library
manager in [PlatformIO Home](../../get-started/platformio-home.md), or use
[`pio pkg search`](../../reference/cli/pio-pkg/search.md):

```bash
pio pkg search "type:library json"
```

## Library sources {#library-sources}

A dependency can be:

- a library from the PlatformIO Registry, with a version requirement;
- a Git, Mercurial or Subversion repository;
- a local or remote `.tar.gz` or `.zip` archive;
- a local folder.

For the exact syntax of each, see
[package specifications](../../reference/cli/pio-pkg/install.md#cmd-pkg-install-specifications).

<a id="dependency-specifications"></a>

## Declare dependencies {#declaring-dependencies}

List dependencies in the [`lib_deps`](../../reference/platformio-ini/env/lib-deps.md)
option, either in the shared [`[env]`](../../reference/platformio-ini/env/index.md#common-env)
section, for all environments, or in an
[`[env:NAME]`](../../reference/platformio-ini/env/index.md#working-env-name)
section, for one environment.

In the example below, `dep_1` and `dep_2` are used by both environments, and
`dep_3` only by `debug`. Because `[env:debug]` sets its own `lib_deps`, it
includes the shared list with `${env.lib_deps}`
([interpolation](../../reference/platformio-ini/interpolation.md)):

```ini
; Common dependencies declared in the common "[env]" section
[env]
platform = ...
board = ...
framework = ...
lib_deps =
  dep_1
  dep_2

[env:release]
build_flags = -D RELEASE=1

; Specific dependencies that extend the common dependencies
[env:debug]
lib_deps =
  ${env.lib_deps}
  dep_3
```

:::tip

If code completion in PlatformIO IDE for VS Code does not see a new library,
run **Command Palette** > **PlatformIO: Rebuild C/C++ Project Index**.

:::

## Pin versions {#declaring-practices}

Always give the owner and a version requirement, so that builds are
reproducible and a library update cannot break your project unexpectedly.

### Recommended {#good-practice}

```ini
[env:myenv]
lib_deps =
  ; Depend on the latest 6.x stable version of ArduinoJson.
  ; The minimum required version is 6.19.4.
  ; New functionality (backward-compatible) and bug-fixed are allowed
  bblanchon/ArduinoJson @ ^6.19.4

  ; Depend on the exact 1.1.1 version
  ; No new functionality (backward-compatible) or bug fixes.
  ; Recommended for safety-critical projects
  me-no-dev/AsyncTCP @ 1.1.1

  ; Depend on the particular tag (v2.13) of a Git repository
  https://github.com/username/HelloWorld.git#v2.13
```

### Avoid {#bad-practice}

```ini
[env:myenv]
lib_deps =
  ; Omit library package owner (<owner>/<name>) and depend on the library by name.
  ; Lead to the conflicts when there are multiple libraries with the same name
  OneWire

  ; Depend on ANY/Latest version of the development platform
  ; allowing breaking changes
  me-no-dev/AsyncTCP

  ; Depend on the development branch of the Git repository,
  ; allow breaking changes, and untested commits
  https://github.com/username/HelloWorld.git
```

## Install dependencies {#installing-dependencies}

PlatformIO installs missing dependencies automatically when you build, test or
debug. To install them without building, run
[`pio pkg install`](../../reference/cli/pio-pkg/install.md) in the project
directory.

## Update dependencies {#updating-dependencies}

PlatformIO never updates dependencies on its own. To see which ones have newer
versions, run [`pio pkg outdated`](../../reference/cli/pio-pkg/outdated.md);
to update them within your version requirements, run
[`pio pkg update`](../../reference/cli/pio-pkg/update.md), for the whole
project or a single environment or library.

Review the changes of a new major version before you allow it: it may break
compatibility.
