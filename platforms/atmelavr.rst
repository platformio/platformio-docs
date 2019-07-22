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

:Configuration:
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
      - Arduino Wiring-based Framework (AVR Core)

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

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_bluefruitmicro`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_circuitplay_classic`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_feather328p`
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_feather32u4`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_flora8`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_gemma`
      - No
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_itsybitsy32u4_3V`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_itsybitsy32u4_5V`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_metro`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket3ftdi`
      - No
      - ATMEGA328P
      - 12MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket3`
      - No
      - ATMEGA328P
      - 12MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket5ftdi`
      - No
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket5`
      - No
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_trinket3`
      - No
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_trinket5`
      - No
      - ATTINY85
      - 16MHz
      - 8KB
      - 512B

Alorium Technology
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_alorium_hinj`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_alorium_sno`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_alorium_xlr8`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

Anarduino
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_miniwireless`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

Arduboy
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_arduboy`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_arduboy_devkit`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

Arduino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_btatmega168`
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_btatmega328`
      - No
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_diecimilaatmega168`
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_diecimilaatmega328`
      - No
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_esplora`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_ethernet`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_fio`
      - No
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_chiwawa`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_leonardo`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_leonardoeth`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_lilypadatmega168`
      - No
      - ATMEGA168
      - 8MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_lilypadatmega328`
      - No
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_LilyPadUSB`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_megaADK`
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_megaatmega1280`
      - No
      - ATMEGA1280
      - 16MHz
      - 124KB
      - 8KB
    * - :ref:`board_atmelavr_megaatmega2560`
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_micro`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_miniatmega168`
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_miniatmega328`
      - No
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_atmegangatmega168`
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_atmegangatmega8`
      - No
      - ATMEGA8
      - 16MHz
      - 7KB
      - 1KB
    * - :ref:`board_atmelavr_nanoatmega168`
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_nanoatmega328`
      - No
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_nanoatmega328new`
      - No
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_pro8MHzatmega168`
      - No
      - ATMEGA168
      - 8MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_pro16MHzatmega168`
      - No
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_pro8MHzatmega328`
      - No
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_pro16MHzatmega328`
      - No
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_robotControl`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_robotMotor`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_uno`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_yun`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_yunmini`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

Atmel
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_attiny13`
      - No
      - ATTINY13
      - 1MHz
      - 1KB
      - 64B
    * - :ref:`board_atmelavr_attiny13a`
      - No
      - ATTINY13A
      - 1MHz
      - 1KB
      - 64B
    * - :ref:`board_atmelavr_attiny1634`
      - No
      - ATTINY1634
      - 8MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_attiny167`
      - No
      - ATTINY167
      - 8MHz
      - 16KB
      - 512B
    * - :ref:`board_atmelavr_attiny2313`
      - No
      - ATTINY2313
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny24`
      - No
      - ATTINY24
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny25`
      - No
      - ATTINY25
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny261`
      - No
      - ATTINY261
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny4313`
      - No
      - ATTINY4313
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny43`
      - No
      - ATTINY43U
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny44`
      - No
      - ATTINY44
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny441`
      - No
      - ATTINY441
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny45`
      - No
      - ATTINY45
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny461`
      - No
      - ATTINY461
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny48`
      - No
      - ATTINY48
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny828`
      - No
      - ATTINY828
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_attiny84`
      - No
      - ATTINY84
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_attiny841`
      - No
      - ATTINY841
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_attiny85`
      - No
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_attiny861`
      - No
      - ATTINY861
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_attiny87`
      - No
      - ATTINY87
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_attiny88`
      - No
      - ATTINY88
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_usbasp`
      - No
      - ATMEGA8
      - 12MHz
      - 8KB
      - 1KB

BQ
~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_zumbt328`
      - No
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB

BSFrance
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_lora32u4II`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB

BitWizard
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_raspduino`
      - No
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB

Controllino
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_controllino_maxi`
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_maxi_automation`
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_mega`
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_mini`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

Digistump
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_digispark-pro`
      - No
      - ATTINY167
      - 16MHz
      - 14.50KB
      - 512B
    * - :ref:`board_atmelavr_digispark-pro64`
      - No
      - ATTINY167
      - 16MHz
      - 14.50KB
      - 512B
    * - :ref:`board_atmelavr_digispark-pro32`
      - No
      - ATTINY167
      - 16MHz
      - 14.50KB
      - 512B
    * - :ref:`board_atmelavr_digispark-tiny`
      - No
      - ATTINY85
      - 16MHz
      - 5.87KB
      - 512B

Dwengo
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_dwenguino`
      - No
      - AT90USB646
      - 16MHz
      - 60KB
      - 2KB

Elektor
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_elektor_uno_r4`
      - No
      - ATMEGA328PB
      - 16MHz
      - 31.50KB
      - 2KB

Engduino
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_engduinov3`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB

EnviroDIY
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_mayfly`
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB

FYSETC
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_fysetc_f6_13`
      - No
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB

LightUp
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_lightup`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB

Linino
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_one`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

LowPowerLab
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_mightyhat`
      - No
      - ATMEGA328P
      - 16MHz
      - 31KB
      - 2KB
    * - :ref:`board_atmelavr_moteino`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_moteino8mhz`
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_moteinomega`
      - No
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB

MediaTek Labs
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_smart7688`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB

Microchip
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_AT90CAN128`
      - No
      - AT90CAN128
      - 16MHz
      - 127KB
      - 4KB
    * - :ref:`board_atmelavr_AT90CAN32`
      - No
      - AT90CAN32
      - 16MHz
      - 31KB
      - 2KB
    * - :ref:`board_atmelavr_AT90CAN64`
      - No
      - AT90CAN64
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega128`
      - No
      - ATMEGA128
      - 16MHz
      - 127KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega1280`
      - No
      - ATMEGA1280
      - 16MHz
      - 127KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega1281`
      - No
      - ATMEGA1281
      - 16MHz
      - 127KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega1284`
      - No
      - ATMEGA1284
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_ATmega1284P`
      - No
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_ATmega16`
      - No
      - ATMEGA16
      - 16MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega164A`
      - No
      - ATMEGA164A
      - 16MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega164P`
      - No
      - ATMEGA164P
      - 16MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega168`
      - No
      - ATMEGA168
      - 16MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega168P`
      - No
      - ATMEGA168P
      - 16MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega168PB`
      - No
      - ATMEGA168PB
      - 16MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega2560`
      - No
      - ATMEGA2560
      - 16MHz
      - 255KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega2561`
      - No
      - ATMEGA2561
      - 16MHz
      - 255KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega32`
      - No
      - ATMEGA32
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega324A`
      - No
      - ATMEGA324A
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega324P`
      - No
      - ATMEGA324P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega324PA`
      - No
      - ATMEGA324PA
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega324PB`
      - No
      - ATMEGA324PB
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega328`
      - No
      - ATMEGA328
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega328P`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega328PB`
      - No
      - ATMEGA328PB
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega48`
      - No
      - ATMEGA48
      - 16MHz
      - 4KB
      - 512B
    * - :ref:`board_atmelavr_ATmega48PB`
      - No
      - ATMEGA48PB
      - 16MHz
      - 4KB
      - 512B
    * - :ref:`board_atmelavr_ATmega64`
      - No
      - ATMEGA64
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega640`
      - No
      - ATMEGA640
      - 16MHz
      - 63KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega644A`
      - No
      - ATMEGA644A
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega644P`
      - No
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega8`
      - No
      - ATMEGA8
      - 16MHz
      - 7.50KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega8535`
      - No
      - ATMEGA8535
      - 16MHz
      - 7.50KB
      - 512B
    * - :ref:`board_atmelavr_ATmega88`
      - No
      - ATMEGA88
      - 16MHz
      - 7.50KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega88P`
      - No
      - ATMEGA88P
      - 16MHz
      - 7.50KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega88PB`
      - No
      - ATMEGA88PB
      - 16MHz
      - 7.50KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega48P`
      - No
      - ATMEGA48P
      - 16MHz
      - 4KB
      - 512B
    * - :ref:`board_atmelavr_at90pwm216`
      - No
      - AT90PWM216
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_at90pwm316`
      - No
      - AT90PWM316
      - 16MHz
      - 16KB
      - 1KB

Microduino
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_168pa16m`
      - No
      - ATMEGA168P
      - 16MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_168pa8m`
      - No
      - ATMEGA168P
      - 8MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_328p16m`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_328p8m`
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_32u416m`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_1284p16m`
      - No
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_1284p8m`
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_644pa16m`
      - No
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_644pa8m`
      - No
      - ATMEGA644P
      - 8MHz
      - 63KB
      - 4KB

