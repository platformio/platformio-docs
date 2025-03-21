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

.. _board_espressif32_rymcu-esp32-c3-devkitm-1:

RYMCU ESP32-C3-DevKitM-1
========================

.. contents::

Hardware
--------

Platform :ref:`platform_espressif32`: ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and Bluetooth. ESP32 integrates an antenna switch, RF balun, power amplifier, low-noise receive amplifier, filters, and power management modules.

.. list-table::

  * - **Microcontroller**
    - ESP32C3
  * - **Frequency**
    - 160MHz
  * - **Flash**
    - 4MB
  * - **RAM**
    - 320KB
  * - **Vendor**
    - `RYMCU <https://rymcu.com/products?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``rymcu-esp32-c3-devkitm-1`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:rymcu-esp32-c3-devkitm-1]
  platform = espressif32
  board = rymcu-esp32-c3-devkitm-1

You can override default RYMCU ESP32-C3-DevKitM-1 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `rymcu-esp32-c3-devkitm-1.json <https://github.com/platformio/platform-espressif32/blob/master/boards/rymcu-esp32-c3-devkitm-1.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:rymcu-esp32-c3-devkitm-1]
  platform = espressif32
  board = rymcu-esp32-c3-devkitm-1

  ; change microcontroller
  board_build.mcu = esp32c3

  ; change MCU frequency
  board_build.f_cpu = 160000000L


Uploading
---------
RYMCU ESP32-C3-DevKitM-1 supports the following uploading protocols:

* ``cmsis-dap``
* ``esp-bridge``
* ``esp-builtin``
* ``esp-prog``
* ``espota``
* ``esptool``
* ``iot-bus-jtag``
* ``jlink``
* ``minimodule``
* ``olimex-arm-usb-ocd``
* ``olimex-arm-usb-ocd-h``
* ``olimex-arm-usb-tiny-h``
* ``olimex-jtag-tiny``
* ``tumpa``

Default protocol is ``esptool``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:rymcu-esp32-c3-devkitm-1]
  platform = espressif32
  board = rymcu-esp32-c3-devkitm-1

  upload_protocol = esptool

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

RYMCU ESP32-C3-DevKitM-1 does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_cmsis-dap`
    - 
    - Yes
  * - ``esp-bridge``
    - 
    - 
  * - ``esp-builtin``
    - 
    - 
  * - :ref:`debugging_tool_esp-prog`
    - 
    - 
  * - :ref:`debugging_tool_iot-bus-jtag`
    - 
    - 
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
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_espidf`
      - Espressif IoT Development Framework. Official development framework for ESP32 chip