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

.. _cmd_lib_stats:

platformio lib stats
====================

.. contents::

Usage
-----

.. code-block:: bash

    platformio lib stats
    pio lib stats


Description
-----------

Show PlatformIO Library Registry statistics:

* Recently updated
* Recently added
* Recent keywords
* Popular keywords
* Featured: Today
* Featured: Week
* Featured: Month

This information is the same that is shown on this page:

* http://platformio.org/lib

Examples
--------

.. code::

    RECENTLY UPDATED
    ****************
    Name                     Date                    Url
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    PacketIO                 2016-12-23 17:10:04     http://platformio.org/lib/show/1377/PacketIO
    PJON                     2016-12-23 15:45:21     http://platformio.org/lib/show/245/PJON
    GobbitLineCommand        2016-12-23 10:00:14     http://platformio.org/lib/show/1320/GobbitLineCommand
    TaskScheduler            2016-12-22 23:45:09     http://platformio.org/lib/show/721/TaskScheduler
    Nokia5110                2016-12-22 11:12:35     http://platformio.org/lib/show/1376/Nokia5110

    RECENTLY ADDED
    **************
    Name                     Date                    Url
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    PacketIO                 2016-12-23 17:10:04     http://platformio.org/lib/show/1377/PacketIO
    Nokia5110                2016-12-22 11:12:35     http://platformio.org/lib/show/1376/Nokia5110
    AnalogKeypad by Makuna   2016-12-22 11:12:31     http://platformio.org/lib/show/1375/AnalogKeypad%20by%20Makuna
    unittest-cpp             2016-12-20 22:00:04     http://platformio.org/lib/show/1374/unittest-cpp
    ROKduino                 2016-12-20 11:20:08     http://platformio.org/lib/show/1373/ROKduino

    RECENT KEYWORDS
    ***************
    Name                     Url
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    cobs                     http://platformio.org/lib/search?query=keyword%3Acobs
    packet                   http://platformio.org/lib/search?query=keyword%3Apacket
    framing                  http://platformio.org/lib/search?query=keyword%3Aframing
    3g                       http://platformio.org/lib/search?query=keyword%3A3g
    tdd                      http://platformio.org/lib/search?query=keyword%3Atdd

    POPULAR KEYWORDS
    ****************
    Name                     Url
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    display                  http://platformio.org/lib/search?query=keyword%3Adisplay
    lcd                      http://platformio.org/lib/search?query=keyword%3Alcd
    sensors                  http://platformio.org/lib/search?query=keyword%3Asensors
    graphics                 http://platformio.org/lib/search?query=keyword%3Agraphics
    communication            http://platformio.org/lib/search?query=keyword%3Acommunication
    oled                     http://platformio.org/lib/search?query=keyword%3Aoled
    tft                      http://platformio.org/lib/search?query=keyword%3Atft
    control                  http://platformio.org/lib/search?query=keyword%3Acontrol
    device                   http://platformio.org/lib/search?query=keyword%3Adevice
    glcd                     http://platformio.org/lib/search?query=keyword%3Aglcd
    displaycore              http://platformio.org/lib/search?query=keyword%3Adisplaycore
    font                     http://platformio.org/lib/search?query=keyword%3Afont
    other                    http://platformio.org/lib/search?query=keyword%3Aother
    i2c                      http://platformio.org/lib/search?query=keyword%3Ai2c
    input                    http://platformio.org/lib/search?query=keyword%3Ainput
    signal                   http://platformio.org/lib/search?query=keyword%3Asignal
    sensor                   http://platformio.org/lib/search?query=keyword%3Asensor
    output                   http://platformio.org/lib/search?query=keyword%3Aoutput
    spi                      http://platformio.org/lib/search?query=keyword%3Aspi
    data                     http://platformio.org/lib/search?query=keyword%3Adata
    timing                   http://platformio.org/lib/search?query=keyword%3Atiming
    serial                   http://platformio.org/lib/search?query=keyword%3Aserial
    temperature              http://platformio.org/lib/search?query=keyword%3Atemperature
    http                     http://platformio.org/lib/search?query=keyword%3Ahttp
    wifi                     http://platformio.org/lib/search?query=keyword%3Awifi
    rf                       http://platformio.org/lib/search?query=keyword%3Arf
    i2cdevlib                http://platformio.org/lib/search?query=keyword%3Ai2cdevlib
    processing               http://platformio.org/lib/search?query=keyword%3Aprocessing
    storage                  http://platformio.org/lib/search?query=keyword%3Astorage
    radio                    http://platformio.org/lib/search?query=keyword%3Aradio
    web                      http://platformio.org/lib/search?query=keyword%3Aweb
    accelerometer            http://platformio.org/lib/search?query=keyword%3Aaccelerometer
    wireless                 http://platformio.org/lib/search?query=keyword%3Awireless
    protocol                 http://platformio.org/lib/search?query=keyword%3Aprotocol
    server                   http://platformio.org/lib/search?query=keyword%3Aserver
    wi-fi                    http://platformio.org/lib/search?query=keyword%3Awi-fi
    ethernet                 http://platformio.org/lib/search?query=keyword%3Aethernet
    mbed                     http://platformio.org/lib/search?query=keyword%3Ambed
    openag                   http://platformio.org/lib/search?query=keyword%3Aopenag
    led                      http://platformio.org/lib/search?query=keyword%3Aled
    esp8266                  http://platformio.org/lib/search?query=keyword%3Aesp8266
    humidity                 http://platformio.org/lib/search?query=keyword%3Ahumidity
    time                     http://platformio.org/lib/search?query=keyword%3Atime
    iot                      http://platformio.org/lib/search?query=keyword%3Aiot
    json                     http://platformio.org/lib/search?query=keyword%3Ajson
    timer                    http://platformio.org/lib/search?query=keyword%3Atimer
    client                   http://platformio.org/lib/search?query=keyword%3Aclient
    driver                   http://platformio.org/lib/search?query=keyword%3Adriver
    button                   http://platformio.org/lib/search?query=keyword%3Abutton
    mbed-official            http://platformio.org/lib/search?query=keyword%3Ambed-official

    FEATURED: TODAY
    ***************
    Name                     Url
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    PubSubClient             http://platformio.org/lib/show/89/PubSubClient
    Adafruit Unified Sensor  http://platformio.org/lib/show/31/Adafruit%20Unified%20Sensor
    DHT sensor library       http://platformio.org/lib/show/19/DHT%20sensor%20library
    ESPAsyncUDP              http://platformio.org/lib/show/359/ESPAsyncUDP
    NtpClientLib             http://platformio.org/lib/show/727/NtpClientLib
    Embedis                  http://platformio.org/lib/show/408/Embedis
    Blynk                    http://platformio.org/lib/show/415/Blynk
    SimpleTimer              http://platformio.org/lib/show/419/SimpleTimer
    Adafruit DHT Unified     http://platformio.org/lib/show/18/Adafruit%20DHT%20Unified
    RTClib                   http://platformio.org/lib/show/83/RTClib

    FEATURED: WEEK
    **************
    Name                     Url
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    DHT sensor library       http://platformio.org/lib/show/19/DHT%20sensor%20library
    Adafruit Unified Sensor  http://platformio.org/lib/show/31/Adafruit%20Unified%20Sensor
    Blynk                    http://platformio.org/lib/show/415/Blynk
    ESPAsyncWebServer        http://platformio.org/lib/show/306/ESPAsyncWebServer
    Adafruit GFX Library     http://platformio.org/lib/show/13/Adafruit%20GFX%20Library
    I2Cdevlib-Core           http://platformio.org/lib/show/11/I2Cdevlib-Core
    TimeAlarms               http://platformio.org/lib/show/68/TimeAlarms
    PubSubClient             http://platformio.org/lib/show/89/PubSubClient
    Timer                    http://platformio.org/lib/show/75/Timer
    esp8266_mdns             http://platformio.org/lib/show/1091/esp8266_mdns

    FEATURED: MONTH
    ***************
    Name                     Url
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ArduinoJson              http://platformio.org/lib/show/64/ArduinoJson
    DHT sensor library       http://platformio.org/lib/show/19/DHT%20sensor%20library
    Adafruit Unified Sensor  http://platformio.org/lib/show/31/Adafruit%20Unified%20Sensor
    PubSubClient             http://platformio.org/lib/show/89/PubSubClient
    OneWire                  http://platformio.org/lib/show/1/OneWire
    ESPAsyncTCP              http://platformio.org/lib/show/305/ESPAsyncTCP
    Time                     http://platformio.org/lib/show/44/Time
    DallasTemperature        http://platformio.org/lib/show/54/DallasTemperature
    ESPAsyncWebServer        http://platformio.org/lib/show/306/ESPAsyncWebServer
    WifiManager              http://platformio.org/lib/show/567/WifiManager