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

.. _cmd_lib_list:

pio lib list
============

.. contents::

Usage
-----

.. code-block:: bash

    pio lib [STORAGE_OPTIONS] list [OPTIONS]

    # list project dependent libraries
    # (run it from a project root where is located "platformio.ini")
    pio lib list [OPTIONS]

    # list libraries from global storage
    pio lib --global list [OPTIONS]
    pio lib -g list [OPTIONS]

    # list libraries from custom storage
    pio lib --storage-dir /path/to/dir list [OPTIONS]
    pio lib -d /path/to/dir list [OPTIONS]

Description
-----------

List installed libraries

Storage Options
---------------

See base options for :ref:`cmd_lib`.

Options
-------

.. program:: pio lib list

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`_ format

Examples
--------

.. code::

    > pio lib -g list

    Library Storage: /storage/dir/...

    Adafruit Unified Sensor
    =======================
    #ID: 31
    Required for all Adafruit Unified Sensor based libraries.

    Version: 1.0.2
    Keywords: sensors
    Compatible frameworks: arduino
    Compatible platforms: atmelavr, atmelsam, espressif8266, intel_arc32, microchippic32, nordicnrf51, teensy, timsp430
    Authors: Adafruit

    ArduinoJson
    ===========
    #ID: 64
    An elegant and efficient JSON library for embedded systems

    Version: 5.8.0
    Keywords: web, json, http, rest
    Compatible frameworks: arduino
    Compatible platforms: atmelavr, atmelsam, espressif8266, intel_arc32, microchippic32, nordicnrf51, teensy, timsp430
    Authors: Benoit Blanchon

    ArduinoJson
    ===========
    #ID: 64
    An elegant and efficient JSON library for embedded systems

    Version: 5.6.7
    Keywords: web, json, http, rest
    Compatible frameworks: arduino
    Compatible platforms: atmelavr, atmelsam, espressif8266, intel_arc32, microchippic32, nordicnrf51, teensy, timsp430
    Authors: Benoit Blanchon

    ArduinoJson
    ===========
    #ID: 64
    An elegant and efficient JSON library for embedded systems

    Version: 5.7.2
    Keywords: web, json, http, rest
    Compatible frameworks: arduino
    Compatible platforms: atmelavr, atmelsam, espressif8266, intel_arc32, microchippic32, nordicnrf51, teensy, timsp430
    Authors: Benoit Blanchon

    Blynk
    =====
    #ID: 415
    Build a smartphone app for your project in minutes. Blynk allows creating IoT solutions easily. It supports  WiFi, BLE, Bluetooth, Ethernet, GSM, USB, Serial. Works with many boards like ESP8266, ESP32, Arduino UNO, Nano, Due, Mega, Zero, MKR100, Yun, Raspberry Pi, Particle, Energia, ARM mbed, Intel Edison/Galileo/Joule, BBC micro:bit, DFRobot, RedBearLab, Microduino, LinkIt ONE ...

    Version: 0.4.3
    Homepage: http://blynk.cc
    Keywords: control, gprs, protocol, communication, app, bluetooth, serial, cloud, web, usb, m2m, ble, 3g, smartphone, http, iot, device, sensors, data, esp8266, mobile, wifi, ethernet, gsm
    Compatible frameworks: energia, wiringpi, arduino
    Compatible platforms: atmelavr, atmelsam, espressif8266, intel_arc32, linux_arm, microchippic32, nordicnrf51, teensy, timsp430, titiva
    Authors: Volodymyr Shymanskyy

    Bounce2
    =======
    #ID: 1106
    Debouncing library for Arduino or Wiring

    Version: 2.1
    Keywords: input, signal, output, bounce
    Compatible frameworks: arduino
    Compatible platforms: atmelavr, atmelsam, espressif8266, intel_arc32, microchippic32, nordicnrf51, teensy, timsp430
    Authors: Thomas O Fredericks

    Homie
    =====
    #ID: 555
    ESP8266 framework for Homie, a lightweight MQTT convention for the IoT

    Version: 1.5.0
    Keywords: home, mqtt, iot, esp8266, automation
    Compatible frameworks: arduino
    Compatible platforms: espressif8266
    Authors: Marvin Roger

    JustWifi
    ========
    #ID: 1282
    Wifi Manager for ESP8266 that supports multiple wifi networks and scan for strongest signal

    Version: 1.1.1
    License: GPL-3.0
    Keywords: manager, wifi, scan
    Compatible frameworks: arduino
    Compatible platforms: espressif8266
    Authors: Xose Perez

    LiquidCrystal
    =============
    #ID: 136
    LiquidCrystal Library is faster and extensable, compatible with the original LiquidCrystal library

    Version: 1.3.4
    Keywords: lcd, hd44780
    Compatible frameworks: arduino
    Compatible platforms: atmelavr
    Authors: F Malpartida

    TextLCD
    =======
    hg+https://developer.mbed.org/users/simon/code/TextLCD/

    Version: 308d188a2d3a
    Keywords: uncategorized

    Time
    ====
    #ID: 44
    Time keeping library

    Version: 1.5
    Homepage: http://playground.arduino.cc/Code/Time
    Keywords: week, rtc, hour, year, month, second, time, date, day, minute
    Compatible frameworks: arduino
    Compatible platforms:
    Authors: Michael Margolis, Paul Stoffregen

    Timezone
    ========
    #ID: 76
    Arduino library to facilitate time zone conversions and automatic daylight saving (summer) time adjustments

    Version: 510ae2f6b6
    Keywords: zone, time
    Compatible frameworks: arduino
    Compatible platforms: atmelavr
    Authors: Jack Christensen

    U8g2
    ====
    #ID: 942
    Monochrome LCD, OLED and eInk Library. Display controller: SSD1305, SSD1306, SSD1322, SSD1325, SSD1327, SSD1606, SH1106, T6963, RA8835, LC7981, PCD8544, PCF8812, UC1604, UC1608, UC1610, UC1611, UC1701, ST7565, ST7567, NT7534, ST7920, LD7032, KS0108. Interfaces: I2C, SPI, Parallel.

    Version: 2.11.4
    Homepage: https://github.com/olikraus/u8g2
    Keywords: display
    Compatible frameworks: arduino
    Compatible platforms: atmelavr, atmelsam, espressif8266, intel_arc32, microchippic32, nordicnrf51, teensy, timsp430
    Authors: oliver

    USB-Host-Shield-20
    ==================
    #ID: 59
    Revision 2.0 of MAX3421E-based USB Host Shield Library

    Version: 1.2.1
    License: GPL-2.0
    Keywords: usb, spp, mass storage, pl2303, acm, ftdi, xbox, host, hid, wii, buzz, ps3, bluetooth, adk, ps4
    Compatible frameworks: spl, arduino
    Compatible platforms: atmelavr, atmelsam, teensy, nordicnrf51, ststm32
    Authors: Oleg Mazurov, Alexei Glushchenko, Kristian Lauszus, Andrew Kroll
