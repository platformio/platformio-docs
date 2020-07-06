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

.. _board_gd32v_gd32vf103v-eval:

GD32VF103V-EVAL
===============

.. contents::

Hardware
--------

Platform :ref:`platform_gd32v`: The GigaDevice GD32V device is a 32-bit general-purpose microcontroller based on the RISC-V core with an impressive balance of processing power, reduced power consumption and peripheral set.

.. list-table::

  * - **Microcontroller**
    - GD32VF103VBT6
  * - **Frequency**
    - 108MHz
  * - **Flash**
    - 128KB
  * - **RAM**
    - 32KB
  * - **Vendor**
    - `Sipeed <https://www.sipeed.com/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``gd32vf103v-eval`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:gd32vf103v-eval]
  platform = gd32v
  board = gd32vf103v-eval

You can override default GD32VF103V-EVAL settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `gd32vf103v-eval.json <https://github.com/sipeed/platform-gd32v/blob/master/boards/gd32vf103v-eval.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:gd32vf103v-eval]
  platform = gd32v
  board = gd32vf103v-eval

  ; change microcontroller
  board_build.mcu = GD32VF103VBT6

  ; change MCU frequency
  board_build.f_cpu = 108000000L


Uploading
---------
GD32VF103V-EVAL supports the next uploading protocols:

* ``altera-usb-blaster``
* ``gd-link``
* ``jlink``
* ``rv-link``
* ``serial``
* ``sipeed-rv-debugger``
* ``um232h``

Default protocol is ``gd-link``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:gd32vf103v-eval]
  platform = gd32v
  board = gd32vf103v-eval

  upload_protocol = gd-link

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

GD32VF103V-EVAL does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_altera-usb-blaster`
    - 
    - Yes
  * - :ref:`debugging_tool_gd-link`
    - 
    - 
  * - :ref:`debugging_tool_jlink`
    - 
    - 
  * - :ref:`debugging_tool_rv-link`
    - 
    - 
  * - :ref:`debugging_tool_sipeed-rv-debugger`
    - 
    - 
  * - :ref:`debugging_tool_um232h`
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

    * - :ref:`framework_gd32vf103-sdk`
      - GigaDevice GD32VF103 Firmware Library (SDK) is a firmware function package, including programs, data structures and macro definitions, all the performance features of peripherals of GD32VF103 devices are involved in the package