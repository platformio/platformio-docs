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

.. _projectconf_upload_speed:

``upload_speed``
----------------

Type: ``Number`` | Multiple: ``No``

A connection speed (`baud rate <http://en.wikipedia.org/wiki/Baud>`_)
which "uploader" tool uses when sending firmware to board.

Common baud rates:
================================
Below are common baud rates for reference:

.. list-table::
   :widths: 15 15 25 20 25 25
   :header-rows: 1

   * - Bauds
     - Bits/s
     - Bit duration
     - Speed (bytes/s)
     - Actual speed (bytes/s)
     - Actual byte duration

   * - 9600
     - 9600
     - 104.167 µs
     - 1200
     - 960
     - 1.042 ms

   * - 19200
     - 19200
     - 52.083 µs
     - 2400
     - 1920
     - 520.833 µs

   * - 57600
     - 57600
     - 17.361 µs
     - 7200
     - 5760
     - 173.611 µs

   * - 115200
     - 115200
     - 8.681 µs
     - 14400
     - 11520
     - 86.806 µs


`Reference <https://lucidar.me/en/serialib/most-used-baud-rates-table/>`_
