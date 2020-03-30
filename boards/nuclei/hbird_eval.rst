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

.. _board_nuclei_hbird_eval:

HummingBird Evaluation Kit
==========================

.. contents::

Hardware
--------

Platform :ref:`platform_nuclei`: Find professional RISC-V Processor IP in Nuclei, first professional RISC-V IP company in Mainland China, match all your requirements in AIoT Era.

.. list-table::

  * - **Microcontroller**
    - HUMMINGBIRD
  * - **Frequency**
    - 5MHz
  * - **Flash**
    - 64KB
  * - **RAM**
    - 64KB
  * - **Vendor**
    - `Nuclei <https://nucleisys.com/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``hbird_eval`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:hbird_eval]
  platform = nuclei
  board = hbird_eval

You can override default HummingBird Evaluation Kit settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `hbird_eval.json <https://github.com/Nuclei-Software/platform-nuclei/blob/master/boards/hbird_eval.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:hbird_eval]
  platform = nuclei
  board = hbird_eval

  ; change microcontroller
  board_build.mcu = HummingBird

  ; change MCU frequency
  board_build.f_cpu = 5000000L

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

HummingBird Evaluation Kit has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_rv-link`
    - Yes
    - Yes

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_nuclei-sdk`
      - Open Source Software Development Kit for the Nuclei N/NX processors