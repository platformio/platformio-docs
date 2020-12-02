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

.. _board_ststm32_armstrap_eagle512:

Armstrap Eagle 512
==================

.. contents::

Hardware
--------

Platform :ref:`platform_ststm32`: The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

.. list-table::

  * - **Microcontroller**
    - STM32F407VET6
  * - **Frequency**
    - 168MHz
  * - **Flash**
    - 512KB
  * - **RAM**
    - 192KB
  * - **Vendor**
    - `Armstrap <http://docs.armstrap.org/en/latest/hardware-overview.html?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``armstrap_eagle512`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:armstrap_eagle512]
  platform = ststm32
  board = armstrap_eagle512

You can override default Armstrap Eagle 512 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `armstrap_eagle512.json <https://github.com/platformio/platform-ststm32/blob/master/boards/armstrap_eagle512.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:armstrap_eagle512]
  platform = ststm32
  board = armstrap_eagle512

  ; change microcontroller
  board_build.mcu = stm32f407vet6

  ; change MCU frequency
  board_build.f_cpu = 168000000L


Uploading
---------
Armstrap Eagle 512 supports the next uploading protocols:

* ``blackmagic``
* ``cmsis-dap``
* ``jlink``
* ``stlink``

Default protocol is ``blackmagic``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:armstrap_eagle512]
  platform = ststm32
  board = armstrap_eagle512

  upload_protocol = blackmagic

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

Armstrap Eagle 512 has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_blackmagic`
    - Yes
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

    * - :ref:`framework_cmsis`
      - The ARM Cortex Microcontroller Software Interface Standard (CMSIS) is a vendor-independent hardware abstraction layer for the Cortex-M processor series and specifies debugger interfaces. The CMSIS enables consistent and simple software interfaces to the processor for interface peripherals, real-time operating systems, and middleware. It simplifies software re-use, reducing the learning curve for new microcontroller developers and cutting the time-to-market for devices

    * - :ref:`framework_stm32cube`
      - STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency

    * - :ref:`framework_spl`
      - The ST Standard Peripheral Library provides a set of functions for handling the peripherals on the STM32 family of microcontrollers.

    * - :ref:`framework_libopencm3`
      - The libOpenCM3 framework aims to create a free and open-source firmware library for various ARM Cortex-M0(+)/M3/M4 microcontrollers, including ST STM32, Ti Tiva and Stellaris, NXP LPC, Atmel SAM3, Energy Micro EFM32 and others