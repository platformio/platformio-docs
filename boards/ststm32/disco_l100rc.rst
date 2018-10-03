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

.. _board_ststm32_disco_l100rc:

ST 32L100DISCOVERY
==================

.. contents::
    :local:

Platform :ref:`platform_ststm32`: The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

System
------

.. list-table::

  * - **Microcontroller**
    - STM32L100RCT6
  * - **Frequency**
    - 32Mhz
  * - **Flash**
    - 256KB
  * - **RAM**
    - 16KB
  * - **Vendor**
    - `ST <https://www.st.com/en/evaluation-tools/32l100cdiscovery.html?utm_source=platformio&utm_medium=docs>`__


Configuration
-------------

Please use ``disco_l100rc`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:disco_l100rc]
  platform = ststm32
  board = disco_l100rc

You can override default ST 32L100DISCOVERY settings per build environment using
``board_{JSON.PATH}`` option, where ``{JSON.PATH}`` is a path from
board manifest `disco_l100rc.json <https://github.com/platformio/platform-ststm32/blob/master/boards/disco_l100rc.json>`_. For example,

.. code-block:: ini

  [env:disco_l100rc]
  platform = ststm32
  board = disco_l100rc

  ; change microcontroller
  board_build.mcu = stm32l100rct6

  ; change MCU frequency
  board_build.f_cpu = 32000000L


Uploading
---------
ST 32L100DISCOVERY supports the next uploading protocols:

* ``stlink``
* ``blackmagic``

Default protocol is ``stlink``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:disco_l100rc]
  platform = ststm32
  board = disco_l100rc

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

ST 32L100DISCOVERY has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_blackmagic`
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

    * - :ref:`framework_stm32cube`
      - STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency.