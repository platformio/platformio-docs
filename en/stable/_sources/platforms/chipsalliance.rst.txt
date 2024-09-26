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

.. _platform_chipsalliance:

CHIPS Alliance
==============

:Registry:
  `https://registry.platformio.org/platforms/platformio/chipsalliance <https://registry.platformio.org/platforms/platformio/chipsalliance>`__
:Configuration:
  :ref:`projectconf_env_platform` = ``platformio/chipsalliance``

The CHIPS Alliance develops high-quality, open source hardware designs relevant to silicon devices and FPGAs.

For more detailed information please visit `vendor site <https://chipsalliance.org?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `CHIPS Alliance development platform repository <https://github.com/platformio/platform-chipsalliance/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `native-bare_c <https://github.com/platformio/platform-chipsalliance/tree/master/examples/native-bare_c?utm_source=platformio.org&utm_medium=docs>`_
* `rtosal-freertos <https://github.com/platformio/platform-chipsalliance/tree/master/examples/rtosal-freertos?utm_source=platformio.org&utm_medium=docs>`_
* `native-asm <https://github.com/platformio/platform-chipsalliance/tree/master/examples/native-asm?utm_source=platformio.org&utm_medium=docs>`_
* `psp-hello-world <https://github.com/platformio/platform-chipsalliance/tree/master/examples/psp-hello-world?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_chipsalliance_swervolf_nexys`
      - 
      - 320MHz
      - 16MB
      - 1.16MB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-chipsalliance/releases>`__
of CHIPS Alliance development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version, NOT recommended
    ; Pin the version as shown below
    [env:latest_stable]
    platform = chipsalliance
    board = ...

    ; Specific version
    [env:custom_stable]
    platform = chipsalliance@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-chipsalliance.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-wd-riscv-sdk <https://registry.platformio.org/tools/platformio/framework-wd-riscv-sdk>`__
      - The WD Firmware package contains Firmware applications and Processor Support Package (PSP) for various cores, alongside demos which support all features.

    * - `tool-openocd-riscv-chipsalliance <https://registry.platformio.org/tools/platformio/tool-openocd-riscv-chipsalliance>`__
      - Fork of Open On-Chip Debugger that has RISC-V support and enabled VPI JTAG

    * - `tool-verilator-swervolf <https://registry.platformio.org/tools/platformio/tool-verilator-swervolf>`__
      - Verilator is an open-source SystemVerilog simulator and lint system

    * - `tool-whisper <https://registry.platformio.org/tools/platformio/tool-whisper>`__
      - Whisper is a RISCV instruction set simulator (ISS) developed for the verification of the Swerv micro-controller. It allows the user to run RISC-V code without RISC-V hardware

    * - `toolchain-riscv <https://registry.platformio.org/tools/platformio/toolchain-riscv>`__
      - GNU toolchain for RISC-V, including GCC

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

    * - :ref:`framework_freertos`
      - FreeRTOS is a real-time operating system kernel for embedded devices that has been ported to 40 microcontroller platforms.

    * - :ref:`framework_wd-riscv-sdk`
      - The WD Firmware package contains Firmware applications and Processor Support Package (PSP) for various cores, alongside demos which support all features.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

Digilent
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_chipsalliance_swervolf_nexys`
      - On-board
      - 
      - 320MHz
      - 16MB
      - 1.16MB
