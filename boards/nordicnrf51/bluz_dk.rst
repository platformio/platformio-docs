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

.. _board_nordicnrf51_bluz_dk:

BluzDK
======

.. contents::

Hardware
--------

Platform :ref:`platform_nordicnrf51`: The Nordic nRF51 Series is a family of highly flexible, multi-protocol, system-on-chip (SoC) devices for ultra-low power wireless applications. nRF51 Series devices support a range of protocol stacks including Bluetooth Smart (previously called Bluetooth low energy), ANT and proprietary 2.4GHz protocols such as Gazell.

.. list-table::

  * - **Microcontroller**
    - NRF51822
  * - **Frequency**
    - 32MHz
  * - **Flash**
    - 256KB
  * - **RAM**
    - 32KB
  * - **Vendor**
    - `BluzDK <https://bluz.io/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``bluz_dk`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:bluz_dk]
  platform = nordicnrf51
  board = bluz_dk

You can override default BluzDK settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `bluz_dk.json <https://github.com/platformio/platform-nordicnrf51/blob/master/boards/bluz_dk.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:bluz_dk]
  platform = nordicnrf51
  board = bluz_dk

  ; change microcontroller
  board_build.mcu = nrf51822

  ; change MCU frequency
  board_build.f_cpu = 32000000L


Uploading
---------
BluzDK supports the following uploading protocols:

* ``blackmagic``
* ``jlink``
* ``nrfjprog``
* ``stlink``

Default protocol is ``jlink``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:bluz_dk]
  platform = nordicnrf51
  board = bluz_dk

  upload_protocol = jlink

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

BluzDK does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

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

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.