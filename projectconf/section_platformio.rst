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

    There is a ``$PROJECT_HASH`` template variable. You can use it in a directory
    path. It will by replaced by a SHA1[0:10] hash of a full project path.
    This is very useful to declare a global storage for project workspaces.
    For example, ``/tmp/pio-workspaces/$PROJECT_HASH`` (Unix) or
    ``$[sysenv.TEMP}/pio-workspaces/$PROJECT_HASH`` (Windows).
    You can set a global workspace directory using system environment
    variable :envvar:`PLATFORMIO_WORKSPACE_DIR`.

    See below available directory ``***_dir`` options.

Generic options
~~~~~~~~~~~~~~~

``description``
^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``No``

Describe a project with a short information. PlatformIO uses it for
:ref:`piohome` in the multiple places.

.. _projectconf_pio_default_envs:

``default_envs``
^^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``Yes``

:ref:`cmd_run` command processes all environments ``[env:***]`` by default
if :option:`platformio run --environment` option is not specified.
:ref:`projectconf_pio_default_envs` allows one to define environments which
should be processed by default.

Also, :ref:`piodebug` checks this option when looking for debug environment.

Example:

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

``extra_configs``
^^^^^^^^^^^^^^^^^

.. versionadded:: 4.0

Type: ``String (Pattern)`` | Multiple: ``Yes``

This option allows extending a base :ref:`projectconf` with extra configuration
files. The format and rules are the same as for the :ref:`projectconf`.
A name of the configuration file can be any.

``extra_configs`` can be a single path to an extra configuration file or a list
of them. Please note that you can use Unix shell-style wildcards:

.. list-table::
    :header-rows:  1

    * - Pattern
      - Meaning

    * - ``*``
      - matches everything

    * - ``?``
      - matches any single character

    * - ``[seq]``
      - matches any character in seq

    * - ``[!seq]``
      - matches any character not in seq

.. note::
    If you declare the same pair of "group" + "option" in an extra configuration
    file which was previously declared in a base :ref:`projectconf`, it will
    be overwritten with a value from extra configuration.

**Example**

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


Directory options
~~~~~~~~~~~~~~~~~

.. _projectconf_pio_core_dir:

``core_dir``
^^^^^^^^^^^^

.. versionadded:: 4.0

Type: ``DirPath`` | Multiple: ``No``

Is used to store development platform packages (toolchains, frameworks, SDKs,
upload and debug tools), global libraries for :ref:`ldf`, and other PlatformIO
Core service data. The size of this folder will depend on number of installed
development platforms.

A default value is User's home directory:

* Unix ``~/.platformio``
* Windows ``%HOMEPATH%\.platformio``

This option can also be configured by global environment variable
:envvar:`PLATFORMIO_CORE_DIR`.

Example:

.. code-block:: ini

    [platformio]
    core_dir = /path/to/custom/pio-core/storage

.. _projectconf_pio_globallib_dir:

``globallib_dir``
^^^^^^^^^^^^^^^^^

.. versionadded:: 4.0

Type: ``DirPath`` | Multiple: ``No`` | Default: ":ref:`projectconf_pio_core_dir`/lib"

Global library storage for PlatfrmIO projects and :ref:`librarymanager` where
:ref:`ldf` looks for dependencies.

This option can also be configured by global environment variable
:envvar:`PLATFORMIO_GLOBALLIB_DIR`.

.. _projectconf_pio_platforms_dir:

``platforms_dir``
^^^^^^^^^^^^^^^^^

.. versionadded:: 4.0

Type: ``DirPath`` | Multiple: ``No`` | Default: ":ref:`projectconf_pio_core_dir`/platforms"

Global storage where **PlatformIO Package Manager** installs :ref:`platforms`.

This option can also be configured by global environment variable
:envvar:`PLATFORMIO_PLATFORMS_DIR`.

.. _projectconf_pio_packages_dir:

``packages_dir``
^^^^^^^^^^^^^^^^

.. versionadded:: 4.0

Type: ``DirPath`` | Multiple: ``No`` | Default: ":ref:`projectconf_pio_core_dir`/packages"

Global storage where **PlatformIO Package Manager** installs :ref:`platforms`
dependencies (toolchains, :ref:`frameworks`, SDKs, upload and debug tools).

This option can also be configured by global environment variable
:envvar:`PLATFORMIO_PACKAGES_DIR`.

.. _projectconf_pio_cache_dir:

``cache_dir``
^^^^^^^^^^^^^

.. versionadded:: 4.0

Type: ``DirPath`` | Multiple: ``No`` | Default: ":ref:`projectconf_pio_core_dir`/cache"

:ref:`piocore` uses this folder to store caching information (requests to
PlatformIO Registry, downloaded packages and other service information).

To reset a cache, please run :ref:`cmd_update` command.

This option can also be configured by global environment variable
:envvar:`PLATFORMIO_CACHE_DIR`.

.. _projectconf_pio_workspace_dir:

``workspace_dir``
^^^^^^^^^^^^^^^^^

.. versionadded:: 4.0

Type: ``DirPath`` | Multiple: ``No`` | Default: "Project/``.pio``"

A path to a project workspace directory where PlatformIO keeps by default
compiled objects, static libraries, firmwares, and external library
dependencies. It is used by the next options:

- :ref:`projectconf_pio_build_dir`
- :ref:`projectconf_pio_libdeps_dir`.

A default value is ``.pio`` and means that folder is located in the root of
project.

This option can also be configured by global environment variable
:envvar:`PLATFORMIO_WORKSPACE_DIR`.

.. _projectconf_pio_build_dir:

``build_dir``
^^^^^^^^^^^^^

