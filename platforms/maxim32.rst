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

.. _platform_maxim32:

Maxim 32
========
:ref:`projectconf_env_platform` = ``maxim32``

Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

For more detailed information please visit `vendor site <https://www.maximintegrated.com/en/products/digital/microcontrollers.html?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Maxim 32 development platform repository <https://github.com/platformio/platform-maxim32/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_:

* `mbed-blink <https://github.com/platformio/platform-maxim32/tree/develop/examples/mbed-blink?utm_source=platformio&utm_medium=docs>`_
* `mbed-dsp <https://github.com/platformio/platform-maxim32/tree/develop/examples/mbed-dsp?utm_source=platformio&utm_medium=docs>`_
* `mbed-events <https://github.com/platformio/platform-maxim32/tree/develop/examples/mbed-events?utm_source=platformio&utm_medium=docs>`_
* `mbed-rtos <https://github.com/platformio/platform-maxim32/tree/develop/examples/mbed-rtos?utm_source=platformio&utm_medium=docs>`_
* `mbed-serial <https://github.com/platformio/platform-maxim32/tree/develop/examples/mbed-serial?utm_source=platformio&utm_medium=docs>`_

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

Supported debugging tools are listed in "Debug" column. For more detailed
information, please scroll table by horizontal.
You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` options.


On-Board tools
~~~~~~~~~~~~~~

Boards listed below have on-board debugging tools and **ARE READY** for debugging!
You do not need to use/buy external debugger.


.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``max32600mbed``
      - `Maxim ARM mbed Enabled Development Platform for MAX32600 <https://developer.mbed.org/platforms/MAX32600mbed/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - MAX32600
      - 24MHz
      - 256KB
      - 32KB


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
    * - ``maxwsnenv``
      - `Maxim Wireless Sensor Node Demonstrator <https://developer.mbed.org/platforms/MAXWSNENV/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap`
      - MAX32610
      - 24MHz
      - 256KB
      - 32KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-maxim32/releases>`__
of Maxim 32 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option as described below:

.. code-block:: ini

    ; Custom stable version
    [env:stable]
    platform =maxim32@x.y.z
    board = ...
    ...

    ; The latest upstream/development version
    [env:upstream]
    platform = https://github.com/platformio/platform-maxim32.git
    board = ...
    ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-mbed <http://mbed.org?utm_source=platformio&utm_medium=docs>`__
      - mbed Framework

    * - `tool-pyocd <https://github.com/mbedmicro/pyOCD?utm_source=platformio&utm_medium=docs>`__
      - Open source python library for programming and debugging ARM Cortex-M microcontrollers using CMSIS-DAP

    * - `toolchain-gccarmnoneeabi <https://launchpad.net/gcc-arm-embedded?utm_source=platformio&utm_medium=docs>`__
      - gcc-arm-embedded

.. warning::
    **Linux Users**:

        * Install "udev" rules :ref:`faq_udev_rules`
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

    * - :ref:`framework_mbed`
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

Maxim
~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``max32600mbed``
      - `Maxim ARM mbed Enabled Development Platform for MAX32600 <https://developer.mbed.org/platforms/MAX32600mbed/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - MAX32600
      - 24MHz
      - 256KB
      - 32KB
    * - ``max32620hsp``
      - `Maxim Health Sensor Platform <https://developer.mbed.org/platforms/MAX32620HSP/?utm_source=platformio&utm_medium=docs>`_
      - No
      - MAX32620
      - 96MHz
      - 2MB
      - 256KB
    * - ``max32625mbed``
      - `MAX32625MBED <https://os.mbed.com/platforms/MAX32625MBED/?utm_source=platformio&utm_medium=docs>`_
      - No
      - MAX32625
      - 96MHz
      - 512KB
      - 160KB
    * - ``max32625nexpaq``
      - `MAX32625NEXPAQ <https://os.mbed.com/platforms/max32625nexpaq/?utm_source=platformio&utm_medium=docs>`_
      - No
      - MAX32625
      - 96MHz
      - 512KB
      - 160KB
    * - ``max32630fthr``
      - `Maxim MAX32630FTHR Application Platform <https://developer.mbed.org/platforms/MAX32630FTHR/?utm_source=platformio&utm_medium=docs>`_
      - No
      - MAX32630
      - 96MHz
      - 2MB
      - 512KB
    * - ``maxwsnenv``
      - `Maxim Wireless Sensor Node Demonstrator <https://developer.mbed.org/platforms/MAXWSNENV/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - MAX32610
      - 24MHz
      - 256KB
      - 32KB
