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

Tutorials
---------

* :ref:`tutorial_nordicnrf52_zephyr_debugging_unit_testing_analysis`
* `Enabling PlatformIO and Zephyr on custom hardware <https://piolabs.com/blog/engineering/platformio-zephyr-custom-hardware.html>`__

Configuration
-------------

.. contents::
    :local:

Project Structure
~~~~~~~~~~~~~~~~~

.. warning::
    Zephyr framework currently requires Python 3.4 or later.

Zephyr framework requires an unusual project structure because most of the framework
configuration is performed by the native for Zephyr build system called ``CMake``.

.. note::
    Since PlatformIO is able to generate CMake-based projects for certain IDEs, Zephyr-related
    files are moved to a separate folder in order to avoid conflicts between project files.
    That requires users to specify relative paths to source files in ``CMakeLists.txt``.

A typical PlatformIO project for Zephyr framework must have the following structure:

.. code-block:: bash

    project_dir
    ├── include
    ├── src
    │    └── main.c
    ├── zephyr
    │    ├── prj.conf
    │    └── CMakeLists.txt
    └── platformio.ini

Besides files related to PlatformIO project, there is an additional folder ``zephyr``
that contains Zephyr-specific files ``CMakeLists.txt`` and ``prj.conf``:

``CMakeLists.txt`` file enables features supported by Zephyr's build system, e.g.
board-specific kernel configuration files. A typical ``CMakeLists.txt`` file has the
following content:

.. code-block:: bash

    # Boilerplate code, which pulls in the Zephyr build system.
    cmake_minimum_required(VERSION 3.13.1)
    include($ENV{ZEPHYR_BASE}/cmake/app/boilerplate.cmake NO_POLICY_SCOPE)
    project(my_zephyr_app)

    # Add your source file to the "app" target. This must come after the boilerplate
    # code, which defines the target. Note relative path to source file
    target_sources(app PRIVATE ../src/main.c)

The files specified in ``target_sources`` are used **ONLY** for generating build
configurations, but it's highly recommended to specify all application source files in
order to keep the project compatible with the usual Zephyr workflow.

Due to the current limitations of CMake file-based API, there is no way to generate build
configuration for source files written in various programming languages if they are not
specified in  ``target_sources`` command. If your project contains libraries written
in languages that differ from the language used for the main application you need to
create an empty file with desired extension (e.g. ``*.cpp`` for ``C++``) in order to
force CMake generate build configuration for this language.

.. note::
    Build configuration generated for source files specified in ``target_sources`` is
    also used as the base build environment for project sources (including libraries).


``prj.conf`` file sets application-specific values for one or more kernel configuration
options. These application settings are merged with board-specific settings to produce a
kernel configuration.

Devicetree overlays
~~~~~~~~~~~~~~~~~~~

Zephyr applications can use overlay files to enable a peripheral that is disabled by
default, select a sensor on the board for an application specific purpose, etc. This
makes it possible to reconfigure the kernel and device drivers without modifying source
code. There are several ways to set ``.overlay`` files:

* Using ``DTC_OVERLAY_FILE`` variable in the ``CMakeLists.txt`` file,
  before including Zephyr's ``boilerplate.cmake`` file. (Recommended)

* Using a ``boards/<BOARD>.overlay`` file in the ``zephyr`` folder, for the current
  board

* Using a ``<BOARD>.overlay`` file in the  ``zephyr`` folder.

.. warning::
    PlatformIO board names may differ from Zephyr targets, which means that to help
    the build system automatically pick up ``.overlay`` file, the ``<BOARD>`` name in
    ``<BOARD>.overlay`` file must have the same name as specified in
    `the official Zephyr board list <https://docs.zephyrproject.org/latest/boards/index.html>`_.

Embedding files at compile time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case your ``CMakeLists.txt`` relies on using ``generate_inc_*`` functions that are
used for generating and compressing individual files (for example certificates for secure
connections) you need to configure your PlatformIO project accordingly using the
following structure:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    framework = zephyr
    board_build.embed_files =
        # files to be embedded
        src/apps-cert.der
        src/apps-key.der

Where ``apps-cert.der`` and ``apps-key.der`` are the files you want to embed to your
project at the compile time.

Zephyr modules
~~~~~~~~~~~~~~

.. note::
    PlatformIO automatically installs several default modules used with Zephyr framework
    including modules that implement silicon vendor Hardware Abstraction Layers (HALs).

Zephyr modules are externally maintained packages that allow using well-established
and mature code created by third party developers.

These modules contain either a single ``module.yml`` file or ``CMakeLists.txt`` and
``Kconfig`` files that describe how to build and configure them. You can specify paths
to additional directories with source code, Kconfig, etc. using ``ZEPHYR_EXTRA_MODULES``
at the top of your project's  ``CMakeLists.txt`` file, for example:

.. code-block:: bash

    # Additional modules
    set(ZEPHYR_EXTRA_MODULES "path/to-zephyr-custom-module"  [...])

    # Boilerplate code, which pulls in the Zephyr build system.
    cmake_minimum_required(VERSION 3.13.1)
    include($ENV{ZEPHYR_BASE}/cmake/app/boilerplate.cmake NO_POLICY_SCOPE)
    project(my_zephyr_app)

    # Add your source file to the "app" target. This must come after
    # the boilerplate code, which defines the target.
    target_sources(app PRIVATE ../src/main.c)

Since the build may not work correctly if the full path to sources is greater than 250
characters (see ``CMAKE_OBJECT_PATH_MAX``) it might be a good idea to keep modules close
to the project configuration files (e.g. in ``zephyr`` folder) in form of a git submodule.

.. warning::
    Make sure the ``ZEPHYR_EXTRA_MODULES`` variable is set before including the boilerplate
    file, as shown above.


Limitations
~~~~~~~~~~~

At the moment several limitations are present:

* The minimum supported version of Python is ``3.4``
* No whitespace characters allowed in project paths.
* OpenThread module is not supported
