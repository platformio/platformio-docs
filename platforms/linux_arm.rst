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

:Registry:
  `https://registry.platformio.org/platforms/platformio/linux_arm <https://registry.platformio.org/platforms/platformio/linux_arm>`__
:Configuration:
  :ref:`projectconf_env_platform` = ``platformio/linux_arm``

Linux ARM is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X, Linux ARM) you can build native application for Linux ARM platform.

For more detailed information please visit `vendor site <https://registry.platformio.org/platforms/platformio/linux_arm?utm_source=platformio.org&utm_medium=docs>`_.

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

    ; Latest stable version, NOT recommended
    ; Pin the version as shown below
    [env:latest_stable]
    platform = linux_arm
    
    ; Specific version
    [env:custom_stable]
    platform = linux_arm@x.y.z
    
Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-linux_arm.git
    

Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-wiringpi <https://registry.platformio.org/tools/platformio/framework-wiringpi>`__
      - WiringPi is a PIN based GPIO access library written in C for the BCM2835, BCM2836 and BCM2837 SoC devices used in all Raspberry Pi

    * - `toolchain-gccarmlinuxgnueabi <https://registry.platformio.org/tools/platformio/toolchain-gccarmlinuxgnueabi>`__
      - GCC Toolchain for Linux ARM GNU EABI

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_wiringpi`
      - WiringPi is a PIN based GPIO access library written in C for the BCM2835, BCM2836 and BCM2837 SoC devices used in all Raspberry Pi

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command
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
