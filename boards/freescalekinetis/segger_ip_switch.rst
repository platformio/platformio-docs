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

.. _board_freescalekinetis_segger_ip_switch:

SEGGER IP Switch Board
======================

.. contents::

Hardware
--------

Platform :ref:`platform_freescalekinetis`: Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

.. list-table::

  * - **Microcontroller**
    - MK66FN2M0VMD18
  * - **Frequency**
    - 180MHz
  * - **Flash**
    - 2MB
  * - **RAM**
    - 256KB
  * - **Vendor**
    - `SEGGER <https://www.segger.com/evaluate-our-software/segger/embosip-switch-board/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``segger_ip_switch`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:segger_ip_switch]
  platform = freescalekinetis
  board = segger_ip_switch

You can override default SEGGER IP Switch Board settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `segger_ip_switch.json <https://github.com/platformio/platform-freescalekinetis/blob/master/boards/segger_ip_switch.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:segger_ip_switch]
  platform = freescalekinetis
  board = segger_ip_switch

  ; change microcontroller
  board_build.mcu = mk66fn2m0vmd18

  ; change MCU frequency
  board_build.f_cpu = 180000000L


Uploading
---------
SEGGER IP Switch Board supports the next uploading protocols:

* ``jlink``
* ``mbed``

Default protocol is ``jlink``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:segger_ip_switch]
  platform = freescalekinetis
  board = segger_ip_switch

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

SEGGER IP Switch Board does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_jlink`
    - 
    - Yes

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_zephyr`
      - The Zephyr Project is a scalable real-time operating system (RTOS) supporting multiple hardware architectures, optimized for resource constrained devices, and built with safety and security in mind