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

.. _platform_linux_arm:

Linux ARM
=========

:Configuration:
  :ref:`projectconf_env_platform` = ``linux_arm``

Linux ARM is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X, Linux ARM) you can build native application for Linux ARM platform.

For more detailed information please visit `vendor site <http://platformio.org/platforms/linux_arm?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Linux ARM development platform repository <https://github.com/platformio/platform-linux_arm/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `wiringpi-serial <https://github.com/platformio/platform-linux_arm/tree/master/examples/wiringpi-serial?utm_source=platformio.org&utm_medium=docs>`_
* `wiringpi-blink <https://github.com/platformio/platform-linux_arm/tree/master/examples/wiringpi-blink?utm_source=platformio.org&utm_medium=docs>`_

Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-linux_arm/releases>`__
of Linux ARM development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = linux_arm
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = linux_arm@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-linux_arm.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-wiringpi <http://wiringpi.com?utm_source=platformio.org&utm_medium=docs>`__
      - WiringPi is a PIN based GPIO access library written in C for the BCM2835, BCM2836 and BCM2837 SoC devices used in all Raspberry Pi

    * - `toolchain-gccarmlinuxgnueabi <https://gcc.gnu.org?utm_source=platformio.org&utm_medium=docs>`__
      - GCC Toolchain for Linux ARM GNU EABI

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_wiringpi`
      - WiringPi is a GPIO access library written in C for the BCM2835 used in the Raspberry Pi. It's designed to be familiar to people who have used the Arduino 'wiring' system

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

Raspberry Pi
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_linux_arm_raspberrypi_1b`
      - No
      - BCM2835
      - 700MHz
      - 512MB
      - 512MB
    * - :ref:`board_linux_arm_raspberrypi_2b`
      - No
      - BCM2836
      - 900MHz
      - 1GB
      - 1GB
    * - :ref:`board_linux_arm_raspberrypi_3b`
      - No
      - BCM2837
      - 1200MHz
      - 1GB
      - 1GB
    * - :ref:`board_linux_arm_raspberrypi_zero`
      - No
      - BCM2835
      - 1000MHz
      - 512MB
      - 512MB
