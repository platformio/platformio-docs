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

.. _framework_shakti-sdk:

Shakti SDK
==========

:Configuration:
  :ref:`projectconf_env_framework` = ``shakti-sdk``

A software development kit for developing applications on Shakti class of processors

.. contents:: Contents
    :local:
    :depth: 1

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_shakti`
      - Shakti is an open-source initiative by the RISE group at IIT-Madras, which is not only building open source, production grade processors, but also associated components like interconnect fabrics, verification tools, storage controllers, peripheral IPs and SOC tools.

Examples
--------

* `Shakti SDK for Shakti <https://github.com/platformio/platform-shakti/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. contents::
    :local:


Tools & Debug Probes
~~~~~~~~~~~~~~~~~~~~

Supported debugging tools are listed in "Debug" column. For more detailed
information, please scroll table by horizontal.
You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further instructions.


On-Board Debug Tools
^^^^^^^^^^^^^^^^^^^^

Boards listed below have on-board debug probe and **ARE READY** for debugging!
You do not need to use/buy external debug probe.


.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_shakti_artix7_35t`
      - :ref:`platform_shakti`
      - E-CLASS
      - 50MHz
      - 0B
      - 128KB
    * - :ref:`board_shakti_artix7_100t`
      - :ref:`platform_shakti`
      - C-CLASS
      - 50MHz
      - 0B
      - 128MB
    * - :ref:`board_shakti_parashu`
      - :ref:`platform_shakti`
      - E-CLASS
      - 50MHz
      - 0B
      - 128KB
    * - :ref:`board_shakti_pinaka`
      - :ref:`platform_shakti`
      - E-CLASS
      - 50MHz
      - 0B
      - 128KB
    * - :ref:`board_shakti_vajra`
      - :ref:`platform_shakti`
      - C-CLASS
      - 50MHz
      - 0B
      - 128MB


Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command
    * For more detailed ``board`` information please scroll the tables below by horizontally.

Xilinx
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_shakti_artix7_35t`
      - :ref:`platform_shakti`
      - On-board
      - E-CLASS
      - 50MHz
      - 0B
      - 128KB
    * - :ref:`board_shakti_artix7_100t`
      - :ref:`platform_shakti`
      - On-board
      - C-CLASS
      - 50MHz
      - 0B
      - 128MB
    * - :ref:`board_shakti_parashu`
      - :ref:`platform_shakti`
      - On-board
      - E-CLASS
      - 50MHz
      - 0B
      - 128KB
    * - :ref:`board_shakti_pinaka`
      - :ref:`platform_shakti`
      - On-board
      - E-CLASS
      - 50MHz
      - 0B
      - 128KB
    * - :ref:`board_shakti_vajra`
      - :ref:`platform_shakti`
      - On-board
      - C-CLASS
      - 50MHz
      - 0B
      - 128MB
