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

.. _board_shakti_vajra:

Vajra on Arty A7-100: Artix-7 FPGA Development Board
====================================================

.. contents::

Hardware
--------

Platform :ref:`platform_shakti`: Shakti is an open-source initiative by the RISE group at IIT-Madras, which is not only building open source, production grade processors, but also associated components like interconnect fabrics, verification tools, storage controllers, peripheral IPs and SOC tools.

.. list-table::

  * - **Microcontroller**
    - C-CLASS
  * - **Frequency**
    - 50MHz
  * - **Flash**
    - 0B
  * - **RAM**
    - 128MB
  * - **Vendor**
    - `Xilinx <https://www.xilinx.com/products/boards-and-kits/1-w51quh.html?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``vajra`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:vajra]
  platform = shakti
  board = vajra

You can override default Vajra on Arty A7-100: Artix-7 FPGA Development Board settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `vajra.json <https://github.com/platformio/platform-shakti/blob/master/boards/vajra.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:vajra]
  platform = shakti
  board = vajra

  ; change microcontroller
  board_build.mcu = C-Class

  ; change MCU frequency
  board_build.f_cpu = 50000000L


Uploading
---------
Vajra on Arty A7-100: Artix-7 FPGA Development Board supports the next uploading protocols:

* ``ftdi``
* ``ftdi``
* ``jlink``
* ``jlink``

Default protocol is ``ftdi``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:vajra]
  platform = shakti
  board = vajra

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

Vajra on Arty A7-100: Artix-7 FPGA Development Board has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

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

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_shakti-sdk`
      - A software development kit for developing applications on Shakti class of processors