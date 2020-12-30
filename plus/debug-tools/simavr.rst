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

.. _debugging_tool_simavr:

simavr
======

simavr is a lean, mean and hackable AVR simulator.
Official reference can be found `here  <https://github.com/buserror/simavr/?utm_source=platformio&utm_medium=docs>`__.

.. contents:: Contents
    :local:

Configuration
-------------

You can configure debugging tool using :ref:`projectconf_debug_tool` option in
:ref:`projectconf`:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    debug_tool = simavr

More options:

* :ref:`projectconf_section_env_debug`

.. begin_platforms

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_atmelavr`
      - Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences

    * - :ref:`framework_simba`
      - Simba is an RTOS and build framework with aims to make embedded programming easy and portable

Boards
------

.. note::
    For more detailed ``board`` information please scroll tables below by horizontal.


.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_ATmega128`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA128
      - 16MHz
      - 128KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega1280`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1280
      - 16MHz
      - 128KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega1281`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1281
      - 16MHz
      - 128KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega1284`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_ATmega1284P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_ATmega16`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA16
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega164P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA164P
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega168P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168P
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega2560`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 256KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega324A`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA324A
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega324P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA324P
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega324PA`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA324PA
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega328P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega48`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA48
      - 16MHz
      - 4KB
      - 512B
    * - :ref:`board_atmelavr_ATmega48P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA48P
      - 16MHz
      - 4KB
      - 512B
    * - :ref:`board_atmelavr_ATmega644P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA644P
      - 16MHz
      - 64KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega8`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA8
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega88`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA88
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega88P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA88P
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_attiny13`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY13
      - 9MHz
      - 1KB
      - 64B
    * - :ref:`board_atmelavr_attiny13a`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY13A
      - 9MHz
      - 1KB
      - 64B
    * - :ref:`board_atmelavr_bluefruitmicro`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_circuitplay_classic`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_feather328p`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_feather32u4`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_flora8`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_gemma`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_itsybitsy32u4_3V`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_itsybitsy32u4_5V`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_metro`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket3ftdi`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 12MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket3`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 12MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket5ftdi`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket5`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_trinket3`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_trinket5`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY85
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_alorium_hinj`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_alorium_sno`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_alorium_xlr8`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_miniwireless`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_arduboy`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_arduboy_devkit`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_btatmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_btatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_diecimilaatmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_diecimilaatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_esplora`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_ethernet`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_fio`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_chiwawa`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_leonardo`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_leonardoeth`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_lilypadatmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 8MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_lilypadatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_LilyPadUSB`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_megaADK`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_megaatmega1280`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1280
      - 16MHz
      - 124KB
      - 8KB
    * - :ref:`board_atmelavr_megaatmega2560`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_micro`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_miniatmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_miniatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_atmegangatmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_atmegangatmega8`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA8
      - 16MHz
      - 7KB
      - 1KB
    * - :ref:`board_atmelavr_nanoatmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_nanoatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_nanoatmega328new`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_pro8MHzatmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 8MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_pro16MHzatmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_pro8MHzatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_pro16MHzatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_robotControl`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_robotMotor`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_uno`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_yun`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_yunmini`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_zumbt328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_raspduino`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_controllino_maxi`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_maxi_automation`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_mega`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_mini`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_digispark-tiny`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY85
      - 16MHz
      - 5.87KB
      - 512B
    * - :ref:`board_atmelavr_engduinov3`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_mayfly`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_fysetc_f6_13`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_attiny2313`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY2313
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny24`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY24
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny25`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY25
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny4313`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY4313
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny44`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY44
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny45`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY45
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny84`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY84
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_attiny85`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_lightblue-bean`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_lightblue-beanplus`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_lightup`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_one`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_smart7688`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_lora32u4II`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_mightyhat`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31KB
      - 2KB
    * - :ref:`board_atmelavr_moteino`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_moteino8mhz`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_moteinomega`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_168pa16m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168P
      - 16MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_168pa8m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168P
      - 8MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_328p16m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_328p8m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_32u416m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_1284p16m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_1284p8m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_644pa16m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_644pa8m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA644P
      - 8MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_emonpi`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_prusa_mm_control`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_panStampAVR`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_a-star32U4`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_prusa_rambo`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_quirkbot`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_blend`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_blendmicro16`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_blendmicro8`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_reprap_rambo`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_sodaq_galora`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_mbili`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_moja`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sodaq_ndogo`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_tatu`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sanguino_atmega1284p`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sanguino_atmega1284_8m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sanguino_atmega644`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA644
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644_8m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA644
      - 8MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644p`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644p_8m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA644P
      - 8MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_seeeduino`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_satmega128rfa1`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA128RFA1
      - 16MHz
      - 16KB
      - 124KB
    * - :ref:`board_atmelavr_sparkfun_digitalsandbox`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_fiov3`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_makeymakey`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_megapro8MHz`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 8MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_sparkfun_megapro16MHz`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_sparkfun_megamini`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 8MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_uview`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_promicro8`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_promicro16`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_qduinomini`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_redboard`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_serial7seg`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sleepypi`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_whispernode`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_the_things_uno`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_tinyduino`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_tinylily`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_usbasp`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA8
      - 12MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_wildfirev2`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 16MHz
      - 120.00KB
      - 16KB
    * - :ref:`board_atmelavr_wildfirev3`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_ftduino`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_bob3`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA88
      - 8MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_nibo2`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA128
      - 16MHz
      - 128KB
      - 4KB
    * - :ref:`board_atmelavr_niboburger`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA16
      - 15MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_niboburger_1284`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 20MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_nibobee`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA16
      - 15MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_nibobee_1284`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 20MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_ardhat`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
