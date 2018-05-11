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

.. _platform_riscv:

RISC-V
======
:ref:`projectconf_env_platform` = ``riscv``

RISC-V is an open, free ISA enabling a new era of processor innovation through open standard collaboration. Born in academia and research, RISC-V ISA delivers a new level of free, extensible software and hardware freedom on architecture, paving the way for the next 50 years of computing design and innovation.

For more detailed information please visit `vendor site <https://riscv.org?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `RISC-V development platform repository <https://github.com/platformio/platform-riscv/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_:

* `freedom-e-sdk_asm <https://github.com/platformio/platform-riscv/tree/develop/examples/freedom-e-sdk_asm?utm_source=platformio&utm_medium=docs>`_
* `freedom-e-sdk_dhrystone <https://github.com/platformio/platform-riscv/tree/develop/examples/freedom-e-sdk_dhrystone?utm_source=platformio&utm_medium=docs>`_
* `freedom-e-sdk_gpio <https://github.com/platformio/platform-riscv/tree/develop/examples/freedom-e-sdk_gpio?utm_source=platformio&utm_medium=docs>`_
* `freedom-e-sdk_hello <https://github.com/platformio/platform-riscv/tree/develop/examples/freedom-e-sdk_hello?utm_source=platformio&utm_medium=docs>`_
* `freedom-e-sdk_smp <https://github.com/platformio/platform-riscv/tree/develop/examples/freedom-e-sdk_smp?utm_source=platformio&utm_medium=docs>`_

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

Supported debugging tools are listed in "Debug" column. For more detailed
information, please scroll table by horizontal.
You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` options.


On-Board tools
~~~~~~~~~~~~~~

Boards listed below have on-board debugging tools and **ARE READY** for debugging!
You do not need to use/buy external debugger.


.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``freedom-e300-hifive1``
      - `HiFive1 <https://www.sifive.com/products/hifive1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_ft2232h` (on-board)
      - FE310
      - 320MHz
      - 16MB
      - 16KB


External tools
~~~~~~~~~~~~~~

Boards listed below are compatible with :ref:`piodebug` but depend on external
debugging tools. See "Debug" column for compatible debugging tools.


.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``coreplexip-e31-arty``
      - `Freedom E310 Arty (Artix-7) FPGA Dev Kit <http://www.xilinx.com/products/boards-and-kits/arty.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - E31
      - 320MHz
      - 16MB
      - 256MB
    * - ``coreplexip-e51-arty``
      - `E51 Arty (Artix-7) FPGA Dev Kit <http://www.xilinx.com/products/boards-and-kits/arty.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - E51
      - 1500MHz
      - 16MB
      - 256MB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-riscv/releases>`__
of RISC-V development platform and the latest upstream version using
:ref:`projectconf_env_platform` option as described below:

.. code-block:: ini

    ; Custom stable version
    [env:stable]
    platform =riscv@x.y.z
    board = ...
    ...

    ; The latest upstream/development version
    [env:upstream]
    platform = https://github.com/platformio/platform-riscv.git
    board = ...
    ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-freedom-e-sdk <https://github.com/sifive/freedom-e-sdk?utm_source=platformio&utm_medium=docs>`__
      - Open Source Software for Developing on the SiFive Freedom E Platform

    * - `tool-openocd <http://openocd.org?utm_source=platformio&utm_medium=docs>`__
      - OpenOCD

    * - `toolchain-riscv <https://github.com/riscv/riscv-gnu-toolchain?utm_source=platformio&utm_medium=docs>`__
      - GNU toolchain for RISC-V, including GCC

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

    * - :ref:`framework_freedom-e-sdk`
      - Open Source Software for Developing on the SiFive Freedom E Platform

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

SiFive
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``freedom-e300-hifive1``
      - `HiFive1 <https://www.sifive.com/products/hifive1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - FE310
      - 320MHz
      - 16MB
      - 16KB

Xilinx
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``coreplexip-e31-arty``
      - `Freedom E310 Arty (Artix-7) FPGA Dev Kit <http://www.xilinx.com/products/boards-and-kits/arty.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - E31
      - 320MHz
      - 16MB
      - 256MB
    * - ``coreplexip-e51-arty``
      - `E51 Arty (Artix-7) FPGA Dev Kit <http://www.xilinx.com/products/boards-and-kits/arty.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - E51
      - 1500MHz
      - 16MB
      - 256MB
