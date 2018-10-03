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

.. _board_ststm32_cloud_jam_l4:

RushUp Cloud-JAM L4
===================

.. contents::

Platform :ref:`platform_ststm32`: The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

System
------

.. list-table::

  * - **Microcontroller**
    - STM32L476RGT6
  * - **Frequency**
    - 80Mhz
  * - **Flash**
    - 1MB
  * - **RAM**
    - 128KB
  * - **Vendor**
    - `RushUp <https://developer.mbed.org/platforms/ST-Nucleo-L476RG/?utm_source=platformio&utm_medium=docs>`__


Configuration
-------------

Please use ``cloud_jam_l4`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:cloud_jam_l4]
  platform = ststm32
  board = cloud_jam_l4

You can override default RushUp Cloud-JAM L4 settings per build environment using
``board_{JSON.PATH}`` option, where ``{JSON.PATH}`` is a path from
board manifest `cloud_jam_l4.json <https://github.com/platformio/platform-ststm32/blob/master/boards/cloud_jam_l4.json>`_. For example,

.. code-block:: ini

  [env:cloud_jam_l4]
  platform = ststm32
  board = cloud_jam_l4

  ; change microcontroller
  board_build.mcu = stm32l476rgt6

  ; change MCU frequency
  board_build.f_cpu = 80000000L


Uploading
---------
RushUp Cloud-JAM L4 supports the next uploading protocols:

* ``jlink``
* ``stlink``
* ``blackmagic``
* ``mbed``

Default protocol is ``mbed``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:cloud_jam_l4]
  platform = ststm32
  board = cloud_jam_l4

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

RushUp Cloud-JAM L4 has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_blackmagic`
    - 
    - 
  * - :ref:`debugging_tool_jlink`
    - 
    - 
  * - :ref:`debugging_tool_stlink`
    - Yes
    - Yes

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_mbed`
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.

    * - :ref:`framework_stm32cube`
      - STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency.