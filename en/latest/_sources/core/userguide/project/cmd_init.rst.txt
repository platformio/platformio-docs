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

.. _cmd_project_init:

pio project init
================

.. contents::

Usage
-----

.. code-block:: bash

    pio project init [OPTIONS]


Description
-----------

Initialize a new PlatformIO based project or update existing with new data.

This command will create:

* :ref:`projectconf`
* :ref:`projectconf_pio_include_dir`, put project header files here
* :ref:`projectconf_pio_src_dir`, put project source files here
  (``*.h, *.c, *.cpp, *.S, *.ino, etc.``)
* :ref:`projectconf_pio_lib_dir`, put project specific (private) libraries here.
  See also :ref:`ldf`
* :ref:`projectconf_pio_test_dir`, put project tests here. More details :ref:`unit_testing`
* Miscellaneous files for VCS and :ref:`ci` support.

Options
-------

.. program:: pio project init

.. option::
    -d, --project-dir

A path to a directory where *PlatformIO* will initialize new project.

.. option::
    -b, --board

If you specify board ``ID`` (you can pass multiple ``--board`` options), then
*PlatformIO* will automatically generate environment for :ref:`projectconf` and
pre-fill these data:

* :ref:`projectconf_env_platform`
* :ref:`projectconf_env_framework`
* :ref:`projectconf_env_board`

The full list with pre-configured boards is available here :ref:`platforms`.

.. option::
    --ide

Initialize PlatformIO project for the specified IDE which can be imported later
via "Import Project" functionality.

A list with supported IDE is available within ``pio project init --help`` command.
Also, please take a look at :ref:`ide` page.

.. option::
    -e, --environment

.. versionadded:: 5.0

Update project using existing environment.

.. option::
    -O, --project-option

Initialize project with additional options from :ref:`projectconf`. For example,
``pio project init --project-option="lib_deps=ArduinoJSON"``.
Multiple options are allowed.

.. option::
    --env-prefix

An environment prefix which will be used with pair in :ref:`projectconf_env_board` ID.
For example, the default environment name for :ref:`board_teensy_teensy31`
board will be ``[env:teensy31]``.

.. option::
    -s, --silent

Suppress progress reporting

Examples
--------

1. Initialize new project in a current working directory

.. code::

    > pio project init

    The current working directory *** will be used for the new project.
    You can specify another project directory via
    `pio project init -d %PATH_TO_THE_PROJECT_DIR%` command.

    The next files/directories will be created in ***
    platformio.ini - Project Configuration File. |-> PLEASE EDIT ME <-|
    src - Put your source files here
    lib - Put here project specific (private) libraries
    Project has been successfully initialized!
    Useful commands:
    `pio run` - process/build project from the current directory
    `pio run --target upload` or `pio run -t upload` - upload firmware to embedded board
    `pio run --target clean` - clean project (remove compiled files)


2. Initialize new project in a specified directory

.. code::

    > pio project init -d %PATH_TO_DIR%

    The next files/directories will be created in ***
     platformio.ini - Project Configuration File. |-> PLEASE EDIT ME <-|
    ...

3. Initialize project for Arduino Uno

.. code::

    > pio project init --board uno

    The current working directory *** will be used for the new project.
    You can specify another project directory via
    `pio project init -d %PATH_TO_THE_PROJECT_DIR%` command.
    ...

4. Initialize project for Teensy 3.1 board with custom :ref:`framework_mbed`

.. code::

    > pio project init --board teensy31 --project-option "framework=mbed"

    The current working directory *** will be used for the new project.
    You can specify another project directory via
    `pio project init -d %PATH_TO_THE_PROJECT_DIR%` command.

    ...

5. Initialize a new project passing working environment name and its options

.. code::

    > pio project init --environment native --project-option="platform=native" --project-option="build_flags=-DRELEASE=1"

    The current working directory *** will be used for the new project.
    ...