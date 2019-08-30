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

.. _platform_sifive:

SiFive
======

:Configuration:
  :ref:`projectconf_env_platform` = ``sifive``

SiFive brings the power of open source and software automation to the semiconductor industry, making it possible to develop new hardware faster and more affordably than ever before. 

For more detailed information please visit `vendor site <https://sifive.com?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `SiFive development platform repository <https://github.com/platformio/platform-sifive/tree/master/examples?utm_source=platformio&utm_medium=docs>`_:

* `freedom-e-sdk_hello <https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_hello?utm_source=platformio&utm_medium=docs>`_
* `freedom-e-sdk_multicore-hello <https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_multicore-hello?utm_source=platformio&utm_medium=docs>`_
* `freedom-e-sdk_sifive-welcome <https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_sifive-welcome?utm_source=platformio&utm_medium=docs>`_
* `freedom-e-sdk_spi <https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_spi?utm_source=platformio&utm_medium=docs>`_
* `freedom-e-sdk_test-coreip <https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_test-coreip?utm_source=platformio&utm_medium=docs>`_
* `freedom-e-sdk_timer-interrupt <https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_timer-interrupt?utm_source=platformio&utm_medium=docs>`_
* `freedom-e-sdk_user-mode <https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_user-mode?utm_source=platformio&utm_medium=docs>`_
* `freedom-e-sdk_user-syscall <https://github.com/platformio/platform-sifive/tree/master/examples/freedom-e-sdk_user-syscall?utm_source=platformio&utm_medium=docs>`_
* `native-blink_asm <https://github.com/platformio/platform-sifive/tree/master/examples/native-blink_asm?utm_source=platformio&utm_medium=docs>`_

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
    * - :ref:`board_sifive_e310-arty`
      - FE310
      - 450MHz
      - 16MB
      - 256MB
    * - :ref:`board_sifive_hifive-unleashed`
      - FU540
      - 1500MHz
      - 32MB
      - 8GB
    * - :ref:`board_sifive_hifive1`
      - FE310
      - 320MHz
      - 16MB
      - 16KB
    * - :ref:`board_sifive_hifive1-revb`
      - FE310
      - 320MHz
      - 16MB
      - 16KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-sifive/releases>`__
of SiFive development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = sifive
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = sifive@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-sifive.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-freedom-e-sdk <https://github.com/sifive/freedom-e-sdk?utm_source=platformio&utm_medium=docs>`__
      - Open Source Software for Developing on the SiFive Freedom E Platform

    * - `tool-jlink <https://www.segger.com/downloads/jlink/?utm_source=platformio&utm_medium=docs>`__
      - SEGGER J-Link Software and Documentation Pack

    * - `tool-openocd-riscv <https://github.com/riscv/riscv-openocd?utm_source=platformio&utm_medium=docs>`__
      - OpenOCD for RISC-V

    * - `tool-qemu-riscv <https://www.qemu.org/?utm_source=platformio&utm_medium=docs>`__
      - Open source machine emulator and virtualizer

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

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_sifive_hifive-unleashed`
      - On-board
      - FU540
      - 1500MHz
      - 32MB
      - 8GB
    * - :ref:`board_sifive_hifive1`
      - On-board
      - FE310
      - 320MHz
      - 16MB
      - 16KB
    * - :ref:`board_sifive_hifive1-revb`
      - On-board
      - FE310
      - 320MHz
      - 16MB
      - 16KB

Xilinx
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_sifive_e310-arty`
      - On-board
      - FE310
      - 450MHz
      - 16MB
      - 256MB
