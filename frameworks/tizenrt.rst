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

.. _framework_tizenrt:

Tizen RT
========
:ref:`projectconf_env_framework` = ``tizenrt``

Tizen RT is a lightweight RTOS-based platform to support low-end IoT devices

For more detailed information please visit `vendor site <https://source.tizen.org/documentation/tizen-rt>`_.


.. contents:: Contents
    :local:

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_samsung_artik`
      - The Samsung ARTIK Smart IoT platform brings hardware modules and cloud services together, with built-in security and an ecosystem of tools and partners to speed up your time-to-market.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by horizontal.

Samsung
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``artik_053``
      - `Samsung ARTIK053 <http://www.artik.io>`_
      - :ref:`Samsung ARTIK <platform_samsung_artik>`
      - :ref:`Yes <piodebug>`
      - S5JT200
      - 320 MHz
      - 8192 Kb
      - 1280 Kb
