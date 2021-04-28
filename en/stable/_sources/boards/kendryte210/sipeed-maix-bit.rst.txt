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

.. _board_kendryte210_sipeed-maix-bit:

Sipeed MAIX BiT
===============

.. contents::

Hardware
--------

Platform :ref:`platform_kendryte210`: Kendryte K210 is an AI capable RISCV64 dual core SoC.

.. list-table::

  * - **Microcontroller**
    - K210
  * - **Frequency**
    - 400MHz
  * - **Flash**
    - 16MB
  * - **RAM**
    - 6MB
  * - **Vendor**
    - `Sipeed <https://www.sipeed.com/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``sipeed-maix-bit`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:sipeed-maix-bit]
  platform = kendryte210
  board = sipeed-maix-bit

You can override default Sipeed MAIX BiT settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `sipeed-maix-bit.json <https://github.com/sipeed/platform-kendryte210/blob/master/boards/sipeed-maix-bit.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:sipeed-maix-bit]
  platform = kendryte210
  board = sipeed-maix-bit

  ; change microcontroller
  board_build.mcu = K210

  ; change MCU frequency
  board_build.f_cpu = 400000000L


Uploading
---------
Sipeed MAIX BiT supports the next uploading protocols:

* ``iot-bus-jtag``
* ``jlink``
* ``kflash``
* ``minimodule``
* ``olimex-arm-usb-ocd``
* ``olimex-arm-usb-ocd-h``
* ``olimex-arm-usb-tiny-h``
* ``olimex-jtag-tiny``
* ``sipeed-rv-debugger``
* ``tumpa``

Default protocol is ``kflash``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:sipeed-maix-bit]
  platform = kendryte210
  board = sipeed-maix-bit

  upload_protocol = kflash

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

Sipeed MAIX BiT does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_iot-bus-jtag`
    - 
    - Yes
  * - :ref:`debugging_tool_jlink`
    - 
    - 
  * - :ref:`debugging_tool_minimodule`
    - 
    - 
  * - :ref:`debugging_tool_olimex-arm-usb-ocd`
    - 
    - 
  * - :ref:`debugging_tool_olimex-arm-usb-ocd-h`
    - 
    - 
  * - :ref:`debugging_tool_olimex-arm-usb-tiny-h`
    - 
    - 
  * - :ref:`debugging_tool_olimex-jtag-tiny`
    - 
    - 
  * - :ref:`debugging_tool_sipeed-rv-debugger`
    - 
    - 
  * - :ref:`debugging_tool_tumpa`
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

    * - :ref:`framework_kendryte-freertos-sdk`
      - Kendryte SDK with FreeRTOS support

    * - :ref:`framework_kendryte-standalone-sdk`
      - Kendryte Standalone SDK without OS support