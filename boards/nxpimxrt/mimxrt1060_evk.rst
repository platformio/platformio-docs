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

.. _board_nxpimxrt_mimxrt1060_evk:

NXP i.MX RT1060 Evaluation Kit
==============================

.. contents::

Hardware
--------

Platform :ref:`platform_nxpimxrt`: The i.MX RT series of crossover processors features the Arm Cortex-M core, real-time functionality and MCU usability at a cost-effective price.

.. list-table::

  * - **Microcontroller**
    - MIMXRT1062DVL6A
  * - **Frequency**
    - 600MHz
  * - **Flash**
    - 8MB
  * - **RAM**
    - 32MB
  * - **Vendor**
    - `NXP <https://www.nxp.com/design/development-boards/i.mx-evaluation-and-development-boards/mimxrt1060-evk-i.mx-rt1060-evaluation-kit:MIMXRT1060-EVK?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``mimxrt1060_evk`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:mimxrt1060_evk]
  platform = nxpimxrt
  board = mimxrt1060_evk

You can override default NXP i.MX RT1060 Evaluation Kit settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `mimxrt1060_evk.json <https://github.com/platformio/platform-nxpimxrt/blob/master/boards/mimxrt1060_evk.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:mimxrt1060_evk]
  platform = nxpimxrt
  board = mimxrt1060_evk

  ; change microcontroller
  board_build.mcu = mimxrt1062dvl6a

  ; change MCU frequency
  board_build.f_cpu = 600000000L


Uploading
---------
NXP i.MX RT1060 Evaluation Kit supports the following uploading protocols:

* ``blackmagic``
* ``jlink``
* ``mbed``

Default protocol is ``mbed``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:mimxrt1060_evk]
  platform = nxpimxrt
  board = mimxrt1060_evk

  upload_protocol = mbed

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

NXP i.MX RT1060 Evaluation Kit has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_blackmagic`
    - 
    - 
  * - :ref:`debugging_tool_jlink`
    - Yes
    - Yes

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_zephyr`
      - Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures