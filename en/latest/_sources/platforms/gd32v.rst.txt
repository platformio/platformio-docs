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

.. _platform_gd32v:

GigaDevice GD32V
================

:Configuration:
  :ref:`projectconf_env_platform` = ``gd32v``

The GigaDevice GD32V device is a 32-bit general-purpose microcontroller based on the RISC-V core with an impressive balance of processing power, reduced power consumption and peripheral set.

For more detailed information please visit `vendor site <https://www.gigadevice.com/products/microcontrollers/gd32/risc-v/?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `GigaDevice GD32V development platform repository <https://github.com/sipeed/platform-gd32v/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `eval-blink <https://github.com/sipeed/platform-gd32v/tree/master/examples/eval-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-blink <https://github.com/sipeed/platform-gd32v/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `longan-nano-blink <https://github.com/sipeed/platform-gd32v/tree/master/examples/longan-nano-blink?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_gd32v_gd32vf103v-eval`
      - GD32VF103VBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_gd32v_sipeed-longan-nano`
      - GD32VF103CBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_gd32v_sipeed-longan-nano-lite`
      - GD32VF103C8T6
      - 108MHz
      - 64KB
      - 20KB
    * - :ref:`board_gd32v_wio_lite_risc-v`
      - GD32VF103CBT6
      - 108MHz
      - 128KB
      - 32KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/sipeed/platform-gd32v/releases>`__
of GigaDevice GD32V development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = gd32v
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = gd32v@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/sipeed/platform-gd32v.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduino-gd32v <https://github.com/sipeed/Maixduino.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for GigaDevice GD32V microcontrollers

    * - `framework-gd32vf103-sdk <https://www.riscv-mcu.com/?utm_source=platformio.org&utm_medium=docs>`__
      - GigaDevice GD32VF103 Firmware Library

    * - `tool-dfuutil <http://dfu-util.sourceforge.net/?utm_source=platformio.org&utm_medium=docs>`__
      - Device Firmware Upgrade Utilities

    * - `tool-gd32vflash <https://github.com/riscv-mcu/gd32-dfu-utils.git?utm_source=platformio.org&utm_medium=docs>`__
      - GigaDevice GD32V Flash tools

    * - `tool-openocd-gd32v <http://openocd.org?utm_source=platformio.org&utm_medium=docs>`__
      - Open On-Chip Debugger branch with RISC-V GigaDevice GD32V support

    * - `toolchain-gd32v <https://github.com/riscv-mcu/riscv-gnu-toolchain?utm_source=platformio.org&utm_medium=docs>`__
      - RISC-V GCC toolchain

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

    * - :ref:`framework_gd32vf103-sdk`
      - GigaDevice GD32VF103 Firmware Library (SDK) is a firmware function package, including programs, data structures and macro definitions, all the performance features of peripherals of GD32VF103 devices are involved in the package

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

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
    * - :ref:`board_gd32v_wio_lite_risc-v`
      - External
      - GD32VF103CBT6
      - 108MHz
      - 128KB
      - 32KB

Sipeed
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_gd32v_gd32vf103v-eval`
      - External
      - GD32VF103VBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_gd32v_sipeed-longan-nano`
      - External
      - GD32VF103CBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_gd32v_sipeed-longan-nano-lite`
      - External
      - GD32VF103C8T6
      - 108MHz
      - 64KB
      - 20KB
