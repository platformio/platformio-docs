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

.. _platform_riscv_gap:

RISC-V GAP
==========

:Configuration:
  :ref:`projectconf_env_platform` = ``riscv_gap``

GreenWaves GAP8 IoT application processor enables the cost-effective development, deployment and autonomous operation of intelligent sensing devices that capture, analyze, classify and act on the fusion of rich data sources such as images, sounds or vibrations.

For more detailed information please visit `vendor site <https://greenwaves-technologies.com/en/gap8-product/?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: riscv_gap_extra.rst

Examples
--------

Examples are listed from `RISC-V GAP development platform repository <https://github.com/platformio/platform-riscv_gap/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `gapuino-mbed-os-irq <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-mbed-os-irq?utm_source=platformio.org&utm_medium=docs>`_
* `gapuino-mbed-autotiler-cifar10 <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-mbed-autotiler-cifar10?utm_source=platformio.org&utm_medium=docs>`_
* `gapuino-mbed-driver-hyper-flash <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-mbed-driver-hyper-flash?utm_source=platformio.org&utm_medium=docs>`_
* `gapuino-pulp-os-i2c-eeprom <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-pulp-os-i2c-eeprom?utm_source=platformio.org&utm_medium=docs>`_
* `gapuino-mbed-events-queue <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-mbed-events-queue?utm_source=platformio.org&utm_medium=docs>`_
* `gapuino-pulp-os-kernel-dma <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-pulp-os-kernel-dma?utm_source=platformio.org&utm_medium=docs>`_
* `gapuino-mbed-driver-hyper-rtc-alarm <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-mbed-driver-hyper-rtc-alarm?utm_source=platformio.org&utm_medium=docs>`_
* `gapuino-mbed-fft2d <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-mbed-fft2d?utm_source=platformio.org&utm_medium=docs>`_
* `gapuino-pulp-os-autotiler-bilinear-resize <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-pulp-os-autotiler-bilinear-resize?utm_source=platformio.org&utm_medium=docs>`_
* `gapuino-mbed-matadd <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-mbed-matadd?utm_source=platformio.org&utm_medium=docs>`_
* `gapuino-mbed-features-cluster-dma <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-mbed-features-cluster-dma?utm_source=platformio.org&utm_medium=docs>`_
* `gapuino-mbed-features-filesystem <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-mbed-features-filesystem?utm_source=platformio.org&utm_medium=docs>`_
* `gapuino-pulp-os-filesystem <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-pulp-os-filesystem?utm_source=platformio.org&utm_medium=docs>`_
* `gapuino-mbed-os-memory-pool <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-mbed-os-memory-pool?utm_source=platformio.org&utm_medium=docs>`_
* `gapuino-pulp-os-autotiler-cifar10 <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-pulp-os-autotiler-cifar10?utm_source=platformio.org&utm_medium=docs>`_
* `gapuino-mbed-driver-cpp-raw-serial <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-mbed-driver-cpp-raw-serial?utm_source=platformio.org&utm_medium=docs>`_
* `gapuino-pulp-os-hello-world <https://github.com/platformio/platform-riscv_gap/tree/master/examples/gapuino-pulp-os-hello-world?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_riscv_gap_gapuino`
      - GAP8
      - 250MHz
      - 64MB
      - 8MB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-riscv_gap/releases>`__
of RISC-V GAP development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = riscv_gap
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = riscv_gap@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-riscv_gap.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-gap_sdk <https://github.com/GreenWaves-Technologies/gap_sdk.git?utm_source=platformio.org&utm_medium=docs>`__
      - SDK for Greenwaves Technologies' GAP8 IoT Application Processor

    * - `tool-pulp_tools <https://github.com/GreenWaves-Technologies/pulp_tools.git?utm_source=platformio.org&utm_medium=docs>`__
      - Top project for building PULP development tools

    * - `toolchain-riscv-pulp <https://www.embecosm.com/resources/tool-chain-downloads/?utm_source=platformio.org&utm_medium=docs#pulp>`__
      - GNU toolchain for RISC-V (PULP platform)

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
      - Arm Mbed OS is an open source embedded operating system designed specifically for the 'things' in the Internet of Things. It includes all the features you need to develop a connected product based on an Arm Cortex-M microcontroller, including security, connectivity, an RTOS and drivers for sensors and I/O devices

    * - :ref:`framework_pulp-os`
      - PULP is a silicon-proven Parallel Ultra Low Power platform targeting high energy efficiencies. The platform is organized in clusters of RISC-V cores that share a tightly-coupled data memory

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

GreenWaves Technologies
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_riscv_gap_gapuino`
      - On-board
      - GAP8
      - 250MHz
      - 64MB
      - 8MB
