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

.. _projectconf_section_platformio:

Section ``[platformio]``
------------------------

.. contents::
    :local:

A ``platformio`` section is used for overriding default configuration options
for :ref:`piocore`.

.. note::
    Relative path is allowed for directory option:

    * ``~`` will be expanded to user's home directory
    * ``../`` or ``..\`` go up to one folder

Options
~~~~~~~

``description``
^^^^^^^^^^^^^^^
Describe a project with a short information. PlatformIO uses it for
:ref:`piohome` in the multiple places.

.. _projectconf_pio_env_default:

``env_default``
^^^^^^^^^^^^^^^

:ref:`cmd_run` command processes all environments ``[env:***]`` by default
if :option:`platformio run --environment` option is not specified.
:ref:`projectconf_pio_env_default` allows to define environments which
should be processed by default.

Also, :ref:`piodebug` checks this option when looking for debug environment.

Multiple environments are allowed if they *are separated with ", "
(comma+space)*. For example.

.. code-block:: ini

    [platformio]
    env_default = uno, nodemcu

    [env:uno]
    platform = atmelavr
    framework = arduino
    board = uno

    [env:nodemcu]
    platform = espressif8266
    framework = arduino
    board = nodemcu

    [env:teensy31]
    platform = teensy
    framework = arduino
    board = teensy31

    [env:lpmsp430g2553]
    platform = timsp430
    framework = energia
    board = lpmsp430g2553
    build_flags = -D LED_BUILTIN=RED_LED

.. _projectconf_pio_home_dir:

``home_dir``
^^^^^^^^^^^^

Is used to store platform toolchains, frameworks, global libraries for
:ref:`ldf`, service data and etc. The size of this folder will depend on
number of installed development platforms.

A default value is User's home directory:

* Unix ``~/.platformio``
* Windows ``%HOMEPATH%\.platformio``

This option can be overridden by global environment variable
:envvar:`PLATFORMIO_HOME_DIR`.

Example:

.. code-block:: ini

    [platformio]
    home_dir = /path/to/custom/pio/storage

.. _projectconf_pio_build_dir:

``build_dir``
^^^^^^^^^^^^^

.. warning::
    **PLEASE DO NOT EDIT FILES IN THIS FOLDER**. PlatformIO will overwrite
    your changes on the next build. **THIS IS A CACHE DIRECTORY**.

*PlatformIO Build System* uses this folder for project
environments to store compiled object files, static libraries, firmwares and
other cached information. It allows PlatformIO to build source code extremely
fast!

*You can delete this folder without any risk!* If you modify :ref:`projectconf`,
then PlatformIO will remove this folder automatically. It will be created on the
next build operation.

A default value is ``.pioenvs`` that means that folder is located in the root of
project.

This option can be overridden by global environment variable
:envvar:`PLATFORMIO_BUILD_DIR`.

.. note::
    If you have any problems with building your Project environments which
    are defined in :ref:`projectconf`, then **TRY TO DELETE** this folder. In
    this situation you will remove all cached files without any risk.

.. _projectconf_pio_include_dir:

``include_dir``
^^^^^^^^^^^^^^^

A path to project's headers files. PlatformIO uses it for :ref:`cmd_run`
command. A default value is ``include`` that means that folder is located in the
root of project. This path will be added to ``CPPPATH`` of build environment.

This option can be overridden by global environment variable
:envvar:`PLATFORMIO_INCLUDE_DIR`.

.. _projectconf_pio_src_dir:

``src_dir``
^^^^^^^^^^^

A path to project's source directory. PlatformIO uses it for :ref:`cmd_run`
command. A default value is ``src`` that means that folder is located in the
root of project.

This option can be overridden by global environment variable
:envvar:`PLATFORMIO_SRC_DIR`.

.. note::
    This option is useful for people who migrate from Arduino/Energia IDEs where
    source directory should have the same name like the main source file.
    See `example <https://github.com/platformio/platformio-examples/tree/develop/atmelavr/arduino-own-src_dir>`__ project with own source directory.

.. _projectconf_pio_lib_dir:

``lib_dir``
^^^^^^^^^^^

You can put here your own/private libraries. The source code of each library
should be placed in separate directory, like
``lib/private_lib/[here are source files]``. This directory has the highest
priority for :ref:`ldf`.

A default value is ``lib`` that means that folder is located in the root of
project.

This option can be overridden by global environment variable
:envvar:`PLATFORMIO_LIB_DIR`.

For example, see how can be organized ``Foo`` and ``Bar`` libraries:

.. code::

    |--lib
    |  |--Bar
    |  |  |--docs
    |  |  |--examples
    |  |  |--src
    |  |     |- Bar.c
    |  |     |- Bar.h
    |  |--Foo
    |  |  |- Foo.c
    |  |  |- Foo.h
    |- platformio.ini
    |--src
       |- main.c


Then in ``src/main.c`` you should use:

.. code-block:: c

    #include <Foo.h>
    #include <Bar.h>

    // rest H/C/CPP code

PlatformIO will find your libraries automatically, configure preprocessor's
include paths and build them.

.. _projectconf_pio_libdeps_dir:

``libdeps_dir``
^^^^^^^^^^^^^^^

Internal storage where :ref:`librarymanager` will install project dependencies
(:ref:`projectconf_lib_deps`). A default value is ``.piolibdeps`` that means
that folder is located in the root of project.

This option can be overridden by global environment variable
:envvar:`PLATFORMIO_LIBDEPS_DIR`.

.. _projectconf_global_lib_extra_dirs:

``lib_extra_dirs``
^^^^^^^^^^^^^^^^^^

.. versionadded:: 3.2

A list with extra storages for a project where :ref:`ldf` will look for libraries.

This option has the same behavior as :ref:`projectconf_lib_extra_dirs` option
for a specific build environment defined in ``[env:]`` section. The main
difference is that the option which is defined in ``[platofrmio]`` section
will be extra applied automatically for all ``[env:]`` sections.

For the possible values and examples please follow to :ref:`projectconf_lib_extra_dirs`.

.. _projectconf_pio_data_dir:

``data_dir``
^^^^^^^^^^^^

Data directory to store contents and :ref:`platform_espressif_uploadfs`.
A default value is ``data`` that means that folder is located in the root of
project.

This option can be overridden by global environment variable
:envvar:`PLATFORMIO_DATA_DIR`.

.. _projectconf_pio_test_dir:

``test_dir``
^^^^^^^^^^^^

Directory where :ref:`unit_testing` engine will look for the tests.
A default value is ``test`` that means that folder is located in the root of
project.

This option can be overridden by global environment variable
:envvar:`PLATFORMIO_TEST_DIR`.

.. _projectconf_pio_boards_dir:

``boards_dir``
^^^^^^^^^^^^^^

Custom board settings per project. You can change this path with your own.
A default value is ``boards`` that means that folder is located in the root of
project.

By default, PlatformIO looks for boards in this order:

1. Project :ref:`projectconf_pio_boards_dir`
2. Global :ref:`projectconf_pio_home_dir`/boards
3. Development platform :ref:`projectconf_pio_home_dir`/platforms/\*/boards.

This option can be overridden by global environment variable
:envvar:`PLATFORMIO_BOARDS_DIR`.
