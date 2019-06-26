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

"platformio.ini" (Project Configuration File)
=============================================

The Project configuration file is named ``platformio.ini``. This is a
`INI-style <http://en.wikipedia.org/wiki/INI_file>`_ file.

``platformio.ini`` has sections (each denoted by a ``[header]``) and
key / value pairs within the sections. Lines beginning with ``;``
are ignored and may be used to provide comments.

Multiple values option can be specified in 2 ways:

1. Split values with ", " (comma + space)
2. Use multi-line format, where each new line should start with 2 spaces
   (minimum)

There are 2 system reserved sections:

* :ref:`piocore` settings: :ref:`projectconf_section_platformio`
* Environment settings: :ref:`projectconf_section_env`

The other sections can be used by users, for example, for
:ref:`projectconf_dynamic_vars`. The sections and their allowable values are
described below.

.. toctree::
    :maxdepth: 2

    [platformio] <projectconf/section_platformio>
    [env] <projectconf/section_env>
    projectconf/build_configurations
    projectconf/dynamic_variables
    projectconf/examples

**Example**

.. code-block:: ini

    [platformio]
    env_default = nodemcuv2

    ; You MUST inject these options into [env:] section
    ; using ${common_env_data.***} (see below)
    [common_env_data]
    build_flags =
        -D VERSION=1.2.3
        -D DEBUG=1
    lib_deps_builtin =
        SPI
        Wire
    lib_deps_external =
        ArduinoJson@~5.6,!=5.4
        https://github.com/gioblu/PJON.git#v2.0
        IRremoteESP8266=https://github.com/markszabo/IRremoteESP8266/archive/master.zip

    [env:nodemcuv2]
    platform = espressif8266
    framework = arduino
    board = nodemcuv2

    ; Build options
    build_flags =
        ${common_env_data.build_flags}
        -DSSID_NAME=HELLO
        -DSSID_PASWORD=WORLD

    ; Library options
    lib_deps =
        ${common_env_data.lib_deps_builtin}
        ${common_env_data.lib_deps_external}
        https://github.com/me-no-dev/ESPAsyncTCP.git
        PubSubClient@2.6
        OneWire

    ; Serial Monitor options
    monitor_speed = 115200
    monitor_options =
        --encoding
        hexlify

    ; Unit Testing options
    test_ignore = test_desktop

    [env:bluepill_f103c8]
    platform = ststm32
    framework = arduino
    board = bluepill_f103c8

    ; Build options
    build_flags = ${common_env_data.build_flags}

    ; Library options
    lib_deps =
        ${common_env_data.lib_deps_external}

    ; Debug options
    debug_tool = custom
    debug_server =
        JLinkGDBServer
        -singlerun
        -if
        SWD
        -select
        USB
        -port
        2331
        -device
        STM32F103C8

    ; Unit Testing options
    test_ignore = test_desktop
