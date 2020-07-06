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

.. _platform_intel_mcs51:

Intel MCS-51 (8051)
===================

:Configuration:
  :ref:`projectconf_env_platform` = ``intel_mcs51``

The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

For more detailed information please visit `vendor site <https://en.wikipedia.org/wiki/Intel_MCS-51?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Intel MCS-51 (8051) development platform repository <https://github.com/platformio/platform-intel_mcs51/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `stc-header <https://github.com/platformio/platform-intel_mcs51/tree/master/examples/stc-header?utm_source=platformio.org&utm_medium=docs>`_
* `native-blink <https://github.com/platformio/platform-intel_mcs51/tree/master/examples/native-blink?utm_source=platformio.org&utm_medium=docs>`_
* `stc-blink <https://github.com/platformio/platform-intel_mcs51/tree/master/examples/stc-blink?utm_source=platformio.org&utm_medium=docs>`_

Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-intel_mcs51/releases>`__
of Intel MCS-51 (8051) development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = intel_mcs51
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = intel_mcs51@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-intel_mcs51.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `tool-stcgal <https://github.com/grigorig/stcgal.git?utm_source=platformio.org&utm_medium=docs>`__
      - Open Source STC MCU ISP flash tool

    * - `toolchain-sdcc <http://sdcc.sourceforge.net?utm_source=platformio.org&utm_medium=docs>`__
      - Small Device C compiler suite

.. warning::
    **Linux Users**:

        * Install "udev" rules :ref:`faq_udev_rules`
        * Raspberry Pi users, please read this article
          `Enable serial port on Raspberry Pi <https://hallard.me/enable-serial-port-on-raspberry-pi/>`__.


    **Windows Users:**

        Please check that you have a correctly installed USB driver from board
        manufacturer


Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

Nuvoton
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_intel_mcs51_n79e8432`
      - No
      - N79E8432
      - 22MHz
      - 4KB
      - 512B
    * - :ref:`board_intel_mcs51_n79e844`
      - No
      - N79E844
      - 22MHz
      - 8KB
      - 512B
    * - :ref:`board_intel_mcs51_n79e845`
      - No
      - N79E845
      - 22MHz
      - 16KB
      - 512B
    * - :ref:`board_intel_mcs51_n79e854`
      - No
      - N79E854
      - 22MHz
      - 8KB
      - 512B
    * - :ref:`board_intel_mcs51_n79e855`
      - No
      - N79E855
      - 22MHz
      - 16KB
      - 512B

STC
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_intel_mcs51_stc15f204ea`
      - No
      - STC15F204EA
      - 11MHz
      - 4KB
      - 256B
    * - :ref:`board_intel_mcs51_stc15f2k60s2`
      - No
      - STC15F2K60S2
      - 6MHz
      - 60KB
      - 2KB
    * - :ref:`board_intel_mcs51_stc15w204s`
      - No
      - STC15W204S
      - 11MHz
      - 4KB
      - 256B
    * - :ref:`board_intel_mcs51_stc15w404as`
      - No
      - STC15W404AS
      - 11MHz
      - 4KB
      - 512B
    * - :ref:`board_intel_mcs51_stc15w408as`
      - No
      - STC15W408AS
      - 11MHz
      - 8KB
      - 512B
    * - :ref:`board_intel_mcs51_stc89c52rc`
      - No
      - STC89C52RC
      - 11MHz
      - 8KB
      - 512B
