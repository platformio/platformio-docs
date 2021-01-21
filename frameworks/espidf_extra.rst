..  Copyright (c) 2020-present PlatformIO <contact@platformio.org>
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

* :ref:`tutorial_espressif32_espidf_debugging_unit_testing_analysis`

Configuration
-------------

.. note::

    Starting with ESP-IDF v4.0, a CMake-based build system is used. Different
    configuration steps are required for ESP-IDF v3.x due to a legacy build system
    based on GNU Make.

.. contents::
    :local:
    :depth: 1


Each release of :ref:`platform_espressif32` platform uses a specific version of ESP-IDF.
The latest version of the platform only supports the latest stable version of the
framework.

.. warning::

    ESP-IDF v4.0 projects are not backwards-compatible with ESP-IDF v3.x projects in
    terms of project configuration process.

Configuration for 4.0
~~~~~~~~~~~~~~~~~~~~~

.. contents::
    :local:

The general project configuration (default optimization level, bootloader configuration
partition tables, etc) is set in a single file called ``sdkconfig`` in the root folder
of the project. This configuration file can be modified via a special target called
``menuconfig`` (PlatformIO v4.3.0 greater is required):

.. code-block:: none

    pio run -t menuconfig

.. warning::
    ESP-IDF requires some extra tools to be installed in your system in order to build
    firmware for supported chips. Most of these tools are available in PlatformIO
    ecosystem as standalone packages, but in order to use configuration tool called
    ``menuconfig`` several additional packages need to be installed on Linux-based
    systems:

    .. code-block:: none

        libncurses5-dev flex bison

    More details about required packages can be found in the official ESP-IDF documentation -
    `Standard Setup of Toolchain for Linux <https://docs.espressif.com/projects/esp-idf/en/latest/get-started/linux-setup.html>`_.

.. hint::
  If menuconfig is not showed properly in the integrated VS Code terminal try changing
  the default terminal shell by clicking the dropdown menu on the top-right of the
  terminal panel and selectiing the ``Select Default Shell`` option.

.. hint::
  In case the ``UP`` and ``DOWN`` arrows don't work in menuconfig try using the ``J``
  key to move the cursor down and ``K`` to move the cursor up. Another option is to use
  ``-`` and ``+`` keys on the numeric keypad.

Project Structure
^^^^^^^^^^^^^^^^^

The ESP-IDF framework requires an unusual project structure because most of the framework
configuration is performed by the native for the ESP-IDF build system called ``CMake``.

A typical PlatformIO project for the ESP-IDF framework must have the following structure:

.. code-block:: none

    project_dir
    ├── include
    ├── src
    │    ├── CMakeLists.txt
    │    └── main.c
    ├── CMakeLists.txt
    └── platformio.ini

.. tip::
    It's also possible to use the default ESP-IDF project structure with ``main`` folder.
    To specify ``main`` as the folder with source files use :ref:`projectconf_pio_src_dir`
    option, for example:

    .. code-block:: ini

        [platformio]
        src_dir = main

        [env:esp32dev]
        platform = espressif32
        framework = espidf
        board = esp32dev


Besides the files related to PlatformIO project, there are several additional
ESP-IDF-specific files: the main ``CMakeLists.txt``, project-specific ``CMakeLists.txt``
in :ref:`projectconf_pio_src_dir` and optional default configuration file ``sdkconfig.defaults``.
``CMakeLists.txt`` files enable features supported by the ESP-IDF's build system, e.g.
ULP configuration, adding extra components, etc. A typical ``CMakeLists.txt`` file in
the root folder has the following content:

.. code-block:: cmake

    # The following lines of boilerplate have to be in your project's CMakeLists
    # in this exact order for cmake to work correctly
    cmake_minimum_required(VERSION 3.16.0)

    include($ENV{IDF_PATH}/tools/cmake/project.cmake)
    project(project-name)

The second ``CMakeLists.txt`` in :ref:`projectconf_pio_src_dir` is responsible for
controlling the build process of the component and its integration into the overall
project. The minimal component ``CMakeLists.txt`` file simply registers the component to
the build system using ``idf_component_register``:

.. code-block:: cmake

    idf_component_register(SRCS "foo.c" "bar.c")

The files specified using ``idf_component_register`` are used **ONLY** for generating
build configurations, but it's highly recommended to specify all application source
files in order to keep the project compatible with the usual ESP-IDF workflow.

