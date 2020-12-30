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

.. _platform_atmelmegaavr:

Atmel megaAVR
=============

:Configuration:
  :ref:`projectconf_env_platform` = ``atmelmegaavr``

8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

For more detailed information please visit `vendor site <https://www.microchip.com/design-centers/8-bit/avr-mcus/device-selection/atmega4809?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: atmelmegaavr_extra.rst

Examples
--------

Examples are listed from `Atmel megaAVR development platform repository <https://github.com/platformio/platform-atmelmegaavr/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `arduino-blink <https://github.com/platformio/platform-atmelmegaavr/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `native-blink <https://github.com/platformio/platform-atmelmegaavr/tree/master/examples/native-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-atmelmegaavr/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-external-libs <https://github.com/platformio/platform-atmelmegaavr/tree/master/examples/arduino-external-libs?utm_source=platformio.org&utm_medium=docs>`_

Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-atmelmegaavr/releases>`__
of Atmel megaAVR development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = atmelmegaavr
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = atmelmegaavr@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-atmelmegaavr.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduino-megaavr <https://github.com/arduino/ArduinoCore-megaavr.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip megaAVR microcontrollers

    * - `framework-arduino-megaavr-megacorex <https://github.com/MCUdude/MegaCoreX.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip megaAVR microcontrollers (MegaCoreX)

    * - `framework-arduino-megaavr-megatinycore <https://github.com/SpenceKonde/megaTinyCore.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip tinyAVR 0-series and 1-series chips (megaTinyCore)

    * - `tool-avrdude-megaavr <http://savannah.nongnu.org/projects/avrdude?utm_source=platformio.org&utm_medium=docs>`__
      - AVRDUDE is a utility to download/upload/manipulate the ROM and EEPROM contents of megaAVR microcontrollers

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

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

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
    * - :ref:`board_atmelmegaavr_nano_every`
      - No
      - ATMEGA4809
      - 16MHz
      - 47.50KB
      - 6KB
    * - :ref:`board_atmelmegaavr_uno_wifi_rev2`
      - No
      - ATMEGA4809
      - 16MHz
      - 47.50KB
      - 6KB

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
    * - :ref:`board_atmelmegaavr_ATmega1608`
      - No
      - ATMEGA1608
      - 16MHz
      - 16KB
      - 2KB
    * - :ref:`board_atmelmegaavr_ATmega1609`
      - No
      - ATMEGA1609
      - 16MHz
      - 16KB
      - 2KB
    * - :ref:`board_atmelmegaavr_ATmega3208`
      - No
      - ATMEGA3208
      - 16MHz
      - 32KB
      - 4KB
    * - :ref:`board_atmelmegaavr_ATmega3209`
      - No
      - ATMEGA3209
      - 16MHz
      - 32KB
      - 4KB
    * - :ref:`board_atmelmegaavr_ATmega4808`
      - No
      - ATMEGA4808
      - 16MHz
      - 48KB
      - 6KB
    * - :ref:`board_atmelmegaavr_ATmega4809`
      - No
      - ATMEGA4809
      - 16MHz
      - 48KB
      - 6KB
    * - :ref:`board_atmelmegaavr_ATmega808`
      - No
      - ATMEGA808
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelmegaavr_ATmega809`
      - No
      - ATMEGA809
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelmegaavr_ATtiny1604`
      - No
      - ATTINY1604
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelmegaavr_ATtiny1606`
      - No
      - ATTINY1606
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelmegaavr_ATtiny1607`
      - No
      - ATTINY1607
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelmegaavr_ATtiny1614`
      - No
      - ATTINY1614
      - 16MHz
      - 16KB
      - 2KB
    * - :ref:`board_atmelmegaavr_ATtiny1616`
      - No
      - ATTINY1616
      - 16MHz
      - 16KB
      - 2KB
    * - :ref:`board_atmelmegaavr_ATtiny1617`
      - No
      - ATTINY1617
      - 16MHz
      - 16KB
      - 2KB
    * - :ref:`board_atmelmegaavr_ATtiny202`
      - No
      - ATTINY202
      - 16MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelmegaavr_ATtiny204`
      - No
      - ATTINY204
      - 16MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelmegaavr_ATtiny212`
      - No
      - ATTINY212
      - 16MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelmegaavr_ATtiny214`
      - No
      - ATTINY214
      - 16MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelmegaavr_ATtiny3216`
      - No
      - ATTINY3216
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelmegaavr_ATtiny3217`
      - No
      - ATTINY3217
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelmegaavr_ATtiny402`
      - No
      - ATTINY402
      - 16MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelmegaavr_ATtiny404`
      - No
      - ATTINY404
      - 16MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelmegaavr_ATtiny406`
      - No
      - ATTINY406
      - 16MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelmegaavr_ATtiny412`
      - No
      - ATTINY412
      - 16MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelmegaavr_ATtiny414`
      - No
      - ATTINY414
      - 16MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelmegaavr_ATtiny416`
      - No
      - ATTINY416
      - 16MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelmegaavr_ATtiny417`
      - No
      - ATTINY417
      - 16MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelmegaavr_ATtiny804`
      - No
      - ATTINY804
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelmegaavr_ATtiny806`
      - No
      - ATTINY806
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelmegaavr_ATtiny807`
      - No
      - ATTINY807
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelmegaavr_ATtiny814`
      - No
      - ATTINY814
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelmegaavr_ATtiny816`
      - No
      - ATTINY816
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelmegaavr_ATtiny817`
      - No
      - ATTINY817
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelmegaavr_avr_iot_wg`
      - No
      - ATMEGA4808
      - 16MHz
      - 48KB
      - 6KB
    * - :ref:`board_atmelmegaavr_curiosity_nano_4809`
      - No
      - ATMEGA4809
      - 16MHz
      - 48KB
      - 6KB
    * - :ref:`board_atmelmegaavr_xplained_pro_4809`
      - No
      - ATMEGA4809
      - 16MHz
      - 48KB
      - 6KB
