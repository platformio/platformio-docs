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

Configuration
-------------

.. contents::
    :local:

LoRaWAN
~~~~~~~

LoRaWAN protocol can be configured in :ref:`projectconf` using the following syntax
``board_build.arduino.lorawan.*`` where ``*`` is an option from the following list:

  .. list-table::
    :header-rows:  1
    :widths: 1 2 3 1

    * - Option
      - Description
      - Possible values
      - Default

    * - ``region``
      - Region definition
      - ``AS923``, ``AU915``, ``CN470``, ``CN779``, ``EU433``, ``EU868``,
        ``KR920``, ``IN865``, ``US915``, ``US915_HYBRID``
      - ``AS923``

    * - ``class``
      - Device class
      - ``CLASS_A``, ``CLASS_C``
      - ``CLASS_A``

    * - ``netmode``
      - Activation method
      - ``OTAA``, ``ABP``
      - ``OTAA``

    * - ``adr``
      - Adaptive Data Rate
      - ``ON``, ``OFF``
      - ``ON``

    * - ``uplinkmode``
      - Uplink confirmed/unconfirmed messages
      - ``CONFIRMED``, ``UNCONFIRMED``
      - ``CONFIRMED``

    * - ``net_reserve``
      - Don't rejoin after reset
      - ``ON``, ``OFF``
      - ``OFF``

    * - ``at_support``
      - AT commands support
      - ``ON``, ``OFF``
      - ``ON``

    * - ``rgb``
      - RGB light for LoRaWAN status
      - ``ACTIVE``, ``DEACTIVE``
      - ``ACTIVE``

    * - ``debug_level``
      - Print LoRaWAN relevant messages print to serial port
      - ``NONE``, ``FREQ`` (Sending/receiving frequency), ``FREQ_AND_DIO``
        (Sending/receiving frequency and DIO pin interrupt information)
      - ``NONE``

**Example**

.. code-block:: ini

    [env:cubecell_board]
    platform = asrmicro650x
    framework = arduino
    board = cubecell_board
    board_build.arduino.lorawan.region = EU433
    board_build.arduino.lorawan.adr = OFF
    board_build.arduino.lorawan.debug_level = FREQ_AND_DIO


More information about LoRaWAN configuration can be found in
`the official CubeCell documentation <https://heltec-automation-docs.readthedocs.io/en/latest/cubecell/index.html>`__.
