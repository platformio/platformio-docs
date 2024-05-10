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

Common baud rates
-----------------

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

   * - 50
     - 50
     - 20.000 ms
     - 6.25
     - 5
     - 200.000 ms

   * - 75
     - 75
     - 13.333 ms
     - 9.375
     - 7.5
     - 133.333 ms

   * - 110
     - 110
     - 9.091 ms
     - 13.75
     - 11
     - 90.909 ms

   * - 134
     - 134
     - 7.463 ms
     - 16.75
     - 13.4
     - 74.627 ms

   * - 150
     - 150
     - 6.667 ms
     - 18.75
     - 15
     - 66.667 ms

   * - 200
     - 200
     - 5.000 ms
     - 25
     - 20
     - 50.000 ms

   * - 300
     - 300
     - 3.333 ms
     - 37.5
     - 30
     - 33.333 ms

   * - 600
     - 600
     - 1.667 ms
     - 75
     - 60
     - 16.667 ms

   * - 1200
     - 1200
     - 833.333 µs
     - 150
     - 120
     - 8.333 ms

   * - 1800
     - 1800
     - 555.556 µs
     - 225
     - 180
     - 5.556 ms

   * - 2400
     - 2400
     - 416.667 µs
     - 300
     - 240
     - 4.167 ms

   * - 4800
     - 4800
     - 208.333 µs
     - 600
     - 480
     - 2.083 ms

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

   * - 28800
     - 28800
     - 34.722 µs
     - 3600
     - 2880
     - 347.222 µs

   * - 38400
     - 38400
     - 26.042 µs
     - 4800
     - 3840
     - 260.417 µs

   * - 57600
     - 57600
     - 17.361 µs
     - 7200
     - 5760
     - 173.611 µs

   * - 76800
     - 76800
     - 13.021 µs
     - 9600
     - 7680
     - 130.208 µs

   * - 115200
     - 115200
     - 8.681 µs
     - 14400
     - 11520
     - 86.806 µs

   * - 230400
     - 230400
     - 4.340 µs
     - 28800
     - 23040
     - 43.403 µs

   * - 460800
     - 460800
     - 2.170 µs
     - 57600
     - 46080
     - 21.701 µs

   * - 576000
     - 576000
     - 1.736 µs
     - 72000
     - 57600
     - 17.361 µs

   * - 921600
     - 921600
     - 1.085 µs
     - 115200
     - 92160
     - 10.851 µs


.. _Credit to: Philippe Lucidarme (lucidar.me)