.. warning::
    By default PlatformIO expects source files to be located in the ``src`` folder. At
    the same time, the default location for source files within the ESP-IDF build system
    is a special folder with the name ``main``. Renaming the main component may require
    users to manually specify additional dependencies:

    .. code-block:: cmake

        idf_component_register(SRCS "main.c" REQUIRES idf::mbedtls)

    More details in the official ESP-IDF documentation -
    `Renaming main component <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/build-system.html?highlight=rename#renaming-main-component>`_.

Due to the current limitations of CMake file-based API, there is no way of generating
build configuration for source files written in various programming languages if they
are not specified in  ``idf_component_register`` command. If your project contains
libraries written in languages that differ from the language used for the main
application you need to create an empty file with the desired extension (e.g. ``*.cpp``
for ``C++``) in order to force CMake generate build configuration for this language.

.. note::
    Build configuration generated for source files specified in ``idf_component_register``
    is also used as the base build environment for project sources (including libraries).


ESP-IDF components
^^^^^^^^^^^^^^^^^^

ESP-IDF modules as modular pieces of standalone code might be useful for structuring
reusable code or including third party components that aren’t part of ESP-IDF.

These components contain either a single ``CMakeLists.txt`` file which controls the
build process of the component and its integration into the overall project. An
optional ``Kconfig`` file defines the component configuration options that can be set
via ``menuconfig``. Some components may also include ``Kconfig.projbuild`` and
``project_include.cmake`` files, which are special files for overriding parts of the
project. All valid components will be compiled as static libraries and linked to the
final firmware. There are two possible ways of adding extra components to PlatformIO
project:

* By adding a new component to an optional folder called ``components`` in the root of
  your project. This folder will be automatically scanned for valid components.
* Using ``EXTRA_COMPONENT_DIRS`` option in the root ``CMakeLists.txt`` file. This option
  represents a list of extra directories to search for components.

An example of specifying ``esp-aws-iot`` as an extra component:

.. code-block:: cmake

    # The following lines of boilerplate have to be in your project's CMakeLists
    # in this exact order for cmake to work correctly
    cmake_minimum_required(VERSION 3.16)

    include($ENV{IDF_PATH}/tools/cmake/project.cmake)
    list(APPEND EXTRA_COMPONENT_DIRS esp-aws-iot)
    project(subscribe_publish)

.. warning::
    Since :ref:`projectconf_pio_src_dir` is also passed to CMake as an extra component,
    you should only append to ``EXTRA_COMPONENT_DIRS`` variable in order not to override
    the default package.

Since the build may not work correctly if the full path to sources is greater than 250
characters (see ``CMAKE_OBJECT_PATH_MAX``) it might be a good idea to keep modules close
to the project files.

ULP coprocessor programming
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to take measurements using ADC, internal temperature sensor or external
I2C sensors, while the main processors are in deep sleep mode you need to use ULP
coprocessor. At the moment ULP can be used only with the :ref:`framework_espidf`.

All ULP code, usually written in assembly in files with ``.S`` extension,
must be placed into a separate directory with the name ``ulp`` in the root folder
of your project. So your project structure should look like this:

.. code-block:: none

    project_dir
    ├── include
    ├── src
    │    ├── CMakeLists.txt
    │    └── main.c
    ├── ulp
    │    └── ulp_code.S
    ├── CMakeLists.txt
    └── platformio.ini

Since PlatformIO uses the code model generated by CMake it's mandatory to specify ULP
source files in ``CMakeLists.txt`` as well. An example of typical ``CMakeLists.txt``
for ULP:

.. code-block:: cmake

    idf_component_register(SRCS "ulp_adc_example_main.c")
    #
    # ULP support additions to component CMakeLists.txt.
    #
    # 1. The ULP app name must be "ulp_main"
    set(ulp_app_name ulp_main)
    #
    # 2. Specify all assembly source files.
    #    Paths are relative because ULP files are placed into a special directory "ulp"
    #    in the root of the project
    set(ulp_s_sources "../ulp/adc.S")
    #
    # 3. List all the component source files which include automatically
    #    generated ULP export file, ${ulp_app_name}.h:
    set(ulp_exp_dep_srcs "ulp_adc_example_main.c")
    #
    # 4. Call function to build ULP binary and embed in project using the argument
    #    values above.
    ulp_embed_binary(${ulp_app_name} ${ulp_s_sources} ${ulp_exp_dep_srcs})

