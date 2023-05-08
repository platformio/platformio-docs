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

.. |PIOREGISTRY| replace:: `PlatformIO Registry <https://registry.platformio.org>`__

.. _cmd_pkg_search:

pio pkg search
==============

.. contents::

Usage
-----

.. code-block:: bash

    pio pkg search [OPTIONS] [QUERY]

Description
-----------

Search the |PIOREGISTRY| for packages matching the search query.
You can use :ref:`cmd_pkg_search_qualifiers` or perform a full-text search over the following package metadata:

- Name
- Description
- Authors
- Keywords
- README file
- Development platform boards.

Multiple :ref:`cmd_pkg_search_qualifiers` and full-text search words are allowed if split with space.
See also :ref:`cmd_pkg_search_operators` for the advanced search.

Options
-------

.. program:: pio pkg search

.. option::
    -p, --page

Number of items to skip before starting to collect the result set.

.. option::
    -s, --sort

Sort method. Available methods are ``relevance``, ``popularity``, ``trending``, ``added``, and ``updated``.

.. _cmd_pkg_search_qualifiers:

Search Qualifiers
-----------------

You can search for packages on the |PIOREGISTRY| and narrow the results using
these search qualifiers in any combination.

Search by type or tier
~~~~~~~~~~~~~~~~~~~~~~

You can search packages by ``type`` (see :ref:`cmd_pkg_install_types`)
or ``tier`` qualifier.

.. list-table::
    :header-rows:  1
    :widths: 20 80

    * - Qualifier
      - Example
    * - ``type:NAME``
      - `type:library <https://registry.platformio.org/search?q=type%3Alibrary>`_
        matches only library packages
    * - ``tier:NAME``
      - *  `tier:official <https://registry.platformio.org/search?q=tier%3Aofficial>`_
           matches high-quality official packages owned and maintained by `PlatformIO Labs <https://piolabs.com>`__
        *  `tier:verified <https://registry.platformio.org/search?q=tier%3Averified>`_
           matches verified packages owned and maintained by third-party technology partners
        *  `tier:community <https://registry.platformio.org/search?q=tier%3Acommunity>`_
           matches community packages.

Search by metadata
~~~~~~~~~~~~~~~~~~

Search for packages by their metadata.

.. list-table::
    :header-rows:  1
    :widths: 20 80

    * - Qualifier
      - Example
    * - ``name:NAME``
      - `name:"Adafruit BusIO" <https://registry.platformio.org/search?q=name%3A%22Adafruit+BusIO%22>`_
        matches Adafruit BusIO library
    * - ``keyword:NAME``
      - `keyword:json <https://registry.platformio.org/search?q=keyword%3Ajson>`_
        matches packages by "json" keyword
    * - ``category:NAME``
      - `category:"AI & ML" <https://registry.platformio.org/search?q=category%3A%22AI+%26+ML%22>`_
        matches AI and ML compatible packages

Search by ownership or contribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Search for packages owned by the ``owner`` or maintained by the ``author``.

.. list-table::
    :header-rows:  1
    :widths: 20 80

    * - Qualifier
      - Example
    * - ``owner:NAME``
      - `owner:espressif <https://registry.platformio.org/search?q=owner%3Aespressif>`_
        matches packages owned by Espressif Systems
    * - ``author:NAME``
      - `author:"Paul Stoffregen" <https://registry.platformio.org/search?q=author%3A%22Paul+Stoffregen%22>`_
        matches packages with Paul Stoffregen's contribution

Filter by compatibility
~~~~~~~~~~~~~~~~~~~~~~~

You can filter packages by compatibility using ``framework`` or ``platform`` qualifier.

.. list-table::
    :header-rows:  1
    :widths: 20 80

    * - Qualifier
      - Example
    * - ``framework:NAME``
      - `framework:arduino json <https://registry.platformio.org/search?q=framework%3Aarduino+json>`_
        matches JSON related packages compatible with Arduino framework
    * - ``platform:NAME``
      - `platform:espressif32 <https://registry.platformio.org/search?q=platform%3Aespressif32>`_
        matches packages compatible with Espressif32 development platform

Search by library header
~~~~~~~~~~~~~~~~~~~~~~~~

You can search for libraries that contain header file.

.. list-table::
    :header-rows:  1
    :widths: 20 80

    * - Qualifier
      - Example
    * - ``header:FILENAME``
      - `header:"Adafruit_Sensor.h" <https://registry.platformio.org/search?q=header%3A%22Adafruit_Sensor.h%22>`_
        matches packages that contain ``Adafruit_Sensor.h`` header/include file.

Filter by dependencies
~~~~~~~~~~~~~~~~~~~~~~~

You can search for packages that depend on the specified package or for package dependencies.

.. list-table::
    :header-rows:  1
    :widths: 20 80

    * - Qualifier
      - Example
    * - ``dependent:OWNER/NAME``
      - `dependent:"bblanchon/ArduinoJson" <https://registry.platformio.org/search?q=dependent%3A%22bblanchon%2FArduinoJson%22>`_
        matches packages that depend on `ArduinoJson <https://registry.platformio.org/libraries/bblanchon/ArduinoJson>`__ library
    * - ``dependency:OWNER/NAME``
      - `dependency:"painlessmesh/painlessMesh" <https://registry.platformio.org/search?q=dependency%3A%22painlessmesh%2FpainlessMesh%22>`_
        matches `painlessMesh <https://registry.platformio.org/libraries/painlessmesh/painlessMesh>`__ dependencies

.. _cmd_pkg_search_operators:

Search Operators
----------------

|PIOREGISTRY| supports the following operators:

.. list-table::
    :header-rows:  1
    :widths: 10 45 45

    * - Operator
      - Description
      - Example
    * - ``+``
      - A leading or trailing plus sign indicates that this word must be present
        in the search result that is returned.
      - `json +arduino <https://registry.platformio.org/search?q=json+%2Barduino>`__
        matches JSON-related packages that contain the "arduino" word in the package metadata

    * - ``-``
      - A leading or trailing minus sign indicates that this word must not be
        present in the search result that is returned.
      - `json -mbed <https://registry.platformio.org/search?q=json+-mbed>`__
        matches JSON-related packages that do not contain the "mbed" word in the package metadata

    * - ``*``
      - The asterisk serves as the truncation (or wildcard) operator. Unlike the
        other operators, it is appended to the word to be affected. Words match if
        they begin with the word preceding the ``*`` operator.
      - `DHT* <https://registry.platformio.org/search?q=DHT*>`__
        matches packages that contain a word that starts with "DHT"

    * - ``"``
      - A phrase that is enclosed within double quote (``"``) characters matches
        only packages that contain the phrase literally, as it was typed.
      - `"humidity sensor" <https://registry.platformio.org/search?q=%22humidity+sensor%22>`__
        matches packages that contain the "humidity sensor" phrase.

Examples
--------

1. List trending libraries

.. code::

    > pio pkg search "type:library" --sort trending

    Found 12374 packages (page 1 of 1238)

    adafruit/Adafruit Unified Sensor
    Library • 1.1.5 • Published on Mon Mar  7 21:09:03 2022
    Required for all Adafruit Unified Sensor based libraries. A unified sensor abstraction layer used by many Adafruit sensor libraries.

    stm32duino/STM32duino FreeRTOS
    Library • 10.3.1 • Published on Mon Feb 28 15:46:45 2022
    Real Time Operating System implemented for STM32
    ...

2. List trending libraries

.. code::

    > pio pkg search "type:library" --sort trending

    Found 12374 packages (page 1 of 1238)

    adafruit/Adafruit Unified Sensor
    Library • 1.1.5 • Published on Mon Mar  7 21:09:03 2022
    Required for all Adafruit Unified Sensor based libraries. A unified sensor abstraction layer used by many Adafruit sensor libraries.

    stm32duino/STM32duino FreeRTOS
    Library • 10.3.1 • Published on Mon Feb 28 15:46:45 2022
    Real Time Operating System implemented for STM32
    ...

3. Search for packages that match words that start with "DHT"

.. code::

    > pio pkg search "DHT*"

    Found 163 packages (page 1 of 17)

    0nism/ESP32-DHT11
    Library • 1.0.1 • Published on Tue Oct 16 19:30:42 2018
    Full featured driver to use DHT11 sensor on esp32 with esp-idf

    adafruit/Adafruit DHT Unified
    Library • 1.0.0 • Published on Fri May 27 20:45:19 2016
    Unified sensor library version of the DHT humidity ...

    robtillaart/DHT20
    Library • 0.1.0 • Published on Tue Jan 11 20:35:46 2022
    Arduino library for I2C DHT20 temperature and humidity sensor.
    ...

4. Search for packages that support STM32F405RG MCU

.. code::

    > pio pkg search "STM32F405RG"

    Found 4 packages (page 1 of 1)

    aceinna/aceinna_imu
    Official Platform • 1.3.8 • Published on Mon Oct 25 16:39:27 2021
    Open-source, embedded development ...

    twilio/Breakout Arduino Library
    Library • 0.1.0 • Published on Tue Oct 23 16:22:19 2018
    Arduino library for the Twilio ...

    platformio/ststm32
    Platform • 15.2.0 • Published on Fri Jan 28 13:21:03 2022
    The STM32 family of 32-bit Flash MCUs ...

    platformio/framework-arduinoststm32
    Tool • 4.20200.220204 • Published on Mon Feb  7 09:47:31 2022
    Arduino Wiring-based Framework for ST STM32 microcontrollers

5. Search for official development platforms that support STM32F405RG MCU

.. code::

    > pio pkg search "type:platform tier:official STM32F405RG"

    Found 1 packages (page 1 of 1)

    aceinna/aceinna_imu
    Official Platform • 1.3.8 • Published on Mon Oct 25 16:39:27 2021
    Open-source, embedded development platform for Aceinna IMU hardware. Run custom algorithms and navigation code on Aceinna IMU/INS hardware.

See Also
--------

* :ref:`cmd_pkg_show`
* :ref:`cmd_pkg_list`
* :ref:`cmd_pkg_install`
