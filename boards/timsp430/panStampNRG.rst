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

.. _board_timsp430_panStampNRG:

PanStamp NRG 1.1
================

.. contents::

Platform :ref:`platform_timsp430`: MSP430 microcontrollers (MCUs) from Texas Instruments (TI) are 16-bit, RISC-based, mixed-signal processors designed for ultra-low power. These MCUs offer the lowest power consumption and the perfect mix of integrated peripherals for thousands of applications.

System
------

.. list-table::

  * - **Microcontroller**
    - CC430F5137
  * - **Frequency**
    - 12Mhz
  * - **Flash**
    - 31.88KB
  * - **RAM**
    - 4KB
  * - **Vendor**
    - `PanStamp <http://www.panstamp.com/product/197/?utm_source=platformio&utm_medium=docs>`__


Configuration
-------------

Please use ``panStampNRG`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:panStampNRG]
  platform = timsp430
  board = panStampNRG

You can override default PanStamp NRG 1.1 settings per build environment using
``board_{JSON.PATH}`` option, where ``{JSON.PATH}`` is a path from
board manifest `panStampNRG.json <https://github.com/platformio/platform-timsp430/blob/master/boards/panStampNRG.json>`_. For example,

.. code-block:: ini

  [env:panStampNRG]
  platform = timsp430
  board = panStampNRG

  ; change microcontroller
  board_build.mcu = cc430f5137

  ; change MCU frequency
  board_build.f_cpu = 12000000L

Debugging
---------
:ref:`piodebug` currently does not support PanStamp NRG 1.1 board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.