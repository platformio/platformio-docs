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

.. _platform_siliconlabsefm32:

Silicon Labs EFM32
==================
:ref:`projectconf_env_platform` = ``siliconlabsefm32``

Silicon Labs EFM32 Gecko 32-bit microcontroller (MCU) family includes devices that offer flash memory configurations up to 256 kB, 32 kB of RAM and CPU speeds up to 48 MHz. Based on the powerful ARM Cortex-M core, the Gecko family features innovative low energy techniques, short wake-up time from energy saving modes and a wide selection of peripherals, making it ideal for battery operated applications and other systems requiring high performance and low-energy consumption.

For more detailed information please visit `vendor site <http://www.silabs.com/products/mcu/32-bit/efm32-gecko/Pages/efm32-gecko.aspx?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Silicon Labs EFM32 development platform repository <https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples?utm_source=platformio&utm_medium=docs>`_:

* `mbed-blink <https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/mbed-blink?utm_source=platformio&utm_medium=docs>`_
* `mbed-dsp <https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/mbed-dsp?utm_source=platformio&utm_medium=docs>`_
* `mbed-events <https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/mbed-events?utm_source=platformio&utm_medium=docs>`_
* `mbed-serial <https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/mbed-serial?utm_source=platformio&utm_medium=docs>`_

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

Supported debugging tools are listed in "Debug" column. For more detailed
information, please scroll table by horizontal.
You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` options.


On-Board Debug Tools
~~~~~~~~~~~~~~~~~~~~~

Boards listed below have on-board debug tool and **ARE READY** for debugging!
You do not need to use/buy external debug tool.


.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``efm32gg_stk3700``
      - `Silicon Labs EFM32GG-STK3700 (Giant Gecko) <https://developer.mbed.org/platforms/EFM32-Giant-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32GG990F1024
      - 48MHz
      - 1MB
      - 128KB
    * - ``efm32hg_stk3400``
      - `Silicon Labs SLSTK3400A USB-enabled (Happy Gecko) <https://developer.mbed.org/platforms/EFM32-Happy-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32HG322F64
      - 24MHz
      - 64KB
      - 8KB
    * - ``efm32lg_stk3600``
      - `Silicon Labs EFM32LG-STK3600 (Leopard Gecko) <https://developer.mbed.org/platforms/EFM32-Leopard-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32LG990F256
      - 48MHz
      - 256KB
      - 32KB
    * - ``efm32pg_stk3401``
      - `Silicon Labs SLSTK3401A (Pearl Gecko) <https://developer.mbed.org/platforms/EFM32-Pearl-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32PG1B200F256
      - 40MHz
      - 256KB
      - 32KB
    * - ``efm32wg_stk3800``
      - `Silicon Labs EFM32WG-STK3800 (Wonder Gecko) <https://developer.mbed.org/platforms/EFM32-Wonder-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32WG990F256
      - 48MHz
      - 256KB
      - 32KB
    * - ``efm32zg_stk3200``
      - `Silicon Labs EFM32ZG-STK3200 (Zero Gecko) <https://developer.mbed.org/platforms/EFM32-Zero-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32ZG222F32
      - 24MHz
      - 32KB
      - 4KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-siliconlabsefm32/releases>`__
of Silicon Labs EFM32 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = siliconlabsefm32
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = siliconlabsefm32@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-siliconlabsefm32.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-mbed <http://mbed.org?utm_source=platformio&utm_medium=docs>`__
      - mbed Framework

    * - `tool-openocd <http://openocd.org?utm_source=platformio&utm_medium=docs>`__
      - OpenOCD

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

Silicon Labs
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``efm32gg_stk3700``
      - `Silicon Labs EFM32GG-STK3700 (Giant Gecko) <https://developer.mbed.org/platforms/EFM32-Giant-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - EFM32GG990F1024
      - 48MHz
      - 1MB
      - 128KB
    * - ``efm32hg_stk3400``
      - `Silicon Labs SLSTK3400A USB-enabled (Happy Gecko) <https://developer.mbed.org/platforms/EFM32-Happy-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - EFM32HG322F64
      - 24MHz
      - 64KB
      - 8KB
    * - ``efm32lg_stk3600``
      - `Silicon Labs EFM32LG-STK3600 (Leopard Gecko) <https://developer.mbed.org/platforms/EFM32-Leopard-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - EFM32LG990F256
      - 48MHz
      - 256KB
      - 32KB
    * - ``efm32pg_stk3401``
      - `Silicon Labs SLSTK3401A (Pearl Gecko) <https://developer.mbed.org/platforms/EFM32-Pearl-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - EFM32PG1B200F256
      - 40MHz
      - 256KB
      - 32KB
    * - ``efm32wg_stk3800``
      - `Silicon Labs EFM32WG-STK3800 (Wonder Gecko) <https://developer.mbed.org/platforms/EFM32-Wonder-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - EFM32WG990F256
      - 48MHz
      - 256KB
      - 32KB
    * - ``efm32zg_stk3200``
      - `Silicon Labs EFM32ZG-STK3200 (Zero Gecko) <https://developer.mbed.org/platforms/EFM32-Zero-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - EFM32ZG222F32
      - 24MHz
      - 32KB
      - 4KB
