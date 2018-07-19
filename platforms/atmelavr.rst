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

.. _platform_atmelavr:

Atmel AVR
=========
:ref:`projectconf_env_platform` = ``atmelavr``

Atmel AVR 8- and 32-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industrys most code-efficient architecture for C and assembly programming.

For more detailed information please visit `vendor site <http://www.atmel.com/products/microcontrollers/avr/default.aspx?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: atmelavr_extra.rst

Examples
--------

Examples are listed from `Atmel AVR development platform repository <https://github.com/platformio/platform-atmelavr/tree/master/examples?utm_source=platformio&utm_medium=docs>`_:

* `arduino-blink <https://github.com/platformio/platform-atmelavr/tree/master/examples/arduino-blink?utm_source=platformio&utm_medium=docs>`_
* `arduino-external-libs <https://github.com/platformio/platform-atmelavr/tree/master/examples/arduino-external-libs?utm_source=platformio&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-atmelavr/tree/master/examples/arduino-internal-libs?utm_source=platformio&utm_medium=docs>`_
* `arduino-own-src_dir <https://github.com/platformio/platform-atmelavr/tree/master/examples/arduino-own-src_dir?utm_source=platformio&utm_medium=docs>`_
* `digitstump-mouse <https://github.com/platformio/platform-atmelavr/tree/master/examples/digitstump-mouse?utm_source=platformio&utm_medium=docs>`_
* `engduino-magnetometer <https://github.com/platformio/platform-atmelavr/tree/master/examples/engduino-magnetometer?utm_source=platformio&utm_medium=docs>`_
* `native-blink <https://github.com/platformio/platform-atmelavr/tree/master/examples/native-blink?utm_source=platformio&utm_medium=docs>`_
* `simba-blink <https://github.com/platformio/platform-atmelavr/tree/master/examples/simba-blink?utm_source=platformio&utm_medium=docs>`_

Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-atmelavr/releases>`__
of Atmel AVR development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = atmelavr
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = atmelavr@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-atmelavr.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinoavr <http://arduino.cc/en/Reference/HomePage?utm_source=platformio&utm_medium=docs>`__
      - Arduino Wiring-based Framework (AVR Core, 1.6)

    * - `framework-simba <https://github.com/eerimoq/simba?utm_source=platformio&utm_medium=docs>`__
      - Simba Framework

    * - `tool-avrdude <http://www.nongnu.org/avrdude/?utm_source=platformio&utm_medium=docs>`__
      - AVRDUDE

    * - `tool-micronucleus <https://github.com/micronucleus/micronucleus?utm_source=platformio&utm_medium=docs>`__
      - Micronucleus

    * - `toolchain-atmelavr <https://gcc.gnu.org/wiki/avr-gcc?utm_source=platformio&utm_medium=docs>`__
      - avr-gcc

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
    * - ``bluefruitmicro``
      - `Adafruit Bluefruit Micro <https://www.adafruit.com/products/2661?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``feather328p``
      - `Adafruit Feather 328P <https://www.adafruit.com/product/3458?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - ``feather32u4``
      - `Adafruit Feather 32u4 <https://learn.adafruit.com/adafruit-feather-32u4-bluefruit-le/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``flora8``
      - `Adafruit Flora <http://www.adafruit.com/product/659?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``gemma``
      - `Adafruit Gemma <http://www.adafruit.com/products/1222?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - ``itsybitsy32u4_3V``
      - `Adafruit ItsyBitsy 3V/8MHz <https://www.adafruit.com/product/3675?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``itsybitsy32u4_5V``
      - `Adafruit ItsyBitsy 5V/16MHz <https://www.adafruit.com/product/3677?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``metro``
      - `Adafruit Metro <https://www.adafruit.com/products/2466?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``protrinket3``
      - `Adafruit Pro Trinket 3V/12MHz (USB) <http://www.adafruit.com/products/2010?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 12MHz
      - 28KB
      - 2KB
    * - ``protrinket3ftdi``
      - `Adafruit Pro Trinket 3V/12MHz (FTDI) <http://www.adafruit.com/products/2010?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 12MHz
      - 28KB
      - 2KB
    * - ``protrinket5``
      - `Adafruit Pro Trinket 5V/16MHz (USB) <http://www.adafruit.com/products/2000?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - ``protrinket5ftdi``
      - `Adafruit Pro Trinket 5V/16MHz (FTDI) <http://www.adafruit.com/products/2000?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - ``trinket3``
      - `Adafruit Trinket 3V/8MHz <http://www.adafruit.com/products/1500?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - ``trinket5``
      - `Adafruit Trinket 5V/16MHz <http://www.adafruit.com/products/1501?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY85
      - 16MHz
      - 8KB
      - 512B

Alorium Technology
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
    * - ``alorium_xlr8``
      - `Alorium XLR8 <http://www.aloriumtech.com/xlr8/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

Anarduino
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
    * - ``miniwireless``
      - `Anarduino MiniWireless <http://www.anarduino.com/miniwireless/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

Arduboy
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
    * - ``arduboy``
      - `Arduboy <https://www.arduboy.com?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``arduboy_devkit``
      - `Arduboy DevKit <https://www.arduboy.com?utm_source=platformio&utm_medium=docs>`_
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``LilyPadUSB``
      - `Arduino LilyPad USB <http://arduino.cc/en/Main/ArduinoBoardLilyPadUSB?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``atmega328pb``
      - `Atmel ATmega328PB <http://www.atmel.com/devices/ATMEGA328PB.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328PB
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``atmegangatmega168``
      - `Arduino NG or older ATmega168 <http://arduino.cc/en/main/boards?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - ``atmegangatmega8``
      - `Arduino NG or older ATmega8 <http://arduino.cc/en/main/boards?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA8
      - 16MHz
      - 7KB
      - 1KB
    * - ``btatmega168``
      - `Arduino BT ATmega168 <http://arduino.cc/en/main/boards?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - ``btatmega328``
      - `Arduino BT ATmega328 <http://arduino.cc/en/main/boards?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - ``chiwawa``
      - `Arduino Industrial 101 <https://store.arduino.cc/arduino-industrial-101?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``diecimilaatmega168``
      - `Arduino Duemilanove or Diecimila ATmega168 <http://arduino.cc/en/Main/ArduinoBoardDiecimila?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - ``diecimilaatmega328``
      - `Arduino Duemilanove or Diecimila ATmega328 <http://arduino.cc/en/Main/ArduinoBoardDiecimila?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - ``esplora``
      - `Arduino Esplora <https://www.arduino.cc/en/Main/ArduinoBoardEsplora?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``ethernet``
      - `Arduino Ethernet <https://www.arduino.cc/en/Main/ArduinoBoardEthernet?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``fio``
      - `Arduino Fio <http://arduino.cc/en/Main/ArduinoBoardFio?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - ``leonardo``
      - `Arduino Leonardo <https://www.arduino.cc/en/Main/ArduinoBoardLeonardo?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``leonardoeth``
      - `Arduino Leonardo ETH <https://www.arduino.cc/en/Main/ArduinoBoardLeonardoEth?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``lilypadatmega168``
      - `Arduino LilyPad ATmega168 <http://arduino.cc/en/Main/ArduinoBoardLilyPad?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA168
      - 8MHz
      - 14KB
      - 1KB
    * - ``lilypadatmega328``
      - `Arduino LilyPad ATmega328 <http://arduino.cc/en/Main/ArduinoBoardLilyPad?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - ``megaADK``
      - `Arduino Mega ADK <https://www.arduino.cc/en/Main/ArduinoBoardMegaADK?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - ``megaatmega1280``
      - `Arduino Mega or Mega 2560 ATmega1280 <https://www.arduino.cc/en/Main/ArduinoBoardMega2560?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA1280
      - 16MHz
      - 124KB
      - 8KB
    * - ``megaatmega2560``
      - `Arduino Mega or Mega 2560 ATmega2560 (Mega 2560) <https://www.arduino.cc/en/Main/ArduinoBoardMega2560?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - ``micro``
      - `Arduino Micro <https://www.arduino.cc/en/Main/ArduinoBoardMicro?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``miniatmega168``
      - `Arduino Mini ATmega168 <http://arduino.cc/en/Main/ArduinoBoardMini?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - ``miniatmega328``
      - `Arduino Mini ATmega328 <http://arduino.cc/en/Main/ArduinoBoardMini?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - ``nanoatmega168``
      - `Arduino Nano ATmega168 <https://www.arduino.cc/en/Main/ArduinoBoardNano?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - ``nanoatmega328``
      - `Arduino Nano ATmega328 <https://www.arduino.cc/en/Main/ArduinoBoardNano?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - ``pro16MHzatmega168``
      - `Arduino Pro or Pro Mini ATmega168 (5V, 16 MHz) <http://arduino.cc/en/Main/ArduinoBoardProMini?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - ``pro16MHzatmega328``
      - `Arduino Pro or Pro Mini ATmega328 (5V, 16 MHz) <http://arduino.cc/en/Main/ArduinoBoardProMini?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - ``pro8MHzatmega168``
      - `Arduino Pro or Pro Mini ATmega168 (3.3V, 8 MHz) <http://arduino.cc/en/Main/ArduinoBoardProMini?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA168
      - 8MHz
      - 14KB
      - 1KB
    * - ``pro8MHzatmega328``
      - `Arduino Pro or Pro Mini ATmega328 (3.3V, 8 MHz) <http://arduino.cc/en/Main/ArduinoBoardProMini?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - ``robotControl``
      - `Arduino Robot Control <https://www.arduino.cc/en/Main/Robot?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``robotMotor``
      - `Arduino Robot Motor <https://www.arduino.cc/en/Main/Robot?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``uno``
      - `Arduino Uno <https://www.arduino.cc/en/Main/ArduinoBoardUno?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``yun``
      - `Arduino Yun <https://www.arduino.cc/en/Main/ArduinoBoardYun?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``yunmini``
      - `Arduino Yun Mini <https://www.arduino.cc/en/Main/ArduinoBoardYunMini?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

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
    * - ``attiny13``
      - `Generic ATTiny13 <http://www.atmel.com/devices/ATTINY13.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY13
      - 9MHz
      - 1KB
      - 64B
    * - ``attiny1634``
      - `Generic ATTiny1634 <http://www.atmel.com/devices/ATTINY1634.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY1634
      - 8MHz
      - 16KB
      - 1KB
    * - ``attiny167``
      - `Generic ATTiny167 <http://www.atmel.com/devices/ATTINY167.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY167
      - 8MHz
      - 16KB
      - 512B
    * - ``attiny2313``
      - `Generic ATTiny2313 <http://www.microchip.com/wwwproducts/en/ATTINY2313?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY2313
      - 8MHz
      - 2KB
      - 128B
    * - ``attiny24``
      - `Generic ATTiny24 <http://www.atmel.com/devices/ATTINY24.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY24
      - 8MHz
      - 2KB
      - 128B
    * - ``attiny25``
      - `Generic ATTiny25 <http://www.atmel.com/devices/ATTINY25.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY25
      - 8MHz
      - 2KB
      - 128B
    * - ``attiny261``
      - `Generic ATTiny261 <http://www.atmel.com/devices/ATTINY261.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY261
      - 8MHz
      - 2KB
      - 128B
    * - ``attiny4313``
      - `Generic ATTiny4313 <http://www.microchip.com/wwwproducts/en/ATTINY4313?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY4313
      - 8MHz
      - 4KB
      - 256B
    * - ``attiny44``
      - `Generic ATTiny44 <http://www.atmel.com/devices/ATTINY44.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY44
      - 8MHz
      - 4KB
      - 256B
    * - ``attiny441``
      - `Generic ATTiny441 <http://www.atmel.com/devices/ATTINY441.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY441
      - 8MHz
      - 4KB
      - 256B
    * - ``attiny45``
      - `Generic ATTiny45 <http://www.atmel.com/devices/ATTINY45.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY45
      - 8MHz
      - 4KB
      - 256B
    * - ``attiny461``
      - `Generic ATTiny461 <http://www.atmel.com/devices/ATTINY461.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY461
      - 8MHz
      - 4KB
      - 256B
    * - ``attiny48``
      - `Generic ATTiny48 <http://www.atmel.com/devices/ATTINY48.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY48
      - 8MHz
      - 4KB
      - 256B
    * - ``attiny828``
      - `Generic ATTiny828 <http://www.atmel.com/devices/ATTINY828.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY828
      - 8MHz
      - 8KB
      - 512B
    * - ``attiny84``
      - `Generic ATTiny84 <http://www.atmel.com/devices/ATTINY84.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY84
      - 8MHz
      - 8KB
      - 512B
    * - ``attiny841``
      - `Generic ATTiny841 <http://www.atmel.com/devices/ATTINY841.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY841
      - 8MHz
      - 8KB
      - 512B
    * - ``attiny85``
      - `Generic ATTiny85 <http://www.atmel.com/devices/ATTINY85.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - ``attiny861``
      - `Generic ATTiny861 <http://www.atmel.com/devices/ATTINY861.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY861
      - 8MHz
      - 8KB
      - 512B
    * - ``attiny87``
      - `Generic ATTiny87 <http://www.atmel.com/devices/ATTINY87.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY87
      - 8MHz
      - 8KB
      - 512B
    * - ``attiny88``
      - `Generic ATTiny88 <http://www.atmel.com/devices/ATTINY88.aspx?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY88
      - 8MHz
      - 8KB
      - 512B
    * - ``usbasp``
      - `USBasp stick <https://www.fischl.de/usbasp/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA8
      - 12MHz
      - 8KB
      - 1KB

BQ
~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``zumbt328``
      - `BQ ZUM BT-328 <http://www.bq.com/gb/products/zum.html?utm_source=platformio&utm_medium=docs>`_
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``raspduino``
      - `BitWizard Raspduino <http://www.bitwizard.nl/wiki/index.php/Raspduino?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB

Controllino
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
    * - ``controllino_maxi``
      - `Controllino Maxi <https://controllino.biz/controllino/maxi/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - ``controllino_maxi_automation``
      - `Controllino Maxi Automation <https://controllino.biz/controllino/maxi-automation/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - ``controllino_mega``
      - `Controllino Mega <https://controllino.biz/controllino/mega/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - ``controllino_mini``
      - `Controllino Mini <https://controllino.biz/controllino/mini/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

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
    * - ``digispark-pro``
      - `Digispark Pro <http://digistump.com/products/109?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY167
      - 16MHz
      - 14.50KB
      - 512B
    * - ``digispark-pro32``
      - `Digispark Pro (32 byte buffer) <http://digistump.com/products/109?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY167
      - 16MHz
      - 14.50KB
      - 512B
    * - ``digispark-pro64``
      - `Digispark Pro (16 MHz) (64 byte buffer) <http://digistump.com/products/109?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY167
      - 16MHz
      - 14.50KB
      - 512B
    * - ``digispark-tiny``
      - `Digispark USB <http://digistump.com/products/1?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATTINY85
      - 16MHz
      - 5.87KB
      - 512B

Dwengo
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
    * - ``dwenguino``
      - `Dwenguino <http://www.dwengo.org/?utm_source=platformio&utm_medium=docs>`_
      - No
      - AT90USB646
      - 16MHz
      - 60KB
      - 2KB

Elektor
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
    * - ``elektor_uno_r4``
      - `Elektor Uno R4 <https://www.elektor.com/elektor-uno-r4?utm_source=platformio&utm_medium=docs>`_
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``engduinov3``
      - `Engduino 3 <http://www.engduino.org?utm_source=platformio&utm_medium=docs>`_
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``mayfly``
      - `EnviroDIY Mayfly <http://envirodiy.org/forums/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB

LightUp
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
    * - ``lightup``
      - `LightUp <https://www.lightup.io/?utm_source=platformio&utm_medium=docs>`_
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``one``
      - `Linino One <http://www.linino.org/portfolio/linino-one/?utm_source=platformio&utm_medium=docs>`_
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``mightyhat``
      - `LowPowerLab MightyHat <https://lowpowerlab.com/shop/product/130?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 31KB
      - 2KB
    * - ``moteino``
      - `LowPowerLab Moteino <https://lowpowerlab.com/shop/moteino-r4?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``moteinomega``
      - `LowPowerLab MoteinoMEGA <http://lowpowerlab.com/blog/2014/08/09/moteinomega-available-now/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB

Mcudude
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
    * - ``mightycore1284``
      - `MightyCore ATmega1284 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - ``mightycore16``
      - `MightyCore ATmega16 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA16
      - 16MHz
      - 15.50KB
      - 1KB
    * - ``mightycore164``
      - `MightyCore ATmega164 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA164P
      - 16MHz
      - 15.50KB
      - 1KB
    * - ``mightycore32``
      - `MightyCore ATmega32 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``mightycore324``
      - `MightyCore ATmega324 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA324P
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``mightycore644``
      - `MightyCore ATmega644 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - ``mightycore8535``
      - `MightyCore ATmega8535 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board?utm_source=platformio&utm_medium=docs>`_
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``smart7688``
      - `LinkIt Smart 7688 Duo <https://www.seeedstudio.com/LinkIt-Smart-7688-Duo-p-2574.html?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB

Microchip
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
    * - ``at90pwm216``
      - `Atmel AT90PWM216 <http://www.microchip.com/wwwproducts/en/AT90PWM216?utm_source=platformio&utm_medium=docs>`_
      - No
      - AT90PWM216
      - 16MHz
      - 16KB
      - 1KB
    * - ``at90pwm316``
      - `Atmel AT90PWM316 <http://www.microchip.com/wwwproducts/en/AT90PWM316?utm_source=platformio&utm_medium=docs>`_
      - No
      - AT90PWM316
      - 16MHz
      - 16KB
      - 1KB

Microduino
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
    * - ``1284p16m``
      - `Microduino Core+ (ATmega1284P@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_Core%2B?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - ``1284p8m``
      - `Microduino Core+ (ATmega1284P@8M,3.3V) <http://wiki.microduinoinc.com/Microduino-Module_Core%2B?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - ``168pa16m``
      - `Microduino Core (Atmega168PA@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_Core?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA168P
      - 16MHz
      - 15.50KB
      - 1KB
    * - ``168pa8m``
      - `Microduino Core (Atmega168PA@8M,3.3V) <http://wiki.microduinoinc.com/Microduino-Module_Core?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA168P
      - 8MHz
      - 15.50KB
      - 1KB
    * - ``328p16m``
      - `Microduino Core (Atmega328P@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_Core?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``328p8m``
      - `Microduino Core (Atmega328P@8M,3.3V) <http://wiki.microduinoinc.com/Microduino-Module_Core?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - ``32u416m``
      - `Microduino Core USB (ATmega32U4@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_CoreUSB?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``644pa16m``
      - `Microduino Core+ (Atmega644PA@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_Core%2B?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - ``644pa8m``
      - `Microduino Core+ (Atmega644PA@8M,3.3V) <http://wiki.microduinoinc.com/Microduino-Module_Core%2B?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA644P
      - 8MHz
      - 63KB
      - 4KB

OpenEnergyMonitor
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``emonpi``
      - `OpenEnergyMonitor emonPi <https://github.com/openenergymonitor/emonpi?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB

PanStamp
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
    * - ``panStampAVR``
      - `PanStamp AVR <http://www.panstamp.com/product/panstamp-avr/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB

Pinoccio
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
    * - ``pinoccio``
      - `Pinoccio Scout <https://www.crowdsupply.com/pinoccio/mesh-sensor-network?utm_source=platformio&utm_medium=docs>`_
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``a-star32U4``
      - `Pololu A-Star 32U4 <https://www.pololu.com/category/149/a-star-programmable-controllers?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

Punch Through
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
    * - ``lightblue-bean``
      - `LightBlue Bean <https://punchthrough.com/bean?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - ``lightblue-beanplus``
      - `LightBlue Bean+ <https://punchthrough.com/bean?utm_source=platformio&utm_medium=docs>`_
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``quirkbot``
      - `Quirkbot <http://quirkbot.com?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB

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
    * - ``blend``
      - `RedBearLab Blend <http://redbearlab.com/blend/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``blendmicro16``
      - `RedBearLab Blend Micro 3.3V/16MHz (overclock) <http://redbearlab.com/blendmicro/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``blendmicro8``
      - `RedBearLab Blend Micro 3.3V/8MHz <http://redbearlab.com/blendmicro/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB

RepRap
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
    * - ``reprap_rambo``
      - `RepRap RAMBo <http://reprap.org/wiki/Rambo?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB

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
    * - ``sodaq_galora``
      - `SODAQ GaLoRa <http://support.sodaq.com/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - ``sodaq_mbili``
      - `SODAQ Mbili <http://support.sodaq.com/sodaq-one/sodaq-mbili-1284p/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - ``sodaq_moja``
      - `SODAQ Moja <http://support.sodaq.com/sodaq-one/moja/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - ``sodaq_ndogo``
      - `SODAQ Ndogo <http://support.sodaq.com/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - ``sodaq_tatu``
      - `SODAQ Tatu <http://support.sodaq.com/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB

Sanguino
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
    * - ``sanguino_atmega1284_8m``
      - `Sanguino ATmega1284p (8MHz) <https://github.com/Lauszus/Sanguino?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - ``sanguino_atmega1284p``
      - `Sanguino ATmega1284p (16MHz) <https://github.com/Lauszus/Sanguino?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - ``sanguino_atmega644``
      - `Sanguino ATmega644 or ATmega644A (16 MHz) <https://github.com/Lauszus/Sanguino?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA644
      - 16MHz
      - 63KB
      - 4KB
    * - ``sanguino_atmega644_8m``
      - `Sanguino ATmega644 or ATmega644A (8 MHz) <https://github.com/Lauszus/Sanguino?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA644
      - 8MHz
      - 63KB
      - 4KB
    * - ``sanguino_atmega644p``
      - `Sanguino ATmega644P or ATmega644PA (16 MHz) <https://github.com/Lauszus/Sanguino?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - ``sanguino_atmega644p_8m``
      - `Sanguino ATmega644P or ATmega644PA (8 MHz) <https://github.com/Lauszus/Sanguino?utm_source=platformio&utm_medium=docs>`_
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``seeeduino``
      - `Seeeduino <https://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

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
    * - ``sparkfun_digitalsandbox``
      - `SparkFun Digital Sandbox <https://www.sparkfun.com/products/12651?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - ``sparkfun_fiov3``
      - `SparkFun Fio V3 3.3V/8MHz <https://www.sparkfun.com/products/11520?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``sparkfun_makeymakey``
      - `SparkFun Makey Makey <https://www.sparkfun.com/products/11511?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``sparkfun_megamini``
      - `SparkFun Mega Pro Mini 3.3V <https://www.sparkfun.com/products/10743?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA2560
      - 8MHz
      - 252KB
      - 8KB
    * - ``sparkfun_megapro16MHz``
      - `SparkFun Mega Pro 5V/16MHz <https://www.sparkfun.com/products/11007?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - ``sparkfun_megapro8MHz``
      - `SparkFun Mega Pro 3.3V/8MHz <https://www.sparkfun.com/products/10744?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA2560
      - 8MHz
      - 252KB
      - 8KB
    * - ``sparkfun_promicro16``
      - `SparkFun Pro Micro 5V/16MHz <https://www.sparkfun.com/products/12640?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - ``sparkfun_promicro8``
      - `SparkFun Pro Micro 3.3V/8MHz <https://www.sparkfun.com/products/12587?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``sparkfun_qduinomini``
      - `SparkFun Qduino Mini <https://www.sparkfun.com/products/13614?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - ``sparkfun_redboard``
      - `SparkFun RedBoard <https://www.sparkfun.com/products/12757?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - ``sparkfun_satmega128rfa1``
      - `SparkFun ATmega128RFA1 Dev Board <https://www.sparkfun.com/products/11197?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA128RFA1
      - 16MHz
      - 16KB
      - 124KB
    * - ``sparkfun_serial7seg``
      - `SparkFun Serial 7-Segment Display <https://www.sparkfun.com/products/11441?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - ``uview``
      - `SparkFun MicroView <https://www.sparkfun.com/products/12923?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

SpellFoundry
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
    * - ``sleepypi``
      - `SpellFoundry Sleepy Pi 2 <https://spellfoundry.com/product/sleepy-pi-2/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB

The Things Network
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
    * - ``the_things_uno``
      - `The Things Uno <https://shop.thethingsnetwork.com/index.php/product/the-things-uno/?utm_source=platformio&utm_medium=docs>`_
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``tinyduino``
      - `TinyCircuits TinyDuino Processor Board <https://tiny-circuits.com/tinyduino-processor-board.html?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - ``tinylily``
      - `TinyCircuits TinyLily Mini Processor <https://tiny-circuits.com/tiny-lily-mini-processor.html?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB

Wicked Device
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
    * - ``wildfirev2``
      - `Wicked Device WildFire V2 <http://shop.wickeddevice.com/resources/wildfire/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA1284P
      - 16MHz
      - 120.00KB
      - 16KB
    * - ``wildfirev3``
      - `Wicked Device WildFire V3 <http://shop.wickeddevice.com/resources/wildfire/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB

makerlab.mx
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
    * - ``altair``
      - `Altair <http://www.aquila.io/en?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA256RFR2
      - 16MHz
      - 248KB
      - 32KB

nicai-systems
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
    * - ``bob3``
      - `nicai-systems BOB3 coding bot <http://www.nicai-systems.com?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA88
      - 8MHz
      - 8KB
      - 1KB
    * - ``nibo2``
      - `nicai-systems NIBO 2 robot <http://www.nicai-systems.com/en/nibo2?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA128
      - 16MHz
      - 128KB
      - 4KB
    * - ``nibobee``
      - `nicai-systems NIBObee robot <http://www.nicai-systems.com/en/nibobee?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA16
      - 15MHz
      - 16KB
      - 1KB
    * - ``nibobee_1284``
      - `nicai-systems NIBObee robot with Tuning Kit <http://www.nicai-systems.com/en/nibobee?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA1284P
      - 20MHz
      - 128KB
      - 16KB
    * - ``niboburger``
      - `nicai-systems NIBO burger robot <http://www.nicai-systems.com/en/nibo-burger?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA16
      - 15MHz
      - 16KB
      - 1KB
    * - ``niboburger_1284``
      - `nicai-systems NIBO burger robot with Tuning Kit <http://www.nicai-systems.com/en/nibo-burger?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA1284P
      - 20MHz
      - 128KB
      - 16KB

ubIQio
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
    * - ``ardhat``
      - `ubIQio Ardhat <http://ardhat.com?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
