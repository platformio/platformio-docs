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

.. _platform_samsung_artik:

Samsung ARTIK
=============
:ref:`projectconf_env_platform` = ``samsung_artik``

The Samsung ARTIK Smart IoT platform brings hardware modules and cloud services together, with built-in security and an ecosystem of tools and partners to speed up your time-to-market.

For more detailed information please visit `vendor site <http://platformio.org/platforms/samsung_artik?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: samsung_artik_extra.rst

Examples
--------

Examples are listed from `Samsung ARTIK development platform repository <https://github.com/platformio/platform-samsung_artik/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_:

* `artik_sdk <https://github.com/platformio/platform-samsung_artik/tree/develop/examples/artik_sdk?utm_source=platformio&utm_medium=docs>`_
* `blink_led_wifi <https://github.com/platformio/platform-samsung_artik/tree/develop/examples/blink_led_wifi?utm_source=platformio&utm_medium=docs>`_
* `hello <https://github.com/platformio/platform-samsung_artik/tree/develop/examples/hello?utm_source=platformio&utm_medium=docs>`_

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

Supported debugging tools are listed in "Debug" column. For more detailed
information, please scroll table by horizontal.
You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` options.


External tools
~~~~~~~~~~~~~~

Boards listed below are compatible with :ref:`piodebug` but depend on external
debugging tools. See "Debug" column for compatible debugging tools.


.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``artik_053``
      - `Samsung ARTIK053 <http://www.artik.io?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_custom` (default)
      - S5JT200
      - 320MHz
      - 8MB
      - 1.25MB


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-tizenrt <http://www.artik.io?utm_source=platformio&utm_medium=docs>`__
      - TizenRT RTOS with library

    * - `tool-artik-openocd <http://openocd.org?utm_source=platformio&utm_medium=docs>`__
      - OpenOCD for ARTIK

    * - `toolchain-gccarmnoneeabi <https://launchpad.net/gcc-arm-embedded?utm_source=platformio&utm_medium=docs>`__
      - gcc-arm-embedded

.. warning::
    **Linux Users**:

        * Install "udev" rules file `99-platformio-udev.rules <https://github.com/platformio/platformio-core/blob/develop/scripts/99-platformio-udev.rules>`_
          (an instruction is located inside a file).
        * Raspberry Pi users, please read this article
          `Enable serial port on Raspberry Pi <https://hallard.me/enable-serial-port-on-raspberry-pi/>`__.


    **Windows Users:**

        Please check that you have a correctly installed USB driver from board
        manufacturer


Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_tizenrt`
      - Tizen RT is a lightweight RTOS-based platform to support low-end IoT devices

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

Samsung
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``artik_053``
      - `Samsung ARTIK053 <http://www.artik.io?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - S5JT200
      - 320MHz
      - 8MB
      - 1.25MB
