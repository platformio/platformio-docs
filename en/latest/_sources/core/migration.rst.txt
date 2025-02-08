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

.. |PIOREGISTRY| replace:: `PlatformIO Registry <https://registry.platformio.org>`__
.. |CORE_6_0|    replace:: **PlatformIO Core 6.0**

.. _core_migration:

Migrating from 5.x to 6.0
=========================

Guidance on how to upgrade from :ref:`piocore` v5.x to v6.x with emphasis on
major changes, what is new, and what has been removed.

.. note::
  PlatformIO Core 6.0 is **FULLY BACKWARD COMPATIBLE*** with PlatformIO 5.0 projects.
  It means, there are no breaking changes or required migration steps.
  Project compatibility between major PlatformIO Core releases is our main task
  and part of PlatformIO's decentralized architecture.

  We highly recommend using the latest PlatformIO Core.
  See :ref:`cmd_upgrade` command.

  ``*`` see a note regarding :ref:`unit_testing` and the grouped test suites
  in the migration steps below.

Please read :ref:`PlatformIO 6.0 Release Notes <release_notes_6>` before.

.. contents:: Contents
  :local:

Migration Steps
---------------

|CORE_6_0| received a lot of new features and updates to improve the
lives of everyday engineers. To benefit from its improvements, we recommend
taking into account the following steps:

#.  Replace deprecated :ref:`cmd_lib`, :ref:`cmd_platform`,
    and :ref:`cmd_update` commands with the unified :ref:`cmd_pkg`
#.  Avoid using global libraries previously installed using the :option:`pio lib --global`
    command. Ensure that the :ref:`projectconf_pio_globallib_dir` folder is empty.
    Please use a declarative approach for the safety-critical embedded development
    and declare project dependencies using the :ref:`projectconf_lib_deps` option
#.  Ensure that project dependencies are declared using the :ref:`projectconf_env_platform`,
    :ref:`projectconf_env_platform_packages`, and :ref:`projectconf_lib_deps` options
    in :ref:`projectconf`:

    a) meet the updated :ref:`cmd_pkg_install_specifications`
    b) use recommended Semantic :ref:`cmd_pkg_install_requirements`
       (check |PIOREGISTRY| for the available package versions)

    **Bad practice** (not recommended)

    .. code:: ini

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

    **Good practice** (highly recommended)

    .. code:: ini

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

#.  If you use a custom testing transport via the "test_transport" option
    in :ref:`projectconf`, please align your codebase with
    :ref:`unit_testing_frameworks_unity_custom_config`. The
    "test_transport" option has been removed.

#.  There is a known bug in PlatformIO Core 5.0 when Unit Testing didn't handle
    correctly grouped test suites. Please ensure that a test suite folder that
    contains test source files is prefixed with ``test_``.
    See :ref:`unit_testing_test_hierarchy` for details.

What is new
-----------

In this section, we are going to highlight the most important changes and
features introduced in |CORE_6_0|. Please visit
:ref:`PlatformIO 6.0 Release Notes <release_notes_6>` for more detailed information.

Package Management
~~~~~~~~~~~~~~~~~~

|CORE_6_0| brings a powerful solution to manage different
:ref:`cmd_pkg_install_types` using the unified :ref:`cmd_pkg`:

* :ref:`cmd_pkg_install` - install the project dependencies or custom packages
* :ref:`cmd_pkg_list` - list installed packages
* :ref:`cmd_pkg_outdated` - check for project outdated packages
* :ref:`cmd_pkg_search` - search for packages
* :ref:`cmd_pkg_show` - show package information
* :ref:`cmd_pkg_uninstall` uninstall the project dependencies or custom packages
* :ref:`cmd_pkg_update` - update the project dependencies or custom packages.

There are no more global packages that could lead to potential issues.
The new package management solution allows you to use a modern declarative approach
for safety-critical embedded development. Using the Semantic :ref:`cmd_pkg_install_requirements`
guarantees the full project reproducibility on any supported host machine for decades.

The new :ref:`cmd_pkg` operates in accordance with the active (working) project.
The :ref:`cmd_pkg_install` command will install all required project dependencies.
The :ref:`cmd_pkg_list` command allows listing not only dependent libraries
but also development platforms and their packages.

The notable addition is the :ref:`cmd_pkg_outdated` command. It allows you to
check for outdated project packages and list version information for all
dependencies. There are three color legends to help you easily identify
which updates are backward-incompatible.

Run package command
^^^^^^^^^^^^^^^^^^^

|PIOREGISTRY| contains a rich set of popular toolchains and other useful tools.
The :ref:`cmd_pkg_exec` command allows you to run an arbitrary command from the specified
package. If you specify package requirements using the :option:`pio pkg exec --package`
option, PlatformIO will ensure that the package is installed before running any command.

Practical use cases include running debugging servers, uploaders or
special tools from a toolchain. A few examples of how to leverage the
new :ref:`cmd_pkg_exec` command:

.. code:: bash

  # Ensure JLink tool is installed and start GDB server
  > pio pkg exec --package=tool-jlink -- JLinkGDBServer -singlerun -if JTAG -select USB -jtagconf -1,-1 -device EFR32BG22CxxxF512 -port 2331

  # Run Espressif SoC serial bootloader utility and erase a flash from the target device
  > pio pkg exec -- esptool.py erase_flash

  # Disassembly AVR ELF file
  > pio pkg exec -- avr-objdump -d -m avr2 .pio/build/uno/firmware.elf

Virtual symbolic links
^^^^^^^^^^^^^^^^^^^^^^

The most requested feature from the library maintainers was the ability to link
the existing package with the project without hard copying (duplicating). As a
workaround, developers used a Unix-native symlink solution and hence it was
not possible to declare a symlinked dependency in the :ref:`projectconf`.

The :ref:`piocore` 6.0 introduces cross-platform virtual symbolic links without
any dependencies on the host OS. PlatformIO ``symlink://`` resources do not
require any specific OS permissions. They are portable between different
host machines.

See :ref:`cmd_pkg_install_specifications` for "Local Folder".

Unit Testing
~~~~~~~~~~~~

It's been `six years <https://github.com/platformio/platformio-core/commit/bb22a1297bc2e4c3131530f15a2b4b3914836560>`_
since we added support for unit testing, and Unity was the only available testing framework.
We didn't expect that the PlatformIO :ref:`unit_testing` solution will gain broad
popularity, especially when it comes to using it on native (host) machines.

So, the time has come to refresh our view on PlatformIO Unit Testing with taking into account
`your feedback and feature requests <https://github.com/platformio/platformio-core/issues?q=is%3Aissue+label%3A%22unit+testing%22+is%3Aclosed+milestone%3A6.0>`_.

Test-driven development
^^^^^^^^^^^^^^^^^^^^^^^

The PlatformIO Core 6.0 introduces an absolutely a new workflow for
`test-driven development <https://en.wikipedia.org/wiki/Test-driven_development>`_
in the embedded systems industry.
Thanks to the rich set of supported :ref:`unit_testing_frameworks` and the ability
to organize tests in groups using the :ref:`unit_testing_test_hierarchy`, you can create
hybrid projects and benefit from multiple testing frameworks depending on the project
requirements simultaneously. See a simple example of the hybrid configuration:

.. code:: ini

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

Use more advanced C++ testing frameworks with Mocking support such as
:ref:`unit_testing_frameworks_googletest` in pair with the :ref:`platform_native`
development platform to run desktop tests on the host machine and a lightweight
framework, such as :ref:`unit_testing_frameworks_unity`, for running tests on
the target embedded device with constrained resources.

Hardware-less development
^^^^^^^^^^^^^^^^^^^^^^^^^

It's hard to imagine today a next-gen project development workflow that does
not benefit from :ref:`ci` systems. PlatformIO already provides multiple
solutions to improve code quality including :ref:`check`. In addition to
the testing frameworks that allow you to mock objects and simulate the
behavior of real objects, the PlatformIO Core 6.0 adds support for the
:ref:`unit_testing_simulators`.

The combination of simulation tools and testing frameworks allow you to
simulate hardware systems and run unit tests in virtual environments.
Simulators can significantly accelerate project development, especially
when used in pair with :ref:`ci`.

Integration of any simulator tool to the PlatformIO :ref:`unit_testing`
is very simple and does not require any extra software or code writing.
Please take a look at the example below how easy it is to integrate
the :ref:`unit_testing_simulators_renode` simulation framework:

.. code-block:: ini

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

What is changed or removed
--------------------------

Dropped automatic updates
~~~~~~~~~~~~~~~~~~~~~~~~~

Thanks to your feedback, we finally removed automatic updates of global libraries
and development platforms. Please use :ref:`cmd_pkg_outdated` to check for outdated
project packages and list version information for all dependencies.

The :ref:`cmd_pkg_update` is intended to update the project dependencies,
custom packages from the |PIOREGISTRY|, or external sources.

Command Line Interface
~~~~~~~~~~~~~~~~~~~~~~

The following commands have been changed in v6.0.

.. list-table::
    :header-rows:  1
    :widths: 25 75

    * - Command
      - Description
    * - :ref:`pio pkg <cmd_pkg>`
      - **NEW** Unified package management solution
    * - :ref:`cmd_project_init`
      - **NEW** :option:`pio project init --no-install-dependencies` option
    * - :ref:`cmd_project_metadata`
      - **NEW** :option:`pio project metadata --json-output-path` option
    * - :ref:`cmd_run`
      - **NEW** :option:`pio run --program-arg` option
    * - :ref:`cmd_test`
      - **NEW** :option:`pio test --program-arg`, :option:`pio test --json-output-path`,
        :option:`pio test --junit-output-path`, and :option:`pio test --list-tests` options
    * - ``pio project data``
      - **RENAMED** to the :ref:`cmd_project_metadata`
    * - :ref:`cmd_lib`
      - **DEPRECATED** in favor of :ref:`cmd_pkg`
    * - :ref:`cmd_platform`
      - **DEPRECATED** in favor of :ref:`cmd_pkg`
    * - :ref:`cmd_update`
      - **DEPRECATED** in favor of :ref:`cmd_pkg`