See full examples with ULP coprocessor programming:

- https://github.com/platformio/platform-espressif32/tree/develop/examples/espidf-ulp-adc
- https://github.com/platformio/platform-espressif32/tree/develop/examples/espidf-ulp-pulse

More details are located in the official ESP-IDF documentation -
`ULP coprocessor programming <https://docs.espressif.com/projects/esp-idf/en/latest/api-guides/ulp.html#accessing-ulp-program-variable>`_.

Limitations
^^^^^^^^^^^

At the moment several limitations are present:

* No whitespace characters allowed in project paths. This limitation is imposed by the
  `native ESP-IDF build system <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html?highlight=spaces#step-2-get-esp-idf>`_.
  This affects users that have a whitespace in their username or added a whitespace to
  the project name. As a workaround, it's recommended to move :ref:`projectconf_pio_core_dir`
  to a folder without spaces. For example:

  .. code-block:: ini

        [platformio]
        core_dir = C:/.platformio

        [env:esp32dev]
        platform = espressif32
        framework = espidf
        board = esp32dev

* The ``src_filter`` option cannot be used. It's done to preserve compatibility with
  existing ESP-IDF projects. List of source files is specified in the project
  ``CMakeLists.txt`` file.

Configuration for 3.0, 3.1, 3.2, 3.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support for ESP-IDF v3.x is considered obsolete and is not available in the latest
platform releases. Please check the `platform release notes <https://github.com/platformio/platform-espressif32/releases>`_
to figure out what version of the platform should be installed to use required ESP-IDF
version, for example:

    .. code-block:: ini

        [env:esp32dev]
        ; v1.10.0 is the last version that supports ESP-IDF v3.3
        platform = espressif32@1.10.0
        framework = espidf
        board = esp32dev

Project Structure
^^^^^^^^^^^^^^^^^

Due to limited support of GNU Make build system used in ESP-IDF v3.x, the project
configuration depends on a pregenerated file ``sdkconfig.h`` which contains a list of
macro definitions ``CONFIG_*``. These definitions describe project settings that will be
used for preparing a proper build environment. You can use the default ``sdkconfig.h``
shipped with the platform or generate a custom one using native ESP-IDF build
environment.

A typical PlatformIO project for ESP-IDF v3.x must have the following structure:

.. code-block:: none

    project_dir
    ├── include
    ├── lib
    │   └── README
    ├── test
    ├── src
    │    ├── sdkconfig.h
    │    └── main.c
    └── platformio.ini

Enable C++ exceptions
^^^^^^^^^^^^^^^^^^^^^

to enable C++ exceptions for :ref:`framework_espidf` add
``-D PIO_FRAMEWORK_ESP_IDF_ENABLE_EXCEPTIONS`` to :ref:`projectconf_build_flags` of
:ref:`projectconf`.

See `project example <https://github.com/platformio/platform-espressif32/tree/v1.10.0/examples/espidf-exceptions>`_
with enabled exceptions.

ULP coprocessor programming
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To use ULP in your project you need to make sure that it's enabled in the ``sdkconfig.h``
configuration file. The following two lines must be added:

.. code-block:: cpp

    #define CONFIG_ULP_COPROC_ENABLED 1
    #define CONFIG_ULP_COPROC_RESERVE_MEM 1024

Usually ``CONFIG_ULP_COPROC_RESERVE_MEM`` is already defined in the default
``sdkconfig.h`` with value ``0``. You can modify this value to meet your requirements.

All ULP code, usually written in assembly in files with ``.S`` extension, must be placed
into a separate directory with the name ``ulp`` in the root folder of your project.
So your project structure should look like this:

.. code-block:: bash

    project_dir
    ├── include
    ├── lib
    │   └── README
    ├── test
    ├── src
    │    ├── main.c
    │    └── sdkconfig.h
    ├── ulp
    │    └── ulp_code.S
    └── platformio.ini

See full examples with ULP coprocessor programming for ESP-IDF v3.x:

- https://github.com/platformio/platform-espressif32/tree/v1.10.0/examples/espidf-ulp-adc
- https://github.com/platformio/platform-espressif32/tree/v1.10.0/examples/espidf-ulp-pulse
