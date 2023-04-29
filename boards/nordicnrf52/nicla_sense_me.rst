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

.. _board_nordicnrf52_nicla_sense_me:

Arduino Nicla Sense ME
======================

.. contents::

Hardware
--------

Platform :ref:`platform_nordicnrf52`: The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor which makes them quite capable Bluetooth Smart SoCs.

.. list-table::

  * - **Microcontroller**
    - NRF52832
  * - **Frequency**
    - 64MHz
  * - **Flash**
    - 515.25KB
  * - **RAM**
    - 62.78KB
  * - **Vendor**
    - `Arduino <https://docs.arduino.cc/hardware/nicla-sense-me?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``nicla_sense_me`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:nicla_sense_me]
  platform = nordicnrf52
  board = nicla_sense_me

You can override default Arduino Nicla Sense ME settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `nicla_sense_me.json <https://github.com/platformio/platform-nordicnrf52/blob/master/boards/nicla_sense_me.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:nicla_sense_me]
  platform = nordicnrf52
  board = nicla_sense_me

  ; change microcontroller
  board_build.mcu = nrf52832

  ; change MCU frequency
  board_build.f_cpu = 64000000L


Uploading
---------
Arduino Nicla Sense ME supports the following uploading protocols:

* ``blackmagic``
* ``cmsis-dap``
* ``jlink``
* ``nrfjprog``
* ``nrfutil``
* ``sam-ba``

Default protocol is ``cmsis-dap``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:nicla_sense_me]
  platform = nordicnrf52
  board = nicla_sense_me

  upload_protocol = cmsis-dap

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

Arduino Nicla Sense ME has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_blackmagic`
    - 
    - 
  * - :ref:`debugging_tool_cmsis-dap`
    - Yes
    - Yes
  * - :ref:`debugging_tool_jlink`
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