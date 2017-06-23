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

.. _embedded_boards:

Embedded Boards
===============

Rapid Embedded Development, Continuous and IDE integration in a few
steps with PlatformIO thanks to built-in project generator for the most
popular embedded boards and IDE.

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by horizontal.


.. contents:: Vendors
    :local:
    
4DSystems
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

    * - ``picadillo_35t``
      - `4DSystems PICadillo 35T <http://www.4dsystems.com.au/product/Picadillo_35T/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX795F512L
      - 80 MHz
      - 512 Kb
      - 128 Kb

96Boards
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

    * - ``b96b_f446ve``
      - `96Boards B96B-F446VE <https://developer.mbed.org/platforms/ST-B96B-F446VE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F446VET6
      - 168 MHz
      - 512 Kb
      - 128 Kb

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
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``adafruit_feather_m0_usb``
      - `Adafruit Feather M0 <https://www.adafruit.com/product/2772>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

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

    * - ``featheresp32``
      - `Adafruit ESP32 Feather <https://www.adafruit.com/product/3405>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

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

    * - ``huzzah``
      - `Adafruit HUZZAH ESP8266 <https://www.adafruit.com/products/2471>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

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

Aiyarafun
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

    * - ``node32s``
      - `Node32s <http://www.ayarafun.com>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

April Brother
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

    * - ``espea32``
      - `April Brother ESPea32 <https://blog.aprbrother.com/product/espea>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

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
      - `Arduino Industrial 101 <http://www.arduino.org/products/boards/4-arduino-boards/arduino-industrial-101>`_
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

    * - ``esplora``
      - `Arduino Esplora <http://www.arduino.org/products/boards/4-arduino-boards/arduino-esplora>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``ethernet``
      - `Arduino Ethernet <http://www.arduino.org/products/boards/4-arduino-boards/arduino-ethernet>`_
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
      - `Arduino Leonardo <http://www.arduino.org/products/boards/4-arduino-boards/arduino-leonardo>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``leonardoeth``
      - `Arduino Leonardo ETH <http://www.arduino.org/products/boards/4-arduino-boards/arduino-leonardo-eth>`_
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
      - `Arduino Mega ADK <http://www.arduino.org/products/boards/4-arduino-boards/arduino-mega-adk>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA2560
      - 16 MHz
      - 256 Kb
      - 8 Kb

    * - ``megaatmega1280``
      - `Arduino Mega or Mega 2560 ATmega1280 <http://www.arduino.org/products/boards/4-arduino-boards/arduino-mega-2560>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1280
      - 16 MHz
      - 128 Kb
      - 8 Kb

    * - ``megaatmega2560``
      - `Arduino Mega or Mega 2560 ATmega2560 (Mega 2560) <http://www.arduino.org/products/boards/4-arduino-boards/arduino-mega-2560>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA2560
      - 16 MHz
      - 256 Kb
      - 8 Kb

    * - ``micro``
      - `Arduino Micro <http://www.arduino.org/products/boards/4-arduino-boards/arduino-micro>`_
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

    * - ``mkr1000USB``
      - `Arduino MKR1000 <https://www.arduino.cc/en/Main/ArduinoMKR1000>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
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
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``mzeropro``
      - `Arduino M0 Pro (Programming/Debug Port) <http://www.arduino.org/products/boards/arduino-m0-pro>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
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

    * - ``nanoatmega168``
      - `Arduino Nano ATmega168 <http://www.arduino.org/products/boards/4-arduino-boards/arduino-nano>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA168
      - 16 MHz
      - 16 Kb
      - 1 Kb

    * - ``nanoatmega328``
      - `Arduino Nano ATmega328 <http://www.arduino.org/products/boards/4-arduino-boards/arduino-nano>`_
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
      - `Arduino Robot Control <http://www.arduino.org/products/boards/4-arduino-boards/arduino-robot>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``robotMotor``
      - `Arduino Robot Motor <http://www.arduino.org/products/boards/4-arduino-boards/arduino-robot>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``tian``
      - `Arduino Tian <http://www.arduino.org/products/boards/arduino-tian>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - 
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``uno``
      - `Arduino Uno <http://www.arduino.org/products/boards/4-arduino-boards/arduino-uno>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``yun``
      - `Arduino Yun <http://www.arduino.org/products/boards/4-arduino-boards/arduino-yun>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``yunmini``
      - `Arduino Yun Mini <http://www.arduino.org/products/boards/4-arduino-boards/arduino-yun-mini>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``zero``
      - `Arduino Zero (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
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

Armstrap
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

    * - ``armstrap_eagle1024``
      - `Armstrap Eagle 1024 <http://docs.armstrap.org/en/latest/hardware-overview.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F417VGT6
      - 168 MHz
      - 1024 Kb
      - 192 Kb

    * - ``armstrap_eagle2048``
      - `Armstrap Eagle 2048 <http://docs.armstrap.org/en/latest/hardware-overview.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F427VIT6
      - 168 MHz
      - 2048 Kb
      - 256 Kb

    * - ``armstrap_eagle512``
      - `Armstrap Eagle 512 <http://docs.armstrap.org/en/latest/hardware-overview.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F407VET6
      - 168 MHz
      - 512 Kb
      - 192 Kb

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
      - :ref:`Yes <piodebug>`
      - ATSAMD21J18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``samd21g18a``
      - `Atmel ATSAMW25-XPRO <https://developer.mbed.org/platforms/SAMW25-XPRO/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - ATSAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``saml21_xpro_b``
      - `Atmel SAML21-XPRO-B <https://developer.mbed.org/platforms/SAML21-XPRO/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - ATSAML21J18B
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``samr21_xpro``
      - `Atmel ATSAMR21-XPRO <https://developer.mbed.org/platforms/SAMR21-XPRO/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - ATSAMR21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

BBC
~~~

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

    * - ``bbcmicrobit``
      - `BBC micro:bit <https://developer.mbed.org/platforms/Microbit/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - 
      - NRF51822
      - 16 MHz
      - 256 Kb
      - 16 Kb

    * - ``bbcmicrobit_b``
      - `BBC micro:bit B(S130) <https://developer.mbed.org/platforms/Microbit/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - 
      - NRF51822
      - 16 MHz
      - 256 Kb
      - 16 Kb

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

CQ Publishing
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

    * - ``lpc11u35_501``
      - `CQ Publishing TG-LPC11U35-501 <https://developer.mbed.org/platforms/TG-LPC11U35-501/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC11U35
      - 48 MHz
      - 64 Kb
      - 10 Kb

DFRobot
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

    * - ``firebeetle32``
      - `FireBeetle-ESP32 <https://dfrobotblog.wordpress.com>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

DOIT
~~~~

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

    * - ``esp32doit-devkit-v1``
      - `DOIT ESP32 DEVKIT V1 <http://www.doit.am/>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

Delta
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

    * - ``delta_dfbm_nq620``
      - `Delta DFBM-NQ620 <https://developer.mbed.org/platforms/Delta-DFBM-NQ620/>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64 MHz
      - 512 Kb
      - 64 Kb

    * - ``dfcm_nnn40``
      - `Delta DFCM-NNN40 <https://developer.mbed.org/platforms/Delta-DFCM-NNN40/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32 MHz
      - 256 Kb
      - 32 Kb

Digilent
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

    * - ``cerebot32mx4``
      - `Digilent Cerebot 32MX4 <http://store.digilentinc.com/cerebot-32mx4-limited-time-see-chipkit-pro-mx4/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX460F512L
      - 80 MHz
      - 512 Kb
      - 32 Kb

    * - ``cerebot32mx7``
      - `Digilent Cerebot 32MX7 <http://www.microchip.com/Developmenttools/ProductDetails.aspx?PartNO=TDGL004>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX795F512L
      - 80 MHz
      - 512 Kb
      - 128 Kb

    * - ``chipkit_cmod``
      - `Digilent chipKIT Cmod <http://store.digilentinc.com/chipkit-cmod-breadboardable-mz-microcontroller-board/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX150F128D
      - 40 MHz
      - 128 Kb
      - 32 Kb

    * - ``chipkit_dp32``
      - `Digilent chipKIT DP32 <http://store.digilentinc.com/chipkit-dp32-dip-package-prototyping-microcontroller-board/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX250F128B
      - 40 MHz
      - 128 Kb
      - 32 Kb

    * - ``chipkit_mx3``
      - `Digilent chipKIT MX3 <http://store.digilentinc.com/chipkit-mx3-microcontroller-board-with-pmod-headers/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX320F128H
      - 80 MHz
      - 128 Kb
      - 16 Kb

    * - ``chipkit_pro_mx4``
      - `Digilent chipKIT Pro MX4 <http://store.digilentinc.com/chipkit-pro-mx4-embedded-systems-trainer-board/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX460F512L
      - 80 MHz
      - 512 Kb
      - 32 Kb

    * - ``chipkit_pro_mx7``
      - `Digilent chipKIT Pro MX7 <http://store.digilentinc.com/chipkit-pro-mx7-advanced-peripherals-embedded-systems-trainer-board/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX795F512L
      - 80 MHz
      - 512 Kb
      - 128 Kb

    * - ``chipkit_uc32``
      - `Digilent chipKIT uC32 <http://store.digilentinc.com/chipkit-uc32-basic-microcontroller-board-with-uno-r3-headers/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX340F512H
      - 80 MHz
      - 512 Kb
      - 32 Kb

    * - ``chipkit_wf32``
      - `Digilent chipKIT WF32 <http://store.digilentinc.com/chipkit-wf32-wifi-enabled-microntroller-board-with-uno-r3-headers/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX695F512L
      - 80 MHz
      - 512 Kb
      - 128 Kb

    * - ``chipkit_wifire``
      - `Digilent chipKIT WiFire <http://store.digilentinc.com/chipkit-wi-fire-wifi-enabled-mz-microcontroller-board/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MZ2048ECG100
      - 200 MHz
      - 2048 Kb
      - 512 Kb

    * - ``mega_pic32``
      - `Digilent chipKIT MAX32 <http://store.digilentinc.com/chipkit-max32-microcontroller-board-with-mega-r3-headers/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX795F512L
      - 80 MHz
      - 512 Kb
      - 128 Kb

    * - ``openscope``
      - `Digilent OpenScope <http://store.digilentinc.com/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MZ2048EFG124
      - 200 MHz
      - 2048 Kb
      - 512 Kb

    * - ``uno_pic32``
      - `Digilent chipKIT UNO32 <http://store.digilentinc.com/chipkit-uno32-basic-microcontroller-board-retired-see-chipkit-uc32/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX320F128H
      - 80 MHz
      - 128 Kb
      - 16 Kb

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
      - `Digistump Digispark Pro (Default 16 MHz) <http://digistump.com/products/109>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY167
      - 16 MHz
      - 16 Kb
      - 0.5 Kb

    * - ``digispark-pro32``
      - `Digistump Digispark Pro (16 MHz) (32 byte buffer) <http://digistump.com/products/109>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY167
      - 16 MHz
      - 16 Kb
      - 0.5 Kb

    * - ``digispark-pro64``
      - `Digistump Digispark Pro (16 MHz) (64 byte buffer) <http://digistump.com/products/109>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY167
      - 16 MHz
      - 16 Kb
      - 0.5 Kb

    * - ``digispark-tiny``
      - `Digistump Digispark (Default - 16 MHz) <http://digistump.com/products/1>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATTINY85
      - 16 MHz
      - 8 Kb
      - 0.5 Kb

    * - ``digix``
      - `Digistump DigiX <http://digistump.com/products/50>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - 
      - AT91SAM3X8E
      - 84 MHz
      - 512 Kb
      - 28 Kb

Doit
~~~~

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

    * - ``espduino``
      - `ESPDuino (ESP-13 Module) <https://www.tindie.com/products/doit/espduinowifi-uno-r3/>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

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

DycodeX
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

    * - ``espectro``
      - `ESPrectro Core <https://shop.makestro.com/en/product/espectro-core/>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

ESP32vn
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

    * - ``esp32vn-iot-uno``
      - `ESP32vn IoT Uno <https://esp32.vn/>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1024 Kb
      - 288 Kb

ESPert
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

    * - ``espresso_lite_v1``
      - `ESPresso Lite 1.0 <http://www.espert.co>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``espresso_lite_v2``
      - `ESPresso Lite 2.0 <http://www.espert.co>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

ESPino
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

    * - ``espino``
      - `ESPino <http://www.espino.io>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

Electronic SweetPeas
~~~~~~~~~~~~~~~~~~~~

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

    * - ``esp320``
      - `Electronic SweetPeas ESP320 <http://www.sweetpeas.se/controller-modules/10-esp210.html>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

Elektor Labs
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

    * - ``elektor_cocorico``
      - `CoCo-ri-Co! <https://developer.mbed.org/platforms/CoCo-ri-Co/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC812
      - 30 MHz
      - 16 Kb
      - 4 Kb

Embedded Artists
~~~~~~~~~~~~~~~~

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

    * - ``lpc11u35``
      - `EA LPC11U35 QuickStart Board <https://developer.mbed.org/platforms/EA-LPC11U35/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC11U35
      - 48 MHz
      - 64 Kb
      - 10 Kb

    * - ``lpc4088``
      - `Embedded Artists LPC4088 QuickStart Board <https://developer.mbed.org/platforms/EA-LPC4088/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC4088
      - 120 MHz
      - 512 Kb
      - 96 Kb

    * - ``lpc4088_dm``
      - `Embedded Artists LPC4088 Display Module <https://developer.mbed.org/platforms/EA-LPC4088-Display-Module/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC4088
      - 120 MHz
      - 512 Kb
      - 96 Kb

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

Espotel
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

    * - ``elmo_f411re``
      - `Espotel LoRa Module <https://developer.mbed.org/platforms/Espotel-ELMO/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100 MHz
      - 512 Kb
      - 128 Kb

Espressif
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

    * - ``esp01``
      - `Espressif Generic ESP8266 ESP-01 512k <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 512 Kb
      - 80 Kb

    * - ``esp01_1m``
      - `Espressif Generic ESP8266 ESP-01 1M <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 1024 Kb
      - 80 Kb

    * - ``esp07``
      - `Espressif Generic ESP8266 ESP-07 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family#esp-07>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``esp12e``
      - `Espressif ESP8266 ESP-12E <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``esp32dev``
      - `Espressif ESP32 Dev Module <https://en.wikipedia.org/wiki/ESP32>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

    * - ``esp8285``
      - `Generic ESP8285 Module <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 448 Kb
      - 80 Kb

    * - ``esp_wroom_02``
      - `ESP-WROOM-02 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``phoenix_v1``
      - `Phoenix 1.0 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 1024 Kb
      - 80 Kb

    * - ``phoenix_v2``
      - `Phoenix 2.0 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 1024 Kb
      - 80 Kb

    * - ``wifinfo``
      - `WifInfo <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 448 Kb
      - 80 Kb

FPGAwars
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

    * - ``icezum``
      - `IceZUM Alhambra FPGA <https://github.com/FPGAwars/icezum/wiki>`_
      - :ref:`Lattice iCE40 <platform_lattice_ice40>`
      - 
      - ICE40-HX1K-TQ144
      - 12 MHz
      - 32 Kb
      - 32 Kb

Freescale
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

    * - ``IBMEthernetKit``
      - `Ethernet IoT Starter Kit <http://developer.mbed.org/platforms/IBMEthernetKit/>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MK64FN1M0VLL12
      - 120 MHz
      - 1024 Kb
      - 256 Kb

    * - ``frdm_k20d50m``
      - `Freescale Kinetis FRDM-K20D50M <https://developer.mbed.org/platforms/FRDM-K20D50M/>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MK20DX128VLH5
      - 48 MHz
      - 128 Kb
      - 16 Kb

    * - ``frdm_k22f``
      - `Freescale Kinetis FRDM-K22F <https://developer.mbed.org/platforms/FRDM-K22F/>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MK22FN512VLH12
      - 120 MHz
      - 512 Kb
      - 128 Kb

    * - ``frdm_k64f``
      - `Freescale Kinetis FRDM-K64F <https://developer.mbed.org/platforms/FRDM-K64F/>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MK64FN1M0VLL12
      - 120 MHz
      - 1024 Kb
      - 256 Kb

    * - ``frdm_kl05z``
      - `Freescale Kinetis FRDM-KL05Z <https://developer.mbed.org/platforms/FRDM-KL05Z/>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL05Z32VFM4
      - 48 MHz
      - 32 Kb
      - 4 Kb

    * - ``frdm_kl25z``
      - `Freescale Kinetis FRDM-KL25Z <https://developer.mbed.org/platforms/KL25Z/>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL25Z128VLK4
      - 48 MHz
      - 128 Kb
      - 16 Kb

    * - ``frdm_kl26z``
      - `Freescale Kinetis FRDM-KL26Z <http://www.nxp.com/products/software-and-tools/hardware-development-tools/freedom-development-boards/freedom-development-platform-for-kinetis-kl16-and-kl26-mcus-up-to-128-kb-flash:FRDM-KL26Z>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL26Z128VLH4
      - 48 MHz
      - 128 Kb
      - 16 Kb

    * - ``frdm_kl27z``
      - `Freescale Kinetis FRDM-KL27Z <http://www.nxp.com/products/software-and-tools/hardware-development-tools/freedom-development-boards/freedom-development-platform-for-kinetis-kl17-and-kl27-mcus:FRDM-KL27Z>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL27Z64VLH4
      - 48 MHz
      - 64 Kb
      - 16 Kb

    * - ``frdm_kl43z``
      - `Freescale Kinetis FRDM-KL43Z <http://www.nxp.com/products/software-and-tools/hardware-development-tools/freedom-development-boards/freedom-development-platform-for-kinetis-kl43-kl33-kl27-kl17-and-kl13-mcus:FRDM-KL43Z>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL43Z256VLH4
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``frdm_kl46z``
      - `Freescale Kinetis FRDM-KL46Z <https://developer.mbed.org/platforms/FRDM-KL46Z/>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL46Z256VLL4
      - 48 MHz
      - 256 Kb
      - 32 Kb

Fubarino
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

    * - ``fubarino_mini``
      - `Fubarino Mini <http://fubarino.org/mini/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX250F128D
      - 48 MHz
      - 128 Kb
      - 32 Kb

    * - ``fubarino_sd``
      - `Fubarino SD (1.5) <http://fubarino.org/sd/index.html>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX795F512H
      - 80 MHz
      - 512 Kb
      - 128 Kb

GHI Electronics
~~~~~~~~~~~~~~~

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

    * - ``oc_mbuino``
      - `mBuino <https://developer.mbed.org/platforms/mBuino/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC11U24
      - 50 MHz
      - 32 Kb
      - 10 Kb

Generic
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

    * - ``bluepill_f103c8``
      - `BluePill F103C8 <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103C8T6
      - 72 MHz
      - 64 Kb
      - 20 Kb

    * - ``genericSTM32F103C8``
      - `STM32F103C8 (20k RAM. 64k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103C8
      - 72 MHz
      - 64 Kb
      - 20 Kb

    * - ``genericSTM32F103CB``
      - `STM32F103CB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103cb.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103CB
      - 72 MHz
      - 128 Kb
      - 20 Kb

    * - ``genericSTM32F103R8``
      - `STM32F103R8 (20k RAM. 64 Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103r8.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103R8
      - 72 MHz
      - 64 Kb
      - 20 Kb

    * - ``genericSTM32F103RB``
      - `STM32F103RB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rb.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RB
      - 72 MHz
      - 128 Kb
      - 20 Kb

    * - ``genericSTM32F103RC``
      - `STM32F103RC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rc.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RC
      - 72 MHz
      - 256 Kb
      - 48 Kb

    * - ``genericSTM32F103RE``
      - `STM32F103RE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103re.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RE
      - 72 MHz
      - 512 Kb
      - 64 Kb

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

Hornbill
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

    * - ``hornbill32dev``
      - `Hornbill ESP32 Dev <https://hackaday.io/project/18997-hornbill>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

    * - ``hornbill32minima``
      - `Hornbill ESP32 Minima <https://hackaday.io/project/18997-hornbill>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

Intel
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

    * - ``genuino101``
      - `Arduino/Genuino 101 <https://www.arduino.cc/en/Main/ArduinoBoard101>`_
      - :ref:`Intel ARC32 <platform_intel_arc32>`
      - 
      - ARCV2EM
      - 32 MHz
      - 192 Kb
      - 80 Kb

IntoRobot
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

    * - ``intorobot``
      - `IntoRobot Fig <http://docs.intorobot.com/zh/hardware/fig/hardware/>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

JKSoft
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

    * - ``wallbot_ble``
      - `JKSoft Wallbot BLE <https://developer.mbed.org/platforms/JKSoft-Wallbot-BLE/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 128 Kb
      - 16 Kb

Lattice
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

    * - ``icestick``
      - `Lattice iCEstick FPGA Evaluation Kit <http://www.latticesemi.com/icestick>`_
      - :ref:`Lattice iCE40 <platform_lattice_ice40>`
      - 
      - ICE40-HX1K-TQ144
      - 12 MHz
      - 32 Kb
      - 32 Kb

LeafLabs
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

    * - ``maple``
      - `Maple <http://www.leaflabs.com/maple/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - 
      - STM32F103RB
      - 72 MHz
      - 128 Kb
      - 17 Kb

    * - ``maple_mini_b20``
      - `Maple Mini Bootloader 2.0 <http://www.leaflabs.com/maple/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - 
      - STM32F103CB
      - 72 MHz
      - 128 Kb
      - 20 Kb

    * - ``maple_mini_origin``
      - `Maple Mini Original <http://www.leaflabs.com/maple/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - 
      - STM32F103CB
      - 72 MHz
      - 128 Kb
      - 17 Kb

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

MakerAsia
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

    * - ``nano32``
      - `MakerAsia Nano32 <http://iot-bits.com/nano32-esp32-development-board>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

