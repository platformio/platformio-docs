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

.. _debugging_tool_avr-stub:

avr-stub
========

avr-stub is a source level debugger based on GDB stub mechanism. It works with ATmega328
and Arduino Mega microcontrollers without an external programmer. The official reference
can be found `here  <https://github.com/jdolinay/avr_debug/?utm_source=platformio&utm_medium=docs>`__.

.. contents:: Contents
    :local:

.. include:: avr-stub_extra.rst

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
    * - :ref:`board_atmelavr_ATmega1280`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1280
      - 16MHz
      - 128KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega2560`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 256KB
      - 8KB
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
    * - :ref:`board_atmelavr_feather328p`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
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
    * - :ref:`board_atmelavr_protrinket5ftdi`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
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
    * - :ref:`board_atmelavr_btatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_diecimilaatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
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
    * - :ref:`board_atmelavr_lilypadatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
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
    * - :ref:`board_atmelavr_miniatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
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
    * - :ref:`board_atmelavr_uno`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
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
    * - :ref:`board_atmelavr_fysetc_f6_13`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB
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
    * - :ref:`board_atmelavr_emonpi`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_panStampAVR`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_prusa_rambo`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_reprap_rambo`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_sodaq_moja`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_seeeduino`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_digitalsandbox`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
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
    * - :ref:`board_atmelavr_ardhat`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
