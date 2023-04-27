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

.. _cmd_pkg_update:

pio pkg update
==============

.. contents::

Usage
-----

.. code-block:: bash

    pio pkg update [OPTIONS]

Description
-----------

Update the project dependencies, custom packages from the |PIOREGISTRY|, or
external sources.

If no custom packages (``--library``, ``--platform``, or ``--tool``) are
specified, the command will update the following project
dependencies based on :ref:`projectconf`:

* Library dependencies declared using the :ref:`projectconf_lib_deps` option
* Development platform declared using the :ref:`projectconf_env_platform` option
  and its dependencies (toolchain, framework, SDKs, debugging server, etc)
* Custom tools declared using the :ref:`projectconf_env_platform_packages` option.

See :ref:`cmd_pkg_install` command for package specification.

Options
-------

.. program:: pio pkg update

.. option::
    -d, --project-dir

Specify the path to project directory. By default, ``--project-dir`` is equal
to current working directory (``CWD``).

.. option::
    -e, --environment

Update project dependencies only for the specified environments.
Multiple environments are allowed.

.. option::
    -p, --platform

Update specified development platform. Multiple items are allowed.

**Examples**

.. code:: shell

    pio pkg update -p "aceinna/aceinna_imu@^1.3.8" -p "platformio/atmelavr"
    pio pkg update --platform "https://github.com/platformio/platform-sifive.git"

.. option::
    -t, --tool

Update specified tool. Multiple items are allowed.

**Examples**

.. code:: shell

    pio pkg update -t "platformio/tool-openocd"
    pio pkg update --tool https://github.com/platformio/platform-sifive.git

.. option::
    -l, --library

Update specified library. Multiple items are allowed.

**Examples**

.. code:: shell

    pio pkg update -l "bblanchon/ArduinoJson@^6.19.2" -l "milesburton/DallasTemperature@^3.9.1"
    pio pkg update --library https://github.com/Makuna/NeoPixelBus.git

.. option::
    --no-save

Prevent saving specified packages to :ref:`projectconf`.

.. option::
    --skip-dependencies

Update a package but skip its dependencies declared in the manifest
:ref:`manifest_library_json_dependencies` field.

.. option::
    -g, --global

Update packages from the global storage:

* :ref:`projectconf_pio_platforms_dir` - development platforms
* :ref:`projectconf_pio_packages_dir` - tools
* :ref:`projectconf_pio_globallib_dir` - libraries.

.. option::
    --storage-dir

Specify a custom Package Manager storage for global packages.

.. option::
    -s, --silent

Suppress progress reporting.

See Also
--------

* :ref:`cmd_pkg_outdated`
* :ref:`cmd_pkg_install`
* :ref:`cmd_pkg_uninstall`
* :ref:`library_json`
