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

.. _platform_raspberrypi:

Raspberry Pi RP2040
===================

:Configuration:
  :ref:`projectconf_env_platform` = ``raspberrypi``

RP2040 is a low-cost, high-performance microcontroller device with with a large on-chip memory, symmetric dual-core processor complex, and rich peripheral.

For more detailed information please visit `vendor site <https://www.raspberrypi.org/documentation/rp2040/getting-started/?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. warning::
    Windows OS may not have necessary drivers to properly program Raspberry Pi Pico boards.
    Please make sure your board is recognized and visible in the Device Managers in both
    generic and bootloader modes. Usually, if there is only a mass storage device called
    ``RPI-RP2`` then you need to program your board manually by dragging and dropping the
    ``firmware.uf2`` file directly to that mass storage device.


Examples
--------

Examples are listed from `Raspberry Pi RP2040 development platform repository <https://github.com/platformio/platform-raspberrypi/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `arduino-blink <https://github.com/platformio/platform-raspberrypi/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-external-libs <https://github.com/platformio/platform-raspberrypi/tree/master/examples/arduino-external-libs?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_raspberrypi_nanorp2040connect`
      - RP2040
      - 133MHz
      - 2MB
      - 264KB
    * - :ref:`board_raspberrypi_pico`
      - RP2040
      - 133MHz
      - 2MB
      - 264KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-raspberrypi/releases>`__
of Raspberry Pi RP2040 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = raspberrypi
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = raspberrypi@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-raspberrypi.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduino-mbed <https://www.arduino.cc/reference/en?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino framework supporting mbed-enabled boards

    * - `tool-jlink <https://www.segger.com/downloads/jlink/?utm_source=platformio.org&utm_medium=docs>`__
      - Software and Documentation Pack for SEGGER J-Link debug probes

    * - `tool-openocd-raspberrypi <http://openocd.org?utm_source=platformio.org&utm_medium=docs>`__
      - Open On-Chip Debugger for Raspberry Pi MCUs

    * - `tool-rp2040tools <https://github.com/arduino/ArduinoCore-mbed?utm_source=platformio.org&utm_medium=docs>`__
      - Tools for interacting with a RP2040 device in BOOTSEL mode or with a RP2040 binary

    * - `toolchain-gccarmnoneeabi <https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm?utm_source=platformio.org&utm_medium=docs>`__
      - GNU toolchain for Arm Cortex-M and Cortex-R processors

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
    * - :ref:`board_raspberrypi_nanorp2040connect`
      - External
      - RP2040
      - 133MHz
      - 2MB
      - 264KB

Raspberry Pi
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_raspberrypi_pico`
      - External
      - RP2040
      - 133MHz
      - 2MB
      - 264KB
