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

.. _platform_samsung_artik:

Samsung ARTIK
=============
:ref:`projectconf_env_platform` = ``samsung_artik``

The Samsung ARTIK Smart IoT platform brings hardware modules and cloud services together, with built-in security and an ecosystem of tools and partners to speed up your time-to-market.

For more detailed information please visit `vendor site <http://platformio.org/platforms/samsung_artik>`_.

.. contents:: Contents
    :local:

Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-tizenrt <http://www.artik.io>`__
      - TizenRT RTOS with library

    * - `tool-artik-openocd <http://openocd.org>`__
      - OpenOCD for ARTIK

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


Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

Samsung
~~~~~~~

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

    * - ``artik_053``
      - `Samsung ARTIK053 <http://www.artik.io>`_
      - :ref:`Samsung ARTIK <platform_samsung_artik>`
      - :ref:`Yes <piodebug>`
      - S5JT200
      - 320 MHz
      - 8192 Kb
      - 1280 Kb

.. include:: samsung_artik_extra.rst
