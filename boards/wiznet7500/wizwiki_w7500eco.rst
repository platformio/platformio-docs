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

.. _board_wiznet7500_wizwiki_w7500eco:

WIZwiki-W7500ECO
================

.. contents::

Hardware
--------

Platform :ref:`platform_wiznet7500`: The IOP (Internet Offload Processor) W7500 is the one-chip solution which integrates an ARM Cortex-M0, 128KB Flash and hardwired TCP/IP core for various embedded application platform especially requiring Internet of things

.. list-table::

  * - **Microcontroller**
    - WIZNET7500ECO
  * - **Frequency**
    - 48MHz
  * - **Flash**
    - 128KB
  * - **RAM**
    - 48KB
  * - **Vendor**
    - `WIZNet <https://developer.mbed.org/platforms/WIZwiki-W7500ECO/?utm_source=platformio&utm_medium=docs>`__


Configuration
-------------

Please use ``wizwiki_w7500eco`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:wizwiki_w7500eco]
  platform = wiznet7500
  board = wizwiki_w7500eco

You can override default WIZwiki-W7500ECO settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `wizwiki_w7500eco.json <https://github.com/platformio/platform-wiznet7500/blob/master/boards/wizwiki_w7500eco.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:wizwiki_w7500eco]
  platform = wiznet7500
  board = wizwiki_w7500eco

  ; change microcontroller
  board_build.mcu = wiznet7500eco

  ; change MCU frequency
  board_build.f_cpu = 48000000L


Uploading
---------
WIZwiki-W7500ECO supports the next uploading protocols:

* ``cmsis-dap``
* ``jlink``
* ``mbed``

Default protocol is ``mbed``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:wizwiki_w7500eco]
  platform = wiznet7500
  board = wizwiki_w7500eco

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

WIZwiki-W7500ECO has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

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