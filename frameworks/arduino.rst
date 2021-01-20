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

.. _framework_arduino:

Arduino
=======

:Configuration:
  :ref:`projectconf_env_framework` = ``arduino``

Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences

For more detailed information please visit `vendor site <http://arduino.cc/en/Reference/HomePage?utm_source=platformio.org&utm_medium=docs>`_.


.. contents:: Contents
    :local:
    :depth: 1
.. include:: arduino_extra.rst

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
      - Platform
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_remram_v1`
      - :ref:`platform_ststm32`
      - STM32F765VIT6
      - 216MHz
      - 2MB
      - 512KB
    * - :ref:`board_ststm32_st3dp001_eval`
      - :ref:`platform_ststm32`
      - STM32F401VGT6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelavr_ATmega128`
      - :ref:`platform_atmelavr`
      - ATMEGA128
      - 16MHz
      - 128KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega1280`
      - :ref:`platform_atmelavr`
      - ATMEGA1280
      - 16MHz
      - 128KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega1281`
      - :ref:`platform_atmelavr`
      - ATMEGA1281
      - 16MHz
      - 128KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega1284`
      - :ref:`platform_atmelavr`
      - ATMEGA1284
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_ATmega1284P`
      - :ref:`platform_atmelavr`
      - ATMEGA1284P
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_ATmega16`
      - :ref:`platform_atmelavr`
      - ATMEGA16
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega164P`
      - :ref:`platform_atmelavr`
      - ATMEGA164P
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega168`
      - :ref:`platform_atmelavr`
      - ATMEGA168
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega168P`
      - :ref:`platform_atmelavr`
      - ATMEGA168P
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega2560`
      - :ref:`platform_atmelavr`
      - ATMEGA2560
      - 16MHz
      - 256KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega324A`
      - :ref:`platform_atmelavr`
      - ATMEGA324A
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega324P`
      - :ref:`platform_atmelavr`
      - ATMEGA324P
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega324PA`
      - :ref:`platform_atmelavr`
      - ATMEGA324PA
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega328`
      - :ref:`platform_atmelavr`
      - ATMEGA328
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega328P`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega48`
      - :ref:`platform_atmelavr`
      - ATMEGA48
      - 16MHz
      - 4KB
      - 512B
    * - :ref:`board_atmelavr_ATmega48P`
      - :ref:`platform_atmelavr`
      - ATMEGA48P
      - 16MHz
      - 4KB
      - 512B
    * - :ref:`board_atmelavr_ATmega644P`
      - :ref:`platform_atmelavr`
      - ATMEGA644P
      - 16MHz
      - 64KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega8`
      - :ref:`platform_atmelavr`
      - ATMEGA8
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega88`
      - :ref:`platform_atmelavr`
      - ATMEGA88
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega88P`
      - :ref:`platform_atmelavr`
      - ATMEGA88P
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_attiny13`
      - :ref:`platform_atmelavr`
      - ATTINY13
      - 9MHz
      - 1KB
      - 64B
    * - :ref:`board_atmelavr_attiny13a`
      - :ref:`platform_atmelavr`
      - ATTINY13A
      - 9MHz
      - 1KB
      - 64B
    * - :ref:`board_atmelavr_bluefruitmicro`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_circuitplay_classic`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_feather328p`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_feather32u4`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_flora8`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_gemma`
      - :ref:`platform_atmelavr`
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_itsybitsy32u4_3V`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_itsybitsy32u4_5V`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_metro`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket3ftdi`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 12MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket3`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 12MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket5ftdi`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket5`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_trinket3`
      - :ref:`platform_atmelavr`
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_trinket5`
      - :ref:`platform_atmelavr`
      - ATTINY85
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_alorium_hinj`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_alorium_sno`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_alorium_xlr8`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_miniwireless`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_arduboy`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_arduboy_devkit`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_btatmega168`
      - :ref:`platform_atmelavr`
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_btatmega328`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_diecimilaatmega168`
      - :ref:`platform_atmelavr`
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_diecimilaatmega328`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_esplora`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_ethernet`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_fio`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_chiwawa`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_leonardo`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_leonardoeth`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_lilypadatmega168`
      - :ref:`platform_atmelavr`
      - ATMEGA168
      - 8MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_lilypadatmega328`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_LilyPadUSB`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelsam_mzeropro`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelavr_megaADK`
      - :ref:`platform_atmelavr`
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_megaatmega1280`
      - :ref:`platform_atmelavr`
      - ATMEGA1280
      - 16MHz
      - 124KB
      - 8KB
    * - :ref:`board_atmelavr_megaatmega2560`
      - :ref:`platform_atmelavr`
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_micro`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_miniatmega168`
      - :ref:`platform_atmelavr`
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_miniatmega328`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_atmegangatmega168`
      - :ref:`platform_atmelavr`
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_atmegangatmega8`
      - :ref:`platform_atmelavr`
      - ATMEGA8
      - 16MHz
      - 7KB
      - 1KB
    * - :ref:`board_atmelavr_nanoatmega168`
      - :ref:`platform_atmelavr`
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_nanoatmega328`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_nanoatmega328new`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_pro8MHzatmega168`
      - :ref:`platform_atmelavr`
      - ATMEGA168
      - 8MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_pro16MHzatmega168`
      - :ref:`platform_atmelavr`
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_pro8MHzatmega328`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_pro16MHzatmega328`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_robotControl`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_robotMotor`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_uno`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_yun`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_yunmini`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelsam_zero`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_samd21g18a`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_bbcmicrobit`
      - :ref:`platform_nordicnrf51`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf52_bbcmicrobit_v2`
      - :ref:`platform_nordicnrf52`
      - NRF52833
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_atmelavr_zumbt328`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_raspduino`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_nordicnrf51_calliope_mini`
      - :ref:`platform_nordicnrf51`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_atmelavr_controllino_maxi`
      - :ref:`platform_atmelavr`
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_maxi_automation`
      - :ref:`platform_atmelavr`
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_mega`
      - :ref:`platform_atmelavr`
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_mini`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_nordicnrf52_delta_dfbm_nq620`
      - :ref:`platform_nordicnrf52`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_atmelavr_digispark-tiny`
      - :ref:`platform_atmelavr`
      - ATTINY85
      - 16MHz
      - 5.87KB
      - 512B
    * - :ref:`board_atmelavr_engduinov3`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_mayfly`
      - :ref:`platform_atmelavr`
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_espressif32_esp-wrover-kit`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_atmelavr_fysetc_f6_13`
      - :ref:`platform_atmelavr`
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_attiny2313`
      - :ref:`platform_atmelavr`
      - ATTINY2313
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny24`
      - :ref:`platform_atmelavr`
      - ATTINY24
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny25`
      - :ref:`platform_atmelavr`
      - ATTINY25
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny4313`
      - :ref:`platform_atmelavr`
      - ATTINY4313
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny44`
      - :ref:`platform_atmelavr`
      - ATTINY44
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny45`
      - :ref:`platform_atmelavr`
      - ATTINY45
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny84`
      - :ref:`platform_atmelavr`
      - ATTINY84
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_attiny85`
      - :ref:`platform_atmelavr`
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_lightblue-bean`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_lightblue-beanplus`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_lightup`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_one`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_smart7688`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_lora32u4II`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_mightyhat`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31KB
      - 2KB
    * - :ref:`board_atmelavr_moteino`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_moteino8mhz`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_moteinomega`
      - :ref:`platform_atmelavr`
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_168pa16m`
      - :ref:`platform_atmelavr`
      - ATMEGA168P
      - 16MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_168pa8m`
      - :ref:`platform_atmelavr`
      - ATMEGA168P
      - 8MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_328p16m`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_328p8m`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_32u416m`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_1284p16m`
      - :ref:`platform_atmelavr`
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_1284p8m`
      - :ref:`platform_atmelavr`
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_644pa16m`
      - :ref:`platform_atmelavr`
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_644pa8m`
      - :ref:`platform_atmelavr`
      - ATMEGA644P
      - 8MHz
      - 63KB
      - 4KB
    * - :ref:`board_ststm32_mxchip_az3166`
      - :ref:`platform_ststm32`
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf51_nrf51_beacon`
      - :ref:`platform_nordicnrf51`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_nrf51_dongle`
      - :ref:`platform_nordicnrf51`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_nrf51_dk`
      - :ref:`platform_nordicnrf51`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf52_nrf52_dk`
      - :ref:`platform_nordicnrf52`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52840_dk`
      - :ref:`platform_nordicnrf52`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_nrf52840_dk_adafruit`
      - :ref:`platform_nordicnrf52`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_atmelavr_emonpi`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_prusa_mm_control`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_ststm32_nucleo_wb55rg_p`
      - :ref:`platform_ststm32`
      - STM32WB55RG
      - 64MHz
      - 512KB
      - 192.00KB
    * - :ref:`board_atmelavr_panStampAVR`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_a-star32U4`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_prusa_rambo`
      - :ref:`platform_atmelavr`
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_quirkbot`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_nordicnrf51_redBearLabBLENano`
      - :ref:`platform_nordicnrf51`
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf52_redbear_blenano2`
      - :ref:`platform_nordicnrf52`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_atmelavr_blend`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_nordicnrf52_redbear_blend2`
      - :ref:`platform_nordicnrf52`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_atmelavr_blendmicro16`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_blendmicro8`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_nordicnrf51_redBearLab`
      - :ref:`platform_nordicnrf51`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_atmelavr_reprap_rambo`
      - :ref:`platform_atmelavr`
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_sodaq_galora`
      - :ref:`platform_atmelavr`
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_mbili`
      - :ref:`platform_atmelavr`
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_moja`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sodaq_ndogo`
      - :ref:`platform_atmelavr`
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_tatu`
      - :ref:`platform_atmelavr`
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_ststm32_disco_f413zh`
      - :ref:`platform_ststm32`
      - STM32F413ZHT6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_disco_f746ng`
      - :ref:`platform_ststm32`
      - STM32F746NGH6
      - 216MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_disco_l475vg_iot01a`
      - :ref:`platform_ststm32`
      - STM32L475VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_disco_l072cz_lrwan1`
      - :ref:`platform_ststm32`
      - STM32L072CZ
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_disco_f072rb`
      - :ref:`platform_ststm32`
      - STM32F072RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f030r8`
      - :ref:`platform_ststm32`
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_nucleo_f031k6`
      - :ref:`platform_ststm32`
      - STM32F031K6T6
      - 48MHz
      - 32KB
      - 4KB
    * - :ref:`board_ststm32_nucleo_f072rb`
      - :ref:`platform_ststm32`
      - STM32F072RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f091rc`
      - :ref:`platform_ststm32`
      - STM32F091RCT6
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_f103rb`
      - :ref:`platform_ststm32`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_nucleo_f207zg`
      - :ref:`platform_ststm32`
      - STM32F207ZGT6
      - 120MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f302r8`
      - :ref:`platform_ststm32`
      - STM32F302R8T6
      - 72MHz
      - 64KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f303k8`
      - :ref:`platform_ststm32`
      - STM32F303K8T6
      - 72MHz
      - 64KB
      - 12KB
    * - :ref:`board_ststm32_nucleo_f303re`
      - :ref:`platform_ststm32`
      - STM32F303RET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_f401re`
      - :ref:`platform_ststm32`
      - STM32F401RET6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_nucleo_f411re`
      - :ref:`platform_ststm32`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f429zi`
      - :ref:`platform_ststm32`
      - STM32F429ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - :ref:`board_ststm32_nucleo_f446re`
      - :ref:`platform_ststm32`
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f746zg`
      - :ref:`platform_ststm32`
      - STM32F746ZGT6
      - 216MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_nucleo_f756zg`
      - :ref:`platform_ststm32`
      - STM32F756ZG
      - 216MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_nucleo_f767zi`
      - :ref:`platform_ststm32`
      - STM32F767ZIT6
      - 216MHz
      - 2MB
      - 512KB
    * - :ref:`board_ststm32_nucleo_h743zi`
      - :ref:`platform_ststm32`
      - STM32H743ZIT6
      - 400MHz
      - 2MB
      - 512KB
    * - :ref:`board_ststm32_nucleo_l031k6`
      - :ref:`platform_ststm32`
      - STM32L031K6T6
      - 32MHz
      - 32KB
      - 8KB
    * - :ref:`board_ststm32_nucleo_l053r8`
      - :ref:`platform_ststm32`
      - STM32L053R8T6
      - 32MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_nucleo_l073rz`
      - :ref:`platform_ststm32`
      - STM32L073RZ
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_nucleo_l152re`
      - :ref:`platform_ststm32`
      - STM32L152RET6
      - 32MHz
      - 512KB
      - 80KB
    * - :ref:`board_ststm32_nucleo_l412kb`
      - :ref:`platform_ststm32`
      - STM32L412KBU6
      - 80MHz
      - 128KB
      - 40KB
    * - :ref:`board_ststm32_nucleo_l432kc`
      - :ref:`platform_ststm32`
      - STM32L432KCU6
      - 80MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_l433rc_p`
      - :ref:`platform_ststm32`
      - STM32L433RC
      - 80MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_l452re`
      - :ref:`platform_ststm32`
      - STM32L452RET6
      - 80MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_l476rg`
      - :ref:`platform_ststm32`
      - STM32L476RGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_l496zg`
      - :ref:`platform_ststm32`
      - STM32L496ZGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_l496zg_p`
      - :ref:`platform_ststm32`
      - STM32L496ZGT6P
      - 80MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_nucleo_l4r5zi`
      - :ref:`platform_ststm32`
      - STM32L4R5ZIT6
      - 120MHz
      - 2MB
      - 640KB
    * - :ref:`board_ststm32_disco_f030r8`
      - :ref:`platform_ststm32`
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_disco_f407vg`
      - :ref:`platform_ststm32`
      - STM32F407VGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_disco_f100rb`
      - :ref:`platform_ststm32`
      - STM32F100RBT6
      - 24MHz
      - 128KB
      - 8KB
    * - :ref:`board_ststm8_stm8sdisco`
      - :ref:`platform_ststm8`
      - STM8S105C6T6
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_sanguino_atmega1284p`
      - :ref:`platform_atmelavr`
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sanguino_atmega1284_8m`
      - :ref:`platform_atmelavr`
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sanguino_atmega644`
      - :ref:`platform_atmelavr`
      - ATMEGA644
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644_8m`
      - :ref:`platform_atmelavr`
      - ATMEGA644
      - 8MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644p`
      - :ref:`platform_atmelavr`
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644p_8m`
      - :ref:`platform_atmelavr`
      - ATMEGA644P
      - 8MHz
      - 63KB
      - 4KB
    * - :ref:`board_nordicnrf51_seeedTinyBLE`
      - :ref:`platform_nordicnrf51`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_atmelavr_seeeduino`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_satmega128rfa1`
      - :ref:`platform_atmelavr`
      - ATMEGA128RFA1
      - 16MHz
      - 16KB
      - 124KB
    * - :ref:`board_atmelavr_sparkfun_digitalsandbox`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_fiov3`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_makeymakey`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_megapro8MHz`
      - :ref:`platform_atmelavr`
      - ATMEGA2560
      - 8MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_sparkfun_megapro16MHz`
      - :ref:`platform_atmelavr`
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_sparkfun_megamini`
      - :ref:`platform_atmelavr`
      - ATMEGA2560
      - 8MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_uview`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_promicro8`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_promicro16`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_qduinomini`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_redboard`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_serial7seg`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sleepypi`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_timsp430_lpmsp430fr5739`
      - :ref:`platform_timsp430`
      - MSP430FR5739
      - 16MHz
      - 15.37KB
      - 1KB
    * - :ref:`board_titiva_lplm4f120h5qr`
      - :ref:`platform_titiva`
      - LPLM4F120H5QR
      - 80MHz
      - 256KB
      - 32KB
    * - :ref:`board_titiva_lptm4c1230c3pm`
      - :ref:`platform_titiva`
      - LPTM4C1230C3PM
      - 80MHz
      - 256KB
      - 32KB
    * - :ref:`board_titiva_lptm4c1294ncpdt`
      - :ref:`platform_titiva`
      - LPTM4C1294NCPDT
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_timsp430_lpmsp430f5529`
      - :ref:`platform_timsp430`
      - MSP430F5529
      - 25MHz
      - 47KB
      - 8KB
    * - :ref:`board_timsp430_lpmsp430fr2311`
      - :ref:`platform_timsp430`
      - MSP430FR2311
      - 16MHz
      - 3.75KB
      - 1KB
    * - :ref:`board_timsp430_lpmsp430fr2433`
      - :ref:`platform_timsp430`
      - MSP430FR2433
      - 8MHz
      - 15KB
      - 4KB
    * - :ref:`board_timsp430_lpmsp430fr4133`
      - :ref:`platform_timsp430`
      - MSP430FR4133
      - 8MHz
      - 15KB
      - 2KB
    * - :ref:`board_timsp430_lpmsp430fr5969`
      - :ref:`platform_timsp430`
      - MSP430FR5969
      - 8MHz
      - 47KB
      - 2KB
    * - :ref:`board_timsp430_lpmsp430fr5994`
      - :ref:`platform_timsp430`
      - MSP430FR5994
      - 16MHz
      - 256KB
      - 4KB
    * - :ref:`board_timsp430_lpmsp430fr6989`
      - :ref:`platform_timsp430`
      - MSP430FR6989
      - 8MHz
      - 47KB
      - 2KB
    * - :ref:`board_timsp430_lpmsp430g2231`
      - :ref:`platform_timsp430`
      - MSP430G2231
      - 1MHz
      - 2KB
      - 256B
    * - :ref:`board_timsp430_lpmsp430g2452`
      - :ref:`platform_timsp430`
      - MSP430G2452
      - 16MHz
      - 8KB
      - 256B
    * - :ref:`board_timsp430_lpmsp430g2553`
      - :ref:`platform_timsp430`
      - MSP430G2553
      - 16MHz
      - 16KB
      - 512B
    * - :ref:`board_atmelavr_whispernode`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_the_things_uno`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_tinyduino`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_tinylily`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_usbasp`
      - :ref:`platform_atmelavr`
      - ATMEGA8
      - 12MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_wildfirev2`
      - :ref:`platform_atmelavr`
      - ATMEGA1284P
      - 16MHz
      - 120.00KB
      - 16KB
    * - :ref:`board_atmelavr_wildfirev3`
      - :ref:`platform_atmelavr`
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1100_boot_kit`
      - :ref:`platform_infineonxmc`
      - XMC1100
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1100_h_bridge2go`
      - :ref:`platform_infineonxmc`
      - XMC1100
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1100_xmc2go`
      - :ref:`platform_infineonxmc`
      - XMC1100
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1300_boot_kit`
      - :ref:`platform_infineonxmc`
      - XMC1300
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1300_sense2gol`
      - :ref:`platform_infineonxmc`
      - XMC1300
      - 32MHz
      - 32KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1400_boot_kit`
      - :ref:`platform_infineonxmc`
      - XMC1400
      - 48MHz
      - 1.95MB
      - 16KB
    * - :ref:`board_infineonxmc_xmc4200_distance2go`
      - :ref:`platform_infineonxmc`
      - XMC4200
      - 80MHz
      - 256KB
      - 40KB
    * - :ref:`board_infineonxmc_xmc4700_relax_kit`
      - :ref:`platform_infineonxmc`
      - XMC4700
      - 144MHz
      - 2.00MB
      - 1.95MB
    * - :ref:`board_nordicnrf52_dwm1001_dev`
      - :ref:`platform_nordicnrf52`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_atmelavr_ftduino`
      - :ref:`platform_atmelavr`
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_bob3`
      - :ref:`platform_atmelavr`
      - ATMEGA88
      - 8MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_nibo2`
      - :ref:`platform_atmelavr`
      - ATMEGA128
      - 16MHz
      - 128KB
      - 4KB
    * - :ref:`board_atmelavr_niboburger`
      - :ref:`platform_atmelavr`
      - ATMEGA16
      - 15MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_niboburger_1284`
      - :ref:`platform_atmelavr`
      - ATMEGA1284P
      - 20MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_nibobee`
      - :ref:`platform_atmelavr`
      - ATMEGA16
      - 15MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_nibobee_1284`
      - :ref:`platform_atmelavr`
      - ATMEGA1284P
      - 20MHz
      - 128KB
      - 16KB
    * - :ref:`board_nordicnrf52_ublox_evk_nina_b1`
      - :ref:`platform_nordicnrf52`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_atmelavr_ardhat`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB


External Debug Tools
^^^^^^^^^^^^^^^^^^^^

Boards listed below are compatible with :ref:`piodebug` but **DEPEND ON**
external debug probe. They **ARE NOT READY** for debugging.
Please click on board name for the further details.


.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_armed_v1`
      - :ref:`platform_ststm32`
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB
    * - :ref:`board_ststm32_rumba32_f446ve`
      - :ref:`platform_ststm32`
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_espressif32_esp32cam`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_alksesp32`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_az-delivery-devkit-v4`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 16MB
      - 520KB
    * - :ref:`board_atmelsam_adafruit_blm_badge`
      - :ref:`platform_atmelsam`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52832`
      - :ref:`platform_nordicnrf52`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_adafruit_clue_nrf52840`
      - :ref:`platform_nordicnrf52`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_atmelsam_adafruit_circuitplayground_m0`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_crickit_m0`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_espressif32_featheresp32`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52840_sense`
      - :ref:`platform_nordicnrf52`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_atmelsam_adafruit_feather_m0`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_feather_m0_express`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_feather_m4_can`
      - :ref:`platform_atmelsam`
      - SAME51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_feather_m4`
      - :ref:`platform_atmelsam`
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_ststm32_adafruit_feather_f405`
      - :ref:`platform_ststm32`
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52840`
      - :ref:`platform_nordicnrf52`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_atmelsam_adafruit_gemma_m0`
      - :ref:`platform_atmelsam`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_grandcentral_m4`
      - :ref:`platform_atmelsam`
      - SAMD51P20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_hallowing`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_hallowing_m4`
      - :ref:`platform_atmelsam`
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_itsybitsy_m0`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_itsybitsy_m4`
      - :ref:`platform_atmelsam`
      - SAMD51G19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_monster_m4sk`
      - :ref:`platform_atmelsam`
      - SAMD51G19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_matrix_portal_m4`
      - :ref:`platform_atmelsam`
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_metro_m0`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_metro_m4`
      - :ref:`platform_atmelsam`
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_metro_m4_airliftlite`
      - :ref:`platform_atmelsam`
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_pygamer_advance_m4`
      - :ref:`platform_atmelsam`
      - SAMD51J20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_pygamer_m4`
      - :ref:`platform_atmelsam`
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_pyportal_m4`
      - :ref:`platform_atmelsam`
      - SAMD51J20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_pyportal_m4_titano`
      - :ref:`platform_atmelsam`
      - SAMD51J20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_qt_py_m0`
      - :ref:`platform_atmelsam`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_trellis_m4`
      - :ref:`platform_atmelsam`
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_trinket_m0`
      - :ref:`platform_atmelsam`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_pirkey`
      - :ref:`platform_atmelsam`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_pybadge_airlift_m4`
      - :ref:`platform_atmelsam`
      - SAMD51J20A
      - 120MHz
      - 1008KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_pybadge_m4`
      - :ref:`platform_atmelsam`
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_ststm32_afroflight_f103cb`
      - :ref:`platform_ststm32`
      - STM32F103CBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_atmelsam_due`
      - :ref:`platform_atmelsam`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_dueUSB`
      - :ref:`platform_atmelsam`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_mzeroUSB`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mzeroproUSB`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrfox1200`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrgsm1400`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrnb1500`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrwan1300`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrwan1310`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrwifi1010`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkr1000USB`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrzero`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf52_nano33ble`
      - :ref:`platform_nordicnrf52`
      - NRF52840
      - 64MHz
      - 960KB
      - 256KB
    * - :ref:`board_atmelsam_tian`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_zeroUSB`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_black_f407ve`
      - :ref:`platform_ststm32`
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_black_f407vg`
      - :ref:`platform_ststm32`
      - STM32F407VGT6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_black_f407ze`
      - :ref:`platform_ststm32`
      - STM32F407ZET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_black_f407zg`
      - :ref:`platform_ststm32`
      - STM32F407ZGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_blackpill_f103c8`
      - :ref:`platform_ststm32`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_blackpill_f103c8_128`
      - :ref:`platform_ststm32`
      - STM32F103C8T6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_robotdyn_blackpill_f303cc`
      - :ref:`platform_ststm32`
      - STM32F303CCT6
      - 72MHz
      - 256KB
      - 40KB
    * - :ref:`board_ststm32_blackpill_f401cc`
      - :ref:`platform_ststm32`
      - STM32F401CCU6
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_blackpill_f401ce`
      - :ref:`platform_ststm32`
      - STM32F401CEU6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_blue_f407ve_mini`
      - :ref:`platform_ststm32`
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_bluepill_f103c6`
      - :ref:`platform_ststm32`
      - STM32F103C6T6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_bluepill_f103c8`
      - :ref:`platform_ststm32`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_bluepill_f103c8_128k`
      - :ref:`platform_ststm32`
      - STM32F103C8T6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_nordicnrf52_bluey`
      - :ref:`platform_nordicnrf52`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf51_bluz_dk`
      - :ref:`platform_nordicnrf51`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_espressif32_briki_abc_esp32`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 3.25MB
      - 320KB
    * - :ref:`board_atmelsam_briki_abc_samd21`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_espressif32_briki_mbc-wb_esp32`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 3.25MB
      - 320KB
    * - :ref:`board_atmelsam_briki_mbcwb_samd21`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_cicada_l082cz`
      - :ref:`platform_ststm32`
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_nordicnrf52_adafruit_cplaynrf52840`
      - :ref:`platform_nordicnrf52`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_ststm32_coreboard_f401rc`
      - :ref:`platform_ststm32`
      - STM32F401RCT6
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_cricket_l082cz`
      - :ref:`platform_ststm32`
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_espressif32_d-duino-32`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32doit-devkit-v1`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_ststm32_demo_f030f4`
      - :ref:`platform_ststm32`
      - STM32F030F4P6
      - 48MHz
      - 16KB
      - 4KB
    * - :ref:`board_atmelsam_digix`
      - :ref:`platform_atmelsam`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_espressif32_pocket_32`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_fm-devkit`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_pico32`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32vn-iot-uno`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_espectro32`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_espino32`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_ststm32_econode_l082cz`
      - :ref:`platform_ststm32`
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_electrosmith_daisy`
      - :ref:`platform_ststm32`
      - STM32H750IBK6
      - 400MHz
      - 512KB
      - 128KB
    * - :ref:`board_espressif32_esp32dev`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_ststm32_diymore_f407vgt`
      - :ref:`platform_ststm32`
      - STM32F407VGT6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_fk407m1`
      - :ref:`platform_ststm32`
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_fysetc_s6`
      - :ref:`platform_ststm32`
      - STM32F446VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_espressif32_firebeetle32`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_frogboard`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_gd32v_gd32vf103v-eval`
      - :ref:`platform_gd32v`
      - GD32VF103VBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_gnat_l082cz`
      - :ref:`platform_ststm32`
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_grasshopper_l082cz`
      - :ref:`platform_ststm32`
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_espressif32_heltec_wifi_lora_32`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wifi_lora_32_V2`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wireless_stick`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_hornbill32dev`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_hornbill32minima`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_iotaap_magnolia`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_nordicnrf52_adafruit_itsybitsy_nrf52840`
      - :ref:`platform_nordicnrf52`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_ststm32_malyanm200_f070cb`
      - :ref:`platform_ststm32`
      - STM32F070CBT6
      - 48MHz
      - 120KB
      - 14.81KB
    * - :ref:`board_ststm32_malyanm300_f070cb`
      - :ref:`platform_ststm32`
      - STM32F070CBT6
      - 48MHz
      - 120KB
      - 14.81KB
    * - :ref:`board_espressif32_mhetesp32devkit`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_mhetesp32minikit`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_ststm32_mkr_sharky`
      - :ref:`platform_ststm32`
      - STM32WB55CG
      - 64MHz
      - 512KB
      - 192.00KB
    * - :ref:`board_atmelsam_mkrvidor4000`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_malyanm200_f103cb`
      - :ref:`platform_ststm32`
      - STM32F103CBT6
      - 72MHz
      - 120KB
      - 20KB
    * - :ref:`board_ststm32_maple`
      - :ref:`platform_ststm32`
      - STM32F103RBT6
      - 72MHz
      - 108KB
      - 17KB
    * - :ref:`board_ststm32_maple_ret6`
      - :ref:`platform_ststm32`
      - STM32F103RET6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_maple_mini_b20`
      - :ref:`platform_ststm32`
      - STM32F103CBT6
      - 72MHz
      - 120KB
      - 20KB
    * - :ref:`board_ststm32_maple_mini_origin`
      - :ref:`platform_ststm32`
      - STM32F103CBT6
      - 72MHz
      - 108KB
      - 17KB
    * - :ref:`board_nordicnrf52_adafruit_metro_nrf52840`
      - :ref:`platform_nordicnrf52`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_ststm32_microduino32_flash`
      - :ref:`platform_ststm32`
      - STM32F103CBT6
      - 72MHz
      - 105.47KB
      - 16.60KB
    * - :ref:`board_atmelsam_minitronics20`
      - :ref:`platform_atmelsam`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_moteino_zero`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_netduino2plus`
      - :ref:`platform_ststm32`
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_atmelsam_nano_33_iot`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_espressif32_node32s`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_nodemcu-32s`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_ststm32_nucleo_g071rb`
      - :ref:`platform_ststm32`
      - STM32G071RBT6
      - 64MHz
      - 128KB
      - 36KB
    * - :ref:`board_ststm32_nucleo_g431kb`
      - :ref:`platform_ststm32`
      - STM32G431KBT6
      - 170MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_g431rb`
      - :ref:`platform_ststm32`
      - STM32G431RBT6
      - 170MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_g474re`
      - :ref:`platform_ststm32`
      - STM32G474RET6
      - 170MHz
      - 512KB
      - 128KB
    * - :ref:`board_espressif32_esp32-devkitlipo`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-evb`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-gateway`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_ststm32_olimexino`
      - :ref:`platform_ststm32`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_nordicnrf51_oshchip`
      - :ref:`platform_nordicnrf51`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_olimex_f103`
      - :ref:`platform_ststm32`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_olimex_p405`
      - :ref:`platform_ststm32`
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_ststm32_pybstick26_duino`
      - :ref:`platform_ststm32`
      - STM32F072RB
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_pybstick26_pro`
      - :ref:`platform_ststm32`
      - STM32F412RE
      - 100MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_pybstick26_lite`
      - :ref:`platform_ststm32`
      - STM32F401CEU6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_pybstick26_std`
      - :ref:`platform_ststm32`
      - STM32F411CEU6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_nordicnrf52_particle_xenon`
      - :ref:`platform_nordicnrf52`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_ststm32_piconomix_px_her0`
      - :ref:`platform_ststm32`
      - STM32L072RB
      - 32MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_prntr_v2`
      - :ref:`platform_ststm32`
      - STM32F407RE
      - 168MHz
      - 512KB
      - 192KB
    * - :ref:`board_espressif32_lopy`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lopy4`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB
    * - :ref:`board_ststm32_rak811_tracker`
      - :ref:`platform_ststm32`
      - STM32L151RBT6
      - 32MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_rak811_tracker_32`
      - :ref:`platform_ststm32`
      - STM32L151RBT6
      - 32MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_rhf76_052`
      - :ref:`platform_ststm32`
      - STM32L051C8T6
      - 32MHz
      - 64KB
      - 8KB
    * - :ref:`board_nordicnrf52_raytac_mdbt50q_rx`
      - :ref:`platform_nordicnrf52`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_espressif32_sg-o_airMon`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_atmelsam_sodaq_autonomo`
      - :ref:`platform_atmelsam`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_explorer`
      - :ref:`platform_atmelsam`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_one`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_sara`
      - :ref:`platform_atmelsam`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_sff`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_disco_g031j6`
      - :ref:`platform_ststm32`
      - STM32G031J6
      - 64MHz
      - 128KB
      - 8KB
    * - :ref:`board_ststm32_olimex_e407`
      - :ref:`platform_ststm32`
      - STM32F407ZGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_olimex_h407`
      - :ref:`platform_ststm32`
      - STM32F407ZGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F103C4`
      - :ref:`platform_ststm32`
      - STM32F103C4
      - 72MHz
      - 16KB
      - 6KB
    * - :ref:`board_ststm32_genericSTM32F103C6`
      - :ref:`platform_ststm32`
      - STM32F103C6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_genericSTM32F103C8`
      - :ref:`platform_ststm32`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103CB`
      - :ref:`platform_ststm32`
      - STM32F103CBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103R4`
      - :ref:`platform_ststm32`
      - STM32F103R4
      - 72MHz
      - 16KB
      - 6KB
    * - :ref:`board_ststm32_genericSTM32F103R6`
      - :ref:`platform_ststm32`
      - STM32F103R6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_genericSTM32F103R8`
      - :ref:`platform_ststm32`
      - STM32F103R8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103RB`
      - :ref:`platform_ststm32`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103RC`
      - :ref:`platform_ststm32`
      - STM32F103RCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_genericSTM32F103RD`
      - :ref:`platform_ststm32`
      - STM32F103RD
      - 72MHz
      - 384KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103RE`
      - :ref:`platform_ststm32`
      - STM32F103RET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103RF`
      - :ref:`platform_ststm32`
      - STM32F103RF
      - 72MHz
      - 768KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103RG`
      - :ref:`platform_ststm32`
      - STM32F103RG
      - 72MHz
      - 1MB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103T4`
      - :ref:`platform_ststm32`
      - STM32F103T4
      - 72MHz
      - 16KB
      - 6KB
    * - :ref:`board_ststm32_genericSTM32F103T6`
      - :ref:`platform_ststm32`
      - STM32F103T6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_genericSTM32F103T8`
      - :ref:`platform_ststm32`
      - STM32F103T8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103TB`
      - :ref:`platform_ststm32`
      - STM32F103TBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103V8`
      - :ref:`platform_ststm32`
      - STM32F103V8
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103VB`
      - :ref:`platform_ststm32`
      - STM32F103VBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103VC`
      - :ref:`platform_ststm32`
      - STM32F103VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_genericSTM32F103VD`
      - :ref:`platform_ststm32`
      - STM32F103VDT6
      - 72MHz
      - 384KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103VE`
      - :ref:`platform_ststm32`
      - STM32F103VET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103VF`
      - :ref:`platform_ststm32`
      - STM32F103VF
      - 72MHz
      - 768KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103VG`
      - :ref:`platform_ststm32`
      - STM32F103VG
      - 72MHz
      - 1MB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103ZC`
      - :ref:`platform_ststm32`
      - STM32F103ZCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_genericSTM32F103ZD`
      - :ref:`platform_ststm32`
      - STM32F103ZDT6
      - 72MHz
      - 384KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103ZE`
      - :ref:`platform_ststm32`
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103ZF`
      - :ref:`platform_ststm32`
      - STM32F103ZF
      - 72MHz
      - 768KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103ZG`
      - :ref:`platform_ststm32`
      - STM32F103ZG
      - 72MHz
      - 1MB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401CB`
      - :ref:`platform_ststm32`
      - STM32F401CB
      - 84MHz
      - 128KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401CC`
      - :ref:`platform_ststm32`
      - STM32F401CC
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401CD`
      - :ref:`platform_ststm32`
      - STM32F401CD
      - 84MHz
      - 384KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401CE`
      - :ref:`platform_ststm32`
      - STM32F401CE
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401RB`
      - :ref:`platform_ststm32`
      - STM32F401RB
      - 84MHz
      - 128KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401RC`
      - :ref:`platform_ststm32`
      - STM32F401RC
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401RD`
      - :ref:`platform_ststm32`
      - STM32F401RD
      - 84MHz
      - 384KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401RE`
      - :ref:`platform_ststm32`
      - STM32F401RE
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F405RG`
      - :ref:`platform_ststm32`
      - STM32F405RG
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F407VET6`
      - :ref:`platform_ststm32`
      - STM32F407VET6
      - 168MHz
      - 502.23KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F407VGT6`
      - :ref:`platform_ststm32`
      - STM32F407VGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_ststm32_genericSTM32F410C8`
      - :ref:`platform_ststm32`
      - STM32F410C8
      - 100MHz
      - 64KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F410CB`
      - :ref:`platform_ststm32`
      - STM32F410CB
      - 100MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F410R8`
      - :ref:`platform_ststm32`
      - STM32F410R8
      - 100MHz
      - 64KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F410RB`
      - :ref:`platform_ststm32`
      - STM32F410RB
      - 100MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F411CC`
      - :ref:`platform_ststm32`
      - STM32F411CC
      - 100MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F411CE`
      - :ref:`platform_ststm32`
      - STM32F411CE
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F411RC`
      - :ref:`platform_ststm32`
      - STM32F411RC
      - 100MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F411RE`
      - :ref:`platform_ststm32`
      - STM32F411RE
      - 100MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F412CE`
      - :ref:`platform_ststm32`
      - STM32F412CE
      - 100MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F412CG`
      - :ref:`platform_ststm32`
      - STM32F412CG
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F412RE`
      - :ref:`platform_ststm32`
      - STM32F412RE
      - 100MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F412RG`
      - :ref:`platform_ststm32`
      - STM32F412RG
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F413CG`
      - :ref:`platform_ststm32`
      - STM32F413CG
      - 100MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F413CH`
      - :ref:`platform_ststm32`
      - STM32F413CH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F413RG`
      - :ref:`platform_ststm32`
      - STM32F413RG
      - 100MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F413RH`
      - :ref:`platform_ststm32`
      - STM32F413RH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F415RG`
      - :ref:`platform_ststm32`
      - STM32F415RG
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F417VE`
      - :ref:`platform_ststm32`
      - STM32F417VE
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F417VG`
      - :ref:`platform_ststm32`
      - STM32F417VG
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F423CH`
      - :ref:`platform_ststm32`
      - STM32F423CH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F423RH`
      - :ref:`platform_ststm32`
      - STM32F423RH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F446RC`
      - :ref:`platform_ststm32`
      - STM32F446RC
      - 180MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F446RE`
      - :ref:`platform_ststm32`
      - STM32F446RE
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_stm32f4stamp`
      - :ref:`platform_ststm32`
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_atmelsam_sainSmartDue`
      - :ref:`platform_atmelsam`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_sainSmartDueUSB`
      - :ref:`platform_atmelsam`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_seeed_femto`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeeduino_lorawan`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeed_wio_lite_mg126`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeed_wio_terminal`
      - :ref:`platform_atmelsam`
      - SAMD51P19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_seeed_xiao`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeed_zero`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_steval_mksboxv1`
      - :ref:`platform_ststm32`
      - STM32L4R9ZI
      - 120MHz
      - 2MB
      - 640KB
    * - :ref:`board_espressif32_wesp32`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_nordicnrf51_Sinobit`
      - :ref:`platform_nordicnrf51`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_gd32v_sipeed-longan-nano`
      - :ref:`platform_gd32v`
      - GD32VF103CBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_gd32v_sipeed-longan-nano-lite`
      - :ref:`platform_gd32v`
      - GD32VF103C8T6
      - 108MHz
      - 64KB
      - 20KB
    * - :ref:`board_kendryte210_sipeed-maix-bit`
      - :ref:`platform_kendryte210`
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-maix-bit-mic`
      - :ref:`platform_kendryte210`
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-maix-go`
      - :ref:`platform_kendryte210`
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-maix-one-dock`
      - :ref:`platform_kendryte210`
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-maixduino`
      - :ref:`platform_kendryte210`
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_atmelsam_sparkfun_samd21_9dof`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_espressif32_esp32thing`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_sparkfun_lora_gateway_1-channel`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_atmelsam_sparkfun_qwiic_micro_samd21e`
      - :ref:`platform_atmelsam`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_redboard_turbo`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd21_dev_usb`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd21_mini_usb`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd21_proRF`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd51_thing_plus`
      - :ref:`platform_atmelsam`
      - SAMD51J20A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_ststm32_sparky_v1`
      - :ref:`platform_ststm32`
      - STM32F303CCT6
      - 72MHz
      - 256KB
      - 40KB
    * - :ref:`board_espressif32_ttgo-lora32-v1`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-lora32-v2`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-t-beam`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB
    * - :ref:`board_espressif32_ttgo-t1`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_nordicnrf52_stct_nrf52_minidev`
      - :ref:`platform_nordicnrf52`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_teensy_teensy31`
      - :ref:`platform_teensy`
      - MK20DX256
      - 72MHz
      - 256KB
      - 64KB
    * - :ref:`board_teensy_teensy35`
      - :ref:`platform_teensy`
      - MK64FX512
      - 120MHz
      - 512KB
      - 255.99KB
    * - :ref:`board_teensy_teensy36`
      - :ref:`platform_teensy`
      - MK66FX1M0
      - 180MHz
      - 1MB
      - 256KB
    * - :ref:`board_teensy_teensy40`
      - :ref:`platform_teensy`
      - IMXRT1062
      - 600MHz
      - 1.94MB
      - 512KB
    * - :ref:`board_teensy_teensy41`
      - :ref:`platform_teensy`
      - IMXRT1062
      - 600MHz
      - 7.75MB
      - 512KB
    * - :ref:`board_teensy_teensylc`
      - :ref:`platform_teensy`
      - MKL26Z64
      - 48MHz
      - 62KB
      - 8KB
    * - :ref:`board_ststm32_thunder_pack`
      - :ref:`platform_ststm32`
      - STM32L072KZ
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_thunder_pack_f411`
      - :ref:`platform_ststm32`
      - STM32F411CEU6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_hy_tinystm103tb`
      - :ref:`platform_ststm32`
      - STM32F103TBU6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_atmelsam_tuinozero96`
      - :ref:`platform_atmelsam`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_vake_v1`
      - :ref:`platform_ststm32`
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_vccgnd_f103zet6`
      - :ref:`platform_ststm32`
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_espressif32_vintlabs-devkit-v1`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_d32`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_d32_pro`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin32`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_nordicnrf51_waveshare_ble400`
      - :ref:`platform_nordicnrf51`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_waveshare_open103z`
      - :ref:`platform_ststm32`
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_blackpill_f411ce`
      - :ref:`platform_ststm32`
      - STM32F411CEU6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_espressif32_wemos_d1_mini32`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wemosbat`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_gd32v_wio_lite_risc-v`
      - :ref:`platform_gd32v`
      - GD32VF103CBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_wraith32_v1`
      - :ref:`platform_ststm32`
      - STM32F051K6
      - 48MHz
      - 32KB
      - 7.75KB
    * - :ref:`board_espressif32_xinabox_cw02`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_nordicnrf52_hackaBLE`
      - :ref:`platform_nordicnrf52`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf51_ng_beacon`
      - :ref:`platform_nordicnrf51`
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB
    * - :ref:`board_espressif32_iotbusio`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_iotbusproteus`
      - :ref:`platform_espressif32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB


Examples
--------

* `Arduino for ASR Microelectronics ASR650x <https://github.com/HelTecAutomation/platform-asrmicro650x/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for Atmel AVR <https://github.com/platformio/platform-atmelavr/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for Atmel megaAVR <https://github.com/platformio/platform-atmelmegaavr/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for Atmel SAM <https://github.com/platformio/platform-atmelsam/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for Espressif 32 <https://github.com/platformio/platform-espressif32/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for Espressif 8266 <https://github.com/platformio/platform-espressif8266/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for GigaDevice GD32V <https://github.com/sipeed/platform-gd32v/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for Infineon XMC <https://github.com/Infineon/platformio-infineonxmc/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for Intel ARC32 <https://github.com/platformio/platform-intel_arc32/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for Kendryte K210 <https://github.com/sipeed/platform-kendryte210/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for Microchip PIC32 <https://github.com/platformio/platform-microchippic32/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for Nordic nRF51 <https://github.com/platformio/platform-nordicnrf51/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for Nordic nRF52 <https://github.com/platformio/platform-nordicnrf52/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for ST STM32 <https://github.com/platformio/platform-ststm32/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for ST STM8 <https://github.com/platformio/platform-ststm8/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for Teensy <https://github.com/platformio/platform-teensy/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for TI MSP430 <https://github.com/platformio/platform-timsp430/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Arduino for TI TIVA <https://github.com/platformio/platform-titiva/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_asrmicro650x`
      - ASR Microelectronics ASR650x series is highly intergrated and ultra low power SoC based on the PSoC 4000 series MCU (ARM Cortex M0+ Core) and Semtech SX1262 transceiver.

    * - :ref:`platform_atmelavr`
      - Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

    * - :ref:`platform_atmelmegaavr`
      - 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

    * - :ref:`platform_atmelsam`
      - Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

    * - :ref:`platform_espressif32`
      - Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

    * - :ref:`platform_espressif8266`
      - Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

    * - :ref:`platform_gd32v`
      - The GigaDevice GD32V device is a 32-bit general-purpose microcontroller based on the RISC-V core with an impressive balance of processing power, reduced power consumption and peripheral set.

    * - :ref:`platform_infineonxmc`
      - Infineon has designed the XMC microcontrollers for real-time critical applications with an industry-standard core. The XMC microcontrollers can be integrated with the Arduino platform

    * - :ref:`platform_intel_arc32`
      - ARC embedded processors are a family of 32-bit CPUs that are widely used in SoC devices for storage, home, mobile, automotive, and Internet of Things applications.

    * - :ref:`platform_kendryte210`
      - Kendryte K210 is an AI capable RISCV64 dual core SoC.

    * - :ref:`platform_microchippic32`
      - Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

    * - :ref:`platform_nordicnrf51`
      - The Nordic nRF51 Series is a family of highly flexible, multi-protocol, system-on-chip (SoC) devices for ultra-low power wireless applications. nRF51 Series devices support a range of protocol stacks including Bluetooth Smart (previously called Bluetooth low energy), ANT and proprietary 2.4GHz protocols such as Gazell.

    * - :ref:`platform_nordicnrf52`
      - The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor and are the most capable Bluetooth Smart SoCs on the market.

    * - :ref:`platform_ststm32`
      - The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

    * - :ref:`platform_ststm8`
      - The STM8 is an 8-bit microcontroller family by STMicroelectronics an extended variant of the ST7 microcontroller architecture. STM8 microcontrollers are particularly low cost for a full-featured 8-bit microcontroller.

    * - :ref:`platform_teensy`
      - Teensy is a complete USB-based microcontroller development system, in a very small footprint, capable of implementing many types of projects. All programming is done via the USB port. No special programmer is needed, only a standard USB cable and a PC or Macintosh with a USB port.

    * - :ref:`platform_timsp430`
      - MSP430 microcontrollers (MCUs) from Texas Instruments (TI) are 16-bit, RISC-based, mixed-signal processors designed for ultra-low power. These MCUs offer the lowest power consumption and the perfect mix of integrated peripherals for thousands of applications.

    * - :ref:`platform_titiva`
      - Texas Instruments TM4C12x MCUs offer the industrys most popular ARM Cortex-M4 core with scalable memory and package options, unparalleled connectivity peripherals, advanced application functions, industry-leading analog integration, and extensive software solutions.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by horizontally.

4D Systems
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_picadillo_35t`
      - :ref:`platform_microchippic32`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB
    * - :ref:`board_espressif8266_gen4iod`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 512KB
      - 80KB

AI Thinker
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32cam`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

AZ-Delivery
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_az-delivery-devkit-v4`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 16MB
      - 520KB

Adafruit
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_adafruit_blm_badge`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelavr_bluefruitmicro`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52832`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_adafruit_clue_nrf52840`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_atmelavr_circuitplay_classic`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelsam_adafruit_circuitplayground_m0`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_crickit_m0`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_espressif32_featheresp32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
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
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52840_sense`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_atmelsam_adafruit_feather_m0`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_feather_m0_express`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_feather_m4_can`
      - :ref:`platform_atmelsam`
      - External
      - SAME51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_feather_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_ststm32_adafruit_feather_f405`
      - :ref:`platform_ststm32`
      - External
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52840`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
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
    * - :ref:`board_atmelsam_adafruit_gemma_m0`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_grandcentral_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51P20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_espressif8266_huzzah`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_atmelsam_adafruit_hallowing`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_hallowing_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
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
    * - :ref:`board_atmelsam_adafruit_itsybitsy_m0`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_itsybitsy_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51G19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_monster_m4sk`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51G19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_matrix_portal_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelavr_metro`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelsam_adafruit_metro_m0`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_metro_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_metro_m4_airliftlite`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
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
    * - :ref:`board_atmelsam_adafruit_pygamer_advance_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_pygamer_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_pyportal_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_pyportal_m4_titano`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_qt_py_m0`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_trellis_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
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
    * - :ref:`board_atmelsam_adafruit_trinket_m0`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_pirkey`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_pybadge_airlift_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J20A
      - 120MHz
      - 1008KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_pybadge_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_nordicnrf52_adafruit_cplaynrf52840`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_itsybitsy_nrf52840`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_metro_nrf52840`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB

AfroFlight
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_afroflight_f103cb`
      - :ref:`platform_ststm32`
      - External
      - STM32F103CBT6
      - 72MHz
      - 128KB
      - 20KB

