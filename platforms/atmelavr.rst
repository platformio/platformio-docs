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

Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

For more detailed information please visit `vendor site <http://www.atmel.com/products/microcontrollers/avr/default.aspx?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: atmelavr_extra.rst

Examples
--------

Examples are listed from `Atmel AVR development platform repository <https://github.com/platformio/platform-atmelavr/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `arduino-blink <https://github.com/platformio/platform-atmelavr/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `simba-blink <https://github.com/platformio/platform-atmelavr/tree/master/examples/simba-blink?utm_source=platformio.org&utm_medium=docs>`_
* `native-blink <https://github.com/platformio/platform-atmelavr/tree/master/examples/native-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-own-src_dir <https://github.com/platformio/platform-atmelavr/tree/master/examples/arduino-own-src_dir?utm_source=platformio.org&utm_medium=docs>`_
* `engduino-magnetometer <https://github.com/platformio/platform-atmelavr/tree/master/examples/engduino-magnetometer?utm_source=platformio.org&utm_medium=docs>`_
* `digitstump-mouse <https://github.com/platformio/platform-atmelavr/tree/master/examples/digitstump-mouse?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-atmelavr/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-external-libs <https://github.com/platformio/platform-atmelavr/tree/master/examples/arduino-external-libs?utm_source=platformio.org&utm_medium=docs>`_

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. contents::
    :local:


Tools & Debug Probes
~~~~~~~~~~~~~~~~~~~~

Supported debugging tools are listed in "Debug" column. For more detailed
information, please scroll table by horizontal.
You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further instructions.


On-Board Debug Tools
^^^^^^^^^^^^^^^^^^^^

Boards listed below have on-board debug probe and **ARE READY** for debugging!
You do not need to use/buy external debug probe.


.. list-table::
    :header-rows:  1

    * - Name
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_ATmega128`
      - ATMEGA128
      - 16MHz
      - 128KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega1280`
      - ATMEGA1280
      - 16MHz
      - 128KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega1281`
      - ATMEGA1281
      - 16MHz
      - 128KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega1284`
      - ATMEGA1284
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_ATmega1284P`
      - ATMEGA1284P
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_ATmega16`
      - ATMEGA16
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega164P`
      - ATMEGA164P
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega168`
      - ATMEGA168
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega168P`
      - ATMEGA168P
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega2560`
      - ATMEGA2560
      - 16MHz
      - 256KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega324A`
      - ATMEGA324A
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega324P`
      - ATMEGA324P
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega324PA`
      - ATMEGA324PA
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega328`
      - ATMEGA328
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega328P`
      - ATMEGA328P
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega48`
      - ATMEGA48
      - 16MHz
      - 4KB
      - 512B
    * - :ref:`board_atmelavr_ATmega48P`
      - ATMEGA48P
      - 16MHz
      - 4KB
      - 512B
    * - :ref:`board_atmelavr_ATmega644P`
      - ATMEGA644P
      - 16MHz
      - 64KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega8`
      - ATMEGA8
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega88`
      - ATMEGA88
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega88P`
      - ATMEGA88P
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_attiny13`
      - ATTINY13
      - 9MHz
      - 1KB
      - 64B
    * - :ref:`board_atmelavr_attiny13a`
      - ATTINY13A
      - 9MHz
      - 1KB
      - 64B
    * - :ref:`board_atmelavr_bluefruitmicro`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_circuitplay_classic`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_feather328p`
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_feather32u4`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_flora8`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_gemma`
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_itsybitsy32u4_3V`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_itsybitsy32u4_5V`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_metro`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket3ftdi`
      - ATMEGA328P
      - 12MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket3`
      - ATMEGA328P
      - 12MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket5ftdi`
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket5`
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_trinket3`
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_trinket5`
      - ATTINY85
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_alorium_hinj`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_alorium_sno`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_alorium_xlr8`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_miniwireless`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_arduboy`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_arduboy_devkit`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_btatmega168`
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_btatmega328`
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_diecimilaatmega168`
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_diecimilaatmega328`
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_esplora`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_ethernet`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_fio`
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_chiwawa`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_leonardo`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_leonardoeth`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_lilypadatmega168`
      - ATMEGA168
      - 8MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_lilypadatmega328`
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_LilyPadUSB`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_megaADK`
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_megaatmega1280`
      - ATMEGA1280
      - 16MHz
      - 124KB
      - 8KB
    * - :ref:`board_atmelavr_megaatmega2560`
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_micro`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_miniatmega168`
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_miniatmega328`
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_atmegangatmega168`
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_atmegangatmega8`
      - ATMEGA8
      - 16MHz
      - 7KB
      - 1KB
    * - :ref:`board_atmelavr_nanoatmega168`
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_nanoatmega328`
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_nanoatmega328new`
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_pro8MHzatmega168`
      - ATMEGA168
      - 8MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_pro16MHzatmega168`
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_pro8MHzatmega328`
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_pro16MHzatmega328`
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_robotControl`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_robotMotor`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_uno`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_yun`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_yunmini`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_zumbt328`
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_raspduino`
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_controllino_maxi`
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_maxi_automation`
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_mega`
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_mini`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_digispark-tiny`
      - ATTINY85
      - 16MHz
      - 5.87KB
      - 512B
    * - :ref:`board_atmelavr_engduinov3`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_mayfly`
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_fysetc_f6_13`
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_attiny2313`
      - ATTINY2313
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny24`
      - ATTINY24
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny25`
      - ATTINY25
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny4313`
      - ATTINY4313
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny44`
      - ATTINY44
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny45`
      - ATTINY45
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny84`
      - ATTINY84
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_attiny85`
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_lightblue-bean`
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_lightblue-beanplus`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_lightup`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_one`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_smart7688`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_lora32u4II`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_mightyhat`
      - ATMEGA328P
      - 16MHz
      - 31KB
      - 2KB
    * - :ref:`board_atmelavr_moteino`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_moteino8mhz`
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_moteinomega`
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_168pa16m`
      - ATMEGA168P
      - 16MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_168pa8m`
      - ATMEGA168P
      - 8MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_328p16m`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_328p8m`
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_32u416m`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_1284p16m`
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_1284p8m`
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_644pa16m`
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_644pa8m`
      - ATMEGA644P
      - 8MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_emonpi`
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_prusa_mm_control`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_panStampAVR`
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_a-star32U4`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_prusa_rambo`
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_quirkbot`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_blend`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_blendmicro16`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_blendmicro8`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_reprap_rambo`
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_sodaq_galora`
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_mbili`
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_moja`
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sodaq_ndogo`
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_tatu`
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sanguino_atmega1284p`
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sanguino_atmega1284_8m`
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sanguino_atmega644`
      - ATMEGA644
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644_8m`
      - ATMEGA644
      - 8MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644p`
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644p_8m`
      - ATMEGA644P
      - 8MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_seeeduino`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_satmega128rfa1`
      - ATMEGA128RFA1
      - 16MHz
      - 16KB
      - 124KB
    * - :ref:`board_atmelavr_sparkfun_digitalsandbox`
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_fiov3`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_makeymakey`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_megapro8MHz`
      - ATMEGA2560
      - 8MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_sparkfun_megapro16MHz`
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_sparkfun_megamini`
      - ATMEGA2560
      - 8MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_uview`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_promicro8`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_promicro16`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_qduinomini`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_redboard`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_serial7seg`
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sleepypi`
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_whispernode`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_the_things_uno`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_tinyduino`
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_tinylily`
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_usbasp`
      - ATMEGA8
      - 12MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_wildfirev2`
      - ATMEGA1284P
      - 16MHz
      - 120.00KB
      - 16KB
    * - :ref:`board_atmelavr_wildfirev3`
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_ftduino`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_bob3`
      - ATMEGA88
      - 8MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_nibo2`
      - ATMEGA128
      - 16MHz
      - 128KB
      - 4KB
    * - :ref:`board_atmelavr_niboburger`
      - ATMEGA16
      - 15MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_niboburger_1284`
      - ATMEGA1284P
      - 20MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_nibobee`
      - ATMEGA16
      - 15MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_nibobee_1284`
      - ATMEGA1284P
      - 20MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_ardhat`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB


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

    * - `framework-arduino-avr <https://www.arduino.cc/reference/en?utm_source=platformio.org&utm_medium=docs>`__
      - The official Arduino Wiring-based Framework for Microchip AVR microcontrollers

    * - `framework-arduino-avr-attiny <https://github.com/SpenceKonde/ATTinyCore.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip AVR microcontrollers (ATTiny Core)

    * - `framework-arduino-avr-bean <https://github.com/PunchThrough/bean-arduino-core.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip AVR microcontrollers (Bean Core)

    * - `framework-arduino-avr-core13 <https://sourceforge.net/projects/ard-core13/?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip AVR microcontrollers (Core13)

    * - `framework-arduino-avr-digistump <https://github.com/digistump/DigistumpArduino/tree/master/digistump-avr.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip AVR microcontrollers (Digistump Core)

    * - `framework-arduino-avr-dwenguino <https://github.com/dwengovzw/Dwengo-library/tree/master/dwenguino/Dwenguino.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip AVR microcontrollers (Dwenguino Core)

    * - `framework-arduino-avr-majorcore <https://github.com/MCUdude/MajorCore.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip AVR microcontrollers (MajorCore)

    * - `framework-arduino-avr-megacore <https://github.com/MCUdude/MegaCore.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip AVR microcontrollers (MegaCore)

    * - `framework-arduino-avr-microcore <https://github.com/MCUdude/MicroCore.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip AVR microcontrollers (MicroCore)

    * - `framework-arduino-avr-mightycore <https://github.com/MCUdude/MightyCore.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip AVR microcontrollers (MightyCore)

    * - `framework-arduino-avr-minicore <https://github.com/MCUdude/MiniCore.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip AVR microcontrollers (MiniCore)

    * - `framework-arduino-avr-nicai <http://www.nicai-systems.com/en/?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip AVR microcontrollers (Nicai Core)

    * - `framework-arduino-avr-panstamp <https://github.com/panStamp/panstamp.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip AVR microcontrollers (Panstamp Core)

    * - `framework-arduino-avr-prusa_rambo <https://github.com/prusa3d/Prusa-Firmware.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip AVR microcontrollers (Prusa Rambo Core)

    * - `framework-simba <https://github.com/eerimoq/simba.git?utm_source=platformio.org&utm_medium=docs>`__
      - Simba is an Embedded Programming Platform. It aims to make embedded programming easy and portable

    * - `tool-avrdude <http://savannah.nongnu.org/projects/avrdude?utm_source=platformio.org&utm_medium=docs>`__
      - AVRDUDE is a utility to download/upload/manipulate the ROM and EEPROM contents of AVR microcontrollers

    * - `tool-micronucleus <https://github.com/micronucleus/micronucleus.git?utm_source=platformio.org&utm_medium=docs>`__
      - ATTiny usb bootloader with a strong emphasis on bootloader compactness

    * - `tool-simavr <https://github.com/buserror/simavr.git?utm_source=platformio.org&utm_medium=docs>`__
      - simavr is a lean, mean and hackable AVR simulator

    * - `toolchain-atmelavr <https://gcc.gnu.org/wiki/avr-gcc?utm_source=platformio.org&utm_medium=docs>`__
      - GCC Toolchain for Microchip AVR microcontrollers

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
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences

    * - :ref:`framework_simba`
      - Simba is an RTOS and build framework with aims to make embedded programming easy and portable

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

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
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_circuitplay_classic`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_feather328p`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_feather32u4`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_flora8`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_gemma`
      - On-board
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_itsybitsy32u4_3V`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_itsybitsy32u4_5V`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_metro`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket3ftdi`
      - On-board
      - ATMEGA328P
      - 12MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket3`
      - On-board
      - ATMEGA328P
      - 12MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket5ftdi`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket5`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_trinket3`
      - On-board
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_trinket5`
      - On-board
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
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_alorium_sno`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_alorium_xlr8`
      - On-board
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
      - On-board
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
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_arduboy_devkit`
      - On-board
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
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_btatmega328`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_diecimilaatmega168`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_diecimilaatmega328`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_esplora`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_ethernet`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_fio`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_chiwawa`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_leonardo`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_leonardoeth`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_lilypadatmega168`
      - On-board
      - ATMEGA168
      - 8MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_lilypadatmega328`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_LilyPadUSB`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_megaADK`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_megaatmega1280`
      - On-board
      - ATMEGA1280
      - 16MHz
      - 124KB
      - 8KB
    * - :ref:`board_atmelavr_megaatmega2560`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_micro`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_miniatmega168`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_miniatmega328`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_atmegangatmega168`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_atmegangatmega8`
      - On-board
      - ATMEGA8
      - 16MHz
      - 7KB
      - 1KB
    * - :ref:`board_atmelavr_nanoatmega168`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_nanoatmega328`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_nanoatmega328new`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_pro8MHzatmega168`
      - On-board
      - ATMEGA168
      - 8MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_pro16MHzatmega168`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_pro8MHzatmega328`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_pro16MHzatmega328`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_robotControl`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_robotMotor`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_uno`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_yun`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_yunmini`
      - On-board
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
      - On-board
      - ATTINY2313
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny24`
      - On-board
      - ATTINY24
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny25`
      - On-board
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
      - On-board
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
      - On-board
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
      - On-board
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
      - On-board
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
      - On-board
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
      - On-board
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
      - On-board
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
      - On-board
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
      - On-board
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
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_maxi_automation`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_mega`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_mini`
      - On-board
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
      - On-board
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
      - On-board
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
      - On-board
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
      - On-board
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
      - On-board
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
      - On-board
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
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31KB
      - 2KB
    * - :ref:`board_atmelavr_moteino`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_moteino8mhz`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_moteinomega`
      - On-board
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
      - On-board
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
      - 128KB
      - 4KB
    * - :ref:`board_atmelavr_AT90CAN32`
      - No
      - AT90CAN32
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_AT90CAN64`
      - No
      - AT90CAN64
      - 16MHz
      - 64KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega128`
      - On-board
      - ATMEGA128
      - 16MHz
      - 128KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega1280`
      - On-board
      - ATMEGA1280
      - 16MHz
      - 128KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega1281`
      - On-board
      - ATMEGA1281
      - 16MHz
      - 128KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega1284`
      - On-board
      - ATMEGA1284
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_ATmega1284P`
      - On-board
      - ATMEGA1284P
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_ATmega16`
      - On-board
      - ATMEGA16
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega162`
      - No
      - ATMEGA162
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega164A`
      - No
      - ATMEGA164A
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega164P`
      - On-board
      - ATMEGA164P
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega168`
      - On-board
      - ATMEGA168
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega168P`
      - On-board
      - ATMEGA168P
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega168PB`
      - No
      - ATMEGA168PB
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega2560`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 256KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega2561`
      - No
      - ATMEGA2561
      - 16MHz
      - 256KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega32`
      - No
      - ATMEGA32
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega324A`
      - On-board
      - ATMEGA324A
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega324P`
      - On-board
      - ATMEGA324P
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega324PA`
      - On-board
      - ATMEGA324PA
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega324PB`
      - No
      - ATMEGA324PB
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega328`
      - On-board
      - ATMEGA328
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega328P`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega328PB`
      - No
      - ATMEGA328PB
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega48`
      - On-board
      - ATMEGA48
      - 16MHz
      - 4KB
      - 512B
    * - :ref:`board_atmelavr_ATmega48P`
      - On-board
      - ATMEGA48P
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
      - 64KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega640`
      - No
      - ATMEGA640
      - 16MHz
      - 64KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega644A`
      - No
      - ATMEGA644A
      - 16MHz
      - 64KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega644P`
      - On-board
      - ATMEGA644P
      - 16MHz
      - 64KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega8`
      - On-board
      - ATMEGA8
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega8515`
      - No
      - ATMEGA8515
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_ATmega8535`
      - No
      - ATMEGA8535
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_ATmega88`
      - On-board
      - ATMEGA88
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega88P`
      - On-board
      - ATMEGA88P
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega88PB`
      - No
      - ATMEGA88PB
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_attiny13`
      - On-board
      - ATTINY13
      - 9MHz
      - 1KB
      - 64B
    * - :ref:`board_atmelavr_attiny13a`
      - On-board
      - ATTINY13A
      - 9MHz
      - 1KB
      - 64B
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
      - On-board
      - ATMEGA168P
      - 16MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_168pa8m`
      - On-board
      - ATMEGA168P
      - 8MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_328p16m`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_328p8m`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_32u416m`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_1284p16m`
      - On-board
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_1284p8m`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_644pa16m`
      - On-board
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_644pa8m`
      - On-board
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
      - On-board
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
      - On-board
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
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

