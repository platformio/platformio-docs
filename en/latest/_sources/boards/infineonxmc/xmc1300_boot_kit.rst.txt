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

.. _board_infineonxmc_xmc1300_boot_kit:

XMC1300 Boot Kit
================

.. contents::

Hardware
--------

Platform :ref:`platform_infineonxmc`: Infineon has designed the XMC microcontrollers for real-time critical applications with an industry-standard core. The XMC microcontrollers can be integrated with the Arduino platform

.. list-table::

  * - **Microcontroller**
    - XMC1300
  * - **Frequency**
    - 32MHz
  * - **Flash**
    - 64KB
  * - **RAM**
    - 16KB
  * - **Vendor**
    - `Infineon <https://www.infineon.com?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``xmc1300_boot_kit`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:xmc1300_boot_kit]
  platform = infineonxmc
  board = xmc1300_boot_kit

You can override default XMC1300 Boot Kit settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `xmc1300_boot_kit.json <https://github.com/Infineon/platformio-infineonxmc/blob/master/boards/xmc1300_boot_kit.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:xmc1300_boot_kit]
  platform = infineonxmc
  board = xmc1300_boot_kit

  ; change microcontroller
  board_build.mcu = XMC1300

  ; change MCU frequency
  board_build.f_cpu = 32000000L

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

XMC1300 Boot Kit has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_jlink`
    - Yes
    - Yes

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences