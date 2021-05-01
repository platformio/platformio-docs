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

.. _debugging_tool_ovpsim:

OVPsim
======

.. image:: ../../_static/images/debug_probes/renode.png
  :target: https://www.ovpworld.org/?utm_source=platformio&utm_medium=docs

OVPsim is a multiprocessor platform emulator (often called a full-system simulator)
used to run unchanged production binaries of the target hardware. It has public APIs
allowing users to create their own processor, peripheral and platform models.
Various models are available as open source. For more information, see `OVPsim's official website <https://www.ovpworld.org/?utm_source=platformio&utm_medium=docs>`__.

.. contents:: Contents
    :local:

.. begin_platforms

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_openhw`
      - OpenHW Group is a not-for-profit, global organization that provides an infrastructure for hosting high quality open-source HW developments in line with industry best practices. The OpenHW CV32E40P RISC-V core is the first open-source core for high-volume chips verified with the state-of-the-art process required for high-integrity, commercial SoCs.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_pulp-runtime`
      - Runtime Environment for Parallel Ultra Low Power platform targeting high energy efficiencies

    * - :ref:`framework_pulp-sdk`
      - Software Development Kit for Parallel Ultra Low Power platform targeting high energy efficiencies

Boards
------

.. note::
    For more detailed ``board`` information please scroll tables below by horizontal.


.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_openhw_nexys_a7`
      - :ref:`platform_openhw`
      - On-board
      - 
      - 320MHz
      - 16MB
      - 1.16MB
