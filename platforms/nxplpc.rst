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

.. _platform_nxplpc:

NXP LPC
=======

:Configuration:
  :ref:`projectconf_env_platform` = ``nxplpc``

The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

For more detailed information please visit `vendor site <http://www.nxp.com/products/microcontrollers/?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `NXP LPC development platform repository <https://github.com/platformio/platform-nxplpc/tree/master/examples?utm_source=platformio&utm_medium=docs>`_:

* `mbed-blink <https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-blink?utm_source=platformio&utm_medium=docs>`_
* `mbed-dsp <https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-dsp?utm_source=platformio&utm_medium=docs>`_
* `mbed-events <https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-events?utm_source=platformio&utm_medium=docs>`_
* `mbed-http-client <https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-http-client?utm_source=platformio&utm_medium=docs>`_
* `mbed-rtos <https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-rtos?utm_source=platformio&utm_medium=docs>`_
* `mbed-rtos-ethernet <https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-rtos-ethernet?utm_source=platformio&utm_medium=docs>`_
* `mbed-serial <https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-serial?utm_source=platformio&utm_medium=docs>`_

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
    * - :ref:`board_nxplpc_lpc11u24_301`
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc4330_m4`
      - LPC4330
      - 204MHz
      - 8MB
      - 264KB
    * - :ref:`board_nxplpc_elektor_cocorico`
      - LPC812
      - 30MHz
      - 16KB
      - 4KB
    * - :ref:`board_nxplpc_lpc4088_dm`
      - LPC4088
      - 120MHz
      - 512KB
      - 96KB
    * - :ref:`board_nxplpc_lpc4088`
      - LPC4088
      - 120MHz
      - 512KB
      - 96KB
    * - :ref:`board_nxplpc_lpc11u68`
      - LPC11U68
      - 50MHz
      - 256KB
      - 36KB
    * - :ref:`board_nxplpc_lpc824`
      - LPC824
      - 30MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc812`
      - LPC812
      - 30MHz
      - 16KB
      - 4KB
    * - :ref:`board_nxplpc_lpc54114`
      - LPC54114J256BD64
      - 100MHz
      - 256KB
      - 192KB
    * - :ref:`board_nxplpc_lpc546xx`
      - LPC54608ET512
      - 180MHz
      - 512KB
      - 200KB
    * - :ref:`board_nxplpc_lpc11u24`
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc1768`
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB
    * - :ref:`board_nxplpc_seeedArchPro`
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB
    * - :ref:`board_nxplpc_lpc1114fn28`
      - LPC1114FN28
      - 48MHz
      - 32KB
      - 4KB
    * - :ref:`board_nxplpc_ssci824`
      - LPC824
      - 30MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_ubloxc027`
      - LPC1768
      - 96MHz
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
    * - :ref:`board_nxplpc_lpc11u35_501`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
    * - :ref:`board_nxplpc_lpc1347`
      - LPC1347
      - 72MHz
      - 64KB
      - 12KB
    * - :ref:`board_nxplpc_lpc11u35`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
    * - :ref:`board_nxplpc_blueboard_lpc11u24`
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11c24`
      - LPC11C24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11u34_421`
      - LPC11U34
      - 48MHz
      - 40KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11u37_501`
      - LPC11U37
      - 48MHz
      - 128KB
      - 10KB
    * - :ref:`board_nxplpc_lpc1549`
      - LPC1549
      - 72MHz
      - 256KB
      - 36KB
    * - :ref:`board_nxplpc_dipcortexm0`
      - LPC11U24
      - 50MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11u35_y5_mbug`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-nxplpc/releases>`__
of NXP LPC development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = nxplpc
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = nxplpc@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-nxplpc.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-mbed <http://mbed.org?utm_source=platformio&utm_medium=docs>`__
      - mbed Framework

    * - `tool-jlink <https://www.segger.com/downloads/jlink/?utm_source=platformio&utm_medium=docs>`__
      - SEGGER J-Link Software and Documentation Pack

    * - `tool-openocd <http://openocd.org?utm_source=platformio&utm_medium=docs>`__
      - OpenOCD

    * - `tool-pyocd <https://github.com/mbedmicro/pyOCD?utm_source=platformio&utm_medium=docs>`__
      - Open source python library for programming and debugging ARM Cortex-M microcontrollers using CMSIS-DAP

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

    * - :ref:`framework_mbed`
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

