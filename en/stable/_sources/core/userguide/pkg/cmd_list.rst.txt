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

.. _cmd_pkg_list:

pio pkg list
============

.. contents::

Usage
-----

.. code-block:: bash

    pio pkg list [OPTIONS]

Description
-----------

Print to stdout installed packages and their dependencies in a tree structure
based on project dependencies declared in :ref:`projectconf`:

* Library dependencies declared using the :ref:`projectconf_lib_deps` option
* Development platform declared using the :ref:`projectconf_env_platform` option
  and its dependencies (toolchain, framework, SDKs, debugging server, etc)
* Custom tools declared using the :ref:`projectconf_env_platform_packages` option.

Globally installed packages can be listed using the :option:`pio pkg list --global` option.

Options
-------

.. program:: pio pkg list

.. option::
    -d, --project-dir

Specify the path to project directory. By default, ``--project-dir`` is equal
to current working directory (``CWD``).

.. option::
    -e, --environment

List installed packages only for the specified environments. Multiple
environments are allowed.

.. option::
    -p, --platform

Filter installed platform package using :ref:`cmd_pkg_install_specifications`.
Multiple items are allowed.

.. option::
    -t, --tool

Filter installed tool package using :ref:`cmd_pkg_install_specifications`.
Multiple items are allowed.

.. option::
    -l, --library

Filter installed library package using :ref:`cmd_pkg_install_specifications`.
Multiple items are allowed.

.. option::
    -g, --global

List installed packages from the global storage:

* :ref:`projectconf_pio_platforms_dir` - development platforms
* :ref:`projectconf_pio_packages_dir` - tools
* :ref:`projectconf_pio_globallib_dir` - libraries.

.. option::
    --storage-dir

Specify a custom Package Manager storage for global packages.

.. option::
    --only-platforms

Print only installed platform packages.

.. option::
    --only-tools

Print only installed tool packages.

.. option::
    --only-libraries

Print only installed library packages.

.. option::
    -v, --verbose

Print additional package information.

See Also
--------

* :ref:`cmd_pkg_outdated`
* :ref:`cmd_pkg_install`
* :ref:`cmd_pkg_update`
* :ref:`cmd_pkg_uninstall`
* :ref:`library_json`
