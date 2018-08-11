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

.. _debugging_tool_atmel-ice:

Atmel-ICE
=========

:Configuration:
  :ref:`projectconf_debug_tool` = ``atmel-ice``

.. image:: ../../_static/debug_probes/atmel-ice.jpg
  :target: https://www.microchip.com/DevelopmentTools/ProductDetails/PartNo/atatmel-ice?PartNO=atatmel-ice&utm_source=platformio&utm_medium=docs

Atmel-ICE is a powerful development tool for debugging and programming ARM®
Cortex®-M based SAM and AVR microcontrollers with on-chip debug capability.
`Vendor information... <https://www.microchip.com/DevelopmentTools/ProductDetails/PartNo/atatmel-ice?PartNO=atatmel-ice&utm_source=platformio&utm_medium=docs>`__

.. contents:: Contents
    :local:
    :depth: 1

Drivers
-------

:Windows:
  When installing the Atmel-ICE on a computer running Microsoft Windows,
  the USB driver is loaded when the Atmel-ICE is first plugged in.

:Mac:
  Not required.

:Linux:
  Please install "udev" rules :ref:`faq_udev_rules`. If you already installed
  them before, please check that your rules are up-to-date or repeat steps.

.. begin_platforms

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_atmelsam`
      - Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

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

    * - :ref:`framework_simba`
      - Simba is an RTOS and build framework. It aims to make embedded programming easy and portable.

Boards
------

.. note::
    For more detailed ``board`` information please scroll tables below by horizontal.


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
    * - ``mzeropro``
      - `Arduino M0 Pro (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardM0PRO?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
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
    * - ``samd21_xpro``
      - `Atmel SAMD21-XPRO <https://developer.mbed.org/platforms/SAMD21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``samd21g18a``
      - `Atmel ATSAMW25-XPRO <https://developer.mbed.org/platforms/SAMW25-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``saml21_xpro_b``
      - `Atmel SAML21-XPRO-B <https://developer.mbed.org/platforms/SAML21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAML21J18B
      - 48MHz
      - 256KB
      - 32KB
    * - ``samr21_xpro``
      - `Atmel ATSAMR21-XPRO <https://developer.mbed.org/platforms/SAMR21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMR21G18A
      - 48MHz
      - 256KB
      - 32KB
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
    * - ``tian``
      - `Arduino Tian <https://www.arduino.cc/en/Main/ArduinoBoardTian?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``zero``
      - `Arduino Zero (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``zeroUSB``
      - `Arduino Zero (USB Native Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
