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

.. _cmd_lib_builtin:

pio lib builtin
===============

.. contents::

Usage
-----

.. code-block:: bash

    pio lib builtin [OPTIONS]


Description
-----------

List built-in libraries based on installed :ref:`platforms` and their
frameworks, SDKs, etc.

Options
-------

.. program:: pio lib builtin

.. option::
    --storage

List libraries from specified storages. For example, ``framework-arduinoavr``.

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`_ format

Examples
--------

.. code::

    > pio lib builtin

    framework-arduinoavr
    ********************

    Bridge
    ======
    Enables the communication between the Linux processor and the microcontroller. For Arduino/Genuino Yún, Yún Shield and TRE only.

    Version: 1.6.1
    Homepage: http://www.arduino.cc/en/Reference/YunBridgeLibrary
    Keywords: communication
    Compatible frameworks: arduino
    Compatible platforms: *
    Authors: Arduino

    EEPROM
    ======
    Enables reading and writing to the permanent board storage.

    Version: 2.0
    Homepage: http://www.arduino.cc/en/Reference/EEPROM
    Keywords: data, storage
    Compatible frameworks: arduino
    Compatible platforms: atmelavr
    Authors: Arduino, Christopher Andrews

    ...


    framework-arduinosam
    ********************

    Audio
    =====
    Allows playing audio files from an SD card. For Arduino DUE only.

    Version: 1.0
    Homepage: http://arduino.cc/en/Reference/Audio
    Keywords: signal, input, output
    Compatible frameworks: arduino
    Compatible platforms: atmelsam
    Authors: Arduino

    ...


    framework-arduinoespressif32
    ****************************

    SPI
    ===
    Enables the communication with devices that use the Serial Peripheral Interface (SPI) Bus. For all Arduino boards, BUT Arduino DUE.

    Version: 1.0
    Homepage: http://arduino.cc/en/Reference/SPI
    Keywords: signal, input, output
    Compatible frameworks: arduino
    Compatible platforms:
    Authors: Hristo Gochkov

    ...

    framework-arduinoespressif8266
    ******************************

    ArduinoOTA
    ==========
    Enables Over The Air upgrades, via wifi and espota.py UDP request/TCP download.

    Version: 1.0
    Keywords: communication
    Compatible frameworks: arduino
    Compatible platforms: espressif8266
    Authors: Ivan Grokhotkov and Miguel Angel Ajo

    DNSServer
    =========
    A simple DNS server for ESP8266.

    Version: 1.1.0
    Keywords: communication
    Compatible frameworks: arduino
    Compatible platforms: espressif8266
    Authors: Kristijan Novoselić

    ...

    framework-arduinointel
    **********************

    Adafruit NeoPixel
    =================
    Arduino library for controlling single-wire-based LED pixels and strip.

    Version: 1.0.3
    Homepage: https://github.com/adafruit/Adafruit_NeoPixel
    Keywords: display
    Compatible frameworks: arduino
    Compatible platforms: *
    Authors: Adafruit

    CurieBLE
    ========
    Library to manage the Bluetooth Low Energy module with Curie Core boards.

    Version: 1.0
    Keywords: communication
    Compatible frameworks: arduino
    Compatible platforms: intel_arc32
    Authors: Emutex

    CurieEEPROM
    ===========
    Enables reading and writing to OTP flash area of Curie

    Version: 1.0
    Homepage: http://www.arduino.cc/en/Reference/EEPROM
    Keywords: data, storage
    Compatible frameworks: arduino
    Compatible platforms: intel_arc32
    Authors: Intel

    ...

    framework-arduinomicrochippic32
    *******************************

    Firmata
    =======
    Enables the communication with computer apps using a standard serial protocol. For all Arduino boards.

    Version: 2.4.4
    Homepage: https://github.com/firmata/arduino
    Keywords: device, control
    Compatible frameworks: arduino
    Compatible platforms: *
    Authors: Firmata Developers

    framework-arduinoteensy
    ***********************

    Adafruit CC3000 Library
    =======================
    Library code for Adafruit's CC3000 WiFi breakouts.

    Version: 1.0.1
    Homepage: https://github.com/adafruit/Adafruit_CC3000_Library
    Keywords: communication
    Compatible frameworks: arduino
    Compatible platforms: *
    Authors: Adafruit

    ...

    framework-energiamsp430
    ***********************

    AIR430BoostEuropeETSI
    =====================
    Library for the CC110L Sub-1GHz radio BoosterPack for use in Europe

    Version: 1.0.0
    Homepage: http://energia.nu/reference/libraries/
    Keywords: communication
    Compatible frameworks: arduino
    Compatible platforms:
    Authors: Energia

    ...

    framework-energiativa
    *********************

    aJson
    =====
    An Arduino library to enable JSON processing with Arduino

    Keywords: json, rest, http, web
    Compatible frameworks: arduino
    Compatible platforms: atmelavr
