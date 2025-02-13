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

.. _platform_nordicnrf51:

Nordic nRF51
============

:Registry:
  `https://registry.platformio.org/platforms/platformio/nordicnrf51 <https://registry.platformio.org/platforms/platformio/nordicnrf51>`__
:Configuration:
  :ref:`projectconf_env_platform` = ``platformio/nordicnrf51``

The Nordic nRF51 Series is a family of highly flexible, multi-protocol, system-on-chip (SoC) devices for ultra-low power wireless applications. nRF51 Series devices support a range of protocol stacks including Bluetooth Smart (previously called Bluetooth low energy), ANT and proprietary 2.4GHz protocols such as Gazell.

For more detailed information please visit `vendor site <https://www.nordicsemi.com/eng/Products/nRF51-Series-SoC?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Nordic nRF51 development platform repository <https://github.com/platformio/platform-nordicnrf51/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `zephyr-blink <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-blink <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-ble-led <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/arduino-ble-led?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-ble-eddystone <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/zephyr-ble-eddystone?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-drivers-entropy <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/zephyr-drivers-entropy?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_nordicnrf51_bbcmicrobit`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf51_calliope_mini`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf51_nrf51_beacon`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_nrf51_dongle`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_nrf51_dk`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_redBearLabBLENano`
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_redBearLab`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf51_seeedTinyBLE`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf51_vbluno51`
      - NRF51822
      - 16MHz
      - 128KB
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
    * - :ref:`board_nordicnrf51_bluz_dk`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_oshchip`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_Sinobit`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_waveshare_ble400`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_ng_beacon`
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-nordicnrf51/releases>`__
of Nordic nRF51 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version, NOT recommended
    ; Pin the version as shown below
    [env:latest_stable]
    platform = nordicnrf51
    board = ...

    ; Specific version
    [env:custom_stable]
    platform = nordicnrf51@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-nordicnrf51.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinonordicnrf5 <https://registry.platformio.org/tools/platformio/framework-arduinonordicnrf5>`__
      - Arduino Wiring-based Framework for Nordic Semiconductor nRF5 based boards

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

    * - `tool-nrfjprog <https://registry.platformio.org/tools/platformio/tool-nrfjprog>`__
      - nRFx command line tools

    * - `tool-openocd <https://registry.platformio.org/tools/platformio/tool-openocd>`__
      - Open On-Chip Debugger. Free and Open On-Chip Debugging, In-System Programming and Boundary-Scan Testing

    * - `tool-sreccat <https://registry.platformio.org/tools/platformio/tool-sreccat>`__
      - Collection of powerful tools for manipulating EPROM load files

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

    * - :ref:`framework_zephyr`
      - Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

BBC
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_bbcmicrobit`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

BluzDK
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_bluz_dk`
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_calliope_mini`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

Nordic
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_nrf51_beacon`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_nrf51_dongle`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_nrf51_dk`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

OSHChip
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_oshchip`
      - External
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

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
    * - :ref:`board_nordicnrf51_redBearLabBLENano`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_redBearLab`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

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
    * - :ref:`board_nordicnrf51_seeedTinyBLE`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

VNG
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_vbluno51`
      - On-board
      - NRF51822
      - 16MHz
      - 128KB
      - 32KB

Waveshare
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_waveshare_ble400`
      - External
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

ng-beacon
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_ng_beacon`
      - External
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB

sino:bit
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_Sinobit`
      - External
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
