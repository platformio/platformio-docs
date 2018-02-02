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
    
1BitSquared
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
    * - ``1bitsy_stm32f415rgt``
      - `1Bitsy <http://1bitsy.org?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F415RGT
      - 168 MHz
      - 1M
      - 128K

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

96Boards
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
    * - ``b96b_f446ve``
      - `96Boards B96B-F446VE <https://developer.mbed.org/platforms/ST-B96B-F446VE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F446VET6
      - 168 MHz
      - 512K
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

AppNearMe
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
    * - ``micronfcboard``
      - `MicroNFCBoard <https://os.mbed.com/platforms/MicroNFCBoard/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - No
      - LPC11U34
      - 48 MHz
      - 48K
      - 10K

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

Armstrap
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
    * - ``armstrap_eagle1024``
      - `Armstrap Eagle 1024 <http://docs.armstrap.org/en/latest/hardware-overview.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F417VGT6
      - 168 MHz
      - 1M
      - 192K
    * - ``armstrap_eagle2048``
      - `Armstrap Eagle 2048 <http://docs.armstrap.org/en/latest/hardware-overview.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F427VIT6
      - 168 MHz
      - 1.99M
      - 256K
    * - ``armstrap_eagle512``
      - `Armstrap Eagle 512 <http://docs.armstrap.org/en/latest/hardware-overview.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F407VET6
      - 168 MHz
      - 512K
      - 192K

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
    * - ``samd21_xpro``
      - `Atmel SAMD21-XPRO <https://developer.mbed.org/platforms/SAMD21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - ATSAMD21J18A
      - 48 MHz
      - 256K
      - 32K
    * - ``samd21g18a``
      - `Atmel ATSAMW25-XPRO <https://developer.mbed.org/platforms/SAMW25-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - ATSAMD21G18A
      - 48 MHz
      - 256K
      - 32K
    * - ``saml21_xpro_b``
      - `Atmel SAML21-XPRO-B <https://developer.mbed.org/platforms/SAML21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - ATSAML21J18B
      - 48 MHz
      - 256K
      - 32K
    * - ``samr21_xpro``
      - `Atmel ATSAMR21-XPRO <https://developer.mbed.org/platforms/SAMR21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - ATSAMR21G18A
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
    * - ``bbcmicrobit_b``
      - `BBC micro:bit B(S130) <https://developer.mbed.org/platforms/Microbit/?utm_source=platformio&utm_medium=docs>`_
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

CQ Publishing
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
    * - ``lpc11u35_501``
      - `CQ Publishing TG-LPC11U35-501 <https://developer.mbed.org/platforms/TG-LPC11U35-501/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U35
      - 48 MHz
      - 64K
      - 10K

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
    * - ``delta_dfcm_nnn50``
      - `Delta DFCM-NNN50 <https://os.mbed.com/platforms/Delta-DFCM-NNN50/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32 MHz
      - 256K
      - 16K
    * - ``dfcm_nnn40``
      - `Delta DFCM-NNN40 <https://developer.mbed.org/platforms/Delta-DFCM-NNN40/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32 MHz
      - 256K
      - 32K

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

Elektor Labs
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
    * - ``elektor_cocorico``
      - `CoCo-ri-Co! <https://developer.mbed.org/platforms/CoCo-ri-Co/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lpc11u35``
      - `EA LPC11U35 QuickStart Board <https://developer.mbed.org/platforms/EA-LPC11U35/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U35
      - 48 MHz
      - 64K
      - 10K
    * - ``lpc4088``
      - `Embedded Artists LPC4088 QuickStart Board <https://developer.mbed.org/platforms/EA-LPC4088/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC4088
      - 120 MHz
      - 512K
      - 96K
    * - ``lpc4088_dm``
      - `Embedded Artists LPC4088 Display Module <https://developer.mbed.org/platforms/EA-LPC4088-Display-Module/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC4088
      - 120 MHz
      - 512K
      - 96K

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

Espotel
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
    * - ``elmo_f411re``
      - `Espotel LoRa Module <https://developer.mbed.org/platforms/Espotel-ELMO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100 MHz
      - 512K
      - 128K

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
      - `Espressif Generic ESP8266 ESP-07 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family#esp-07&utm_source=platformio&utm_medium=docs>`_
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

FPGAwars
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
    * - ``icezum``
      - `IceZUM Alhambra FPGA <https://github.com/FPGAwars/icezum/wiki?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Lattice iCE40 <platform_lattice_ice40>`
      - No
      - ICE40-HX1K-TQ144
      - 12 MHz
      - 32K
      - 32K

Freescale
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
    * - ``IBMEthernetKit``
      - `Ethernet IoT Starter Kit <http://developer.mbed.org/platforms/IBMEthernetKit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MK64FN1M0VLL12
      - 120 MHz
      - 1M
      - 256K
    * - ``frdm_k20d50m``
      - `Freescale Kinetis FRDM-K20D50M <https://developer.mbed.org/platforms/FRDM-K20D50M/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MK20DX128VLH5
      - 48 MHz
      - 128K
      - 16K
    * - ``frdm_k22f``
      - `Freescale Kinetis FRDM-K22F <https://developer.mbed.org/platforms/FRDM-K22F/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MK22FN512VLH12
      - 120 MHz
      - 512K
      - 128K
    * - ``frdm_k64f``
      - `Freescale Kinetis FRDM-K64F <https://developer.mbed.org/platforms/FRDM-K64F/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MK64FN1M0VLL12
      - 120 MHz
      - 1M
      - 256K
    * - ``frdm_k66f``
      - `Freescale Kinetis FRDM-K66F <https://developer.mbed.org/platforms/FRDM-K66F/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MK66FN2M0VMD18
      - 180 MHz
      - 2M
      - 256K
    * - ``frdm_kl05z``
      - `Freescale Kinetis FRDM-KL05Z <https://developer.mbed.org/platforms/FRDM-KL05Z/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL05Z32VFM4
      - 48 MHz
      - 32K
      - 4K
    * - ``frdm_kl25z``
      - `Freescale Kinetis FRDM-KL25Z <https://developer.mbed.org/platforms/KL25Z/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL25Z128VLK4
      - 48 MHz
      - 128K
      - 16K
    * - ``frdm_kl26z``
      - `Freescale Kinetis FRDM-KL26Z <http://www.nxp.com/products/software-and-tools/hardware-development-tools/freedom-development-boards/freedom-development-platform-for-kinetis-kl16-and-kl26-mcus-up-to-128-kb-flash:FRDM-KL26Z?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL26Z128VLH4
      - 48 MHz
      - 128K
      - 16K
    * - ``frdm_kl27z``
      - `Freescale Kinetis FRDM-KL27Z <http://www.nxp.com/products/software-and-tools/hardware-development-tools/freedom-development-boards/freedom-development-platform-for-kinetis-kl17-and-kl27-mcus:FRDM-KL27Z?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL27Z64VLH4
      - 48 MHz
      - 64K
      - 16K
    * - ``frdm_kl43z``
      - `Freescale Kinetis FRDM-KL43Z <http://www.nxp.com/products/software-and-tools/hardware-development-tools/freedom-development-boards/freedom-development-platform-for-kinetis-kl43-kl33-kl27-kl17-and-kl13-mcus:FRDM-KL43Z?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL43Z256VLH4
      - 48 MHz
      - 256K
      - 32K
    * - ``frdm_kl46z``
      - `Freescale Kinetis FRDM-KL46Z <https://developer.mbed.org/platforms/FRDM-KL46Z/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL46Z256VLL4
      - 48 MHz
      - 256K
      - 32K
    * - ``frdm_kw41z``
      - `Freescale Kinetis FRDM-KW41Z <https://os.mbed.com/platforms/FRDM-KW41Z/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKW41Z512VHT4
      - 48 MHz
      - 512K
      - 128K

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

GHI Electronics
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
    * - ``oc_mbuino``
      - `mBuino <https://developer.mbed.org/platforms/mBuino/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - No
      - LPC11U24
      - 50 MHz
      - 32K
      - 10K

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

JKSoft
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
    * - ``wallbot_ble``
      - `JKSoft Wallbot BLE <https://developer.mbed.org/platforms/JKSoft-Wallbot-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 128K
      - 16K

Lattice
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
    * - ``icestick``
      - `Lattice iCEstick FPGA Evaluation Kit <http://www.latticesemi.com/icestick?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Lattice iCE40 <platform_lattice_ice40>`
      - No
      - ICE40-HX1K-TQ144
      - 12 MHz
      - 32K
      - 32K

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

Maxim
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
    * - ``max32600mbed``
      - `Maxim ARM mbed Enabled Development Platform for MAX32600 <https://developer.mbed.org/platforms/MAX32600mbed/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - No
      - MAX32600
      - 24 MHz
      - 256K
      - 32K
    * - ``max32620hsp``
      - `Maxim Health Sensor Platform <https://developer.mbed.org/platforms/MAX32620HSP/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - No
      - MAX32620
      - 96 MHz
      - 2M
      - 256K
    * - ``max32625mbed``
      - `MAX32625MBED <https://os.mbed.com/platforms/MAX32625MBED/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - No
      - MAX32625
      - 96 MHz
      - 512K
      - 160K
    * - ``max32625nexpaq``
      - `MAX32625NEXPAQ <https://os.mbed.com/platforms/max32625nexpaq/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - No
      - MAX32625
      - 96 MHz
      - 512K
      - 160K
    * - ``max32630fthr``
      - `Maxim MAX32630FTHR Application Platform <https://developer.mbed.org/platforms/MAX32630FTHR/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - No
      - MAX32630
      - 96 MHz
      - 2M
      - 512K
    * - ``maxwsnenv``
      - `Maxim Wireless Sensor Node Demonstrator <https://developer.mbed.org/platforms/MAXWSNENV/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - No
      - MAX32610
      - 24 MHz
      - 256K
      - 32K

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

Microchip
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
    * - ``at90pwm216``
      - `Atmel AT90PWM216 <http://www.microchip.com/wwwproducts/en/AT90PWM216?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - AT90PWM216
      - 16 MHz
      - 16K
      - 1K
    * - ``at90pwm316``
      - `Atmel AT90PWM316 <http://www.microchip.com/wwwproducts/en/AT90PWM316?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - No
      - AT90PWM316
      - 16 MHz
      - 16K
      - 1K

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

Micromint
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
    * - ``lpc4330_m4``
      - `Bambino-210E <https://developer.mbed.org/platforms/Micromint-Bambino-210E/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC4330
      - 204 MHz
      - 8M
      - 264K
    * - ``lpc4337``
      - `LPCXpresso4337 <https://developer.mbed.org/platforms/LPCXpresso4337/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC4337
      - 204 MHz
      - 1M
      - 136K

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
    * - ``hexiwear``
      - `Hexiwear <https://developer.mbed.org/platforms/Hexiwear/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MK64FN1M0VDC12
      - 120 MHz
      - 1M
      - 256K

MultiTech
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
    * - ``mts_dragonfly_f411re``
      - `MTS Dragonfly <https://developer.mbed.org/platforms/MTS-Dragonfly/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100 MHz
      - 512K
      - 128K
    * - ``mts_mdot_f405rg``
      - `MultiTech mDot <https://developer.mbed.org/platforms/MTS-mDot-F411/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100 MHz
      - 512K
      - 128K
    * - ``mts_mdot_f411re``
      - `MultiTech mDot F411 <https://developer.mbed.org/platforms/MTS-mDot-F411/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100 MHz
      - 512K
      - 128K
    * - ``xdot_l151cc``
      - `MultiTech xDot <https://developer.mbed.org/platforms/MTS-xDot-L151CC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L151CCU6
      - 32 MHz
      - 256K
      - 32K

NGX Technologies
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
    * - ``blueboard_lpc11u24``
      - `NGX Technologies BlueBoard-LPC11U24 <https://developer.mbed.org/platforms/BlueBoard-LPC11U24/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lpc11c24``
      - `NXP LPC11C24 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-m0-cores:LPC11C24FBD48?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11C24
      - 48 MHz
      - 32K
      - 8K
    * - ``lpc11u24``
      - `NXP mbed LPC11U24 <https://developer.mbed.org/platforms/mbed-LPC11U24/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U24
      - 48 MHz
      - 32K
      - 8K
    * - ``lpc11u24_301``
      - `ARM mbed LPC11U24 (+CAN) <https://developer.mbed.org/handbook/mbed-NXP-LPC11U24?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U24
      - 48 MHz
      - 32K
      - 8K
    * - ``lpc11u34_421``
      - `NXP LPC11U34 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/40kb-flash-8kb-sram-lqfp48-package:LPC11U34FBD48?lang_cd=en&utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U34
      - 48 MHz
      - 40K
      - 8K
    * - ``lpc11u37_501``
      - `NXP LPC11U37 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/128kb-flash-10kb-sram-lqfp48-package:LPC11U37FBD48?lang_cd=en&utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U37
      - 48 MHz
      - 128K
      - 10K
    * - ``lpc11u68``
      - `LPCXpresso11U68 <https://developer.mbed.org/platforms/LPCXpresso11U68/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U68
      - 50 MHz
      - 256K
      - 36K
    * - ``lpc1549``
      - `NXP LPCXpresso1549 <https://developer.mbed.org/platforms/LPCXpresso1549/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC1549
      - 72 MHz
      - 256K
      - 36K
    * - ``lpc1768``
      - `NXP mbed LPC1768 <http://developer.mbed.org/platforms/mbed-LPC1768/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC1768
      - 96 MHz
      - 512K
      - 64K
    * - ``lpc2368``
      - `NXP LPC2368 <https://developer.mbed.org/platforms/mbed-LPC2368/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - No
      - LPC2368
      - 72 MHz
      - 512K
      - 58K
    * - ``lpc2460``
      - `NXP LPC2460 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-arm7-arm9-mcus/lpc-arm7-mcus/lpc2100-200-300-400/flashless-16-bit-32-bit-microcontroller-ethernet-can-isp-iap-usb-2.0-device-host-otg-external-memory-interface:LPC2460FBD208?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC2460
      - 72 MHz
      - 64K
      - 16K
    * - ``lpc812``
      - `NXP LPC800-MAX <https://developer.mbed.org/platforms/NXP-LPC800-MAX/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC812
      - 30 MHz
      - 16K
      - 4K
    * - ``lpc824``
      - `LPCXpresso824-MAX <https://developer.mbed.org/platforms/LPCXpresso824-MAX/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC824
      - 30 MHz
      - 32K
      - 8K

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
    * - ``nrf51_mkit``
      - `Nordic nRF51822-mKIT <http://developer.mbed.org/platforms/Nordic-nRF51822/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 128K
      - 16K
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

Outrageous Circuits
~~~~~~~~~~~~~~~~~~~

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
    * - ``mbuino``
      - `Outrageous Circuits mBuino <https://developer.mbed.org/platforms/Outrageous-Circuits-mBuino/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - No
      - LPC11U24
      - 48 MHz
      - 32K
      - 8K

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

Raspberry Pi
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
    * - ``raspberrypi_1b``
      - `Raspberry Pi 1 Model B <https://www.raspberrypi.org?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - No
      - BCM2835
      - 700 MHz
      - 512M
      - 512M
    * - ``raspberrypi_2b``
      - `Raspberry Pi 2 Model B <https://www.raspberrypi.org?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - No
      - BCM2836
      - 900 MHz
      - 1G
      - 1G
    * - ``raspberrypi_3b``
      - `Raspberry Pi 3 Model B <https://www.raspberrypi.org?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - No
      - BCM2837
      - 1200 MHz
      - 1G
      - 1G
    * - ``raspberrypi_zero``
      - `Raspberry Pi Zero <https://www.raspberrypi.org?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - No
      - BCM2835
      - 1000 MHz
      - 512M
      - 512M

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

RushUp
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
    * - ``cloud_jam``
      - `RushUp Cloud-JAM <https://developer.mbed.org/platforms/ST-Nucleo-F401RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F401RET6
      - 84 MHz
      - 512K
      - 96K
    * - ``cloud_jam_l4``
      - `RushUp Cloud-JAM L4 <https://developer.mbed.org/platforms/ST-Nucleo-L476RG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L476RGT6
      - 80 MHz
      - 1M
      - 128K
    * - ``kitra_520``
      - `RushUp Kitra 520 <https://www.rushup.tech/kitra?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - No
      - EXYNOS3250
      - 1000 MHz
      - 4G
      - 512M

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
    * - ``disco_f030r8``
      - `ST STM32F0308DISCOVERY <http://www.st.com/en/evaluation-tools/32f0308discovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F030R8T6
      - 48 MHz
      - 64K
      - 8K
    * - ``disco_f051r8``
      - `ST STM32F0DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF253215?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F051R8T6
      - 48 MHz
      - 64K
      - 8K
    * - ``disco_f100rb``
      - `ST STM32VLDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF250863?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F100RBT6
      - 24 MHz
      - 128K
      - 8K
    * - ``disco_f303vc``
      - `ST STM32F3DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF254044?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F303VCT6
      - 72 MHz
      - 256K
      - 48K
    * - ``disco_f334c8``
      - `ST 32F3348DISCOVERY <http://www.st.com/web/en/catalog/tools/PF260318?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F334C8T6
      - 72 MHz
      - 64K
      - 12K
    * - ``disco_f401vc``
      - `ST 32F401CDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF259098?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F401VCT6
      - 84 MHz
      - 256K
      - 64K
    * - ``disco_f407vg``
      - `ST STM32F4DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF252419?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F407VGT6
      - 168 MHz
      - 1M
      - 128K
    * - ``disco_f411ve``
      - `ST 32F411EDISCOVERY <http://www.st.com/en/evaluation-tools/32f411ediscovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411VET6
      - 100 MHz
      - 512K
      - 128K
    * - ``disco_f413zh``
      - `ST 32F413HDISCOVERY <https://os.mbed.com/platforms/ST-Discovery-F413H/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F413ZHT6
      - 100 MHz
      - 512K
      - 128K
    * - ``disco_f429zi``
      - `ST 32F429IDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF259090?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F429ZIT6
      - 180 MHz
      - 2M
      - 256K
    * - ``disco_f469ni``
      - `ST 32F469IDISCOVERY <http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF262395?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F469NIH6
      - 180 MHz
      - 1M
      - 384K
    * - ``disco_f746ng``
      - `ST 32F746GDISCOVERY <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/32f746gdiscovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F746NGH6
      - 216 MHz
      - 1M
      - 320K
    * - ``disco_f769ni``
      - `ST 32F769IDISCOVERY <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/32f769idiscovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F769NIH6
      - 80 MHz
      - 1M
      - 512K
    * - ``disco_l053c8``
      - `ST 32L0538DISCOVERY <http://www.st.com/web/en/catalog/tools/PF260319?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L053C8T6
      - 32 MHz
      - 64K
      - 8K
    * - ``disco_l072cz_lrwan1``
      - `ST DISCO-L072CZ-LRWAN1 <https://developer.mbed.org/platforms/ST-Discovery-LRWAN1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L072CZ
      - 32 MHz
      - 192K
      - 20K
    * - ``disco_l152rb``
      - `ST STM32LDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF258515?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L152RBT6
      - 32 MHz
      - 128K
      - 16K
    * - ``disco_l475vg_iot01a``
      - `ST DISCO-L475VG-IOT01A <https://developer.mbed.org/platforms/ST-Discovery-L475E-IOT01A/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L475VGT6
      - 80 MHz
      - 1M
      - 128K
    * - ``disco_l476vg``
      - `ST 32L476GDISCOVERY <http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF261635?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L476VGT6
      - 80 MHz
      - 1M
      - 128K
    * - ``eval_l073z``
      - `ST STM32L073Z-EVAL <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-eval-boards/stm32l073z-eval.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L073VZT6
      - 32 MHz
      - 192K
      - 20K
    * - ``nucleo_f030r8``
      - `ST Nucleo F030R8 <https://developer.mbed.org/platforms/ST-Nucleo-F030R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F030R8T6
      - 48 MHz
      - 64K
      - 8K
    * - ``nucleo_f031k6``
      - `ST Nucleo F031K6 <https://developer.mbed.org/platforms/ST-Nucleo-F031K6/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F031K6T6
      - 48 MHz
      - 32K
      - 4K
    * - ``nucleo_f042k6``
      - `ST Nucleo F042K6 <https://developer.mbed.org/platforms/ST-Nucleo-F042K6/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F042K6T6
      - 48 MHz
      - 32K
      - 6K
    * - ``nucleo_f070rb``
      - `ST Nucleo F070RB <https://developer.mbed.org/platforms/ST-Nucleo-F070RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F070RBT6
      - 48 MHz
      - 128K
      - 16K
    * - ``nucleo_f072rb``
      - `ST Nucleo F072RB <https://developer.mbed.org/platforms/ST-Nucleo-F072RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F072RBT6
      - 48 MHz
      - 128K
      - 16K
    * - ``nucleo_f091rc``
      - `ST Nucleo F091RC <https://developer.mbed.org/platforms/ST-Nucleo-F091RC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F091RCT6
      - 48 MHz
      - 256K
      - 32K
    * - ``nucleo_f103rb``
      - `ST Nucleo F103RB <https://developer.mbed.org/platforms/ST-Nucleo-F103RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RBT6
      - 72 MHz
      - 128K
      - 20K
    * - ``nucleo_f207zg``
      - `ST Nucleo F207ZG <https://developer.mbed.org/platforms/ST-Nucleo-F207ZG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F207ZGT6
      - 120 MHz
      - 1M
      - 128K
    * - ``nucleo_f302r8``
      - `ST Nucleo F302R8 <https://developer.mbed.org/platforms/ST-Nucleo-F302R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F302R8T6
      - 72 MHz
      - 64K
      - 16K
    * - ``nucleo_f303k8``
      - `ST Nucleo F303K8 <https://developer.mbed.org/platforms/ST-Nucleo-F303K8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F303K8T6
      - 72 MHz
      - 64K
      - 16K
    * - ``nucleo_f303re``
      - `ST Nucleo F303RE <http://developer.mbed.org/platforms/ST-Nucleo-F303RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F303RET6
      - 72 MHz
      - 512K
      - 64K
    * - ``nucleo_f303ze``
      - `ST Nucleo F303ZE <https://developer.mbed.org/platforms/ST-Nucleo-F303ZE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F303ZET6
      - 72 MHz
      - 512K
      - 64K
    * - ``nucleo_f334r8``
      - `ST Nucleo F334R8 <https://developer.mbed.org/platforms/ST-Nucleo-F334R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F334R8T6
      - 72 MHz
      - 64K
      - 16K
    * - ``nucleo_f401re``
      - `ST Nucleo F401RE <https://developer.mbed.org/platforms/ST-Nucleo-F401RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F401RET6
      - 84 MHz
      - 512K
      - 96K
    * - ``nucleo_f410rb``
      - `ST Nucleo F410RB <https://developer.mbed.org/platforms/ST-Nucleo-F410RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F410RBT6
      - 100 MHz
      - 128K
      - 32K
    * - ``nucleo_f411re``
      - `ST Nucleo F411RE <https://developer.mbed.org/platforms/ST-Nucleo-F411RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100 MHz
      - 512K
      - 128K
    * - ``nucleo_f412zg``
      - `ST Nucleo F412ZG <https://developer.mbed.org/platforms/ST-Nucleo-F411RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F412ZGT6
      - 100 MHz
      - 1M
      - 256K
    * - ``nucleo_f429zi``
      - `ST Nucleo F429ZI <https://developer.mbed.org/platforms/ST-Nucleo-F429ZI/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F429ZIT6
      - 180 MHz
      - 2M
      - 256K
    * - ``nucleo_f446re``
      - `ST Nucleo F446RE <https://developer.mbed.org/platforms/ST-Nucleo-F446RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F446RET6
      - 180 MHz
      - 512K
      - 128K
    * - ``nucleo_f446ze``
      - `ST Nucleo F446ZE <https://developer.mbed.org/platforms/ST-Nucleo-F446ZE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F446ZET6
      - 180 MHz
      - 512K
      - 128K
    * - ``nucleo_f746zg``
      - `ST Nucleo F746ZG <https://developer.mbed.org/platforms/ST-Nucleo-F446ZE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F746ZGT6
      - 216 MHz
      - 1M
      - 320K
    * - ``nucleo_f767zi``
      - `ST Nucleo F767ZI <https://developer.mbed.org/platforms/ST-Nucleo-F767ZI/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F767ZIT6
      - 216 MHz
      - 2M
      - 512K
    * - ``nucleo_l011k4``
      - `ST Nucleo L011K4 <https://developer.mbed.org/platforms/ST-Nucleo-L011K4/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L011K4T6
      - 32 MHz
      - 16K
      - 2K
    * - ``nucleo_l031k6``
      - `ST Nucleo L031K6 <https://developer.mbed.org/platforms/ST-Nucleo-L031K6/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L031K6T6
      - 32 MHz
      - 32K
      - 8K
    * - ``nucleo_l053r8``
      - `ST Nucleo L053R8 <https://developer.mbed.org/platforms/ST-Nucleo-L053R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L053R8T6
      - 48 MHz
      - 64K
      - 8K
    * - ``nucleo_l073rz``
      - `ST Nucleo L073RZ <https://developer.mbed.org/platforms/ST-Nucleo-L073RZ/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L073RZ
      - 32 MHz
      - 192K
      - 20K
    * - ``nucleo_l152re``
      - `ST Nucleo L152RE <https://developer.mbed.org/platforms/ST-Nucleo-L152RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L152RET6
      - 32 MHz
      - 512K
      - 80K
    * - ``nucleo_l432kc``
      - `ST Nucleo L432KC <https://developer.mbed.org/platforms/ST-Nucleo-L432KC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L432KCU6
      - 80 MHz
      - 256K
      - 64K
    * - ``nucleo_l476rg``
      - `ST Nucleo L476RG <https://developer.mbed.org/platforms/ST-Nucleo-L476RG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L476RGT6
      - 80 MHz
      - 1M
      - 128K

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

Samsung
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
    * - ``artik_053``
      - `Samsung ARTIK053 <http://www.artik.io?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Samsung ARTIK <platform_samsung_artik>`
      - :ref:`Yes <piodebug>`
      - S5JT200
      - 320 MHz
      - 8M
      - 1.25M
    * - ``artik_1020``
      - `Samsung ARTIK 1020 <https://www.artik.io?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - No
      - EXYNOS5422
      - 1500 MHz
      - 16G
      - 2G
    * - ``artik_520``
      - `Samsung ARTIK 520 <https://www.artik.io?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - No
      - EXYNOS3250
      - 1000 MHz
      - 4G
      - 512M
    * - ``artik_530``
      - `Samsung ARTIK 530 <https://www.artik.io?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - No
      - S5P4418
      - 1200 MHz
      - 4G
      - 512M
    * - ``artik_710``
      - `Samsung ARTIK 710 <https://www.artik.io?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - No
      - S5P6818
      - 1400 MHz
      - 4G
      - 1G

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
    * - ``seeedArchBLE``
      - `Seeed Arch BLE <https://developer.mbed.org/platforms/Seeed-Arch-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 128K
      - 16K
    * - ``seeedArchGPRS``
      - `Seeed Arch GPRS V2 <https://www.seeedstudio.com/Arch-GPRS-V2-p-2026.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - No
      - LPC11U37
      - 48 MHz
      - 128K
      - 10K
    * - ``seeedArchLink``
      - `Seeed Arch Link <https://developer.mbed.org/platforms/Seeed-Arch-Link/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 256K
      - 16K
    * - ``seeedArchMax``
      - `Seeed Arch Max <https://developer.mbed.org/platforms/Seeed-Arch-Max/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F407VET6
      - 168 MHz
      - 512K
      - 192K
    * - ``seeedArchPro``
      - `Seeed Arch Pro <https://developer.mbed.org/platforms/Seeeduino-Arch-Pro/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC1768
      - 96 MHz
      - 512K
      - 64K
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
    * - ``xadow_m0``
      - `Seeed Xadow M0 <https://developer.mbed.org/platforms/Seeed-Xadow-M0/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - No
      - LPC11U35
      - 48 MHz
      - 64K
      - 10K

Semtech
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
    * - ``mote_l152rc``
      - `NAMote72 <https://developer.mbed.org/platforms/NAMote-72/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L152RC
      - 32 MHz
      - 256K
      - 32K

Silicon Labs
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
    * - ``efm32gg_stk3700``
      - `Silicon Labs EFM32GG-STK3700 (Giant Gecko) <https://developer.mbed.org/platforms/EFM32-Giant-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM32GG990F1024
      - 48 MHz
      - 1M
      - 128K
    * - ``efm32hg_stk3400``
      - `Silicon Labs SLSTK3400A USB-enabled (Happy Gecko) <https://developer.mbed.org/platforms/EFM32-Happy-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM32HG322F64
      - 24 MHz
      - 64K
      - 8K
    * - ``efm32lg_stk3600``
      - `Silicon Labs EFM32LG-STK3600 (Leopard Gecko) <https://developer.mbed.org/platforms/EFM32-Leopard-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM32LG990F256
      - 48 MHz
      - 256K
      - 32K
    * - ``efm32pg_stk3401``
      - `Silicon Labs SLSTK3401A (Pearl Gecko) <https://developer.mbed.org/platforms/EFM32-Pearl-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM32PG1B200F256
      - 40 MHz
      - 256K
      - 32K
    * - ``efm32wg_stk3800``
      - `Silicon Labs EFM32WG-STK3800 (Wonder Gecko) <https://developer.mbed.org/platforms/EFM32-Wonder-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM32WG990F256
      - 48 MHz
      - 256K
      - 32K
    * - ``efm32zg_stk3200``
      - `Silicon Labs EFM32ZG-STK3200 (Zero Gecko) <https://developer.mbed.org/platforms/EFM32-Zero-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM32ZG222F32
      - 24 MHz
      - 32K
      - 4K

Smeshlink
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
    * - ``xbed_lpc1768``
      - `Smeshlink xbed LPC1768 <https://developer.mbed.org/platforms/xbed-LPC1768/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``dipcortexm0``
      - `Solder Splash Labs DipCortex M0 <https://developer.mbed.org/platforms/DipCortex-M0/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U24
      - 50 MHz
      - 32K
      - 8K
    * - ``lpc1347``
      - `DipCortex M3 <https://developer.mbed.org/platforms/DipCortex-M3/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC1347
      - 72 MHz
      - 64K
      - 12K

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

Switch Science
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
    * - ``hrm1017``
      - `Switch Science mbed HRM1017 <https://developer.mbed.org/platforms/mbed-HRM1017/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 256K
      - 16K
    * - ``lpc1114fn28``
      - `Switch Science mbed LPC1114FN28 <https://developer.mbed.org/platforms/LPC1114FN28/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC1114FN28
      - 48 MHz
      - 32K
      - 4K
    * - ``ssci824``
      - `Switch Science mbed LPC824 <https://developer.mbed.org/platforms/Switch-Science-mbed-LPC824/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC824
      - 30 MHz
      - 32K
      - 8K
    * - ``ty51822r3``
      - `Switch Science mbed TY51822r3 <https://developer.mbed.org/platforms/Switch-Science-mbed-TY51822r3/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32 MHz
      - 256K
      - 32K

TI
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
    * - ``lplm4f120h5qr``
      - `TI LaunchPad (Stellaris) w/ lm4f120 (80MHz) <http://www.ti.com/tool/ek-lm4f120xl?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI TIVA <platform_titiva>`
      - :ref:`Yes <piodebug>`
      - LPLM4F120H5QR
      - 80 MHz
      - 256K
      - 32K
    * - ``lpmsp430f5529``
      - `TI LaunchPad MSP-EXP430F5529LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430f5529lp.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`Yes <piodebug>`
      - MSP430F5529
      - 16 MHz
      - 128K
      - 8K
    * - ``lpmsp430fr4133``
      - `TI LaunchPad MSP-EXP430FR4133LP <http://www.ti.com/tool/msp-exp430fr4133?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`Yes <piodebug>`
      - MSP430FR4133
      - 8 MHz
      - 15K
      - 2K
    * - ``lpmsp430fr5739``
      - `TI FraunchPad MSP-EXP430FR5739LP <http://www.ti.com/tool/msp-exp430fr5739?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`Yes <piodebug>`
      - MSP430FR5739
      - 16 MHz
      - 16K
      - 512B
    * - ``lpmsp430fr5969``
      - `TI LaunchPad MSP-EXP430FR5969LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430fr5969.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`Yes <piodebug>`
      - MSP430FR5969
      - 8 MHz
      - 64K
      - 2K
    * - ``lpmsp430fr6989``
      - `TI LaunchPad MSP-EXP430FR6989LP <http://www.ti.com/tool/msp-exp430fr6989?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`Yes <piodebug>`
      - MSP430FR6989
      - 8 MHz
      - 127K
      - 2K
    * - ``lpmsp430g2553``
      - `TI LaunchPad MSP-EXP430G2553LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430g2.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`Yes <piodebug>`
      - MSP430G2553
      - 16 MHz
      - 16K
      - 512B
    * - ``lptm4c1230c3pm``
      - `TI LaunchPad (Tiva C) w/ tm4c123 (80MHz) <http://www.ti.com/ww/en/launchpad/launchpads-connected-ek-tm4c123gxl.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI TIVA <platform_titiva>`
      - :ref:`Yes <piodebug>`
      - LPTM4C1230C3PM
      - 80 MHz
      - 256K
      - 32K
    * - ``lptm4c1294ncpdt``
      - `TI LaunchPad (Tiva C) w/ tm4c129 (120MHz) <http://www.ti.com/ww/en/launchpad/launchpads-connected-ek-tm4c1294xl.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI TIVA <platform_titiva>`
      - :ref:`Yes <piodebug>`
      - LPTM4C1294NCPDT
      - 120 MHz
      - 1M
      - 256K

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

