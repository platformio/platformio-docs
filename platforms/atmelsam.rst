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

.. _platform_atmelsam:

Atmel SAM
=========
:ref:`projectconf_env_platform` = ``atmelsam``

Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

For more detailed information please visit `vendor site <http://www.atmel.com/products/microcontrollers/arm/default.aspx?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Atmel SAM development platform repository <https://github.com/platformio/platform-atmelsam/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_:

* `arduino-blink <https://github.com/platformio/platform-atmelsam/tree/develop/examples/arduino-blink?utm_source=platformio&utm_medium=docs>`_
* `arduino-external-libs <https://github.com/platformio/platform-atmelsam/tree/develop/examples/arduino-external-libs?utm_source=platformio&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-atmelsam/tree/develop/examples/arduino-internal-libs?utm_source=platformio&utm_medium=docs>`_
* `arduino-web-thing-led <https://github.com/platformio/platform-atmelsam/tree/develop/examples/arduino-web-thing-led?utm_source=platformio&utm_medium=docs>`_
* `mbed-blink <https://github.com/platformio/platform-atmelsam/tree/develop/examples/mbed-blink?utm_source=platformio&utm_medium=docs>`_
* `mbed-dsp <https://github.com/platformio/platform-atmelsam/tree/develop/examples/mbed-dsp?utm_source=platformio&utm_medium=docs>`_
* `mbed-events <https://github.com/platformio/platform-atmelsam/tree/develop/examples/mbed-events?utm_source=platformio&utm_medium=docs>`_
* `mbed-serial <https://github.com/platformio/platform-atmelsam/tree/develop/examples/mbed-serial?utm_source=platformio&utm_medium=docs>`_
* `simba-blink <https://github.com/platformio/platform-atmelsam/tree/develop/examples/simba-blink?utm_source=platformio&utm_medium=docs>`_

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
    * - ``mzeropro``
      - `Arduino M0 Pro (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardM0PRO?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``samd21_xpro``
      - `Atmel SAMD21-XPRO <https://developer.mbed.org/platforms/SAMD21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``samd21g18a``
      - `Atmel ATSAMW25-XPRO <https://developer.mbed.org/platforms/SAMW25-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``saml21_xpro_b``
      - `Atmel SAML21-XPRO-B <https://developer.mbed.org/platforms/SAML21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAML21J18B
      - 48MHz
      - 256KB
      - 32KB
    * - ``samr21_xpro``
      - `Atmel ATSAMR21-XPRO <https://developer.mbed.org/platforms/SAMR21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMR21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``zero``
      - `Arduino Zero (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB


External Debug Tools
~~~~~~~~~~~~~~~~~~~~~

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
    * - ``adafruit_circuitplayground_m0``
      - `Adafruit Circuit Playground Express <https://www.adafruit.com/product/3333?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_feather_m0``
      - `Adafruit Feather M0 <https://www.adafruit.com/product/2772?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_feather_m0_express``
      - `Adafruit Feather M0 Express <https://www.adafruit.com/product/3403?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_gemma_m0``
      - `Adafruit Gemma M0 <https://www.adafruit.com/product/3501?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_metro_m0``
      - `Adafruit Metro M0 Expresss <https://www.adafruit.com/product/3505?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_trinket_m0``
      - `Adafruit Trinket M0 <https://www.adafruit.com/product/3500?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``digix``
      - `Digistump DigiX <http://digistump.com/products/50?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 28KB
    * - ``due``
      - `Arduino Due (Programming Port) <https://www.arduino.cc/en/Main/ArduinoBoardDue?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 32KB
    * - ``dueUSB``
      - `Arduino Due (USB Native Port) <https://www.arduino.cc/en/Main/ArduinoBoardDue?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 32KB
    * - ``macchina2``
      - `Macchina M2 <https://www.macchina.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 32KB
    * - ``mkr1000USB``
      - `Arduino MKR1000 <https://www.arduino.cc/en/Main/ArduinoMKR1000?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrfox1200``
      - `Arduino MKR FOX 1200 <https://www.arduino.cc/en/Main.ArduinoBoardMKRFox1200?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrgsm1400``
      - `Arduino MKR GSM 1400 <https://store.arduino.cc/mkr-gsm-1400?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrwan1300``
      - `Arduino MKR WAN 1300 <https://store.arduino.cc/mkr-wan-1300?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrzero``
      - `Arduino MKRZERO <https://www.arduino.cc/en/Main/ArduinoBoardMKRZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mzeroUSB``
      - `Arduino M0 <https://www.arduino.cc/en/Main/ArduinoBoardM0?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mzeroproUSB``
      - `Arduino M0 Pro (Native USB Port) <https://www.arduino.cc/en/Main/ArduinoBoardM0PRO?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sainSmartDue``
      - `SainSmart Due (Programming Port) <http://www.sainsmart.com/arduino/control-boards/sainsmart-due-atmel-sam3x8e-arm-cortex-m3-board-black.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 32KB
    * - ``sainSmartDueUSB``
      - `SainSmart Due (USB Native Port) <http://www.sainsmart.com/arduino/control-boards/sainsmart-due-atmel-sam3x8e-arm-cortex-m3-board-black.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 32KB
    * - ``sodaq_autonomo``
      - `SODAQ Autonomo <http://support.sodaq.com/sodaq-one/autonomo/getting-started-autonomo/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sodaq_explorer``
      - `SODAQ ExpLoRer <http://support.sodaq.com/sodaq-one/explorer/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sodaq_one``
      - `SODAQ ONE <http://support.sodaq.com/sodaq-one/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sparkfun_samd21_dev_usb``
      - `SparkFun SAMD21 Dev Breakout <https://www.sparkfun.com/products/13672?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sparkfun_samd21_mini_usb``
      - `SparkFun SAMD21 Mini Breakout <https://www.sparkfun.com/products/13664?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``tian``
      - `Arduino Tian <https://www.arduino.cc/en/Main/ArduinoBoardTian?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``zeroUSB``
      - `Arduino Zero (USB Native Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-atmelsam/releases>`__
of Atmel SAM development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = atmelsam
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = atmelsam@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-atmelsam.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinosam <http://arduino.cc/en/Reference/HomePage?utm_source=platformio&utm_medium=docs>`__
      - Arduino Wiring-based Framework (SAM Core, 1.6)

    * - `framework-mbed <http://mbed.org?utm_source=platformio&utm_medium=docs>`__
      - mbed Framework

    * - `framework-simba <https://github.com/eerimoq/simba?utm_source=platformio&utm_medium=docs>`__
      - Simba Framework

    * - `tool-avrdude <http://www.nongnu.org/avrdude/?utm_source=platformio&utm_medium=docs>`__
      - AVRDUDE

    * - `tool-bossac <https://sourceforge.net/projects/b-o-s-s-a/?utm_source=platformio&utm_medium=docs>`__
      - BOSSA CLI

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

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_mbed`
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.

    * - :ref:`framework_simba`
      - Simba is an RTOS and build framework. It aims to make embedded programming easy and portable.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

Adafruit
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
    * - ``adafruit_circuitplayground_m0``
      - `Adafruit Circuit Playground Express <https://www.adafruit.com/product/3333?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_feather_m0``
      - `Adafruit Feather M0 <https://www.adafruit.com/product/2772?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_feather_m0_express``
      - `Adafruit Feather M0 Express <https://www.adafruit.com/product/3403?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_gemma_m0``
      - `Adafruit Gemma M0 <https://www.adafruit.com/product/3501?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_metro_m0``
      - `Adafruit Metro M0 Expresss <https://www.adafruit.com/product/3505?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_trinket_m0``
      - `Adafruit Trinket M0 <https://www.adafruit.com/product/3500?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB

Arduino
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
    * - ``due``
      - `Arduino Due (Programming Port) <https://www.arduino.cc/en/Main/ArduinoBoardDue?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 32KB
    * - ``dueUSB``
      - `Arduino Due (USB Native Port) <https://www.arduino.cc/en/Main/ArduinoBoardDue?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 32KB
    * - ``mkr1000USB``
      - `Arduino MKR1000 <https://www.arduino.cc/en/Main/ArduinoMKR1000?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrfox1200``
      - `Arduino MKR FOX 1200 <https://www.arduino.cc/en/Main.ArduinoBoardMKRFox1200?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrgsm1400``
      - `Arduino MKR GSM 1400 <https://store.arduino.cc/mkr-gsm-1400?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrwan1300``
      - `Arduino MKR WAN 1300 <https://store.arduino.cc/mkr-wan-1300?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrzero``
      - `Arduino MKRZERO <https://www.arduino.cc/en/Main/ArduinoBoardMKRZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mzeroUSB``
      - `Arduino M0 <https://www.arduino.cc/en/Main/ArduinoBoardM0?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mzeropro``
      - `Arduino M0 Pro (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardM0PRO?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mzeroproUSB``
      - `Arduino M0 Pro (Native USB Port) <https://www.arduino.cc/en/Main/ArduinoBoardM0PRO?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``tian``
      - `Arduino Tian <https://www.arduino.cc/en/Main/ArduinoBoardTian?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``zero``
      - `Arduino Zero (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``zeroUSB``
      - `Arduino Zero (USB Native Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero?utm_source=platformio&utm_medium=docs>`_
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``samd21_xpro``
      - `Atmel SAMD21-XPRO <https://developer.mbed.org/platforms/SAMD21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``samd21g18a``
      - `Atmel ATSAMW25-XPRO <https://developer.mbed.org/platforms/SAMW25-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``saml21_xpro_b``
      - `Atmel SAML21-XPRO-B <https://developer.mbed.org/platforms/SAML21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAML21J18B
      - 48MHz
      - 256KB
      - 32KB
    * - ``samr21_xpro``
      - `Atmel ATSAMR21-XPRO <https://developer.mbed.org/platforms/SAMR21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMR21G18A
      - 48MHz
      - 256KB
      - 32KB

Digistump
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
    * - ``digix``
      - `Digistump DigiX <http://digistump.com/products/50?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 28KB

Macchina
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
    * - ``macchina2``
      - `Macchina M2 <https://www.macchina.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 32KB

SODAQ
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
    * - ``sodaq_autonomo``
      - `SODAQ Autonomo <http://support.sodaq.com/sodaq-one/autonomo/getting-started-autonomo/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sodaq_explorer``
      - `SODAQ ExpLoRer <http://support.sodaq.com/sodaq-one/explorer/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sodaq_one``
      - `SODAQ ONE <http://support.sodaq.com/sodaq-one/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

SainSmart
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
    * - ``sainSmartDue``
      - `SainSmart Due (Programming Port) <http://www.sainsmart.com/arduino/control-boards/sainsmart-due-atmel-sam3x8e-arm-cortex-m3-board-black.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 32KB
    * - ``sainSmartDueUSB``
      - `SainSmart Due (USB Native Port) <http://www.sainsmart.com/arduino/control-boards/sainsmart-due-atmel-sam3x8e-arm-cortex-m3-board-black.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 32KB

SparkFun
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
    * - ``sparkfun_samd21_dev_usb``
      - `SparkFun SAMD21 Dev Breakout <https://www.sparkfun.com/products/13672?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sparkfun_samd21_mini_usb``
      - `SparkFun SAMD21 Mini Breakout <https://www.sparkfun.com/products/13664?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
