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

.. _framework_arduino:

Arduino
=======
:ref:`projectconf_env_framework` = ``arduino``

Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

For more detailed information please visit `vendor site <http://arduino.cc/en/Reference/HomePage?utm_source=platformio&utm_medium=docs>`_.


.. contents:: Contents
    :local:
    :depth: 1
.. include:: arduino_extra.rst

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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``bbcmicrobit``
      - `BBC micro:bit <https://developer.mbed.org/platforms/Microbit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 16 MHz
      - 256K
      - 16K
    * - ``delta_dfbm_nq620``
      - `Delta DFBM-NQ620 <https://developer.mbed.org/platforms/Delta-DFBM-NQ620/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_cmsis-dap` (default, on-board), :ref:`debugging_tool_stlink`
      - NRF52832
      - 64 MHz
      - 512K
      - 64K
    * - ``mxchip_az3166``
      - `Microsoft Azure IoT Development Kit (MXChip AZ3166) <https://microsoft.github.io/azure-iot-developer-kit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F412ZGT6
      - 100 MHz
      - 1M
      - 256K
    * - ``mzeropro``
      - `Arduino M0 Pro (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardM0PRO?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``nrf51_dk``
      - `Nordic nRF51-DK <https://developer.mbed.org/platforms/Nordic-nRF51-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_stlink`
      - NRF51822
      - 32 MHz
      - 256K
      - 32K
    * - ``nrf51_dongle``
      - `Nordic nRF51-Dongle <https://developer.mbed.org/platforms/Nordic-nRF51-Dongle/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink` (on-board)
      - NRF51822
      - 32 MHz
      - 256K
      - 32K
    * - ``nrf52840_dk``
      - `Nordic nRF52840-DK <https://os.mbed.com/platforms/Nordic-nRF52840-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink` (default, on-board), :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_stlink`
      - NRF52840
      - 64 MHz
      - 1M
      - 256K
    * - ``nrf52_dk``
      - `Nordic nRF52-DK <https://developer.mbed.org/platforms/Nordic-nRF52-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink` (default, on-board), :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_stlink`
      - NRF52832
      - 64 MHz
      - 512K
      - 64K
    * - ``nucleo_f103rb``
      - `ST Nucleo F103RB <https://developer.mbed.org/platforms/ST-Nucleo-F103RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F103RBT6
      - 72 MHz
      - 128K
      - 20K
    * - ``redBearLab``
      - `RedBearLab nRF51822 <https://developer.mbed.org/platforms/RedBearLab-nRF51822/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_stlink`
      - NRF51822
      - 16 MHz
      - 256K
      - 16K
    * - ``redBearLabBLENano``
      - `RedBearLab BLE Nano 1.5 <https://developer.mbed.org/platforms/RedBearLab-BLE-Nano/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_stlink`
      - NRF51822
      - 16 MHz
      - 256K
      - 32K
    * - ``redbear_blend2``
      - `RedBearLab Blend 2 <https://redbear.cc/product/ble/blend-2.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_cmsis-dap` (default, on-board), :ref:`debugging_tool_stlink`
      - NRF52832
      - 64 MHz
      - 512K
      - 64K
    * - ``seeedTinyBLE``
      - `Seeed Tiny BLE <http://developer.mbed.org/platforms/Seeed-Tiny-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_stlink`
      - NRF51822
      - 16 MHz
      - 256K
      - 16K
    * - ``ublox_evk_nina_b1``
      - `u-blox EVK-NINA-B1 <https://os.mbed.com/platforms/u-blox-EVK-NINA-B1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_stlink`
      - NRF52832
      - 64 MHz
      - 512K
      - 64K
    * - ``zero``
      - `Arduino Zero (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K


External tools
~~~~~~~~~~~~~~

Boards listed below are compatible with :ref:`piodebug` but depend on external
debugging tools. See "Debug" column for compatible debugging tools.


.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``adafruit_circuitplayground_m0``
      - `Adafruit Circuit Playground Express <https://www.adafruit.com/product/3000?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``adafruit_feather_m0``
      - `Adafruit Feather M0 <https://www.adafruit.com/product/2772?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``adafruit_metro_m0``
      - `Adafruit Metro M0 Expresss <https://www.adafruit.com/product/3505?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``bluepill_f103c8``
      - `BluePill F103C8 <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103C8T6
      - 72 MHz
      - 64K
      - 20K
    * - ``bluz_dk``
      - `BluzDK <https://bluz.io/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32 MHz
      - 256K
      - 32K
    * - ``genericSTM32F103C8``
      - `STM32F103C8 (20k RAM. 64k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103C8T6
      - 72 MHz
      - 64K
      - 20K
    * - ``genericSTM32F103CB``
      - `STM32F103CB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103cb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103CBT6
      - 72 MHz
      - 128K
      - 20K
    * - ``genericSTM32F103R8``
      - `STM32F103R8 (20k RAM. 64 Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103r8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103R8T6
      - 72 MHz
      - 64K
      - 20K
    * - ``genericSTM32F103RB``
      - `STM32F103RB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103RBT6
      - 72 MHz
      - 128K
      - 20K
    * - ``genericSTM32F103RC``
      - `STM32F103RC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rc.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103RCT6
      - 72 MHz
      - 256K
      - 48K
    * - ``genericSTM32F103RE``
      - `STM32F103RE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103re.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103RET6
      - 72 MHz
      - 512K
      - 64K
    * - ``genericSTM32F103VC``
      - `STM32F103VC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103VCT6
      - 72 MHz
      - 256K
      - 48K
    * - ``genericSTM32F103VE``
      - `STM32F103VE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103VET6
      - 72 MHz
      - 512K
      - 64K
    * - ``maple``
      - `Maple <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`
      - STM32F103RBT6
      - 72 MHz
      - 108K
      - 17K
    * - ``maple_mini_b20``
      - `Maple Mini Bootloader 2.0 <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`
      - STM32F103CBT6
      - 72 MHz
      - 120K
      - 20K
    * - ``maple_mini_origin``
      - `Maple Mini Original <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`
      - STM32F103CBT6
      - 72 MHz
      - 108K
      - 17K
    * - ``mkr1000USB``
      - `Arduino MKR1000 <https://www.arduino.cc/en/Main/ArduinoMKR1000?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``mzeroUSB``
      - `Arduino M0 <https://www.arduino.cc/en/Main/ArduinoBoardM0?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``ng_beacon``
      - `ng-beacon <https://github.com/urish/ng-beacon?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32 MHz
      - 256K
      - 32K
    * - ``oshchip``
      - `OSHChip <http://oshchip.org/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32 MHz
      - 256K
      - 32K
    * - ``redbear_blenano2``
      - `RedBearLab BLE Nano 2 <https://redbear.cc/product/ble-nano-2-soldered.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_cmsis-dap` (default), :ref:`debugging_tool_stlink`
      - NRF52832
      - 64 MHz
      - 512K
      - 64K
    * - ``rfduino``
      - `RFduino <http://www.rfduino.com/product/rfd22102-rfduino-dip/index.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16 MHz
      - 128K
      - 8K
    * - ``sodaq_explorer``
      - `SODAQ ExpLoRer <http://support.sodaq.com/sodaq-one/explorer/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_jlink`
      - SAMD21J18A
      - 48 MHz
      - 256K
      - 32K
    * - ``sodaq_one``
      - `SODAQ ONE <http://support.sodaq.com/sodaq-one/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``sparkfun_samd21_dev_usb``
      - `SparkFun SAMD21 Dev Breakout <https://www.sparkfun.com/products/13672?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``sparkfun_samd21_mini_usb``
      - `SparkFun SAMD21 Mini Breakout <https://www.sparkfun.com/products/13664?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``stct_nrf52_minidev``
      - `Taida Century nRF52 mini board <http://taida-century.com/en/index.asp?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64 MHz
      - 512K
      - 64K
    * - ``teensy35``
      - `Teensy 3.5 <https://www.pjrc.com/store/teensy35.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`debugging_tool_jlink`
      - MK64FX512
      - 120 MHz
      - 512K
      - 192K
    * - ``teensy36``
      - `Teensy 3.6 <https://www.pjrc.com/store/teensy36.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`debugging_tool_jlink`
      - MK66FX1M0
      - 180 MHz
      - 1M
      - 256K
    * - ``waveshare_ble400``
      - `Waveshare BLE400 <http://www.waveshare.com/wiki/BLE400?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32 MHz
      - 256K
      - 32K


Examples
--------

* `Arduino for Atmel AVR <https://github.com/platformio/platform-atmelavr/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Atmel SAM <https://github.com/platformio/platform-atmelsam/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Espressif 32 <https://github.com/platformio/platform-espressif32/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Espressif 8266 <https://github.com/platformio/platform-espressif8266/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Intel ARC32 <https://github.com/platformio/platform-intel_arc32/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Microchip PIC32 <https://github.com/platformio/platform-microchippic32/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Nordic nRF51 <https://github.com/platformio/platform-nordicnrf51/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Nordic nRF52 <https://github.com/platformio/platform-nordicnrf52/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for ST STM32 <https://github.com/platformio/platform-ststm32/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Teensy <https://github.com/platformio/platform-teensy/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for TI MSP430 <https://github.com/platformio/platform-timsp430/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_atmelavr`
      - Atmel AVR 8- and 32-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industrys most code-efficient architecture for C and assembly programming.

    * - :ref:`platform_atmelsam`
      - Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

    * - :ref:`platform_espressif32`
      - Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

    * - :ref:`platform_espressif8266`
      - Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

    * - :ref:`platform_intel_arc32`
      - ARC embedded processors are a family of 32-bit CPUs that are widely used in SoC devices for storage, home, mobile, automotive, and Internet of Things applications.

    * - :ref:`platform_microchippic32`
      - Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

    * - :ref:`platform_nordicnrf51`
      - The Nordic nRF51 Series is a family of highly flexible, multi-protocol, system-on-chip (SoC) devices for ultra-low power wireless applications. nRF51 Series devices support a range of protocol stacks including Bluetooth Smart (previously called Bluetooth low energy), ANT and proprietary 2.4GHz protocols such as Gazell.

    * - :ref:`platform_nordicnrf52`
      - The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor and are the most capable Bluetooth Smart SoCs on the market. 

    * - :ref:`platform_ststm32`
      - The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

    * - :ref:`platform_teensy`
      - Teensy is a complete USB-based microcontroller development system, in a very small footprint, capable of implementing many types of projects. All programming is done via the USB port. No special programmer is needed, only a standard USB cable and a PC or Macintosh with a USB port.

    * - :ref:`platform_timsp430`
      - MSP430 microcontrollers (MCUs) from Texas Instruments (TI) are 16-bit, RISC-based, mixed-signal processors designed for ultra-low power. These MCUs offer the lowest power consumption and the perfect mix of integrated peripherals for thousands of applications.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by horizontal.

4D Systems
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``gen4iod``
      - `4D Systems gen4 IoD Range <http://www.4dsystems.com.au/product/gen4_IoD/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 512K
      - 80K

4DSystems
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``picadillo_35t``
      - `4DSystems PICadillo 35T <http://www.4dsystems.com.au/product/Picadillo_35T/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX795F512L
      - 80 MHz
      - 508K
      - 128K

Adafruit
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``adafruit_circuitplayground_m0``
      - `Adafruit Circuit Playground Express <https://www.adafruit.com/product/3000?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``adafruit_feather_m0``
      - `Adafruit Feather M0 <https://www.adafruit.com/product/2772?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``adafruit_feather_m0_express``
      - `Adafruit Feather M0 Express <https://www.adafruit.com/product/3403?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - No
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``adafruit_gemma_m0``
      - `Adafruit Gemma M0 <https://www.adafruit.com/product/3501?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - No
      - SAMD21E18A
      - 48 MHz
      - 256K
      - 32K
    * - ``adafruit_metro_m0``
      - `Adafruit Metro M0 Expresss <https://www.adafruit.com/product/3505?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``adafruit_trinket_m0``
      - `Adafruit Trinket M0 <https://www.adafruit.com/product/3500?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - No
      - SAMD21E18A
      - 48 MHz
      - 256K
      - 32K
    * - ``bluefruitmicro``
      - `Adafruit Bluefruit Micro <https://www.adafruit.com/products/2661?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8 MHz
      - 28K
      - 2.50K
    * - ``feather32u4``
      - `Adafruit Feather <https://learn.adafruit.com/adafruit-feather-32u4-bluefruit-le/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8 MHz
      - 28K
      - 2.50K
    * - ``featheresp32``
      - `Adafruit ESP32 Feather <https://www.adafruit.com/product/3405?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K
    * - ``flora8``
      - `Adafruit Flora <http://www.adafruit.com/product/659?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8 MHz
      - 28K
      - 2.50K
    * - ``gemma``
      - `Adafruit Gemma <http://www.adafruit.com/products/1222?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY85
      - 8 MHz
      - 8K
      - 512B
    * - ``huzzah``
      - `Adafruit HUZZAH ESP8266 <https://www.adafruit.com/products/2471?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K
    * - ``metro``
      - `Adafruit Metro <https://www.adafruit.com/products/2466?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 31.50K
      - 2K
    * - ``protrinket3``
      - `Adafruit Pro Trinket 3V/12MHz (USB) <http://www.adafruit.com/products/2010?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 12 MHz
      - 28K
      - 2K
    * - ``protrinket3ftdi``
      - `Adafruit Pro Trinket 3V/12MHz (FTDI) <http://www.adafruit.com/products/2010?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 12 MHz
      - 28K
      - 2K
    * - ``protrinket5``
      - `Adafruit Pro Trinket 5V/16MHz (USB) <http://www.adafruit.com/products/2000?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 28K
      - 2K
    * - ``protrinket5ftdi``
      - `Adafruit Pro Trinket 5V/16MHz (FTDI) <http://www.adafruit.com/products/2000?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 28K
      - 2K
    * - ``trinket3``
      - `Adafruit Trinket 3V/8MHz <http://www.adafruit.com/products/1500?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY85
      - 8 MHz
      - 8K
      - 512B
    * - ``trinket5``
      - `Adafruit Trinket 5V/16MHz <http://www.adafruit.com/products/1501?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY85
      - 16 MHz
      - 8K
      - 512B

Aiyarafun
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``node32s``
      - `Node32s <http://www.ayarafun.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

Alorium Technology
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``alorium_xlr8``
      - `Alorium XLR8 <http://www.aloriumtech.com/xlr8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 31.50K
      - 2K

Anarduino
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``miniwireless``
      - `Anarduino MiniWireless <http://www.anarduino.com/miniwireless/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 31.50K
      - 2K

April Brother
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``espea32``
      - `April Brother ESPea32 <https://blog.aprbrother.com/product/espea?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

Arduboy
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``arduboy``
      - `Arduboy <https://www.arduboy.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K
    * - ``arduboy_devkit``
      - `Arduboy DevKit <https://www.arduboy.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K

Arduino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``LilyPadUSB``
      - `Arduino LilyPad USB <http://arduino.cc/en/Main/ArduinoBoardLilyPadUSB?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8 MHz
      - 28K
      - 2.50K
    * - ``atmega328pb``
      - `Atmel ATmega328PB <http://www.atmel.com/devices/ATMEGA328PB.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328PB
      - 16 MHz
      - 31.50K
      - 2K
    * - ``atmegangatmega168``
      - `Arduino NG or older ATmega168 <http://arduino.cc/en/main/boards?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168
      - 16 MHz
      - 14K
      - 1K
    * - ``atmegangatmega8``
      - `Arduino NG or older ATmega8 <http://arduino.cc/en/main/boards?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA8
      - 16 MHz
      - 7K
      - 1K
    * - ``btatmega168``
      - `Arduino BT ATmega168 <http://arduino.cc/en/main/boards?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168
      - 16 MHz
      - 14K
      - 1K
    * - ``btatmega328``
      - `Arduino BT ATmega328 <http://arduino.cc/en/main/boards?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 28K
      - 2K
    * - ``chiwawa``
      - `Arduino Industrial 101 <https://store.arduino.cc/arduino-industrial-101?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K
    * - ``diecimilaatmega168``
      - `Arduino Duemilanove or Diecimila ATmega168 <http://arduino.cc/en/Main/ArduinoBoardDiecimila?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168
      - 16 MHz
      - 14K
      - 1K
    * - ``diecimilaatmega328``
      - `Arduino Duemilanove or Diecimila ATmega328 <http://arduino.cc/en/Main/ArduinoBoardDiecimila?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 30K
      - 2K
    * - ``due``
      - `Arduino Due (Programming Port) <https://www.arduino.cc/en/Main/ArduinoBoardDue?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - No
      - AT91SAM3X8E
      - 84 MHz
      - 512K
      - 32K
    * - ``dueUSB``
      - `Arduino Due (USB Native Port) <https://www.arduino.cc/en/Main/ArduinoBoardDue?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - No
      - AT91SAM3X8E
      - 84 MHz
      - 512K
      - 32K
    * - ``esplora``
      - `Arduino Esplora <https://www.arduino.cc/en/Main/ArduinoBoardEsplora?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K
    * - ``ethernet``
      - `Arduino Ethernet <https://www.arduino.cc/en/Main/ArduinoBoardEthernet?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 31.50K
      - 2K
    * - ``fio``
      - `Arduino Fio <http://arduino.cc/en/Main/ArduinoBoardFio?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8 MHz
      - 30K
      - 2K
    * - ``leonardo``
      - `Arduino Leonardo <https://www.arduino.cc/en/Main/ArduinoBoardLeonardo?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K
    * - ``leonardoeth``
      - `Arduino Leonardo ETH <https://www.arduino.cc/en/Main/ArduinoBoardLeonardoEth?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K
    * - ``lilypadatmega168``
      - `Arduino LilyPad ATmega168 <http://arduino.cc/en/Main/ArduinoBoardLilyPad?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168
      - 8 MHz
      - 14K
      - 1K
    * - ``lilypadatmega328``
      - `Arduino LilyPad ATmega328 <http://arduino.cc/en/Main/ArduinoBoardLilyPad?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8 MHz
      - 30K
      - 2K
    * - ``megaADK``
      - `Arduino Mega ADK <https://www.arduino.cc/en/Main/ArduinoBoardMegaADK?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA2560
      - 16 MHz
      - 248K
      - 8K
    * - ``megaatmega1280``
      - `Arduino Mega or Mega 2560 ATmega1280 <https://www.arduino.cc/en/Main/ArduinoBoardMega2560?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1280
      - 16 MHz
      - 124K
      - 8K
    * - ``megaatmega2560``
      - `Arduino Mega or Mega 2560 ATmega2560 (Mega 2560) <https://www.arduino.cc/en/Main/ArduinoBoardMega2560?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA2560
      - 16 MHz
      - 248K
      - 8K
    * - ``micro``
      - `Arduino Micro <https://www.arduino.cc/en/Main/ArduinoBoardMicro?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K
    * - ``miniatmega168``
      - `Arduino Mini ATmega168 <http://arduino.cc/en/Main/ArduinoBoardMini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168
      - 16 MHz
      - 14K
      - 1K
    * - ``miniatmega328``
      - `Arduino Mini ATmega328 <http://arduino.cc/en/Main/ArduinoBoardMini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 28K
      - 2K
    * - ``mkr1000USB``
      - `Arduino MKR1000 <https://www.arduino.cc/en/Main/ArduinoMKR1000?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``mkrfox1200``
      - `Arduino MKRFox1200 <https://www.arduino.cc/en/Main.ArduinoBoardMKRFox1200?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - No
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``mkrzero``
      - `Arduino MKRZero <https://www.arduino.cc/en/Main/ArduinoBoardMKRZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - No
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``mzeroUSB``
      - `Arduino M0 <https://www.arduino.cc/en/Main/ArduinoBoardM0?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``mzeropro``
      - `Arduino M0 Pro (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardM0PRO?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``mzeroproUSB``
      - `Arduino M0 Pro (Native USB Port) <https://www.arduino.cc/en/Main/ArduinoBoardM0PRO?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - No
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``nanoatmega168``
      - `Arduino Nano ATmega168 <https://www.arduino.cc/en/Main/ArduinoBoardNano?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168
      - 16 MHz
      - 14K
      - 1K
    * - ``nanoatmega328``
      - `Arduino Nano ATmega328 <https://www.arduino.cc/en/Main/ArduinoBoardNano?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 30K
      - 2K
    * - ``pro16MHzatmega168``
      - `Arduino Pro or Pro Mini ATmega168 (5V, 16 MHz) <http://arduino.cc/en/Main/ArduinoBoardProMini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168
      - 16 MHz
      - 14K
      - 1K
    * - ``pro16MHzatmega328``
      - `Arduino Pro or Pro Mini ATmega328 (5V, 16 MHz) <http://arduino.cc/en/Main/ArduinoBoardProMini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 30K
      - 2K
    * - ``pro8MHzatmega168``
      - `Arduino Pro or Pro Mini ATmega168 (3.3V, 8 MHz) <http://arduino.cc/en/Main/ArduinoBoardProMini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168
      - 8 MHz
      - 14K
      - 1K
    * - ``pro8MHzatmega328``
      - `Arduino Pro or Pro Mini ATmega328 (3.3V, 8 MHz) <http://arduino.cc/en/Main/ArduinoBoardProMini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8 MHz
      - 30K
      - 2K
    * - ``robotControl``
      - `Arduino Robot Control <https://www.arduino.cc/en/Main/Robot?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K
    * - ``robotMotor``
      - `Arduino Robot Motor <https://www.arduino.cc/en/Main/Robot?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K
    * - ``tian``
      - `Arduino Tian <https://www.arduino.cc/en/Main/ArduinoBoardTian?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - No
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``uno``
      - `Arduino Uno <https://www.arduino.cc/en/Main/ArduinoBoardUno?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 31.50K
      - 2K
    * - ``yun``
      - `Arduino Yun <https://www.arduino.cc/en/Main/ArduinoBoardYun?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K
    * - ``yunmini``
      - `Arduino Yun Mini <https://www.arduino.cc/en/Main/ArduinoBoardYunMini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K
    * - ``zero``
      - `Arduino Zero (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``zeroUSB``
      - `Arduino Zero (USB Native Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - No
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K

BBC
~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``bbcmicrobit``
      - `BBC micro:bit <https://developer.mbed.org/platforms/Microbit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 256K
      - 16K

BQ
~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``zumbt328``
      - `BQ ZUM BT-328 <http://www.bq.com/gb/products/zum.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 28K
      - 2K

BitWizard
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``raspduino``
      - `BitWizard Raspduino <http://www.bitwizard.nl/wiki/index.php/Raspduino?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 30K
      - 2K

BluzDK
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``bluz_dk``
      - `BluzDK <https://bluz.io/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32 MHz
      - 256K
      - 32K

Controllino
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``controllino_maxi``
      - `Controllino Maxi <https://controllino.biz/controllino/maxi/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA2560
      - 16 MHz
      - 248K
      - 8K
    * - ``controllino_maxi_automation``
      - `Controllino Maxi Automation <https://controllino.biz/controllino/maxi-automation/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA2560
      - 16 MHz
      - 248K
      - 8K
    * - ``controllino_mega``
      - `Controllino Mega <https://controllino.biz/controllino/mega/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA2560
      - 16 MHz
      - 248K
      - 8K
    * - ``controllino_mini``
      - `Controllino Mini <https://controllino.biz/controllino/mini/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 31.50K
      - 2K

DFRobot
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``firebeetle32``
      - `FireBeetle-ESP32 <https://dfrobotblog.wordpress.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

DOIT
~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp32doit-devkit-v1``
      - `DOIT ESP32 DEVKIT V1 <http://www.doit.am/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

Delta
~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``delta_dfbm_nq620``
      - `Delta DFBM-NQ620 <https://developer.mbed.org/platforms/Delta-DFBM-NQ620/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64 MHz
      - 512K
      - 64K

DigiStump
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``oak``
      - `DigiStump Oak <http://digistump.com/category/22?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K

Digilent
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``cerebot32mx4``
      - `Digilent Cerebot 32MX4 <http://store.digilentinc.com/cerebot-32mx4-limited-time-see-chipkit-pro-mx4/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX460F512L
      - 80 MHz
      - 508K
      - 32K
    * - ``cerebot32mx7``
      - `Digilent Cerebot 32MX7 <http://www.microchip.com/Developmenttools/ProductDetails.aspx?PartNO=TDGL004&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX795F512L
      - 80 MHz
      - 508K
      - 128K
    * - ``chipkit_cmod``
      - `Digilent chipKIT Cmod <http://store.digilentinc.com/chipkit-cmod-breadboardable-mz-microcontroller-board/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX150F128D
      - 40 MHz
      - 124K
      - 32K
    * - ``chipkit_dp32``
      - `Digilent chipKIT DP32 <http://store.digilentinc.com/chipkit-dp32-dip-package-prototyping-microcontroller-board/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX250F128B
      - 40 MHz
      - 120K
      - 32K
    * - ``chipkit_mx3``
      - `Digilent chipKIT MX3 <http://store.digilentinc.com/chipkit-mx3-microcontroller-board-with-pmod-headers/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX320F128H
      - 80 MHz
      - 124K
      - 16K
    * - ``chipkit_pro_mx4``
      - `Digilent chipKIT Pro MX4 <http://store.digilentinc.com/chipkit-pro-mx4-embedded-systems-trainer-board/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX460F512L
      - 80 MHz
      - 508K
      - 32K
    * - ``chipkit_pro_mx7``
      - `Digilent chipKIT Pro MX7 <http://store.digilentinc.com/chipkit-pro-mx7-advanced-peripherals-embedded-systems-trainer-board/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX795F512L
      - 80 MHz
      - 508K
      - 128K
    * - ``chipkit_uc32``
      - `Digilent chipKIT uC32 <http://store.digilentinc.com/chipkit-uc32-basic-microcontroller-board-with-uno-r3-headers/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX340F512H
      - 80 MHz
      - 508K
      - 32K
    * - ``chipkit_wf32``
      - `Digilent chipKIT WF32 <http://store.digilentinc.com/chipkit-wf32-wifi-enabled-microntroller-board-with-uno-r3-headers/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX695F512L
      - 80 MHz
      - 508K
      - 128K
    * - ``chipkit_wifire``
      - `Digilent chipKIT WiFire <http://store.digilentinc.com/chipkit-wi-fire-wifi-enabled-mz-microcontroller-board/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MZ2048ECG100
      - 200 MHz
      - 1.98M
      - 512K
    * - ``mega_pic32``
      - `Digilent chipKIT MAX32 <http://store.digilentinc.com/chipkit-max32-microcontroller-board-with-mega-r3-headers/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX795F512L
      - 80 MHz
      - 508K
      - 128K
    * - ``openscope``
      - `Digilent OpenScope <http://store.digilentinc.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MZ2048EFG124
      - 200 MHz
      - 1.98M
      - 512K
    * - ``uno_pic32``
      - `Digilent chipKIT UNO32 <http://store.digilentinc.com/chipkit-uno32-basic-microcontroller-board-retired-see-chipkit-uc32/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX320F128H
      - 80 MHz
      - 124K
      - 16K

Digistump
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``digispark-pro``
      - `Digispark Pro <http://digistump.com/products/109?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY167
      - 16 MHz
      - 14.50K
      - 512B
    * - ``digispark-pro32``
      - `Digispark Pro (32 byte buffer) <http://digistump.com/products/109?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY167
      - 16 MHz
      - 14.50K
      - 512B
    * - ``digispark-pro64``
      - `Digispark Pro (16 MHz) (64 byte buffer) <http://digistump.com/products/109?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY167
      - 16 MHz
      - 14.50K
      - 512B
    * - ``digispark-tiny``
      - `Digispark USB <http://digistump.com/products/1?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY85
      - 16 MHz
      - 5.87K
      - 512B
    * - ``digix``
      - `Digistump DigiX <http://digistump.com/products/50?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - No
      - AT91SAM3X8E
      - 84 MHz
      - 512K
      - 28K

Doit
~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``espduino``
      - `ESPDuino (ESP-13 Module) <https://www.tindie.com/products/doit/espduinowifi-uno-r3/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K

Dongsen Technology
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``pocket_32``
      - `Dongsen Tech Pocket 32 <http://dong-sen.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

Dwengo
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``dwenguino``
      - `Dwenguino <http://www.dwengo.org/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - AT90USB646
      - 16 MHz
      - 60K
      - 2K

DycodeX
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``espectro``
      - `ESPectro Core <https://shop.makestro.com/en/product/espectro-core/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K
    * - ``espectro32``
      - `ESPectro32 <https://shop.makestro.com/product/espectro32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

ESP32vn
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp32vn-iot-uno``
      - `ESP32vn IoT Uno <https://esp32.vn/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

ESPert
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``espresso_lite_v1``
      - `ESPresso Lite 1.0 <http://www.espert.co?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K
    * - ``espresso_lite_v2``
      - `ESPresso Lite 2.0 <http://www.espert.co?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K

ESPino
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``espino``
      - `ESPino <http://www.espino.io?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K

Electronic SweetPeas
~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp320``
      - `Electronic SweetPeas ESP320 <http://www.sweetpeas.se/controller-modules/10-esp210.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

Elektor
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``elektor_uno_r4``
      - `Elektor Uno R4 <https://www.elektor.com/elektor-uno-r4?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328PB
      - 16 MHz
      - 31.50K
      - 2K

Engduino
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``engduinov3``
      - `Engduino 3 <http://www.engduino.org?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8 MHz
      - 28K
      - 2.50K

EnviroDIY
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``mayfly``
      - `EnviroDIY Mayfly <http://envirodiy.org/forums/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 8 MHz
      - 127K
      - 16K

Espressif
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp-wrover-kit``
      - `Espressif ESP-WROVER-KIT <https://espressif.com/en/products/hardware/esp-wrover-kit/overview?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K
    * - ``esp01``
      - `Espressif Generic ESP8266 ESP-01 512k <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 512K
      - 80K
    * - ``esp01_1m``
      - `Espressif Generic ESP8266 ESP-01 1M <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 1M
      - 80K
    * - ``esp07``
      - `Espressif Generic ESP8266 ESP-07 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs#esp-07>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K
    * - ``esp12e``
      - `Espressif ESP8266 ESP-12E <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K
    * - ``esp32dev``
      - `Espressif ESP32 Dev Module <https://en.wikipedia.org/wiki/ESP32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K
    * - ``esp8285``
      - `Generic ESP8285 Module <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 423.98K
      - 80K
    * - ``esp_wroom_02``
      - `ESP-WROOM-02 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K
    * - ``phoenix_v1``
      - `Phoenix 1.0 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K
    * - ``phoenix_v2``
      - `Phoenix 2.0 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K
    * - ``wifinfo``
      - `WifInfo <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 1M
      - 80K

Fubarino
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``fubarino_mini``
      - `Fubarino Mini <http://fubarino.org/mini/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX250F128D
      - 48 MHz
      - 120K
      - 32K
    * - ``fubarino_sd``
      - `Fubarino SD (1.5) <http://fubarino.org/sd/index.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX795F512H
      - 80 MHz
      - 508K
      - 128K

Generic
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``bluepill_f103c8``
      - `BluePill F103C8 <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103C8T6
      - 72 MHz
      - 64K
      - 20K
    * - ``genericSTM32F103C8``
      - `STM32F103C8 (20k RAM. 64k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103C8T6
      - 72 MHz
      - 64K
      - 20K
    * - ``genericSTM32F103CB``
      - `STM32F103CB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103cb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103CBT6
      - 72 MHz
      - 128K
      - 20K
    * - ``genericSTM32F103R8``
      - `STM32F103R8 (20k RAM. 64 Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103r8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103R8T6
      - 72 MHz
      - 64K
      - 20K
    * - ``genericSTM32F103RB``
      - `STM32F103RB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RBT6
      - 72 MHz
      - 128K
      - 20K
    * - ``genericSTM32F103RC``
      - `STM32F103RC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rc.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RCT6
      - 72 MHz
      - 256K
      - 48K
    * - ``genericSTM32F103RE``
      - `STM32F103RE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103re.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RET6
      - 72 MHz
      - 512K
      - 64K
    * - ``genericSTM32F103VC``
      - `STM32F103VC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103VCT6
      - 72 MHz
      - 256K
      - 48K
    * - ``genericSTM32F103VE``
      - `STM32F103VE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103VET6
      - 72 MHz
      - 512K
      - 64K

Generic ATTiny
~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``attiny13``
      - `Generic ATTiny13 <http://www.atmel.com/devices/ATTINY13.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY13
      - 9 MHz
      - 1K
      - 64B
    * - ``attiny1634``
      - `Generic ATTiny1634 <http://www.atmel.com/devices/ATTINY1634.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY1634
      - 8 MHz
      - 16K
      - 1K
    * - ``attiny167``
      - `Generic ATTiny167 <http://www.atmel.com/devices/ATTINY167.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY167
      - 8 MHz
      - 16K
      - 512B
    * - ``attiny2313``
      - `Generic ATTiny2313 <http://www.microchip.com/wwwproducts/en/ATTINY2313?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY2313
      - 8 MHz
      - 2K
      - 128B
    * - ``attiny24``
      - `Generic ATTiny24 <http://www.atmel.com/devices/ATTINY24.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY24
      - 8 MHz
      - 2K
      - 128B
    * - ``attiny25``
      - `Generic ATTiny25 <http://www.atmel.com/devices/ATTINY25.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY25
      - 8 MHz
      - 2K
      - 128B
    * - ``attiny261``
      - `Generic ATTiny261 <http://www.atmel.com/devices/ATTINY261.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY261
      - 8 MHz
      - 2K
      - 128B
    * - ``attiny4313``
      - `Generic ATTiny4313 <http://www.microchip.com/wwwproducts/en/ATTINY4313?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY4313
      - 8 MHz
      - 4K
      - 256B
    * - ``attiny44``
      - `Generic ATTiny44 <http://www.atmel.com/devices/ATTINY44.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY44
      - 8 MHz
      - 4K
      - 256B
    * - ``attiny441``
      - `Generic ATTiny441 <http://www.atmel.com/devices/ATTINY441.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY441
      - 8 MHz
      - 4K
      - 256B
    * - ``attiny45``
      - `Generic ATTiny45 <http://www.atmel.com/devices/ATTINY45.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY45
      - 8 MHz
      - 4K
      - 256B
    * - ``attiny461``
      - `Generic ATTiny461 <http://www.atmel.com/devices/ATTINY461.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY461
      - 8 MHz
      - 4K
      - 256B
    * - ``attiny48``
      - `Generic ATTiny48 <http://www.atmel.com/devices/ATTINY48.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY48
      - 8 MHz
      - 4K
      - 256B
    * - ``attiny84``
      - `Generic ATTiny84 <http://www.atmel.com/devices/ATTINY84.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY84
      - 8 MHz
      - 8K
      - 512B
    * - ``attiny841``
      - `Generic ATTiny841 <http://www.atmel.com/devices/ATTINY841.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY841
      - 8 MHz
      - 8K
      - 512B
    * - ``attiny85``
      - `Generic ATTiny85 <http://www.atmel.com/devices/ATTINY85.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY85
      - 8 MHz
      - 8K
      - 512B
    * - ``attiny861``
      - `Generic ATTiny861 <http://www.atmel.com/devices/ATTINY861.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY861
      - 8 MHz
      - 8K
      - 512B
    * - ``attiny87``
      - `Generic ATTiny87 <http://www.atmel.com/devices/ATTINY87.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY87
      - 8 MHz
      - 8K
      - 512B
    * - ``attiny88``
      - `Generic ATTiny88 <http://www.atmel.com/devices/ATTINY88.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY88
      - 8 MHz
      - 8K
      - 512B

Heltec
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``heltec_wifi_kit_8``
      - `Heltec Wifi kit 8 <http://www.heltec.cn/project/wifi_kit_8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K

Heltec Automation
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``heltec_wifi_kit_32``
      - `Heltec WIFI Kit 32 <http://www.heltec.cn?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K
    * - ``heltec_wifi_lora_32``
      - `Heltec WIFI LoRa 32 <http://www.heltec.cn?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

Hornbill
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``hornbill32dev``
      - `Hornbill ESP32 Dev <https://hackaday.io/project/18997-hornbill?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K
    * - ``hornbill32minima``
      - `Hornbill ESP32 Minima <https://hackaday.io/project/18997-hornbill?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

Intel
~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``genuino101``
      - `Arduino/Genuino 101 <https://www.arduino.cc/en/Main/ArduinoBoard101?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Intel ARC32 <platform_intel_arc32>`
      - No
      - ARCV2EM
      - 32 MHz
      - 152K
      - 80K

IntoRobot
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``intorobot``
      - `IntoRobot Fig <http://docs.intorobot.com/zh/hardware/fig/hardware/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

LeafLabs
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``maple``
      - `Maple <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RBT6
      - 72 MHz
      - 108K
      - 17K
    * - ``maple_mini_b20``
      - `Maple Mini Bootloader 2.0 <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103CBT6
      - 72 MHz
      - 120K
      - 20K
    * - ``maple_mini_origin``
      - `Maple Mini Original <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103CBT6
      - 72 MHz
      - 108K
      - 17K

LightUp
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lightup``
      - `LightUp <https://www.lightup.io/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8 MHz
      - 28K
      - 2.50K

Linino
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``one``
      - `Linino One <http://www.linino.org/portfolio/linino-one/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K

LowPowerLab
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``mightyhat``
      - `LowPowerLab MightyHat <https://lowpowerlab.com/shop/product/130?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 31K
      - 2K
    * - ``moteino``
      - `LowPowerLab Moteino <https://lowpowerlab.com/shop/moteino-r4?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 31.50K
      - 2K
    * - ``moteinomega``
      - `LowPowerLab MoteinoMEGA <http://lowpowerlab.com/blog/2014/08/09/moteinomega-available-now/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 16 MHz
      - 127K
      - 16K

M5Stack
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``m5stack-core-esp32``
      - `M5Stack Core ESP32 <http://www.m5stack.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

MH-ET Live
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``mhetesp32devkit``
      - `MH ET LIVE ESP32DevKIT <http://forum.mhetlive.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K
    * - ``mhetesp32minikit``
      - `MH ET LIVE ESP32MiniKit <http://forum.mhetlive.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

MXChip
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``mxchip_az3166``
      - `Microsoft Azure IoT Development Kit (MXChip AZ3166) <https://microsoft.github.io/azure-iot-developer-kit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F412ZGT6
      - 100 MHz
      - 1M
      - 256K

Macchina
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``macchina2``
      - `Macchina M2 <https://www.macchina.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - No
      - AT91SAM3X8E
      - 84 MHz
      - 512K
      - 32K

MakerAsia
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``nano32``
      - `MakerAsia Nano32 <http://iot-bits.com/nano32-esp32-development-board?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

Mcudude
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``mightycore1284``
      - `MightyCore ATmega1284 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 16 MHz
      - 127K
      - 16K
    * - ``mightycore16``
      - `MightyCore ATmega16 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA16
      - 16 MHz
      - 15.50K
      - 1K
    * - ``mightycore164``
      - `MightyCore ATmega164 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA164P
      - 16 MHz
      - 15.50K
      - 1K
    * - ``mightycore32``
      - `MightyCore ATmega32 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32
      - 16 MHz
      - 31.50K
      - 2K
    * - ``mightycore324``
      - `MightyCore ATmega324 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA324P
      - 16 MHz
      - 31.50K
      - 2K
    * - ``mightycore644``
      - `MightyCore ATmega644 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA644P
      - 16 MHz
      - 63K
      - 4K
    * - ``mightycore8535``
      - `MightyCore ATmega8535 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA16
      - 16 MHz
      - 7.50K
      - 512B

MediaTek Labs
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``smart7688``
      - `LinkIt Smart 7688 Duo <https://www.seeedstudio.com/LinkIt-Smart-7688-Duo-p-2574.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8 MHz
      - 28K
      - 2.50K

Microduino
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``1284p16m``
      - `Microduino Core+ (ATmega1284P@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_Core%2B?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 16 MHz
      - 127K
      - 16K
    * - ``1284p8m``
      - `Microduino Core+ (ATmega1284P@8M,3.3V) <http://wiki.microduinoinc.com/Microduino-Module_Core%2B?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 8 MHz
      - 127K
      - 16K
    * - ``168pa16m``
      - `Microduino Core (Atmega168PA@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_Core?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168P
      - 16 MHz
      - 15.50K
      - 1K
    * - ``168pa8m``
      - `Microduino Core (Atmega168PA@8M,3.3V) <http://wiki.microduinoinc.com/Microduino-Module_Core?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168P
      - 8 MHz
      - 15.50K
      - 1K
    * - ``328p16m``
      - `Microduino Core (Atmega328P@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_Core?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 31.50K
      - 2K
    * - ``328p8m``
      - `Microduino Core (Atmega328P@8M,3.3V) <http://wiki.microduinoinc.com/Microduino-Module_Core?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8 MHz
      - 31.50K
      - 2K
    * - ``32u416m``
      - `Microduino Core USB (ATmega32U4@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_CoreUSB?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K
    * - ``644pa16m``
      - `Microduino Core+ (Atmega644PA@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_Core%2B?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA644P
      - 16 MHz
      - 63K
      - 4K
    * - ``644pa8m``
      - `Microduino Core+ (Atmega644PA@8M,3.3V) <http://wiki.microduinoinc.com/Microduino-Module_Core%2B?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA644P
      - 8 MHz
      - 63K
      - 4K
    * - ``microduino-core-esp32``
      - `Microduino Core ESP32 <https://microduinoinc.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

MikroElektronika
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``clicker2``
      - `MikroElektronika Clicker 2 <http://www.mikroe.com/pic/clicker/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX460F512L
      - 80 MHz
      - 508K
      - 32K
    * - ``flipnclickmz``
      - `MikroElektronika Flip N Click MZ <https://shop.mikroe.com/flipclick-pic32mz?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MZ2048EFH100
      - 252 MHz
      - 1.98M
      - 512K

NodeMCU
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``nodemcu``
      - `NodeMCU 0.9 (ESP-12 Module) <http://www.nodemcu.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K
    * - ``nodemcu-32s``
      - `NodeMCU-32S <http://www.nodemcu.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K
    * - ``nodemcuv2``
      - `NodeMCU 1.0 (ESP-12E Module) <http://www.nodemcu.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K

Noduino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``quantum``
      - `Noduino Quantum <http://wiki.jackslab.org/Noduino?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

Nordic
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``nrf51_dk``
      - `Nordic nRF51-DK <https://developer.mbed.org/platforms/Nordic-nRF51-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32 MHz
      - 256K
      - 32K
    * - ``nrf51_dongle``
      - `Nordic nRF51-Dongle <https://developer.mbed.org/platforms/Nordic-nRF51-Dongle/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32 MHz
      - 256K
      - 32K
    * - ``nrf52840_dk``
      - `Nordic nRF52840-DK <https://os.mbed.com/platforms/Nordic-nRF52840-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52840
      - 64 MHz
      - 1M
      - 256K
    * - ``nrf52_dk``
      - `Nordic nRF52-DK <https://developer.mbed.org/platforms/Nordic-nRF52-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64 MHz
      - 512K
      - 64K

OLIMEX
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp32-evb``
      - `OLIMEX ESP32-EVB <https://www.olimex.com/Products/IoT/ESP32-EVB/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K
    * - ``esp32-gateway``
      - `OLIMEX ESP32-GATEWAY <https://www.olimex.com/Products/IoT/ESP32-GATEWAY/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

OSHChip
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``oshchip``
      - `OSHChip <http://oshchip.org/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32 MHz
      - 256K
      - 32K

Olimex
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``modwifi``
      - `Olimex MOD-WIFI-ESP8266(-DEV) <https://www.olimex.com/Products/IoT/MOD-WIFI-ESP8266-DEV/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 2M
      - 80K
    * - ``pinguino32``
      - `Olimex PIC32-PINGUINO <https://www.olimex.com/Products/Duino/PIC32/PIC32-PINGUINO/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX440F256H
      - 80 MHz
      - 252K
      - 32K

Onehorse
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``onehorse32dev``
      - `Onehorse ESP32 Dev Module <https://www.tindie.com/products/onehorse/esp32-development-board/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

OpenBCI
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``openbci``
      - `OpenBCI 32bit <http://shop.openbci.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX250F128B
      - 40 MHz
      - 120K
      - 32K

OpenEnergyMonitor
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``emonpi``
      - `OpenEnergyMonitor emonPi <https://github.com/openenergymonitor/emonpi?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 30K
      - 2K

PONTECH
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``usbono_pic32``
      - `PONTECH UAV100 <http://www.pontech.com/productdisplay/uav100?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX440F512H
      - 80 MHz
      - 508K
      - 32K

PanStamp
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``panStampAVR``
      - `PanStamp AVR <http://www.panstamp.com/product/panstamp-avr/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8 MHz
      - 31.50K
      - 2K
    * - ``panStampNRG``
      - `PanStamp NRG 1.1 <http://www.panstamp.com/product/197/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - No
      - CC430F5137
      - 12 MHz
      - 31.88K
      - 4K

Pinoccio
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``pinoccio``
      - `Pinoccio Scout <https://www.crowdsupply.com/pinoccio/mesh-sensor-network?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA256RFR2
      - 16 MHz
      - 248K
      - 32K

Pololu Corporation
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``a-star32U4``
      - `Pololu A-Star 32U4 <https://www.pololu.com/category/149/a-star-programmable-controllers?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K

Pontech
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``nofire``
      - `Pontech NoFire <http://www.pontech.com/products?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MZ2048EFG100
      - 200 MHz
      - 1.98M
      - 512K
    * - ``quick240_usb``
      - `Pontech Quick240 <http://chipkit.net/wpcproduct/pontech-quick240/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX795F512L
      - 80 MHz
      - 508K
      - 128K

Punch Through
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lightblue-bean``
      - `LightBlue Bean <https://punchthrough.com/bean?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8 MHz
      - 31.50K
      - 2K
    * - ``lightblue-beanplus``
      - `LightBlue Bean+ <https://punchthrough.com/bean?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 31.50K
      - 2K

Quirkbot
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``quirkbot``
      - `Quirkbot <http://quirkbot.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8 MHz
      - 28K
      - 2.50K

RFduino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``rfduino``
      - `RFduino <http://www.rfduino.com/product/rfd22102-rfduino-dip/index.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 128K
      - 8K

RedBearLab
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``blend``
      - `RedBearLab Blend <http://redbearlab.com/blend/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K
    * - ``blendmicro16``
      - `RedBearLab Blend Micro 3.3V/16MHz (overclock) <http://redbearlab.com/blendmicro/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K
    * - ``blendmicro8``
      - `RedBearLab Blend Micro 3.3V/8MHz <http://redbearlab.com/blendmicro/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8 MHz
      - 28K
      - 2.50K
    * - ``redBearLab``
      - `RedBearLab nRF51822 <https://developer.mbed.org/platforms/RedBearLab-nRF51822/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 256K
      - 16K
    * - ``redBearLabBLENano``
      - `RedBearLab BLE Nano 1.5 <https://developer.mbed.org/platforms/RedBearLab-BLE-Nano/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 256K
      - 32K
    * - ``redbear_blenano2``
      - `RedBearLab BLE Nano 2 <https://redbear.cc/product/ble-nano-2-soldered.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64 MHz
      - 512K
      - 64K
    * - ``redbear_blend2``
      - `RedBearLab Blend 2 <https://redbear.cc/product/ble/blend-2.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64 MHz
      - 512K
      - 64K

RepRap
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``reprap_rambo``
      - `RepRap RAMBo <http://reprap.org/wiki/Rambo?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA2560
      - 16 MHz
      - 252K
      - 8K

SODAQ
~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``sodaq_autonomo``
      - `SODAQ Autonomo <http://support.sodaq.com/sodaq-one/autonomo/getting-started-autonomo/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - No
      - SAMD21J18A
      - 48 MHz
      - 256K
      - 32K
    * - ``sodaq_explorer``
      - `SODAQ ExpLoRer <http://support.sodaq.com/sodaq-one/explorer/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21J18A
      - 48 MHz
      - 256K
      - 32K
    * - ``sodaq_galora``
      - `SODAQ GaLoRa <http://support.sodaq.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 8 MHz
      - 127K
      - 16K
    * - ``sodaq_mbili``
      - `SODAQ Mbili <http://support.sodaq.com/sodaq-one/sodaq-mbili-1284p/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 8 MHz
      - 127K
      - 16K
    * - ``sodaq_moja``
      - `SODAQ Moja <http://support.sodaq.com/sodaq-one/moja/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8 MHz
      - 31.50K
      - 2K
    * - ``sodaq_ndogo``
      - `SODAQ Ndogo <http://support.sodaq.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 8 MHz
      - 127K
      - 16K
    * - ``sodaq_one``
      - `SODAQ ONE <http://support.sodaq.com/sodaq-one/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``sodaq_tatu``
      - `SODAQ Tatu <http://support.sodaq.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 8 MHz
      - 127K
      - 16K

ST
~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``nucleo_f103rb``
      - `ST Nucleo F103RB <https://developer.mbed.org/platforms/ST-Nucleo-F103RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RBT6
      - 72 MHz
      - 128K
      - 20K

SainSmart
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``sainSmartDue``
      - `SainSmart Due (Programming Port) <http://www.sainsmart.com/arduino/control-boards/sainsmart-due-atmel-sam3x8e-arm-cortex-m3-board-black.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - No
      - AT91SAM3X8E
      - 84 MHz
      - 512K
      - 32K
    * - ``sainSmartDueUSB``
      - `SainSmart Due (USB Native Port) <http://www.sainsmart.com/arduino/control-boards/sainsmart-due-atmel-sam3x8e-arm-cortex-m3-board-black.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - No
      - AT91SAM3X8E
      - 84 MHz
      - 512K
      - 32K

Sanguino
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``sanguino_atmega1284_8m``
      - `Sanguino ATmega1284p (8MHz) <https://code.google.com/p/sanguino/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 8 MHz
      - 127K
      - 16K
    * - ``sanguino_atmega1284p``
      - `Sanguino ATmega1284p (16MHz) <https://code.google.com/p/sanguino/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 16 MHz
      - 127K
      - 16K
    * - ``sanguino_atmega644``
      - `Sanguino ATmega644 or ATmega644A (16 MHz) <https://code.google.com/p/sanguino/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA644
      - 16 MHz
      - 63K
      - 4K
    * - ``sanguino_atmega644_8m``
      - `Sanguino ATmega644 or ATmega644A (8 MHz) <https://code.google.com/p/sanguino/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA644
      - 8 MHz
      - 63K
      - 4K
    * - ``sanguino_atmega644p``
      - `Sanguino ATmega644P or ATmega644PA (16 MHz) <https://code.google.com/p/sanguino/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA644P
      - 16 MHz
      - 63K
      - 4K
    * - ``sanguino_atmega644p_8m``
      - `Sanguino ATmega644P or ATmega644PA (8 MHz) <https://code.google.com/p/sanguino/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA644P
      - 8 MHz
      - 63K
      - 4K

SeeedStudio
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``cui32stem``
      - `SeeedStudio CUI32stem <http://www.seeedstudio.com/wiki/CUI32Stem?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX795F512H
      - 80 MHz
      - 508K
      - 128K
    * - ``seeedTinyBLE``
      - `Seeed Tiny BLE <http://developer.mbed.org/platforms/Seeed-Tiny-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 256K
      - 16K
    * - ``seeeduino``
      - `Seeeduino <https://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 31.50K
      - 2K
    * - ``wio_node``
      - `Wio Node <https://www.seeedstudio.com/Wio-Node-p-2637.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K

SparkFun
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``sparkfunBlynk``
      - `SparkFun Blynk Board <https://www.sparkfun.com/products/13794?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K
    * - ``sparkfun_digitalsandbox``
      - `SparkFun Digital Sandbox <https://www.sparkfun.com/products/12651?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8 MHz
      - 31.50K
      - 2K
    * - ``sparkfun_fiov3``
      - `SparkFun Fio V3 3.3V/8MHz <https://www.sparkfun.com/products/11520?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8 MHz
      - 28K
      - 2.50K
    * - ``sparkfun_makeymakey``
      - `SparkFun Makey Makey <https://www.sparkfun.com/products/11511?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K
    * - ``sparkfun_megamini``
      - `SparkFun Mega Pro Mini 3.3V <https://www.sparkfun.com/products/10743?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA2560
      - 8 MHz
      - 252K
      - 8K
    * - ``sparkfun_megapro16MHz``
      - `SparkFun Mega Pro 5V/16MHz <https://www.sparkfun.com/products/11007?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA2560
      - 16 MHz
      - 248K
      - 8K
    * - ``sparkfun_megapro8MHz``
      - `SparkFun Mega Pro 3.3V/8MHz <https://www.sparkfun.com/products/10744?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA2560
      - 8 MHz
      - 252K
      - 8K
    * - ``sparkfun_promicro16``
      - `SparkFun Pro Micro 5V/16MHz <https://www.sparkfun.com/products/12640?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K
    * - ``sparkfun_promicro8``
      - `SparkFun Pro Micro 3.3V/8MHz <https://www.sparkfun.com/products/12587?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8 MHz
      - 28K
      - 2.50K
    * - ``sparkfun_qduinomini``
      - `SparkFun Qduino Mini <https://www.sparkfun.com/products/13614?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8 MHz
      - 28K
      - 2.50K
    * - ``sparkfun_redboard``
      - `SparkFun RedBoard <https://www.sparkfun.com/products/12757?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 31.50K
      - 2K
    * - ``sparkfun_samd21_dev_usb``
      - `SparkFun SAMD21 Dev Breakout <https://www.sparkfun.com/products/13672?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``sparkfun_samd21_mini_usb``
      - `SparkFun SAMD21 Mini Breakout <https://www.sparkfun.com/products/13664?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``sparkfun_satmega128rfa1``
      - `SparkFun ATmega128RFA1 Dev Board <https://www.sparkfun.com/products/11197?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA128RFA1
      - 16 MHz
      - 16K
      - 124K
    * - ``sparkfun_serial7seg``
      - `SparkFun Serial 7-Segment Display <https://www.sparkfun.com/products/11441?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8 MHz
      - 31.50K
      - 2K
    * - ``thing``
      - `SparkFun ESP8266 Thing <https://www.sparkfun.com/products/13231?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 512K
      - 80K
    * - ``thingdev``
      - `SparkFun ESP8266 Thing Dev <https://www.sparkfun.com/products/13231?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 512K
      - 80K
    * - ``uview``
      - `SparkFun MicroView <https://www.sparkfun.com/products/12923?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 31.50K
      - 2K

SparkFun Electronics
~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp32thing``
      - `SparkFun ESP32 Thing <https://www.sparkfun.com/products/13907?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

SpellFoundry
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``sleepypi``
      - `SpellFoundry Sleepy Pi 2 <https://spellfoundry.com/product/sleepy-pi-2/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8 MHz
      - 30K
      - 2K

SweetPea
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp210``
      - `SweetPea ESP-210 <http://wiki.sweetpeas.se/index.php?title=ESP-210&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K

Taida Century
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``stct_nrf52_minidev``
      - `Taida Century nRF52 mini board <http://taida-century.com/en/index.asp?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64 MHz
      - 512K
      - 64K

Teensy
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``teensy20``
      - `Teensy 2.0 <https://www.pjrc.com/store/teensy.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 31.50K
      - 2.50K
    * - ``teensy20pp``
      - `Teensy++ 2.0 <https://www.pjrc.com/store/teensypp.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - No
      - AT90USB1286
      - 16 MHz
      - 127K
      - 8K
    * - ``teensy30``
      - `Teensy 3.0 <https://www.pjrc.com/store/teensy3.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - No
      - MK20DX128
      - 48 MHz
      - 128K
      - 16K
    * - ``teensy31``
      - `Teensy 3.1 / 3.2 <https://www.pjrc.com/store/teensy31.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - No
      - MK20DX256
      - 72 MHz
      - 256K
      - 64K
    * - ``teensy35``
      - `Teensy 3.5 <https://www.pjrc.com/store/teensy35.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`Yes <piodebug>`
      - MK64FX512
      - 120 MHz
      - 512K
      - 192K
    * - ``teensy36``
      - `Teensy 3.6 <https://www.pjrc.com/store/teensy36.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`Yes <piodebug>`
      - MK66FX1M0
      - 180 MHz
      - 1M
      - 256K
    * - ``teensylc``
      - `Teensy LC <http://www.pjrc.com/teensy/teensyLC.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - No
      - MKL26Z64
      - 48 MHz
      - 62K
      - 8K

ThaiEasyElec
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``espino32``
      - `ESPino32 <http://thaieasyelec.com/products/development-boards/espino-wifi-development-board-detail.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K
    * - ``espinotee``
      - `ThaiEasyElec ESPino <http://www.thaieasyelec.com/products/wireless-modules/wifi-modules/espino-wifi-development-board-detail.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K

The Things Network
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``the_things_uno``
      - `The Things Uno <https://shop.thethingsnetwork.com/index.php/product/the-things-uno/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16 MHz
      - 28K
      - 2.50K

TinyCircuits
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``tinyduino``
      - `TinyCircuits TinyDuino Processor Board <https://tiny-circuits.com/tinyduino-processor-board.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8 MHz
      - 30K
      - 2K
    * - ``tinylily``
      - `TinyCircuits TinyLily Mini Processor <https://tiny-circuits.com/tiny-lily-mini-processor.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8 MHz
      - 30K
      - 2K

UBW32
~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``ubw32_mx460``
      - `UBW32 MX460 <http://www.schmalzhaus.com/UBW32/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX460F512L
      - 80 MHz
      - 508K
      - 32K
    * - ``ubw32_mx795``
      - `UBW32 MX795 <http://www.schmalzhaus.com/UBW32/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX795F512L
      - 80 MHz
      - 508K
      - 128K

WEMOS
~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``d1``
      - `WEMOS D1 R1 (Retired) <https://wiki.wemos.cc/products:d1:d1?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K
    * - ``d1_mini``
      - `WeMos D1 R2 & mini <https://wiki.wemos.cc/products:d1:d1_mini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 4M
      - 80K
    * - ``d1_mini_lite``
      - `WeMos D1 mini Lite <https://wiki.wemos.cc/products:d1:d1_mini_lite?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 1M
      - 80K
    * - ``d1_mini_pro``
      - `WeMos D1 mini Pro <https://wiki.wemos.cc/products:d1:d1_mini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80 MHz
      - 16M
      - 80K
    * - ``lolin32``
      - `WEMOS LOLIN32 <https://wemos.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K
    * - ``wemosbat``
      - `WeMos WiFi & Bluetooth Battery <https://www.wemos.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

Waveshare
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``waveshare_ble400``
      - `Waveshare BLE400 <http://www.waveshare.com/wiki/BLE400?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32 MHz
      - 256K
      - 32K

Wicked Device
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``wildfirev2``
      - `Wicked Device WildFire V2 <http://shop.wickeddevice.com/resources/wildfire/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 16 MHz
      - 120.00K
      - 16K
    * - ``wildfirev3``
      - `Wicked Device WildFire V3 <http://shop.wickeddevice.com/resources/wildfire/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 16 MHz
      - 127K
      - 16K

Widora
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``widora-air``
      - `Widora AIR <http://widora.io?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K

chipKIT
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lenny``
      - `chipKIT Lenny <http://chipkit.net/tag/lenny/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX270F256D
      - 40 MHz
      - 120K
      - 32K

element14
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``chipkit_pi``
      - `Element14 chipKIT Pi <http://www.element14.com/community/community/knode/dev_platforms_kits/element14_dev_kits/microchip-chipkit/chipkit_pi?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX250F128B
      - 40 MHz
      - 120K
      - 32K

makerlab.mx
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``altair``
      - `Altair <http://www.aquila.io/en?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA256RFR2
      - 16 MHz
      - 248K
      - 32K

ng-beacon
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``ng_beacon``
      - `ng-beacon <https://github.com/urish/ng-beacon?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32 MHz
      - 256K
      - 32K

nicai-systems
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``bob3``
      - `nicai-systems BOB3 coding bot <http://www.nicai-systems.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA88
      - 8 MHz
      - 8K
      - 1K
    * - ``nibo2``
      - `nicai-systems NIBO 2 robot <http://www.nicai-systems.com/en/nibo2?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA128
      - 16 MHz
      - 128K
      - 4K
    * - ``nibobee``
      - `nicai-systems NIBObee robot <http://www.nicai-systems.com/en/nibobee?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA16
      - 15 MHz
      - 16K
      - 1K
    * - ``nibobee_1284``
      - `nicai-systems NIBObee robot with Tuning Kit <http://www.nicai-systems.com/en/nibobee?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 20 MHz
      - 128K
      - 16K
    * - ``niboburger``
      - `nicai-systems NIBO burger robot <http://www.nicai-systems.com/en/nibo-burger?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA16
      - 15 MHz
      - 16K
      - 1K
    * - ``niboburger_1284``
      - `nicai-systems NIBO burger robot with Tuning Kit <http://www.nicai-systems.com/en/nibo-burger?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 20 MHz
      - 128K
      - 16K

u-blox
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``nina_w10``
      - `u-blox NINA-W10 series <https://www.u-blox.com/en/product/nina-w10-series?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240 MHz
      - 1.25M
      - 288K
    * - ``ublox_evk_nina_b1``
      - `u-blox EVK-NINA-B1 <https://os.mbed.com/platforms/u-blox-EVK-NINA-B1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64 MHz
      - 512K
      - 64K

ubIQio
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``ardhat``
      - `ubIQio Ardhat <http://ardhat.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16 MHz
      - 31.50K
      - 2K