VNG
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
    * - ``vbluno51``
      - `VNG VBLUNO51 <https://os.mbed.com/platforms/VBLUNO51/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 128K
      - 32K

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

WIZNet
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
    * - ``wizwiki_w7500``
      - `WIZNet WIZwiki-W7500 <https://developer.mbed.org/platforms/WIZwiki-W7500/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`WIZNet W7500 <platform_wiznet7500>`
      - :ref:`Yes <piodebug>`
      - WIZNET7500
      - 48 MHz
      - 128K
      - 48K
    * - ``wizwiki_w7500eco``
      - `WIZNet WIZwiki-W7500ECO <https://developer.mbed.org/platforms/WIZwiki-W7500ECO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`WIZNet W7500 <platform_wiznet7500>`
      - :ref:`Yes <piodebug>`
      - WIZNET7500ECO
      - 48 MHz
      - 128K
      - 48K
    * - ``wizwiki_w7500p``
      - `WIZNet WIZwiki-W7500P <https://developer.mbed.org/platforms/WIZwiki-W7500P/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`WIZNet W7500 <platform_wiznet7500>`
      - :ref:`Yes <piodebug>`
      - WIZNET7500P
      - 48 MHz
      - 128K
      - 48K

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
    * - ``ublox_c030_n211``
      - `u-blox C030-N211 IoT Starter Kit <https://os.mbed.com/platforms/ublox-C030-N211/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F437VG
      - 180 MHz
      - 1M
      - 256K
    * - ``ublox_c030_u201``
      - `u-blox C030-U201 IoT Starter Kit <https://os.mbed.com/platforms/ublox-C030-N211/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F437VG
      - 180 MHz
      - 1M
      - 256K
    * - ``ublox_evk_nina_b1``
      - `u-blox EVK-NINA-B1 <https://os.mbed.com/platforms/u-blox-EVK-NINA-B1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64 MHz
      - 512K
      - 64K
    * - ``ublox_evk_odin_w2``
      - `u-blox EVK-ODIN-W2 <https://developer.mbed.org/platforms/ublox-EVK-ODIN-W2/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F439ZIY6
      - 168 MHz
      - 2M
      - 256K
    * - ``ubloxc027``
      - `u-blox C027 <https://developer.mbed.org/platforms/u-blox-C027/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC1768
      - 96 MHz
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

y5 design
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
    * - ``lpc11u35_y5_mbug``
      - `y5 LPC11U35 mbug <https://developer.mbed.org/platforms/Y5-LPC11U35-MBUG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U35
      - 48 MHz
      - 64K
      - 10K
    * - ``nrf51822_y5_mbug``
      - `y5 nRF51822 mbug <https://developer.mbed.org/platforms/Y5-NRF51822-MBUG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16 MHz
      - 256K
      - 16K
