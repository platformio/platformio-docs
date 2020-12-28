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

.. _platform_nuclei:

Nuclei
======

:Configuration:
  :ref:`projectconf_env_platform` = ``nuclei``

Find professional RISC-V Processor IP in Nuclei, first professional RISC-V IP company in Mainland China, match all your requirements in AIoT Era.

For more detailed information please visit `vendor site <https://nucleisys.com/?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Nuclei development platform repository <https://github.com/Nuclei-Software/platform-nuclei/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `freertos_demo <https://github.com/Nuclei-Software/platform-nuclei/tree/master/examples/freertos_demo?utm_source=platformio.org&utm_medium=docs>`_
* `rtthread_demo <https://github.com/Nuclei-Software/platform-nuclei/tree/master/examples/rtthread_demo?utm_source=platformio.org&utm_medium=docs>`_
* `demo_dsp <https://github.com/Nuclei-Software/platform-nuclei/tree/master/examples/demo_dsp?utm_source=platformio.org&utm_medium=docs>`_
* `helloworld <https://github.com/Nuclei-Software/platform-nuclei/tree/master/examples/helloworld?utm_source=platformio.org&utm_medium=docs>`_
* `dhrystone <https://github.com/Nuclei-Software/platform-nuclei/tree/master/examples/dhrystone?utm_source=platformio.org&utm_medium=docs>`_
* `whetstone <https://github.com/Nuclei-Software/platform-nuclei/tree/master/examples/whetstone?utm_source=platformio.org&utm_medium=docs>`_
* `demo_eclic <https://github.com/Nuclei-Software/platform-nuclei/tree/master/examples/demo_eclic?utm_source=platformio.org&utm_medium=docs>`_
* `ucosii_demo <https://github.com/Nuclei-Software/platform-nuclei/tree/master/examples/ucosii_demo?utm_source=platformio.org&utm_medium=docs>`_
* `coremark <https://github.com/Nuclei-Software/platform-nuclei/tree/master/examples/coremark?utm_source=platformio.org&utm_medium=docs>`_
* `demo_timer <https://github.com/Nuclei-Software/platform-nuclei/tree/master/examples/demo_timer?utm_source=platformio.org&utm_medium=docs>`_
* `rtthread_msh <https://github.com/Nuclei-Software/platform-nuclei/tree/master/examples/rtthread_msh?utm_source=platformio.org&utm_medium=docs>`_
* `demo_nice <https://github.com/Nuclei-Software/platform-nuclei/tree/master/examples/demo_nice?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_nuclei_gd32vf103v_rvstar`
      - GD32VF103VBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_nuclei_hbird_eval`
      - HUMMINGBIRD
      - 5MHz
      - 64KB
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
    * - :ref:`board_nuclei_gd32vf103v_eval`
      - GD32VF103VBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_nuclei_gd32vf103c_longan_nano`
      - GD32VF103CBT6
      - 108MHz
      - 128KB
      - 32KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/Nuclei-Software/platform-nuclei/releases>`__
of Nuclei development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = nuclei
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = nuclei@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/Nuclei-Software/platform-nuclei.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-nuclei-sdk <https://github.com/Nuclei-Software/nuclei-sdk.git?utm_source=platformio.org&utm_medium=docs>`__
      - Nuclei N/NX Embedded Software Development Kit

    * - `tool-jlink <https://www.segger.com/downloads/jlink/?utm_source=platformio.org&utm_medium=docs>`__
      - Software and Documentation Pack for SEGGER J-Link debug probes

    * - `tool-openocd-nuclei <http://openocd.org?utm_source=platformio.org&utm_medium=docs>`__
      - Open On-Chip Debugger branch with RISC-V Nuclei support

    * - `toolchain-riscv-gcc-nuclei <https://github.com/riscv-mcu/riscv-gnu-toolchain.git?utm_source=platformio.org&utm_medium=docs>`__
      - Nuclei RISC-V GCC toolchain

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

    * - :ref:`framework_nuclei-sdk`
      - Open Source Software Development Kit for the Nuclei N/NX processors

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

GigaDevice
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nuclei_gd32vf103v_eval`
      - External
      - GD32VF103VBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_nuclei_gd32vf103c_longan_nano`
      - External
      - GD32VF103CBT6
      - 108MHz
      - 128KB
      - 32KB

Nuclei
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nuclei_gd32vf103v_rvstar`
      - On-board
      - GD32VF103VBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_nuclei_hbird_eval`
      - On-board
      - HUMMINGBIRD
      - 5MHz
      - 64KB
      - 64KB