OpenEnergyMonitor
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_emonpi`
      - No
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB

PanStamp
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_panStampAVR`
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB

Pinoccio
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_pinoccio`
      - No
      - ATMEGA256RFR2
      - 16MHz
      - 248KB
      - 32KB

Pololu Corporation
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_a-star32U4`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

Punch Through
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_lightblue-bean`
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_lightblue-beanplus`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

Quirkbot
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_quirkbot`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB

RedBearLab
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_blend`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_blendmicro16`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_blendmicro8`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB

RepRap
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_reprap_rambo`
      - No
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB

SODAQ
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_sodaq_galora`
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_mbili`
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_moja`
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sodaq_ndogo`
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_tatu`
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB

Sanguino
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_sanguino_atmega1284p`
      - No
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sanguino_atmega1284_8m`
      - No
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sanguino_atmega644`
      - No
      - ATMEGA644
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644_8m`
      - No
      - ATMEGA644
      - 8MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644p`
      - No
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644p_8m`
      - No
      - ATMEGA644P
      - 8MHz
      - 63KB
      - 4KB

SeeedStudio
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_seeeduino`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

SparkFun
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_sparkfun_satmega128rfa1`
      - No
      - ATMEGA128RFA1
      - 16MHz
      - 16KB
      - 124KB
    * - :ref:`board_atmelavr_sparkfun_digitalsandbox`
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_fiov3`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_makeymakey`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_megapro8MHz`
      - No
      - ATMEGA2560
      - 8MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_sparkfun_megapro16MHz`
      - No
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_sparkfun_megamini`
      - No
      - ATMEGA2560
      - 8MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_uview`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_promicro8`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_promicro16`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_qduinomini`
      - No
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_redboard`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_serial7seg`
      - No
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB

SpellFoundry
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_sleepypi`
      - No
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB

The Things Network
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_the_things_uno`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

Till Harbaum
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_ftduino`
      - No
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

TinyCircuits
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_tinyduino`
      - No
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_tinylily`
      - No
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB

Wicked Device
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_wildfirev2`
      - No
      - ATMEGA1284P
      - 16MHz
      - 120.00KB
      - 16KB
    * - :ref:`board_atmelavr_wildfirev3`
      - No
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB

Wisen
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_whispernode`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

makerlab.mx
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_altair`
      - No
      - ATMEGA256RFR2
      - 16MHz
      - 248KB
      - 32KB

nicai-systems
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_bob3`
      - No
      - ATMEGA88
      - 8MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_nibo2`
      - No
      - ATMEGA128
      - 16MHz
      - 128KB
      - 4KB
    * - :ref:`board_atmelavr_niboburger`
      - No
      - ATMEGA16
      - 15MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_niboburger_1284`
      - No
      - ATMEGA1284P
      - 20MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_nibobee`
      - No
      - ATMEGA16
      - 15MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_nibobee_1284`
      - No
      - ATMEGA1284P
      - 20MHz
      - 128KB
      - 16KB

ubIQio
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_ardhat`
      - No
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
