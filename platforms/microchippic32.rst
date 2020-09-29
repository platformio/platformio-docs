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

:Configuration:
  :ref:`projectconf_env_platform` = ``microchippic32``

Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

For more detailed information please visit `vendor site <http://www.microchip.com/design-centers/32-bit?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Microchip PIC32 development platform repository <https://github.com/platformio/platform-microchippic32/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `arduino-blink <https://github.com/platformio/platform-microchippic32/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-microchippic32/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs>`_

Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-microchippic32/releases>`__
of Microchip PIC32 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = microchippic32
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = microchippic32@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-microchippic32.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinomicrochippic32 <http://chipkit.net/?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip PIC32 microcontrollers

    * - `tool-pic32prog <https://github.com/sergev/pic32prog.git?utm_source=platformio.org&utm_medium=docs>`__
      - Flash programming utility for Microchip PIC32 microcontrollers

    * - `toolchain-microchippic32 <https://github.com/chipKIT32/chipKIT-cxx.git?utm_source=platformio.org&utm_medium=docs>`__
      - GCC Toolchain for Microchip PIC32

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

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

4D Systems
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_picadillo_35t`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB

BOXTEC
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_helvepic32`
      - No
      - 32MX250F128B
      - 48MHz
      - 120KB
      - 32KB
    * - :ref:`board_microchippic32_helvepic32_breadboardside`
      - No
      - 32MX250F128B
      - 48MHz
      - 120KB
      - 32KB
    * - :ref:`board_microchippic32_helvepic32_smd`
      - No
      - 32MX250F128D
      - 48MHz
      - 120KB
      - 32KB
    * - :ref:`board_microchippic32_helvepic32_mx270`
      - No
      - 32MX270F256B
      - 48MHz
      - 244KB
      - 62KB
    * - :ref:`board_microchippic32_helvepic32_robot`
      - No
      - 32MX270F256D
      - 48MHz
      - 244KB
      - 62KB
    * - :ref:`board_microchippic32_helvepic32_smd_mx270`
      - No
      - 32MX270F256D
      - 48MHz
      - 244KB
      - 62KB

ChipKIT
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_rgb_station`
      - No
      - 32MX270F256D
      - 48MHz
      - 240KB
      - 62KB

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
    * - :ref:`board_microchippic32_cerebot32mx4`
      - No
      - 32MX460F512L
      - 80MHz
      - 508KB
      - 32KB
    * - :ref:`board_microchippic32_cerebot32mx7`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB
    * - :ref:`board_microchippic32_openscope`
      - No
      - 32MZ2048EFG124
      - 200MHz
      - 1.98MB
      - 512KB
    * - :ref:`board_microchippic32_chipkit_cmod`
      - No
      - 32MX150F128D
      - 40MHz
      - 124KB
      - 32KB
    * - :ref:`board_microchippic32_chipkit_dp32`
      - No
      - 32MX250F128B
      - 40MHz
      - 120KB
      - 32KB
    * - :ref:`board_microchippic32_mega_pic32`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB
    * - :ref:`board_microchippic32_chipkit_mx3`
      - No
      - 32MX320F128H
      - 80MHz
      - 124KB
      - 16KB
    * - :ref:`board_microchippic32_chipkit_pro_mx4`
      - No
      - 32MX460F512L
      - 80MHz
      - 508KB
      - 32KB
    * - :ref:`board_microchippic32_chipkit_pro_mx7`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB
    * - :ref:`board_microchippic32_uno_pic32`
      - No
      - 32MX320F128H
      - 80MHz
      - 124KB
      - 16KB
    * - :ref:`board_microchippic32_chipkit_wf32`
      - No
      - 32MX695F512L
      - 80MHz
      - 508KB
      - 128KB
    * - :ref:`board_microchippic32_chipkit_wifire`
      - No
      - 32MZ2048ECG100
      - 200MHz
      - 1.98MB
      - 512KB
    * - :ref:`board_microchippic32_chipkit_uc32`
      - No
      - 32MX340F512H
      - 80MHz
      - 508KB
      - 32KB
    * - :ref:`board_microchippic32_chipkit_wifire_revc`
      - No
      - 32MZ2048EFG100
      - 200MHz
      - 1.98MB
      - 512KB

Fubarino
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_fubarino_mini`
      - No
      - 32MX250F128D
      - 48MHz
      - 120KB
      - 32KB
    * - :ref:`board_microchippic32_fubarino_sd`
      - No
      - 32MX795F512H
      - 80MHz
      - 508KB
      - 128KB
    * - :ref:`board_microchippic32_fubarino_mini_20`
      - No
      - 32MX270F256D
      - 48MHz
      - 240KB
      - 62KB

Makerology
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_dsmini`
      - No
      - 32MX150F128C
      - 40MHz
      - 120KB
      - 32KB

MikroElektronika
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_clicker2`
      - No
      - 32MX460F512L
      - 80MHz
      - 508KB
      - 32KB
    * - :ref:`board_microchippic32_flipnclickmz`
      - No
      - 32MZ2048EFH100
      - 252MHz
      - 1.98MB
      - 512KB

Olimex
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_pinguino32`
      - No
      - 32MX440F256H
      - 80MHz
      - 252KB
      - 32KB

OpenBCI
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_openbci`
      - No
      - 32MX250F128B
      - 40MHz
      - 120KB
      - 32KB

PONTECH
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_usbono_pic32`
      - No
      - 32MX440F512H
      - 80MHz
      - 508KB
      - 32KB

Pontech
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_nofire`
      - No
      - 32MZ2048EFG100
      - 200MHz
      - 1.98MB
      - 512KB
    * - :ref:`board_microchippic32_quick240_usb`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB

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
    * - :ref:`board_microchippic32_cui32stem`
      - No
      - 32MX795F512H
      - 80MHz
      - 508KB
      - 128KB

SparkFun
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_cui32`
      - No
      - 32MX440F512H
      - 80MHz
      - 508KB
      - 32KB

UBW32
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_ubw32_mx460`
      - No
      - 32MX460F512L
      - 80MHz
      - 508KB
      - 32KB
    * - :ref:`board_microchippic32_ubw32_mx795`
      - No
      - 32MX795F512L
      - 80MHz
      - 508KB
      - 128KB

chipKIT
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_lenny`
      - No
      - 32MX270F256D
      - 40MHz
      - 120KB
      - 32KB

element14
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_microchippic32_chipkit_pi`
      - No
      - 32MX250F128B
      - 40MHz
      - 120KB
      - 32KB
