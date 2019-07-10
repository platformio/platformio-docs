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

.. _board_sifive_e310-arty:

Arty FPGA Dev Kit
=================

.. contents::

Hardware
--------

Platform :ref:`platform_sifive`: SiFive brings the power of open source and software automation to the semiconductor industry, making it possible to develop new hardware faster and more affordably than ever before. 

.. list-table::

  * - **Microcontroller**
    - FE310
  * - **Frequency**
    - 450MHz
  * - **Flash**
    - 16MB
  * - **RAM**
    - 256MB
  * - **Vendor**
    - `Xilinx <https://store.digilentinc.com/arty-a7-artix-7-fpga-development-board-for-makers-and-hobbyists/?utm_source=platformio&utm_medium=docs>`__


Configuration
-------------

Please use ``e310-arty`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:e310-arty]
  platform = sifive
  board = e310-arty

You can override default Arty FPGA Dev Kit settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `e310-arty.json <https://github.com/platformio/platform-sifive/blob/master/boards/e310-arty.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:e310-arty]
  platform = sifive
  board = e310-arty

  ; change microcontroller
  board_build.mcu = fe310

  ; change MCU frequency
  board_build.f_cpu = 450000000L


Uploading
---------
Arty FPGA Dev Kit supports the next uploading protocols:

* ``ftdi``
* ``jlink``
* ``minimodule``
* ``olimex-arm-usb-ocd``
* ``olimex-arm-usb-ocd-h``
* ``olimex-arm-usb-tiny-h``
* ``olimex-jtag-tiny``
* ``tumpa``

Default protocol is ``ftdi``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:e310-arty]
  platform = sifive
  board = e310-arty

  upload_protocol = ftdi

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

Arty FPGA Dev Kit has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_ftdi`
    - Yes
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
  * - :ref:`debugging_tool_qemu`
    - Yes
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

    * - :ref:`framework_freedom-e-sdk`
      - Open Source Software for Developing on the SiFive Freedom E Platform