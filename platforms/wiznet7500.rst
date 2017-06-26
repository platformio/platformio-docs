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

.. _platform_wiznet7500:

WIZNet W7500
============
:ref:`projectconf_env_platform` = ``wiznet7500``

The IOP (Internet Offload Processor) W7500  is the one-chip solution which integrates an ARM Cortex-M0, 128KB Flash and hardwired TCP/IP core for various embedded application platform especially requiring Internet of things

For more detailed information please visit `vendor site <http://www.wiznet.io/product-item/w7500/>`_.

.. contents:: Contents
    :local:

Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-mbed <http://mbed.org>`__
      - mbed Framework

    * - `tool-openocd <http://openocd.org>`__
      - OpenOCD

    * - `toolchain-gccarmnoneeabi <https://launchpad.net/gcc-arm-embedded>`__
      - gcc-arm-embedded

.. warning::
    **Linux Users**:

        * Install "udev" rules file `99-platformio-udev.rules <https://github.com/platformio/platformio-core/blob/develop/scripts/99-platformio-udev.rules>`_
          (an instruction is located inside a file).
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

    * - :ref:`framework_mbed`
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

WIZNet
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``wizwiki_w7500``
      - `WIZNet WIZwiki-W7500 <https://developer.mbed.org/platforms/WIZwiki-W7500/>`_
      - :ref:`WIZNet W7500 <platform_wiznet7500>`
      - :ref:`Yes <piodebug>`
      - WIZNET7500
      - 48 MHz
      - 128 Kb
      - 48 Kb

    * - ``wizwiki_w7500eco``
      - `WIZNet WIZwiki-W7500ECO <https://developer.mbed.org/platforms/WIZwiki-W7500ECO/>`_
      - :ref:`WIZNet W7500 <platform_wiznet7500>`
      - :ref:`Yes <piodebug>`
      - WIZNET7500ECO
      - 48 MHz
      - 128 Kb
      - 48 Kb

    * - ``wizwiki_w7500p``
      - `WIZNet WIZwiki-W7500P <https://developer.mbed.org/platforms/WIZwiki-W7500P/>`_
      - :ref:`WIZNet W7500 <platform_wiznet7500>`
      - :ref:`Yes <piodebug>`
      - WIZNET7500P
      - 48 MHz
      - 128 Kb
      - 48 Kb