AppNearMe
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_micronfcboard`
      - No
      - LPC11U34
      - 48MHz
      - 48KB
      - 10KB

CQ Publishing
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc11u35_501`
      - Yes :sup:`?`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB

Elektor Labs
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_elektor_cocorico`
      - Yes
      - LPC812
      - 30MHz
      - 16KB
      - 4KB

Embedded Artists
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc11u35`
      - Yes :sup:`?`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
    * - :ref:`board_nxplpc_lpc4088_dm`
      - Yes
      - LPC4088
      - 120MHz
      - 512KB
      - 96KB
    * - :ref:`board_nxplpc_lpc4088`
      - Yes
      - LPC4088
      - 120MHz
      - 512KB
      - 96KB

GHI Electronics
~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_oc_mbuino`
      - No
      - LPC11U24
      - 50MHz
      - 32KB
      - 10KB

Micromint
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc4330_m4`
      - Yes
      - LPC4330
      - 204MHz
      - 8MB
      - 264KB

NGX Technologies
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_blueboard_lpc11u24`
      - Yes :sup:`?`
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB

NXP
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc11u24_301`
      - Yes
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11u68`
      - Yes
      - LPC11U68
      - 50MHz
      - 256KB
      - 36KB
    * - :ref:`board_nxplpc_lpc824`
      - Yes
      - LPC824
      - 30MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11c24`
      - Yes :sup:`?`
      - LPC11C24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11u34_421`
      - Yes :sup:`?`
      - LPC11U34
      - 48MHz
      - 40KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11u37_501`
      - Yes :sup:`?`
      - LPC11U37
      - 48MHz
      - 128KB
      - 10KB
    * - :ref:`board_nxplpc_lpc812`
      - Yes
      - LPC812
      - 30MHz
      - 16KB
      - 4KB
    * - :ref:`board_nxplpc_lpc1549`
      - Yes :sup:`?`
      - LPC1549
      - 72MHz
      - 256KB
      - 36KB
    * - :ref:`board_nxplpc_lpc54114`
      - Yes
      - LPC54114J256BD64
      - 100MHz
      - 256KB
      - 192KB
    * - :ref:`board_nxplpc_lpc546xx`
      - Yes
      - LPC54608ET512
      - 180MHz
      - 512KB
      - 200KB
    * - :ref:`board_nxplpc_lpc11u24`
      - Yes
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc1768`
      - Yes
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB

Outrageous Circuits
~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_mbuino`
      - No
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB

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
    * - :ref:`board_nxplpc_seeedArchGPRS`
      - No
      - LPC11U37
      - 48MHz
      - 128KB
      - 10KB
    * - :ref:`board_nxplpc_seeedArchPro`
      - Yes
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB
    * - :ref:`board_nxplpc_xadow_m0`
      - No
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB

Smeshlink
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_xbed_lpc1768`
      - No
      - LPC1768
      - 96MHz
      - 512KB
      - 32KB

Solder Splash Labs
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc1347`
      - Yes :sup:`?`
      - LPC1347
      - 72MHz
      - 64KB
      - 12KB
    * - :ref:`board_nxplpc_dipcortexm0`
      - Yes :sup:`?`
      - LPC11U24
      - 50MHz
      - 32KB
      - 8KB

Switch Science
~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc1114fn28`
      - Yes
      - LPC1114FN28
      - 48MHz
      - 32KB
      - 4KB
    * - :ref:`board_nxplpc_ssci824`
      - Yes
      - LPC824
      - 30MHz
      - 32KB
      - 8KB

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
    * - :ref:`board_nxplpc_ubloxc027`
      - Yes
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB

y5 design
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc11u35_y5_mbug`
      - Yes :sup:`?`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
