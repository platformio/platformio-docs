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

.. _board_ststm32_lilygo_t3_stm32_v1:

LilyGo T3-STM32
===============

.. contents::

Hardware
--------

Platform :ref:`platform_ststm32`: The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

.. list-table::

  * - **Microcontroller**
    - STM32WLE5CCU7
  * - **Frequency**
    - 48MHz
  * - **Flash**
    - 256KB
  * - **RAM**
    - 64KB
  * - **Vendor**
    - `LilyGo <https://github.com/Xinyuan-LilyGO/T3-STM32?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``lilygo_t3_stm32_v1`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:lilygo_t3_stm32_v1]
  platform = ststm32
  board = lilygo_t3_stm32_v1

You can override default LilyGo T3-STM32 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `lilygo_t3_stm32_v1.json <https://github.com/platformio/platform-ststm32/blob/master/boards/lilygo_t3_stm32_v1.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:lilygo_t3_stm32_v1]
  platform = ststm32
  board = lilygo_t3_stm32_v1

  ; change microcontroller
  board_build.mcu = stm32wle5ccu7

  ; change MCU frequency
  board_build.f_cpu = 48000000L


Uploading
---------
LilyGo T3-STM32 supports the following uploading protocols:

* ``jlink``
* ``serial``
* ``stlink``

Default protocol is ``serial``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:lilygo_t3_stm32_v1]
  platform = ststm32
  board = lilygo_t3_stm32_v1

  upload_protocol = serial

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

LilyGo T3-STM32 does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_jlink`
    - 
    - Yes
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
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.