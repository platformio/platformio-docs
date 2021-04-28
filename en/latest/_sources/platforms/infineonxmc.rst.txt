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

.. _platform_infineonxmc:

Infineon XMC
============

:Configuration:
  :ref:`projectconf_env_platform` = ``infineonxmc``

Infineon has designed the XMC microcontrollers for real-time critical applications with an industry-standard core. The XMC microcontrollers can be integrated with the Arduino platform

For more detailed information please visit `vendor site <https://www.infineon.com?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Infineon XMC development platform repository <https://github.com/Infineon/platformio-infineonxmc/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `ifx9201 <https://github.com/Infineon/platformio-infineonxmc/tree/master/examples/ifx9201?utm_source=platformio.org&utm_medium=docs>`_
* `device-control <https://github.com/Infineon/platformio-infineonxmc/tree/master/examples/device-control?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-blink <https://github.com/Infineon/platformio-infineonxmc/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `spi <https://github.com/Infineon/platformio-infineonxmc/tree/master/examples/spi?utm_source=platformio.org&utm_medium=docs>`_
* `ultrasonic <https://github.com/Infineon/platformio-infineonxmc/tree/master/examples/ultrasonic?utm_source=platformio.org&utm_medium=docs>`_
* `rtc <https://github.com/Infineon/platformio-infineonxmc/tree/master/examples/rtc?utm_source=platformio.org&utm_medium=docs>`_
* `radar <https://github.com/Infineon/platformio-infineonxmc/tree/master/examples/radar?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-wire <https://github.com/Infineon/platformio-infineonxmc/tree/master/examples/arduino-wire?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_infineonxmc_xmc1100_boot_kit`
      - XMC1100
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1100_h_bridge2go`
      - XMC1100
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1100_xmc2go`
      - XMC1100
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1300_boot_kit`
      - XMC1300
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1300_sense2gol`
      - XMC1300
      - 32MHz
      - 32KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1400_boot_kit`
      - XMC1400
      - 48MHz
      - 1.95MB
      - 16KB
    * - :ref:`board_infineonxmc_xmc4200_distance2go`
      - XMC4200
      - 80MHz
      - 256KB
      - 40KB
    * - :ref:`board_infineonxmc_xmc4700_relax_kit`
      - XMC4700
      - 144MHz
      - 2.00MB
      - 1.95MB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/Infineon/platformio-infineonxmc/releases>`__
of Infineon XMC development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = infineonxmc
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = infineonxmc@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/Infineon/platformio-infineonxmc.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinoxmc <https://github.com/Infineon/XMC-for-Arduino.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Infineon's XMC microcontrollers

    * - `tool-jlink <https://www.segger.com/downloads/jlink/?utm_source=platformio.org&utm_medium=docs>`__
      - Software and Documentation Pack for SEGGER J-Link debug probes

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

Infineon
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_infineonxmc_xmc1100_boot_kit`
      - On-board
      - XMC1100
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1100_h_bridge2go`
      - On-board
      - XMC1100
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1100_xmc2go`
      - On-board
      - XMC1100
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1300_boot_kit`
      - On-board
      - XMC1300
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1300_sense2gol`
      - On-board
      - XMC1300
      - 32MHz
      - 32KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1400_boot_kit`
      - On-board
      - XMC1400
      - 48MHz
      - 1.95MB
      - 16KB
    * - :ref:`board_infineonxmc_xmc4200_distance2go`
      - On-board
      - XMC4200
      - 80MHz
      - 256KB
      - 40KB
    * - :ref:`board_infineonxmc_xmc4700_relax_kit`
      - On-board
      - XMC4700
      - 144MHz
      - 2.00MB
      - 1.95MB
