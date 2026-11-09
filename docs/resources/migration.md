---
description: Upgrade projects from PlatformIO Core 5.x to 6.0 - required changes, new features and removed commands.
---

# Migrating from 5.x to 6.0

Guidance on how to upgrade from [PlatformIO Core (CLI)](../get-started/platformio-core.md) v5.x to v6.x with emphasis on major changes, what is new, and what has been removed.

:::note

PlatformIO Core 6.0 is **FULLY BACKWARD COMPATIBLE\*** with PlatformIO 5.0 projects. It means, there are no breaking changes or required migration steps. Project compatibility between major PlatformIO Core releases is our main task and part of PlatformIO's decentralized architecture.

We highly recommend using the latest PlatformIO Core. See [pio upgrade](../reference/cli/pio-upgrade.md) command.

`*` see a note regarding [Unit Testing](../guides/unit-testing/index.md) and the grouped test suites in the migration steps below.

:::

Please read [PlatformIO 6.0 Release Notes](./changelog.mdx#release-notes-6) before.

## Migration Steps {#migration-steps}

**PlatformIO Core 6.0** received a lot of new features and updates to improve the lives of everyday engineers. To benefit from its improvements, we recommend taking into account the following steps:

1. Replace deprecated `$ pio lib`, `$ pio platform`, and `$ pio update` commands with the unified [Package Management CLI](../reference/cli/pio-pkg/index.md)

2. Avoid using global libraries previously installed using the `$ pio lib --global` command. Ensure that the [globallib_dir](../reference/platformio-ini/platformio/globallib-dir.md) folder is empty. Please use a declarative approach for the safety-critical embedded development and declare project dependencies using the [lib_deps](../reference/platformio-ini/env/lib-deps.md) option

3. Ensure that project dependencies are declared using the [platform](../reference/platformio-ini/env/platform.md), [platform_packages](../reference/platformio-ini/env/platform-packages.md), and [lib_deps](../reference/platformio-ini/env/lib-deps.md) options in ["platformio.ini" (Project Configuration File)](../reference/platformio-ini/index.md):

   1. meet the updated [Package Specifications](../reference/cli/pio-pkg/install.md#cmd-pkg-install-specifications)
   2. use recommended Semantic [Version Requirements](../reference/cli/pio-pkg/install.md#cmd-pkg-install-requirements) (check [PlatformIO Registry](https://registry.platformio.org) for the available package versions)

   **Bad practice** (not recommended)

   ```ini
   [env:myenv]
   ; Depend on ANY/Latest version of the development platform
   ; allowing breaking changes
   platform = platformio/espressif32

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

   **Good practice** (highly recommended)

   ```ini
   [env:myenv]
   ; Depend on the latest compatible version of development platform
   ; allowing new functionality (backward-compatible), and bug fixes.
   ; No breaking changes
   ; FYI: ^4 == ^4.0.0 == (>=4.0.0, <5.0.0)
   platform = platformio/espressif32 @ ^4

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

4. If you use a custom testing transport via the "test_transport" option in ["platformio.ini" (Project Configuration File)](../reference/platformio-ini/index.md), please align your codebase with [Custom unity_config.h](../guides/unit-testing/frameworks/unity.md#unit-testing-frameworks-unity-custom-config). The "test_transport" option has been removed.

5. There is a known bug in PlatformIO Core 5.0 when Unit Testing didn't handle correctly grouped test suites. Please ensure that a test suite folder that contains test source files is prefixed with `test_`. See [Test Hierarchy](../guides/unit-testing/structure/hierarchy.md) for details.

## What is new {#what-is-new}

In this section, we are going to highlight the most important changes and features introduced in **PlatformIO Core 6.0**. Please visit [PlatformIO 6.0 Release Notes](./changelog.mdx#release-notes-6) for more detailed information.

### Package Management {#package-management}

**PlatformIO Core 6.0** brings a powerful solution to manage different [Package Types](../reference/cli/pio-pkg/install.md#cmd-pkg-install-types) using the unified [Package Management CLI](../reference/cli/pio-pkg/index.md):

- [pio pkg install](../reference/cli/pio-pkg/install.md) - install the project dependencies or custom packages
- [pio pkg list](../reference/cli/pio-pkg/list.md) - list installed packages
- [pio pkg outdated](../reference/cli/pio-pkg/outdated.md) - check for project outdated packages
- [pio pkg search](../reference/cli/pio-pkg/search.md) - search for packages
- [pio pkg show](../reference/cli/pio-pkg/show.md) - show package information
- [pio pkg uninstall](../reference/cli/pio-pkg/uninstall.md) uninstall the project dependencies or custom packages
- [pio pkg update](../reference/cli/pio-pkg/update.md) - update the project dependencies or custom packages.

There are no more global packages that could lead to potential issues. The new package management solution allows you to use a modern declarative approach for safety-critical embedded development. Using the Semantic [Version Requirements](../reference/cli/pio-pkg/install.md#cmd-pkg-install-requirements) guarantees the full project reproducibility on any supported host machine for decades.

The new [Package Management CLI](../reference/cli/pio-pkg/index.md) operates in accordance with the active (working) project. The [pio pkg install](../reference/cli/pio-pkg/install.md) command will install all required project dependencies. The [pio pkg list](../reference/cli/pio-pkg/list.md) command allows listing not only dependent libraries but also development platforms and their packages.

The notable addition is the [pio pkg outdated](../reference/cli/pio-pkg/outdated.md) command. It allows you to check for outdated project packages and list version information for all dependencies. There are three color legends to help you easily identify which updates are backward-incompatible.

#### Run package command {#run-package-command}

[PlatformIO Registry](https://registry.platformio.org) contains a rich set of popular toolchains and other useful tools. The [pio pkg exec](../reference/cli/pio-pkg/exec.md) command allows you to run an arbitrary command from the specified package. If you specify package requirements using the [`pio pkg exec --package`](../reference/cli/pio-pkg/exec.md#cmdoption-pio-pkg-exec-p) option, PlatformIO will ensure that the package is installed before running any command.

Practical use cases include running debugging servers, uploaders or special tools from a toolchain. A few examples of how to leverage the new [pio pkg exec](../reference/cli/pio-pkg/exec.md) command:

```bash
# Ensure JLink tool is installed and start GDB server
> pio pkg exec --package=tool-jlink -- JLinkGDBServer -singlerun -if JTAG -select USB -jtagconf -1,-1 -device EFR32BG22CxxxF512 -port 2331

# Run Espressif SoC serial bootloader utility and erase a flash from the target device
> pio pkg exec -- esptool.py erase_flash

# Disassembly AVR ELF file
> pio pkg exec -- avr-objdump -d -m avr2 .pio/build/uno/firmware.elf
```

#### Virtual symbolic links {#virtual-symbolic-links}

The most requested feature from the library maintainers was the ability to link the existing package with the project without hard copying (duplicating). As a workaround, developers used a Unix-native symlink solution and hence it was not possible to declare a symlinked dependency in the ["platformio.ini" (Project Configuration File)](../reference/platformio-ini/index.md).

The [PlatformIO Core (CLI)](../get-started/platformio-core.md) 6.0 introduces cross-platform virtual symbolic links without any dependencies on the host OS. PlatformIO `symlink://` resources do not require any specific OS permissions. They are portable between different host machines.

See [Package Specifications](../reference/cli/pio-pkg/install.md#cmd-pkg-install-specifications) for "Local Folder".

### Unit Testing {#unit-testing}

It's been [six years](https://github.com/platformio/platformio-core/commit/bb22a1297bc2e4c3131530f15a2b4b3914836560) since we added support for unit testing, and Unity was the only available testing framework. We didn't expect that the PlatformIO [Unit Testing](../guides/unit-testing/index.md) solution will gain broad popularity, especially when it comes to using it on native (host) machines.

So, the time has come to refresh our view on PlatformIO Unit Testing with taking into account [your feedback and feature requests](https://github.com/platformio/platformio-core/issues?q=is%3Aissue+label%3A%22unit+testing%22+is%3Aclosed+milestone%3A6.0).

#### Test-driven development {#test-driven-development}

The PlatformIO Core 6.0 introduces an absolutely a new workflow for [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development) in the embedded systems industry. Thanks to the rich set of supported [Testing Frameworks](../guides/unit-testing/frameworks/index.md) and the ability to organize tests in groups using the [Test Hierarchy](../guides/unit-testing/structure/hierarchy.md), you can create hybrid projects and benefit from multiple testing frameworks depending on the project requirements simultaneously. See a simple example of the hybrid configuration:

```ini
[env:native]
platform = native
test_framework = googletest
test_filter =
  common/*
  native/*

[env:embedded]
platform = ...
framework = ...
test_framework = unity
test_filter =
  common/*
  embedded/*
```

Use more advanced C++ testing frameworks with Mocking support such as [GoogleTest](../guides/unit-testing/frameworks/googletest.md) in pair with the [Native](/hardware/platforms/native) development platform to run desktop tests on the host machine and a lightweight framework, such as [Unity](../guides/unit-testing/frameworks/unity.md), for running tests on the target embedded device with constrained resources.

#### Hardware-less development {#hardware-less-development}

It's hard to imagine today a next-gen project development workflow that does not benefit from [Continuous Integration](../guides/ci/index.md) systems. PlatformIO already provides multiple solutions to improve code quality including [Static Code Analysis](../guides/static-code-analysis/index.md). In addition to the testing frameworks that allow you to mock objects and simulate the behavior of real objects, the PlatformIO Core 6.0 adds support for the [Simulators](../guides/unit-testing/simulators/index.md).

The combination of simulation tools and testing frameworks allow you to simulate hardware systems and run unit tests in virtual environments. Simulators can significantly accelerate project development, especially when used in pair with [Continuous Integration](../guides/ci/index.md).

Integration of any simulator tool to the PlatformIO [Unit Testing](../guides/unit-testing/index.md) is very simple and does not require any extra software or code writing. Please take a look at the example below how easy it is to integrate the [Renode](../guides/unit-testing/simulators/renode.md) simulation framework:

```ini
[env:hifive1-revb]
platform = sifive
framework = zephyr
board = hifive1-revb

platform_packages =
    platformio/tool-renode
test_testing_command =
    ${platformio.packages_dir}/tool-renode/renode
    --disable-xwt
    -e include @scripts/single-node/sifive_fe310.resc
    -e showAnalyzer uart1
    -e sysbus LoadELF @${platformio.build_dir}/${this.__env__}/firmware.elf
    -e start
```

## What is changed or removed {#what-is-changed-or-removed}

### Dropped automatic updates {#dropped-automatic-updates}

Thanks to your feedback, we finally removed automatic updates of global libraries and development platforms. Please use [pio pkg outdated](../reference/cli/pio-pkg/outdated.md) to check for outdated project packages and list version information for all dependencies.

The [pio pkg update](../reference/cli/pio-pkg/update.md) is intended to update the project dependencies, custom packages from the [PlatformIO Registry](https://registry.platformio.org), or external sources.

### Command Line Interface {#command-line-interface}

The following commands have been changed in v6.0.

| Command | Description |
|---|---|
| [pio pkg](../reference/cli/pio-pkg/index.md) | **NEW** Unified package management solution |
| [pio project init](../reference/cli/pio-project/init.md) | **NEW** [`pio project init --no-install-dependencies`](../reference/cli/pio-project/init.md#cmdoption-pio-project-init-no-install-dependencies) option |
| [pio project metadata](../reference/cli/pio-project/metadata.md) | **NEW** [`pio project metadata --json-output-path`](../reference/cli/pio-project/metadata.md#cmdoption-pio-project-metadata-json-output-path) option |
| [pio run](../reference/cli/pio-run.md) | **NEW** [`pio run --program-arg`](../reference/cli/pio-run.md#cmdoption-pio-run-a) option |
| [pio test](../reference/cli/pio-test.md) | **NEW** [`pio test --program-arg`](../reference/cli/pio-test.md#cmdoption-pio-test-a), [`pio test --json-output-path`](../reference/cli/pio-test.md#cmdoption-pio-test-json-output-path), [`pio test --junit-output-path`](../reference/cli/pio-test.md#cmdoption-pio-test-junit-output-path), and [`pio test --list-tests`](../reference/cli/pio-test.md#cmdoption-pio-test-list-tests) options |
| `pio project data` | **RENAMED** to the [pio project metadata](../reference/cli/pio-project/metadata.md) |
| `pio lib` | **DEPRECATED** in favor of [Package Management CLI](../reference/cli/pio-pkg/index.md) |
| `pio platform` | **DEPRECATED** in favor of [Package Management CLI](../reference/cli/pio-pkg/index.md) |
| `pio update` | **DEPRECATED** in favor of [Package Management CLI](../reference/cli/pio-pkg/index.md) |
