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

.. _platform_microchippic32:

Microchip PIC32
===============
:ref:`projectconf_env_platform` = ``microchippic32``

Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

For more detailed information please visit `vendor site <http://www.microchip.com/design-centers/32-bit?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Microchip PIC32 development platform repository <https://github.com/platformio/platform-microchippic32/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_:

* `arduino-blink <https://github.com/platformio/platform-microchippic32/tree/develop/examples/arduino-blink?utm_source=platformio&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-microchippic32/tree/develop/examples/arduino-internal-libs?utm_source=platformio&utm_medium=docs>`_

Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-microchippic32/releases>`__
of Microchip PIC32 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below:

.. code-block:: ini

    ; Custom stable version
    [env:stable]
    platform =microchippic32@x.y.z
    board = ...
    ...

    ; The latest upstream/development version
    [env:upstream]
    platform = https://github.com/platformio/platform-microchippic32.git
    board = ...
    ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinomicrochippic32 <https://github.com/chipKIT32/chipKIT-core?utm_source=platformio&utm_medium=docs>`__
      - Arduino Wiring-based Framework (PIC32 Core)

    * - `tool-pic32prog <https://github.com/sergev/pic32prog?utm_source=platformio&utm_medium=docs>`__
      - pic32prog

    * - `toolchain-microchippic32 <https://github.com/chipKIT32/chipKIT-cxx?utm_source=platformio&utm_medium=docs>`__
      - GCC for Microchip PIC32

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
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

4DSystems
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``picadillo_35t``
      - `4DSystems PICadillo 35T <http://www.4dsystems.com.au/product/Picadillo_35T/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB

Digilent
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``cerebot32mx4``
      - `Digilent Cerebot 32MX4 <http://store.digilentinc.com/cerebot-32mx4-limited-time-see-chipkit-pro-mx4/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX460F512L
      - 80MHz
      - 508KB
      - 32KB
    * - ``cerebot32mx7``
      - `Digilent Cerebot 32MX7 <http://www.microchip.com/Developmenttools/ProductDetails.aspx?PartNO=TDGL004&utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB
    * - ``chipkit_cmod``
      - `Digilent chipKIT Cmod <http://store.digilentinc.com/chipkit-cmod-breadboardable-mz-microcontroller-board/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX150F128D
      - 40MHz
      - 124KB
      - 32KB
    * - ``chipkit_dp32``
      - `Digilent chipKIT DP32 <http://store.digilentinc.com/chipkit-dp32-dip-package-prototyping-microcontroller-board/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX250F128B
      - 40MHz
      - 120KB
      - 32KB
    * - ``chipkit_mx3``
      - `Digilent chipKIT MX3 <http://store.digilentinc.com/chipkit-mx3-microcontroller-board-with-pmod-headers/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX320F128H
      - 80MHz
      - 124KB
      - 16KB
    * - ``chipkit_pro_mx4``
      - `Digilent chipKIT Pro MX4 <http://store.digilentinc.com/chipkit-pro-mx4-embedded-systems-trainer-board/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX460F512L
      - 80MHz
      - 508KB
      - 32KB
    * - ``chipkit_pro_mx7``
      - `Digilent chipKIT Pro MX7 <http://store.digilentinc.com/chipkit-pro-mx7-advanced-peripherals-embedded-systems-trainer-board/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB
    * - ``chipkit_uc32``
      - `Digilent chipKIT uC32 <http://store.digilentinc.com/chipkit-uc32-basic-microcontroller-board-with-uno-r3-headers/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX340F512H
      - 80MHz
      - 508KB
      - 32KB
    * - ``chipkit_wf32``
      - `Digilent chipKIT WF32 <http://store.digilentinc.com/chipkit-wf32-wifi-enabled-microntroller-board-with-uno-r3-headers/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX695F512L
      - 80MHz
      - 508KB
      - 128KB
    * - ``chipkit_wifire``
      - `Digilent chipKIT WiFire <http://store.digilentinc.com/chipkit-wi-fire-wifi-enabled-mz-microcontroller-board/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MZ2048ECG100
      - 200MHz
      - 1.98MB
      - 512KB
    * - ``mega_pic32``
      - `Digilent chipKIT MAX32 <http://store.digilentinc.com/chipkit-max32-microcontroller-board-with-mega-r3-headers/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB
    * - ``openscope``
      - `Digilent OpenScope <http://store.digilentinc.com/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MZ2048EFG124
      - 200MHz
      - 1.98MB
      - 512KB
    * - ``uno_pic32``
      - `Digilent chipKIT UNO32 <http://store.digilentinc.com/chipkit-uno32-basic-microcontroller-board-retired-see-chipkit-uc32/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX320F128H
      - 80MHz
      - 124KB
      - 16KB

Fubarino
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``fubarino_mini``
      - `Fubarino Mini <http://fubarino.org/mini/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX250F128D
      - 48MHz
      - 120KB
      - 32KB
    * - ``fubarino_sd``
      - `Fubarino SD (1.5) <http://fubarino.org/sd/index.html?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX795F512H
      - 80MHz
      - 508KB
      - 128KB

MikroElektronika
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``clicker2``
      - `MikroElektronika Clicker 2 <http://www.mikroe.com/pic/clicker/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX460F512L
      - 80MHz
      - 508KB
      - 32KB
    * - ``flipnclickmz``
      - `MikroElektronika Flip N Click MZ <https://shop.mikroe.com/flipclick-pic32mz?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MZ2048EFH100
      - 252MHz
      - 1.98MB
      - 512KB

Olimex
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
    * - ``pinguino32``
      - `Olimex PIC32-PINGUINO <https://www.olimex.com/Products/Duino/PIC32/PIC32-PINGUINO/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX440F256H
      - 80MHz
      - 252KB
      - 32KB

OpenBCI
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``openbci``
      - `OpenBCI 32bit <http://shop.openbci.com/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX250F128B
      - 40MHz
      - 120KB
      - 32KB

PONTECH
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``usbono_pic32``
      - `PONTECH UAV100 <http://www.pontech.com/productdisplay/uav100?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX440F512H
      - 80MHz
      - 508KB
      - 32KB

Pontech
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``nofire``
      - `Pontech NoFire <http://www.pontech.com/products?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MZ2048EFG100
      - 200MHz
      - 1.98MB
      - 512KB
    * - ``quick240_usb``
      - `Pontech Quick240 <http://chipkit.net/wpcproduct/pontech-quick240/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB

SeeedStudio
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``cui32stem``
      - `SeeedStudio CUI32stem <http://www.seeedstudio.com/wiki/CUI32Stem?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX795F512H
      - 80MHz
      - 508KB
      - 128KB

UBW32
~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``ubw32_mx460``
      - `UBW32 MX460 <http://www.schmalzhaus.com/UBW32/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX460F512L
      - 80MHz
      - 508KB
      - 32KB
    * - ``ubw32_mx795``
      - `UBW32 MX795 <http://www.schmalzhaus.com/UBW32/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB

chipKIT
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lenny``
      - `chipKIT Lenny <http://chipkit.net/tag/lenny/?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX270F256D
      - 40MHz
      - 120KB
      - 32KB

element14
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``chipkit_pi``
      - `Element14 chipKIT Pi <http://www.element14.com/community/community/knode/dev_platforms_kits/element14_dev_kits/microchip-chipkit/chipkit_pi?utm_source=platformio&utm_medium=docs>`_
      - No
      - 32MX250F128B
      - 40MHz
      - 120KB
      - 32KB