.. warning::
    **PLEASE DO NOT EDIT FILES IN THIS FOLDER**. PlatformIO will overwrite
    your changes on the next build. **THIS IS A CACHE DIRECTORY**.

Type: ``DirPath`` | Multiple: ``No`` | Default: ":ref:`projectconf_pio_workspace_dir`/build"

*PlatformIO Build System* uses this folder for project
environments to store compiled object files, static libraries, firmwares and
other cached information. It allows PlatformIO to build source code extremely
fast!

*You can delete this folder without any risk!* If you modify :ref:`projectconf`,
then PlatformIO will remove this folder automatically. It will be created on the
next build operation.

This option can also be configured by global environment variable
:envvar:`PLATFORMIO_BUILD_DIR`.

.. note::
    If you have any problems with building your project environments which
    are defined in :ref:`projectconf`, then **TRY TO DELETE** this folder. In
    this situation you will remove all cached files without any risk. Also,
    you can use "clean" target for :option:`platformio run --target` command.

.. _projectconf_pio_libdeps_dir:

``libdeps_dir``
^^^^^^^^^^^^^^^

Type: ``DirPath`` | Multiple: ``No`` | Default: ":ref:`projectconf_pio_workspace_dir`/libdeps"

Internal storage where :ref:`librarymanager` will install project dependencies
(:ref:`projectconf_lib_deps`).

This option can also be configured by global environment variable
:envvar:`PLATFORMIO_LIBDEPS_DIR`.

.. _projectconf_pio_include_dir:

``include_dir``
^^^^^^^^^^^^^^^

Type: ``DirPath`` | Multiple: ``No`` | Default: "Project/``include``"

A path to project's default header files. PlatformIO uses it for :ref:`cmd_run`
command. A default value is ``include`` that means that folder is located in the
root of project. This path will be added to ``CPPPATH`` of build environment.

If you need to add extra include directories to ``CPPPATH`` scope, please use
:ref:`projectconf_build_flags` with ``-I /path/to/extra/dir`` option.

This option can also be configured by global environment variable
:envvar:`PLATFORMIO_INCLUDE_DIR`.

.. _projectconf_pio_src_dir:

``src_dir``
^^^^^^^^^^^

Type: ``DirPath`` | Multiple: ``No`` | Default: "Project/``src``"

A path to project's source directory. PlatformIO uses it for :ref:`cmd_run`
command. A default value is ``src`` that means that folder is located in the
root of project.

This option can also be configured by global environment variable
:envvar:`PLATFORMIO_SRC_DIR`.

.. note::
    This option is useful for people who migrate from Arduino IDE where
    source directory should have the same name as a main source file.
    See `example <https://github.com/platformio/platformio-examples/tree/develop/atmelavr/arduino-own-src_dir>`__ project with own source directory.

.. _projectconf_pio_lib_dir:

``lib_dir``
^^^^^^^^^^^

Type: ``DirPath`` | Multiple: ``No`` | Default: "Project/``lib``"

You can put here your own/private libraries. The source code of each library
should be placed in separate directory, like
``lib/private_lib/[here are source files]``. This directory has the highest
priority for :ref:`ldf`.

A default value is ``lib`` that means that folder is located in the root of
project.

This option can also be configured by global environment variable
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

.. _projectconf_pio_data_dir:

``data_dir``
^^^^^^^^^^^^

Type: ``DirPath`` | Multiple: ``No`` | Default: "Project/``data``"

Data directory to store contents and :ref:`platform_espressif_uploadfs`.
A default value is ``data`` that means that folder is located in the root of
project.

This option can also be configured by global environment variable
:envvar:`PLATFORMIO_DATA_DIR`.

.. _projectconf_pio_test_dir:

``test_dir``
^^^^^^^^^^^^

Type: ``DirPath`` | Multiple: ``No`` | Default: "Project/``test``"

Directory where :ref:`unit_testing` engine will look for the tests.
A default value is ``test`` that means that folder is located in the root of
project.

This option can also be configured by global environment variable
:envvar:`PLATFORMIO_TEST_DIR`.

.. _projectconf_pio_boards_dir:

``boards_dir``
^^^^^^^^^^^^^^

Type: ``DirPath`` | Multiple: ``No`` | Default: "Project/``boards``"

Custom board settings per project. You can change this path with your own.
A default value is ``boards`` that means that folder is located in the root of
project.

By default, PlatformIO looks for boards in this order:

1. Project :ref:`projectconf_pio_boards_dir`
2. Global :ref:`projectconf_pio_core_dir`/boards
3. Development platform :ref:`projectconf_pio_core_dir`/platforms/\*/boards.

This option can also be configured by global environment variable
:envvar:`PLATFORMIO_BOARDS_DIR`.

.. _projectconf_pio_shared_dir:

``shared_dir``
^^^^^^^^^^^^^^

Type: ``DirPath`` | Multiple: ``No`` | Default: "Project/``shared``"

:ref:`pioremote` uses this folder to synchronize extra files between remote
machine. For example, you can share :ref:`projectconf_extra_scripts`.

Please note that these folders are automatically shared between remote machine
with :option:`platformio remote run --force-remote` or
:option:`platformio remote test --force-remote` commands:

- :ref:`projectconf_pio_lib_dir`
- :ref:`projectconf_pio_include_dir`
- :ref:`projectconf_pio_src_dir`
- :ref:`projectconf_pio_boards_dir`
- :ref:`projectconf_pio_data_dir`
- :ref:`projectconf_pio_test_dir`

A default value is ``shared`` that means that folder is located in the root of
project.

This option can also be configured by global environment variable
:envvar:`PLATFORMIO_SHARED_DIR`.