Airbot
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_wraith32_v1`
      - :ref:`platform_ststm32`
      - External
      - STM32F051K6
      - 48MHz
      - 32KB
      - 7.75KB

Aiyarafun
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_node32s`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Alorium Technology
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
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

Amperka
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_wifi_slot`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

Anarduino
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_miniwireless`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

April Brother
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_espea32`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Arduboy
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
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

Arduino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
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
    * - :ref:`board_atmelsam_due`
      - :ref:`platform_atmelsam`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_dueUSB`
      - :ref:`platform_atmelsam`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
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
    * - :ref:`board_atmelsam_mzeroUSB`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mzeroproUSB`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mzeropro`
      - :ref:`platform_atmelsam`
      - On-board
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrfox1200`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrgsm1400`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrnb1500`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrwan1300`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrwan1310`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrwifi1010`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkr1000USB`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrzero`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
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
    * - :ref:`board_nordicnrf52_nano33ble`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 960KB
      - 256KB
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
    * - :ref:`board_atmelmegaavr_nano_every`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATMEGA4809
      - 16MHz
      - 47.50KB
      - 6KB
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
    * - :ref:`board_atmelsam_tian`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelavr_uno`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelmegaavr_uno_wifi_rev2`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATMEGA4809
      - 16MHz
      - 47.50KB
      - 6KB
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
    * - :ref:`board_atmelsam_zero`
      - :ref:`platform_atmelsam`
      - On-board
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_zeroUSB`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrvidor4000`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_nano_33_iot`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

Armed
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_armed_v1`
      - :ref:`platform_ststm32`
      - External
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB

Atmel
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_samd21g18a`
      - :ref:`platform_atmelsam`
      - On-board
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelavr_attiny1634`
      - :ref:`platform_atmelavr`
      - No
      - ATTINY1634
      - 8MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_attiny167`
      - :ref:`platform_atmelavr`
      - No
      - ATTINY167
      - 8MHz
      - 16KB
      - 512B
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
    * - :ref:`board_atmelavr_attiny261`
      - :ref:`platform_atmelavr`
      - No
      - ATTINY261
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
    * - :ref:`board_atmelavr_attiny43`
      - :ref:`platform_atmelavr`
      - No
      - ATTINY43U
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
    * - :ref:`board_atmelavr_attiny441`
      - :ref:`platform_atmelavr`
      - No
      - ATTINY441
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
    * - :ref:`board_atmelavr_attiny461`
      - :ref:`platform_atmelavr`
      - No
      - ATTINY461
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny48`
      - :ref:`platform_atmelavr`
      - No
      - ATTINY48
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny828`
      - :ref:`platform_atmelavr`
      - No
      - ATTINY828
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_attiny84`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY84
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_attiny841`
      - :ref:`platform_atmelavr`
      - No
      - ATTINY841
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
    * - :ref:`board_atmelavr_attiny861`
      - :ref:`platform_atmelavr`
      - No
      - ATTINY861
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_attiny87`
      - :ref:`platform_atmelavr`
      - No
      - ATTINY87
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_attiny88`
      - :ref:`platform_atmelavr`
      - No
      - ATTINY88
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_usbasp`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA8
      - 12MHz
      - 8KB
      - 1KB

BBC
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_bbcmicrobit`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf52_bbcmicrobit_v2`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52833
      - 64MHz
      - 512KB
      - 64KB

BOXTEC
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_helvepic32`
      - :ref:`platform_microchippic32`
      - No
      - 32MX250F128B
      - 48MHz
      - 120KB
      - 32KB
    * - :ref:`board_microchippic32_helvepic32_breadboardside`
      - :ref:`platform_microchippic32`
      - No
      - 32MX250F128B
      - 48MHz
      - 120KB
      - 32KB
    * - :ref:`board_microchippic32_helvepic32_smd`
      - :ref:`platform_microchippic32`
      - No
      - 32MX250F128D
      - 48MHz
      - 120KB
      - 32KB
    * - :ref:`board_microchippic32_helvepic32_mx270`
      - :ref:`platform_microchippic32`
      - No
      - 32MX270F256B
      - 48MHz
      - 244KB
      - 62KB
    * - :ref:`board_microchippic32_helvepic32_robot`
      - :ref:`platform_microchippic32`
      - No
      - 32MX270F256D
      - 48MHz
      - 244KB
      - 62KB
    * - :ref:`board_microchippic32_helvepic32_smd_mx270`
      - :ref:`platform_microchippic32`
      - No
      - 32MX270F256D
      - 48MHz
      - 244KB
      - 62KB

BPI Tech
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_bpi-bit`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 160MHz
      - 4MB
      - 320KB

BQ
~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_zumbt328`
      - :ref:`platform_atmelavr`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_lora32u4II`
      - :ref:`platform_atmelavr`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_raspduino`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB

BluzDK
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_bluz_dk`
      - :ref:`platform_nordicnrf51`
      - External
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

Calliope
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_calliope_mini`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

ChipKIT
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_rgb_station`
      - :ref:`platform_microchippic32`
      - No
      - 32MX270F256D
      - 48MHz
      - 240KB
      - 62KB

Controllino
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
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

DFRobot
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_firebeetle32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

DOIT
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32doit-devkit-v1`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

DSTIKE
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_d-duino-32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Delta
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_delta_dfbm_nq620`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

DigiStump
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_oak`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

Digilent
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_cerebot32mx4`
      - :ref:`platform_microchippic32`
      - No
      - 32MX460F512L
      - 80MHz
      - 508KB
      - 32KB
    * - :ref:`board_microchippic32_cerebot32mx7`
      - :ref:`platform_microchippic32`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB
    * - :ref:`board_microchippic32_openscope`
      - :ref:`platform_microchippic32`
      - No
      - 32MZ2048EFG124
      - 200MHz
      - 1.98MB
      - 512KB
    * - :ref:`board_microchippic32_chipkit_cmod`
      - :ref:`platform_microchippic32`
      - No
      - 32MX150F128D
      - 40MHz
      - 124KB
      - 32KB
    * - :ref:`board_microchippic32_chipkit_dp32`
      - :ref:`platform_microchippic32`
      - No
      - 32MX250F128B
      - 40MHz
      - 120KB
      - 32KB
    * - :ref:`board_microchippic32_mega_pic32`
      - :ref:`platform_microchippic32`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB
    * - :ref:`board_microchippic32_chipkit_mx3`
      - :ref:`platform_microchippic32`
      - No
      - 32MX320F128H
      - 80MHz
      - 124KB
      - 16KB
    * - :ref:`board_microchippic32_chipkit_pro_mx4`
      - :ref:`platform_microchippic32`
      - No
      - 32MX460F512L
      - 80MHz
      - 508KB
      - 32KB
    * - :ref:`board_microchippic32_chipkit_pro_mx7`
      - :ref:`platform_microchippic32`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB
    * - :ref:`board_microchippic32_uno_pic32`
      - :ref:`platform_microchippic32`
      - No
      - 32MX320F128H
      - 80MHz
      - 124KB
      - 16KB
    * - :ref:`board_microchippic32_chipkit_wf32`
      - :ref:`platform_microchippic32`
      - No
      - 32MX695F512L
      - 80MHz
      - 508KB
      - 128KB
    * - :ref:`board_microchippic32_chipkit_wifire`
      - :ref:`platform_microchippic32`
      - No
      - 32MZ2048ECG100
      - 200MHz
      - 1.98MB
      - 512KB
    * - :ref:`board_microchippic32_chipkit_uc32`
      - :ref:`platform_microchippic32`
      - No
      - 32MX340F512H
      - 80MHz
      - 508KB
      - 32KB
    * - :ref:`board_microchippic32_chipkit_wifire_revc`
      - :ref:`platform_microchippic32`
      - No
      - 32MZ2048EFG100
      - 200MHz
      - 1.98MB
      - 512KB

Digistump
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_digispark-pro`
      - :ref:`platform_atmelavr`
      - No
      - ATTINY167
      - 16MHz
      - 14.50KB
      - 512B
    * - :ref:`board_atmelavr_digispark-pro64`
      - :ref:`platform_atmelavr`
      - No
      - ATTINY167
      - 16MHz
      - 14.50KB
      - 512B
    * - :ref:`board_atmelavr_digispark-pro32`
      - :ref:`platform_atmelavr`
      - No
      - ATTINY167
      - 16MHz
      - 14.50KB
      - 512B
    * - :ref:`board_atmelavr_digispark-tiny`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY85
      - 16MHz
      - 5.87KB
      - 512B
    * - :ref:`board_atmelsam_digix`
      - :ref:`platform_atmelsam`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB

Diymore
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_diymore_f407vgt`
      - :ref:`platform_ststm32`
      - External
      - STM32F407VGT6
      - 168MHz
      - 512KB
      - 128KB

Doit
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_espmxdevkit`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_espduino`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

Dongsen Technology
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_pocket_32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Dwengo
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_dwenguino`
      - :ref:`platform_atmelavr`
      - No
      - AT90USB646
      - 16MHz
      - 60KB
      - 2KB

DycodeX
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_espectro`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif32_espectro32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

ESP32vn
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32vn-iot-uno`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

ESPert
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_espresso_lite_v1`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_espresso_lite_v2`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

ESPino
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_espino`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

Econode
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_econode_l082cz`
      - :ref:`platform_ststm32`
      - External
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB

Electronic SweetPeas
~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp320`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Electronut Labs
~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_bluey`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_hackaBLE`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

Electrosmith
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_electrosmith_daisy`
      - :ref:`platform_ststm32`
      - External
      - STM32H750IBK6
      - 400MHz
      - 512KB
      - 128KB

Elektor
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_elektor_uno_r4`
      - :ref:`platform_atmelavr`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_engduinov3`
      - :ref:`platform_atmelavr`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_mayfly`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB

Espressif
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_esp_wroom_02`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 2MB
      - 80KB
    * - :ref:`board_espressif32_pico32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp-wrover-kit`
      - :ref:`platform_espressif32`
      - On-board
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32dev`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif8266_esp12e`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_esp01_1m`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_esp01`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 512KB
      - 80KB
    * - :ref:`board_espressif8266_esp07`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_esp07s`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_esp8285`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_phoenix_v1`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_phoenix_v2`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_wifinfo`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB

FYSETC
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_fysetc_f6_13`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB
    * - :ref:`board_ststm32_fysetc_s6`
      - :ref:`platform_ststm32`
      - External
      - STM32F446VET6
      - 168MHz
      - 512KB
      - 128KB

Fred
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_frogboard`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Fubarino
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_fubarino_mini`
      - :ref:`platform_microchippic32`
      - No
      - 32MX250F128D
      - 48MHz
      - 120KB
      - 32KB
    * - :ref:`board_microchippic32_fubarino_sd`
      - :ref:`platform_microchippic32`
      - No
      - 32MX795F512H
      - 80MHz
      - 508KB
      - 128KB
    * - :ref:`board_microchippic32_fubarino_mini_20`
      - :ref:`platform_microchippic32`
      - No
      - 32MX270F256D
      - 48MHz
      - 240KB
      - 62KB

Generic
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_blackpill_f103c8`
      - :ref:`platform_ststm32`
      - External
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_blackpill_f103c8_128`
      - :ref:`platform_ststm32`
      - External
      - STM32F103C8T6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_bluepill_f103c6`
      - :ref:`platform_ststm32`
      - External
      - STM32F103C6T6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_bluepill_f103c8`
      - :ref:`platform_ststm32`
      - External
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_bluepill_f103c8_128k`
      - :ref:`platform_ststm32`
      - External
      - STM32F103C8T6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_demo_f030f4`
      - :ref:`platform_ststm32`
      - External
      - STM32F030F4P6
      - 48MHz
      - 16KB
      - 4KB
    * - :ref:`board_ststm32_fk407m1`
      - :ref:`platform_ststm32`
      - External
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F103C4`
      - :ref:`platform_ststm32`
      - External
      - STM32F103C4
      - 72MHz
      - 16KB
      - 6KB
    * - :ref:`board_ststm32_genericSTM32F103C6`
      - :ref:`platform_ststm32`
      - External
      - STM32F103C6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_genericSTM32F103C8`
      - :ref:`platform_ststm32`
      - External
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103CB`
      - :ref:`platform_ststm32`
      - External
      - STM32F103CBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103R4`
      - :ref:`platform_ststm32`
      - External
      - STM32F103R4
      - 72MHz
      - 16KB
      - 6KB
    * - :ref:`board_ststm32_genericSTM32F103R6`
      - :ref:`platform_ststm32`
      - External
      - STM32F103R6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_genericSTM32F103R8`
      - :ref:`platform_ststm32`
      - External
      - STM32F103R8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103RB`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103RC`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_genericSTM32F103RD`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RD
      - 72MHz
      - 384KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103RE`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103RF`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RF
      - 72MHz
      - 768KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103RG`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RG
      - 72MHz
      - 1MB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103T4`
      - :ref:`platform_ststm32`
      - External
      - STM32F103T4
      - 72MHz
      - 16KB
      - 6KB
    * - :ref:`board_ststm32_genericSTM32F103T6`
      - :ref:`platform_ststm32`
      - External
      - STM32F103T6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_genericSTM32F103T8`
      - :ref:`platform_ststm32`
      - External
      - STM32F103T8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103TB`
      - :ref:`platform_ststm32`
      - External
      - STM32F103TBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103V8`
      - :ref:`platform_ststm32`
      - External
      - STM32F103V8
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103VB`
      - :ref:`platform_ststm32`
      - External
      - STM32F103VBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103VC`
      - :ref:`platform_ststm32`
      - External
      - STM32F103VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_genericSTM32F103VD`
      - :ref:`platform_ststm32`
      - External
      - STM32F103VDT6
      - 72MHz
      - 384KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103VE`
      - :ref:`platform_ststm32`
      - External
      - STM32F103VET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103VF`
      - :ref:`platform_ststm32`
      - External
      - STM32F103VF
      - 72MHz
      - 768KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103VG`
      - :ref:`platform_ststm32`
      - External
      - STM32F103VG
      - 72MHz
      - 1MB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103ZC`
      - :ref:`platform_ststm32`
      - External
      - STM32F103ZCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_genericSTM32F103ZD`
      - :ref:`platform_ststm32`
      - External
      - STM32F103ZDT6
      - 72MHz
      - 384KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103ZE`
      - :ref:`platform_ststm32`
      - External
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103ZF`
      - :ref:`platform_ststm32`
      - External
      - STM32F103ZF
      - 72MHz
      - 768KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103ZG`
      - :ref:`platform_ststm32`
      - External
      - STM32F103ZG
      - 72MHz
      - 1MB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401CB`
      - :ref:`platform_ststm32`
      - External
      - STM32F401CB
      - 84MHz
      - 128KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401CC`
      - :ref:`platform_ststm32`
      - External
      - STM32F401CC
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401CD`
      - :ref:`platform_ststm32`
      - External
      - STM32F401CD
      - 84MHz
      - 384KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401CE`
      - :ref:`platform_ststm32`
      - External
      - STM32F401CE
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401RB`
      - :ref:`platform_ststm32`
      - External
      - STM32F401RB
      - 84MHz
      - 128KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401RC`
      - :ref:`platform_ststm32`
      - External
      - STM32F401RC
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401RD`
      - :ref:`platform_ststm32`
      - External
      - STM32F401RD
      - 84MHz
      - 384KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401RE`
      - :ref:`platform_ststm32`
      - External
      - STM32F401RE
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F405RG`
      - :ref:`platform_ststm32`
      - External
      - STM32F405RG
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F407VET6`
      - :ref:`platform_ststm32`
      - External
      - STM32F407VET6
      - 168MHz
      - 502.23KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F407VGT6`
      - :ref:`platform_ststm32`
      - External
      - STM32F407VGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_ststm32_genericSTM32F410C8`
      - :ref:`platform_ststm32`
      - External
      - STM32F410C8
      - 100MHz
      - 64KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F410CB`
      - :ref:`platform_ststm32`
      - External
      - STM32F410CB
      - 100MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F410R8`
      - :ref:`platform_ststm32`
      - External
      - STM32F410R8
      - 100MHz
      - 64KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F410RB`
      - :ref:`platform_ststm32`
      - External
      - STM32F410RB
      - 100MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F411CC`
      - :ref:`platform_ststm32`
      - External
      - STM32F411CC
      - 100MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F411CE`
      - :ref:`platform_ststm32`
      - External
      - STM32F411CE
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F411RC`
      - :ref:`platform_ststm32`
      - External
      - STM32F411RC
      - 100MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F411RE`
      - :ref:`platform_ststm32`
      - External
      - STM32F411RE
      - 100MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F412CE`
      - :ref:`platform_ststm32`
      - External
      - STM32F412CE
      - 100MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F412CG`
      - :ref:`platform_ststm32`
      - External
      - STM32F412CG
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F412RE`
      - :ref:`platform_ststm32`
      - External
      - STM32F412RE
      - 100MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F412RG`
      - :ref:`platform_ststm32`
      - External
      - STM32F412RG
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F413CG`
      - :ref:`platform_ststm32`
      - External
      - STM32F413CG
      - 100MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F413CH`
      - :ref:`platform_ststm32`
      - External
      - STM32F413CH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F413RG`
      - :ref:`platform_ststm32`
      - External
      - STM32F413RG
      - 100MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F413RH`
      - :ref:`platform_ststm32`
      - External
      - STM32F413RH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F415RG`
      - :ref:`platform_ststm32`
      - External
      - STM32F415RG
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F417VE`
      - :ref:`platform_ststm32`
      - External
      - STM32F417VE
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F417VG`
      - :ref:`platform_ststm32`
      - External
      - STM32F417VG
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F423CH`
      - :ref:`platform_ststm32`
      - External
      - STM32F423CH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F423RH`
      - :ref:`platform_ststm32`
      - External
      - STM32F423RH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F446RC`
      - :ref:`platform_ststm32`
      - External
      - STM32F446RC
      - 180MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F446RE`
      - :ref:`platform_ststm32`
      - External
      - STM32F446RE
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_stm32f4stamp`
      - :ref:`platform_ststm32`
      - External
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 192KB

Gimasi
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_tuinozero96`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

HY
~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_hy_tinystm103tb`
      - :ref:`platform_ststm32`
      - External
      - STM32F103TBU6
      - 72MHz
      - 128KB
      - 20KB

Hardkernel
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_odroid_esp32`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

Heltec
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_asrmicro650x_cubecell_capsule_solar_sensor`
      - :ref:`platform_asrmicro650x`
      - No
      - ASR6502
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_asrmicro650x_cubecell_node`
      - :ref:`platform_asrmicro650x`
      - No
      - ASR6502
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_asrmicro650x_cubecell_board`
      - :ref:`platform_asrmicro650x`
      - No
      - ASR6501
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_asrmicro650x_cubecell_board_plus`
      - :ref:`platform_asrmicro650x`
      - No
      - ASR6502
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_asrmicro650x_cubecell_capsule`
      - :ref:`platform_asrmicro650x`
      - No
      - ASR6501
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_asrmicro650x_cubecell_gps`
      - :ref:`platform_asrmicro650x`
      - No
      - ASR6502
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_asrmicro650x_cubecell_module`
      - :ref:`platform_asrmicro650x`
      - No
      - ASR6501
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_asrmicro650x_cubecell_module_plus`
      - :ref:`platform_asrmicro650x`
      - No
      - ASR6502
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_espressif8266_heltec_wifi_kit_8`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

Heltec Automation
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_heltec_wifi_kit_32`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wifi_lora_32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wifi_lora_32_V2`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wireless_stick`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 8MB
      - 320KB

Hornbill
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_hornbill32dev`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_hornbill32minima`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

ITEAD
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_sonoff_basic`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_sonoff_s20`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_sonoff_sv`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_sonoff_th`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB

Infineon
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_infineonxmc_xmc1100_boot_kit`
      - :ref:`platform_infineonxmc`
      - On-board
      - XMC1100
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1100_h_bridge2go`
      - :ref:`platform_infineonxmc`
      - On-board
      - XMC1100
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1100_xmc2go`
      - :ref:`platform_infineonxmc`
      - On-board
      - XMC1100
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1300_boot_kit`
      - :ref:`platform_infineonxmc`
      - On-board
      - XMC1300
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1300_sense2gol`
      - :ref:`platform_infineonxmc`
      - On-board
      - XMC1300
      - 32MHz
      - 32KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1400_boot_kit`
      - :ref:`platform_infineonxmc`
      - On-board
      - XMC1400
      - 48MHz
      - 1.95MB
      - 16KB
    * - :ref:`board_infineonxmc_xmc4200_distance2go`
      - :ref:`platform_infineonxmc`
      - On-board
      - XMC4200
      - 80MHz
      - 256KB
      - 40KB
    * - :ref:`board_infineonxmc_xmc4700_relax_kit`
      - :ref:`platform_infineonxmc`
      - On-board
      - XMC4700
      - 144MHz
      - 2.00MB
      - 1.95MB

Intel
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_intel_arc32_genuino101`
      - :ref:`platform_intel_arc32`
      - No
      - ARCV2EM
      - 32MHz
      - 152KB
      - 80KB

IntoRobot
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_intorobot`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Invent One
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_inventone`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

IoTaaP
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_iotaap_magnolia`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

LeafLabs
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_maple`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RBT6
      - 72MHz
      - 108KB
      - 17KB
    * - :ref:`board_ststm32_maple_ret6`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RET6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_maple_mini_b20`
      - :ref:`platform_ststm32`
      - External
      - STM32F103CBT6
      - 72MHz
      - 120KB
      - 20KB
    * - :ref:`board_ststm32_maple_mini_origin`
      - :ref:`platform_ststm32`
      - External
      - STM32F103CBT6
      - 72MHz
      - 108KB
      - 17KB

LightUp
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_lightup`
      - :ref:`platform_atmelavr`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_one`
      - :ref:`platform_atmelavr`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_current_ranger`
      - :ref:`platform_atmelsam`
      - No
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
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
    * - :ref:`board_atmelsam_moteino_zero`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

M5Stack
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_m5stack-core-esp32`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_m5stack-fire`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 6.25MB
    * - :ref:`board_espressif32_m5stack-grey`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 520KB
    * - :ref:`board_espressif32_m5stick-c`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

MH-ET Live
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_mhetesp32devkit`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_mhetesp32minikit`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

MXChip
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_mxchip_az3166`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB

Magicblocks.io
~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_magicbit`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

MakerAsia
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_nano32`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Makerology
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_dsmini`
      - :ref:`platform_microchippic32`
      - No
      - 32MX150F128C
      - 40MHz
      - 120KB
      - 32KB

Malyan
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_malyanm200_f070cb`
      - :ref:`platform_ststm32`
      - External
      - STM32F070CBT6
      - 48MHz
      - 120KB
      - 14.81KB
    * - :ref:`board_ststm32_malyanm300_f070cb`
      - :ref:`platform_ststm32`
      - External
      - STM32F070CBT6
      - 48MHz
      - 120KB
      - 14.81KB
    * - :ref:`board_ststm32_malyanm200_f103cb`
      - :ref:`platform_ststm32`
      - External
      - STM32F103CBT6
      - 72MHz
      - 120KB
      - 20KB

MediaTek Labs
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_smart7688`
      - :ref:`platform_atmelavr`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_AT90CAN128`
      - :ref:`platform_atmelavr`
      - No
      - AT90CAN128
      - 16MHz
      - 128KB
      - 4KB
    * - :ref:`board_atmelavr_AT90CAN32`
      - :ref:`platform_atmelavr`
      - No
      - AT90CAN32
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_AT90CAN64`
      - :ref:`platform_atmelavr`
      - No
      - AT90CAN64
      - 16MHz
      - 64KB
      - 4KB
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
    * - :ref:`board_atmelmegaavr_ATmega1608`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATMEGA1608
      - 16MHz
      - 16KB
      - 2KB
    * - :ref:`board_atmelmegaavr_ATmega1609`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATMEGA1609
      - 16MHz
      - 16KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega162`
      - :ref:`platform_atmelavr`
      - No
      - ATMEGA162
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega164A`
      - :ref:`platform_atmelavr`
      - No
      - ATMEGA164A
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
    * - :ref:`board_atmelavr_ATmega168PB`
      - :ref:`platform_atmelavr`
      - No
      - ATMEGA168PB
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
    * - :ref:`board_atmelavr_ATmega2561`
      - :ref:`platform_atmelavr`
      - No
      - ATMEGA2561
      - 16MHz
      - 256KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega32`
      - :ref:`platform_atmelavr`
      - No
      - ATMEGA32
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelmegaavr_ATmega3208`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATMEGA3208
      - 16MHz
      - 32KB
      - 4KB
    * - :ref:`board_atmelmegaavr_ATmega3209`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATMEGA3209
      - 16MHz
      - 32KB
      - 4KB
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
    * - :ref:`board_atmelavr_ATmega324PB`
      - :ref:`platform_atmelavr`
      - No
      - ATMEGA324PB
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
    * - :ref:`board_atmelavr_ATmega328PB`
      - :ref:`platform_atmelavr`
      - No
      - ATMEGA328PB
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
    * - :ref:`board_atmelmegaavr_ATmega4808`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATMEGA4808
      - 16MHz
      - 48KB
      - 6KB
    * - :ref:`board_atmelmegaavr_ATmega4809`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATMEGA4809
      - 16MHz
      - 48KB
      - 6KB
    * - :ref:`board_atmelavr_ATmega48P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA48P
      - 16MHz
      - 4KB
      - 512B
    * - :ref:`board_atmelavr_ATmega48PB`
      - :ref:`platform_atmelavr`
      - No
      - ATMEGA48PB
      - 16MHz
      - 4KB
      - 512B
    * - :ref:`board_atmelavr_ATmega64`
      - :ref:`platform_atmelavr`
      - No
      - ATMEGA64
      - 16MHz
      - 64KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega640`
      - :ref:`platform_atmelavr`
      - No
      - ATMEGA640
      - 16MHz
      - 64KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega644A`
      - :ref:`platform_atmelavr`
      - No
      - ATMEGA644A
      - 16MHz
      - 64KB
      - 4KB
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
    * - :ref:`board_atmelmegaavr_ATmega808`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATMEGA808
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelmegaavr_ATmega809`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATMEGA809
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega8515`
      - :ref:`platform_atmelavr`
      - No
      - ATMEGA8515
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_ATmega8535`
      - :ref:`platform_atmelavr`
      - No
      - ATMEGA8535
      - 16MHz
      - 8KB
      - 512B
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
    * - :ref:`board_atmelavr_ATmega88PB`
      - :ref:`platform_atmelavr`
      - No
      - ATMEGA88PB
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
    * - :ref:`board_atmelmegaavr_ATtiny1604`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY1604
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelmegaavr_ATtiny1606`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY1606
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelmegaavr_ATtiny1607`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY1607
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelmegaavr_ATtiny1614`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY1614
      - 16MHz
      - 16KB
      - 2KB
    * - :ref:`board_atmelmegaavr_ATtiny1616`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY1616
      - 16MHz
      - 16KB
      - 2KB
    * - :ref:`board_atmelmegaavr_ATtiny1617`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY1617
      - 16MHz
      - 16KB
      - 2KB
    * - :ref:`board_atmelmegaavr_ATtiny202`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY202
      - 16MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelmegaavr_ATtiny204`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY204
      - 16MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelmegaavr_ATtiny212`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY212
      - 16MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelmegaavr_ATtiny214`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY214
      - 16MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelmegaavr_ATtiny3216`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY3216
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelmegaavr_ATtiny3217`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY3217
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelmegaavr_ATtiny402`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY402
      - 16MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelmegaavr_ATtiny404`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY404
      - 16MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelmegaavr_ATtiny406`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY406
      - 16MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelmegaavr_ATtiny412`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY412
      - 16MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelmegaavr_ATtiny414`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY414
      - 16MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelmegaavr_ATtiny416`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY416
      - 16MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelmegaavr_ATtiny417`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY417
      - 16MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelmegaavr_ATtiny804`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY804
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelmegaavr_ATtiny806`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY806
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelmegaavr_ATtiny807`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY807
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelmegaavr_ATtiny814`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY814
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelmegaavr_ATtiny816`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY816
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelmegaavr_ATtiny817`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATTINY817
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelmegaavr_avr_iot_wg`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATMEGA4808
      - 16MHz
      - 48KB
      - 6KB
    * - :ref:`board_atmelmegaavr_curiosity_nano_4809`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATMEGA4809
      - 16MHz
      - 48KB
      - 6KB
    * - :ref:`board_atmelmegaavr_xplained_pro_4809`
      - :ref:`platform_atmelmegaavr`
      - No
      - ATMEGA4809
      - 16MHz
      - 48KB
      - 6KB

Microduino
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
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
    * - :ref:`board_espressif32_microduino-core-esp32`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_ststm32_microduino32_flash`
      - :ref:`platform_ststm32`
      - External
      - STM32F103CBT6
      - 72MHz
      - 105.47KB
      - 16.60KB
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

Midatronics
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_mkr_sharky`
      - :ref:`platform_ststm32`
      - External
      - STM32WB55CG
      - 64MHz
      - 512KB
      - 192.00KB

MikroElektronika
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_clicker2`
      - :ref:`platform_microchippic32`
      - No
      - 32MX460F512L
      - 80MHz
      - 508KB
      - 32KB
    * - :ref:`board_microchippic32_flipnclickmz`
      - :ref:`platform_microchippic32`
      - No
      - 32MZ2048EFH100
      - 252MHz
      - 1.98MB
      - 512KB

Netduino
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_netduino2plus`
      - :ref:`platform_ststm32`
      - External
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 192KB

NodeMCU
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_nodemcu`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_nodemcuv2`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif32_nodemcu-32s`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Noduino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_quantum`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

Nordic
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_nrf51_beacon`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_nrf51_dongle`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_nrf51_dk`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf52_nrf52_dk`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52840_dk`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_nrf52840_dk_adafruit`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB

OLIMEX
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32-devkitlipo`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-evb`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-gateway`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-pro`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-poe`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-poe-iso`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

OROCA
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_oroca_edubot`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

OSHChip
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_oshchip`
      - :ref:`platform_nordicnrf51`
      - External
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

Olimex
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_olimexino`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_espressif8266_modwifi`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 2MB
      - 80KB
    * - :ref:`board_microchippic32_pinguino32`
      - :ref:`platform_microchippic32`
      - No
      - 32MX440F256H
      - 80MHz
      - 252KB
      - 32KB
    * - :ref:`board_ststm32_olimex_f103`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_olimex_p405`
      - :ref:`platform_ststm32`
      - External
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_ststm32_olimex_e407`
      - :ref:`platform_ststm32`
      - External
      - STM32F407ZGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_olimex_h407`
      - :ref:`platform_ststm32`
      - External
      - STM32F407ZGT6
      - 168MHz
      - 1MB
      - 128KB

Onehorse
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_onehorse32dev`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

OpenBCI
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_openbci`
      - :ref:`platform_microchippic32`
      - No
      - 32MX250F128B
      - 40MHz
      - 120KB
      - 32KB

OpenEnergyMonitor
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_emonpi`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB

PONTECH
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_usbono_pic32`
      - :ref:`platform_microchippic32`
      - No
      - 32MX440F512H
      - 80MHz
      - 508KB
      - 32KB

PYBStick
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_pybstick26_duino`
      - :ref:`platform_ststm32`
      - External
      - STM32F072RB
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_pybstick26_pro`
      - :ref:`platform_ststm32`
      - External
      - STM32F412RE
      - 100MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_pybstick26_lite`
      - :ref:`platform_ststm32`
      - External
      - STM32F401CEU6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_pybstick26_std`
      - :ref:`platform_ststm32`
      - External
      - STM32F411CEU6
      - 100MHz
      - 512KB
      - 128KB

PanStamp
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_panStampAVR`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB

Particle
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_particle_xenon`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB

Piconomix
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_piconomix_px_her0`
      - :ref:`platform_ststm32`
      - External
      - STM32L072RB
      - 32MHz
      - 128KB
      - 20KB

Pinoccio
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_pinoccio`
      - :ref:`platform_atmelavr`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_a-star32U4`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

Pontech
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_nofire`
      - :ref:`platform_microchippic32`
      - No
      - 32MZ2048EFG100
      - 200MHz
      - 1.98MB
      - 512KB
    * - :ref:`board_microchippic32_quick240_usb`
      - :ref:`platform_microchippic32`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB

PrntrBoard
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_prntr_v2`
      - :ref:`platform_ststm32`
      - External
      - STM32F407RE
      - 168MHz
      - 512KB
      - 192KB

Prusa 3D
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_prusa_mm_control`
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

Punch Through
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
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

Pycom Ltd.
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_pycom_gpy`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lopy`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lopy4`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB

Qmobot LLP
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_qchip`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Quirkbot
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_quirkbot`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB

RAK
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_rak811_tracker`
      - :ref:`platform_ststm32`
      - External
      - STM32L151RBT6
      - 32MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_rak811_tracker_32`
      - :ref:`platform_ststm32`
      - External
      - STM32L151RBT6
      - 32MHz
      - 128KB
      - 32KB

RUMBA
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_rumba32_f446ve`
      - :ref:`platform_ststm32`
      - External
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB

Raytac
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_raytac_mdbt50q_rx`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB

RedBearLab
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_redBearLabBLENano`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf52_redbear_blenano2`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_atmelavr_blend`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_nordicnrf52_redbear_blend2`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
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
    * - :ref:`board_nordicnrf51_redBearLab`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

RemRam
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_remram_v1`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F765VIT6
      - 216MHz
      - 2MB
      - 512KB

RepRap
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_reprap_rambo`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB

ReprapWorld
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_minitronics20`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB

RobotDyn
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_robotdyn_blackpill_f303cc`
      - :ref:`platform_ststm32`
      - External
      - STM32F303CCT6
      - 72MHz
      - 256KB
      - 40KB

RoboticsBrno
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_alksesp32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

SG-O
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_sg-o_airMon`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

SODAQ
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_sodaq_autonomo`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_explorer`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
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
    * - :ref:`board_atmelsam_sodaq_one`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_sara`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_sff`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelavr_sodaq_tatu`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB

ST
~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_st3dp001_eval`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F401VGT6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_black_f407ve`
      - :ref:`platform_ststm32`
      - External
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_black_f407vg`
      - :ref:`platform_ststm32`
      - External
      - STM32F407VGT6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_black_f407ze`
      - :ref:`platform_ststm32`
      - External
      - STM32F407ZET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_black_f407zg`
      - :ref:`platform_ststm32`
      - External
      - STM32F407ZGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_blackpill_f401cc`
      - :ref:`platform_ststm32`
      - External
      - STM32F401CCU6
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_blackpill_f401ce`
      - :ref:`platform_ststm32`
      - External
      - STM32F401CEU6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_blue_f407ve_mini`
      - :ref:`platform_ststm32`
      - External
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_coreboard_f401rc`
      - :ref:`platform_ststm32`
      - External
      - STM32F401RCT6
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_g071rb`
      - :ref:`platform_ststm32`
      - External
      - STM32G071RBT6
      - 64MHz
      - 128KB
      - 36KB
    * - :ref:`board_ststm32_nucleo_g431kb`
      - :ref:`platform_ststm32`
      - External
      - STM32G431KBT6
      - 170MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_g431rb`
      - :ref:`platform_ststm32`
      - External
      - STM32G431RBT6
      - 170MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_g474re`
      - :ref:`platform_ststm32`
      - External
      - STM32G474RET6
      - 170MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_wb55rg_p`
      - :ref:`platform_ststm32`
      - On-board
      - STM32WB55RG
      - 64MHz
      - 512KB
      - 192.00KB
    * - :ref:`board_ststm32_rhf76_052`
      - :ref:`platform_ststm32`
      - External
      - STM32L051C8T6
      - 32MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_disco_f413zh`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F413ZHT6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_disco_f746ng`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F746NGH6
      - 216MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_disco_l475vg_iot01a`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L475VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_disco_l072cz_lrwan1`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L072CZ
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_disco_f072rb`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F072RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f030r8`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_nucleo_f031k6`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F031K6T6
      - 48MHz
      - 32KB
      - 4KB
    * - :ref:`board_ststm32_nucleo_f072rb`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F072RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f091rc`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F091RCT6
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_f103rb`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_nucleo_f207zg`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F207ZGT6
      - 120MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f302r8`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F302R8T6
      - 72MHz
      - 64KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f303k8`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F303K8T6
      - 72MHz
      - 64KB
      - 12KB
    * - :ref:`board_ststm32_nucleo_f303re`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F303RET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_f401re`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F401RET6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_nucleo_f411re`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f429zi`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F429ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - :ref:`board_ststm32_nucleo_f446re`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f746zg`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F746ZGT6
      - 216MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_nucleo_f756zg`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F756ZG
      - 216MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_nucleo_f767zi`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F767ZIT6
      - 216MHz
      - 2MB
      - 512KB
    * - :ref:`board_ststm32_nucleo_h743zi`
      - :ref:`platform_ststm32`
      - On-board
      - STM32H743ZIT6
      - 400MHz
      - 2MB
      - 512KB
    * - :ref:`board_ststm32_nucleo_l031k6`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L031K6T6
      - 32MHz
      - 32KB
      - 8KB
    * - :ref:`board_ststm32_nucleo_l053r8`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L053R8T6
      - 32MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_nucleo_l073rz`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L073RZ
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_nucleo_l152re`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L152RET6
      - 32MHz
      - 512KB
      - 80KB
    * - :ref:`board_ststm32_nucleo_l412kb`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L412KBU6
      - 80MHz
      - 128KB
      - 40KB
    * - :ref:`board_ststm32_nucleo_l432kc`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L432KCU6
      - 80MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_l433rc_p`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L433RC
      - 80MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_l452re`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L452RET6
      - 80MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_l476rg`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L476RGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_l496zg`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L496ZGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_l496zg_p`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L496ZGT6P
      - 80MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_nucleo_l4r5zi`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L4R5ZIT6
      - 120MHz
      - 2MB
      - 640KB
    * - :ref:`board_ststm32_disco_f030r8`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_disco_f407vg`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F407VGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_disco_g031j6`
      - :ref:`platform_ststm32`
      - External
      - STM32G031J6
      - 64MHz
      - 128KB
      - 8KB
    * - :ref:`board_ststm32_disco_f100rb`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F100RBT6
      - 24MHz
      - 128KB
      - 8KB
    * - :ref:`board_ststm8_stm8sdisco`
      - :ref:`platform_ststm8`
      - On-board
      - STM8S105C6T6
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_ststm8_stm8sblue`
      - :ref:`platform_ststm8`
      - No
      - STM8S103F3P6
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_ststm8_stm8sblack`
      - :ref:`platform_ststm8`
      - No
      - STM8S105K4T6
      - 16MHz
      - 16KB
      - 2KB
    * - :ref:`board_ststm32_steval_mksboxv1`
      - :ref:`platform_ststm32`
      - External
      - STM32L4R9ZI
      - 120MHz
      - 2MB
      - 640KB

SainSmart
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_sainSmartDue`
      - :ref:`platform_atmelsam`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_sainSmartDueUSB`
      - :ref:`platform_atmelsam`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB

Sanguino
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
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

Schirmilabs
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_eduinowifi`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

Seeed
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_seeed_femto`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeeduino_lorawan`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeed_wio_lite_mg126`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeed_wio_terminal`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51P19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_seeed_xiao`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeed_zero`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

SeeedStudio
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_seeedTinyBLE`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_microchippic32_cui32stem`
      - :ref:`platform_microchippic32`
      - No
      - 32MX795F512H
      - 80MHz
      - 508KB
      - 128KB
    * - :ref:`board_atmelavr_seeeduino`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_espressif8266_wio_link`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_gd32v_wio_lite_risc-v`
      - :ref:`platform_gd32v`
      - External
      - GD32VF103CBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_espressif8266_wio_node`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

Silicognition
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_wesp32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Sipeed
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_gd32v_gd32vf103v-eval`
      - :ref:`platform_gd32v`
      - External
      - GD32VF103VBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_gd32v_sipeed-longan-nano`
      - :ref:`platform_gd32v`
      - External
      - GD32VF103CBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_gd32v_sipeed-longan-nano-lite`
      - :ref:`platform_gd32v`
      - External
      - GD32VF103C8T6
      - 108MHz
      - 64KB
      - 20KB
    * - :ref:`board_kendryte210_sipeed-maix-bit`
      - :ref:`platform_kendryte210`
      - External
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-maix-bit-mic`
      - :ref:`platform_kendryte210`
      - External
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-maix-go`
      - :ref:`platform_kendryte210`
      - External
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-maix-one-dock`
      - :ref:`platform_kendryte210`
      - External
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-maixduino`
      - :ref:`platform_kendryte210`
      - External
      - K210
      - 400MHz
      - 16MB
      - 6MB

SparkFun
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_cui32`
      - :ref:`platform_microchippic32`
      - No
      - 32MX440F512H
      - 80MHz
      - 508KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd21_9dof`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelavr_sparkfun_satmega128rfa1`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA128RFA1
      - 16MHz
      - 16KB
      - 124KB
    * - :ref:`board_espressif8266_sparkfunBlynk`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_atmelavr_sparkfun_digitalsandbox`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_espressif8266_thing`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 512KB
      - 80KB
    * - :ref:`board_espressif8266_thingdev`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 512KB
      - 80KB
    * - :ref:`board_atmelavr_sparkfun_fiov3`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_espressif32_sparkfun_lora_gateway_1-channel`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
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
    * - :ref:`board_atmelsam_sparkfun_qwiic_micro_samd21e`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelavr_sparkfun_redboard`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelsam_sparkfun_redboard_turbo`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd21_dev_usb`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd21_mini_usb`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd21_proRF`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd51_thing_plus`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J20A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelavr_sparkfun_serial7seg`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB

SparkFun Electronics
~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32thing`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

SpellFoundry
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_sleepypi`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB

SweetPea
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_esp210`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

TI
~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_timsp430_lpmsp430fr5739`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430FR5739
      - 16MHz
      - 15.37KB
      - 1KB
    * - :ref:`board_titiva_lplm4f120h5qr`
      - :ref:`platform_titiva`
      - On-board
      - LPLM4F120H5QR
      - 80MHz
      - 256KB
      - 32KB
    * - :ref:`board_titiva_lptm4c1230c3pm`
      - :ref:`platform_titiva`
      - On-board
      - LPTM4C1230C3PM
      - 80MHz
      - 256KB
      - 32KB
    * - :ref:`board_titiva_lptm4c1294ncpdt`
      - :ref:`platform_titiva`
      - On-board
      - LPTM4C1294NCPDT
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_timsp430_lpmsp430f5529`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430F5529
      - 25MHz
      - 47KB
      - 8KB
    * - :ref:`board_timsp430_lpmsp430fr2311`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430FR2311
      - 16MHz
      - 3.75KB
      - 1KB
    * - :ref:`board_timsp430_lpmsp430fr2433`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430FR2433
      - 8MHz
      - 15KB
      - 4KB
    * - :ref:`board_timsp430_lpmsp430fr4133`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430FR4133
      - 8MHz
      - 15KB
      - 2KB
    * - :ref:`board_timsp430_lpmsp430fr5969`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430FR5969
      - 8MHz
      - 47KB
      - 2KB
    * - :ref:`board_timsp430_lpmsp430fr5994`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430FR5994
      - 16MHz
      - 256KB
      - 4KB
    * - :ref:`board_timsp430_lpmsp430fr6989`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430FR6989
      - 8MHz
      - 47KB
      - 2KB
    * - :ref:`board_timsp430_lpmsp430g2231`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430G2231
      - 1MHz
      - 2KB
      - 256B
    * - :ref:`board_timsp430_lpmsp430g2452`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430G2452
      - 16MHz
      - 8KB
      - 256B
    * - :ref:`board_timsp430_lpmsp430g2553`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430G2553
      - 16MHz
      - 16KB
      - 512B

TTGO
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_ttgo-lora32-v1`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-lora32-v2`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-t-beam`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB
    * - :ref:`board_espressif32_ttgo-t-watch`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-t1`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Taida Century
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_stct_nrf52_minidev`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

TauLabs
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_sparky_v1`
      - :ref:`platform_ststm32`
      - External
      - STM32F303CCT6
      - 72MHz
      - 256KB
      - 40KB

Teensy
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_teensy_teensy2`
      - :ref:`platform_teensy`
      - No
      - ATMEGA32U4
      - 16MHz
      - 31.50KB
      - 2.50KB
    * - :ref:`board_teensy_teensy30`
      - :ref:`platform_teensy`
      - No
      - MK20DX128
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_teensy_teensy31`
      - :ref:`platform_teensy`
      - External
      - MK20DX256
      - 72MHz
      - 256KB
      - 64KB
    * - :ref:`board_teensy_teensy35`
      - :ref:`platform_teensy`
      - External
      - MK64FX512
      - 120MHz
      - 512KB
      - 255.99KB
    * - :ref:`board_teensy_teensy36`
      - :ref:`platform_teensy`
      - External
      - MK66FX1M0
      - 180MHz
      - 1MB
      - 256KB
    * - :ref:`board_teensy_teensy40`
      - :ref:`platform_teensy`
      - External
      - IMXRT1062
      - 600MHz
      - 1.94MB
      - 512KB
    * - :ref:`board_teensy_teensy41`
      - :ref:`platform_teensy`
      - External
      - IMXRT1062
      - 600MHz
      - 7.75MB
      - 512KB
    * - :ref:`board_teensy_teensylc`
      - :ref:`platform_teensy`
      - External
      - MKL26Z64
      - 48MHz
      - 62KB
      - 8KB
    * - :ref:`board_teensy_teensy2pp`
      - :ref:`platform_teensy`
      - No
      - AT90USB1286
      - 16MHz
      - 127KB
      - 8KB

ThaiEasyElec
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_espino32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif8266_espinotee`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

The Things Network
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_the_things_uno`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

ThunderPack
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_thunder_pack`
      - :ref:`platform_ststm32`
      - External
      - STM32L072KZ
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_thunder_pack_f411`
      - :ref:`platform_ststm32`
      - External
      - STM32F411CEU6
      - 100MHz
      - 512KB
      - 128KB

Till Harbaum
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_ftduino`
      - :ref:`platform_atmelavr`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
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

TinyPICO
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_tinypico`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Tlera Corporation
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_cicada_l082cz`
      - :ref:`platform_ststm32`
      - External
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_cricket_l082cz`
      - :ref:`platform_ststm32`
      - External
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_gnat_l082cz`
      - :ref:`platform_ststm32`
      - External
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_grasshopper_l082cz`
      - :ref:`platform_ststm32`
      - External
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB

Turta
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_turta_iot_node`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

UBW32
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_ubw32_mx460`
      - :ref:`platform_microchippic32`
      - No
      - 32MX460F512L
      - 80MHz
      - 508KB
      - 32KB
    * - :ref:`board_microchippic32_ubw32_mx795`
      - :ref:`platform_microchippic32`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB

Unknown
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_fm-devkit`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

VAE
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_vake_v1`
      - :ref:`platform_ststm32`
      - External
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB

VCCGND
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_vccgnd_f103zet6`
      - :ref:`platform_ststm32`
      - External
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB

VintLabs
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_vintlabs-devkit-v1`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

WEMOS
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_d1`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif32_lolin_d32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_d32_pro`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wemos_d1_mini32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif8266_d1_mini`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_d1_mini_lite`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_d1_mini_pro`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 16MB
      - 80KB
    * - :ref:`board_espressif32_wemosbat`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Waveshare
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_waveshare_ble400`
      - :ref:`platform_nordicnrf51`
      - External
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_waveshare_open103z`
      - :ref:`platform_ststm32`
      - External
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB

WeAct
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_blackpill_f411ce`
      - :ref:`platform_ststm32`
      - External
      - STM32F411CEU6
      - 100MHz
      - 512KB
      - 128KB

Wicked Device
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
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

Widora
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_widora-air`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

WifiDuino
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_wifiduino`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

Wisen
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_whispernode`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

XinaBox
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_xinabox_cw01`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif32_xinabox_cw02`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

YeaCreate
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_nscreen-32`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

chipKIT
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_lenny`
      - :ref:`platform_microchippic32`
      - No
      - 32MX270F256D
      - 40MHz
      - 120KB
      - 32KB

decaWave
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_dwm1001_dev`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

element14
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_chipkit_pi`
      - :ref:`platform_microchippic32`
      - No
      - 32MX250F128B
      - 40MHz
      - 120KB
      - 32KB

makerlab.mx
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_altair`
      - :ref:`platform_atmelavr`
      - No
      - ATMEGA256RFR2
      - 16MHz
      - 248KB
      - 32KB

meteca
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_briki_abc_esp32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 3.25MB
      - 320KB
    * - :ref:`board_atmelsam_briki_abc_samd21`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_espressif32_briki_mbc-wb_esp32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 3.25MB
      - 320KB
    * - :ref:`board_atmelsam_briki_mbcwb_samd21`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

ng-beacon
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_ng_beacon`
      - :ref:`platform_nordicnrf51`
      - External
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB

nicai-systems
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
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

oddWires
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_iotbusio`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_iotbusproteus`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

sduino
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm8_mb208`
      - :ref:`platform_ststm8`
      - No
      - STM8S208MBT6
      - 16MHz
      - 128KB
      - 6KB
    * - :ref:`board_ststm8_s8uno`
      - :ref:`platform_ststm8`
      - No
      - STM8S105K6T6
      - 16MHz
      - 32KB
      - 2KB

sino:bit
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_Sinobit`
      - :ref:`platform_nordicnrf51`
      - External
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

u-blox
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_ublox_evk_nina_b1`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_espressif32_nina_w10`
      - :ref:`platform_espressif32`
      - No
      - ESP32
      - 240MHz
      - 2MB
      - 320KB

ubIQio
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_ardhat`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
