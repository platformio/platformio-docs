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

``platformio.ini`` is a configuration file that lets you set up your development
environment, share your code and configurations with others, and leverage a
declarative approach to development. You can use ``platformio.ini`` to
configure multiple platforms and architectures without having to worry
about different toolchains or build systems for each one.

Each PlatformIO project has its own ``platformio.ini`` that
is located in the root directory of the project. This is an
`INI-style <http://en.wikipedia.org/wiki/INI_file>`_ file.
``platformio.ini`` has sections (each denoted by a ``[header]``) and
key/value pairs within the sections. Lines beginning with ``;``
are ignored and may be used to provide comments.

Multiple value options can be specified in two ways:

1. Split values with ", " (comma + space)
2. Multi-line format, where each new line starts with at least two spaces.

Here are the allowed sections and their allowed contents:

.. toctree::
    :maxdepth: 2

    sections/platformio/index
    sections/env/index
    interpolation
    examples

**Example**

For more examples, see :ref:`official project examples and community projects <tutorials>`.

.. code-block:: ini

    [platformio]
    default_envs = nodemcuv2

    ; custom common options
    [common]
    build_flags =
        -D VERSION=1.2.3
        -D DEBUG=1
    lib_deps_builtin =
        SPI
        Wire
    lib_deps_external =
        bblanchon/ArduinoJson @ ~5.6,!=5.4
        https://github.com/gioblu/PJON.git#v2.0
        IRremoteESP8266=https://github.com/markszabo/IRremoteESP8266/archive/master.zip

    [env:nodemcuv2]
    platform = espressif8266
    framework = arduino
    board = nodemcuv2

    ; Build options
    build_flags =
        ${common.build_flags}
        -DSSID_NAME=HELLO
        -DSSID_PASWORD=WORLD

    ; Library options
    lib_deps =
        ${common.lib_deps_builtin}
        ${common.lib_deps_external}
        https://github.com/me-no-dev/ESPAsyncTCP.git
        knolleary/PubSubClient@^2.8
        paulstoffregen/OneWire

    ; Serial Monitor options
    monitor_speed = 115200
    monitor_flags =
        --encoding
        hexlify

    ; Unit Testing options
    test_ignore = test_desktop

    [env:bluepill_f103c8]
    platform = ststm32
    framework = arduino
    board = bluepill_f103c8

    ; Library options
    lib_deps = ${common.lib_deps_external}

    ; Debug options
    debug_tool = custom
    debug_server =
        ${platformio.packages_dir}/tool-jlink/JLinkGDBServer
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
