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

.. _platform_nxplpc:

NXP LPC
=======
:ref:`projectconf_env_platform` = ``nxplpc``

The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

For more detailed information please visit `vendor site <http://www.nxp.com/products/microcontrollers/?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are located in `NXP LPC development platform repository <https://github.com/platformio/platform-nxplpc/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_.


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
    * - ``elektor_cocorico``
      - `CoCo-ri-Co! <https://developer.mbed.org/platforms/CoCo-ri-Co/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - LPC812
      - 30 MHz
      - 16K
      - 4K
    * - ``lpc1114fn28``
      - `Switch Science mbed LPC1114FN28 <https://developer.mbed.org/platforms/LPC1114FN28/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - LPC1114FN28
      - 48 MHz
      - 32K
      - 4K
    * - ``lpc11u24``
      - `NXP mbed LPC11U24 <https://developer.mbed.org/platforms/mbed-LPC11U24/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - LPC11U24
      - 48 MHz
      - 32K
      - 8K
    * - ``lpc11u24_301``
      - `ARM mbed LPC11U24 (+CAN) <https://developer.mbed.org/handbook/mbed-NXP-LPC11U24?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - LPC11U24
      - 48 MHz
      - 32K
      - 8K
    * - ``lpc11u68``
      - `LPCXpresso11U68 <https://developer.mbed.org/platforms/LPCXpresso11U68/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - LPC11U68
      - 50 MHz
      - 256K
      - 36K
    * - ``lpc1768``
      - `NXP mbed LPC1768 <http://developer.mbed.org/platforms/mbed-LPC1768/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - LPC1768
      - 96 MHz
      - 512K
      - 64K
    * - ``lpc4088``
      - `Embedded Artists LPC4088 QuickStart Board <https://developer.mbed.org/platforms/EA-LPC4088/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - LPC4088
      - 120 MHz
      - 512K
      - 96K
    * - ``lpc4088_dm``
      - `Embedded Artists LPC4088 Display Module <https://developer.mbed.org/platforms/EA-LPC4088-Display-Module/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - LPC4088
      - 120 MHz
      - 512K
      - 96K
    * - ``lpc4330_m4``
      - `Bambino-210E <https://developer.mbed.org/platforms/Micromint-Bambino-210E/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - LPC4330
      - 204 MHz
      - 8M
      - 264K
    * - ``lpc812``
      - `NXP LPC800-MAX <https://developer.mbed.org/platforms/NXP-LPC800-MAX/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - LPC812
      - 30 MHz
      - 16K
      - 4K
    * - ``lpc824``
      - `LPCXpresso824-MAX <https://developer.mbed.org/platforms/LPCXpresso824-MAX/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - LPC824
      - 30 MHz
      - 32K
      - 8K
    * - ``seeedArchPro``
      - `Seeed Arch Pro <https://developer.mbed.org/platforms/Seeeduino-Arch-Pro/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - LPC1768
      - 96 MHz
      - 512K
      - 64K
    * - ``ssci824``
      - `Switch Science mbed LPC824 <https://developer.mbed.org/platforms/Switch-Science-mbed-LPC824/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - LPC824
      - 30 MHz
      - 32K
      - 8K
    * - ``ubloxc027``
      - `u-blox C027 <https://developer.mbed.org/platforms/u-blox-C027/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - LPC1768
      - 96 MHz
      - 512K
      - 64K


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
    * - ``blueboard_lpc11u24``
      - `NGX Technologies BlueBoard-LPC11U24 <https://developer.mbed.org/platforms/BlueBoard-LPC11U24/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U24
      - 48 MHz
      - 32K
      - 8K
    * - ``dipcortexm0``
      - `Solder Splash Labs DipCortex M0 <https://developer.mbed.org/platforms/DipCortex-M0/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U24
      - 50 MHz
      - 32K
      - 8K
    * - ``lpc11c24``
      - `NXP LPC11C24 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-m0-cores:LPC11C24FBD48?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11C24
      - 48 MHz
      - 32K
      - 8K
    * - ``lpc11u34_421``
      - `NXP LPC11U34 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/40kb-flash-8kb-sram-lqfp48-package:LPC11U34FBD48?lang_cd=en&utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U34
      - 48 MHz
      - 40K
      - 8K
    * - ``lpc11u35``
      - `EA LPC11U35 QuickStart Board <https://developer.mbed.org/platforms/EA-LPC11U35/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U35
      - 48 MHz
      - 64K
      - 10K
    * - ``lpc11u35_501``
      - `CQ Publishing TG-LPC11U35-501 <https://developer.mbed.org/platforms/TG-LPC11U35-501/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U35
      - 48 MHz
      - 64K
      - 10K
    * - ``lpc11u35_y5_mbug``
      - `y5 LPC11U35 mbug <https://developer.mbed.org/platforms/Y5-LPC11U35-MBUG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U35
      - 48 MHz
      - 64K
      - 10K
    * - ``lpc11u37_501``
      - `NXP LPC11U37 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/128kb-flash-10kb-sram-lqfp48-package:LPC11U37FBD48?lang_cd=en&utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U37
      - 48 MHz
      - 128K
      - 10K
    * - ``lpc1347``
      - `DipCortex M3 <https://developer.mbed.org/platforms/DipCortex-M3/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_jlink`
      - LPC1347
      - 72 MHz
      - 64K
      - 12K
    * - ``lpc1549``
      - `NXP LPCXpresso1549 <https://developer.mbed.org/platforms/LPCXpresso1549/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC1549
      - 72 MHz
      - 256K
      - 36K
    * - ``lpc2460``
      - `NXP LPC2460 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-arm7-arm9-mcus/lpc-arm7-mcus/lpc2100-200-300-400/flashless-16-bit-32-bit-microcontroller-ethernet-can-isp-iap-usb-2.0-device-host-otg-external-memory-interface:LPC2460FBD208?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_jlink`
      - LPC2460
      - 72 MHz
      - 64K
      - 16K
    * - ``lpc4337``
      - `LPCXpresso4337 <https://developer.mbed.org/platforms/LPCXpresso4337/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC4337
      - 204 MHz
      - 1M
      - 136K


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

    * - :ref:`framework_mbed`
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

AppNearMe
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``micronfcboard``
      - `MicroNFCBoard <https://os.mbed.com/platforms/MicroNFCBoard/?utm_source=platformio&utm_medium=docs>`_
      - No
      - LPC11U34
      - 48 MHz
      - 48K
      - 10K

CQ Publishing
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lpc11u35_501``
      - `CQ Publishing TG-LPC11U35-501 <https://developer.mbed.org/platforms/TG-LPC11U35-501/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC11U35
      - 48 MHz
      - 64K
      - 10K

Elektor Labs
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
    * - ``elektor_cocorico``
      - `CoCo-ri-Co! <https://developer.mbed.org/platforms/CoCo-ri-Co/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC812
      - 30 MHz
      - 16K
      - 4K

Embedded Artists
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lpc11u35``
      - `EA LPC11U35 QuickStart Board <https://developer.mbed.org/platforms/EA-LPC11U35/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC11U35
      - 48 MHz
      - 64K
      - 10K
    * - ``lpc4088``
      - `Embedded Artists LPC4088 QuickStart Board <https://developer.mbed.org/platforms/EA-LPC4088/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC4088
      - 120 MHz
      - 512K
      - 96K
    * - ``lpc4088_dm``
      - `Embedded Artists LPC4088 Display Module <https://developer.mbed.org/platforms/EA-LPC4088-Display-Module/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC4088
      - 120 MHz
      - 512K
      - 96K

GHI Electronics
~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``oc_mbuino``
      - `mBuino <https://developer.mbed.org/platforms/mBuino/?utm_source=platformio&utm_medium=docs>`_
      - No
      - LPC11U24
      - 50 MHz
      - 32K
      - 10K

Micromint
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lpc4330_m4``
      - `Bambino-210E <https://developer.mbed.org/platforms/Micromint-Bambino-210E/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC4330
      - 204 MHz
      - 8M
      - 264K
    * - ``lpc4337``
      - `LPCXpresso4337 <https://developer.mbed.org/platforms/LPCXpresso4337/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC4337
      - 204 MHz
      - 1M
      - 136K

