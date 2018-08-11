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

.. _platform_nordicnrf51:

Nordic nRF51
============

:Configuration:
  :ref:`projectconf_env_platform` = ``nordicnrf51``

The Nordic nRF51 Series is a family of highly flexible, multi-protocol, system-on-chip (SoC) devices for ultra-low power wireless applications. nRF51 Series devices support a range of protocol stacks including Bluetooth Smart (previously called Bluetooth low energy), ANT and proprietary 2.4GHz protocols such as Gazell.

For more detailed information please visit `vendor site <https://www.nordicsemi.com/eng/Products/nRF51-Series-SoC?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Nordic nRF51 development platform repository <https://github.com/platformio/platform-nordicnrf51/tree/master/examples?utm_source=platformio&utm_medium=docs>`_:

* `arduino-ble-led <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/arduino-ble-led?utm_source=platformio&utm_medium=docs>`_
* `arduino-blink <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/arduino-blink?utm_source=platformio&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/arduino-internal-libs?utm_source=platformio&utm_medium=docs>`_
* `mbed-ble-thermometer <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/mbed-ble-thermometer?utm_source=platformio&utm_medium=docs>`_
* `mbed-blink <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/mbed-blink?utm_source=platformio&utm_medium=docs>`_
* `mbed-events <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/mbed-events?utm_source=platformio&utm_medium=docs>`_
* `mbed-microbit-hello-world <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/mbed-microbit-hello-world?utm_source=platformio&utm_medium=docs>`_
* `mbed-serial <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/mbed-serial?utm_source=platformio&utm_medium=docs>`_

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. contents::
    :local:


Tools & Debug Probes
~~~~~~~~~~~~~~~~~~~~

Supported debugging tools are listed in "Debug" column. For more detailed
information, please scroll table by horizontal.
You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` options.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further instructions.


On-Board Debug Tools
^^^^^^^^^^^^^^^^^^^^

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
    * - ``bbcmicrobit``
      - `BBC micro:bit <https://developer.mbed.org/platforms/Microbit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``bbcmicrobit_b``
      - `BBC micro:bit B(S130) <https://developer.mbed.org/platforms/Microbit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``delta_dfcm_nnn50``
      - `Delta DFCM-NNN50 <https://os.mbed.com/platforms/Delta-DFCM-NNN50/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 32MHz
      - 256KB
      - 16KB
    * - ``dfcm_nnn40``
      - `Delta DFCM-NNN40 <https://developer.mbed.org/platforms/Delta-DFCM-NNN40/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``hrm1017``
      - `Switch Science mbed HRM1017 <https://developer.mbed.org/platforms/mbed-HRM1017/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``nrf51822_y5_mbug``
      - `y5 nRF51822 mbug <https://developer.mbed.org/platforms/Y5-NRF51822-MBUG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``nrf51_dk``
      - `Nordic nRF51-DK <https://developer.mbed.org/platforms/Nordic-nRF51-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``nrf51_dongle``
      - `Nordic nRF51-Dongle <https://developer.mbed.org/platforms/Nordic-nRF51-Dongle/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink` (on-board)
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``nrf51_mkit``
      - `Nordic nRF51822-mKIT <http://developer.mbed.org/platforms/Nordic-nRF51822/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB
    * - ``redBearLab``
      - `RedBearLab nRF51822 <https://developer.mbed.org/platforms/RedBearLab-nRF51822/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``redBearLabBLENano``
      - `RedBearLab BLE Nano 1.5 <https://developer.mbed.org/platforms/RedBearLab-BLE-Nano/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB
    * - ``seeedArchBLE``
      - `Seeed Arch BLE <https://developer.mbed.org/platforms/Seeed-Arch-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB
    * - ``seeedArchLink``
      - `Seeed Arch Link <https://developer.mbed.org/platforms/Seeed-Arch-Link/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``seeedTinyBLE``
      - `Seeed Tiny BLE <http://developer.mbed.org/platforms/Seeed-Tiny-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``ty51822r3``
      - `Switch Science mbed TY51822r3 <https://developer.mbed.org/platforms/Switch-Science-mbed-TY51822r3/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``vbluno51``
      - `VNG VBLUNO51 <https://os.mbed.com/platforms/VBLUNO51/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 16MHz
      - 128KB
      - 32KB
    * - ``wallbot_ble``
      - `JKSoft Wallbot BLE <https://developer.mbed.org/platforms/JKSoft-Wallbot-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB


External Debug Tools
^^^^^^^^^^^^^^^^^^^^

Boards listed below are compatible with :ref:`piodebug` but **DEPEND ON**
external debug tool. See "Debug" column for compatible debug tools.


.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``Sinobit``
      - `Sino:Bit <https://github.com/sinobitorg/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``bluz_dk``
      - `BluzDK <https://bluz.io/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``ng_beacon``
      - `ng-beacon <https://github.com/urish/ng-beacon?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``oshchip``
      - `OSHChip <http://oshchip.org/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``rfduino``
      - `RFduino <http://www.rfduino.com/product/rfd22102-rfduino-dip/index.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 128KB
      - 8KB
    * - ``waveshare_ble400``
      - `Waveshare BLE400 <http://www.waveshare.com/wiki/BLE400?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-nordicnrf51/releases>`__
