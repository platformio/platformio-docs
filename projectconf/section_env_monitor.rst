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

.. _projectconf_section_env_monitor:

Monitor options
---------------

.. contents::
    :local:

Custom options for :ref:`cmd_device_monitor` command.

.. _projectconf_monitor_port:

``monitor_port``
^^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``No``

Port, a number or a device name, or valid `URL Handlers <https://pyserial.readthedocs.io/en/latest/url_handlers.html#urls>`__.
See :option:`pio device monitor --port`. To print all available serial ports please use :ref:`cmd_device_list` command.

Please note that you can use Unix shell-style wildcards:

.. list-table::
    :header-rows:  1

    * - Pattern
      - Meaning

    * - ``*``
      - matches everything

    * - ``?``
      - matches any single character

    * - ``[seq]``
      - matches any character in seq

    * - ``[!seq]``
      - matches any character not in seq

Example:

.. code-block:: ini

    [env:custom_monitor_port]
    ...
    ; Unix
    monitor_port = /dev/ttyUSB1

    ; Windows, COM1 or COM3
    monitor_port = COM[13]

    ; Socket
    monitor_port = socket://localhost:4444

.. _projectconf_monitor_speed:

``monitor_speed``
^^^^^^^^^^^^^^^^^

Type: ``Integer`` | Multiple: ``No`` | Default: ``9600``

A monitor speed (`baud rate <http://en.wikipedia.org/wiki/Baud>`_).
See :option:`pio device monitor --baud`.

Example:

.. code-block:: ini

    [env:custom_monitor_speedrate]
    ...
    monitor_speed = 115200

.. _projectconf_monitor_filters:

``monitor_filters``
^^^^^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``Yes``

Apply filters and text transformation for device output. See available filters at
:ref:`cmd_device_monitor_filters`.

Example:

.. code-block:: ini

    [env:log_output_to_file_with_timestamp]
    ...
    platform = ...
    monitor_filters = log2file, time, default

.. _projectconf_monitor_rts:

``monitor_rts``
^^^^^^^^^^^^^^^

Type: ``Integer (0 or 1)`` | Multiple: ``No``

A monitor initial ``RTS`` line state. See :option:`pio device monitor --rts`.

.. _projectconf_monitor_dtr:

``monitor_dtr``
^^^^^^^^^^^^^^^

Type: ``Integer (0 or 1)`` | Multiple: ``No``

A monitor initial ``DTR`` line state. See :option:`pio device monitor --dtr`.

.. _projectconf_monitor_flags:

``monitor_flags``
^^^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``Yes``

Pass extra flags and options to :ref:`cmd_device_monitor` command. Please note
that each flag, option or its value should be passed in a new line. See
example below.

Available flags and options are the same which are documented for
:ref:`cmd_device_monitor` command.

Example:

.. code-block:: ini

    [env:extra_monitor_flags]
    platform = ...
    board = ...
    monitor_flags=
        --parity
        N
        --encoding
        hexlify
