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

.. _board_ststm32_olimexino:

OLIMEXINO-STM32
===============

.. contents::

Hardware
--------

Platform :ref:`platform_ststm32`: The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

.. list-table::

  * - **Microcontroller**
    - STM32F103RBT6
  * - **Frequency**
    - 72MHz
  * - **Flash**
    - 128KB
  * - **RAM**
    - 20KB
  * - **Vendor**
    - `Olimex <https://docs.zephyrproject.org/latest/boards/arm/olimexino_stm32/doc/index.html?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``olimexino`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:olimexino]
  platform = ststm32
  board = olimexino

You can override default OLIMEXINO-STM32 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `olimexino.json <https://github.com/platformio/platform-ststm32/blob/master/boards/olimexino.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:olimexino]
  platform = ststm32
  board = olimexino

  ; change microcontroller
  board_build.mcu = stm32f103rbt6

  ; change MCU frequency
  board_build.f_cpu = 72000000L


Uploading
---------
OLIMEXINO-STM32 supports the next uploading protocols:

* ``blackmagic``
* ``cmsis-dap``
* ``jlink``
* ``stlink``

Default protocol is ``stlink``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:olimexino]
  platform = ststm32
  board = olimexino

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

OLIMEXINO-STM32 does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

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

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences

    * - :ref:`framework_cmsis`
      - The ARM Cortex Microcontroller Software Interface Standard (CMSIS) is a vendor-independent hardware abstraction layer for the Cortex-M processor series and specifies debugger interfaces. The CMSIS enables consistent and simple software interfaces to the processor for interface peripherals, real-time operating systems, and middleware. It simplifies software re-use, reducing the learning curve for new microcontroller developers and cutting the time-to-market for devices

    * - :ref:`framework_mbed`
      - Arm Mbed OS is an open source embedded operating system designed specifically for the 'things' in the Internet of Things. It includes all the features you need to develop a connected product based on an Arm Cortex-M microcontroller, including security, connectivity, an RTOS and drivers for sensors and I/O devices

    * - :ref:`framework_stm32cube`
      - STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency

    * - :ref:`framework_zephyr`
      - The Zephyr Project is a scalable real-time operating system (RTOS) supporting multiple hardware architectures, optimized for resource constrained devices, and built with safety and security in mind

    * - :ref:`framework_libopencm3`
      - The libOpenCM3 framework aims to create a free and open-source firmware library for various ARM Cortex-M0(+)/M3/M4 microcontrollers, including ST STM32, Ti Tiva and Stellaris, NXP LPC, Atmel SAM3, Energy Micro EFM32 and others