NGX Technologies
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``blueboard_lpc11u24``
      - `NGX Technologies BlueBoard-LPC11U24 <https://developer.mbed.org/platforms/BlueBoard-LPC11U24/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC11U24
      - 48 MHz
      - 32K
      - 8K

NXP
~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lpc11c24``
      - `NXP LPC11C24 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-m0-cores:LPC11C24FBD48?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC11C24
      - 48 MHz
      - 32K
      - 8K
    * - ``lpc11u24``
      - `NXP mbed LPC11U24 <https://developer.mbed.org/platforms/mbed-LPC11U24/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC11U24
      - 48 MHz
      - 32K
      - 8K
    * - ``lpc11u24_301``
      - `ARM mbed LPC11U24 (+CAN) <https://developer.mbed.org/handbook/mbed-NXP-LPC11U24?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC11U24
      - 48 MHz
      - 32K
      - 8K
    * - ``lpc11u34_421``
      - `NXP LPC11U34 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/40kb-flash-8kb-sram-lqfp48-package:LPC11U34FBD48?lang_cd=en&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC11U34
      - 48 MHz
      - 40K
      - 8K
    * - ``lpc11u37_501``
      - `NXP LPC11U37 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/128kb-flash-10kb-sram-lqfp48-package:LPC11U37FBD48?lang_cd=en&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC11U37
      - 48 MHz
      - 128K
      - 10K
    * - ``lpc11u68``
      - `LPCXpresso11U68 <https://developer.mbed.org/platforms/LPCXpresso11U68/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC11U68
      - 50 MHz
      - 256K
      - 36K
    * - ``lpc1549``
      - `NXP LPCXpresso1549 <https://developer.mbed.org/platforms/LPCXpresso1549/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC1549
      - 72 MHz
      - 256K
      - 36K
    * - ``lpc1768``
      - `NXP mbed LPC1768 <http://developer.mbed.org/platforms/mbed-LPC1768/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC1768
      - 96 MHz
      - 512K
      - 64K
    * - ``lpc2368``
      - `NXP LPC2368 <https://developer.mbed.org/platforms/mbed-LPC2368/?utm_source=platformio&utm_medium=docs>`_
      - No
      - LPC2368
      - 72 MHz
      - 512K
      - 58K
    * - ``lpc2460``
      - `NXP LPC2460 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-arm7-arm9-mcus/lpc-arm7-mcus/lpc2100-200-300-400/flashless-16-bit-32-bit-microcontroller-ethernet-can-isp-iap-usb-2.0-device-host-otg-external-memory-interface:LPC2460FBD208?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC2460
      - 72 MHz
      - 64K
      - 16K
    * - ``lpc812``
      - `NXP LPC800-MAX <https://developer.mbed.org/platforms/NXP-LPC800-MAX/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC812
      - 30 MHz
      - 16K
      - 4K
    * - ``lpc824``
      - `LPCXpresso824-MAX <https://developer.mbed.org/platforms/LPCXpresso824-MAX/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC824
      - 30 MHz
      - 32K
      - 8K

Outrageous Circuits
~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``mbuino``
      - `Outrageous Circuits mBuino <https://developer.mbed.org/platforms/Outrageous-Circuits-mBuino/?utm_source=platformio&utm_medium=docs>`_
      - No
      - LPC11U24
      - 48 MHz
      - 32K
      - 8K

SeeedStudio
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``seeedArchGPRS``
      - `Seeed Arch GPRS V2 <https://www.seeedstudio.com/Arch-GPRS-V2-p-2026.html?utm_source=platformio&utm_medium=docs>`_
      - No
      - LPC11U37
      - 48 MHz
      - 128K
      - 10K
    * - ``seeedArchPro``
      - `Seeed Arch Pro <https://developer.mbed.org/platforms/Seeeduino-Arch-Pro/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC1768
      - 96 MHz
      - 512K
      - 64K
    * - ``xadow_m0``
      - `Seeed Xadow M0 <https://developer.mbed.org/platforms/Seeed-Xadow-M0/?utm_source=platformio&utm_medium=docs>`_
      - No
      - LPC11U35
      - 48 MHz
      - 64K
      - 10K

Smeshlink
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``xbed_lpc1768``
      - `Smeshlink xbed LPC1768 <https://developer.mbed.org/platforms/xbed-LPC1768/?utm_source=platformio&utm_medium=docs>`_
      - No
      - LPC1768
      - 96 MHz
      - 512K
      - 32K

Solder Splash Labs
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``dipcortexm0``
      - `Solder Splash Labs DipCortex M0 <https://developer.mbed.org/platforms/DipCortex-M0/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC11U24
      - 50 MHz
      - 32K
      - 8K
    * - ``lpc1347``
      - `DipCortex M3 <https://developer.mbed.org/platforms/DipCortex-M3/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC1347
      - 72 MHz
      - 64K
      - 12K

Switch Science
~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lpc1114fn28``
      - `Switch Science mbed LPC1114FN28 <https://developer.mbed.org/platforms/LPC1114FN28/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC1114FN28
      - 48 MHz
      - 32K
      - 4K
    * - ``ssci824``
      - `Switch Science mbed LPC824 <https://developer.mbed.org/platforms/Switch-Science-mbed-LPC824/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC824
      - 30 MHz
      - 32K
      - 8K

u-blox
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``ubloxc027``
      - `u-blox C027 <https://developer.mbed.org/platforms/u-blox-C027/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC1768
      - 96 MHz
      - 512K
      - 64K

y5 design
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lpc11u35_y5_mbug``
      - `y5 LPC11U35 mbug <https://developer.mbed.org/platforms/Y5-LPC11U35-MBUG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPC11U35
      - 48 MHz
      - 64K
      - 10K
