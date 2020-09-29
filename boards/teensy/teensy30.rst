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

.. _board_teensy_teensy30:

Teensy 3.0
==========

.. contents::

Hardware
--------

Platform :ref:`platform_teensy`: Teensy is a complete USB-based microcontroller development system, in a very small footprint, capable of implementing many types of projects. All programming is done via the USB port. No special programmer is needed, only a standard USB cable and a PC or Macintosh with a USB port.

.. list-table::

  * - **Microcontroller**
    - MK20DX128
  * - **Frequency**
    - 48MHz
  * - **Flash**
    - 128KB
  * - **RAM**
    - 16KB
  * - **Vendor**
    - `Teensy <https://www.pjrc.com/store/teensy3.html?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``teensy30`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:teensy30]
  platform = teensy
  board = teensy30

You can override default Teensy 3.0 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `teensy30.json <https://github.com/platformio/platform-teensy/blob/master/boards/teensy30.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:teensy30]
  platform = teensy
  board = teensy30

  ; change microcontroller
  board_build.mcu = mk20dx128

  ; change MCU frequency
  board_build.f_cpu = 48000000L


Uploading
---------
Teensy 3.0 supports the next uploading protocols:

* ``teensy-cli``
* ``teensy-gui``

Default protocol is ``teensy-gui``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:teensy30]
  platform = teensy
  board = teensy30

  upload_protocol = teensy-gui

Debugging
---------
:ref:`piodebug` currently does not support Teensy 3.0 board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences