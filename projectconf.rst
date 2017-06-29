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

.. _projectconf:

Project Configuration File ``platformio.ini``
=============================================

The Project configuration file is named ``platformio.ini``. This is a
`INI-style <http://en.wikipedia.org/wiki/INI_file>`_ file.

``platformio.ini`` has sections (each denoted by a ``[header]``) and
key / value pairs within the sections. Lines beginning with ``;``
are ignored and may be used to provide comments.

Multi-values option could be specified in 2 ways:

1. Split values with ", " (comma + space)
2. Use multi-line format, where each new line should start with 2 spaces
   (minimum)

**Example**

.. code-block:: ini

    [platformio]
    env_default = uno
    ; Unix
    lib_extra_dirs = ${env.HOME}/Documents/Arduino/libraries
    ; Windows
    lib_extra_dirs = ${env.HOMEDRIVE}${env.HOMEPATH}\Documents\Arduino\libraries

    ; You MUST inject these options into [env:] section
    ; using ${common_env_data.***} (see below)
    [common_env_data]
    build_flags = -D VERSION=1.2.3 -D DEBUG=1
    lib_deps_builtin =
      SPI
      Wire
    lib_deps_external =
        ArduinoJson@~5.6,!=5.4
        https://github.com/gioblu/PJON.git#v2.0
        https://github.com/me-no-dev/ESPAsyncTCP.git
        https://github.com/adafruit/DHT-sensor-library/archive/master.zip

    [env:uno]
    platform = atmelavr
    framework = arduino
    board = uno
    build_flags = ${common_env_data.build_flags}
    lib_deps = ${common_env_data.lib_deps_builtin}, ${common_env_data.lib_deps_external}

    [env:nodemcuv2]
    platform = espressif8266
    framework = arduino
    board = nodemcuv2
    build_flags = ${common_env_data.build_flags} -DSSID_NAME=HELLO -DSSID_PASWORD=WORLD
    lib_deps =
      ${common_env_data.lib_deps_builtin}
      ${common_env_data.lib_deps_external}
      PubSubClient@2.6
      OneWire


There are 2 system reserved sections:

* :ref:`piocore` settings: :ref:`projectconf_section_platformio`
* Environment settings: :ref:`projectconf_section_env`

The other sections can be used by users, for example, for
:ref:`projectconf_dynamic_vars`. The sections and their allowable values are
described below.

.. toctree::
    :maxdepth: 2

    projectconf/section_platformio
    projectconf/section_env
    projectconf/dynamic_variables
    projectconf/examples
