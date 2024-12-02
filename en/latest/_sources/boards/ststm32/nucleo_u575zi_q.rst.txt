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

.. _board_ststm32_nucleo_u575zi_q:

ST Nucleo U575ZI-Q
==================

.. contents::

Hardware
--------

Platform :ref:`platform_ststm32`: The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

.. list-table::

  * - **Microcontroller**
    - STM32U575ZIT6Q
  * - **Frequency**
    - 160MHz
  * - **Flash**
    - 2MB
  * - **RAM**
    - 256KB
  * - **Vendor**
    - `ST <https://www.st.com/en/evaluation-tools/nucleo-u575zi-q.html?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``nucleo_u575zi_q`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:nucleo_u575zi_q]
  platform = ststm32
  board = nucleo_u575zi_q

You can override default ST Nucleo U575ZI-Q settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `nucleo_u575zi_q.json <https://github.com/platformio/platform-ststm32/blob/master/boards/nucleo_u575zi_q.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:nucleo_u575zi_q]
  platform = ststm32
  board = nucleo_u575zi_q

  ; change microcontroller
  board_build.mcu = stm32u575zit6q

  ; change MCU frequency
  board_build.f_cpu = 160000000L


Uploading
---------
ST Nucleo U575ZI-Q supports the following uploading protocols:

* ``blackmagic``
* ``cmsis-dap``
* ``jlink``
* ``mbed``
* ``stlink``

Default protocol is ``stlink``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:nucleo_u575zi_q]
  platform = ststm32
  board = nucleo_u575zi_q

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

ST Nucleo U575ZI-Q has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

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
    - Yes
    - Yes

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_mbed`
      - Arm Mbed OS is a platform operating system designed for the internet of things