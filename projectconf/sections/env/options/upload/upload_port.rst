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

.. _projectconf_upload_port:

``upload_port``
---------------

Type: ``String (Pattern)`` | Multiple: ``No``

This option is used by "uploader" tool when sending firmware to board via
``upload_port``. For example,

* ``/dev/ttyUSB0`` - Serial port (Unix-based OS)
* ``COM3`` - Serial port (Windows OS)
* ``192.168.0.13`` - IP address when using OTA
* ``/media/disk`` - physical path to media disk/flash drive
  (:ref:`framework_mbed` enabled boards)
* ``D:`` - physical path to media disk/flash drive (Windows OS).

If ``upload_port`` isn't specified, then *PlatformIO* will try to detect it
automatically.

To print all available serial ports please use :ref:`cmd_device_list` command.

This option can also be set by global environment variable
:envvar:`PLATFORMIO_UPLOAD_PORT`.

Please note that you can use patterns:

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

**Example**

.. code-block:: ini

    [env:uno]
    platform = atmelavr
    framework = arduino
    ; any port that starts with /dev/ttyUSB
    upload_port = /dev/ttyUSB*

    ; COM1 or COM3
    upload_port = COM[13]