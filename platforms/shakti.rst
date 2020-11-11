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

.. _platform_shakti:

Shakti
======

:Configuration:
  :ref:`projectconf_env_platform` = ``shakti``

Shakti is an open-source initiative by the RISE group at IIT-Madras, which is not only building open source, production grade processors, but also associated components like interconnect fabrics, verification tools, storage controllers, peripheral IPs and SOC tools.

For more detailed information please visit `vendor site <https://shakti.org.in/?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Shakti development platform repository <https://github.com/platformio/platform-shakti/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `shakti-sdk_gpio-keypad <https://github.com/platformio/platform-shakti/tree/master/examples/shakti-sdk_gpio-keypad?utm_source=platformio.org&utm_medium=docs>`_
* `shakti-sdk_i2c-lm75 <https://github.com/platformio/platform-shakti/tree/master/examples/shakti-sdk_i2c-lm75?utm_source=platformio.org&utm_medium=docs>`_
* `shakti-sdk_uart-hello <https://github.com/platformio/platform-shakti/tree/master/examples/shakti-sdk_uart-hello?utm_source=platformio.org&utm_medium=docs>`_
* `shakti-sdk_weatherstation <https://github.com/platformio/platform-shakti/tree/master/examples/shakti-sdk_weatherstation?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_shakti_artix7_35t`
      - E-CLASS
      - 50MHz
      - 0B
      - 128KB
    * - :ref:`board_shakti_artix7_100t`
      - C-CLASS
      - 50MHz
      - 0B
      - 128MB
    * - :ref:`board_shakti_parashu`
      - E-CLASS
      - 50MHz
      - 0B
      - 128KB
    * - :ref:`board_shakti_pinaka`
      - E-CLASS
      - 50MHz
      - 0B
      - 128KB
    * - :ref:`board_shakti_vajra`
      - C-CLASS
      - 50MHz
      - 0B
      - 128MB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-shakti/releases>`__
of Shakti development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = shakti
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = shakti@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-shakti.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-shakti-sdk <https://gitlab.com/shaktiproject/software/shakti-sdk.git?utm_source=platformio.org&utm_medium=docs>`__
      - A software development kit for developing applications on Shakti class of processors

    * - `tool-jlink <https://www.segger.com/downloads/jlink/?utm_source=platformio.org&utm_medium=docs>`__
      - Software and Documentation Pack for SEGGER J-Link debug probes

    * - `tool-openocd-riscv <http://openocd.org?utm_source=platformio.org&utm_medium=docs>`__
      - Fork of Open On-Chip Debugger that has RISC-V support

    * - `tool-qemu-riscv <https://www.qemu.org?utm_source=platformio.org&utm_medium=docs>`__
      - QEMU is a generic and open source machine emulator and virtualizer

    * - `toolchain-riscv <https://github.com/riscv/riscv-gnu-toolchain.git?utm_source=platformio.org&utm_medium=docs>`__
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

    * - :ref:`framework_shakti-sdk`
      - A software development kit for developing applications on Shakti class of processors

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

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
    * - :ref:`board_shakti_artix7_35t`
      - On-board
      - E-CLASS
      - 50MHz
      - 0B
      - 128KB
    * - :ref:`board_shakti_artix7_100t`
      - On-board
      - C-CLASS
      - 50MHz
      - 0B
      - 128MB
    * - :ref:`board_shakti_parashu`
      - On-board
      - E-CLASS
      - 50MHz
      - 0B
      - 128KB
    * - :ref:`board_shakti_pinaka`
      - On-board
      - E-CLASS
      - 50MHz
      - 0B
      - 128KB
    * - :ref:`board_shakti_vajra`
      - On-board
      - C-CLASS
      - 50MHz
      - 0B
      - 128MB
