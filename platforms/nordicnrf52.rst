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

:Registry:
  `https://registry.platformio.org/platforms/platformio/nordicnrf52 <https://registry.platformio.org/platforms/platformio/nordicnrf52>`__
:Configuration:
  :ref:`projectconf_env_platform` = ``platformio/nordicnrf52``

The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor which makes them quite capable Bluetooth Smart SoCs.

For more detailed information please visit `vendor site <https://www.nordicsemi.com/Products/nRF52-Series-SoC?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: nordicnrf52_extra.rst

Examples
--------

Examples are listed from `Nordic nRF52 development platform repository <https://github.com/platformio/platform-nordicnrf52/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `zephyr-blink <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-net-echo-client <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/zephyr-net-echo-client?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-blink <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-ble-battery <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/mbed-rtos-ble-battery?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-ble-led <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/arduino-ble-led?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-blink-baremetal <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/mbed-rtos-blink-baremetal?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-ble-beacon <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/zephyr-ble-beacon?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-subsys-nvs <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/zephyr-subsys-nvs?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-nfc <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/mbed-rtos-nfc?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-nina-b1-generic-example <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/arduino-nina-b1-generic-example?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-bluefruit-bleuart <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/arduino-bluefruit-bleuart?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-serial-plotter <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/arduino-serial-plotter?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_nordicnrf52_nicla_sense_me`
      - NRF52832
      - 64MHz
      - 515.25KB
      - 62.78KB
    * - :ref:`board_nordicnrf52_bbcmicrobit_v2`
      - NRF52833
      - 64MHz
      - 512KB
      - 128KB
    * - :ref:`board_nordicnrf52_laird_bl652_dvk`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_laird_bl653_dvk`
      - NRF52833
      - 64MHz
      - 512KB
      - 128KB
    * - :ref:`board_nordicnrf52_laird_bl654_dvk`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_delta_dfbm_nq620`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_electronut_blip`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_electronut_papyr`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_nrf52832_mdk`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52840_mdk`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_nrf52_dk`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52833_dk`
      - NRF52833
      - 64MHz
      - 512KB
      - 128KB
    * - :ref:`board_nordicnrf52_nrf52840_dk`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_nrf52840_dk_adafruit`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_reel_board`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_reel_board_v2`
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
    * - :ref:`board_nordicnrf52_vbluno52`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_dwm1001_dev`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_ublox_bmd345eval_nrf52840`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
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
    * - :ref:`board_nordicnrf52_96b_nitrogen`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52832`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_adafruit_clue_nrf52840`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52840_sense`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52840`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_ledglasses_nrf52840`
      - NRF52840
      - 64MHz
      - 796KB
      - 232KB
    * - :ref:`board_nordicnrf52_nano33ble`
      - NRF52840
      - 64MHz
      - 960KB
      - 256KB
    * - :ref:`board_nordicnrf52_bluey`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_calliopemini_v3`
      - NRF52833
      - 64MHz
      - 512KB
      - 128KB
    * - :ref:`board_nordicnrf52_adafruit_cplaynrf52840`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_holyiot_yj16019`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_adafruit_itsybitsy_nrf52840`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_laird_pinnacle_100_dvk`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_adafruit_metro_nrf52840`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_thingy_52`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_particle_argon`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_particle_boron`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_particle_xenon`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_raytac_mdbt50q_rx`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_ruuvitag`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_sdt52832b`
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

    ; Latest stable version, NOT recommended
    ; Pin the version as shown below
    [env:latest_stable]
    platform = nordicnrf52
    board = ...

    ; Specific version
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

    * - `framework-arduino-mbed <https://registry.platformio.org/tools/platformio/framework-arduino-mbed>`__
      - Arduino framework supporting mbed-enabled boards

    * - `framework-arduinoadafruitnrf52 <https://registry.platformio.org/tools/platformio/framework-arduinoadafruitnrf52>`__
      - Arduino Wiring-based Framework for Nordic Semiconductor nRF52 BLE SoC

    * - `framework-arduinonordicnrf5 <https://registry.platformio.org/tools/platformio/framework-arduinonordicnrf5>`__
      - Arduino Wiring-based Framework for Nordic Semiconductor nRF5 based boards

    * - `framework-cmsis <https://registry.platformio.org/tools/platformio/framework-cmsis>`__
      - Vendor-independent hardware abstraction layer for the Cortex-M processor series

    * - `framework-mbed <https://registry.platformio.org/tools/platformio/framework-mbed>`__
      - Arm Mbed OS is a platform operating system designed for the internet of things

    * - `framework-zephyr <https://registry.platformio.org/tools/platformio/framework-zephyr>`__
      - Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures

    * - `tool-adafruit-nrfutil <https://registry.platformio.org/tools/platformio/tool-adafruit-nrfutil>`__
      - adafruit-nrfutil is a Python package that includes the adafruit-nrfutil command line utility and the nordicsemi library.

    * - `tool-bossac-nordicnrf52 <https://registry.platformio.org/tools/platformio/tool-bossac-nordicnrf52>`__
      - Basic Open Source SAM-BA Application (BOSSA) for Nordic nRF52 microcontrollers

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

    * - :ref:`framework_mbed`
      - Arm Mbed OS is a platform operating system designed for the internet of things

    * - :ref:`framework_zephyr`
      - Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

96Boards
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_96b_nitrogen`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

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
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52832`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_adafruit_clue_nrf52840`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52840_sense`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52840`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_ledglasses_nrf52840`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 232KB
    * - :ref:`board_nordicnrf52_adafruit_cplaynrf52840`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_itsybitsy_nrf52840`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_metro_nrf52840`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB

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
    * - :ref:`board_nordicnrf52_nano33ble`
      - External
      - NRF52840
      - 64MHz
      - 960KB
      - 256KB
    * - :ref:`board_nordicnrf52_nicla_sense_me`
      - On-board
      - NRF52832
      - 64MHz
      - 515.25KB
      - 62.78KB

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
    * - :ref:`board_nordicnrf52_bbcmicrobit_v2`
      - On-board
      - NRF52833
      - 64MHz
      - 512KB
      - 128KB

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
    * - :ref:`board_nordicnrf52_calliopemini_v3`
      - External
      - NRF52833
      - 64MHz
      - 512KB
      - 128KB

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

ElectronutLabs
~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_electronut_blip`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_electronut_papyr`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB

Holyiot
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_holyiot_yj16019`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

Laird Connectivity
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_laird_bl652_dvk`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_laird_bl653_dvk`
      - On-board
      - NRF52833
      - 64MHz
      - 512KB
      - 128KB
    * - :ref:`board_nordicnrf52_laird_bl654_dvk`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_laird_pinnacle_100_dvk`
      - External
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB

Makerdiary
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_nrf52832_mdk`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52840_mdk`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB

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
    * - :ref:`board_nordicnrf52_thingy_52`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52_dk`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52833_dk`
      - On-board
      - NRF52833
      - 64MHz
      - 512KB
      - 128KB
    * - :ref:`board_nordicnrf52_nrf52840_dk`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_nrf52840_dk_adafruit`
      - On-board
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB

PHYTEC
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_reel_board`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_reel_board_v2`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB

Particle
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_particle_argon`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_particle_boron`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_particle_xenon`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB

Raytac
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_raytac_mdbt50q_rx`
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

Ruuvi
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_ruuvitag`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

Sigma Delta Technologies
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_sdt52832b`
      - External
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
    * - :ref:`board_nordicnrf52_vbluno52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

decaWave
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_dwm1001_dev`
      - On-board
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
    * - :ref:`board_nordicnrf52_ublox_bmd345eval_nrf52840`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_ublox_evk_nina_b1`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
