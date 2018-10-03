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

.. _board_samsung_artik_artik_053:

Samsung ARTIK053
================

.. contents::

Platform :ref:`platform_samsung_artik`: The Samsung ARTIK Smart IoT platform brings hardware modules and cloud services together, with built-in security and an ecosystem of tools and partners to speed up your time-to-market.

System
------

.. list-table::

  * - **Microcontroller**
    - S5JT200
  * - **Frequency**
    - 320Mhz
  * - **Flash**
    - 8MB
  * - **RAM**
    - 1.25MB
  * - **Vendor**
    - `Samsung <http://www.artik.io?utm_source=platformio&utm_medium=docs>`__


Configuration
-------------

Please use ``artik_053`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:artik_053]
  platform = samsung_artik
  board = artik_053

You can override default Samsung ARTIK053 settings per build environment using
``board_{JSON.PATH}`` option, where ``{JSON.PATH}`` is a path from
board manifest `artik_053.json <https://github.com/platformio/platform-samsung_artik/blob/master/boards/artik_053.json>`_. For example,

.. code-block:: ini

  [env:artik_053]
  platform = samsung_artik
  board = artik_053

  ; change microcontroller
  board_build.mcu = s5jt200

  ; change MCU frequency
  board_build.f_cpu = 320000000L

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

Samsung ARTIK053 has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_ftdi`
    - Yes
    - Yes

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_tizenrt`
      - Tizen RT is a lightweight RTOS-based platform to support low-end IoT devices