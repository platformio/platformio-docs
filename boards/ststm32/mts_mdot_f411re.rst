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

.. _board_ststm32_mts_mdot_f411re:

MultiTech mDot F411
===================

.. contents::

Platform :ref:`platform_ststm32`: The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

System
------

.. list-table::

  * - **Microcontroller**
    - STM32F411RET6
  * - **Frequency**
    - 100Mhz
  * - **Flash**
    - 512KB
  * - **RAM**
    - 128KB
  * - **Vendor**
    - `MultiTech <https://developer.mbed.org/platforms/MTS-mDot-F411/?utm_source=platformio&utm_medium=docs>`__


Configuration
-------------

Please use ``mts_mdot_f411re`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:mts_mdot_f411re]
  platform = ststm32
  board = mts_mdot_f411re

You can override default MultiTech mDot F411 settings per build environment using
``board_{JSON.PATH}`` option, where ``{JSON.PATH}`` is a path from
board manifest `mts_mdot_f411re.json <https://github.com/platformio/platform-ststm32/blob/master/boards/mts_mdot_f411re.json>`_. For example,

.. code-block:: ini

  [env:mts_mdot_f411re]
  platform = ststm32
  board = mts_mdot_f411re

  ; change microcontroller
  board_build.mcu = stm32f411ret6

  ; change MCU frequency
  board_build.f_cpu = 100000000L


Uploading
---------
MultiTech mDot F411 supports the next uploading protocols:

* ``jlink``
* ``stlink``
* ``blackmagic``
* ``mbed``

Default protocol is ``mbed``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:mts_mdot_f411re]
  platform = ststm32
  board = mts_mdot_f411re

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

MultiTech mDot F411 does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_blackmagic`
    - 
    - Yes
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
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.

    * - :ref:`framework_stm32cube`
      - STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency.