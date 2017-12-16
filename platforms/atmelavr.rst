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

For more detailed information please visit `vendor site <http://www.atmel.com/products/microcontrollers/avr/default.aspx>`_.

.. contents:: Contents
    :local:

Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinoavr <http://arduino.cc/en/Reference/HomePage>`__
      - Arduino Wiring-based Framework (AVR Core, 1.6)

    * - `framework-simba <https://github.com/eerimoq/simba>`__
      - Simba Framework

    * - `tool-avrdude <http://www.nongnu.org/avrdude/>`__
      - AVRDUDE

    * - `tool-micronucleus <https://github.com/micronucleus/micronucleus>`__
      - Micronucleus

    * - `toolchain-atmelavr <https://gcc.gnu.org/wiki/avr-gcc>`__
      - avr-gcc

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

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

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

    * - ``bluefruitmicro``
      - `Adafruit Bluefruit Micro <https://www.adafruit.com/products/2661>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 8 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``feather32u4``
      - `Adafruit Feather <https://learn.adafruit.com/adafruit-feather-32u4-bluefruit-le/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 8 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``flora8``
      - `Adafruit Flora <http://www.adafruit.com/product/659>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 8 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``gemma``
      - `Adafruit Gemma <http://www.adafruit.com/products/1222>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY85
      - 8 MHz
      - 8 Kb
      - 0.5 Kb

    * - ``metro``
      - `Adafruit Metro <https://www.adafruit.com/products/2466>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``protrinket3``
      - `Adafruit Pro Trinket 3V/12MHz (USB) <http://www.adafruit.com/products/2010>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 12 MHz
      - 32 Kb
      - 2 Kb

    * - ``protrinket3ftdi``
      - `Adafruit Pro Trinket 3V/12MHz (FTDI) <http://www.adafruit.com/products/2010>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 12 MHz
      - 32 Kb
      - 2 Kb

    * - ``protrinket5``
      - `Adafruit Pro Trinket 5V/16MHz (USB) <http://www.adafruit.com/products/2000>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``protrinket5ftdi``
      - `Adafruit Pro Trinket 5V/16MHz (FTDI) <http://www.adafruit.com/products/2000>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``trinket3``
      - `Adafruit Trinket 3V/8MHz <http://www.adafruit.com/products/1500>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY85
      - 8 MHz
      - 8 Kb
      - 0.5 Kb

    * - ``trinket5``
      - `Adafruit Trinket 5V/16MHz <http://www.adafruit.com/products/1501>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY85
      - 16 MHz
      - 8 Kb
      - 0.5 Kb

Alorium Technology
~~~~~~~~~~~~~~~~~~

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

    * - ``alorium_xlr8``
      - `Alorium XLR8 <http://www.aloriumtech.com/xlr8/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

Anarduino
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

    * - ``miniwireless``
      - `Anarduino MiniWireless <http://www.anarduino.com/miniwireless/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

Arduboy
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

    * - ``arduboy``
      - `Arduboy <https://www.arduboy.com>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``arduboy_devkit``
      - `Arduboy DevKit <https://www.arduboy.com>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

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

    * - ``LilyPadUSB``
      - `Arduino LilyPad USB <http://arduino.cc/en/Main/ArduinoBoardLilyPadUSB>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 8 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``atmega328pb``
      - `Atmel ATmega328PB <http://www.atmel.com/devices/ATMEGA328PB.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328PB
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``atmegangatmega168``
      - `Arduino NG or older ATmega168 <http://arduino.cc/en/main/boards>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA168
      - 16 MHz
      - 16 Kb
      - 1 Kb

    * - ``atmegangatmega8``
      - `Arduino NG or older ATmega8 <http://arduino.cc/en/main/boards>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA8
      - 16 MHz
      - 8 Kb
      - 1 Kb

    * - ``btatmega168``
      - `Arduino BT ATmega168 <http://arduino.cc/en/main/boards>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA168
      - 16 MHz
      - 16 Kb
      - 1 Kb

    * - ``btatmega328``
      - `Arduino BT ATmega328 <http://arduino.cc/en/main/boards>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``chiwawa``
      - `Arduino Industrial 101 <https://store.arduino.cc/arduino-industrial-101>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``diecimilaatmega168``
      - `Arduino Duemilanove or Diecimila ATmega168 <http://arduino.cc/en/Main/ArduinoBoardDiecimila>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA168
      - 16 MHz
      - 16 Kb
      - 1 Kb

    * - ``diecimilaatmega328``
      - `Arduino Duemilanove or Diecimila ATmega328 <http://arduino.cc/en/Main/ArduinoBoardDiecimila>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``esplora``
      - `Arduino Esplora <https://www.arduino.cc/en/Main/ArduinoBoardEsplora>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``ethernet``
      - `Arduino Ethernet <https://www.arduino.cc/en/Main/ArduinoBoardEthernet>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``fio``
      - `Arduino Fio <http://arduino.cc/en/Main/ArduinoBoardFio>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 8 MHz
      - 32 Kb
      - 2 Kb

    * - ``leonardo``
      - `Arduino Leonardo <https://www.arduino.cc/en/Main/ArduinoBoardLeonardo>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``leonardoeth``
      - `Arduino Leonardo ETH <https://www.arduino.cc/en/Main/ArduinoBoardLeonardoEth>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``lilypadatmega168``
      - `Arduino LilyPad ATmega168 <http://arduino.cc/en/Main/ArduinoBoardLilyPad>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA168
      - 8 MHz
      - 16 Kb
      - 1 Kb

    * - ``lilypadatmega328``
      - `Arduino LilyPad ATmega328 <http://arduino.cc/en/Main/ArduinoBoardLilyPad>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 8 MHz
      - 32 Kb
      - 2 Kb

    * - ``megaADK``
      - `Arduino Mega ADK <https://www.arduino.cc/en/Main/ArduinoBoardMegaADK>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA2560
      - 16 MHz
      - 256 Kb
      - 8 Kb

    * - ``megaatmega1280``
      - `Arduino Mega or Mega 2560 ATmega1280 <https://www.arduino.cc/en/Main/ArduinoBoardMega2560>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1280
      - 16 MHz
      - 128 Kb
      - 8 Kb

    * - ``megaatmega2560``
      - `Arduino Mega or Mega 2560 ATmega2560 (Mega 2560) <https://www.arduino.cc/en/Main/ArduinoBoardMega2560>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA2560
      - 16 MHz
      - 256 Kb
      - 8 Kb

    * - ``micro``
      - `Arduino Micro <https://www.arduino.cc/en/Main/ArduinoBoardMicro>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``miniatmega168``
      - `Arduino Mini ATmega168 <http://arduino.cc/en/Main/ArduinoBoardMini>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA168
      - 16 MHz
      - 16 Kb
      - 1 Kb

    * - ``miniatmega328``
      - `Arduino Mini ATmega328 <http://arduino.cc/en/Main/ArduinoBoardMini>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``nanoatmega168``
      - `Arduino Nano ATmega168 <https://www.arduino.cc/en/Main/ArduinoBoardNano>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA168
      - 16 MHz
      - 16 Kb
      - 1 Kb

    * - ``nanoatmega328``
      - `Arduino Nano ATmega328 <https://www.arduino.cc/en/Main/ArduinoBoardNano>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``pro16MHzatmega168``
      - `Arduino Pro or Pro Mini ATmega168 (5V, 16 MHz) <http://arduino.cc/en/Main/ArduinoBoardProMini>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA168
      - 16 MHz
      - 16 Kb
      - 1 Kb

    * - ``pro16MHzatmega328``
      - `Arduino Pro or Pro Mini ATmega328 (5V, 16 MHz) <http://arduino.cc/en/Main/ArduinoBoardProMini>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``pro8MHzatmega168``
      - `Arduino Pro or Pro Mini ATmega168 (3.3V, 8 MHz) <http://arduino.cc/en/Main/ArduinoBoardProMini>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA168
      - 8 MHz
      - 16 Kb
      - 1 Kb

    * - ``pro8MHzatmega328``
      - `Arduino Pro or Pro Mini ATmega328 (3.3V, 8 MHz) <http://arduino.cc/en/Main/ArduinoBoardProMini>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 8 MHz
      - 32 Kb
      - 2 Kb

    * - ``robotControl``
      - `Arduino Robot Control <https://www.arduino.cc/en/Main/Robot>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``robotMotor``
      - `Arduino Robot Motor <https://www.arduino.cc/en/Main/Robot>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``uno``
      - `Arduino Uno <https://www.arduino.cc/en/Main/ArduinoBoardUno>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``yun``
      - `Arduino Yun <https://www.arduino.cc/en/Main/ArduinoBoardYun>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``yunmini``
      - `Arduino Yun Mini <https://www.arduino.cc/en/Main/ArduinoBoardYunMini>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

BQ
~~

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

    * - ``zumbt328``
      - `BQ ZUM BT-328 <http://www.bq.com/gb/products/zum.html>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

BitWizard
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

    * - ``raspduino``
      - `BitWizard Raspduino <http://www.bitwizard.nl/wiki/index.php/Raspduino>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

Controllino
~~~~~~~~~~~

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

    * - ``controllino_maxi``
      - `Controllino Maxi <https://controllino.biz/controllino/maxi/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA2560
      - 16 MHz
      - 256 Kb
      - 8 Kb

    * - ``controllino_maxi_automation``
      - `Controllino Maxi Automation <https://controllino.biz/controllino/maxi-automation/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA2560
      - 16 MHz
      - 256 Kb
      - 8 Kb

    * - ``controllino_mega``
      - `Controllino Mega <https://controllino.biz/controllino/mega/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA2560
      - 16 MHz
      - 256 Kb
      - 8 Kb

    * - ``controllino_mini``
      - `Controllino Mini <https://controllino.biz/controllino/mini/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

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

    * - ``digispark-pro``
      - `Digispark Pro <http://digistump.com/products/109>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY167
      - 16 MHz
      - 16 Kb
      - 0.5 Kb

    * - ``digispark-pro32``
      - `Digispark Pro (32 byte buffer) <http://digistump.com/products/109>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY167
      - 16 MHz
      - 16 Kb
      - 0.5 Kb

    * - ``digispark-pro64``
      - `Digispark Pro (16 MHz) (64 byte buffer) <http://digistump.com/products/109>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY167
      - 16 MHz
      - 16 Kb
      - 0.5 Kb

    * - ``digispark-tiny``
      - `Digispark USB <http://digistump.com/products/1>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY85
      - 16 MHz
      - 8 Kb
      - 0.5 Kb

Dwengo
~~~~~~

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

    * - ``dwenguino``
      - `Dwenguino <http://www.dwengo.org/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - AT90USB646
      - 16 MHz
      - 64 Kb
      - 2 Kb

Elektor
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

    * - ``elektor_uno_r4``
      - `Elektor Uno R4 <https://www.elektor.com/elektor-uno-r4>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328PB
      - 16 MHz
      - 32 Kb
      - 2 Kb

Engduino
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

    * - ``engduinov3``
      - `Engduino 3 <http://www.engduino.org>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 8 MHz
      - 32 Kb
      - 2.5 Kb

EnviroDIY
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

    * - ``mayfly``
      - `EnviroDIY Mayfly <http://envirodiy.org/forums/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 8 MHz
      - 128 Kb
      - 16 Kb

Generic ATTiny
~~~~~~~~~~~~~~

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

    * - ``attiny13``
      - `Generic ATTiny13 <http://www.atmel.com/devices/ATTINY13.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY13
      - 9 MHz
      - 1 Kb
      - 0.0625 Kb

    * - ``attiny1634``
      - `Generic ATTiny1634 <http://www.atmel.com/devices/ATTINY1634.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY1634
      - 8 MHz
      - 16 Kb
      - 1 Kb

    * - ``attiny167``
      - `Generic ATTiny167 <http://www.atmel.com/devices/ATTINY167.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY167
      - 8 MHz
      - 16 Kb
      - 0.5 Kb

    * - ``attiny2313``
      - `Generic ATTiny2313 <http://www.microchip.com/wwwproducts/en/ATTINY2313>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY2313
      - 8 MHz
      - 2 Kb
      - 0.125 Kb

    * - ``attiny24``
      - `Generic ATTiny24 <http://www.atmel.com/devices/ATTINY24.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY24
      - 8 MHz
      - 2 Kb
      - 0.125 Kb

    * - ``attiny25``
      - `Generic ATTiny25 <http://www.atmel.com/devices/ATTINY25.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY25
      - 8 MHz
      - 2 Kb
      - 0.125 Kb

    * - ``attiny261``
      - `Generic ATTiny261 <http://www.atmel.com/devices/ATTINY261.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY261
      - 8 MHz
      - 2 Kb
      - 0.125 Kb

    * - ``attiny4313``
      - `Generic ATTiny4313 <http://www.microchip.com/wwwproducts/en/ATTINY4313>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY4313
      - 8 MHz
      - 4 Kb
      - 0.25 Kb

    * - ``attiny44``
      - `Generic ATTiny44 <http://www.atmel.com/devices/ATTINY44.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY44
      - 8 MHz
      - 4 Kb
      - 0.25 Kb

    * - ``attiny441``
      - `Generic ATTiny441 <http://www.atmel.com/devices/ATTINY441.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY441
      - 8 MHz
      - 4 Kb
      - 0.25 Kb

    * - ``attiny45``
      - `Generic ATTiny45 <http://www.atmel.com/devices/ATTINY45.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY45
      - 8 MHz
      - 4 Kb
      - 0.25 Kb

    * - ``attiny461``
      - `Generic ATTiny461 <http://www.atmel.com/devices/ATTINY461.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY461
      - 8 MHz
      - 4 Kb
      - 0.25 Kb

    * - ``attiny48``
      - `Generic ATTiny48 <http://www.atmel.com/devices/ATTINY48.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY48
      - 8 MHz
      - 4 Kb
      - 0.25 Kb

    * - ``attiny84``
      - `Generic ATTiny84 <http://www.atmel.com/devices/ATTINY84.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY84
      - 8 MHz
      - 8 Kb
      - 0.5 Kb

    * - ``attiny841``
      - `Generic ATTiny841 <http://www.atmel.com/devices/ATTINY841.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY841
      - 8 MHz
      - 8 Kb
      - 0.5 Kb

    * - ``attiny85``
      - `Generic ATTiny85 <http://www.atmel.com/devices/ATTINY85.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY85
      - 8 MHz
      - 8 Kb
      - 0.5 Kb

    * - ``attiny861``
      - `Generic ATTiny861 <http://www.atmel.com/devices/ATTINY861.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY861
      - 8 MHz
      - 8 Kb
      - 0.5 Kb

    * - ``attiny87``
      - `Generic ATTiny87 <http://www.atmel.com/devices/ATTINY87.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY87
      - 8 MHz
      - 8 Kb
      - 0.5 Kb

    * - ``attiny88``
      - `Generic ATTiny88 <http://www.atmel.com/devices/ATTINY88.aspx>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY88
      - 8 MHz
      - 8 Kb
      - 0.5 Kb

LightUp
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

    * - ``lightup``
      - `LightUp <https://www.lightup.io/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 8 MHz
      - 32 Kb
      - 2.5 Kb

Linino
~~~~~~

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

    * - ``one``
      - `Linino One <http://www.linino.org/portfolio/linino-one/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

LowPowerLab
~~~~~~~~~~~

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

    * - ``mightyhat``
      - `LowPowerLab MightyHat <https://lowpowerlab.com/shop/product/130>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``moteino``
      - `LowPowerLab Moteino <https://lowpowerlab.com/shop/moteino-r4>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``moteinomega``
      - `LowPowerLab MoteinoMEGA <http://lowpowerlab.com/blog/2014/08/09/moteinomega-available-now/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 16 MHz
      - 128 Kb
      - 16 Kb