Maxim
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

    * - ``max32600mbed``
      - `Maxim ARM mbed Enabled Development Platform for MAX32600 <https://developer.mbed.org/platforms/MAX32600mbed/>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - 
      - MAX32600
      - 24 MHz
      - 256 Kb
      - 32 Kb

    * - ``max32620hsp``
      - `Maxim Health Sensor Platform <https://developer.mbed.org/platforms/MAX32620HSP/>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - 
      - MAX32620
      - 96 MHz
      - 2048 Kb
      - 256 Kb

    * - ``max32630fthr``
      - `Maxim MAX32630FTHR Application Platform <https://developer.mbed.org/platforms/MAX32630FTHR/>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - 
      - MAX32630
      - 96 MHz
      - 2048 Kb
      - 512 Kb

    * - ``maxwsnenv``
      - `Maxim Wireless Sensor Node Demonstrator <https://developer.mbed.org/platforms/MAXWSNENV/>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - 
      - MAX32610
      - 24 MHz
      - 256 Kb
      - 32 Kb

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
      - `Microduino Core+ (ATmega1284P@16M,5V) <https://www.microduino.cc/wiki/index.php?title=Microduino-Core%2B>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 16 MHz
      - 128 Kb
      - 16 Kb

    * - ``1284p8m``
      - `Microduino Core+ (ATmega1284P@8M,3.3V) <https://www.microduino.cc/wiki/index.php?title=Microduino-Core%2B>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 8 MHz
      - 128 Kb
      - 16 Kb

    * - ``168pa16m``
      - `Microduino Core (Atmega168PA@16M,5V) <https://www.microduino.cc/wiki/index.php?title=Microduino-Core>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA168P
      - 16 MHz
      - 16 Kb
      - 1 Kb

    * - ``168pa8m``
      - `Microduino Core (Atmega168PA@8M,3.3V) <https://www.microduino.cc/wiki/index.php?title=Microduino-Core>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA168P
      - 8 MHz
      - 16 Kb
      - 1 Kb

    * - ``328p16m``
      - `Microduino Core (Atmega328P@16M,5V) <https://www.microduino.cc/wiki/index.php?title=Microduino-Core>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``328p8m``
      - `Microduino Core (Atmega328P@8M,3.3V) <https://www.microduino.cc/wiki/index.php?title=Microduino-Core>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 8 MHz
      - 32 Kb
      - 2 Kb

    * - ``32u416m``
      - `Microduino Core USB (ATmega32U4@16M,5V) <https://www.microduino.cc/wiki/index.php?title=Microduino-CoreUSB>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``644pa16m``
      - `Microduino Core+ (Atmega644PA@16M,5V) <https://www.microduino.cc/wiki/index.php?title=Microduino-Core%2B>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA644P
      - 16 MHz
      - 64 Kb
      - 4 Kb

    * - ``644pa8m``
      - `Microduino Core+ (Atmega644PA@8M,3.3V) <https://www.microduino.cc/wiki/index.php?title=Microduino-Core%2B>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA644P
      - 8 MHz
      - 64 Kb
      - 4 Kb

Micromint
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

    * - ``lpc4330_m4``
      - `Bambino-210E <https://developer.mbed.org/platforms/Micromint-Bambino-210E/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC4330
      - 204 MHz
      - 8192 Kb
      - 264 Kb

    * - ``lpc4337``
      - `LPCXpresso4337 <https://developer.mbed.org/platforms/LPCXpresso4337/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC4337
      - 204 MHz
      - 1024 Kb
      - 136 Kb

MikroElektronika
~~~~~~~~~~~~~~~~

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

    * - ``clicker2``
      - `MikroElektronika Clicker 2 <http://www.mikroe.com/pic/clicker/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX460F512L
      - 80 MHz
      - 512 Kb
      - 32 Kb

    * - ``hexiwear``
      - `Hexiwear <https://developer.mbed.org/platforms/Hexiwear/>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MK64FN1M0VDC12
      - 120 MHz
      - 1024 Kb
      - 256 Kb

MultiTech
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

    * - ``mts_dragonfly_f411re``
      - `MTS Dragonfly <https://developer.mbed.org/platforms/MTS-Dragonfly/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100 MHz
      - 512 Kb
      - 128 Kb

    * - ``mts_mdot_f405rg``
      - `MultiTech mDot <https://developer.mbed.org/platforms/MTS-mDot-F411/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100 MHz
      - 512 Kb
      - 128 Kb

    * - ``mts_mdot_f411re``
      - `MultiTech mDot F411 <https://developer.mbed.org/platforms/MTS-mDot-F411/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100 MHz
      - 512 Kb
      - 128 Kb

    * - ``xdot_l151cc``
      - `MultiTech xDot <https://developer.mbed.org/platforms/MTS-xDot-L151CC/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - 
      - STM32L151CCU6
      - 32 MHz
      - 256 Kb
      - 32 Kb

NGX Technologies
~~~~~~~~~~~~~~~~

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

    * - ``blueboard_lpc11u24``
      - `NGX Technologies BlueBoard-LPC11U24 <https://developer.mbed.org/platforms/BlueBoard-LPC11U24/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC11U24
      - 48 MHz
      - 32 Kb
      - 8 Kb

NXP
~~~

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

    * - ``lpc11c24``
      - `NXP LPC11C24 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-m0-cores:LPC11C24FBD48>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC11C24
      - 48 MHz
      - 32 Kb
      - 8 Kb

    * - ``lpc11u24``
      - `NXP mbed LPC11U24 <https://developer.mbed.org/platforms/mbed-LPC11U24/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U24
      - 48 MHz
      - 32 Kb
      - 8 Kb

    * - ``lpc11u24_301``
      - `ARM mbed LPC11U24 (+CAN) <https://developer.mbed.org/handbook/mbed-NXP-LPC11U24>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U24
      - 48 MHz
      - 32 Kb
      - 8 Kb

    * - ``lpc11u34_421``
      - `NXP LPC11U34 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/40kb-flash-8kb-sram-lqfp48-package:LPC11U34FBD48?lang_cd=en>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC11U34
      - 48 MHz
      - 64 Kb
      - 8 Kb

    * - ``lpc11u37_501``
      - `NXP LPC11U37 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/128kb-flash-10kb-sram-lqfp48-package:LPC11U37FBD48?lang_cd=en>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC11U37
      - 48 MHz
      - 128 Kb
      - 10 Kb

    * - ``lpc11u68``
      - `LPCXpresso11U68 <https://developer.mbed.org/platforms/LPCXpresso11U68/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U68
      - 50 MHz
      - 256 Kb
      - 36 Kb

    * - ``lpc1549``
      - `NXP LPCXpresso1549 <https://developer.mbed.org/platforms/LPCXpresso1549/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC1549
      - 72 MHz
      - 256 Kb
      - 36 Kb

    * - ``lpc1768``
      - `NXP mbed LPC1768 <http://developer.mbed.org/platforms/mbed-LPC1768/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC1768
      - 96 MHz
      - 512 Kb
      - 64 Kb

    * - ``lpc2368``
      - `NXP LPC2368 <https://developer.mbed.org/platforms/mbed-LPC2368/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC2368
      - 72 MHz
      - 512 Kb
      - 58 Kb

    * - ``lpc2460``
      - `NXP LPC2460 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-arm7-arm9-mcus/lpc-arm7-mcus/lpc2100-200-300-400/flashless-16-bit-32-bit-microcontroller-ethernet-can-isp-iap-usb-2.0-device-host-otg-external-memory-interface:LPC2460FBD208>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC2460
      - 72 MHz
      - 64 Kb
      - 16 Kb

    * - ``lpc812``
      - `NXP LPC800-MAX <https://developer.mbed.org/platforms/NXP-LPC800-MAX/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC812
      - 30 MHz
      - 16 Kb
      - 4 Kb

    * - ``lpc824``
      - `LPCXpresso824-MAX <https://developer.mbed.org/platforms/LPCXpresso824-MAX/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC824
      - 30 MHz
      - 32 Kb
      - 8 Kb

    * - ``micronfcboard``
      - `MicroNFCBoard <https://developer.mbed.org/platforms/MicroNFCBoard/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC11U34
      - 48 MHz
      - 64 Kb
      - 10 Kb

NodeMCU
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

    * - ``nodemcu``
      - `NodeMCU 0.9 (ESP-12 Module) <http://www.nodemcu.com/>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``nodemcu-32s``
      - `NodeMCU-32S <http://www.nodemcu.com/>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

    * - ``nodemcuv2``
      - `NodeMCU 1.0 (ESP-12E Module) <http://www.nodemcu.com/>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

Noduino
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

    * - ``quantum``
      - `Noduino Quantum <http://wiki.jackslab.org/Noduino>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

Nordic
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

    * - ``nrf51_dk``
      - `Nordic nRF51-DK <https://developer.mbed.org/platforms/Nordic-nRF51-DK/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32 MHz
      - 256 Kb
      - 32 Kb

    * - ``nrf51_dongle``
      - `Nordic nRF51-Dongle <https://developer.mbed.org/platforms/Nordic-nRF51-Dongle/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32 MHz
      - 256 Kb
      - 32 Kb

    * - ``nrf51_mkit``
      - `Nordic nRF51822-mKIT <http://developer.mbed.org/platforms/Nordic-nRF51822/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 128 Kb
      - 16 Kb

    * - ``nrf52_dk``
      - `Nordic nRF52-DK <https://developer.mbed.org/platforms/Nordic-nRF52-DK/>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64 MHz
      - 512 Kb
      - 64 Kb

Olimex
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

    * - ``modwifi``
      - `Olimex MOD-WIFI-ESP8266(-DEV) <https://www.olimex.com/Products/IoT/MOD-WIFI-ESP8266-DEV/open-source-hardware>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 2048 Kb
      - 80 Kb

    * - ``pinguino32``
      - `Olimex PIC32-PINGUINO <https://www.olimex.com/Products/Duino/PIC32/PIC32-PINGUINO/open-source-hardware>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX440F256H
      - 80 MHz
      - 256 Kb
      - 32 Kb

Onehorse
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

    * - ``onehorse32dev``
      - `Onehorse ESP32 Dev Module <https://www.tindie.com/products/onehorse/esp32-development-board/>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

OpenBCI
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

    * - ``openbci``
      - `OpenBCI 32bit <http://shop.openbci.com/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX250F128B
      - 40 MHz
      - 128 Kb
      - 32 Kb

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

Outrageous Circuits
~~~~~~~~~~~~~~~~~~~

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

    * - ``mbuino``
      - `Outrageous Circuits mBuino <https://developer.mbed.org/platforms/Outrageous-Circuits-mBuino/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC11U24
      - 48 MHz
      - 32 Kb
      - 8 Kb

PONTECH
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

    * - ``quick240_usb``
      - `PONTECH quicK240 <http://quick240.com/quicki/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX795F512L
      - 80 MHz
      - 512 Kb
      - 128 Kb

    * - ``usbono_pic32``
      - `PONTECH UAV100 <http://www.pontech.com/productdisplay/uav100>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX440F512H
      - 80 MHz
      - 512 Kb
      - 32 Kb

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

    * - ``panStampNRG``
      - `PanStamp NRG 1.1 <http://www.panstamp.com/product/197/>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - 
      - CC430F5137
      - 12 MHz
      - 32 Kb
      - 4 Kb

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

RFduino
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

    * - ``rfduino``
      - `RFduino <http://www.rfduino.com/product/rfd22102-rfduino-dip/index.html>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - 
      - NRF51822
      - 16 MHz
      - 128 Kb
      - 8 Kb

Raspberry Pi
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

    * - ``raspberrypi_1b``
      - `Raspberry Pi 1 Model B <https://www.raspberrypi.org>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - 
      - BCM2835
      - 700 MHz
      - 524288 Kb
      - 524288 Kb

    * - ``raspberrypi_2b``
      - `Raspberry Pi 2 Model B <https://www.raspberrypi.org>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - 
      - BCM2836
      - 900 MHz
      - 1048576 Kb
      - 1048576 Kb

    * - ``raspberrypi_3b``
      - `Raspberry Pi 3 Model B <https://www.raspberrypi.org>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - 
      - BCM2837
      - 1200 MHz
      - 1048576 Kb
      - 1048576 Kb

    * - ``raspberrypi_zero``
      - `Raspberry Pi Zero <https://www.raspberrypi.org>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - 
      - BCM2835
      - 1000 MHz
      - 524288 Kb
      - 524288 Kb

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

    * - ``redBearLab``
      - `RedBearLab nRF51822 <https://developer.mbed.org/platforms/RedBearLab-nRF51822/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 256 Kb
      - 16 Kb

    * - ``redBearLabBLENano``
      - `RedBearLab BLE Nano <https://developer.mbed.org/platforms/RedBearLab-BLE-Nano/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 256 Kb
      - 32 Kb

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

    * - ``sodaq_one``
      - `SODAQ ONE <http://support.sodaq.com/sodaq-one/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - 
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``sodaq_tatu``
      - `SODAQ Tatu <http://support.sodaq.com/>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA1284P
      - 8 MHz
      - 128 Kb
      - 16 Kb

    * - ``sodaq_wdt``
      - `SODAQ WDT <http://support.sodaq.com/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - 
      - SAMD21J18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

ST
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

    * - ``disco_f030r8``
      - `ST STM32F0308DISCOVERY <http://www.st.com/en/evaluation-tools/32f0308discovery.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F030R8T6
      - 48 MHz
      - 64 Kb
      - 8 Kb

    * - ``disco_f051r8``
      - `ST STM32F0DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF253215>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F051R8T6
      - 48 MHz
      - 64 Kb
      - 8 Kb

    * - ``disco_f100rb``
      - `ST STM32VLDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF250863>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F100RBT6
      - 24 MHz
      - 128 Kb
      - 8 Kb

    * - ``disco_f303vc``
      - `ST STM32F3DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF254044>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F303VCT6
      - 72 MHz
      - 256 Kb
      - 48 Kb

    * - ``disco_f334c8``
      - `ST 32F3348DISCOVERY <http://www.st.com/web/en/catalog/tools/PF260318>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F334C8T6
      - 72 MHz
      - 64 Kb
      - 12 Kb

    * - ``disco_f401vc``
      - `ST 32F401CDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF259098>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F401VCT6
      - 84 MHz
      - 256 Kb
      - 64 Kb

    * - ``disco_f407vg``
      - `ST STM32F4DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF252419>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F407VGT6
      - 168 MHz
      - 1024 Kb
      - 128 Kb

    * - ``disco_f411ve``
      - `ST 32F411EDISCOVERY <http://www.st.com/en/evaluation-tools/32f411ediscovery.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411VET6
      - 100 MHz
      - 512 Kb
      - 128 Kb

    * - ``disco_f429zi``
      - `ST 32F429IDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF259090>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F429ZIT6
      - 180 MHz
      - 2048 Kb
      - 256 Kb

    * - ``disco_f469ni``
      - `ST 32F469IDISCOVERY <http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF262395>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F469NIH6
      - 180 MHz
      - 1024 Kb
      - 384 Kb

    * - ``disco_f746ng``
      - `ST 32F746GDISCOVERY <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/32f746gdiscovery.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F746NGH6
      - 216 MHz
      - 1024 Kb
      - 320 Kb

    * - ``disco_f769ni``
      - `ST 32F769IDISCOVERY <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/32f769idiscovery.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F769NIH6
      - 80 MHz
      - 1024 Kb
      - 512 Kb

    * - ``disco_l053c8``
      - `ST 32L0538DISCOVERY <http://www.st.com/web/en/catalog/tools/PF260319>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L053C8T6
      - 32 MHz
      - 64 Kb
      - 8 Kb

    * - ``disco_l072cz_lrwan1``
      - `ST DISCO-L072CZ-LRWAN1 <https://developer.mbed.org/platforms/ST-Discovery-LRWAN1/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L072CZ
      - 32 MHz
      - 192 Kb
      - 20 Kb

    * - ``disco_l152rb``
      - `ST STM32LDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF258515>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L152RBT6
      - 32 MHz
      - 128 Kb
      - 16 Kb

    * - ``disco_l476vg``
      - `ST 32L476GDISCOVERY <http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF261635>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L476VGT6
      - 80 MHz
      - 1024 Kb
      - 128 Kb

    * - ``nucleo_f030r8``
      - `ST Nucleo F030R8 <https://developer.mbed.org/platforms/ST-Nucleo-F030R8/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F030R8T6
      - 48 MHz
      - 64 Kb
      - 8 Kb

    * - ``nucleo_f031k6``
      - `ST Nucleo F031K6 <https://developer.mbed.org/platforms/ST-Nucleo-F031K6/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F031K6T6
      - 48 MHz
      - 32 Kb
      - 4 Kb

    * - ``nucleo_f042k6``
      - `ST Nucleo F042K6 <https://developer.mbed.org/platforms/ST-Nucleo-F042K6/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F042K6T6
      - 48 MHz
      - 32 Kb
      - 6 Kb

    * - ``nucleo_f070rb``
      - `ST Nucleo F070RB <https://developer.mbed.org/platforms/ST-Nucleo-F070RB/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F070RBT6
      - 48 MHz
      - 128 Kb
      - 16 Kb

    * - ``nucleo_f072rb``
      - `ST Nucleo F072RB <https://developer.mbed.org/platforms/ST-Nucleo-F072RB/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F072RBT6
      - 48 MHz
      - 128 Kb
      - 16 Kb

    * - ``nucleo_f091rc``
      - `ST Nucleo F091RC <https://developer.mbed.org/platforms/ST-Nucleo-F091RC/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F091RCT6
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``nucleo_f103rb``
      - `ST Nucleo F103RB <https://developer.mbed.org/platforms/ST-Nucleo-F103RB/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RBT6
      - 72 MHz
      - 128 Kb
      - 20 Kb

    * - ``nucleo_f207zg``
      - `ST Nucleo F207ZG <https://developer.mbed.org/platforms/ST-Nucleo-F207ZG/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F207ZGT6
      - 120 MHz
      - 1024 Kb
      - 128 Kb

    * - ``nucleo_f302r8``
      - `ST Nucleo F302R8 <https://developer.mbed.org/platforms/ST-Nucleo-F302R8/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F302R8T6
      - 72 MHz
      - 64 Kb
      - 16 Kb

    * - ``nucleo_f303k8``
      - `ST Nucleo F303K8 <https://developer.mbed.org/platforms/ST-Nucleo-F303K8/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F303K8T6
      - 72 MHz
      - 64 Kb
      - 16 Kb

    * - ``nucleo_f303re``
      - `ST Nucleo F303RE <http://developer.mbed.org/platforms/ST-Nucleo-F303RE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F303RET6
      - 72 MHz
      - 512 Kb
      - 64 Kb

    * - ``nucleo_f303ze``
      - `ST Nucleo F303ZE <https://developer.mbed.org/platforms/ST-Nucleo-F303ZE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F303ZET6
      - 72 MHz
      - 512 Kb
      - 64 Kb

    * - ``nucleo_f334r8``
      - `ST Nucleo F334R8 <https://developer.mbed.org/platforms/ST-Nucleo-F334R8/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F334R8T6
      - 72 MHz
      - 64 Kb
      - 16 Kb

    * - ``nucleo_f401re``
      - `ST Nucleo F401RE <https://developer.mbed.org/platforms/ST-Nucleo-F401RE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F401RET6
      - 84 MHz
      - 512 Kb
      - 96 Kb

    * - ``nucleo_f410rb``
      - `ST Nucleo F410RB <https://developer.mbed.org/platforms/ST-Nucleo-F410RB/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F410RBT6
      - 100 MHz
      - 128 Kb
      - 32 Kb

    * - ``nucleo_f411re``
      - `ST Nucleo F411RE <https://developer.mbed.org/platforms/ST-Nucleo-F411RE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100 MHz
      - 512 Kb
      - 128 Kb

    * - ``nucleo_f412zg``
      - `ST Nucleo F412ZG <https://developer.mbed.org/platforms/ST-Nucleo-F411RE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F412ZGT6
      - 100 MHz
      - 1024 Kb
      - 256 Kb

    * - ``nucleo_f429zi``
      - `ST Nucleo F429ZI <https://developer.mbed.org/platforms/ST-Nucleo-F429ZI/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F429ZIT6
      - 180 MHz
      - 2048 Kb
      - 256 Kb

    * - ``nucleo_f446re``
      - `ST Nucleo F446RE <https://developer.mbed.org/platforms/ST-Nucleo-F446RE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F446RET6
      - 180 MHz
      - 512 Kb
      - 128 Kb

    * - ``nucleo_f446ze``
      - `ST Nucleo F446ZE <https://developer.mbed.org/platforms/ST-Nucleo-F446ZE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F446ZET6
      - 180 MHz
      - 512 Kb
      - 128 Kb

    * - ``nucleo_f746zg``
      - `ST Nucleo F746ZG <https://developer.mbed.org/platforms/ST-Nucleo-F446ZE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F746ZGT6
      - 216 MHz
      - 1024 Kb
      - 320 Kb

    * - ``nucleo_f767zi``
      - `ST Nucleo F767ZI <https://developer.mbed.org/platforms/ST-Nucleo-F767ZI/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F767ZIT6
      - 216 MHz
      - 2048 Kb
      - 512 Kb

    * - ``nucleo_l011k4``
      - `ST Nucleo L011K4 <https://developer.mbed.org/platforms/ST-Nucleo-L011K4/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L011K4T6
      - 32 MHz
      - 16 Kb
      - 2 Kb

    * - ``nucleo_l031k6``
      - `ST Nucleo L031K6 <https://developer.mbed.org/platforms/ST-Nucleo-L031K6/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L031K6T6
      - 32 MHz
      - 32 Kb
      - 8 Kb

    * - ``nucleo_l053r8``
      - `ST Nucleo L053R8 <https://developer.mbed.org/platforms/ST-Nucleo-L053R8/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L053R8T6
      - 48 MHz
      - 64 Kb
      - 8 Kb

    * - ``nucleo_l073rz``
      - `ST Nucleo L073RZ <https://developer.mbed.org/platforms/ST-Nucleo-L073RZ/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L073RZ
      - 32 MHz
      - 192 Kb
      - 20 Kb

    * - ``nucleo_l152re``
      - `ST Nucleo L152RE <https://developer.mbed.org/platforms/ST-Nucleo-L152RE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L152RET6
      - 32 MHz
      - 512 Kb
      - 80 Kb

    * - ``nucleo_l432kc``
      - `ST Nucleo L432KC <https://developer.mbed.org/platforms/ST-Nucleo-L432KC/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L432KCU6
      - 80 MHz
      - 256 Kb
      - 64 Kb

    * - ``nucleo_l476rg``
      - `ST Nucleo L476RG <https://developer.mbed.org/platforms/ST-Nucleo-L476RG/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L476RGT6
      - 80 MHz
      - 1024 Kb
      - 128 Kb

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

