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

Port, a number or a device name, or valid `URL Handlers <https://pyserial.readthedocs.io/en/latest/url_handlers.html>`__.

To print all available serial ports please use :ref:`cmd_device_list` command.

Please note that you can use patterns for serial ports:

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

Type: ``Number`` | Multiple: ``No`` | Default: ``9600``

A monitor speed (`baud rate <http://en.wikipedia.org/wiki/Baud>`_).
See :option:`pio device monitor --baud`.

Example:

.. code-block:: ini

    [env:custom_monitor_speedrate]
    ...
    monitor_speed = 115200

.. _projectconf_monitor_parity:

``monitor_parity``
^^^^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``No`` | Default: ``N``

Enable parity checking. See :option:`pio device monitor --parity`
for the available values.

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
    monitor_filters =
      default   ; Remove typical terminal control codes from input
      time      ; Add timestamp with milliseconds for each new line
      log2file  ; Log data to a file “platformio-device-monitor-*.log” located in the current working directory

.. _projectconf_monitor_rts:

``monitor_rts``
^^^^^^^^^^^^^^^

Type: ``Number (0 or 1)`` | Multiple: ``No``

A monitor initial ``RTS`` line state. See :option:`pio device monitor --rts`.

.. _projectconf_monitor_dtr:

``monitor_dtr``
^^^^^^^^^^^^^^^

Type: ``Number (0 or 1)`` | Multiple: ``No``

A monitor initial ``DTR`` line state. See :option:`pio device monitor --dtr`.

.. _projectconf_monitor_eol:

``monitor_eol``
^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``No`` | Default: ``CRLF``

A monitor end of line mode. See :option:`pio device monitor --eol`.

.. _projectconf_monitor_raw:

``monitor_raw``
^^^^^^^^^^^^^^^

Type: ``Bool (yes or no)`` | Multiple: ``No`` | Default: ``no``

Disable encodings/transformations of device output.
See :option:`pio device monitor --raw`.

.. _projectconf_monitor_echo:

``monitor_echo``
^^^^^^^^^^^^^^^^

Type: ``Bool (yes or no)`` | Multiple: ``No`` | Default: ``no``

Enable a monitor local echo. See :option:`pio device monitor --echo`.

.. _projectconf_monitor_encoding:

``monitor_encoding``
^^^^^^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``No`` | Default: ``UTF-8``

Set the encoding for the serial port. See :option:`pio device monitor --encoding`.
