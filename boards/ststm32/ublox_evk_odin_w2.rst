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

.. _board_ststm32_ublox_evk_odin_w2:

u-blox EVK-ODIN-W2
==================

.. contents::

Hardware
--------

Platform :ref:`platform_ststm32`: The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

.. list-table::

  * - **Microcontroller**
    - STM32F439ZIY6
  * - **Frequency**
    - 168MHz
  * - **Flash**
    - 2MB
  * - **RAM**
    - 256KB
  * - **Vendor**
    - `u-blox <https://developer.mbed.org/platforms/ublox-EVK-ODIN-W2/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``ublox_evk_odin_w2`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:ublox_evk_odin_w2]
  platform = ststm32
  board = ublox_evk_odin_w2

You can override default u-blox EVK-ODIN-W2 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `ublox_evk_odin_w2.json <https://github.com/platformio/platform-ststm32/blob/master/boards/ublox_evk_odin_w2.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:ublox_evk_odin_w2]
  platform = ststm32
  board = ublox_evk_odin_w2

  ; change microcontroller
  board_build.mcu = stm32f439ziy6

  ; change MCU frequency
  board_build.f_cpu = 168000000L


Uploading
---------
u-blox EVK-ODIN-W2 supports the next uploading protocols:

* ``blackmagic``
* ``cmsis-dap``
* ``jlink``
* ``stlink``

Default protocol is ``stlink``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:ublox_evk_odin_w2]
  platform = ststm32
  board = ublox_evk_odin_w2

  upload_protocol = stlink

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

u-blox EVK-ODIN-W2 does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_blackmagic`
    - 
    - Yes
  * - :ref:`debugging_tool_cmsis-dap`
    - 
    - 
  * - :ref:`debugging_tool_jlink`
    - 
    - 
  * - :ref:`debugging_tool_stlink`
    - 
    - 

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_mbed`
      - Arm Mbed OS is an open source embedded operating system designed specifically for the 'things' in the Internet of Things. It includes all the features you need to develop a connected product based on an Arm Cortex-M microcontroller, including security, connectivity, an RTOS and drivers for sensors and I/O devices

    * - :ref:`framework_stm32cube`
      - STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency