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

.. _cmd_lib_stats:

pio lib stats
=============

.. contents::

Usage
-----

.. code-block:: bash

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

* https://platformio.org/lib

Options
-------

.. program:: pio lib show

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`_ format

Examples
--------

.. code::

    RECENTLY UPDATED
    ****************
    Name                     Date                    Url
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    GroveEncoder             12 hours ago            https://platformio.org/lib/show/1382/GroveEncoder
    RF24G                    12 hours ago            https://platformio.org/lib/show/1381/RF24G
    Sim800L Library Revised  12 hours ago            https://platformio.org/lib/show/1380/Sim800L%20Library%20Revised
    ArduinoSTL               12 hours ago            https://platformio.org/lib/show/750/ArduinoSTL
    hd44780                  13 hours ago            https://platformio.org/lib/show/738/hd44780

    RECENTLY ADDED
    **************
    Name                     Date                    Url
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    GroveEncoder             12 hours ago            https://platformio.org/lib/show/1382/GroveEncoder
    RF24G                    12 hours ago            https://platformio.org/lib/show/1381/RF24G
    Sim800L Library Revised  12 hours ago            https://platformio.org/lib/show/1380/Sim800L%20Library%20Revised
    DS3231                   a day ago               https://platformio.org/lib/show/1379/DS3231
    ArduboyPlaytune          4 days ago              https://platformio.org/lib/show/1378/ArduboyPlaytune

    RECENT KEYWORDS
    ***************
    Name                     Url
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    cobs                     https://platformio.org/lib/search?query=keyword%3Acobs
    packet                   https://platformio.org/lib/search?query=keyword%3Apacket
    framing                  https://platformio.org/lib/search?query=keyword%3Aframing
    3g                       https://platformio.org/lib/search?query=keyword%3A3g
    tdd                      https://platformio.org/lib/search?query=keyword%3Atdd

    POPULAR KEYWORDS
    ****************
    Name                     Url
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    display                  https://platformio.org/lib/search?query=keyword%3Adisplay
    lcd                      https://platformio.org/lib/search?query=keyword%3Alcd
    sensors                  https://platformio.org/lib/search?query=keyword%3Asensors
    graphics                 https://platformio.org/lib/search?query=keyword%3Agraphics
    communication            https://platformio.org/lib/search?query=keyword%3Acommunication
    oled                     https://platformio.org/lib/search?query=keyword%3Aoled
    tft                      https://platformio.org/lib/search?query=keyword%3Atft
    control                  https://platformio.org/lib/search?query=keyword%3Acontrol
    device                   https://platformio.org/lib/search?query=keyword%3Adevice
    glcd                     https://platformio.org/lib/search?query=keyword%3Aglcd
    displaycore              https://platformio.org/lib/search?query=keyword%3Adisplaycore
    font                     https://platformio.org/lib/search?query=keyword%3Afont
    other                    https://platformio.org/lib/search?query=keyword%3Aother
    i2c                      https://platformio.org/lib/search?query=keyword%3Ai2c
    input                    https://platformio.org/lib/search?query=keyword%3Ainput
    signal                   https://platformio.org/lib/search?query=keyword%3Asignal
    sensor                   https://platformio.org/lib/search?query=keyword%3Asensor
    output                   https://platformio.org/lib/search?query=keyword%3Aoutput
    spi                      https://platformio.org/lib/search?query=keyword%3Aspi
    data                     https://platformio.org/lib/search?query=keyword%3Adata
    timing                   https://platformio.org/lib/search?query=keyword%3Atiming
    serial                   https://platformio.org/lib/search?query=keyword%3Aserial
    temperature              https://platformio.org/lib/search?query=keyword%3Atemperature
    http                     https://platformio.org/lib/search?query=keyword%3Ahttp
    wifi                     https://platformio.org/lib/search?query=keyword%3Awifi
    rf                       https://platformio.org/lib/search?query=keyword%3Arf
    i2cdevlib                https://platformio.org/lib/search?query=keyword%3Ai2cdevlib
    processing               https://platformio.org/lib/search?query=keyword%3Aprocessing
    storage                  https://platformio.org/lib/search?query=keyword%3Astorage
    radio                    https://platformio.org/lib/search?query=keyword%3Aradio
    web                      https://platformio.org/lib/search?query=keyword%3Aweb
    accelerometer            https://platformio.org/lib/search?query=keyword%3Aaccelerometer
    wireless                 https://platformio.org/lib/search?query=keyword%3Awireless
    protocol                 https://platformio.org/lib/search?query=keyword%3Aprotocol
    server                   https://platformio.org/lib/search?query=keyword%3Aserver
    wi-fi                    https://platformio.org/lib/search?query=keyword%3Awi-fi
    ethernet                 https://platformio.org/lib/search?query=keyword%3Aethernet
    mbed                     https://platformio.org/lib/search?query=keyword%3Ambed
    openag                   https://platformio.org/lib/search?query=keyword%3Aopenag
    led                      https://platformio.org/lib/search?query=keyword%3Aled
    esp8266                  https://platformio.org/lib/search?query=keyword%3Aesp8266
    humidity                 https://platformio.org/lib/search?query=keyword%3Ahumidity
    time                     https://platformio.org/lib/search?query=keyword%3Atime
    iot                      https://platformio.org/lib/search?query=keyword%3Aiot
    json                     https://platformio.org/lib/search?query=keyword%3Ajson
    timer                    https://platformio.org/lib/search?query=keyword%3Atimer
    client                   https://platformio.org/lib/search?query=keyword%3Aclient
    driver                   https://platformio.org/lib/search?query=keyword%3Adriver
    button                   https://platformio.org/lib/search?query=keyword%3Abutton
    mbed-official            https://platformio.org/lib/search?query=keyword%3Ambed-official

    FEATURED: TODAY
    ***************
    Name                     Url
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    PubSubClient             https://platformio.org/lib/show/89/PubSubClient
    Adafruit Unified Sensor  https://platformio.org/lib/show/31/Adafruit%20Unified%20Sensor
    DHT sensor library       https://platformio.org/lib/show/19/DHT%20sensor%20library
    ESPAsyncUDP              https://platformio.org/lib/show/359/ESPAsyncUDP
    NtpClientLib             https://platformio.org/lib/show/727/NtpClientLib
    Embedis                  https://platformio.org/lib/show/408/Embedis
    Blynk                    https://platformio.org/lib/show/415/Blynk
    SimpleTimer              https://platformio.org/lib/show/419/SimpleTimer
    Adafruit DHT Unified     https://platformio.org/lib/show/18/Adafruit%20DHT%20Unified
    RTClib                   https://platformio.org/lib/show/83/RTClib

    FEATURED: WEEK
    **************
    Name                     Url
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    DHT sensor library       https://platformio.org/lib/show/19/DHT%20sensor%20library
    Adafruit Unified Sensor  https://platformio.org/lib/show/31/Adafruit%20Unified%20Sensor
    Blynk                    https://platformio.org/lib/show/415/Blynk
    ESPAsyncWebServer        https://platformio.org/lib/show/306/ESPAsyncWebServer
    Adafruit GFX Library     https://platformio.org/lib/show/13/Adafruit%20GFX%20Library
    I2Cdevlib-Core           https://platformio.org/lib/show/11/I2Cdevlib-Core
    TimeAlarms               https://platformio.org/lib/show/68/TimeAlarms
    PubSubClient             https://platformio.org/lib/show/89/PubSubClient
    Timer                    https://platformio.org/lib/show/75/Timer
    esp8266_mdns             https://platformio.org/lib/show/1091/esp8266_mdns

    FEATURED: MONTH
    ***************
    Name                     Url
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ArduinoJson              https://platformio.org/lib/show/64/ArduinoJson
    DHT sensor library       https://platformio.org/lib/show/19/DHT%20sensor%20library
    Adafruit Unified Sensor  https://platformio.org/lib/show/31/Adafruit%20Unified%20Sensor
    PubSubClient             https://platformio.org/lib/show/89/PubSubClient
    OneWire                  https://platformio.org/lib/show/1/OneWire
    ESPAsyncTCP              https://platformio.org/lib/show/305/ESPAsyncTCP
    Time                     https://platformio.org/lib/show/44/Time
    DallasTemperature        https://platformio.org/lib/show/54/DallasTemperature
    ESPAsyncWebServer        https://platformio.org/lib/show/306/ESPAsyncWebServer
    WifiManager              https://platformio.org/lib/show/567/WifiManager