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

:Configuration:
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
      - 16MHz
      - 256KB
      - 16KB
    * - ``delta_dfbm_nq620``
      - `Delta DFBM-NQ620 <https://developer.mbed.org/platforms/Delta-DFBM-NQ620/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``disco_f407vg``
      - `ST STM32F4DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF252419?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F407VGT6
      - 168MHz
      - 1MB
      - 128KB
    * - ``esp-wrover-kit``
      - `Espressif ESP-WROVER-KIT <https://espressif.com/en/products/hardware/esp-wrover-kit/overview?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_ftdi` (default, on-board), :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``mxchip_az3166``
      - `Microsoft Azure IoT Development Kit (MXChip AZ3166) <https://microsoft.github.io/azure-iot-developer-kit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB
    * - ``mzeropro``
      - `Arduino M0 Pro (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardM0PRO?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``nrf51_dk``
      - `Nordic nRF51-DK <https://developer.mbed.org/platforms/Nordic-nRF51-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``nrf51_dongle``
      - `Nordic nRF51-Dongle <https://developer.mbed.org/platforms/Nordic-nRF51-Dongle/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink` (on-board)
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``nrf52840_dk``
      - `Nordic nRF52840-DK <https://os.mbed.com/platforms/Nordic-nRF52840-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - ``nrf52_dk``
      - `Nordic nRF52-DK <https://developer.mbed.org/platforms/Nordic-nRF52-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``nucleo_f103rb``
      - `ST Nucleo F103RB <https://developer.mbed.org/platforms/ST-Nucleo-F103RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``redBearLab``
      - `RedBearLab nRF51822 <https://developer.mbed.org/platforms/RedBearLab-nRF51822/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``redBearLabBLENano``
      - `RedBearLab BLE Nano 1.5 <https://developer.mbed.org/platforms/RedBearLab-BLE-Nano/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB
    * - ``redbear_blenano2``
      - `RedBearLab BLE Nano 2 <https://redbear.cc/product/ble-nano-2-soldered.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``redbear_blend2``
      - `RedBearLab Blend 2 <https://redbear.cc/product/ble/blend-2.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``samd21g18a``
      - `Atmel ATSAMW25-XPRO <https://developer.mbed.org/platforms/SAMW25-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``seeedTinyBLE``
      - `Seeed Tiny BLE <http://developer.mbed.org/platforms/Seeed-Tiny-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``ublox_evk_nina_b1``
      - `u-blox EVK-NINA-B1 <https://os.mbed.com/platforms/u-blox-EVK-NINA-B1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``xmc1100_boot_kit``
      - `XMC1100 Boot Kit <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`debugging_tool_jlink` (on-board)
      - XMC1100
      - 32MHz
      - 64KB
      - 64KB
    * - ``xmc1100_h_bridge2go``
      - `XMC1100 H-Bridge 2Go <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`debugging_tool_jlink` (on-board)
      - XMC1100
      - 32MHz
      - 64KB
      - 64KB
    * - ``xmc1100_xmc2go``
      - `XMC1100 XMC2Go <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`debugging_tool_jlink` (on-board)
      - XMC1100
      - 32MHz
      - 64KB
      - 64KB
    * - ``xmc1300_boot_kit``
      - `XMC1300 Boot Kit <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`debugging_tool_jlink` (on-board)
      - XMC1300
      - 32MHz
      - 64KB
      - 64KB
    * - ``xmc1300_sense2gol``
      - `XMC1300 Sense2GoL <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`debugging_tool_jlink` (on-board)
      - XMC1300
      - 32MHz
      - 64KB
      - 122.23KB
    * - ``xmc4200_distance2go``
      - `XMC4200 Distance2Go <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`debugging_tool_jlink` (on-board)
      - XMC4200
      - 80MHz
      - 250KB
      - 256KB
    * - ``xmc4700_relax_kit``
      - `XMC4700 Relax Kit <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`debugging_tool_jlink` (on-board)
      - XMC4700
      - 144MHz
      - 2.00MB
      - 1.95MB
    * - ``zero``
      - `Arduino Zero (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB


External Debug Tools
^^^^^^^^^^^^^^^^^^^^

Boards listed below are compatible with :ref:`piodebug` but **DEPEND ON**
external debug tool. See "Debug" column for compatible debug tools.


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
    * - ``Sinobit``
      - `Sino:Bit <https://github.com/sinobitorg/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``adafruit_circuitplayground_m0``
      - `Adafruit Circuit Playground Express <https://www.adafruit.com/product/3333?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_feather_m0``
      - `Adafruit Feather M0 <https://www.adafruit.com/product/2772?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_feather_m0_express``
      - `Adafruit Feather M0 Express <https://www.adafruit.com/product/3403?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_feather_m4``
      - `Adafruit Feather M4 (SAMD51) <https://www.adafruit.com/product/3857?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - ``adafruit_gemma_m0``
      - `Adafruit Gemma M0 <https://www.adafruit.com/product/3501?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_itsybitsy_m0``
      - `Adafruit ItsyBitsy M0 <https://www.adafruit.com/product/3727?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_itsybitsy_m4``
      - `Adafruit ItsyBitsy M4 (SAMD51) <https://www.adafruit.com/product/3800?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - ``adafruit_metro_m0``
      - `Adafruit Metro M0 Expresss <https://www.adafruit.com/product/3505?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_metro_m4``
      - `Adafruit Metro M4 (SAMD51) <https://www.adafruit.com/product/3382?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - ``adafruit_pirkey``
      - `Adafruit pIRkey <https://www.adafruit.com/product/3364?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_trinket_m0``
      - `Adafruit Trinket M0 <https://www.adafruit.com/product/3500?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``alksesp32``
      - `ALKS ESP32 <https://github.com/RoboticsBrno/ArduinoLearningKitStarter.git?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``bluepill_f103c8``
      - `BluePill F103C8 <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``bluey``
      - `Bluey nRF52832 IoT <https://electronut.in/portfolio/bluey/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``bluz_dk``
      - `BluzDK <https://bluz.io/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``digix``
      - `Digistump DigiX <http://digistump.com/products/50?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - ``due``
      - `Arduino Due (Programming Port) <https://www.arduino.cc/en/Main/ArduinoBoardDue?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - ``dueUSB``
      - `Arduino Due (USB Native Port) <https://www.arduino.cc/en/Main/ArduinoBoardDue?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - ``esp32-evb``
      - `OLIMEX ESP32-EVB <https://www.olimex.com/Products/IoT/ESP32-EVB/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32-gateway``
      - `OLIMEX ESP32-GATEWAY <https://www.olimex.com/Products/IoT/ESP32-GATEWAY/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32dev``
      - `Espressif ESP32 Dev Module <https://en.wikipedia.org/wiki/ESP32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32doit-devkit-v1``
      - `DOIT ESP32 DEVKIT V1 <http://www.doit.am/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32thing``
      - `SparkFun ESP32 Thing <https://www.sparkfun.com/products/13907?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32vn-iot-uno``
      - `ESP32vn IoT Uno <https://esp32.vn/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``espectro32``
      - `ESPectro32 <https://shop.makestro.com/product/espectro32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``espino32``
      - `ESPino32 <http://thaieasyelec.com/products/development-boards/espino-wifi-development-board-detail.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``featheresp32``
      - `Adafruit ESP32 Feather <https://www.adafruit.com/product/3405?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``firebeetle32``
      - `FireBeetle-ESP32 <https://dfrobotblog.wordpress.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``genericSTM32F103C8``
      - `STM32F103C8 (20k RAM. 64k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``genericSTM32F103CB``
      - `STM32F103CB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103cb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103CBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``genericSTM32F103R8``
      - `STM32F103R8 (20k RAM. 64 Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103r8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103R8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``genericSTM32F103RB``
      - `STM32F103RB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``genericSTM32F103RC``
      - `STM32F103RC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rc.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103RCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``genericSTM32F103RE``
      - `STM32F103RE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103re.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103RET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``genericSTM32F103T8``
      - `STM32F103T8 (20k RAM. 64k Flash) <http://www.st.com/en/microcontrollers/stm32f103t8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103T8T6
      - 72MHz
      - 20KB
      - 64KB
    * - ``genericSTM32F103TB``
      - `STM32F103TB (20k RAM. 128k Flash) <http://www.st.com/en/microcontrollers/stm32f103tb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103TBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``genericSTM32F103VB``
      - `STM32F103VB (20k RAM. 128k Flash) <http://www.st.com/en/microcontrollers/stm32f103vb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103VBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``genericSTM32F103VC``
      - `STM32F103VC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``genericSTM32F103VD``
      - `STM32F103VD (64k RAM. 384k Flash) <http://www.st.com/en/microcontrollers/stm32f103vd.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103VDT6
      - 72MHz
      - 384KB
      - 64KB
    * - ``genericSTM32F103VE``
      - `STM32F103VE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103VET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``genericSTM32F103ZC``
      - `STM32F103ZC (48k RAM. 256k Flash) <http://www.st.com/en/microcontrollers/stm32f103zc.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103ZCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``genericSTM32F103ZD``
      - `STM32F103ZD (64k RAM. 384k Flash) <http://www.st.com/en/microcontrollers/stm32f103zd.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103ZDT6
      - 72MHz
      - 384KB
      - 64KB
    * - ``genericSTM32F103ZE``
      - `STM32F103ZE (64k RAM. 512k Flash) <http://www.st.com/en/microcontrollers/stm32f103ze.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``genericSTM32F407VET6``
      - `STM32F407VE (192k RAM. 512k Flash) <http://www.st.com/en/microcontrollers/stm32f407ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink`
      - STM32F407VET6
      - 168MHz
      - 502.23KB
      - 128KB
    * - ``hackaBLE``
      - `hackaBLE <https://electronut.in/portfolio/hackaBLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``hornbill32dev``
      - `Hornbill ESP32 Dev <https://hackaday.io/project/18997-hornbill?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``hornbill32minima``
      - `Hornbill ESP32 Minima <https://hackaday.io/project/18997-hornbill?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin32``
      - `WEMOS LOLIN32 <https://wiki.wemos.cc/products:lolin32:lolin32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin_d32``
      - `WEMOS LOLIN D32 <https://wiki.wemos.cc/products:d32:d32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin_d32_pro``
      - `WEMOS LOLIN D32 PRO <https://wiki.wemos.cc/products:d32:d32_pro?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``macchina2``
      - `Macchina M2 <https://www.macchina.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - ``maple``
      - `Maple <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103RBT6
      - 72MHz
      - 108KB
      - 17KB
    * - ``maple_mini_b20``
      - `Maple Mini Bootloader 2.0 <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103CBT6
      - 72MHz
      - 120KB
      - 20KB
    * - ``maple_mini_origin``
      - `Maple Mini Original <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103CBT6
      - 72MHz
      - 108KB
      - 17KB
    * - ``maple_ret6``
      - `Maple (RET6) <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103RET6
      - 72MHz
      - 256KB
      - 48KB
    * - ``mhetesp32devkit``
      - `MH ET LIVE ESP32DevKIT <http://forum.mhetlive.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``mhetesp32minikit``
      - `MH ET LIVE ESP32MiniKit <http://forum.mhetlive.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``microduino32_flash``
      - `Microduino Core STM32 to Flash <http://wiki.microduinoinc.com/Microduino-Module_CoreSTM32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103CBT6
      - 72MHz
      - 105.47KB
      - 16.60KB
    * - ``mkr1000USB``
      - `Arduino MKR1000 <https://www.arduino.cc/en/Main/ArduinoMKR1000?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrfox1200``
      - `Arduino MKR FOX 1200 <https://www.arduino.cc/en/Main.ArduinoBoardMKRFox1200?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrgsm1400``
      - `Arduino MKR GSM 1400 <https://store.arduino.cc/mkr-gsm-1400?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrwan1300``
      - `Arduino MKR WAN 1300 <https://store.arduino.cc/mkr-wan-1300?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrzero``
      - `Arduino MKRZERO <https://www.arduino.cc/en/Main/ArduinoBoardMKRZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``moteino_zero``
      - `Moteino M0 <https://lowpowerlab.com/shop/product/184?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mzeroUSB``
      - `Arduino M0 <https://www.arduino.cc/en/Main/ArduinoBoardM0?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mzeroproUSB``
      - `Arduino M0 Pro (Native USB Port) <https://www.arduino.cc/en/Main/ArduinoBoardM0PRO?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``ng_beacon``
      - `ng-beacon <https://github.com/urish/ng-beacon?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``node32s``
      - `Node32s <http://www.ayarafun.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``nodemcu-32s``
      - `NodeMCU-32S <http://www.nodemcu.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``oshchip``
      - `OSHChip <http://oshchip.org/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``pocket_32``
      - `Dongsen Tech Pocket 32 <http://dong-sen.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``rfduino``
      - `RFduino <http://www.rfduino.com/product/rfd22102-rfduino-dip/index.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 128KB
      - 8KB
    * - ``sainSmartDue``
      - `SainSmart Due (Programming Port) <http://www.sainsmart.com/arduino/control-boards/sainsmart-due-atmel-sam3x8e-arm-cortex-m3-board-black.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - ``sainSmartDueUSB``
      - `SainSmart Due (USB Native Port) <http://www.sainsmart.com/arduino/control-boards/sainsmart-due-atmel-sam3x8e-arm-cortex-m3-board-black.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - ``sodaq_autonomo``
      - `SODAQ Autonomo <http://support.sodaq.com/sodaq-one/autonomo/getting-started-autonomo/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sodaq_explorer``
      - `SODAQ ExpLoRer <http://support.sodaq.com/sodaq-one/explorer/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sodaq_one``
      - `SODAQ ONE <http://support.sodaq.com/sodaq-one/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sparkfun_samd21_dev_usb``
      - `SparkFun SAMD21 Dev Breakout <https://www.sparkfun.com/products/13672?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sparkfun_samd21_mini_usb``
      - `SparkFun SAMD21 Mini Breakout <https://www.sparkfun.com/products/13664?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``stct_nrf52_minidev``
      - `Taida Century nRF52 mini board <http://taida-century.com/en/index.asp?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``teensy31``
      - `Teensy 3.1 / 3.2 <https://www.pjrc.com/store/teensy31.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`debugging_tool_jlink`
      - MK20DX256
      - 72MHz
      - 256KB
      - 64KB
    * - ``teensy35``
      - `Teensy 3.5 <https://www.pjrc.com/store/teensy35.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`debugging_tool_jlink`
      - MK64FX512
      - 120MHz
      - 512KB
      - 192KB
    * - ``teensy36``
      - `Teensy 3.6 <https://www.pjrc.com/store/teensy36.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`debugging_tool_jlink`
      - MK66FX1M0
      - 180MHz
      - 1MB
      - 256KB
    * - ``teensylc``
      - `Teensy LC <http://www.pjrc.com/teensy/teensyLC.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`debugging_tool_jlink`
      - MKL26Z64
      - 48MHz
      - 62KB
      - 8KB
    * - ``tian``
      - `Arduino Tian <https://www.arduino.cc/en/Main/ArduinoBoardTian?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``ttgo-lora32-v1``
      - `TTGO LoRa32-OLED V1 <https://www.google.com.ua/search?q=TTGO+LoRa32-OLED+V1&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``waveshare_ble400``
      - `Waveshare BLE400 <http://www.waveshare.com/wiki/BLE400?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``wemosbat``
      - `WeMos WiFi & Bluetooth Battery <https://www.wemos.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``xinabox_cw02``
      - `XinaBox CW02 <https://xinabox.cc/products/cw02?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``zeroUSB``
      - `Arduino Zero (USB Native Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB


Examples
--------

* `Arduino for Atmel AVR <https://github.com/platformio/platform-atmelavr/tree/master/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Atmel SAM <https://github.com/platformio/platform-atmelsam/tree/master/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Espressif 32 <https://github.com/platformio/platform-espressif32/tree/master/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Espressif 8266 <https://github.com/platformio/platform-espressif8266/tree/master/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Infineon XMC <https://github.com/Infineon/platformio-infineonxmc/tree/master/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Intel ARC32 <https://github.com/platformio/platform-intel_arc32/tree/master/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Microchip PIC32 <https://github.com/platformio/platform-microchippic32/tree/master/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Nordic nRF51 <https://github.com/platformio/platform-nordicnrf51/tree/master/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Nordic nRF52 <https://github.com/platformio/platform-nordicnrf52/tree/master/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for ST STM32 <https://github.com/platformio/platform-ststm32/tree/master/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for Teensy <https://github.com/platformio/platform-teensy/tree/master/examples?utm_source=platformio&utm_medium=docs>`_
* `Arduino for TI MSP430 <https://github.com/platformio/platform-timsp430/tree/master/examples?utm_source=platformio&utm_medium=docs>`_

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

    * - :ref:`platform_infineonxmc`
      - Infineon has designed the XMC microcontrollers for real-time critical applications with an industry-standard core. The XMC microcontrollers can be integrated with the Arduino platform

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
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
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
      - 80MHz
      - 512KB
      - 80KB

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
      - 80MHz
      - 508KB
      - 128KB

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
      - `Adafruit Circuit Playground Express <https://www.adafruit.com/product/3333?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_feather_m0``
      - `Adafruit Feather M0 <https://www.adafruit.com/product/2772?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_feather_m0_express``
      - `Adafruit Feather M0 Express <https://www.adafruit.com/product/3403?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_feather_m4``
      - `Adafruit Feather M4 (SAMD51) <https://www.adafruit.com/product/3857?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - ``adafruit_gemma_m0``
      - `Adafruit Gemma M0 <https://www.adafruit.com/product/3501?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_itsybitsy_m0``
      - `Adafruit ItsyBitsy M0 <https://www.adafruit.com/product/3727?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_itsybitsy_m4``
      - `Adafruit ItsyBitsy M4 (SAMD51) <https://www.adafruit.com/product/3800?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - ``adafruit_metro_m0``
      - `Adafruit Metro M0 Expresss <https://www.adafruit.com/product/3505?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_metro_m4``
      - `Adafruit Metro M4 (SAMD51) <https://www.adafruit.com/product/3382?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - ``adafruit_pirkey``
      - `Adafruit pIRkey <https://www.adafruit.com/product/3364?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_trinket_m0``
      - `Adafruit Trinket M0 <https://www.adafruit.com/product/3500?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``bluefruitmicro``
      - `Adafruit Bluefruit Micro <https://www.adafruit.com/products/2661?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``feather328p``
      - `Adafruit Feather 328P <https://www.adafruit.com/product/3458?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - ``feather32u4``
      - `Adafruit Feather 32u4 <https://learn.adafruit.com/adafruit-feather-32u4-bluefruit-le/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``featheresp32``
      - `Adafruit ESP32 Feather <https://www.adafruit.com/product/3405?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``flora8``
      - `Adafruit Flora <http://www.adafruit.com/product/659?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``gemma``
      - `Adafruit Gemma <http://www.adafruit.com/products/1222?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - ``huzzah``
      - `Adafruit HUZZAH ESP8266 <https://www.adafruit.com/products/2471?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - ``itsybitsy32u4_3V``
      - `Adafruit ItsyBitsy 3V/8MHz <https://www.adafruit.com/product/3675?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``itsybitsy32u4_5V``
      - `Adafruit ItsyBitsy 5V/16MHz <https://www.adafruit.com/product/3677?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``metro``
      - `Adafruit Metro <https://www.adafruit.com/products/2466?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``protrinket3``
      - `Adafruit Pro Trinket 3V/12MHz (USB) <http://www.adafruit.com/products/2010?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 12MHz
      - 28KB
      - 2KB
    * - ``protrinket3ftdi``
      - `Adafruit Pro Trinket 3V/12MHz (FTDI) <http://www.adafruit.com/products/2010?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 12MHz
      - 28KB
      - 2KB
    * - ``protrinket5``
      - `Adafruit Pro Trinket 5V/16MHz (USB) <http://www.adafruit.com/products/2000?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - ``protrinket5ftdi``
      - `Adafruit Pro Trinket 5V/16MHz (FTDI) <http://www.adafruit.com/products/2000?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - ``trinket3``
      - `Adafruit Trinket 3V/8MHz <http://www.adafruit.com/products/1500?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - ``trinket5``
      - `Adafruit Trinket 5V/16MHz <http://www.adafruit.com/products/1501?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY85
      - 16MHz
      - 8KB
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
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
      - 16MHz
      - 31.50KB
      - 2KB

Amperka
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
    * - ``wifi_slot``
      - `WiFi Slot <http://wiki.amperka.ru/wifi-slot?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

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
      - 16MHz
      - 31.50KB
      - 2KB

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
      - 240MHz
      - 4MB
      - 320KB

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
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``arduboy_devkit``
      - `Arduboy DevKit <https://www.arduboy.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

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
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``atmega328pb``
      - `Atmel ATmega328PB <http://www.atmel.com/devices/ATMEGA328PB.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328PB
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``atmegangatmega168``
      - `Arduino NG or older ATmega168 <http://arduino.cc/en/main/boards?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - ``atmegangatmega8``
      - `Arduino NG or older ATmega8 <http://arduino.cc/en/main/boards?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA8
      - 16MHz
      - 7KB
      - 1KB
    * - ``btatmega168``
      - `Arduino BT ATmega168 <http://arduino.cc/en/main/boards?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - ``btatmega328``
      - `Arduino BT ATmega328 <http://arduino.cc/en/main/boards?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - ``chiwawa``
      - `Arduino Industrial 101 <https://store.arduino.cc/arduino-industrial-101?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``diecimilaatmega168``
      - `Arduino Duemilanove or Diecimila ATmega168 <http://arduino.cc/en/Main/ArduinoBoardDiecimila?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - ``diecimilaatmega328``
      - `Arduino Duemilanove or Diecimila ATmega328 <http://arduino.cc/en/Main/ArduinoBoardDiecimila?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - ``due``
      - `Arduino Due (Programming Port) <https://www.arduino.cc/en/Main/ArduinoBoardDue?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - ``dueUSB``
      - `Arduino Due (USB Native Port) <https://www.arduino.cc/en/Main/ArduinoBoardDue?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - ``esplora``
      - `Arduino Esplora <https://www.arduino.cc/en/Main/ArduinoBoardEsplora?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``ethernet``
      - `Arduino Ethernet <https://www.arduino.cc/en/Main/ArduinoBoardEthernet?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``fio``
      - `Arduino Fio <http://arduino.cc/en/Main/ArduinoBoardFio?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - ``leonardo``
      - `Arduino Leonardo <https://www.arduino.cc/en/Main/ArduinoBoardLeonardo?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``leonardoeth``
      - `Arduino Leonardo ETH <https://www.arduino.cc/en/Main/ArduinoBoardLeonardoEth?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``lilypadatmega168``
      - `Arduino LilyPad ATmega168 <http://arduino.cc/en/Main/ArduinoBoardLilyPad?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168
      - 8MHz
      - 14KB
      - 1KB
    * - ``lilypadatmega328``
      - `Arduino LilyPad ATmega328 <http://arduino.cc/en/Main/ArduinoBoardLilyPad?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - ``megaADK``
      - `Arduino Mega ADK <https://www.arduino.cc/en/Main/ArduinoBoardMegaADK?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - ``megaatmega1280``
      - `Arduino Mega or Mega 2560 ATmega1280 <https://www.arduino.cc/en/Main/ArduinoBoardMega2560?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1280
      - 16MHz
      - 124KB
      - 8KB
    * - ``megaatmega2560``
      - `Arduino Mega or Mega 2560 ATmega2560 (Mega 2560) <https://www.arduino.cc/en/Main/ArduinoBoardMega2560?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - ``micro``
      - `Arduino Micro <https://www.arduino.cc/en/Main/ArduinoBoardMicro?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``miniatmega168``
      - `Arduino Mini ATmega168 <http://arduino.cc/en/Main/ArduinoBoardMini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - ``miniatmega328``
      - `Arduino Mini ATmega328 <http://arduino.cc/en/Main/ArduinoBoardMini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - ``mkr1000USB``
      - `Arduino MKR1000 <https://www.arduino.cc/en/Main/ArduinoMKR1000?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrfox1200``
      - `Arduino MKR FOX 1200 <https://www.arduino.cc/en/Main.ArduinoBoardMKRFox1200?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrgsm1400``
      - `Arduino MKR GSM 1400 <https://store.arduino.cc/mkr-gsm-1400?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrwan1300``
      - `Arduino MKR WAN 1300 <https://store.arduino.cc/mkr-wan-1300?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrzero``
      - `Arduino MKRZERO <https://www.arduino.cc/en/Main/ArduinoBoardMKRZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mzeroUSB``
      - `Arduino M0 <https://www.arduino.cc/en/Main/ArduinoBoardM0?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mzeropro``
      - `Arduino M0 Pro (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardM0PRO?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mzeroproUSB``
      - `Arduino M0 Pro (Native USB Port) <https://www.arduino.cc/en/Main/ArduinoBoardM0PRO?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``nanoatmega168``
      - `Arduino Nano ATmega168 <https://www.arduino.cc/en/Main/ArduinoBoardNano?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - ``nanoatmega328``
      - `Arduino Nano ATmega328 <https://www.arduino.cc/en/Main/ArduinoBoardNano?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - ``nanoatmega328new``
      - `Arduino Nano ATmega328 (New Bootloader) <https://www.arduino.cc/en/Main/ArduinoBoardNano?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - ``pro16MHzatmega168``
      - `Arduino Pro or Pro Mini ATmega168 (5V, 16 MHz) <http://arduino.cc/en/Main/ArduinoBoardProMini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - ``pro16MHzatmega328``
      - `Arduino Pro or Pro Mini ATmega328 (5V, 16 MHz) <http://arduino.cc/en/Main/ArduinoBoardProMini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - ``pro8MHzatmega168``
      - `Arduino Pro or Pro Mini ATmega168 (3.3V, 8 MHz) <http://arduino.cc/en/Main/ArduinoBoardProMini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168
      - 8MHz
      - 14KB
      - 1KB
    * - ``pro8MHzatmega328``
      - `Arduino Pro or Pro Mini ATmega328 (3.3V, 8 MHz) <http://arduino.cc/en/Main/ArduinoBoardProMini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - ``robotControl``
      - `Arduino Robot Control <https://www.arduino.cc/en/Main/Robot?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``robotMotor``
      - `Arduino Robot Motor <https://www.arduino.cc/en/Main/Robot?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``tian``
      - `Arduino Tian <https://www.arduino.cc/en/Main/ArduinoBoardTian?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``uno``
      - `Arduino Uno <https://www.arduino.cc/en/Main/ArduinoBoardUno?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``yun``
      - `Arduino Yun <https://www.arduino.cc/en/Main/ArduinoBoardYun?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``yunmini``
      - `Arduino Yun Mini <https://www.arduino.cc/en/Main/ArduinoBoardYunMini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``zero``
      - `Arduino Zero (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``zeroUSB``
      - `Arduino Zero (USB Native Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

Atmel
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
    * - ``attiny13``
      - `Generic ATTiny13 <http://www.atmel.com/devices/ATTINY13.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY13
      - 9MHz
      - 1KB
      - 64B
    * - ``attiny1634``
      - `Generic ATTiny1634 <http://www.atmel.com/devices/ATTINY1634.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY1634
      - 8MHz
      - 16KB
      - 1KB
    * - ``attiny167``
      - `Generic ATTiny167 <http://www.atmel.com/devices/ATTINY167.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY167
      - 8MHz
      - 16KB
      - 512B
    * - ``attiny2313``
      - `Generic ATTiny2313 <http://www.microchip.com/wwwproducts/en/ATTINY2313?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY2313
      - 8MHz
      - 2KB
      - 128B
    * - ``attiny24``
      - `Generic ATTiny24 <http://www.atmel.com/devices/ATTINY24.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY24
      - 8MHz
      - 2KB
      - 128B
    * - ``attiny25``
      - `Generic ATTiny25 <http://www.atmel.com/devices/ATTINY25.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY25
      - 8MHz
      - 2KB
      - 128B
    * - ``attiny261``
      - `Generic ATTiny261 <http://www.atmel.com/devices/ATTINY261.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY261
      - 8MHz
      - 2KB
      - 128B
    * - ``attiny4313``
      - `Generic ATTiny4313 <http://www.microchip.com/wwwproducts/en/ATTINY4313?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY4313
      - 8MHz
      - 4KB
      - 256B
    * - ``attiny44``
      - `Generic ATTiny44 <http://www.atmel.com/devices/ATTINY44.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY44
      - 8MHz
      - 4KB
      - 256B
    * - ``attiny441``
      - `Generic ATTiny441 <http://www.atmel.com/devices/ATTINY441.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY441
      - 8MHz
      - 4KB
      - 256B
    * - ``attiny45``
      - `Generic ATTiny45 <http://www.atmel.com/devices/ATTINY45.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY45
      - 8MHz
      - 4KB
      - 256B
    * - ``attiny461``
      - `Generic ATTiny461 <http://www.atmel.com/devices/ATTINY461.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY461
      - 8MHz
      - 4KB
      - 256B
    * - ``attiny48``
      - `Generic ATTiny48 <http://www.atmel.com/devices/ATTINY48.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY48
      - 8MHz
      - 4KB
      - 256B
    * - ``attiny828``
      - `Generic ATTiny828 <http://www.atmel.com/devices/ATTINY828.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY828
      - 8MHz
      - 8KB
      - 512B
    * - ``attiny84``
      - `Generic ATTiny84 <http://www.atmel.com/devices/ATTINY84.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY84
      - 8MHz
      - 8KB
      - 512B
    * - ``attiny841``
      - `Generic ATTiny841 <http://www.atmel.com/devices/ATTINY841.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY841
      - 8MHz
      - 8KB
      - 512B
    * - ``attiny85``
      - `Generic ATTiny85 <http://www.atmel.com/devices/ATTINY85.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - ``attiny861``
      - `Generic ATTiny861 <http://www.atmel.com/devices/ATTINY861.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY861
      - 8MHz
      - 8KB
      - 512B
    * - ``attiny87``
      - `Generic ATTiny87 <http://www.atmel.com/devices/ATTINY87.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY87
      - 8MHz
      - 8KB
      - 512B
    * - ``attiny88``
      - `Generic ATTiny88 <http://www.atmel.com/devices/ATTINY88.aspx?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY88
      - 8MHz
      - 8KB
      - 512B
    * - ``samd21g18a``
      - `Atmel ATSAMW25-XPRO <https://developer.mbed.org/platforms/SAMW25-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``usbasp``
      - `USBasp stick <https://www.fischl.de/usbasp/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA8
      - 12MHz
      - 8KB
      - 1KB

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
      - 16MHz
      - 256KB
      - 16KB

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
      - 16MHz
      - 28KB
      - 2KB

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
      - 16MHz
      - 30KB
      - 2KB

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
      - 32MHz
      - 256KB
      - 32KB

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
      - 16MHz
      - 248KB
      - 8KB
    * - ``controllino_maxi_automation``
      - `Controllino Maxi Automation <https://controllino.biz/controllino/maxi-automation/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - ``controllino_mega``
      - `Controllino Mega <https://controllino.biz/controllino/mega/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - ``controllino_mini``
      - `Controllino Mini <https://controllino.biz/controllino/mini/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

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
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
      - 64MHz
      - 512KB
      - 64KB

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
      - 80MHz
      - 4MB
      - 80KB

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
      - 80MHz
      - 508KB
      - 32KB
    * - ``cerebot32mx7``
      - `Digilent Cerebot 32MX7 <http://www.microchip.com/Developmenttools/ProductDetails.aspx?PartNO=TDGL004&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB
    * - ``chipkit_cmod``
      - `Digilent chipKIT Cmod <http://store.digilentinc.com/chipkit-cmod-breadboardable-mz-microcontroller-board/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX150F128D
      - 40MHz
      - 124KB
      - 32KB
    * - ``chipkit_dp32``
      - `Digilent chipKIT DP32 <http://store.digilentinc.com/chipkit-dp32-dip-package-prototyping-microcontroller-board/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX250F128B
      - 40MHz
      - 120KB
      - 32KB
    * - ``chipkit_mx3``
      - `Digilent chipKIT MX3 <http://store.digilentinc.com/chipkit-mx3-microcontroller-board-with-pmod-headers/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX320F128H
      - 80MHz
      - 124KB
      - 16KB
    * - ``chipkit_pro_mx4``
      - `Digilent chipKIT Pro MX4 <http://store.digilentinc.com/chipkit-pro-mx4-embedded-systems-trainer-board/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX460F512L
      - 80MHz
      - 508KB
      - 32KB
    * - ``chipkit_pro_mx7``
      - `Digilent chipKIT Pro MX7 <http://store.digilentinc.com/chipkit-pro-mx7-advanced-peripherals-embedded-systems-trainer-board/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB
    * - ``chipkit_uc32``
      - `Digilent chipKIT uC32 <http://store.digilentinc.com/chipkit-uc32-basic-microcontroller-board-with-uno-r3-headers/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX340F512H
      - 80MHz
      - 508KB
      - 32KB
    * - ``chipkit_wf32``
      - `Digilent chipKIT WF32 <http://store.digilentinc.com/chipkit-wf32-wifi-enabled-microntroller-board-with-uno-r3-headers/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX695F512L
      - 80MHz
      - 508KB
      - 128KB
    * - ``chipkit_wifire``
      - `Digilent chipKIT WiFire <http://store.digilentinc.com/chipkit-wi-fire-wifi-enabled-mz-microcontroller-board/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MZ2048ECG100
      - 200MHz
      - 1.98MB
      - 512KB
    * - ``mega_pic32``
      - `Digilent chipKIT MAX32 <http://store.digilentinc.com/chipkit-max32-microcontroller-board-with-mega-r3-headers/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB
    * - ``openscope``
      - `Digilent OpenScope <http://store.digilentinc.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MZ2048EFG124
      - 200MHz
      - 1.98MB
      - 512KB
    * - ``uno_pic32``
      - `Digilent chipKIT UNO32 <http://store.digilentinc.com/chipkit-uno32-basic-microcontroller-board-retired-see-chipkit-uc32/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX320F128H
      - 80MHz
      - 124KB
      - 16KB

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
      - 16MHz
      - 14.50KB
      - 512B
    * - ``digispark-pro32``
      - `Digispark Pro (32 byte buffer) <http://digistump.com/products/109?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY167
      - 16MHz
      - 14.50KB
      - 512B
    * - ``digispark-pro64``
      - `Digispark Pro (16 MHz) (64 byte buffer) <http://digistump.com/products/109?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY167
      - 16MHz
      - 14.50KB
      - 512B
    * - ``digispark-tiny``
      - `Digispark USB <http://digistump.com/products/1?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATTINY85
      - 16MHz
      - 5.87KB
      - 512B
    * - ``digix``
      - `Digistump DigiX <http://digistump.com/products/50?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB

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
      - 80MHz
      - 4MB
      - 80KB

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
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
      - 16MHz
      - 60KB
      - 2KB

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
      - 80MHz
      - 4MB
      - 80KB
    * - ``espectro32``
      - `ESPectro32 <https://shop.makestro.com/product/espectro32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
      - 80MHz
      - 4MB
      - 80KB
    * - ``espresso_lite_v2``
      - `ESPresso Lite 2.0 <http://www.espert.co?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

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
      - 80MHz
      - 4MB
      - 80KB

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
      - 240MHz
      - 4MB
      - 320KB

Electronut Labs
~~~~~~~~~~~~~~~

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
    * - ``bluey``
      - `Bluey nRF52832 IoT <https://electronut.in/portfolio/bluey/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``hackaBLE``
      - `hackaBLE <https://electronut.in/portfolio/hackaBLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

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
      - 16MHz
      - 31.50KB
      - 2KB

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
      - 8MHz
      - 28KB
      - 2.50KB

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
      - 8MHz
      - 127KB
      - 16KB

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
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp01``
      - `Espressif Generic ESP8266 ESP-01 512k <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 512KB
      - 80KB
    * - ``esp01_1m``
      - `Espressif Generic ESP8266 ESP-01 1M <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - ``esp07``
      - `Espressif Generic ESP8266 ESP-07 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs#esp-07>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - ``esp12e``
      - `Espressif ESP8266 ESP-12E <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - ``esp32dev``
      - `Espressif ESP32 Dev Module <https://en.wikipedia.org/wiki/ESP32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp8285``
      - `Generic ESP8285 Module <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 423.98KB
      - 80KB
    * - ``esp_wroom_02``
      - `ESP-WROOM-02 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 2MB
      - 80KB
    * - ``phoenix_v1``
      - `Phoenix 1.0 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - ``phoenix_v2``
      - `Phoenix 2.0 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - ``pico32``
      - `ESP32 Pico Kit <http://esp-idf.readthedocs.io/en/latest/get-started/get-started-pico-kit.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``wifinfo``
      - `WifInfo <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB

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
      - 48MHz
      - 120KB
      - 32KB
    * - ``fubarino_sd``
      - `Fubarino SD (1.5) <http://fubarino.org/sd/index.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX795F512H
      - 80MHz
      - 508KB
      - 128KB

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
      - 72MHz
      - 64KB
      - 20KB
    * - ``genericSTM32F103C8``
      - `STM32F103C8 (20k RAM. 64k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``genericSTM32F103CB``
      - `STM32F103CB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103cb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103CBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``genericSTM32F103R8``
      - `STM32F103R8 (20k RAM. 64 Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103r8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103R8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``genericSTM32F103RB``
      - `STM32F103RB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``genericSTM32F103RC``
      - `STM32F103RC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rc.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``genericSTM32F103RE``
      - `STM32F103RE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103re.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``genericSTM32F103T8``
      - `STM32F103T8 (20k RAM. 64k Flash) <http://www.st.com/en/microcontrollers/stm32f103t8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103T8T6
      - 72MHz
      - 20KB
      - 64KB
    * - ``genericSTM32F103TB``
      - `STM32F103TB (20k RAM. 128k Flash) <http://www.st.com/en/microcontrollers/stm32f103tb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103TBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``genericSTM32F103VB``
      - `STM32F103VB (20k RAM. 128k Flash) <http://www.st.com/en/microcontrollers/stm32f103vb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103VBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``genericSTM32F103VC``
      - `STM32F103VC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``genericSTM32F103VD``
      - `STM32F103VD (64k RAM. 384k Flash) <http://www.st.com/en/microcontrollers/stm32f103vd.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103VDT6
      - 72MHz
      - 384KB
      - 64KB
    * - ``genericSTM32F103VE``
      - `STM32F103VE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103VET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``genericSTM32F103ZC``
      - `STM32F103ZC (48k RAM. 256k Flash) <http://www.st.com/en/microcontrollers/stm32f103zc.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103ZCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``genericSTM32F103ZD``
      - `STM32F103ZD (64k RAM. 384k Flash) <http://www.st.com/en/microcontrollers/stm32f103zd.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103ZDT6
      - 72MHz
      - 384KB
      - 64KB
    * - ``genericSTM32F103ZE``
      - `STM32F103ZE (64k RAM. 512k Flash) <http://www.st.com/en/microcontrollers/stm32f103ze.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``genericSTM32F407VET6``
      - `STM32F407VE (192k RAM. 512k Flash) <http://www.st.com/en/microcontrollers/stm32f407ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F407VET6
      - 168MHz
      - 502.23KB
      - 128KB

Hardkernel
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
    * - ``odroid_esp32``
      - `ODROID-GO <https://www.hardkernel.com/main/products/prdt_info.php?g_code=G152875062626&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

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
      - 80MHz
      - 4MB
      - 80KB

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
      - 240MHz
      - 4MB
      - 320KB
    * - ``heltec_wifi_lora_32``
      - `Heltec WIFI LoRa 32 <http://www.heltec.cn?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``hornbill32minima``
      - `Hornbill ESP32 Minima <https://hackaday.io/project/18997-hornbill?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Infineon
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
    * - ``xmc1100_boot_kit``
      - `XMC1100 Boot Kit <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`Yes <piodebug>`
      - XMC1100
      - 32MHz
      - 64KB
      - 64KB
    * - ``xmc1100_h_bridge2go``
      - `XMC1100 H-Bridge 2Go <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`Yes <piodebug>`
      - XMC1100
      - 32MHz
      - 64KB
      - 64KB
    * - ``xmc1100_xmc2go``
      - `XMC1100 XMC2Go <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`Yes <piodebug>`
      - XMC1100
      - 32MHz
      - 64KB
      - 64KB
    * - ``xmc1300_boot_kit``
      - `XMC1300 Boot Kit <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`Yes <piodebug>`
      - XMC1300
      - 32MHz
      - 64KB
      - 64KB
    * - ``xmc1300_sense2gol``
      - `XMC1300 Sense2GoL <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`Yes <piodebug>`
      - XMC1300
      - 32MHz
      - 64KB
      - 122.23KB
    * - ``xmc4200_distance2go``
      - `XMC4200 Distance2Go <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`Yes <piodebug>`
      - XMC4200
      - 80MHz
      - 250KB
      - 256KB
    * - ``xmc4700_relax_kit``
      - `XMC4700 Relax Kit <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`Yes <piodebug>`
      - XMC4700
      - 144MHz
      - 2.00MB
      - 1.95MB

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
      - 32MHz
      - 152KB
      - 80KB

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
      - 240MHz
      - 4MB
      - 320KB

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
      - 72MHz
      - 108KB
      - 17KB
    * - ``maple_mini_b20``
      - `Maple Mini Bootloader 2.0 <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103CBT6
      - 72MHz
      - 120KB
      - 20KB
    * - ``maple_mini_origin``
      - `Maple Mini Original <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103CBT6
      - 72MHz
      - 108KB
      - 17KB
    * - ``maple_ret6``
      - `Maple (RET6) <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RET6
      - 72MHz
      - 256KB
      - 48KB

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
      - 8MHz
      - 28KB
      - 2.50KB

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
      - 16MHz
      - 28KB
      - 2.50KB

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
      - 16MHz
      - 31KB
      - 2KB
    * - ``moteino``
      - `LowPowerLab Moteino <https://lowpowerlab.com/shop/moteino-r4?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``moteino_zero``
      - `Moteino M0 <https://lowpowerlab.com/shop/product/184?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``moteinomega``
      - `LowPowerLab MoteinoMEGA <http://lowpowerlab.com/blog/2014/08/09/moteinomega-available-now/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB

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
      - 240MHz
      - 4MB
      - 320KB
    * - ``m5stack-fire``
      - `M5Stack FIRE <http://www.m5stack.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

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
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``mhetesp32minikit``
      - `MH ET LIVE ESP32MiniKit <http://forum.mhetlive.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
      - 100MHz
      - 1MB
      - 256KB

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
      - :ref:`Yes <piodebug>`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB

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
      - 240MHz
      - 4MB
      - 320KB

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
      - 16MHz
      - 127KB
      - 16KB
    * - ``mightycore16``
      - `MightyCore ATmega16 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA16
      - 16MHz
      - 15.50KB
      - 1KB
    * - ``mightycore164``
      - `MightyCore ATmega164 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA164P
      - 16MHz
      - 15.50KB
      - 1KB
    * - ``mightycore32``
      - `MightyCore ATmega32 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``mightycore324``
      - `MightyCore ATmega324 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA324P
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``mightycore644``
      - `MightyCore ATmega644 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - ``mightycore8535``
      - `MightyCore ATmega8535 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA16
      - 16MHz
      - 7.50KB
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
      - 8MHz
      - 28KB
      - 2.50KB

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
      - 16MHz
      - 127KB
      - 16KB
    * - ``1284p8m``
      - `Microduino Core+ (ATmega1284P@8M,3.3V) <http://wiki.microduinoinc.com/Microduino-Module_Core%2B?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - ``168pa16m``
      - `Microduino Core (Atmega168PA@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_Core?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168P
      - 16MHz
      - 15.50KB
      - 1KB
    * - ``168pa8m``
      - `Microduino Core (Atmega168PA@8M,3.3V) <http://wiki.microduinoinc.com/Microduino-Module_Core?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA168P
      - 8MHz
      - 15.50KB
      - 1KB
    * - ``328p16m``
      - `Microduino Core (Atmega328P@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_Core?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``328p8m``
      - `Microduino Core (Atmega328P@8M,3.3V) <http://wiki.microduinoinc.com/Microduino-Module_Core?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - ``32u416m``
      - `Microduino Core USB (ATmega32U4@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_CoreUSB?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``644pa16m``
      - `Microduino Core+ (Atmega644PA@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_Core%2B?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - ``644pa8m``
      - `Microduino Core+ (Atmega644PA@8M,3.3V) <http://wiki.microduinoinc.com/Microduino-Module_Core%2B?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA644P
      - 8MHz
      - 63KB
      - 4KB
    * - ``microduino-core-esp32``
      - `Microduino Core ESP32 <https://microduinoinc.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``microduino32_flash``
      - `Microduino Core STM32 to Flash <http://wiki.microduinoinc.com/Microduino-Module_CoreSTM32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103CBT6
      - 72MHz
      - 105.47KB
      - 16.60KB

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
      - 80MHz
      - 508KB
      - 32KB
    * - ``flipnclickmz``
      - `MikroElektronika Flip N Click MZ <https://shop.mikroe.com/flipclick-pic32mz?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MZ2048EFH100
      - 252MHz
      - 1.98MB
      - 512KB

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
      - 80MHz
      - 4MB
      - 80KB
    * - ``nodemcu-32s``
      - `NodeMCU-32S <http://www.nodemcu.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``nodemcuv2``
      - `NodeMCU 1.0 (ESP-12E Module) <http://www.nodemcu.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

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
      - 240MHz
      - 16MB
      - 320KB

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
      - 32MHz
      - 256KB
      - 32KB
    * - ``nrf51_dongle``
      - `Nordic nRF51-Dongle <https://developer.mbed.org/platforms/Nordic-nRF51-Dongle/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``nrf52840_dk``
      - `Nordic nRF52840-DK <https://os.mbed.com/platforms/Nordic-nRF52840-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - ``nrf52_dk``
      - `Nordic nRF52-DK <https://developer.mbed.org/platforms/Nordic-nRF52-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

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
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32-gateway``
      - `OLIMEX ESP32-GATEWAY <https://www.olimex.com/Products/IoT/ESP32-GATEWAY/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
      - 32MHz
      - 256KB
      - 32KB

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
      - 80MHz
      - 2MB
      - 80KB
    * - ``pinguino32``
      - `Olimex PIC32-PINGUINO <https://www.olimex.com/Products/Duino/PIC32/PIC32-PINGUINO/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX440F256H
      - 80MHz
      - 252KB
      - 32KB

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
      - 240MHz
      - 4MB
      - 320KB

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
      - 40MHz
      - 120KB
      - 32KB

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
      - 16MHz
      - 30KB
      - 2KB

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
      - 80MHz
      - 508KB
      - 32KB

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
      - 8MHz
      - 31.50KB
      - 2KB
    * - ``panStampNRG``
      - `PanStamp NRG 1.1 <http://www.panstamp.com/product/197/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - No
      - CC430F5137
      - 12MHz
      - 31.88KB
      - 4KB

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
      - 16MHz
      - 248KB
      - 32KB

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
      - 16MHz
      - 28KB
      - 2.50KB

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
      - 200MHz
      - 1.98MB
      - 512KB
    * - ``quick240_usb``
      - `Pontech Quick240 <http://chipkit.net/wpcproduct/pontech-quick240/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB

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
      - 8MHz
      - 31.50KB
      - 2KB
    * - ``lightblue-beanplus``
      - `LightBlue Bean+ <https://punchthrough.com/bean?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

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
      - 8MHz
      - 28KB
      - 2.50KB

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
      - 16MHz
      - 128KB
      - 8KB

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
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``blendmicro16``
      - `RedBearLab Blend Micro 3.3V/16MHz (overclock) <http://redbearlab.com/blendmicro/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``blendmicro8``
      - `RedBearLab Blend Micro 3.3V/8MHz <http://redbearlab.com/blendmicro/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``redBearLab``
      - `RedBearLab nRF51822 <https://developer.mbed.org/platforms/RedBearLab-nRF51822/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``redBearLabBLENano``
      - `RedBearLab BLE Nano 1.5 <https://developer.mbed.org/platforms/RedBearLab-BLE-Nano/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB
    * - ``redbear_blenano2``
      - `RedBearLab BLE Nano 2 <https://redbear.cc/product/ble-nano-2-soldered.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``redbear_blend2``
      - `RedBearLab Blend 2 <https://redbear.cc/product/ble/blend-2.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

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
      - 16MHz
      - 252KB
      - 8KB

RoboticsBrno
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
    * - ``alksesp32``
      - `ALKS ESP32 <https://github.com/RoboticsBrno/ArduinoLearningKitStarter.git?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
      - :ref:`Yes <piodebug>`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sodaq_explorer``
      - `SODAQ ExpLoRer <http://support.sodaq.com/sodaq-one/explorer/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sodaq_galora``
      - `SODAQ GaLoRa <http://support.sodaq.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - ``sodaq_mbili``
      - `SODAQ Mbili <http://support.sodaq.com/sodaq-one/sodaq-mbili-1284p/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - ``sodaq_moja``
      - `SODAQ Moja <http://support.sodaq.com/sodaq-one/moja/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - ``sodaq_ndogo``
      - `SODAQ Ndogo <http://support.sodaq.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - ``sodaq_one``
      - `SODAQ ONE <http://support.sodaq.com/sodaq-one/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sodaq_tatu``
      - `SODAQ Tatu <http://support.sodaq.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB

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
    * - ``disco_f407vg``
      - `ST STM32F4DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF252419?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F407VGT6
      - 168MHz
      - 1MB
      - 128KB
    * - ``nucleo_f103rb``
      - `ST Nucleo F103RB <https://developer.mbed.org/platforms/ST-Nucleo-F103RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB

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
      - :ref:`Yes <piodebug>`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - ``sainSmartDueUSB``
      - `SainSmart Due (USB Native Port) <http://www.sainsmart.com/arduino/control-boards/sainsmart-due-atmel-sam3x8e-arm-cortex-m3-board-black.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB

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
      - `Sanguino ATmega1284p (8MHz) <https://github.com/Lauszus/Sanguino?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - ``sanguino_atmega1284p``
      - `Sanguino ATmega1284p (16MHz) <https://github.com/Lauszus/Sanguino?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - ``sanguino_atmega644``
      - `Sanguino ATmega644 or ATmega644A (16 MHz) <https://github.com/Lauszus/Sanguino?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA644
      - 16MHz
      - 63KB
      - 4KB
    * - ``sanguino_atmega644_8m``
      - `Sanguino ATmega644 or ATmega644A (8 MHz) <https://github.com/Lauszus/Sanguino?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA644
      - 8MHz
      - 63KB
      - 4KB
    * - ``sanguino_atmega644p``
      - `Sanguino ATmega644P or ATmega644PA (16 MHz) <https://github.com/Lauszus/Sanguino?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - ``sanguino_atmega644p_8m``
      - `Sanguino ATmega644P or ATmega644PA (8 MHz) <https://github.com/Lauszus/Sanguino?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA644P
      - 8MHz
      - 63KB
      - 4KB

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
      - 80MHz
      - 508KB
      - 128KB
    * - ``seeedTinyBLE``
      - `Seeed Tiny BLE <http://developer.mbed.org/platforms/Seeed-Tiny-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``seeeduino``
      - `Seeeduino <https://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``wio_link``
      - `Wio Link <https://www.seeedstudio.com/Wio-Link-p-2604.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - ``wio_node``
      - `Wio Node <https://www.seeedstudio.com/Wio-Node-p-2637.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

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
      - 80MHz
      - 4MB
      - 80KB
    * - ``sparkfun_digitalsandbox``
      - `SparkFun Digital Sandbox <https://www.sparkfun.com/products/12651?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - ``sparkfun_fiov3``
      - `SparkFun Fio V3 3.3V/8MHz <https://www.sparkfun.com/products/11520?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``sparkfun_makeymakey``
      - `SparkFun Makey Makey <https://www.sparkfun.com/products/11511?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``sparkfun_megamini``
      - `SparkFun Mega Pro Mini 3.3V <https://www.sparkfun.com/products/10743?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA2560
      - 8MHz
      - 252KB
      - 8KB
    * - ``sparkfun_megapro16MHz``
      - `SparkFun Mega Pro 5V/16MHz <https://www.sparkfun.com/products/11007?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - ``sparkfun_megapro8MHz``
      - `SparkFun Mega Pro 3.3V/8MHz <https://www.sparkfun.com/products/10744?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA2560
      - 8MHz
      - 252KB
      - 8KB
    * - ``sparkfun_promicro16``
      - `SparkFun Pro Micro 5V/16MHz <https://www.sparkfun.com/products/12640?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``sparkfun_promicro8``
      - `SparkFun Pro Micro 3.3V/8MHz <https://www.sparkfun.com/products/12587?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``sparkfun_qduinomini``
      - `SparkFun Qduino Mini <https://www.sparkfun.com/products/13614?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``sparkfun_redboard``
      - `SparkFun RedBoard <https://www.sparkfun.com/products/12757?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``sparkfun_samd21_dev_usb``
      - `SparkFun SAMD21 Dev Breakout <https://www.sparkfun.com/products/13672?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sparkfun_samd21_mini_usb``
      - `SparkFun SAMD21 Mini Breakout <https://www.sparkfun.com/products/13664?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sparkfun_satmega128rfa1``
      - `SparkFun ATmega128RFA1 Dev Board <https://www.sparkfun.com/products/11197?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA128RFA1
      - 16MHz
      - 16KB
      - 124KB
    * - ``sparkfun_serial7seg``
      - `SparkFun Serial 7-Segment Display <https://www.sparkfun.com/products/11441?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - ``thing``
      - `SparkFun ESP8266 Thing <https://www.sparkfun.com/products/13231?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 512KB
      - 80KB
    * - ``thingdev``
      - `SparkFun ESP8266 Thing Dev <https://www.sparkfun.com/products/13231?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 512KB
      - 80KB
    * - ``uview``
      - `SparkFun MicroView <https://www.sparkfun.com/products/12923?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

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
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
      - 8MHz
      - 30KB
      - 2KB

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
      - 80MHz
      - 4MB
      - 80KB

TTGO
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
    * - ``ttgo-lora32-v1``
      - `TTGO LoRa32-OLED V1 <https://www.google.com.ua/search?q=TTGO+LoRa32-OLED+V1&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
      - 64MHz
      - 512KB
      - 64KB

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
      - 16MHz
      - 31.50KB
      - 2.50KB
    * - ``teensy20pp``
      - `Teensy++ 2.0 <https://www.pjrc.com/store/teensypp.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - No
      - AT90USB1286
      - 16MHz
      - 127KB
      - 8KB
    * - ``teensy30``
      - `Teensy 3.0 <https://www.pjrc.com/store/teensy3.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - No
      - MK20DX128
      - 48MHz
      - 128KB
      - 16KB
    * - ``teensy31``
      - `Teensy 3.1 / 3.2 <https://www.pjrc.com/store/teensy31.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`Yes <piodebug>`
      - MK20DX256
      - 72MHz
      - 256KB
      - 64KB
    * - ``teensy35``
      - `Teensy 3.5 <https://www.pjrc.com/store/teensy35.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`Yes <piodebug>`
      - MK64FX512
      - 120MHz
      - 512KB
      - 192KB
    * - ``teensy36``
      - `Teensy 3.6 <https://www.pjrc.com/store/teensy36.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`Yes <piodebug>`
      - MK66FX1M0
      - 180MHz
      - 1MB
      - 256KB
    * - ``teensylc``
      - `Teensy LC <http://www.pjrc.com/teensy/teensyLC.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`Yes <piodebug>`
      - MKL26Z64
      - 48MHz
      - 62KB
      - 8KB

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
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``espinotee``
      - `ThaiEasyElec ESPino <http://www.thaieasyelec.com/products/wireless-modules/wifi-modules/espino-wifi-development-board-detail.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

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
      - 16MHz
      - 28KB
      - 2.50KB

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
      - 8MHz
      - 30KB
      - 2KB
    * - ``tinylily``
      - `TinyCircuits TinyLily Mini Processor <https://tiny-circuits.com/tiny-lily-mini-processor.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB

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
      - 80MHz
      - 508KB
      - 32KB
    * - ``ubw32_mx795``
      - `UBW32 MX795 <http://www.schmalzhaus.com/UBW32/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB

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
      - 80MHz
      - 4MB
      - 80KB
    * - ``d1_mini``
      - `WeMos D1 R2 & mini <https://wiki.wemos.cc/products:d1:d1_mini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - ``d1_mini_lite``
      - `WeMos D1 mini Lite <https://wiki.wemos.cc/products:d1:d1_mini_lite?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - ``d1_mini_pro``
      - `WeMos D1 mini Pro <https://wiki.wemos.cc/products:d1:d1_mini?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 16MB
      - 80KB
    * - ``lolin32``
      - `WEMOS LOLIN32 <https://wiki.wemos.cc/products:lolin32:lolin32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin_d32``
      - `WEMOS LOLIN D32 <https://wiki.wemos.cc/products:d32:d32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin_d32_pro``
      - `WEMOS LOLIN D32 PRO <https://wiki.wemos.cc/products:d32:d32_pro?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``wemosbat``
      - `WeMos WiFi & Bluetooth Battery <https://www.wemos.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
      - 32MHz
      - 256KB
      - 32KB

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
      - 16MHz
      - 120.00KB
      - 16KB
    * - ``wildfirev3``
      - `Wicked Device WildFire V3 <http://shop.wickeddevice.com/resources/wildfire/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB

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
      - 240MHz
      - 16MB
      - 320KB

WifiDuino
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
    * - ``wifiduino``
      - `WiFiduino <https://www.facebook.com/WifiDuino/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

XinaBox
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
    * - ``xinabox_cw01``
      - `XinaBox CW01 <https://xinabox.cc/products/cw01?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - ``xinabox_cw02``
      - `XinaBox CW02 <https://xinabox.cc/products/cw02?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
      - 40MHz
      - 120KB
      - 32KB

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
      - 40MHz
      - 120KB
      - 32KB

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
      - 16MHz
      - 248KB
      - 32KB

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
      - 32MHz
      - 256KB
      - 32KB

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
      - 8MHz
      - 8KB
      - 1KB
    * - ``nibo2``
      - `nicai-systems NIBO 2 robot <http://www.nicai-systems.com/en/nibo2?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA128
      - 16MHz
      - 128KB
      - 4KB
    * - ``nibobee``
      - `nicai-systems NIBObee robot <http://www.nicai-systems.com/en/nibobee?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA16
      - 15MHz
      - 16KB
      - 1KB
    * - ``nibobee_1284``
      - `nicai-systems NIBObee robot with Tuning Kit <http://www.nicai-systems.com/en/nibobee?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 20MHz
      - 128KB
      - 16KB
    * - ``niboburger``
      - `nicai-systems NIBO burger robot <http://www.nicai-systems.com/en/nibo-burger?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA16
      - 15MHz
      - 16KB
      - 1KB
    * - ``niboburger_1284``
      - `nicai-systems NIBO burger robot with Tuning Kit <http://www.nicai-systems.com/en/nibo-burger?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - ATMEGA1284P
      - 20MHz
      - 128KB
      - 16KB

sino:bit
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
    * - ``Sinobit``
      - `Sino:Bit <https://github.com/sinobitorg/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

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
      - 240MHz
      - 2MB
      - 320KB
    * - ``ublox_evk_nina_b1``
      - `u-blox EVK-NINA-B1 <https://os.mbed.com/platforms/u-blox-EVK-NINA-B1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

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
      - 16MHz
      - 31.50KB
      - 2KB
