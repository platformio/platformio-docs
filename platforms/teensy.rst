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

:Registry:
  `https://registry.platformio.org/platforms/platformio/teensy <https://registry.platformio.org/platforms/platformio/teensy>`__
:Configuration:
  :ref:`projectconf_env_platform` = ``platformio/teensy``

Teensy is a complete USB-based microcontroller development system, in a very small footprint, capable of implementing many types of projects. All programming is done via the USB port. No special programmer is needed, only a standard USB cable and a PC or Macintosh with a USB port.

For more detailed information please visit `vendor site <https://www.pjrc.com/teensy?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: teensy_extra.rst

Examples
--------

Examples are listed from `Teensy development platform repository <https://github.com/platformio/platform-teensy/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `zephyr-blink <https://github.com/platformio/platform-teensy/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-blink <https://github.com/platformio/platform-teensy/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-hid-usb-mouse <https://github.com/platformio/platform-teensy/tree/master/examples/arduino-hid-usb-mouse?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-teensy/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-synchronization <https://github.com/platformio/platform-teensy/tree/master/examples/zephyr-synchronization?utm_source=platformio.org&utm_medium=docs>`_

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


External Debug Tools
^^^^^^^^^^^^^^^^^^^^

Boards listed below are compatible with :ref:`piodebug` but **DEPEND ON**
external debug probe. They **ARE NOT READY** for debugging.
Please click on board name for the further details.


.. list-table::
    :header-rows:  1

    * - Name
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_teensy_teensymm`
      - IMXRT1062
      - 600MHz
      - 7.75MB
      - 512KB
    * - :ref:`board_teensy_teensy31`
      - MK20DX256
      - 72MHz
      - 256KB
      - 64KB
    * - :ref:`board_teensy_teensy35`
      - MK64FX512
      - 120MHz
      - 512KB
      - 255.99KB
    * - :ref:`board_teensy_teensy36`
      - MK66FX1M0
      - 180MHz
      - 1MB
      - 256KB
    * - :ref:`board_teensy_teensy40`
      - IMXRT1062
      - 600MHz
      - 1.94MB
      - 512KB
    * - :ref:`board_teensy_teensy41`
      - IMXRT1062
      - 600MHz
      - 7.75MB
      - 512KB
    * - :ref:`board_teensy_teensylc`
      - MKL26Z64
      - 48MHz
      - 62KB
      - 8KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-teensy/releases>`__
of Teensy development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version, NOT recommended
    ; Pin the version as shown below
    [env:latest_stable]
    platform = teensy
    board = ...

    ; Specific version
    [env:custom_stable]
    platform = teensy@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-teensy.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinoteensy <https://registry.platformio.org/tools/platformio/framework-arduinoteensy>`__
      - Arduino Wiring-based Framework for Teensy boards

    * - `framework-zephyr <https://registry.platformio.org/tools/platformio/framework-zephyr>`__
      - Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures

    * - `tool-cmake <https://registry.platformio.org/tools/platformio/tool-cmake>`__
      - CMake is an open-source, cross-platform family of tools designed to build, test and package software

    * - `tool-dtc <https://registry.platformio.org/tools/platformio/tool-dtc>`__
      - Device tree compiler

    * - `tool-gperf <https://registry.platformio.org/tools/platformio/tool-gperf>`__
      - GNU gperf is a perfect hash function generator

    * - `tool-jlink <https://registry.platformio.org/tools/platformio/tool-jlink>`__
      - Software and Documentation Pack for SEGGER J-Link debug probes

    * - `tool-ninja <https://registry.platformio.org/tools/platformio/tool-ninja>`__
      - Ninja is a small build system with a focus on speed

    * - `tool-teensy <https://registry.platformio.org/tools/platformio/tool-teensy>`__
      - Upload tools for Teensy boards

    * - `toolchain-atmelavr <https://registry.platformio.org/tools/platformio/toolchain-atmelavr>`__
      - GCC Toolchain for Microchip AVR microcontrollers

    * - `toolchain-gccarmnoneeabi <https://registry.platformio.org/tools/platformio/toolchain-gccarmnoneeabi>`__
      - GNU toolchain for Arm Cortex-M and Cortex-R processors

    * - `toolchain-gccarmnoneeabi-teensy <https://registry.platformio.org/tools/platformio/toolchain-gccarmnoneeabi-teensy>`__
      - GNU toolchain for Teensy boards based on Arm Cortex-M

.. warning::
    **Linux Users**:

        * Install "udev" rules :ref:`platformio_udev_rules`
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

    * - :ref:`framework_zephyr`
      - Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

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
    * - :ref:`board_teensy_teensymm`
      - External
      - IMXRT1062
      - 600MHz
      - 7.75MB
      - 512KB

Teensy
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_teensy_teensy2`
      - No
      - ATMEGA32U4
      - 16MHz
      - 31.50KB
      - 2.50KB
    * - :ref:`board_teensy_teensy30`
      - No
      - MK20DX128
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_teensy_teensy31`
      - External
      - MK20DX256
      - 72MHz
      - 256KB
      - 64KB
    * - :ref:`board_teensy_teensy35`
      - External
      - MK64FX512
      - 120MHz
      - 512KB
      - 255.99KB
    * - :ref:`board_teensy_teensy36`
      - External
      - MK66FX1M0
      - 180MHz
      - 1MB
      - 256KB
    * - :ref:`board_teensy_teensy40`
      - External
      - IMXRT1062
      - 600MHz
      - 1.94MB
      - 512KB
    * - :ref:`board_teensy_teensy41`
      - External
      - IMXRT1062
      - 600MHz
      - 7.75MB
      - 512KB
    * - :ref:`board_teensy_teensylc`
      - External
      - MKL26Z64
      - 48MHz
      - 62KB
      - 8KB
    * - :ref:`board_teensy_teensy2pp`
      - No
      - AT90USB1286
      - 16MHz
      - 127KB
      - 8KB