Samsung
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

    * - ``artik_1020``
      - `Samsung ARTIK 1020 <https://www.artik.io>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - 
      - EXYNOS5422
      - 1500 MHz
      - 16777216 Kb
      - 2097152 Kb

    * - ``artik_520``
      - `Samsung ARTIK 520 <https://www.artik.io>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - 
      - EXYNOS3250
      - 1000 MHz
      - 4194304 Kb
      - 524288 Kb

    * - ``artik_530``
      - `Samsung ARTIK 530 <https://www.artik.io>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - 
      - S5P4418
      - 1200 MHz
      - 4194304 Kb
      - 524288 Kb

    * - ``artik_710``
      - `Samsung ARTIK 710 <https://www.artik.io>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - 
      - S5P6818
      - 1400 MHz
      - 4194304 Kb
      - 1048576 Kb

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

    * - ``cui32stem``
      - `SeeedStudio CUI32stem <http://www.seeedstudio.com/wiki/CUI32Stem>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX795F512H
      - 80 MHz
      - 512 Kb
      - 128 Kb

    * - ``seeedArchBLE``
      - `Seeed Arch BLE <https://developer.mbed.org/platforms/Seeed-Arch-BLE/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 128 Kb
      - 16 Kb

    * - ``seeedArchGPRS``
      - `Seeed Arch GPRS V2 <https://www.seeedstudio.com/Arch-GPRS-V2-p-2026.html>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC11U37
      - 48 MHz
      - 128 Kb
      - 10 Kb

    * - ``seeedArchLink``
      - `Seeed Arch Link <https://developer.mbed.org/platforms/Seeed-Arch-Link/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 256 Kb
      - 16 Kb

    * - ``seeedArchMax``
      - `Seeed Arch Max <https://developer.mbed.org/platforms/Seeed-Arch-Max/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F407VET6
      - 168 MHz
      - 512 Kb
      - 192 Kb

    * - ``seeedArchPro``
      - `Seeed Arch Pro <https://developer.mbed.org/platforms/Seeeduino-Arch-Pro/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC1768
      - 96 MHz
      - 512 Kb
      - 64 Kb

    * - ``seeedTinyBLE``
      - `Seeed Tiny BLE <http://developer.mbed.org/platforms/Seeed-Tiny-BLE/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 256 Kb
      - 16 Kb

    * - ``xadow_m0``
      - `Seeed Xadow M0 <https://developer.mbed.org/platforms/Seeed-Xadow-M0/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC11U35
      - 48 MHz
      - 64 Kb
      - 10 Kb

Semtech
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

    * - ``mote_l152rc``
      - `NAMote72 <https://developer.mbed.org/platforms/NAMote-72/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L152RC
      - 32 MHz
      - 256 Kb
      - 32 Kb

Silicon Labs
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

    * - ``efm32gg_stk3700``
      - `Silicon Labs EFM32GG-STK3700 (Giant Gecko) <https://developer.mbed.org/platforms/EFM32-Giant-Gecko/>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM32GG990F1024
      - 48 MHz
      - 1024 Kb
      - 128 Kb

    * - ``efm32hg_stk3400``
      - `Silicon Labs SLSTK3400A USB-enabled (Happy Gecko) <https://developer.mbed.org/platforms/EFM32-Happy-Gecko/>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM32HG322F64
      - 24 MHz
      - 64 Kb
      - 8 Kb

    * - ``efm32lg_stk3600``
      - `Silicon Labs EFM32LG-STK3600 (Leopard Gecko) <https://developer.mbed.org/platforms/EFM32-Leopard-Gecko/>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM32LG990F256
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``efm32pg_stk3401``
      - `Silicon Labs SLSTK3401A (Pearl Gecko) <https://developer.mbed.org/platforms/EFM32-Pearl-Gecko/>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM32PG1B200F256
      - 40 MHz
      - 256 Kb
      - 32 Kb

    * - ``efm32wg_stk3800``
      - `Silicon Labs EFM32WG-STK3800 (Wonder Gecko) <https://developer.mbed.org/platforms/EFM32-Wonder-Gecko/>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM32WG990F256
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``efm32zg_stk3200``
      - `Silicon Labs EFM32ZG-STK3200 (Zero Gecko) <https://developer.mbed.org/platforms/EFM32-Zero-Gecko/>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM2ZG222F32
      - 24 MHz
      - 32 Kb
      - 4 Kb

Smeshlink
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

    * - ``xbed_lpc1768``
      - `Smeshlink xbed LPC1768 <https://developer.mbed.org/platforms/xbed-LPC1768/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC1768
      - 96 MHz
      - 512 Kb
      - 32 Kb

Solder Splash Labs
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

    * - ``dipcortexm0``
      - `Solder Splash Labs DipCortex M0 <https://developer.mbed.org/platforms/DipCortex-M0/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC11U24
      - 50 MHz
      - 32 Kb
      - 8 Kb

    * - ``lpc1347``
      - `DipCortex M3 <https://developer.mbed.org/platforms/DipCortex-M3/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC1347
      - 72 MHz
      - 64 Kb
      - 12 Kb

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

    * - ``sparkfunBlynk``
      - `SparkFun Blynk Board <https://www.sparkfun.com/products/13794>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

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

    * - ``sparkfun_samd21_dev_usb``
      - `SparkFun SAMD21 Dev Breakout <https://www.sparkfun.com/products/13672>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``sparkfun_samd21_mini_usb``
      - `SparkFun SAMD21 Mini Breakout <https://www.sparkfun.com/products/13664>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

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

    * - ``thing``
      - `SparkFun ESP8266 Thing <https://www.sparkfun.com/products/13231>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 512 Kb
      - 80 Kb

    * - ``thingdev``
      - `SparkFun ESP8266 Thing Dev <https://www.sparkfun.com/products/13231>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 512 Kb
      - 80 Kb

    * - ``uview``
      - `SparkFun MicroView <https://www.sparkfun.com/products/12923>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

SparkFun Electronics
~~~~~~~~~~~~~~~~~~~~

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

    * - ``esp32thing``
      - `SparkFun ESP32 Thing <https://www.sparkfun.com/products/13907>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

SweetPea
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

    * - ``esp210``
      - `SweetPea ESP-210 <http://wiki.sweetpeas.se/index.php?title=ESP-210>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

Switch Science
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

    * - ``hrm1017``
      - `Switch Science mbed HRM1017 <https://developer.mbed.org/platforms/mbed-HRM1017/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 256 Kb
      - 16 Kb

    * - ``lpc1114fn28``
      - `Switch Science mbed LPC1114FN28 <https://developer.mbed.org/platforms/LPC1114FN28/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC1114FN28
      - 48 MHz
      - 32 Kb
      - 4 Kb

    * - ``ssci824``
      - `Switch Science mbed LPC824 <https://developer.mbed.org/platforms/Switch-Science-mbed-LPC824/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC824
      - 30 MHz
      - 32 Kb
      - 8 Kb

    * - ``ty51822r3``
      - `Switch Science mbed TY51822r3 <https://developer.mbed.org/platforms/Switch-Science-mbed-TY51822r3/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32 MHz
      - 256 Kb
      - 32 Kb