of Nordic nRF51 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = nordicnrf51
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = nordicnrf51@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-nordicnrf51.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinonordicnrf5 <https://github.com/sandeepmistry/arduino-nRF5?utm_source=platformio&utm_medium=docs>`__
      - Arduino Wiring-based Framework (Nordic NRF5 Core)

    * - `framework-mbed <http://mbed.org?utm_source=platformio&utm_medium=docs>`__
      - mbed Framework

    * - `tool-jlink <https://www.segger.com/downloads/jlink/?utm_source=platformio&utm_medium=docs>`__
      - SEGGER J-Link Software and Documentation Pack

    * - `tool-nrfjprog <https://www.nordicsemi.com?utm_source=platformio&utm_medium=docs>`__
      - nRF5x command line tool

    * - `tool-openocd <http://openocd.org?utm_source=platformio&utm_medium=docs>`__
      - OpenOCD

    * - `tool-sreccat <https://github.com/marcows/SRecord?utm_source=platformio&utm_medium=docs>`__
      - Merging tool

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

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_mbed`
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

BBC
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
    * - ``bbcmicrobit``
      - `BBC micro:bit <https://developer.mbed.org/platforms/Microbit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``bbcmicrobit_b``
      - `BBC micro:bit B(S130) <https://developer.mbed.org/platforms/Microbit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

BluzDK
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
    * - ``bluz_dk``
      - `BluzDK <https://bluz.io/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

Delta
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
    * - ``delta_dfcm_nnn50``
      - `Delta DFCM-NNN50 <https://os.mbed.com/platforms/Delta-DFCM-NNN50/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 16KB
    * - ``dfcm_nnn40``
      - `Delta DFCM-NNN40 <https://developer.mbed.org/platforms/Delta-DFCM-NNN40/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

JKSoft
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
    * - ``wallbot_ble``
      - `JKSoft Wallbot BLE <https://developer.mbed.org/platforms/JKSoft-Wallbot-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB

Nordic
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
    * - ``nrf51_dk``
      - `Nordic nRF51-DK <https://developer.mbed.org/platforms/Nordic-nRF51-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``nrf51_dongle``
      - `Nordic nRF51-Dongle <https://developer.mbed.org/platforms/Nordic-nRF51-Dongle/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``nrf51_mkit``
      - `Nordic nRF51822-mKIT <http://developer.mbed.org/platforms/Nordic-nRF51822/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB

OSHChip
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
    * - ``oshchip``
      - `OSHChip <http://oshchip.org/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

RFduino
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
    * - ``rfduino``
      - `RFduino <http://www.rfduino.com/product/rfd22102-rfduino-dip/index.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 128KB
      - 8KB

RedBearLab
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``redBearLab``
      - `RedBearLab nRF51822 <https://developer.mbed.org/platforms/RedBearLab-nRF51822/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``redBearLabBLENano``
      - `RedBearLab BLE Nano 1.5 <https://developer.mbed.org/platforms/RedBearLab-BLE-Nano/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB

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
    * - ``seeedArchBLE``
      - `Seeed Arch BLE <https://developer.mbed.org/platforms/Seeed-Arch-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB
    * - ``seeedArchLink``
      - `Seeed Arch Link <https://developer.mbed.org/platforms/Seeed-Arch-Link/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``seeedTinyBLE``
      - `Seeed Tiny BLE <http://developer.mbed.org/platforms/Seeed-Tiny-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

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
    * - ``hrm1017``
      - `Switch Science mbed HRM1017 <https://developer.mbed.org/platforms/mbed-HRM1017/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``ty51822r3``
      - `Switch Science mbed TY51822r3 <https://developer.mbed.org/platforms/Switch-Science-mbed-TY51822r3/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

VNG
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
    * - ``vbluno51``
      - `VNG VBLUNO51 <https://os.mbed.com/platforms/VBLUNO51/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 128KB
      - 32KB

Waveshare
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
    * - ``waveshare_ble400``
      - `Waveshare BLE400 <http://www.waveshare.com/wiki/BLE400?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

ng-beacon
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
    * - ``ng_beacon``
      - `ng-beacon <https://github.com/urish/ng-beacon?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

sino:bit
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``Sinobit``
      - `Sino:Bit <https://github.com/sinobitorg/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

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
    * - ``nrf51822_y5_mbug``
      - `y5 nRF51822 mbug <https://developer.mbed.org/platforms/Y5-NRF51822-MBUG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
