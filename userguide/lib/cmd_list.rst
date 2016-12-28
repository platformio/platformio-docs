..  Copyright 2014-present PlatformIO <contact@platformio.org>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _cmd_lib_list:

platformio lib list
===================

.. contents::

Usage
-----

.. code-block:: bash

    platformio lib [STORAGE_OPTIONS] list [OPTIONS]
    pio lib [STORAGE_OPTIONS] list [OPTIONS]

    # list project dependent libraries
    # (run it from a project root where is located "platformio.ini")
    platformio lib list [OPTIONS]

    # list libraries from global storage
    platformio lib --global list [OPTIONS]
    platformio lib -g list [OPTIONS]

    # list libraries from custom storage
    platformio lib --storage-dir /path/to/dir list [OPTIONS]
    platformio lib -d /path/to/dir list [OPTIONS]

Description
-----------

List installed libraries

Storage Options
---------------

See base options for :ref:`cmd_lib`.

Options
~~~~~~~

.. program:: platformio lib list

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`_ format

Examples
--------

.. code::

    > platformio lib -g list

    Library Storage: /storage/dir/...
    Adafruit Unified Sensor
    =======================
    #ID: 31
    Required for all Adafruit Unified Sensor based libraries.

    Keywords: sensors
    Compatible frameworks: arduino
    Compatible platforms: atmelavr, atmelsam, espressif8266, intel_arc32, microchippic32, nordicnrf51, teensy, timsp430
    Authors: Adafruit

    ArduinoJson
    ===========
    #ID: 64
    An elegant and efficient JSON library for embedded systems

    Keywords: web, json, http, rest
    Compatible frameworks: arduino
    Compatible platforms: atmelavr, atmelsam, espressif8266, intel_arc32, microchippic32, nordicnrf51, teensy, timsp430
    Authors: Benoit Blanchon

    Bounce2
    =======
    #ID: 1106
    Debouncing library for Arduino or Wiring

    Keywords: input, signal, ouput, bounce
    Compatible frameworks: arduino
    Compatible platforms: atmelavr, atmelsam, espressif8266, intel_arc32, microchippic32, nordicnrf51, teensy, timsp430
    Authors: Thomas O Fredericks

    DCF77
    =====
    #ID: 169
    Read and decode the atomic time broadcasted by the DCF77 radiostation.

    Keywords: dcf77, time
    Compatible frameworks: arduino
    Compatible platforms:
    Authors: Thijs Elenbaas

    DHT sensor library
    ==================
    #ID: 19
    Arduino library for DHT11, DHT22, etc Temp & Humidity Sensors

    Keywords: unified, dht, sensor, temperature, humidity
    Compatible frameworks: arduino
    Compatible platforms: atmelavr
    Authors: Adafruit Industries

    Homie
    =====
    #ID: 555
    ESP8266 framework for Homie, a lightweight MQTT convention for the IoT

    Keywords: home, mqtt, iot, esp8266, automation
    Compatible frameworks: arduino
    Compatible platforms: espressif8266
    Authors: Marvin Roger

    LiquidCrystal
    =============
    #ID: 136
    LiquidCrystal Library is faster and extensable, compatible with the original LiquidCrystal library

    Keywords: lcd, hd44780
    Compatible frameworks: arduino
    Compatible platforms: atmelavr
    Authors: F Malpartida

    MFRC522
    =======
    #ID: 63
    Read a card using a MFRC522 reader on your SPI interface

    Keywords: spi, rfid
    Compatible frameworks: arduino
    Compatible platforms: atmelavr, ststm32, teensy, espressif8266
    Authors: Miki Balboa

    OneWire
    =======
    #ID: 1
    Control 1-Wire protocol (DS18S20, DS18B20, DS2408 and etc)

    Homepage: https://www.pjrc.com/teensy/td_libs_OneWire.html
    Keywords: onewire, temperature, bus, 1-wire, ibutton, sensor
    Compatible frameworks: arduino
    Compatible platforms:
    Authors: Paul Stoffregen, Jim Studt, Tom Pollard, Derek Yerger, Josh Larios, Robin James, Glenn Trewitt, Jason Dangel, Guillermo Lovato, Ken Butcher, Mark Tillotson, Bertrik Sikken, Scott Roberts

    PID
    ===
    #ID: 2
    A PID controller seeks to keep some input variable close to a desired setpoint by adjusting an output. The way in which it does this can be 'tuned' by adjusting three parameters (P,I,D).

    Homepage: http://playground.arduino.cc/Code/PIDLibrary
    Keywords: controller, pid, signal
    Compatible frameworks: arduino
    Compatible platforms: atmelavr
    Authors: Brett Beauregard

    PubSubClient
    ============
    #ID: 89
    A client library for MQTT messaging. MQTT is a lightweight messaging protocol ideal for small devices. This library allows you to send and receive MQTT messages. It supports the latest MQTT 3.1.1 protocol and can be configured to use the older MQTT 3.1 if needed. It supports all Arduino Ethernet Client compatible hardware, including the Intel Galileo/Edison, ESP8266 and TI CC3000.

    Homepage: http://pubsubclient.knolleary.net
    Keywords: ethernet, mqtt, iot, m2m
    Compatible frameworks: arduino
    Compatible platforms: atmelavr, atmelsam, espressif8266, intel_arc32, microchippic32, nordicnrf51, teensy, timsp430
    Authors: Nick O'Leary

    SPI4Teensy3
    ===========
    #ID: 417
    Faster SPI library optimized for the Teensy 3.0

    Keywords: spi
    Compatible frameworks: arduino
    Compatible platforms: teensy
    Authors: Andrew Kroll

    TextLCD
    =======
    hg+https://developer.mbed.org/users/simon/code/TextLCD/


    Time
    ====
    #ID: 44
    Time keeping library

    Homepage: http://playground.arduino.cc/Code/Time
    Keywords: week, rtc, hour, year, month, second, time, date, day, minute
    Compatible frameworks: arduino
    Compatible platforms:
    Authors: Michael Margolis, Paul Stoffregen

    Timezone
    ========
    #ID: 76
    Arduino library to facilitate time zone conversions and automatic daylight saving (summer) time adjustments

    Keywords: zone, time
    Compatible frameworks: arduino
    Compatible platforms: atmelavr
    Authors: Jack Christensen

    USB-Host-Shield-20
    ==================
    #ID: 59
    Revision 2.0 of MAX3421E-based USB Host Shield Library

    License: GPL-2.0
    Keywords: usb, spp, mass storage, pl2303, acm, ftdi, xbox, host, hid, wii, buzz, ps3, bluetooth, adk, ps4
    Compatible frameworks: spl, arduino
    Compatible platforms: atmelavr, atmelsam, teensy, nordicnrf51, ststm32
    Authors: Oleg Mazurov, Alexei Glushchenko, Kristian Lauszus, Andrew Kroll
