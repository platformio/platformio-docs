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

.. _cmd_ci:

pio ci
======

.. contents::

Usage
-----

.. code-block:: bash

    pio ci [OPTIONS] [SRC]


Description
-----------

:ref:`cmd_ci` command is conceived of as "hot key" for building project with
arbitrary source code structure. In a nutshell, using ``SRC`` and
:option:`pio ci --lib` contents PlatformIO initializes via
:ref:`cmd_project_init` new project in :option:`pio ci --build-dir`
with the build environments (using :option:`pio ci --board` or
:option:`pio ci --project-conf`) and processes them via :ref:`cmd_run`
command.

:ref:`cmd_ci` command accepts **multiple** ``SRC`` arguments,
:option:`pio ci --lib` and :option:`pio ci --exclude` options
which can be a path to directory, file or
`Glob Pattern <http://en.wikipedia.org/wiki/Glob_(programming)>`_.
Also, you can omit ``SRC`` argument and set path (multiple paths are allowed
denoting with ``:``) to
``PLATFORMIO_CI_SRC`` `Environment variable <http://en.wikipedia.org/wiki/Environment_variable>`_

For more details as for integration with the popular Continuous Integration
Systems please follow to :ref:`ci` page.

.. note::
    :ref:`cmd_ci` command is useful for library developers. It allows one to build
    different examples without creating own project per them. Also, is possible
    to upload firmware to the target device. In this case, you need to pass
    additional option ``--project-option="targets=upload"``. What is more,
    you can specify custom upload port using
    ``--project-option="upload_port=<port>"`` option.
    See :option:`pio ci --project-option` for details.

Options
-------

.. program:: pio ci

.. option::
    -l, --lib

Source code which will be copied to ``<BUILD_DIR>/lib`` directly.

If :option:`pio ci --lib` is a path to file (not to directory), then
PlatformIO will create temporary directory within ``<BUILD_DIR>/lib`` and copy
the rest files into it.


.. option::
    --exclude

Exclude directories and/-or files from :option:`pio ci --build-dir`. The
path must be relative to PlatformIO project within
:option:`pio ci --build-dir`.

For example, exclude from project ``src`` directory:

* ``examples`` folder
* ``*.h`` files from ``foo`` folder

.. code-block:: bash

    pio ci --exclude=src/examples --exclude=src/foo/*.h [SRC]

.. option::
    -b, --board

Build project with automatically pre-generated environments based on board
settings.

For more details please look into :option:`pio project init --board`.

.. option::
    --build-dir

Path to directory where PlatformIO will initialise new project. By default it's
temporary directory within your operating system.

.. note::

    This directory will be removed at the end of build process. If you want to
    keep it, please use :option:`pio ci --keep-build-dir`.

.. option::
    --keep-build-dir

Don't remove :option:`pio ci --build-dir` after build process.

.. option::
    -c, --project-conf

Build project using pre-configured :ref:`projectconf`.

.. option::
    -O, --project-option

Pass additional options from :ref:`projectconf` to :ref:`cmd_project_init` command.
For example, automatically install dependent libraries
``pio ci --project-option="lib_deps=ArduinoJSON"`` or ignore specific
library ``pio ci --project-option="lib_ignore=SomeLib"``.

.. note::
    Use multiple ``--project-option`` to pass multiple options to
    :ref:`projectconf`. One option per one argument. For example,
    ``pio ci --project-option="build_unflags = -std=gnu++11" --project-option="build_flags = -std=c++14"``

.. option::
    -v, --verbose

Shows detailed information when processing environments.

This option can also be set globally using :ref:`setting_force_verbose` setting
or by environment variable :envvar:`PLATFORMIO_SETTING_FORCE_VERBOSE`.

Examples
--------

For the others examples please follow to :ref:`ci` page.
