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

.. _cmd_pkg_uninstall:

pio pkg uninstall
=================

.. contents::

Usage
-----

.. code-block:: bash

    pio pkg uninstall [OPTIONS]

Description
-----------

Uninstall the project dependencies or custom packages from the |PIOREGISTRY| or
external sources.

If no custom packages (``--library``, ``--platform``, or ``--tool``) are
specified, the command will uninstall the following project
dependencies based on :ref:`projectconf`:

* Library dependencies declared using the :ref:`projectconf_lib_deps` option
* Development platform declared using the :ref:`projectconf_env_platform` option
  and its dependencies (toolchain, framework, SDKs, debugging server, etc)
* Custom tools declared using the :ref:`projectconf_env_platform_packages` option.

See :ref:`cmd_pkg_install` command for package specification.

Options
-------

.. program:: pio pkg uninstall

.. option::
    -d, --project-dir

Specify the path to project directory. By default, ``--project-dir`` is equal
to current working directory (``CWD``).

.. option::
    -e, --environment

Uninstall project dependencies only for the specified environments.
Multiple environments are allowed.

.. option::
    -p, --platform

Uninstall specified development platform using :ref:`cmd_pkg_install_specifications`.
Multiple items are allowed.

**Examples**

.. code:: shell

    pio pkg uninstall -p "aceinna/aceinna_imu@^1.3.8" -p "platformio/atmelavr"
    pio pkg uninstall --platform "https://github.com/platformio/platform-sifive.git"

.. option::
    -t, --tool

Uninstall specified tool using :ref:`cmd_pkg_install_specifications`.
Multiple items are allowed.

**Examples**

.. code:: shell

    pio pkg uninstall -t "platformio/tool-openocd"
    pio pkg uninstall --tool https://github.com/platformio/platform-sifive.git

.. option::
    -l, --library

Uninstall specified library using :ref:`cmd_pkg_install_specifications`.
Multiple items are allowed.

**Examples**

.. code:: shell

    pio pkg uninstall -l "bblanchon/ArduinoJson@^6.19.2" -l "milesburton/DallasTemperature@^3.9.1"
    pio pkg uninstall --library https://github.com/Makuna/NeoPixelBus.git

.. option::
    --no-save

Prevent removing specified packages from :ref:`projectconf`.

.. option::
    --skip-dependencies

Uninstall a package and keep its dependencies declared in the manifest
:ref:`manifest_library_json_dependencies` field.

.. option::
    -g, --global

Uninstall packages from the global storage:

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

* :ref:`cmd_pkg_install`
* :ref:`cmd_pkg_outdated`
* :ref:`library_json`
