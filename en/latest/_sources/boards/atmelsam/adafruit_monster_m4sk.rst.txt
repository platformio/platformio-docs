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

.. _board_atmelsam_adafruit_monster_m4sk:

Adafruit MONSTER M4SK
=====================

.. contents::

Hardware
--------

Platform :ref:`platform_atmelsam`: Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

.. list-table::

  * - **Microcontroller**
    - SAMD51G19A
  * - **Frequency**
    - 120MHz
  * - **Flash**
    - 496KB
  * - **RAM**
    - 192KB
  * - **Vendor**
    - `Adafruit <https://www.adafruit.com/product/4343?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``adafruit_monster_m4sk`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:adafruit_monster_m4sk]
  platform = atmelsam
  board = adafruit_monster_m4sk

You can override default Adafruit MONSTER M4SK settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `adafruit_monster_m4sk.json <https://github.com/platformio/platform-atmelsam/blob/master/boards/adafruit_monster_m4sk.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:adafruit_monster_m4sk]
  platform = atmelsam
  board = adafruit_monster_m4sk

  ; change microcontroller
  board_build.mcu = samd51g19a

  ; change MCU frequency
  board_build.f_cpu = 120000000L


Uploading
---------
Adafruit MONSTER M4SK supports the next uploading protocols:

* ``atmel-ice``
* ``jlink``
* ``sam-ba``

Default protocol is ``sam-ba``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:adafruit_monster_m4sk]
  platform = atmelsam
  board = adafruit_monster_m4sk

  upload_protocol = sam-ba

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

Adafruit MONSTER M4SK does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_atmel-ice`
    - 
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
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences