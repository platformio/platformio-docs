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

.. _board_ststm32_blues_swan_r5:

Blues Swan R5
=============

.. contents::

Hardware
--------

Platform :ref:`platform_ststm32`: The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

.. list-table::

  * - **Microcontroller**
    - STM32L4R5ZIY6
  * - **Frequency**
    - 120MHz
  * - **Flash**
    - 2MB
  * - **RAM**
    - 640KB
  * - **Vendor**
    - `Blues <https://blues.com/products/swan/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``blues_swan_r5`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:blues_swan_r5]
  platform = ststm32
  board = blues_swan_r5

You can override default Blues Swan R5 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `blues_swan_r5.json <https://github.com/platformio/platform-ststm32/blob/master/boards/blues_swan_r5.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:blues_swan_r5]
  platform = ststm32
  board = blues_swan_r5

  ; change microcontroller
  board_build.mcu = stm32l4r5ziy6

  ; change MCU frequency
  board_build.f_cpu = 120000000L


Uploading
---------
Blues Swan R5 supports the following uploading protocols:

* ``blackmagic``
* ``cmsis-dap``
* ``dfu``
* ``jlink``
* ``mbed``
* ``serial``
* ``stlink``

Default protocol is ``stlink``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:blues_swan_r5]
  platform = ststm32
  board = blues_swan_r5

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

Blues Swan R5 does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_blackmagic`
    - 
    - 
  * - :ref:`debugging_tool_cmsis-dap`
    - 
    - 
  * - :ref:`debugging_tool_jlink`
    - 
    - 
  * - :ref:`debugging_tool_stlink`
    - 
    - Yes

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_cmsis`
      - Vendor-independent hardware abstraction layer for the Cortex-M processor series

    * - :ref:`framework_libopencm3`
      - The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers.

    * - :ref:`framework_stm32cube`
      - STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency