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

.. _projectconf_pio_extra_configs:

``extra_configs``
^^^^^^^^^^^^^^^^^

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

    ; Global data for all [env:***]
    [env]
    platform = platformio/espressif32
    framework = espidf

    ; Custom data group
    ; can be use in [env:***] via ${common.***}
    [common]
    debug_flags = -D RELEASE
    lib_flags = -lc -lm

    [env:esp-wrover-kit]
    board = esp-wrover-kit
    build_flags = ${common.debug_flags}


*"extra_envs.ini"*

.. code-block:: ini

    [env:esp32dev]
    board = esp32dev
    build_flags = ${common.lib_flags} ${common.debug_flags}

    [env:lolin32]
    platform = platformio/espressif32
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
    platform = platformio/espressif32
    framework = espidf
    board = esp-wrover-kit
    build_flags = ${common.debug_flags}

    [env:esp32dev]
    platform = platformio/espressif32
    framework = espidf
    board = esp32dev
    build_flags = ${common.lib_flags} ${common.debug_flags}

    [env:lolin32]
    platform = platformio/espressif32
    framework = espidf
    board = lolin32
    build_flags = -Og
