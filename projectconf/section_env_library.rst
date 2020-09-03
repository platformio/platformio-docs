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

.. _projectconf_section_env_library:

Library options
---------------

.. seealso::
    Please make sure to read :ref:`ldf` guide first.

.. contents::
    :local:

.. _projectconf_lib_deps:

``lib_deps``
^^^^^^^^^^^^

.. seealso::
    Please make sure to read :ref:`ldf` guide first.

Type: ``String`` | Multiple: ``Yes``

Specify project dependencies that should be installed automatically to
:ref:`projectconf_pio_libdeps_dir` before environment processing.

If you have multiple build environments that depend on the same libraries,
you can use :ref:`projectconf_dynamic_vars` to use common configuration.

**Valid forms**

.. code-block:: ini

  ; one line definition (comma + space)
  [env:myenv]
  lib_deps = LIBRARY_1, LIBRARY_2, LIBRARY_N

  ; multi-line definition
  [env:myenv2]
  lib_deps =
    LIBRARY_1
    LIBRARY_2
    LIBRARY_N

The each line with ``LIBRARY_1... LIBRARY_N`` will be passed automatically to
:ref:`cmd_lib_install` command.

Please check :ref:`cmd_lib_install` for the valid declaration formats.

Example:

.. code-block:: ini

  [env:myenv]
  lib_deps =
    ; name-based (built-in library in framework)
    SPI

    ; owner-based declaration
    knolleary/PubSubClient

    ; SemVer specification
    bblanchon/ArduinoJson @ ~5.6,!=5.4

    ; external Git resource
    https://github.com/gioblu/PJON.git#v2.0

    ; custom name
    IRremoteESP8266=https://github.com/markszabo/IRremoteESP8266/archive/master.zip


.. _projectconf_lib_ignore:

``lib_ignore``
^^^^^^^^^^^^^^

.. seealso::
    Please make sure to read :ref:`ldf` guide first.

Type: ``String`` | Multiple: ``Yes``

Specify libraries which should be ignored by Library Dependency Finder.

The correct value for this option is a library name (not folder name).
You will see these names in "Library Dependency Graph" when building a project
between ``<`` and ``>`` symbols.

**Example:**

``Build output``

.. code::

    ...
    Library Dependency Finder -> http://bit.ly/configure-pio-ldf
    LDF MODES: FINDER(chain+) COMPATIBILITY(soft)
    Collected 54 compatible libraries
    Scanning dependencies...
    Dependency Graph
    |-- <Hash> v1.0
    |-- <AsyncMqttClient> v0.8.2
    |   |-- <ESPAsyncTCP> v1.1.3
    |-- <ESP8266WiFi> v1.0
    |-- <ESP Async WebServer> v1.1.1
    |   |-- <ESPAsyncTCP> v1.1.3
    |   |-- <ESP8266WiFi> v1.0
    |   |-- <Hash> v1.0
    |   |-- <ArduinoJson> v5.13.1
    |-- <ArduinoJson> v5.13.1
    |-- <DNSServer> v1.1.0
    |   |-- <ESP8266WiFi> v1.0
    |-- <Ticker> v1.0
    ....

``platformio.ini``

.. code-block:: ini

    [env:myenv]
    ; Single line
    lib_ignore = AsyncMqttClient, DNSServer

    ; Multi-line
    lib_ignore =
      AsyncMqttClient
      ESP Async WebServer

.. _projectconf_lib_extra_dirs:

``lib_extra_dirs``
^^^^^^^^^^^^^^^^^^

.. seealso::
    Please make sure to read :ref:`ldf` guide first.

Type: ``DirPath`` | Multiple: ``Yes``

A list with extra directories/storages where :ref:`ldf` will
look for dependencies.

This option can also be set by global environment variable
:envvar:`PLATFORMIO_LIB_EXTRA_DIRS`.

.. warning::
  This is a not direct path to a library with source code. It should be a path
  to storage that contains libraries grouped by folders. For example,
  ``D:\PlatformIO\extra\libraries`` but not ``D:\PlatformIO\extra\libraries\FooLibrary``.

Example:

.. code-block:: ini

    [env:myenv]
    lib_extra_dirs =
        /common/libraries
        /iot/libraries

.. _projectconf_lib_ldf_mode:

``lib_ldf_mode``
^^^^^^^^^^^^^^^^

.. seealso::
    Please make sure to read :ref:`ldf` guide first.

Type: ``String`` | Multiple: ``No`` | Default: ``chain``

This option specifies how does Library Dependency Finder should analyze
dependencies (``#include`` directives). See :ref:`ldf_mode` for details
and available options.

Example:

.. code-block:: ini

    [env:myenv]
    ; evaluate C/C++ Preprocessor conditional syntax
    lib_ldf_mode = chain+

.. _projectconf_lib_compat_mode:

``lib_compat_mode``
^^^^^^^^^^^^^^^^^^^

.. seealso::
    Please make sure to read :ref:`ldf` guide first.

Type: ``String`` | Multiple: ``No`` | Default: ``soft``

Library compatibility mode allows one to control strictness of Library Dependency
Finder. See :ref:`ldf_compat_mode` for details and available options..

By default, this value is set to ``lib_compat_mode = soft`` and means that LDF
will check only for framework compatibility.

Example:

.. code-block:: ini

    [env:myenv]
    ; Checks for the compatibility with frameworks and dev/platforms
    lib_compat_mode = strict

.. _projectconf_lib_archive:

``lib_archive``
^^^^^^^^^^^^^^^

Type: ``Bool (yes or no)`` | Multiple: ``No`` | Default: ``yes``

Create an archive (``*.a``, static library) from the object files and link it
into a firmware (program). This is default behavior of PlatformIO Build System
(``lib_archive = yes``).

Setting ``lib_archive = no`` will instruct PlatformIO Build System to link object
files directly (in-line). This could be useful if you need to override ``weak``
symbols defined in framework or other libraries.

You can disable library archiving per a custom library using
:ref:`libjson_archive` field in :ref:`library_json` manifest.

Example:

.. code-block:: ini

    [env:myenv]
    lib_archive = no
