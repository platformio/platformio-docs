<a id="librarymanager-dependencies"></a>

# Dependency Management {#dependency-management}

Modern software projects rarely work in isolation. In most cases, a project relies on reusable functionality in the form of libraries or is broken up into individual components to compose a modularized system. Dependency management is a technique for declaring, resolving, and using dependencies required by the project in an automated fashion.

PlatformIO is the missing solution in the embedded system industry which has built-in support for dependency management and lives up to the task of fulfilling typical scenarios encountered in modern software projects.

## Library Registry {#library-registry}

[PlatformIO Registry](https://registry.platformio.org) contains a rich set of popular libraries with examples and instructions on how to add them to your project. Libraries in PlatformIO are isolated between projects and project environments. This helps you to avoid conflicts or break existing projects when you update libraries to the newest versions.

If you prefer using [PlatformIO Core (CLI)](../../get-started/platformio-core.md) instead of web browsing, the [pio pkg search](../../reference/cli/pio-pkg/search.md) command allows you to search for libraries matching the search query.

## Library sources {#library-sources}

PlatformIO supports different library sources which you can use for declaring dependencies. The most popular are:

- Versioned libraries from [PlatformIO Registry](https://registry.platformio.org)
- VCS repositories (Git, Hg, SVN)
- Remote or local library as a TAR or ZIP archive
- Local library as a source folder.

## Dependency specifications {#dependency-specifications}

Please check [Package Specifications](../../reference/cli/pio-pkg/install.md#cmd-pkg-install-specifications) for the available options.

## Declaring dependencies {#declaring-dependencies}

["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) and the [lib_deps](../../reference/platformio-ini/env/lib-deps.md) is the only place for declaring project dependencies. There are 2 sections where dependencies can be declared:

1. [Section \[env\]](../../reference/platformio-ini/env/index.md) - declare common dependencies for all environments
2. [Working \[env:NAME\]](../../reference/platformio-ini/env/index.md#projectconf-section-env-named) - declare specific dependencies for the working environment.

Please take a look at the example below. The `dep_1` and `dep_2` dependencies are common to the `release` and `debug` working environments, whereas the `dep_3` is a specific only for the `debug` working environment. The `[env:debug]` section overrides common `lib_deps` option, and the `${env.lib_deps}` ([Interpolation of Values](../projects/interpolation.md) technique) is used to merge the common and custom dependencies.

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

:::note

If some libraries are not visible in [PlatformIO IDE](../../get-started/platformio-ide.md) and Code Completion or Code Linting does not work properly, please perform

- **VSCode**: "Menu: View > Command Palette... > PlatformIO: Rebuild C/C++ Project Index"

:::

## Declaring practices {#declaring-practices}

### Good practice {#good-practice}

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

### Bad practice {#bad-practice}

:::warning

**NOT RECOMMENDED**

:::

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

## Installing dependencies {#installing-dependencies}

PlatformIO automatically resolves and installs project dependencies when you build, debug, or test a project. If you want to install project dependencies manually, please use [PlatformIO Core (CLI)](../../get-started/platformio-core.md) and the [pio pkg install](../../reference/cli/pio-pkg/install.md) command.

## Updating dependencies {#updating-dependencies}

PlatformIO does not update project dependencies automatically. You need to use [PlatformIO Core (CLI)](../../get-started/platformio-core.md) and the [pio pkg update](../../reference/cli/pio-pkg/update.md) command to update all project dependencies or for the specified environment. It is also possible to update the specified dependency.

We recommend using the [pio pkg outdated](../../reference/cli/pio-pkg/outdated.md) command, checking available updates, and avoiding versions that introduce breaking changes.
