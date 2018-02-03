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

.. _platform_teensy:

Teensy
======
:ref:`projectconf_env_platform` = ``teensy``

Teensy is a complete USB-based microcontroller development system, in a very small footprint, capable of implementing many types of projects. All programming is done via the USB port. No special programmer is needed, only a standard USB cable and a PC or Macintosh with a USB port.

For more detailed information please visit `vendor site <https://www.pjrc.com/teensy?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: teensy_extra.rst

Examples
--------

Examples are listed from `Teensy development platform repository <https://github.com/platformio/platform-teensy/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_:

* `arduino-blink <https://github.com/platformio/platform-teensy/tree/develop/examples/arduino-blink?utm_source=platformio&utm_medium=docs>`_
* `arduino-hid-usb-mouse <https://github.com/platformio/platform-teensy/tree/develop/examples/arduino-hid-usb-mouse?utm_source=platformio&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-teensy/tree/develop/examples/arduino-internal-libs?utm_source=platformio&utm_medium=docs>`_
* `mbed-blink <https://github.com/platformio/platform-teensy/tree/develop/examples/mbed-blink?utm_source=platformio&utm_medium=docs>`_
* `mbed-dsp <https://github.com/platformio/platform-teensy/tree/develop/examples/mbed-dsp?utm_source=platformio&utm_medium=docs>`_
* `mbed-events <https://github.com/platformio/platform-teensy/tree/develop/examples/mbed-events?utm_source=platformio&utm_medium=docs>`_
* `mbed-rtos <https://github.com/platformio/platform-teensy/tree/develop/examples/mbed-rtos?utm_source=platformio&utm_medium=docs>`_
* `mbed-serial <https://github.com/platformio/platform-teensy/tree/develop/examples/mbed-serial?utm_source=platformio&utm_medium=docs>`_

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

Supported debugging tools are listed in "Debug" column. For more detailed
information, please scroll table by horizontal.
You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` options.


External tools
~~~~~~~~~~~~~~

Boards listed below are compatible with :ref:`piodebug` but depend on external
debugging tools. See "Debug" column for compatible debugging tools.


.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``teensy35``
      - `Teensy 3.5 <https://www.pjrc.com/store/teensy35.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_jlink`
      - MK64FX512
      - 120 MHz
      - 512K
      - 192K
    * - ``teensy36``
      - `Teensy 3.6 <https://www.pjrc.com/store/teensy36.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_jlink`
      - MK66FX1M0
      - 180 MHz
      - 1M
      - 256K


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinoteensy <http://arduino.cc/en/Reference/HomePage?utm_source=platformio&utm_medium=docs>`__
      - Arduino Wiring-based Framework

    * - `framework-mbed <http://mbed.org?utm_source=platformio&utm_medium=docs>`__
      - mbed Framework

    * - `tool-teensy <https://www.pjrc.com/teensy/loader.html?utm_source=platformio&utm_medium=docs>`__
      - Teensy Loader

    * - `toolchain-atmelavr <https://gcc.gnu.org/wiki/avr-gcc?utm_source=platformio&utm_medium=docs>`__
      - avr-gcc

    * - `toolchain-gccarmnoneeabi <https://launchpad.net/gcc-arm-embedded?utm_source=platformio&utm_medium=docs>`__
      - gcc-arm-embedded

.. warning::
    **Linux Users**:

        * Install "udev" rules file `99-platformio-udev.rules <https://github.com/platformio/platformio-core/blob/develop/scripts/99-platformio-udev.rules>`_
          (an instruction is located inside a file).
        * Raspberry Pi users, please read this article
          `Enable serial port on Raspberry Pi <https://hallard.me/enable-serial-port-on-raspberry-pi/>`__.


    **Windows Users:**

        Teensy programming uses only Windows built-in HID
        drivers. When Teensy is programmed to act as a USB Serial device,
        Windows XP, Vista, 7 and 8 require `this serial driver
        <http://www.pjrc.com/teensy/serial_install.exe>`_
        is needed to access the COM port your program uses. No special driver
        installation is necessary on Windows 10.


Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_mbed`
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

Teensy
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
    * - ``teensy20``
      - `Teensy 2.0 <https://www.pjrc.com/store/teensy.html?utm_source=platformio&utm_medium=docs>`_
      - No
      - ATMEGA32U4
      - 16 MHz
      - 31.50K
      - 2.50K
    * - ``teensy20pp``
      - `Teensy++ 2.0 <https://www.pjrc.com/store/teensypp.html?utm_source=platformio&utm_medium=docs>`_
      - No
      - AT90USB1286
      - 16 MHz
      - 127K
      - 8K
    * - ``teensy30``
      - `Teensy 3.0 <https://www.pjrc.com/store/teensy3.html?utm_source=platformio&utm_medium=docs>`_
      - No
      - MK20DX128
      - 48 MHz
      - 128K
      - 16K
    * - ``teensy31``
      - `Teensy 3.1 / 3.2 <https://www.pjrc.com/store/teensy31.html?utm_source=platformio&utm_medium=docs>`_
      - No
      - MK20DX256
      - 72 MHz
      - 256K
      - 64K
    * - ``teensy35``
      - `Teensy 3.5 <https://www.pjrc.com/store/teensy35.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - MK64FX512
      - 120 MHz
      - 512K
      - 192K
    * - ``teensy36``
      - `Teensy 3.6 <https://www.pjrc.com/store/teensy36.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - MK66FX1M0
      - 180 MHz
      - 1M
      - 256K
    * - ``teensylc``
      - `Teensy LC <http://www.pjrc.com/teensy/teensyLC.html?utm_source=platformio&utm_medium=docs>`_
      - No
      - MKL26Z64
      - 48 MHz
      - 62K
      - 8K
