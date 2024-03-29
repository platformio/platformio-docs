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

.. _board_linux_arm_raspberrypi_3b:

Raspberry Pi 3 Model B
======================

.. contents::

Hardware
--------

Platform :ref:`platform_linux_arm`: Linux ARM is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X, Linux ARM) you can build native application for Linux ARM platform.

.. list-table::

  * - **Microcontroller**
    - BCM2837
  * - **Frequency**
    - 1200MHz
  * - **Flash**
    - 1GB
  * - **RAM**
    - 1GB
  * - **Vendor**
    - `Raspberry Pi <https://www.raspberrypi.org?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``raspberrypi_3b`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:raspberrypi_3b]
  platform = linux_arm
  board = raspberrypi_3b

You can override default Raspberry Pi 3 Model B settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `raspberrypi_3b.json <https://github.com/platformio/platform-linux_arm/blob/master/boards/raspberrypi_3b.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:raspberrypi_3b]
  platform = linux_arm
  board = raspberrypi_3b

  ; change microcontroller
  board_build.mcu = bcm2837

  ; change MCU frequency
  board_build.f_cpu = 1200000000L

Debugging
---------
:ref:`piodebug` currently does not support Raspberry Pi 3 Model B board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_wiringpi`
      - WiringPi is a PIN based GPIO access library written in C for the BCM2835, BCM2836 and BCM2837 SoC devices used in all Raspberry Pi