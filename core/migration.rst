..  Copyright (c) 2014-present PlatformIO <contact@platformio.org>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _core_migration:

Migrating from 3.x to 4.0
=========================

Guidance on how to upgrade from :ref:`piocore` v3.x to v4.x with emphasis on
major changes, what is new, and what has been removed.

Please read :ref:`PlatformIO 4.0 Release Notes <release_notes_4>` before.

.. contents:: Contents
  :local:

Compatibility
-------------

**PlatformIO Core 4.0 is fully backward compatible with v3.x**. The only major
change is a new location for project build artifacts and library dependencies.
The previous ``.pioenvs`` (:ref:`projectconf_pio_build_dir`) and
``.piolibdeps`` (:ref:`projectconf_pio_libdeps_dir`) folders were moved to a
new :ref:`projectconf_pio_workspace_dir`.

.. note::
  If you manually added library dependencies to old ``.piolibdeps`` folder,
  please declare them in :ref:`projectconf_lib_deps`. **We do not recommend**
  modifying any files or folders in :ref:`projectconf_pio_workspace_dir`.
  This is an internal location for PlatformIO Core artifacts and temporary files.
  PlatformIO Core 4.0 may delete/cleanup this folder in a service purpose any time.

Infrastructure
--------------

Finally, Python 3 interpreter is officially supported! The minimum requirements
are Python 2.7 or Python 3.5+.

We also added full support for operating system locales other than UTF-8.
So, your project path can contain non-ASCII/non-Latin chars now.

If you are :ref:`platforms` maintainer or you need to show a progress bar
(upload progress, connecting status...), PlatformIO Core 4.0 has re-factored
target runner where line-buffering was totally removed. Just print any progress
information in real time and PlatformIO Core will display it instantly on user
the side. For example, a writing progress from :ref:`platform_atmelavr`
"avrdude" programmer:

.. code-block:: shell

    ...
    Looking for upload port...
    Auto-detected: /dev/cu.usbmodemFA141
    Uploading build/uno/firmware.hex

    avrdude: AVR device initialized and ready to accept instructions

    Reading | ################################################## | 100% 0.00s

    avrdude: Device signature = 0x1e950f (probably m328p)
    avrdude: reading input file "build/uno/firmware.hex"
    avrdude: writing flash (930 bytes):

    Writing | ##########################

What is new
-----------

In this section, we are going to highlight the most important changes and
features introduced in :ref:`piocore` 4.0. Please visit
:ref:`PlatformIO 4.0 Release Notes <release_notes_4>` for more detailed information.

:ref:`projectconf`
~~~~~~~~~~~~~~~~~~

A project configuration parser was rewritten from scratch. It has strict
options typing (`API <https://github.com/platformio/platformio-core/blob/develop/platformio/project/options.py>`__)
and helps to avoid issues when option values are invalid (for example,
invalid :ref:`ldf_mode` or non-existing :ref:`projectconf_debug_svd_path`).

Global scope ``[env]``
^^^^^^^^^^^^^^^^^^^^^^

One of the most requested features was a "global" or "common" project
environment (:ref:`projectconf_section_env`) where developers can share common configuration between all declared build environments ``[env:NAME]``.

The previous solution in PlatformIO Core 3.0 was using :ref:`projectconf_dynamic_vars`.
As practice has shown, this approach was not good and more advanced :ref:`projectconf`
looked so complicated and hard for managing (for example, open source
projects `MarlinFirmware <https://github.com/MarlinFirmware/Marlin/blob/3bf43b6c1e5051ee279a07babffdfb73e3aa812d/platformio.ini>`__,
`Espurna <https://github.com/xoseperez/espurna/blob/2cd7a8717aff1d277b4777d7f90a3e086ed9e619/code/platformio.ini>`__).

PlatformIO Core 4.0 introduces a new global scope named ``[env]`` which allows
declaring global options that will be shared between all ``[env:NAME]``
sections in :ref:`projectconf`. For example,

.. code-block:: ini

    [env]
    platform = ststm32
    framework = stm32cube
    board = nucleo_l152re
    lib_deps = Dep1, Dep2

    [env:release]
    build_flags = -D RELEASE
    lib_deps =
        ${env.lib_deps}
        Dep3

    [env:debug]
    build_type = debug
    build_flags = -D DEBUG
    lib_deps = DepCustom

In this example we have 2 build environments ``release`` and ``debug``. This
is the same if you duplicate all options (PlatformIO Core 3.0 compatible):

.. code-block:: ini

    [env:release]
    platform = ststm32
    framework = stm32cube
    board = nucleo_l152re
    build_flags = -D RELEASE
    lib_deps = Dep1, Dep2, Dep3

    [env:debug]
    platform = ststm32
    framework = stm32cube
    board = nucleo_l152re
    build_type = debug
    build_flags = -D DEBUG
    lib_deps = DepCustom

External Configuration Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To simplify the project configuration process, PlatformIO Core 4.0 adds support
for external :ref:`projectconf`. Yes! You can finally extend one configuration
file with another or with a list of them. The cool feature is a support for
Unix shell-style wildcards. So, you can dynamically generate :ref:`projectconf`
files or load bunch of them from a folder.
See :ref:`projectconf_pio_extra_configs` option for details and a simple example
below:

*Base "platformio.ini"*

.. code-block:: ini

    [platformio]
    extra_configs =
      extra_envs.ini
      extra_debug.ini

    [common]
    debug_flags = -D RELEASE
    lib_flags = -lc -lm

    [env:esp-wrover-kit]
    platform = espressif32
    framework = espidf
    board = esp-wrover-kit
    build_flags = ${common.debug_flags}


*"extra_envs.ini"*

.. code-block:: ini

    [env:esp32dev]
    platform = espressif32
    framework = espidf
    board = esp32dev
    build_flags = ${common.lib_flags} ${common.debug_flags}

    [env:lolin32]
    platform = espressif32
    framework = espidf
    board = lolin32
    build_flags = ${common.debug_flags}


*"extra_debug.ini"*

.. code-block:: ini

    # Override base "common.debug_flags"
    [common]
    debug_flags = -D DEBUG=1

    [env:lolin32]
    build_flags = -Og

After a parsing process, configuration state will be the next:

.. code-block:: ini

    [common]
    debug_flags = -D DEBUG=1
    lib_flags = -lc -lm

    [env:esp-wrover-kit]
    platform = espressif32
    framework = espidf
    board = esp-wrover-kit
    build_flags = ${common.debug_flags}

    [env:esp32dev]
    platform = espressif32
    framework = espidf
    board = esp32dev
    build_flags = ${common.lib_flags} ${common.debug_flags}

    [env:lolin32]
    platform = espressif32
    framework = espidf
    board = lolin32
    build_flags = -Og

New Options
^^^^^^^^^^^

We have added new options and changed some existing ones. Here are the new or
updated options.

.. list-table::
    :header-rows:  1

    * - Section
      - Option
      - Description
    * - platformio
      - :ref:`projectconf_pio_extra_configs`
      - Extend base configuration with external :ref:`projectconf`
    * - platformio
      - :ref:`projectconf_pio_core_dir`
      - Directory where PlatformIO stores development platform packages
        (toolchains, frameworks, SDKs, upload and debug tools), global
        libraries for :ref:`ldf`, and other PlatformIO Core service data
    * - platformio
      - :ref:`projectconf_pio_globallib_dir`
      - Global library storage for PlatfrmIO projects and
        :ref:`librarymanager` where :ref:`ldf` looks for dependencies
    * - platformio
      - :ref:`projectconf_pio_platforms_dir`
      - Global storage where **PlatformIO Package Manager**
        installs :ref:`platforms`
    * - platformio
      - :ref:`projectconf_pio_packages_dir`
      - Global storage where **PlatformIO Package Manager** installs
        :ref:`platforms` dependencies (toolchains, :ref:`frameworks`, SDKs,
        upload and debug tools)
    * - platformio
      - :ref:`projectconf_pio_cache_dir`
      - :ref:`piocore` uses this folder to store caching information (requests
        to PlatformIO Registry, downloaded packages and other service information)
    * - platformio
      - :ref:`projectconf_pio_workspace_dir`
      - A path to a project workspace directory where PlatformIO keeps by
        default compiled objects, static libraries, firmwares, and external
        library dependencies
    * - platformio
      - :ref:`projectconf_pio_shared_dir`
      - :ref:`pioremote` uses this folder to synchronize extra files between
        remote machine
    * - env
      - :ref:`projectconf_build_type`
      - See extended documentation for :ref:`build_configurations`
    * - env
      - :ref:`projectconf_monitor_flags`
      - Pass extra flags and options to :ref:`cmd_device_monitor` command
    * - env
      - :ref:`projectconf_upload_command`
      - Override default :ref:`platforms` upload command with a custom one.