Prusa 3D
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_prusa_mm_control`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_prusa_rambo`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB

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
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_lightblue-beanplus`
      - On-board
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
      - On-board
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
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_blendmicro16`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_blendmicro8`
      - On-board
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
      - On-board
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
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_mbili`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_moja`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sodaq_ndogo`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_tatu`
      - On-board
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
      - On-board
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sanguino_atmega1284_8m`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sanguino_atmega644`
      - On-board
      - ATMEGA644
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644_8m`
      - On-board
      - ATMEGA644
      - 8MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644p`
      - On-board
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644p_8m`
      - On-board
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
      - On-board
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
      - On-board
      - ATMEGA128RFA1
      - 16MHz
      - 16KB
      - 124KB
    * - :ref:`board_atmelavr_sparkfun_digitalsandbox`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_fiov3`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_makeymakey`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_megapro8MHz`
      - On-board
      - ATMEGA2560
      - 8MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_sparkfun_megapro16MHz`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_sparkfun_megamini`
      - On-board
      - ATMEGA2560
      - 8MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_uview`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_promicro8`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_promicro16`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_qduinomini`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_redboard`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_serial7seg`
      - On-board
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
      - On-board
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
      - On-board
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
      - On-board
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
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_tinylily`
      - On-board
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
      - On-board
      - ATMEGA1284P
      - 16MHz
      - 120.00KB
      - 16KB
    * - :ref:`board_atmelavr_wildfirev3`
      - On-board
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
      - On-board
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
      - On-board
      - ATMEGA88
      - 8MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_nibo2`
      - On-board
      - ATMEGA128
      - 16MHz
      - 128KB
      - 4KB
    * - :ref:`board_atmelavr_niboburger`
      - On-board
      - ATMEGA16
      - 15MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_niboburger_1284`
      - On-board
      - ATMEGA1284P
      - 20MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_nibobee`
      - On-board
      - ATMEGA16
      - 15MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_nibobee_1284`
      - On-board
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
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
