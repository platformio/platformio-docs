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

.. _platform_nordicnrf52:

Nordic nRF52
============

:Configuration:
  :ref:`projectconf_env_platform` = ``nordicnrf52``

The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor and are the most capable Bluetooth Smart SoCs on the market.

For more detailed information please visit `vendor site <https://www.nordicsemi.com/Products/nRF52-Series-SoC?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: nordicnrf52_extra.rst

Examples
--------

Examples are listed from `Nordic nRF52 development platform repository <https://github.com/platformio/platform-nordicnrf52/tree/master/examples?utm_source=platformio&utm_medium=docs>`_:

* `arduino-ble-led <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/arduino-ble-led?utm_source=platformio&utm_medium=docs>`_
* `arduino-blink <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/arduino-blink?utm_source=platformio&utm_medium=docs>`_
* `mbed-ble-thermometer <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/mbed-ble-thermometer?utm_source=platformio&utm_medium=docs>`_
* `mbed-blink <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/mbed-blink?utm_source=platformio&utm_medium=docs>`_
* `mbed-dsp <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/mbed-dsp?utm_source=platformio&utm_medium=docs>`_
* `mbed-events <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/mbed-events?utm_source=platformio&utm_medium=docs>`_
* `mbed-rtos <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/mbed-rtos?utm_source=platformio&utm_medium=docs>`_
* `mbed-serial <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/mbed-serial?utm_source=platformio&utm_medium=docs>`_

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
    * - :ref:`board_nordicnrf52_delta_dfbm_nq620`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52_dk`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52840_dk`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_redbear_blenano2`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_redbear_blend2`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_ublox_evk_nina_b1`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB


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
    * - :ref:`board_nordicnrf52_bluey`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_stct_nrf52_minidev`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_hackaBLE`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-nordicnrf52/releases>`__
of Nordic nRF52 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = nordicnrf52
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = nordicnrf52@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-nordicnrf52.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinonordicnrf5 <https://github.com/sandeepmistry/arduino-nRF5?utm_source=platformio&utm_medium=docs>`__
      - Arduino Wiring-based Framework (Nordic NRF5 Core)

    * - `framework-mbed <http://mbed.org?utm_source=platformio&utm_medium=docs>`__
      - mbed Framework

    * - `tool-jlink <https://www.segger.com/downloads/jlink/?utm_source=platformio&utm_medium=docs>`__
      - SEGGER J-Link Software and Documentation Pack

    * - `tool-nrfjprog <https://www.nordicsemi.com?utm_source=platformio&utm_medium=docs>`__
      - nRF5x command line tool

    * - `tool-openocd <http://openocd.org?utm_source=platformio&utm_medium=docs>`__
      - OpenOCD

    * - `tool-sreccat <https://github.com/marcows/SRecord?utm_source=platformio&utm_medium=docs>`__
      - Merging tool

    * - `toolchain-gccarmnoneeabi <https://launchpad.net/gcc-arm-embedded?utm_source=platformio&utm_medium=docs>`__
      - gcc-arm-embedded

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
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_mbed`
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

Delta
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_delta_dfbm_nq620`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

Electronut Labs
~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_bluey`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_hackaBLE`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

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
    * - :ref:`board_nordicnrf52_nrf52_dk`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52840_dk`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB

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
    * - :ref:`board_nordicnrf52_redbear_blenano2`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_redbear_blend2`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

Taida Century
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_stct_nrf52_minidev`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

u-blox
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_ublox_evk_nina_b1`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
