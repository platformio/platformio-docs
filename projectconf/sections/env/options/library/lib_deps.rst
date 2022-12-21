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

.. _projectconf_lib_deps:

``lib_deps``
------------

Type: ``Package Specification`` | Multiple: ``Yes``

.. seealso::
    Please make sure to read :ref:`librarymanager_dependencies` guide first.

Specify project dependencies using :ref:`cmd_pkg_install_specifications`
that should be installed automatically to the
:ref:`projectconf_pio_libdeps_dir` before environment processing.

If you have multiple build environments that depend on the same libraries,
you can use :ref:`projectconf_section_env` or :ref:`projectconf_interpolation`
to use the common configuration.

Check the `PlatformIO Registry <https://registry.platformio.org>`__
for the available libraries and the installation instructions.

**Example**

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
