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

Platform ``atmelsam``
=====================
Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

For more detailed information please visit `vendor site <http://www.atmel.com/products/microcontrollers/arm/default.aspx>`_.

.. contents::

Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinosam <http://arduino.cc/en/Reference/HomePage>`__
      - Arduino Wiring-based Framework (SAM Core, 1.6)

    * - `framework-mbed <http://mbed.org>`__
      - mbed Framework

    * - `framework-simba <https://github.com/eerimoq/simba>`__
      - Simba Framework

    * - `tool-avrdude <http://www.nongnu.org/avrdude/>`__
      - AVRDUDE

    * - `tool-bossac <https://sourceforge.net/projects/b-o-s-s-a/>`__
      - BOSSA CLI

    * - `tool-openocd <http://openocd.org>`__
      - OpenOCD

    * - `toolchain-gccarmnoneeabi <https://launchpad.net/gcc-arm-embedded>`__
      - gcc-arm-embedded

.. warning::
    **Linux Users**:

    * Ubuntu/Debian users may need to add own "username" to the "dialout"
      group if they are not "root", doing this issuing a
      ``sudo usermod -a -G dialout yourusername``.
    * Install "udev" rules file `99-platformio-udev.rules <https://github.com/platformio/platformio-core/blob/develop/scripts/99-platformio-udev.rules>`_
      (an instruction is located in the file).
    * Raspberry Pi users, please read this article
      `Enable serial port on Raspberry Pi <https://hallard.me/enable-serial-port-on-raspberry-pi/>`__.


    **Windows Users:** Please check that you have correctly installed USB
    driver from board manufacturer



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
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

Adafruit
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``adafruit_circuitplayground_m0``
      - `Adafruit Circuit Playground Express <https://www.adafruit.com/product/3000>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <debugging>`
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``adafruit_feather_m0_usb``
      - `Adafruit Feather M0 <https://www.adafruit.com/product/2772>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <debugging>`
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

Arduino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``due``
      - `Arduino Due (Programming Port) <http://www.arduino.org/products/boards/4-arduino-boards/arduino-due>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      -
      - AT91SAM3X8E
      - 84 MHz
      - 512 Kb
      - 32 Kb

    * - ``dueUSB``
      - `Arduino Due (USB Native Port) <http://www.arduino.org/products/boards/4-arduino-boards/arduino-due>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      -
      - AT91SAM3X8E
      - 84 MHz
      - 512 Kb
      - 32 Kb

    * - ``mkr1000USB``
      - `Arduino MKR1000 <https://www.arduino.cc/en/Main/ArduinoMKR1000>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <debugging>`
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``mkrfox1200``
      - `Arduino MKRFox1200 <https://www.arduino.cc/en/Main.ArduinoBoardMKRFox1200>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      -
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``mkrzero``
      - `Arduino MKRZero <https://www.arduino.cc/en/Main/ArduinoBoardMKRZero>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      -
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``mzeroUSB``
      - `Arduino M0 <http://www.arduino.org/products/boards/arduino-m0>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <debugging>`
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``mzeropro``
      - `Arduino M0 Pro (Programming/Debug Port) <http://www.arduino.org/products/boards/arduino-m0-pro>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <debugging>`
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``mzeroproUSB``
      - `Arduino M0 Pro (Native USB Port) <http://www.arduino.org/products/boards/arduino-m0-pro>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      -
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``tian``
      - `Arduino Tian <http://www.arduino.org/products/boards/arduino-tian>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      -
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``zero``
      - `Arduino Zero (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <debugging>`
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``zeroUSB``
      - `Arduino Zero (USB Native Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      -
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

Atmel
~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``samd21_xpro``
      - `Atmel SAMD21-XPRO <https://developer.mbed.org/platforms/SAMD21-XPRO/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <debugging>`
      - ATSAMD21J18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``samd21g18a``
      - `Atmel ATSAMW25-XPRO <https://developer.mbed.org/platforms/SAMW25-XPRO/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <debugging>`
      - ATSAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``saml21_xpro_b``
      - `Atmel SAML21-XPRO-B <https://developer.mbed.org/platforms/SAML21-XPRO/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <debugging>`
      - ATSAML21J18B
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``samr21_xpro``
      - `Atmel ATSAMR21-XPRO <https://developer.mbed.org/platforms/SAMR21-XPRO/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <debugging>`
      - ATSAMR21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

Digistump
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``digix``
      - `Digistump DigiX <http://digistump.com/products/50>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      -
      - AT91SAM3X8E
      - 84 MHz
      - 512 Kb
      - 28 Kb

SODAQ
~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``sodaq_autonomo``
      - `SODAQ Autonomo <http://support.sodaq.com/sodaq-one/autonomo/getting-started-autonomo/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      -
      - SAMD21J18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``sodaq_explorer``
      - `SODAQ ExpLoRer <http://support.sodaq.com/sodaq-one/explorer/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      -
      - SAMD21J18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``sodaq_one``
      - `SODAQ ONE <http://support.sodaq.com/sodaq-one/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      -
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``sodaq_wdt``
      - `SODAQ WDT <http://support.sodaq.com/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      -
      - SAMD21J18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

SainSmart
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``sainSmartDue``
      - `SainSmart Due (Programming Port) <http://www.sainsmart.com/arduino/control-boards/sainsmart-due-atmel-sam3x8e-arm-cortex-m3-board-black.html>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      -
      - AT91SAM3X8E
      - 84 MHz
      - 512 Kb
      - 32 Kb

    * - ``sainSmartDueUSB``
      - `SainSmart Due (USB Native Port) <http://www.sainsmart.com/arduino/control-boards/sainsmart-due-atmel-sam3x8e-arm-cortex-m3-board-black.html>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      -
      - AT91SAM3X8E
      - 84 MHz
      - 512 Kb
      - 32 Kb

SparkFun
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``sparkfun_samd21_dev_usb``
      - `SparkFun SAMD21 Dev Breakout <https://www.sparkfun.com/products/13672>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <debugging>`
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``sparkfun_samd21_mini_usb``
      - `SparkFun SAMD21 Mini Breakout <https://www.sparkfun.com/products/13664>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <debugging>`
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb
