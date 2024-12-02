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

.. _platform_renesas-ra:

Renesas RA
==========

:Registry:
  `https://registry.platformio.org/platforms/platformio/renesas-ra <https://registry.platformio.org/platforms/platformio/renesas-ra>`__
:Configuration:
  :ref:`projectconf_env_platform` = ``platformio/renesas-ra``

Renesas Advanced (RA) 32-bit microcontrollers with the Arm Cortex-M33, -M23 and -M4 processor cores deliver key advantages compared to competitive Arm Cortex-M MCUs by providing stronger embedded security, superior CoreMark performance and ultra-low power operation.

For more detailed information please visit `vendor site <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Renesas RA development platform repository <https://github.com/platformio/platform-renesas-ra/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `arduino-uno-r4-led-animation <https://github.com/platformio/platform-renesas-ra/tree/master/examples/arduino-uno-r4-led-animation?utm_source=platformio.org&utm_medium=docs>`_
* `fsp-button-isr <https://github.com/platformio/platform-renesas-ra/tree/master/examples/fsp-button-isr?utm_source=platformio.org&utm_medium=docs>`_
* `cmsis-blink <https://github.com/platformio/platform-renesas-ra/tree/master/examples/cmsis-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-blink <https://github.com/platformio/platform-renesas-ra/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-renesas-ra/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs>`_
* `fsp-blink <https://github.com/platformio/platform-renesas-ra/tree/master/examples/fsp-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-iot-cloud-basic <https://github.com/platformio/platform-renesas-ra/tree/master/examples/arduino-iot-cloud-basic?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-wifiscan <https://github.com/platformio/platform-renesas-ra/tree/master/examples/arduino-wifiscan?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_renesas-ra_uno_r4_wifi`
      - RA4M1
      - 48MHz
      - 256KB
      - 32KB


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
    * - :ref:`board_renesas-ra_portenta_c33`
      - R7FA6M5BH2CBG
      - 200MHz
      - 2MB
      - 511.35KB
    * - :ref:`board_renesas-ra_uno_r4_minima`
      - RA4M1
      - 48MHz
      - 256KB
      - 32KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-renesas-ra/releases>`__
of Renesas RA development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version, NOT recommended
    ; Pin the version as shown below
    [env:latest_stable]
    platform = renesas-ra
    board = ...

    ; Specific version
    [env:custom_stable]
    platform = renesas-ra@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-renesas-ra.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinorenesas-portenta <https://registry.platformio.org/tools/platformio/framework-arduinorenesas-portenta>`__
      - Arduino Wiring-based Framework for Renesas MCUs (Portenta core)

    * - `framework-arduinorenesas-uno <https://registry.platformio.org/tools/platformio/framework-arduinorenesas-uno>`__
      - Arduino Wiring-based Framework for Renesas MCUs (UNOR4 core)

    * - `framework-cmsis-renesas <https://registry.platformio.org/tools/platformio/framework-cmsis-renesas>`__
      - Renesas FSP CMSIS module for Renesas RA MCU family

    * - `framework-renesas-fsp <https://registry.platformio.org/tools/platformio/framework-renesas-fsp>`__
      - The Renesas Flexible Software Package (FSP) is an enhanced software package designed to provide easy-to-use, scalable, high-quality software for embedded system designs using Renesas RA family of Arm Microcontrollers.

    * - `tool-bossac <https://registry.platformio.org/tools/platformio/tool-bossac>`__
      - Basic Open Source SAM-BA Application (BOSSA)

    * - `tool-dfuutil-arduino <https://registry.platformio.org/tools/platformio/tool-dfuutil-arduino>`__
      - Device Firmware Upgrade Utilities

    * - `tool-jlink <https://registry.platformio.org/tools/platformio/tool-jlink>`__
      - Software and Documentation Pack for SEGGER J-Link debug probes

    * - `tool-openocd <https://registry.platformio.org/tools/platformio/tool-openocd>`__
      - Open On-Chip Debugger. Free and Open On-Chip Debugging, In-System Programming and Boundary-Scan Testing

    * - `toolchain-gccarmnoneeabi <https://registry.platformio.org/tools/platformio/toolchain-gccarmnoneeabi>`__
      - GNU toolchain for Arm Cortex-M and Cortex-R processors

.. warning::
    **Linux Users**:

        * Install "udev" rules :ref:`platformio_udev_rules`
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

    * - :ref:`framework_cmsis`
      - Vendor-independent hardware abstraction layer for the Cortex-M processor series

    * - :ref:`framework_fsp`
      - The Renesas Flexible Software Package (FSP) is an enhanced software package designed to provide easy-to-use, scalable, high-quality software for embedded system designs using Renesas RA family of Arm Microcontrollers.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command
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
    * - :ref:`board_renesas-ra_portenta_c33`
      - External
      - R7FA6M5BH2CBG
      - 200MHz
      - 2MB
      - 511.35KB
    * - :ref:`board_renesas-ra_uno_r4_minima`
      - External
      - RA4M1
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_renesas-ra_uno_r4_wifi`
      - On-board
      - RA4M1
      - 48MHz
      - 256KB
      - 32KB
