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

.. _projectconf_monitor_port:

``monitor_port``
----------------

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
