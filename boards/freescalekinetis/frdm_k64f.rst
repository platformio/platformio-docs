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

.. _board_freescalekinetis_frdm_k64f:

Freescale Kinetis FRDM-K64F
===========================

.. contents::

Platform :ref:`platform_freescalekinetis`: Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

System
------

.. list-table::

  * - **Microcontroller**
    - MK64FN1M0VLL12
  * - **Frequency**
    - 120Mhz
  * - **Flash**
    - 1MB
  * - **RAM**
    - 256KB
  * - **Vendor**
    - `Freescale <https://developer.mbed.org/platforms/FRDM-K64F/?utm_source=platformio&utm_medium=docs>`__


Configuration
-------------

Please use ``frdm_k64f`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:frdm_k64f]
  platform = freescalekinetis
  board = frdm_k64f

You can override default Freescale Kinetis FRDM-K64F settings per build environment using
``board_{JSON.PATH}`` option, where ``{JSON.PATH}`` is a path from
board manifest `frdm_k64f.json <https://github.com/platformio/platform-freescalekinetis/blob/master/boards/frdm_k64f.json>`_. For example,

.. code-block:: ini

  [env:frdm_k64f]
  platform = freescalekinetis
  board = frdm_k64f

  ; change microcontroller
  board_build.mcu = mk64fn1m0vll12

  ; change MCU frequency
  board_build.f_cpu = 120000000L


Uploading
---------
Freescale Kinetis FRDM-K64F supports the next uploading protocols:

* ``cmsis-dap``
* ``jlink``
* ``mbed``

Default protocol is ``mbed``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:frdm_k64f]
  platform = freescalekinetis
  board = frdm_k64f

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

Freescale Kinetis FRDM-K64F has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
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

    * - :ref:`framework_mbed`
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.