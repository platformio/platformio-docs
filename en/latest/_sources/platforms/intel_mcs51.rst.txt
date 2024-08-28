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

:Registry:
  `https://registry.platformio.org/platforms/platformio/intel_mcs51 <https://registry.platformio.org/platforms/platformio/intel_mcs51>`__
:Configuration:
  :ref:`projectconf_env_platform` = ``platformio/intel_mcs51``

The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

For more detailed information please visit `vendor site <https://en.wikipedia.org/wiki/Intel_MCS-51?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Intel MCS-51 (8051) development platform repository <https://github.com/platformio/platform-intel_mcs51/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `anymcu-blink <https://github.com/platformio/platform-intel_mcs51/tree/master/examples/anymcu-blink?utm_source=platformio.org&utm_medium=docs>`_
* `stc-header <https://github.com/platformio/platform-intel_mcs51/tree/master/examples/stc-header?utm_source=platformio.org&utm_medium=docs>`_
* `assembly-blink <https://github.com/platformio/platform-intel_mcs51/tree/master/examples/assembly-blink?utm_source=platformio.org&utm_medium=docs>`_
* `native-blink <https://github.com/platformio/platform-intel_mcs51/tree/master/examples/native-blink?utm_source=platformio.org&utm_medium=docs>`_
* `anymcu-header <https://github.com/platformio/platform-intel_mcs51/tree/master/examples/anymcu-header?utm_source=platformio.org&utm_medium=docs>`_
* `stc-blink <https://github.com/platformio/platform-intel_mcs51/tree/master/examples/stc-blink?utm_source=platformio.org&utm_medium=docs>`_

Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-intel_mcs51/releases>`__
of Intel MCS-51 (8051) development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version, NOT recommended
    ; Pin the version as shown below
    [env:latest_stable]
    platform = intel_mcs51
    board = ...

    ; Specific version
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

    * - `tool-stcgal <https://registry.platformio.org/tools/platformio/tool-stcgal>`__
      - Open Source STC MCU ISP flash tool

    * - `tool-vnproch55x <https://registry.platformio.org/tools/platformio/tool-vnproch55x>`__
      - CH55X Programming software

    * - `toolchain-sdcc <https://registry.platformio.org/tools/platformio/toolchain-sdcc>`__
      - Small Device C compiler suite

.. warning::
    **Linux Users**:

        * Install "udev" rules :ref:`platformio_udev_rules`
        * Raspberry Pi users, please read this article
          `Enable serial port on Raspberry Pi <https://hallard.me/enable-serial-port-on-raspberry-pi/>`__.


    **Windows Users:**

        Please check that you have a correctly installed USB driver from board
        manufacturer


Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

Intel & Licensees
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_intel_mcs51_Generic8051`
      - No
      - 8051
      - 11MHz
      - 4KB
      - 128B

Intel & licensees
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_intel_mcs51_Generic8052`
      - No
      - 8052
      - 11MHz
      - 8KB
      - 256B

Microchip & Atmel
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_intel_mcs51_AT89S51`
      - No
      - AT89S51
      - 11MHz
      - 4KB
      - 128B
    * - :ref:`board_intel_mcs51_AT89S52`
      - No
      - AT89S52
      - 11MHz
      - 8KB
      - 256B

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
    * - :ref:`board_intel_mcs51_ML51BB9AE`
      - No
      - ML51BB9AE
      - 24MHz
      - 16KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_ML51DB9AE`
      - No
      - ML51DB9AE
      - 24MHz
      - 16KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_ML51EB9AE`
      - No
      - ML51EB9AE
      - 24MHz
      - 16KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_ML51EC0AE`
      - No
      - ML51EC0AE
      - 24MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_ML51FB9AE`
      - No
      - ML51FB9AE
      - 24MHz
      - 16KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_ML51LD1AE`
      - No
      - ML51LD1AE
      - 24MHz
      - 64KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_ML51OB9AE`
      - No
      - ML51OB9AE
      - 24MHz
      - 16KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_ML51PB9AE`
      - No
      - ML51PB9AE
      - 24MHz
      - 16KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_ML51PC0AE`
      - No
      - ML51PC0AE
      - 24MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_ML51SD1AE`
      - No
      - ML51SD1AE
      - 24MHz
      - 64KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_ML51TB9AE`
      - No
      - ML51TB9AE
      - 24MHz
      - 16KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_ML51TC0AE`
      - No
      - ML51TC0AE
      - 24MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_ML51TC1AE`
      - No
      - ML51TC1AE
      - 24MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_ML51TD1AE`
      - No
      - ML51TD1AE
      - 24MHz
      - 64KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_ML51UB9AE`
      - No
      - ML51UB9AE
      - 24MHz
      - 16KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_ML51UC0AE`
      - No
      - ML51UC0AE
      - 24MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_ML51XB9AE`
      - No
      - ML51XB9AE
      - 24MHz
      - 16KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_ML54LD1AE`
      - No
      - ML54LD1AE
      - 24MHz
      - 64KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_ML54MD1AE`
      - No
      - ML54MD1AE
      - 24MHz
      - 64KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_ML54SD1AE`
      - No
      - ML54SD1AE
      - 24MHz
      - 64KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_ML56LD1AE`
      - No
      - ML56LD1AE
      - 24MHz
      - 64KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_ML56MD1AE`
      - No
      - ML56MD1AE
      - 24MHz
      - 64KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_ML56SD1AE`
      - No
      - ML56SD1AE
      - 24MHz
      - 64KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_MS51BA9AE`
      - No
      - MS51BA9AE
      - 16MHz
      - 8KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_MS51DA9AE`
      - No
      - MS51DA9AE
      - 16MHz
      - 8KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_MS51EC0AE`
      - No
      - MS51EC0AE
      - 16MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_MS51FB9AE`
      - No
      - MS51FB9AE
      - 16MHz
      - 16KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_MS51FC0AE`
      - No
      - MS51FC0AE
      - 16MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_MS51IA9AE`
      - No
      - MS51IA9AE
      - 16MHz
      - 8KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_MS51PC0AE`
      - No
      - MS51PC0AE
      - 16MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_MS51TC0AE`
      - No
      - MS51TC0AE
      - 16MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_MS51XB9AE`
      - No
      - MS51XB9AE
      - 16MHz
      - 16KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_MS51XB9BE`
      - No
      - MS51XB9BE
      - 16MHz
      - 16KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_MS51XC0BE`
      - No
      - MS51XC0BE
      - 16MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_N76E003`
      - No
      - N76E003
      - 16MHz
      - 18KB
      - 1KB
    * - :ref:`board_intel_mcs51_N76E616`
      - No
      - N76E616
      - 11MHz
      - 18KB
      - 512B
    * - :ref:`board_intel_mcs51_N76E885`
      - No
      - N76E885
      - 22MHz
      - 18KB
      - 512B
    * - :ref:`board_intel_mcs51_N78E055`
      - No
      - N78E055
      - 22MHz
      - 16KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_N78E059`
      - No
      - N78E059
      - 22MHz
      - 32KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_N78E366`
      - No
      - N78E366
      - 22MHz
      - 64KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_N78E517`
      - No
      - N78E517
      - 22MHz
      - 64KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_N79E352`
      - No
      - N79E352
      - 22MHz
      - 8KB
      - 256B
    * - :ref:`board_intel_mcs51_N79E715`
      - No
      - N79E715
      - 22MHz
      - 16KB
      - 512B
    * - :ref:`board_intel_mcs51_N79E813`
      - No
      - N79E813
      - 22MHz
      - 4KB
      - 512B
    * - :ref:`board_intel_mcs51_N79E8132`
      - No
      - N79E8132
      - 22MHz
      - 4KB
      - 512B
    * - :ref:`board_intel_mcs51_N79E814`
      - No
      - N79E814
      - 22MHz
      - 8KB
      - 512B
    * - :ref:`board_intel_mcs51_N79E815`
      - No
      - N79E815
      - 22MHz
      - 16KB
      - 512B
    * - :ref:`board_intel_mcs51_N79E822`
      - No
      - N79E822
      - 6MHz
      - 2KB
      - 256B
    * - :ref:`board_intel_mcs51_N79E823`
      - No
      - N79E823
      - 6MHz
      - 4KB
      - 256B
    * - :ref:`board_intel_mcs51_N79E824`
      - No
      - N79E824
      - 6MHz
      - 8KB
      - 256B
    * - :ref:`board_intel_mcs51_N79E825`
      - No
      - N79E825
      - 6MHz
      - 16KB
      - 256B
    * - :ref:`board_intel_mcs51_N79E843`
      - No
      - N79E843
      - 22MHz
      - 4KB
      - 512B
    * - :ref:`board_intel_mcs51_N79E8432`
      - No
      - N79E8432
      - 22MHz
      - 4KB
      - 512B
    * - :ref:`board_intel_mcs51_N79E844`
      - No
      - N79E844
      - 22MHz
      - 8KB
      - 512B
    * - :ref:`board_intel_mcs51_N79E845`
      - No
      - N79E845
      - 22MHz
      - 16KB
      - 512B
    * - :ref:`board_intel_mcs51_N79E854`
      - No
      - N79E854
      - 22MHz
      - 8KB
      - 512B
    * - :ref:`board_intel_mcs51_N79E855`
      - No
      - N79E855
      - 22MHz
      - 16KB
      - 512B
    * - :ref:`board_intel_mcs51_N79E875`
      - No
      - N79E875
      - 22MHz
      - 16KB
      - 512B
    * - :ref:`board_intel_mcs51_W79E2051`
      - No
      - W79E2051
      - 22MHz
      - 2KB
      - 256B
    * - :ref:`board_intel_mcs51_W79E4051`
      - No
      - W79E4051
      - 22MHz
      - 4KB
      - 256B
    * - :ref:`board_intel_mcs51_W79E632`
      - No
      - W79E632
      - 11MHz
      - 64KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_W79E633`
      - No
      - W79E633
      - 22MHz
      - 64KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_W79E658`
      - No
      - W79E658
      - 22MHz
      - 64KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_W79E659`
      - No
      - W79E659
      - 22MHz
      - 32KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_W79E8213`
      - No
      - W79E8213
      - 20MHz
      - 4KB
      - 128B

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
    * - :ref:`board_intel_mcs51_IAP12C5A62S2`
      - No
      - IAP12C5A62S2
      - 11MHz
      - 62KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_IAP15F106`
      - No
      - IAP15F106
      - 11MHz
      - 6KB
      - 128B
    * - :ref:`board_intel_mcs51_IAP15F206A`
      - No
      - IAP15F206A
      - 11MHz
      - 6KB
      - 256B
    * - :ref:`board_intel_mcs51_IAP15F2K61S`
      - No
      - IAP15F2K61S
      - 11MHz
      - 61KB
      - 2KB
    * - :ref:`board_intel_mcs51_IAP15F2K61S2`
      - No
      - IAP15F2K61S2
      - 11MHz
      - 61KB
      - 2KB
    * - :ref:`board_intel_mcs51_IAP15F413AD`
      - No
      - IAP15F413AD
      - 11MHz
      - 13KB
      - 512B
    * - :ref:`board_intel_mcs51_IAP15W105`
      - No
      - IAP15W105
      - 11MHz
      - 5KB
      - 128B
    * - :ref:`board_intel_mcs51_IAP15W1K29S`
      - No
      - IAP15W1K29S
      - 11MHz
      - 29KB
      - 1KB
    * - :ref:`board_intel_mcs51_IAP15W205S`
      - No
      - IAP15W205S
      - 11MHz
      - 5KB
      - 256B
    * - :ref:`board_intel_mcs51_IAP15W413AS`
      - No
      - IAP15W413AS
      - 11MHz
      - 13KB
      - 512B
    * - :ref:`board_intel_mcs51_IAP15W413S`
      - No
      - IAP15W413S
      - 11MHz
      - 13KB
      - 512B
    * - :ref:`board_intel_mcs51_IAP15W4K58S4`
      - No
      - IAP15W4K58S4
      - 11MHz
      - 58KB
      - 4KB
    * - :ref:`board_intel_mcs51_IAP15W4K61S4`
      - No
      - IAP15W4K61S4
      - 11MHz
      - 61KB
      - 4KB
    * - :ref:`board_intel_mcs51_IAP15W4K63S4`
      - No
      - IAP15W4K63S4
      - 11MHz
      - 63.50KB
      - 4KB
    * - :ref:`board_intel_mcs51_IRC15F107W`
      - No
      - IRC15F107W
      - 11MHz
      - 6KB
      - 128B
    * - :ref:`board_intel_mcs51_IRC15F2K63S2`
      - No
      - IRC15F2K63S2
      - 11MHz
      - 63.50KB
      - 2KB
    * - :ref:`board_intel_mcs51_IRC15W107`
      - No
      - IRC15W107
      - 11MHz
      - 7KB
      - 128B
    * - :ref:`board_intel_mcs51_IRC15W1K31S`
      - No
      - IRC15W1K31S
      - 11MHz
      - 31.50KB
      - 1KB
    * - :ref:`board_intel_mcs51_IRC15W207S`
      - No
      - IRC15W207S
      - 11MHz
      - 7.50KB
      - 256B
    * - :ref:`board_intel_mcs51_IRC15W415AS`
      - No
      - IRC15W415AS
      - 11MHz
      - 15.50KB
      - 512B
    * - :ref:`board_intel_mcs51_IRC15W415S`
      - No
      - IRC15W415S
      - 11MHz
      - 15.50KB
      - 512B
    * - :ref:`board_intel_mcs51_STC12C5A08S2`
      - No
      - STC12C5A08S2
      - 11MHz
      - 8KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC12C5A16S2`
      - No
      - STC12C5A16S2
      - 11MHz
      - 16KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC12C5A32S2`
      - No
      - STC12C5A32S2
      - 11MHz
      - 32KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC12C5A40S2`
      - No
      - STC12C5A40S2
      - 11MHz
      - 40KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC12C5A48S2`
      - No
      - STC12C5A48S2
      - 11MHz
      - 48KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC12C5A52S2`
      - No
      - STC12C5A52S2
      - 11MHz
      - 52KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC12C5A56S2`
      - No
      - STC12C5A56S2
      - 11MHz
      - 56KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC12C5A60S2`
      - No
      - STC12C5A60S2
      - 11MHz
      - 59.71KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC15F100`
      - No
      - STC15F100
      - 11MHz
      - 512B
      - 128B
    * - :ref:`board_intel_mcs51_STC15F100W`
      - No
      - STC15F100W
      - 11MHz
      - 512B
      - 128B
    * - :ref:`board_intel_mcs51_STC15F101`
      - No
      - STC15F101
      - 11MHz
      - 1KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15F101E`
      - No
      - STC15F101E
      - 11MHz
      - 1KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15F101W`
      - No
      - STC15F101W
      - 11MHz
      - 1KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15F102`
      - No
      - STC15F102
      - 11MHz
      - 2KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15F102E`
      - No
      - STC15F102E
      - 11MHz
      - 2KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15F102W`
      - No
      - STC15F102W
      - 11MHz
      - 2KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15F103`
      - No
      - STC15F103
      - 11MHz
      - 3KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15F103E`
      - No
      - STC15F103E
      - 11MHz
      - 3KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15F103W`
      - No
      - STC15F103W
      - 11MHz
      - 3KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15F104`
      - No
      - STC15F104
      - 11MHz
      - 4KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15F104E`
      - No
      - STC15F104E
      - 11MHz
      - 4KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15F104W`
      - No
      - STC15F104W
      - 11MHz
      - 4KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15F105`
      - No
      - STC15F105
      - 11MHz
      - 5KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15F105E`
      - No
      - STC15F105E
      - 11MHz
      - 5KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15F105W`
      - No
      - STC15F105W
      - 11MHz
      - 5KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15F201A`
      - No
      - STC15F201A
      - 11MHz
      - 1KB
      - 256B
    * - :ref:`board_intel_mcs51_STC15F201EA`
      - No
      - STC15F201EA
      - 11MHz
      - 1KB
      - 256B
    * - :ref:`board_intel_mcs51_STC15F202A`
      - No
      - STC15F202A
      - 11MHz
      - 2KB
      - 256B
    * - :ref:`board_intel_mcs51_STC15F202EA`
      - No
      - STC15F202EA
      - 11MHz
      - 2KB
      - 256B
    * - :ref:`board_intel_mcs51_STC15F203A`
      - No
      - STC15F203A
      - 11MHz
      - 3KB
      - 256B
    * - :ref:`board_intel_mcs51_STC15F203EA`
      - No
      - STC15F203EA
      - 11MHz
      - 3KB
      - 256B
    * - :ref:`board_intel_mcs51_STC15F204A`
      - No
      - STC15F204A
      - 11MHz
      - 4KB
      - 256B
    * - :ref:`board_intel_mcs51_STC15F204EA`
      - No
      - STC15F204EA
      - 11MHz
      - 4KB
      - 256B
    * - :ref:`board_intel_mcs51_STC15F205A`
      - No
      - STC15F205A
      - 11MHz
      - 5KB
      - 256B
    * - :ref:`board_intel_mcs51_STC15F205EA`
      - No
      - STC15F205EA
      - 11MHz
      - 5KB
      - 256B
    * - :ref:`board_intel_mcs51_STC15F2K08S2`
      - No
      - STC15F2K08S2
      - 11MHz
      - 8KB
      - 2KB
    * - :ref:`board_intel_mcs51_STC15F2K16S2`
      - No
      - STC15F2K16S2
      - 11MHz
      - 16KB
      - 2KB
    * - :ref:`board_intel_mcs51_STC15F2K24AS`
      - No
      - STC15F2K24AS
      - 11MHz
      - 24KB
      - 2KB
    * - :ref:`board_intel_mcs51_STC15F2K24S2`
      - No
      - STC15F2K24S2
      - 11MHz
      - 24KB
      - 2KB
    * - :ref:`board_intel_mcs51_STC15F2K32S2`
      - No
      - STC15F2K32S2
      - 11MHz
      - 32KB
      - 2KB
    * - :ref:`board_intel_mcs51_STC15F2K40S2`
      - No
      - STC15F2K40S2
      - 11MHz
      - 40KB
      - 2KB
    * - :ref:`board_intel_mcs51_STC15F2K48S2`
      - No
      - STC15F2K48S2
      - 11MHz
      - 48KB
      - 2KB
    * - :ref:`board_intel_mcs51_STC15F2K52S2`
      - No
      - STC15F2K52S2
      - 6MHz
      - 52KB
      - 2KB
    * - :ref:`board_intel_mcs51_STC15F2K56S2`
      - No
      - STC15F2K56S2
      - 11MHz
      - 56KB
      - 2KB
    * - :ref:`board_intel_mcs51_STC15F2K60S2`
      - No
      - STC15F2K60S2
      - 11MHz
      - 60KB
      - 2KB
    * - :ref:`board_intel_mcs51_STC15F408AD`
      - No
      - STC15F408AD
      - 11MHz
      - 8KB
      - 512B
    * - :ref:`board_intel_mcs51_STC15W100`
      - No
      - STC15W100
      - 11MHz
      - 512B
      - 128B
    * - :ref:`board_intel_mcs51_STC15W101`
      - No
      - STC15W101
      - 11MHz
      - 1KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15W102`
      - No
      - STC15W102
      - 11MHz
      - 2KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15W103`
      - No
      - STC15W103
      - 11MHz
      - 3KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15W104`
      - No
      - STC15W104
      - 11MHz
      - 4KB
      - 128B
    * - :ref:`board_intel_mcs51_STC15W1K16S`
      - No
      - STC15W1K16S
      - 11MHz
      - 16KB
      - 1KB
    * - :ref:`board_intel_mcs51_STC15W1K20S`
      - No
      - STC15W1K20S
      - 11MHz
      - 20KB
      - 1KB
    * - :ref:`board_intel_mcs51_STC15W1K24S`
      - No
      - STC15W1K24S
      - 11MHz
      - 24KB
      - 1KB
    * - :ref:`board_intel_mcs51_STC15W201S`
      - No
      - STC15W201S
      - 11MHz
      - 1KB
      - 256B
    * - :ref:`board_intel_mcs51_STC15W202S`
      - No
      - STC15W202S
      - 11MHz
      - 2KB
      - 256B
    * - :ref:`board_intel_mcs51_STC15W203S`
      - No
      - STC15W203S
      - 11MHz
      - 3KB
      - 256B
    * - :ref:`board_intel_mcs51_STC15W204S`
      - No
      - STC15W204S
      - 11MHz
      - 4KB
      - 256B
    * - :ref:`board_intel_mcs51_STC15W401AS`
      - No
      - STC15W401AS
      - 11MHz
      - 1KB
      - 512B
    * - :ref:`board_intel_mcs51_STC15W402AS`
      - No
      - STC15W402AS
      - 11MHz
      - 2KB
      - 512B
    * - :ref:`board_intel_mcs51_STC15W404AS`
      - No
      - STC15W404AS
      - 11MHz
      - 4KB
      - 512B
    * - :ref:`board_intel_mcs51_STC15W404S`
      - No
      - STC15W404S
      - 11MHz
      - 4KB
      - 512B
    * - :ref:`board_intel_mcs51_STC15W408AS`
      - No
      - STC15W408AS
      - 11MHz
      - 8KB
      - 512B
    * - :ref:`board_intel_mcs51_STC15W408S`
      - No
      - STC15W408S
      - 11MHz
      - 8KB
      - 512B
    * - :ref:`board_intel_mcs51_STC15W410S`
      - No
      - STC15W410S
      - 11MHz
      - 10KB
      - 512B
    * - :ref:`board_intel_mcs51_STC15W4K16S4`
      - No
      - STC15W4K16S4
      - 11MHz
      - 16KB
      - 4KB
    * - :ref:`board_intel_mcs51_STC15W4K32S4`
      - No
      - STC15W4K32S4
      - 11MHz
      - 32KB
      - 4KB
    * - :ref:`board_intel_mcs51_STC15W4K40S4`
      - No
      - STC15W4K40S4
      - 11MHz
      - 40KB
      - 4KB
    * - :ref:`board_intel_mcs51_STC15W4K48S4`
      - No
      - STC15W4K48S4
      - 11MHz
      - 48KB
      - 4KB
    * - :ref:`board_intel_mcs51_STC15W4K56S4`
      - No
      - STC15W4K56S4
      - 11MHz
      - 56KB
      - 4KB
    * - :ref:`board_intel_mcs51_STC89C516RD+`
      - No
      - STC89C516RD+
      - 11MHz
      - 64KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC89C51RC`
      - No
      - STC89C51RC
      - 11MHz
      - 4KB
      - 512B
    * - :ref:`board_intel_mcs51_STC89C52RC`
      - No
      - STC89C52RC
      - 11MHz
      - 8KB
      - 512B
    * - :ref:`board_intel_mcs51_STC89C53RC`
      - No
      - STC89C53RC
      - 11MHz
      - 13KB
      - 512B
    * - :ref:`board_intel_mcs51_STC89C54RD+`
      - No
      - STC89C54RD+
      - 11MHz
      - 16KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC89C58RD+`
      - No
      - STC89C58RD+
      - 11MHz
      - 32KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8A4K16S2A12`
      - No
      - STC8A4K16S2A12
      - 11MHz
      - 16KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_STC8A4K32S2A12`
      - No
      - STC8A4K32S2A12
      - 11MHz
      - 32KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_STC8A4K60S2A12`
      - No
      - STC8A4K60S2A12
      - 11MHz
      - 60KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_STC8A4K64S2A12`
      - No
      - STC8A4K64S2A12
      - 11MHz
      - 64KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_STC8A8K16D4`
      - No
      - STC8A8K16D4
      - 11MHz
      - 16KB
      - 8.25KB
    * - :ref:`board_intel_mcs51_STC8A8K16S4A12`
      - No
      - STC8A8K16S4A12
      - 11MHz
      - 16KB
      - 8.25KB
    * - :ref:`board_intel_mcs51_STC8A8K32D4`
      - No
      - STC8A8K32D4
      - 11MHz
      - 32KB
      - 8.25KB
    * - :ref:`board_intel_mcs51_STC8A8K32S4A12`
      - No
      - STC8A8K32S4A12
      - 11MHz
      - 32KB
      - 8.25KB
    * - :ref:`board_intel_mcs51_STC8A8K60D4`
      - No
      - STC8A8K60D4
      - 11MHz
      - 60KB
      - 8.25KB
    * - :ref:`board_intel_mcs51_STC8A8K60S4A12`
      - No
      - STC8A8K60S4A12
      - 11MHz
      - 60KB
      - 8.25KB
    * - :ref:`board_intel_mcs51_STC8A8K64D4`
      - No
      - STC8A8K64D4
      - 11MHz
      - 64KB
      - 8.25KB
    * - :ref:`board_intel_mcs51_STC8A8K64S4A12`
      - No
      - STC8A8K64S4A12
      - 11MHz
      - 64KB
      - 8.25KB
    * - :ref:`board_intel_mcs51_STC8C1K08`
      - No
      - STC8C1K08
      - 11MHz
      - 8KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8C1K12`
      - No
      - STC8C1K12
      - 11MHz
      - 12KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8C2K16S2`
      - No
      - STC8C2K16S2
      - 11MHz
      - 16KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8C2K16S4`
      - No
      - STC8C2K16S4
      - 11MHz
      - 16KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8C2K32S2`
      - No
      - STC8C2K32S2
      - 11MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8C2K32S4`
      - No
      - STC8C2K32S4
      - 11MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8C2K60S2`
      - No
      - STC8C2K60S2
      - 11MHz
      - 60KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8C2K60S4`
      - No
      - STC8C2K60S4
      - 11MHz
      - 60KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8C2K64S2`
      - No
      - STC8C2K64S2
      - 11MHz
      - 64KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8C2K64S4`
      - No
      - STC8C2K64S4
      - 11MHz
      - 64KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8F1K08`
      - No
      - STC8F1K08
      - 11MHz
      - 8KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8F1K08S`
      - No
      - STC8F1K08S
      - 11MHz
      - 8KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8F1K08S2`
      - No
      - STC8F1K08S2
      - 11MHz
      - 8KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8F1K08S2A10`
      - No
      - STC8F1K08S2A10
      - 11MHz
      - 8KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8F1K17`
      - No
      - STC8F1K17
      - 11MHz
      - 17KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8F1K17S2`
      - No
      - STC8F1K17S2
      - 11MHz
      - 17KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8F2K08S2`
      - No
      - STC8F2K08S2
      - 11MHz
      - 8KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8F2K16S2`
      - No
      - STC8F2K16S2
      - 11MHz
      - 16KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8F2K16S4`
      - No
      - STC8F2K16S4
      - 11MHz
      - 16KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8F2K32S2`
      - No
      - STC8F2K32S2
      - 11MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8F2K32S4`
      - No
      - STC8F2K32S4
      - 11MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8F2K60S2`
      - No
      - STC8F2K60S2
      - 11MHz
      - 60KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8F2K60S4`
      - No
      - STC8F2K60S4
      - 11MHz
      - 60KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8F2K64S2`
      - No
      - STC8F2K64S2
      - 11MHz
      - 64KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8F2K64S4`
      - No
      - STC8F2K64S4
      - 11MHz
      - 64KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8G1K08`
      - No
      - STC8G1K08
      - 11MHz
      - 8KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8G1K08A`
      - No
      - STC8G1K08A
      - 11MHz
      - 8KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8G1K08T`
      - No
      - STC8G1K08T
      - 11MHz
      - 8KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8G1K12`
      - No
      - STC8G1K12
      - 11MHz
      - 12KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8G1K12A`
      - No
      - STC8G1K12A
      - 11MHz
      - 12KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8G1K17`
      - No
      - STC8G1K17
      - 11MHz
      - 17KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8G1K17A`
      - No
      - STC8G1K17A
      - 11MHz
      - 17KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8G1K17T`
      - No
      - STC8G1K17T
      - 11MHz
      - 17KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8G2K16S2`
      - No
      - STC8G2K16S2
      - 11MHz
      - 16KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8G2K16S4`
      - No
      - STC8G2K16S4
      - 11MHz
      - 16KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8G2K32S2`
      - No
      - STC8G2K32S2
      - 11MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8G2K32S4`
      - No
      - STC8G2K32S4
      - 11MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8G2K60S2`
      - No
      - STC8G2K60S2
      - 11MHz
      - 60KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8G2K60S4`
      - No
      - STC8G2K60S4
      - 11MHz
      - 60KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8G2K64S2`
      - No
      - STC8G2K64S2
      - 11MHz
      - 64KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8G2K64S4`
      - No
      - STC8G2K64S4
      - 11MHz
      - 64KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8H04`
      - No
      - STC8H04
      - 11MHz
      - 4KB
      - 256B
    * - :ref:`board_intel_mcs51_STC8H04A10`
      - No
      - STC8H04A10
      - 11MHz
      - 4KB
      - 256B
    * - :ref:`board_intel_mcs51_STC8H1K08`
      - No
      - STC8H1K08
      - 11MHz
      - 8KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8H1K08S2`
      - No
      - STC8H1K08S2
      - 11MHz
      - 8KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8H1K08S2A10`
      - No
      - STC8H1K08S2A10
      - 11MHz
      - 8KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8H1K12`
      - No
      - STC8H1K12
      - 11MHz
      - 12KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8H1K16`
      - No
      - STC8H1K16
      - 11MHz
      - 16KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8H1K16S2`
      - No
      - STC8H1K16S2
      - 11MHz
      - 16KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8H1K16S2A10`
      - No
      - STC8H1K16S2A10
      - 11MHz
      - 16KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8H1K17`
      - No
      - STC8H1K17
      - 11MHz
      - 17KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8H1K24`
      - No
      - STC8H1K24
      - 11MHz
      - 24KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8H1K28`
      - No
      - STC8H1K28
      - 11MHz
      - 28KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8H1K32S2`
      - No
      - STC8H1K32S2
      - 11MHz
      - 32KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8H1K32S2A10`
      - No
      - STC8H1K32S2A10
      - 11MHz
      - 32KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8H1K33`
      - No
      - STC8H1K33
      - 11MHz
      - 33KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8H1K64S2A10`
      - No
      - STC8H1K64S2A10
      - 11MHz
      - 32KB
      - 1.25KB
    * - :ref:`board_intel_mcs51_STC8H2K32T`
      - No
      - STC8H2K32T
      - 11MHz
      - 32KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8H2K48T`
      - No
      - STC8H2K48T
      - 11MHz
      - 48KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8H2K60T`
      - No
      - STC8H2K60T
      - 11MHz
      - 60KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8H2K64T`
      - No
      - STC8H2K64T
      - 11MHz
      - 64KB
      - 2.25KB
    * - :ref:`board_intel_mcs51_STC8H3K32S2`
      - No
      - STC8H3K32S2
      - 11MHz
      - 32KB
      - 3.25KB
    * - :ref:`board_intel_mcs51_STC8H3K32S4`
      - No
      - STC8H3K32S4
      - 11MHz
      - 32KB
      - 3.25KB
    * - :ref:`board_intel_mcs51_STC8H3K48S2`
      - No
      - STC8H3K48S2
      - 11MHz
      - 32KB
      - 3.25KB
    * - :ref:`board_intel_mcs51_STC8H3K48S4`
      - No
      - STC8H3K48S4
      - 11MHz
      - 48KB
      - 3.25KB
    * - :ref:`board_intel_mcs51_STC8H3K60S2`
      - No
      - STC8H3K60S2
      - 11MHz
      - 60KB
      - 3.25KB
    * - :ref:`board_intel_mcs51_STC8H3K60S4`
      - No
      - STC8H3K60S4
      - 11MHz
      - 60KB
      - 3.25KB
    * - :ref:`board_intel_mcs51_STC8H3K64S2`
      - No
      - STC8H3K64S2
      - 11MHz
      - 64KB
      - 3.25KB
    * - :ref:`board_intel_mcs51_STC8H3K64S4`
      - No
      - STC8H3K64S4
      - 11MHz
      - 64KB
      - 3.25KB
    * - :ref:`board_intel_mcs51_STC8H4K32LCD`
      - No
      - STC8H4K32LCD
      - 11MHz
      - 32KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_STC8H4K32TLCD`
      - No
      - STC8H4K32TLCD
      - 11MHz
      - 32KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_STC8H4K32TLR`
      - No
      - STC8H4K32TLR
      - 11MHz
      - 32KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_STC8H4K48LCD`
      - No
      - STC8H4K48LCD
      - 11MHz
      - 48KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_STC8H4K48TLCD`
      - No
      - STC8H4K48TLCD
      - 11MHz
      - 48KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_STC8H4K48TLR`
      - No
      - STC8H4K48TLR
      - 11MHz
      - 48KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_STC8H4K60LCD`
      - No
      - STC8H4K60LCD
      - 11MHz
      - 60KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_STC8H4K60TLCD`
      - No
      - STC8H4K60TLCD
      - 11MHz
      - 60KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_STC8H4K60TLR`
      - No
      - STC8H4K60TLR
      - 11MHz
      - 60KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_STC8H4K64LCD`
      - No
      - STC8H4K64LCD
      - 11MHz
      - 64KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_STC8H4K64TLCD`
      - No
      - STC8H4K64TLCD
      - 11MHz
      - 64KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_STC8H4K64TLR`
      - No
      - STC8H4K64TLR
      - 11MHz
      - 64KB
      - 4.25KB
    * - :ref:`board_intel_mcs51_STC8H8K32U`
      - No
      - STC8H8K32U
      - 11MHz
      - 32KB
      - 8.25KB
    * - :ref:`board_intel_mcs51_STC8H8K48U`
      - No
      - STC8H8K48U
      - 11MHz
      - 48KB
      - 8.25KB
    * - :ref:`board_intel_mcs51_STC8H8K60U`
      - No
      - STC8H8K60U
      - 11MHz
      - 60KB
      - 8.25KB
    * - :ref:`board_intel_mcs51_STC8H8K64U`
      - No
      - STC8H8K64U
      - 11MHz
      - 64KB
      - 8.25KB

WCH
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_intel_mcs51_CH559`
      - No
      - CH559
      - 12MHz
      - 64KB
      - 6.25KB