Library Management
~~~~~~~~~~~~~~~~~~

Library management brings a few new changes which resolve historical issues
presented in PlatformIO 3.0:

1. ``.piolibdeps`` folder was moved to :ref:`projectconf_pio_libdeps_dir`
   of :ref:`project workspace <projectconf_pio_workspace_dir>`.

   If you manually added library dependencies to old ``.piolibdeps`` folder,
   please declare them in :ref:`projectconf_lib_deps`. **We do not recommend**
   modifying any files or folders in :ref:`projectconf_pio_workspace_dir`.
   This is an internal location for PlatformIO Core artifacts and temporary files.
   PlatformIO Core 4.0 may delete/cleanup this folder in a service purpose any time.

2. :ref:`ldf` now uses isolated library dependency storage per project build
   environment. It resolves conflicts when the libraries from different
   build environments declared via :ref:`projectconf_lib_deps` option
   were installed into the same ``.piolibdeps`` folder.

See **Library Management** section in :ref:`release_notes_4` release notes
for more details.

Build System
~~~~~~~~~~~~

PlatformIO Core 4.0 uses a new :ref:`projectconf_pio_build_dir` instead of
``.pioenvs`` for compiled objects, archived libraries, firmware binaries
and, other artifacts. A new :ref:`projectconf_build_type` option allows you
to control a build process between "Release" and "Debug" modes
(see :ref:`build_configurations`).

See **Build System** section in :ref:`release_notes_4` release notes
for more details.

Package Dependencies
^^^^^^^^^^^^^^^^^^^^^

PlatformIO has decentralized architecture and allows platform maintainers
to create :ref:`platform_creating` for PlatformIO ecosystem. Each development
platform depends on a list of packages (toolchains, SDKs, debugging servers,
etc). PlatformIO Package Manager installs these packages automatically and
PlatformIO Build System uses them later.

Starting from PlatformIO Core 4.0, developers can see which versions of
a development platform or its dependent packages will be used. This is a great addition
to track changes (:ref:`frameworks`, SDKs) between :ref:`platforms` updates.
See an example with "staging" (Git) version of :ref:`platform_espressif8266`
development platform:

.. code-block:: shell

  Processing nodemcuv2 (platform: https://github.com/platformio/platform-espressif8266.git#feature/stage; board: nodemcuv2; framework: arduino)
  -------------------------------------------------------------------------------
  Verbose mode can be enabled via `-v, --verbose` option
  CONFIGURATION: https://docs.platformio.org/page/boards/espressif8266/nodemcuv2.html
  PLATFORM: Espressif 8266 (Stage) 2.3.0-alpha.1 #990141d > NodeMCU 1.0 (ESP-12E Module)
  HARDWARE: ESP8266 80MHz, 80KB RAM, 4MB Flash
  PACKAGES: toolchain-xtensa 2.40802.190218 (4.8.2), tool-esptool 1.413.0 (4.13), tool-esptoolpy 1.20600.0 (2.6.0), framework-arduinoespressif8266 78a1a66
  LDF: Library Dependency Finder -> http://bit.ly/configure-pio-ldf
  LDF Modes: Finder ~ chain+, Compatibility ~ soft
  Found 35 compatible libraries
  Scanning dependencies...

Custom Platform Packages
^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes you need to override default :ref:`platforms` packages or add an
extra. PlatformIO Core 4.0 introduces a new configuration option
:ref:`projectconf_env_platform_packages` per a build environment.
Also, using this option you can install external packages and use them later
as programmers or upload tools. See a few examples:

.. code-block:: ini

    [env:override_default_toolchain]
    platform = atmelavr
    platform_packages =
      ; use GCC AVR 5.0+
      toolchain-gccarmnoneeabi@>1.50000.0

    [env:override_framework]
    platform = espressif8266
    platform_packages =
      ; use upstream Git version
      framework-arduinoespressif8266 @ https://github.com/esp8266/Arduino.git

    [env:external_package]
    platform = ststm32
    platform_packages =
      ; latest openOCD from PlatformIO Package Registry
      tool-openocd

      ; source code of ST-Link
      tool-stlink-source @ https://github.com/texane/stlink.git

Custom Upload Command
^^^^^^^^^^^^^^^^^^^^^

PlatformIO's :ref:`platforms` have pre-configured settings to program boards
or devices. They depend on a type of bootloader or programming interface.
PlatformIO Core 4.0 allows you to override default upload command using
:ref:`projectconf_upload_command` option in :ref:`projectconf`:

.. code-block:: ini

    [env:custom_upload_cmd]
    platform = ...
    framework = ...
    board = ...
    upload_command = /my/flasher arg1 arg2 --flag1 $SOURCE

See real examples for :ref:`projectconf_upload_command`.

Shared Cache Directory
^^^^^^^^^^^^^^^^^^^^^^

PlatformIO Core 4.0 allows you to configure a shared folder for the derived
files (objects, firmwares, ELFs) from a build system using
:ref:`projectconf_pio_build_cache_dir`. You can use it in multi-environments
project configuration to avoid multiple compilations of the same source code
files.

The example of :ref:`projectconf` below instructs PlatformIO Build System to
check :ref:`projectconf_pio_build_cache_dir` for already compiled objects for
:ref:`framework_stm32cube` and project source files. The cached object will
not be used if the original source file was modified or build environment has
a different configuration (new build flags, etc):

.. code-block:: ini

    [platformio]
    ; set a path to a cache folder
    build_cache_dir = /tmp/platformio-shared-cache

    [env:bluepill_f103c6]
    platform = ststm32
    framework = stm32cube
    board = bluepill_f103c6

    [env:nucleo_f411re]
    platform = ststm32
    framework = stm32cube
    board = nucleo_f411re

You can also use the same :ref:`projectconf_pio_build_cache_dir` between
different projects if they use the same :ref:`platforms` and :ref:`frameworks`.

What is changed or removed
--------------------------

Command Line Interface
~~~~~~~~~~~~~~~~~~~~~~

The following commands have been changed in v4.0.

.. list-table::
    :header-rows:  1

    * - Command
      - Description
    * - :ref:`cmd_run`
      - Added :option:`platformio run --jobs` option
    * - :ref:`cmd_update`
      - Replaced ``-c, --only-check`` with :option:`platformio update --dry-run`
    * - :ref:`cmd_lib_update`
      - Replaced ``-c, --only-check`` with :option:`platformio lib update --dry-run`
    * - :ref:`cmd_platform_update`
      - Replaced ``-c, --only-check`` with :option:`platformio platform update --dry-run`
    * - :ref:`cmd_remote_update`
      - Replaced ``-c, --only-check`` with :option:`platformio remote update --dry-run`

:ref:`projectconf`
~~~~~~~~~~~~~~~~~~

The following options have been changed in v4.0.

.. list-table::
    :header-rows:  1

    * - Section
      - Option
      - Description
    * - platformio
      - ``env_default``
      - Renamed to :ref:`projectconf_pio_default_envs`
    * - platformio
      - ``home_dir``
      - Renamed to :ref:`projectconf_pio_core_dir`
    * - env
      - ``debug_load_cmd``
      - Renamed to :ref:`projectconf_debug_load_cmds` and allowed to pass more
        than one load command