Mcudude
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

    * - ``mightycore1284``
      - `MightyCore ATmega1284 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 16 MHz
      - 128 Kb
      - 16 Kb

    * - ``mightycore16``
      - `MightyCore ATmega16 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA16
      - 16 MHz
      - 16 Kb
      - 1 Kb

    * - ``mightycore164``
      - `MightyCore ATmega164 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA164P
      - 16 MHz
      - 16 Kb
      - 1 Kb

    * - ``mightycore32``
      - `MightyCore ATmega32 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``mightycore324``
      - `MightyCore ATmega324 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA324P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``mightycore644``
      - `MightyCore ATmega644 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA644P
      - 16 MHz
      - 64 Kb
      - 4 Kb

    * - ``mightycore8535``
      - `MightyCore ATmega8535 <https://www.tindie.com/products/MCUdude/dip-40-arduino-compatible-development-board>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA16
      - 16 MHz
      - 8 Kb
      - 0.5 Kb

MediaTek Labs
~~~~~~~~~~~~~

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

    * - ``smart7688``
      - `LinkIt Smart 7688 Duo <https://www.seeedstudio.com/LinkIt-Smart-7688-Duo-p-2574.html>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 8 MHz
      - 32 Kb
      - 2.5 Kb

Microchip
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

    * - ``at90pwm316``
      - `Atmel AT90PWM316 <http://www.microchip.com/wwwproducts/en/AT90PWM316>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - AT90PWM316
      - 0 MHz
      - 16 Kb
      - 1 Kb

Microduino
~~~~~~~~~~

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

    * - ``1284p16m``
      - `Microduino Core+ (ATmega1284P@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_Core%2B>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 16 MHz
      - 128 Kb
      - 16 Kb

    * - ``1284p8m``
      - `Microduino Core+ (ATmega1284P@8M,3.3V) <http://wiki.microduinoinc.com/Microduino-Module_Core%2B>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 8 MHz
      - 128 Kb
      - 16 Kb

    * - ``168pa16m``
      - `Microduino Core (Atmega168PA@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_Core>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA168P
      - 16 MHz
      - 16 Kb
      - 1 Kb

    * - ``168pa8m``
      - `Microduino Core (Atmega168PA@8M,3.3V) <http://wiki.microduinoinc.com/Microduino-Module_Core>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA168P
      - 8 MHz
      - 16 Kb
      - 1 Kb

    * - ``328p16m``
      - `Microduino Core (Atmega328P@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_Core>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``328p8m``
      - `Microduino Core (Atmega328P@8M,3.3V) <http://wiki.microduinoinc.com/Microduino-Module_Core>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 8 MHz
      - 32 Kb
      - 2 Kb

    * - ``32u416m``
      - `Microduino Core USB (ATmega32U4@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_CoreUSB>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``644pa16m``
      - `Microduino Core+ (Atmega644PA@16M,5V) <http://wiki.microduinoinc.com/Microduino-Module_Core%2B>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA644P
      - 16 MHz
      - 64 Kb
      - 4 Kb

    * - ``644pa8m``
      - `Microduino Core+ (Atmega644PA@8M,3.3V) <http://wiki.microduinoinc.com/Microduino-Module_Core%2B>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA644P
      - 8 MHz
      - 64 Kb
      - 4 Kb

OpenEnergyMonitor
~~~~~~~~~~~~~~~~~

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

    * - ``emonpi``
      - `OpenEnergyMonitor emonPi <https://github.com/openenergymonitor/emonpi>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

PanStamp
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

    * - ``panStampAVR``
      - `PanStamp AVR <http://www.panstamp.com/product/panstamp-avr/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 8 MHz
      - 32 Kb
      - 2 Kb

Pinoccio
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

    * - ``pinoccio``
      - `Pinoccio Scout <https://www.crowdsupply.com/pinoccio/mesh-sensor-network>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA256RFR2
      - 16 MHz
      - 256 Kb
      - 32 Kb

Pololu Corporation
~~~~~~~~~~~~~~~~~~

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

    * - ``a-star32U4``
      - `Pololu A-Star 32U4 <https://www.pololu.com/category/149/a-star-programmable-controllers>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

Punch Through
~~~~~~~~~~~~~

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

    * - ``lightblue-bean``
      - `LightBlue Bean <https://punchthrough.com/bean>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 8 MHz
      - 32 Kb
      - 2 Kb

    * - ``lightblue-beanplus``
      - `LightBlue Bean+ <https://punchthrough.com/bean>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

Quirkbot
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

    * - ``quirkbot``
      - `Quirkbot <http://quirkbot.com>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 8 MHz
      - 32 Kb
      - 2.5 Kb

RedBearLab
~~~~~~~~~~

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

    * - ``blend``
      - `RedBearLab Blend <http://redbearlab.com/blend/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``blendmicro16``
      - `RedBearLab Blend Micro 3.3V/16MHz (overclock) <http://redbearlab.com/blendmicro/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``blendmicro8``
      - `RedBearLab Blend Micro 3.3V/8MHz <http://redbearlab.com/blendmicro/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 8 MHz
      - 32 Kb
      - 2.5 Kb

RepRap
~~~~~~

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

    * - ``reprap_rambo``
      - `RepRap RAMBo <http://reprap.org/wiki/Rambo>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA2560
      - 16 MHz
      - 256 Kb
      - 8 Kb

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

    * - ``sodaq_galora``
      - `SODAQ GaLoRa <http://support.sodaq.com/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 8 MHz
      - 128 Kb
      - 16 Kb

    * - ``sodaq_mbili``
      - `SODAQ Mbili <http://support.sodaq.com/sodaq-one/sodaq-mbili-1284p/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 8 MHz
      - 128 Kb
      - 16 Kb

    * - ``sodaq_moja``
      - `SODAQ Moja <http://support.sodaq.com/sodaq-one/moja/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 8 MHz
      - 32 Kb
      - 2 Kb

    * - ``sodaq_ndogo``
      - `SODAQ Ndogo <http://support.sodaq.com/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 8 MHz
      - 128 Kb
      - 16 Kb

    * - ``sodaq_tatu``
      - `SODAQ Tatu <http://support.sodaq.com/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 8 MHz
      - 128 Kb
      - 16 Kb

Sanguino
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

    * - ``sanguino_atmega1284_8m``
      - `Sanguino ATmega1284p (8MHz) <https://code.google.com/p/sanguino/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 8 MHz
      - 128 Kb
      - 16 Kb

    * - ``sanguino_atmega1284p``
      - `Sanguino ATmega1284p (16MHz) <https://code.google.com/p/sanguino/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 16 MHz
      - 128 Kb
      - 16 Kb

    * - ``sanguino_atmega644``
      - `Sanguino ATmega644 or ATmega644A (16 MHz) <https://code.google.com/p/sanguino/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA644
      - 16 MHz
      - 64 Kb
      - 4 Kb

    * - ``sanguino_atmega644_8m``
      - `Sanguino ATmega644 or ATmega644A (8 MHz) <https://code.google.com/p/sanguino/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA644
      - 8 MHz
      - 64 Kb
      - 4 Kb

    * - ``sanguino_atmega644p``
      - `Sanguino ATmega644P or ATmega644PA (16 MHz) <https://code.google.com/p/sanguino/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA644P
      - 16 MHz
      - 64 Kb
      - 4 Kb

    * - ``sanguino_atmega644p_8m``
      - `Sanguino ATmega644P or ATmega644PA (8 MHz) <https://code.google.com/p/sanguino/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA644P
      - 8 MHz
      - 64 Kb
      - 4 Kb

SeeedStudio
~~~~~~~~~~~

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

    * - ``seeeduino``
      - `Seeeduino <https://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

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

    * - ``sparkfun_digitalsandbox``
      - `SparkFun Digital Sandbox <https://www.sparkfun.com/products/12651>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 8 MHz
      - 32 Kb
      - 2 Kb

    * - ``sparkfun_fiov3``
      - `SparkFun Fio V3 3.3V/8MHz <https://www.sparkfun.com/products/11520>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 8 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``sparkfun_makeymakey``
      - `SparkFun Makey Makey <https://www.sparkfun.com/products/11511>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``sparkfun_megamini``
      - `SparkFun Mega Pro Mini 3.3V <https://www.sparkfun.com/products/10743>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA2560
      - 8 MHz
      - 256 Kb
      - 8 Kb

    * - ``sparkfun_megapro16MHz``
      - `SparkFun Mega Pro 5V/16MHz <https://www.sparkfun.com/products/11007>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA2560
      - 16 MHz
      - 256 Kb
      - 8 Kb

    * - ``sparkfun_megapro8MHz``
      - `SparkFun Mega Pro 3.3V/8MHz <https://www.sparkfun.com/products/10744>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA2560
      - 8 MHz
      - 256 Kb
      - 8 Kb

    * - ``sparkfun_promicro16``
      - `SparkFun Pro Micro 5V/16MHz <https://www.sparkfun.com/products/12640>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``sparkfun_promicro8``
      - `SparkFun Pro Micro 3.3V/8MHz <https://www.sparkfun.com/products/12587>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 8 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``sparkfun_qduinomini``
      - `SparkFun Qduino Mini <https://www.sparkfun.com/products/13614>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 8 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``sparkfun_redboard``
      - `SparkFun RedBoard <https://www.sparkfun.com/products/12757>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``sparkfun_satmega128rfa1``
      - `SparkFun ATmega128RFA1 Dev Board <https://www.sparkfun.com/products/11197>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA128RFA1
      - 16 MHz
      - 16 Kb
      - 124 Kb

    * - ``sparkfun_serial7seg``
      - `SparkFun Serial 7-Segment Display <https://www.sparkfun.com/products/11441>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 8 MHz
      - 32 Kb
      - 2 Kb

    * - ``uview``
      - `SparkFun MicroView <https://www.sparkfun.com/products/12923>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

SpellFoundry
~~~~~~~~~~~~

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

    * - ``sleepypi``
      - `SpellFoundry Sleepy Pi 2 <https://spellfoundry.com/product/sleepy-pi-2/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 8 MHz
      - 32 Kb
      - 2 Kb

The Things Network
~~~~~~~~~~~~~~~~~~

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

    * - ``the_things_uno``
      - `The Things Uno <https://shop.thethingsnetwork.com/index.php/product/the-things-uno/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

TinyCircuits
~~~~~~~~~~~~

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

    * - ``tinyduino``
      - `TinyCircuits TinyDuino Processor Board <https://tiny-circuits.com/tinyduino-processor-board.html>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 8 MHz
      - 32 Kb
      - 2 Kb

    * - ``tinylily``
      - `TinyCircuits TinyLily Mini Processor <https://tiny-circuits.com/tiny-lily-mini-processor.html>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 8 MHz
      - 32 Kb
      - 2 Kb

Wicked Device
~~~~~~~~~~~~~

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

    * - ``wildfirev2``
      - `Wicked Device WildFire V2 <http://shop.wickeddevice.com/resources/wildfire/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 16 MHz
      - 128 Kb
      - 16 Kb

    * - ``wildfirev3``
      - `Wicked Device WildFire V3 <http://shop.wickeddevice.com/resources/wildfire/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 16 MHz
      - 128 Kb
      - 16 Kb

makerlab.mx
~~~~~~~~~~~

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

    * - ``altair``
      - `Altair <http://www.aquila.io/en>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA256RFR2
      - 16 MHz
      - 256 Kb
      - 32 Kb

nicai-systems
~~~~~~~~~~~~~

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

    * - ``bob3``
      - `nicai-systems BOB3 coding bot <http://www.nicai-systems.com>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA88
      - 8 MHz
      - 8 Kb
      - 1 Kb

    * - ``nibo2``
      - `nicai-systems NIBO 2 robot <http://www.nicai-systems.com/en/nibo2>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA128
      - 16 MHz
      - 128 Kb
      - 4 Kb

    * - ``nibobee``
      - `nicai-systems NIBObee robot <http://www.nicai-systems.com/en/nibobee>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA16
      - 15 MHz
      - 16 Kb
      - 1 Kb

    * - ``nibobee_1284``
      - `nicai-systems NIBObee robot with Tuning Kit <http://www.nicai-systems.com/en/nibobee>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 20 MHz
      - 128 Kb
      - 16 Kb

    * - ``niboburger``
      - `nicai-systems NIBO burger robot <http://www.nicai-systems.com/en/nibo-burger>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA16
      - 15 MHz
      - 16 Kb
      - 1 Kb

    * - ``niboburger_1284``
      - `nicai-systems NIBO burger robot with Tuning Kit <http://www.nicai-systems.com/en/nibo-burger>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 20 MHz
      - 128 Kb
      - 16 Kb

ubIQio
~~~~~~

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

    * - ``ardhat``
      - `ubIQio Ardhat <http://ardhat.com>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

.. include:: atmelavr_extra.rst
