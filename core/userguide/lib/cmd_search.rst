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

.. _cmd_lib_search:

pio lib search
=====================

.. contents::

Usage
-----

.. code-block:: bash

    pio lib search [OPTIONS] [QUERY]

Description
-----------

Search for library in `PlatformIO Library Registry <https://platformio.org/lib>`_
by :ref:`library_json` fields in the boolean mode.

The boolean search capability supports the following operators:

.. list-table::
    :header-rows:  1

    * - Operator
      - Description
    * - ``+``
      - A leading or trailing plus sign indicates that this word must be present
        in library fields (see above) that is returned.
    * - ``-``
      - A leading or trailing minus sign indicates that this word must not be
        present in any of the libraries that are returned.
    * - ``(no operator)``
      - By default (when neither ``+`` nor ``-`` is specified), the
        word is optional, but the libraries that contain it are rated higher.
    * - ``> <``
      - These two operators are used to change a word's contribution to the
        relevance value that is assigned to a library. The ``>`` operator
        increases the contribution and the ``<`` operator decreases it.
    * - ``( )``
      - Parentheses group words into subexpressions. Parenthesized groups can
        be nested.
    * - ``~``
      - A leading tilde acts as a negation operator, causing the word's
        contribution to the library's relevance to be negative. This is useful for
        marking "noise" words. A library containing such a word is rated lower than
        others, but is not excluded altogether, as it would be with the ``-`` operator.
    * - ``*``
      - The asterisk serves as the truncation (or wildcard) operator. Unlike the
        other operators, it is appended to the word to be affected. Words match if
        they begin with the word preceding the ``*`` operator.
    * - ``"``
      - A phrase that is enclosed within double quote (``"``) characters matches
        only libraries that contain the phrase literally, as it was typed.

For more detail information please go to
`MySQL Boolean Full-Text Searches <http://dev.mysql.com/doc/refman/5.6/en/fulltext-boolean.html>`_.

Options
-------

.. program:: pio lib search

.. option::
    --id

Filter libraries by registry ID

.. option::
    -n, --name

Filter libraries by specified name (strict search)

.. option::
    -a, --author

Filter libraries by specified author

.. option::
    -k, --keyword

Filter libraries by specified keyword

.. option::
    -f, --framework

Filter libraries by specified framework

.. option::
    -p, --platform

Filter libraries by specified keyword

.. option::
    -i, --header

Filter libraries by header file (include)

For example, ``pio lib search --header "OneWire.h"``

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`_ format

.. option::
   --page

Manually paginate through search results. This option is useful in pair with
``--json-output``.

Examples
--------

1. List all libraries

.. code::

    > pio lib search

    Found N libraries:

    ArduinoJson
    ===========
    #ID: 64
    An elegant and efficient JSON library for embedded systems

    Keywords: web, json, http, rest
    Compatible frameworks: Arduino
    Compatible platforms: Atmel AVR, Atmel SAM, Espressif 8266, Intel ARC32, Microchip PIC32, Nordic nRF51, Teensy, TI MSP430
    Authors: Benoit Blanchon

    DHT sensor library
    ==================
    #ID: 19
    Arduino library for DHT11, DHT22, etc Temp & Humidity Sensors

    Keywords: unified, dht, sensor, temperature, humidity
    Compatible frameworks: Arduino
    Compatible platforms: Atmel AVR
    Authors: Adafruit Industries

    PubSubClient
    ============
    #ID: 89
    A client library for MQTT messaging. MQTT is a lightweight messaging protocol ideal for small devices. This library allows you to send and receive MQTT messages. It supports the latest MQTT 3.1.1 protocol and can be configured to use the older MQTT 3.1...

    Keywords: ethernet, mqtt, iot, m2m
    Compatible frameworks: Arduino
    Compatible platforms: Atmel AVR, Atmel SAM, Espressif 8266, Intel ARC32, Microchip PIC32, Nordic nRF51, Teensy, TI MSP430
    Authors: Nick O'Leary

    ...

    ESPAsyncWebServer
    =================
    #ID: 306
    Asynchronous HTTP and WebSocket Server Library for ESP8266 and ESP32

    Keywords: async, websocket, http, webserver
    Compatible frameworks: Arduino
    Compatible platforms: Espressif 8266
    Authors: Hristo Gochkov

    Show next libraries? [y/N]:
    ...

2. Search for `1-Wire libraries <https://platformio.org/lib/search?query=%25221-wire%2522>`_

.. code::

    > pio lib search "1-wire"

    Found N libraries:

    DS1820
    ======
    #ID: 196
    Dallas / Maxim DS1820 1-Wire library. For communication with multiple DS1820 on a single 1-Wire bus. Also supports DS18S20 and DS18B20.

    Keywords: ds18s20, 1-wire, ds1820, ds18b20
    Compatible frameworks: mbed
    Compatible platforms: Freescale Kinetis, Nordic nRF51, NXP LPC, ST STM32, Teensy
    Authors: Michael Hagberg

    OneWire
    =======
    #ID: 1
    Control 1-Wire protocol (DS18S20, DS18B20, DS2408 and etc)

    Keywords: onewire, temperature, bus, 1-wire, ibutton, sensor
    Compatible frameworks: Arduino
    Compatible platforms:
    Authors: Paul Stoffregen, Jim Studt, Tom Pollard, Derek Yerger, Josh Larios, Robin James, Glenn Trewitt, Jason Dangel, Guillermo Lovato, Ken Butcher, Mark Tillotson, Bertrik Sikken, Scott Roberts

    Show next libraries? [y/N]:
    ...

3. Search for `Arduino-based "I2C" libraries <https://platformio.org/lib/search?query=framework%253Aarduino%2520i2c>`_

.. code::

    > pio lib search "i2c" --framework="arduino"

    Found N libraries:

    I2Cdevlib-AK8975
    ================
    #ID: 10
    AK8975 is 3-axis electronic compass IC with high sensitive Hall sensor technology

    Keywords: i2c, i2cdevlib, sensor, compass
    Compatible frameworks: Arduino
    Compatible platforms: Atmel AVR
    Authors: Jeff Rowberg

    I2Cdevlib-Core
    ==============
    #ID: 11
    The I2C Device Library (I2Cdevlib) is a collection of uniform and well-documented classes to provide simple and intuitive interfaces to I2C devices.

    Keywords: i2cdevlib, i2c
    Compatible frameworks: Arduino
    Compatible platforms: Atmel AVR
    Authors: Jeff Rowberg

    Adafruit 9DOF Library
    =====================
    #ID: 14
    Unified sensor driver for the Adafruit 9DOF Breakout (L3GD20 / LSM303)

    Keywords: magnetometer, unified, accelerometer, spi, compass, i2c, sensor, gyroscope
    Compatible frameworks: Arduino
    Compatible platforms: Atmel AVR
    Authors: Adafruit Industries

    Show next libraries? [y/N]:
    ...

4. Search for `libraries by "web" and "http" keywords <https://platformio.org/lib/search?query=keyword%253A%2522web%2522%2520keyword%253A%2522http%2522>`_.

.. code::

    > pio lib search --keyword="web" --keyword="http"

    Found N libraries:

    ArduinoJson
    ===========
    #ID: 64
    An elegant and efficient JSON library for embedded systems

    Keywords: web, json, http, rest
    Compatible frameworks: Arduino
    Compatible platforms: Atmel AVR, Atmel SAM, Espressif 8266, Intel ARC32, Microchip PIC32, Nordic nRF51, Teensy, TI MSP430
    Authors: Benoit Blanchon

    ESPAsyncWebServer
    =================
    #ID: 306
    Asynchronous HTTP and WebSocket Server Library for ESP8266 and ESP32

    Keywords: async, websocket, http, webserver
    Compatible frameworks: Arduino
    Compatible platforms: Espressif 8266
    Authors: Hristo Gochkov

    ESP8266wifi
    ===========
    #ID: 1101
    ESP8266 Arduino library with built in reconnect functionality

    Keywords: web, http, wifi, server, client, wi-fi
    Compatible frameworks: Arduino
    Compatible platforms: Atmel AVR
    Authors: Jonas Ekstrand

    Blynk
    =====
    #ID: 415
    Build a smartphone app for your project in minutes. Blynk allows creating IoT solutions easily. It supports  WiFi, BLE, Bluetooth, Ethernet, GSM, USB, Serial. Works with many boards like ESP8266, ESP32, Arduino UNO, Nano, Due, Mega, Zero, MKR100, Yun,...

    Keywords: control, gprs, protocol, communication, app, bluetooth, serial, cloud, web, usb, m2m, ble, 3g, smartphone, http, iot, device, sensors, data, esp8266, mobile, wifi, ethernet, gsm
    Compatible frameworks: Arduino, Energia, WiringPi
    Compatible platforms: Atmel AVR, Atmel SAM, Espressif 8266, Intel ARC32, Linux ARM, Microchip PIC32, Nordic nRF51, Teensy, TI MSP430, TI Tiva
    Authors: Volodymyr Shymanskyy

    Show next libraries? [y/N]:
    ...

5. Search for `libraries by "Adafruit Industries" author <https://platformio.org/lib/search?query=author%253A%2522Adafruit%20Industries%2522>`_

.. code::

    > pio lib search --author="Adafruit Industries"

    Found N libraries:

    DHT sensor library
    ==================
    #ID: 19
    Arduino library for DHT11, DHT22, etc Temp & Humidity Sensors

    Keywords: unified, dht, sensor, temperature, humidity
    Compatible frameworks: Arduino
    Compatible platforms: Atmel AVR
    Authors: Adafruit Industries

    Adafruit DHT Unified
    ====================
    #ID: 18
    Unified sensor library for DHT (DHT11, DHT22 and etc) temperature and humidity sensors

    Keywords: unified, dht, sensor, temperature, humidity
    Compatible frameworks: Arduino
    Compatible platforms: Atmel AVR
    Authors: Adafruit Industries

    Show next libraries? [y/N]:
    ...

6. Search for `libraries which are compatible with Dallas temperature sensors <https://platformio.org/lib/search?query=DS*>`_
   like DS18B20, DS18S20 and etc.

.. code::

    > pio lib search "DS*"

    Found N libraries:

    DS1820
    ======
    #ID: 196
    Dallas / Maxim DS1820 1-Wire library. For communication with multiple DS1820 on a single 1-Wire bus. Also supports DS18S20 and DS18B20.

    Keywords: ds18s20, 1-wire, ds1820, ds18b20
    Compatible frameworks: mbed
    Compatible platforms: Freescale Kinetis, Nordic nRF51, NXP LPC, ST STM32, Teensy
    Authors: Michael Hagberg

    I2Cdevlib-DS1307
    ================
    #ID: 99
    The DS1307 serial real-time clock (RTC) is a low-power, full binary-coded decimal (BCD) clock/calendar plus 56 bytes of NV SRAM

    Keywords: i2cdevlib, clock, i2c, rtc, time
    Compatible frameworks: Arduino
    Compatible platforms: Atmel AVR
    Authors: Jeff Rowberg

    Show next libraries? [y/N]:
    ...

7. Search for `Energia-based *nRF24* or *HttpClient* libraries <https://platformio.org/lib/search?query=framework%253Aenergia%2520%252B(nRF24%2520HttpClient)>`_.
   The search query that is described below can be interpreted like
   ``energia nRF24 OR energia HttpClient``

.. code::

    > pio lib search "+(nRF24 HttpClient)" --framework="arduino"

    Found N libraries:

    RadioHead
    =========
    #ID: 124
    The RadioHead Packet Radio library which provides a complete object-oriented library for sending and receiving packetized messages via RF22/24/26/27/69, Si4460/4461/4463/4464, nRF24/nRF905, SX1276/77/78, RFM95/96/97/98 and etc.

    Keywords: rf, radio, wireless
    Compatible frameworks: Arduino, Energia
    Compatible platforms: Atmel AVR, Atmel SAM, Espressif 32, Espressif 8266, Infineon XMC, Intel ARC32, Kendryte K210, Microchip PIC32, Nordic nRF51, Nordic nRF52, ST STM32, ST STM8, Teensy, TI MSP430, TI Tiva
    Authors: Mike McCauley

    ArduinoHttpClient
    =================
    #ID: 798
    [EXPERIMENTAL] Easily interact with web servers from Arduino, using HTTP and WebSocket's.

    Keywords: communication
    Compatible frameworks: Arduino
    Compatible platforms: Atmel AVR, Atmel SAM, Espressif 32, Espressif 8266, Intel ARC32, Microchip PIC32, Nordic nRF51, Nordic nRF52, ST STM32, ST STM8, Teensy, TI MSP430
    Authors: Arduino

    HttpClient
    ==========
    #ID: 66
    Library to easily make HTTP GET, POST and PUT requests to a web server.

    Keywords: communication
    Compatible frameworks: Arduino
    Compatible platforms: Atmel AVR, Atmel SAM, Espressif 32, Espressif 8266, Intel ARC32, Microchip PIC32, Nordic nRF51, Nordic nRF52, ST STM32, Teensy, TI MSP430
    Authors: Adrian McEwen

    Show next libraries? [y/N]:
    ...


8. Search for the `all sensor libraries excluding temperature <https://platformio.org/lib/search?query=sensor%2520-temperature>`_.

.. code::

    > pio lib search "sensor -temperature"

    Found N libraries:

    SparkFun VL6180 Sensor
    ======================
    #ID: 407
    The VL6180 combines an IR emitter, a range sensor, and an ambient light sensor together for you to easily use and communicate with via an I2C interface.

    Keywords: sensors
    Compatible frameworks: Arduino
    Compatible platforms: Atmel AVR, Atmel SAM, Espressif 8266, Intel ARC32, Microchip PIC32, Nordic nRF51, Teensy, TI MSP430
    Authors: Casey Kuhns@SparkFun, SparkFun Electronics

    I2Cdevlib-AK8975
    ================
    #ID: 10
    AK8975 is 3-axis electronic compass IC with high sensitive Hall sensor technology

    Keywords: i2c, i2cdevlib, sensor, compass
    Compatible frameworks: Arduino
    Compatible platforms: Atmel AVR
    Authors: Jeff Rowberg

    Adafruit 9DOF Library
    =====================
    #ID: 14
    Unified sensor driver for the Adafruit 9DOF Breakout (L3GD20 / LSM303)

    Keywords: magnetometer, unified, accelerometer, spi, compass, i2c, sensor, gyroscope
    Compatible frameworks: Arduino
    Compatible platforms: Atmel AVR
    Authors: Adafruit Industries

    Show next libraries? [y/N]:
    ...