TI
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

    * - ``lplm4f120h5qr``
      - `TI LaunchPad (Stellaris) w/ lm4f120 (80MHz) <http://www.ti.com/tool/ek-lm4f120xl>`_
      - :ref:`TI TIVA <platform_titiva>`
      - :ref:`Yes <piodebug>`
      - LPLM4F120H5QR
      - 80 MHz
      - 256 Kb
      - 32 Kb

    * - ``lpmsp430f5529``
      - `TI LaunchPad MSP-EXP430F5529LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430f5529lp.html>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`Yes <piodebug>`
      - MSP430F5529
      - 16 MHz
      - 128 Kb
      - 8 Kb

    * - ``lpmsp430fr4133``
      - `TI LaunchPad MSP-EXP430FR4133LP <http://www.ti.com/tool/msp-exp430fr4133>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`Yes <piodebug>`
      - MSP430FR4133
      - 8 MHz
      - 16 Kb
      - 2 Kb

    * - ``lpmsp430fr5739``
      - `TI FraunchPad MSP-EXP430FR5739LP <http://www.ti.com/tool/msp-exp430fr5739>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`Yes <piodebug>`
      - MSP430FR5739
      - 16 MHz
      - 16 Kb
      - 0.5 Kb

    * - ``lpmsp430fr5969``
      - `TI LaunchPad MSP-EXP430FR5969LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430fr5969.html>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`Yes <piodebug>`
      - MSP430FR5969
      - 8 MHz
      - 64 Kb
      - 2 Kb

    * - ``lpmsp430fr6989``
      - `TI LaunchPad MSP-EXP430FR6989LP <http://www.ti.com/tool/msp-exp430fr6989>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`Yes <piodebug>`
      - MSP430FR6989
      - 8 MHz
      - 128 Kb
      - 2 Kb

    * - ``lpmsp430g2553``
      - `TI LaunchPad MSP-EXP430G2553LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430g2.html>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`Yes <piodebug>`
      - MSP430G2553
      - 16 MHz
      - 16 Kb
      - 0.5 Kb

    * - ``lptm4c1230c3pm``
      - `TI LaunchPad (Tiva C) w/ tm4c123 (80MHz) <http://www.ti.com/ww/en/launchpad/launchpads-connected-ek-tm4c123gxl.html>`_
      - :ref:`TI TIVA <platform_titiva>`
      - :ref:`Yes <piodebug>`
      - LPTM4C1230C3PM
      - 80 MHz
      - 256 Kb
      - 32 Kb

    * - ``lptm4c1294ncpdt``
      - `TI LaunchPad (Tiva C) w/ tm4c129 (120MHz) <http://www.ti.com/ww/en/launchpad/launchpads-connected-ek-tm4c1294xl.html>`_
      - :ref:`TI TIVA <platform_titiva>`
      - :ref:`Yes <piodebug>`
      - LPTM4C1294NCPDT
      - 120 MHz
      - 1024 Kb
      - 256 Kb

Teensy
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

    * - ``teensy20``
      - `Teensy 2.0 <https://www.pjrc.com/store/teensy.html>`_
      - :ref:`Teensy <platform_teensy>`
      - 
      - ATMEGA32U4
      - 16 MHz
      - 32 Kb
      - 2.5 Kb

    * - ``teensy20pp``
      - `Teensy++ 2.0 <https://www.pjrc.com/store/teensypp.html>`_
      - :ref:`Teensy <platform_teensy>`
      - 
      - AT90USB1286
      - 16 MHz
      - 128 Kb
      - 8 Kb

    * - ``teensy30``
      - `Teensy 3.0 <https://www.pjrc.com/store/teensy3.html>`_
      - :ref:`Teensy <platform_teensy>`
      - 
      - MK20DX128
      - 48 MHz
      - 128 Kb
      - 16 Kb

    * - ``teensy31``
      - `Teensy 3.1 / 3.2 <https://www.pjrc.com/store/teensy31.html>`_
      - :ref:`Teensy <platform_teensy>`
      - 
      - MK20DX256
      - 72 MHz
      - 256 Kb
      - 64 Kb

    * - ``teensy35``
      - `Teensy 3.5 <https://www.pjrc.com/store/teensy35.html>`_
      - :ref:`Teensy <platform_teensy>`
      - 
      - MK64FX512
      - 120 MHz
      - 512 Kb
      - 192 Kb

    * - ``teensy36``
      - `Teensy 3.6 <https://www.pjrc.com/store/teensy36.html>`_
      - :ref:`Teensy <platform_teensy>`
      - 
      - MK66FX1M0
      - 180 MHz
      - 1024 Kb
      - 256 Kb

    * - ``teensylc``
      - `Teensy LC <http://www.pjrc.com/teensy/teensyLC.html>`_
      - :ref:`Teensy <platform_teensy>`
      - 
      - MKL26Z64
      - 48 MHz
      - 64 Kb
      - 8 Kb

ThaiEasyElec
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

    * - ``espinotee``
      - `ThaiEasyElec ESPino <http://www.thaieasyelec.com/products/wireless-modules/wifi-modules/espino-wifi-development-board-detail.html>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

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

UBW32
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

    * - ``ubw32_mx460``
      - `UBW32 MX460 <http://www.schmalzhaus.com/UBW32/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX460F512L
      - 80 MHz
      - 512 Kb
      - 32 Kb

    * - ``ubw32_mx795``
      - `UBW32 MX795 <http://www.schmalzhaus.com/UBW32/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX795F512L
      - 80 MHz
      - 512 Kb
      - 128 Kb

WEMOS
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

    * - ``d1``
      - `WEMOS D1 (Retired) <https://wiki.wemos.cc/products:d1:d1>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``d1_mini``
      - `WEMOS D1 mini <https://wiki.wemos.cc/products:d1:d1_mini>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``d1_mini_lite``
      - `WEMOS D1 mini Lite <https://wiki.wemos.cc/products:d1:d1_mini_lite>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 960 Kb
      - 80 Kb

    * - ``lolin32``
      - `WEMOS LOLIN32 <https://wemos.cc>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

WIZNet
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

    * - ``wizwiki_w7500``
      - `WIZNet WIZwiki-W7500 <https://developer.mbed.org/platforms/WIZwiki-W7500/>`_
      - :ref:`WIZNet W7500 <platform_wiznet7500>`
      - :ref:`Yes <piodebug>`
      - WIZNET7500
      - 48 MHz
      - 128 Kb
      - 48 Kb

    * - ``wizwiki_w7500eco``
      - `WIZNet WIZwiki-W7500ECO <https://developer.mbed.org/platforms/WIZwiki-W7500ECO/>`_
      - :ref:`WIZNet W7500 <platform_wiznet7500>`
      - :ref:`Yes <piodebug>`
      - WIZNET7500ECO
      - 48 MHz
      - 128 Kb
      - 48 Kb

    * - ``wizwiki_w7500p``
      - `WIZNet WIZwiki-W7500P <https://developer.mbed.org/platforms/WIZwiki-W7500P/>`_
      - :ref:`WIZNet W7500 <platform_wiznet7500>`
      - :ref:`Yes <piodebug>`
      - WIZNET7500P
      - 48 MHz
      - 128 Kb
      - 48 Kb

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

Widora
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

    * - ``widora-air``
      - `Widora AIR <http://widora.io>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

chipKIT
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

    * - ``lenny``
      - `chipKIT Lenny <http://chipkit.net/tag/lenny/>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX270F256D
      - 40 MHz
      - 128 Kb
      - 32 Kb

element14
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

    * - ``chipkit_pi``
      - `Element14 chipKIT Pi <http://www.element14.com/community/community/knode/dev_platforms_kits/element14_dev_kits/microchip-chipkit/chipkit_pi>`_
      - :ref:`Microchip PIC32 <platform_microchippic32>`
      - 
      - 32MX250F128B
      - 40 MHz
      - 128 Kb
      - 32 Kb

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

u-blox
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

    * - ``ublox_evk_odin_w2``
      - `u-blox EVK-ODIN-W2 <https://developer.mbed.org/platforms/ublox-EVK-ODIN-W2/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F439ZIY6
      - 168 MHz
      - 2048 Kb
      - 256 Kb

    * - ``ubloxc027``
      - `u-blox C027 <https://developer.mbed.org/platforms/u-blox-C027/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC1768
      - 96 MHz
      - 512 Kb
      - 64 Kb

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

y5 design
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

    * - ``lpc11u35_y5_mbug``
      - `y5 LPC11U35 mbug <https://developer.mbed.org/platforms/Y5-LPC11U35-MBUG/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - 
      - LPC11U35
      - 48 MHz
      - 64 Kb
      - 10 Kb

    * - ``nrf51822_y5_mbug``
      - `y5 nRF51822 mbug <https://developer.mbed.org/platforms/Y5-NRF51822-MBUG/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 256 Kb
      - 16 Kb
