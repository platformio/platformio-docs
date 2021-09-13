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

.. _platform_openhw:

OpenHW Group
============

:Configuration:
  :ref:`projectconf_env_platform` = ``openhw``

OpenHW Group is a not-for-profit, global organization that provides an infrastructure for hosting high quality open-source HW developments in line with industry best practices. The OpenHW CV32E40P RISC-V core is the first open-source core for high-volume chips verified with the state-of-the-art process required for high-integrity, commercial SoCs.

For more detailed information please visit `vendor site <https://www.openhwgroup.org/?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `OpenHW Group development platform repository <https://github.com/platformio/platform-openhw/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `pulp-sdk-asm <https://github.com/platformio/platform-openhw/tree/master/examples/pulp-sdk-asm?utm_source=platformio.org&utm_medium=docs>`_
* `pulp-runtime-sort <https://github.com/platformio/platform-openhw/tree/master/examples/pulp-runtime-sort?utm_source=platformio.org&utm_medium=docs>`_
* `pulp-sdk-sort <https://github.com/platformio/platform-openhw/tree/master/examples/pulp-sdk-sort?utm_source=platformio.org&utm_medium=docs>`_
* `native-sort <https://github.com/platformio/platform-openhw/tree/master/examples/native-sort?utm_source=platformio.org&utm_medium=docs>`_
* `native-asm <https://github.com/platformio/platform-openhw/tree/master/examples/native-asm?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_openhw_nexys_a7`
      - 
      - 320MHz
      - 16MB
      - 1.16MB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-openhw/releases>`__
of OpenHW Group development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = openhw
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = openhw@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-openhw.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-pulp-runtime <https://github.com/pulp-platform/pulp-runtime.git?utm_source=platformio.org&utm_medium=docs>`__
      - Runtime Environment for Parallel Ultra Low Power platform

    * - `framework-pulp-sdk <https://github.com/pulp-platform/pulp-sdk.git?utm_source=platformio.org&utm_medium=docs>`__
      - Software Development Kit for Parallel Ultra Low Power platform

    * - `tool-openocd-riscv-pulp <http://openocd.org?utm_source=platformio.org&utm_medium=docs>`__
      - Fork of Open On-Chip Debugger that has RISC-V support for PULP platform

    * - `tool-ovpsim-corev <https://github.com/openhwgroup/riscv-ovpsim-corev.git?utm_source=platformio.org&utm_medium=docs>`__
      - Imperas RISC-V OVPsim CORE-V simulator provides a reference of the OpenHW Group CORE-V processor cores. The riscvOVPsim familiy of simulators implement the full and complete functionality of the RISC-V Foundation's public User and Privilege specifications.

    * - `tool-renode <https://renode.io?utm_source=platformio.org&utm_medium=docs>`__
      - Renode is a development framework which accelerates IoT and embedded systems development by letting you simulate physical hardware systems

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

    * - :ref:`framework_pulp-runtime`
      - Runtime Environment for Parallel Ultra Low Power platform targeting high energy efficiencies

    * - :ref:`framework_pulp-sdk`
      - Software Development Kit for Parallel Ultra Low Power platform targeting high energy efficiencies

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
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
    * - :ref:`board_openhw_nexys_a7`
      - On-board
      - 
      - 320MHz
      - 16MB
      - 1.16MB
