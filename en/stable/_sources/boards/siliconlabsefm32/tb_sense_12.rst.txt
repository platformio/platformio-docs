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

.. _board_siliconlabsefm32_tb_sense_12:

Thunderboard Sense 2 Sensor-to-Cloud Advanced IoT
=================================================

.. contents::

Hardware
--------

Platform :ref:`platform_siliconlabsefm32`: Silicon Labs EFM32 Gecko 32-bit microcontroller (MCU) family includes devices that offer flash memory configurations up to 256 kB, 32 kB of RAM and CPU speeds up to 48 MHz. Based on the powerful ARM Cortex-M core, the Gecko family features innovative low energy techniques, short wake-up time from energy saving modes and a wide selection of peripherals, making it ideal for battery operated applications and other systems requiring high performance and low-energy consumption.

.. list-table::

  * - **Microcontroller**
    - EFR32MG12P432F1024
  * - **Frequency**
    - 40MHz
  * - **Flash**
    - 1MB
  * - **RAM**
    - 256KB
  * - **Vendor**
    - `Silicon Labs <https://www.silabs.com/products/development-tools/thunderboard/thunderboard-sense-two-kit?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``tb_sense_12`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:tb_sense_12]
  platform = siliconlabsefm32
  board = tb_sense_12

You can override default Thunderboard Sense 2 Sensor-to-Cloud Advanced IoT settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `tb_sense_12.json <https://github.com/platformio/platform-siliconlabsefm32/blob/master/boards/tb_sense_12.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:tb_sense_12]
  platform = siliconlabsefm32
  board = tb_sense_12

  ; change microcontroller
  board_build.mcu = EFR32MG12P432F1024

  ; change MCU frequency
  board_build.f_cpu = 40000000L


Uploading
---------
Thunderboard Sense 2 Sensor-to-Cloud Advanced IoT supports the next uploading protocols:

* ``blackmagic``
* ``jlink``
* ``mbed``

Default protocol is ``mbed``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:tb_sense_12]
  platform = siliconlabsefm32
  board = tb_sense_12

  upload_protocol = mbed

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

Thunderboard Sense 2 Sensor-to-Cloud Advanced IoT has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_blackmagic`
    - 
    - 
  * - :ref:`debugging_tool_jlink`
    - Yes
    - Yes

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_mbed`
      - Arm Mbed OS is an open source embedded operating system designed specifically for the 'things' in the Internet of Things. It includes all the features you need to develop a connected product based on an Arm Cortex-M microcontroller, including security, connectivity, an RTOS and drivers for sensors and I/O devices