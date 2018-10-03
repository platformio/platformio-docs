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

.. _platform_freescalekinetis:

Freescale Kinetis
=================

:Configuration:
  :ref:`projectconf_env_platform` = ``freescalekinetis``

Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

For more detailed information please visit `vendor site <http://www.freescale.com/webapp/sps/site/homepage.jsp?code=KINETIS&utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Freescale Kinetis development platform repository <https://github.com/platformio/platform-freescalekinetis/tree/master/examples?utm_source=platformio&utm_medium=docs>`_:

* `mbed-blink <https://github.com/platformio/platform-freescalekinetis/tree/master/examples/mbed-blink?utm_source=platformio&utm_medium=docs>`_
* `mbed-dsp <https://github.com/platformio/platform-freescalekinetis/tree/master/examples/mbed-dsp?utm_source=platformio&utm_medium=docs>`_
* `mbed-events <https://github.com/platformio/platform-freescalekinetis/tree/master/examples/mbed-events?utm_source=platformio&utm_medium=docs>`_
* `mbed-rtos <https://github.com/platformio/platform-freescalekinetis/tree/master/examples/mbed-rtos?utm_source=platformio&utm_medium=docs>`_
* `mbed-rtos-ethernet <https://github.com/platformio/platform-freescalekinetis/tree/master/examples/mbed-rtos-ethernet?utm_source=platformio&utm_medium=docs>`_
* `mbed-serial <https://github.com/platformio/platform-freescalekinetis/tree/master/examples/mbed-serial?utm_source=platformio&utm_medium=docs>`_

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
    * - :ref:`board_freescalekinetis_IBMEthernetKit`
      - MK64FN1M0VLL12
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_freescalekinetis_frdm_k20d50m`
      - MK20DX128VLH5
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_freescalekinetis_frdm_k22f`
      - MK22FN512VLH12
      - 120MHz
      - 512KB
      - 128KB
    * - :ref:`board_freescalekinetis_frdm_k64f`
      - MK64FN1M0VLL12
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_freescalekinetis_frdm_k66f`
      - MK66FN2M0VMD18
      - 180MHz
      - 2MB
      - 256KB
    * - :ref:`board_freescalekinetis_frdm_k82f`
      - MK82FN256VLL15
      - 150MHz
      - 256KB
      - 256KB
    * - :ref:`board_freescalekinetis_frdm_kl05z`
      - MKL05Z32VFM4
      - 48MHz
      - 32KB
      - 4KB
    * - :ref:`board_freescalekinetis_frdm_kl25z`
      - MKL25Z128VLK4
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_freescalekinetis_frdm_kl26z`
      - MKL26Z128VLH4
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_freescalekinetis_frdm_kl27z`
      - MKL27Z64VLH4
      - 48MHz
      - 64KB
      - 16KB
    * - :ref:`board_freescalekinetis_frdm_kl43z`
      - MKL43Z256VLH4
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_freescalekinetis_frdm_kl46z`
      - MKL46Z256VLL4
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_freescalekinetis_frdm_kw41z`
      - MKW41Z512VHT4
      - 48MHz
      - 512KB
      - 128KB


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
    * - :ref:`board_freescalekinetis_frdm_kl82z`
      - MKL82Z128VLK7
      - 96MHz
      - 128KB
      - 96KB
    * - :ref:`board_freescalekinetis_frdm_kw24d`
      - MKW24D512
      - 50MHz
      - 512KB
      - 64KB
    * - :ref:`board_freescalekinetis_hexiwear`
      - MK64FN1M0VDC12
      - 120MHz
      - 1MB
      - 256KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-freescalekinetis/releases>`__
of Freescale Kinetis development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = freescalekinetis
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = freescalekinetis@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-freescalekinetis.git
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

Freescale
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_freescalekinetis_IBMEthernetKit`
      - Yes
      - MK64FN1M0VLL12
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_freescalekinetis_frdm_k20d50m`
      - Yes
      - MK20DX128VLH5
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_freescalekinetis_frdm_k22f`
      - Yes
      - MK22FN512VLH12
      - 120MHz
      - 512KB
      - 128KB
    * - :ref:`board_freescalekinetis_frdm_k64f`
      - Yes
      - MK64FN1M0VLL12
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_freescalekinetis_frdm_k66f`
      - Yes
      - MK66FN2M0VMD18
      - 180MHz
      - 2MB
      - 256KB
    * - :ref:`board_freescalekinetis_frdm_k82f`
      - Yes
      - MK82FN256VLL15
      - 150MHz
      - 256KB
      - 256KB
    * - :ref:`board_freescalekinetis_frdm_kl05z`
      - Yes
      - MKL05Z32VFM4
      - 48MHz
      - 32KB
      - 4KB
    * - :ref:`board_freescalekinetis_frdm_kl25z`
      - Yes
      - MKL25Z128VLK4
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_freescalekinetis_frdm_kl26z`
      - Yes
      - MKL26Z128VLH4
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_freescalekinetis_frdm_kl27z`
      - Yes
      - MKL27Z64VLH4
      - 48MHz
      - 64KB
      - 16KB
    * - :ref:`board_freescalekinetis_frdm_kl43z`
      - Yes
      - MKL43Z256VLH4
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_freescalekinetis_frdm_kl46z`
      - Yes
      - MKL46Z256VLL4
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_freescalekinetis_frdm_kl82z`
      - Yes :sup:`?`
      - MKL82Z128VLK7
      - 96MHz
      - 128KB
      - 96KB
    * - :ref:`board_freescalekinetis_frdm_kw24d`
      - Yes :sup:`?`
      - MKW24D512
      - 50MHz
      - 512KB
      - 64KB
    * - :ref:`board_freescalekinetis_frdm_kw41z`
      - Yes
      - MKW41Z512VHT4
      - 48MHz
      - 512KB
      - 128KB

MikroElektronika
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_freescalekinetis_hexiwear`
      - Yes :sup:`?`
      - MK64FN1M0VDC12
      - 120MHz
      - 1MB
      - 256KB
