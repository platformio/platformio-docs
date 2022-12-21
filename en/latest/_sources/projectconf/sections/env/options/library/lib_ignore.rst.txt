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

.. _projectconf_lib_ignore:

``lib_ignore``
--------------

.. seealso::
    Please make sure to read :ref:`ldf` guide first.

Type: ``String`` | Multiple: ``Yes``

Specify libraries which should be ignored by Library Dependency Finder.

The correct value for this option is a library name (not folder name).
You will see these names in "Library Dependency Graph" when building a project
between ``<`` and ``>`` symbols.

**Example:**

``Build output``

.. code::

    ...
    Library Dependency Finder -> https://bit.ly/configure-pio-ldf
    LDF MODES: FINDER(chain+) COMPATIBILITY(soft)
    Collected 54 compatible libraries
    Scanning dependencies...
    Dependency Graph
    |-- <Hash> v1.0
    |-- <AsyncMqttClient> v0.8.2
    |   |-- <ESPAsyncTCP> v1.1.3
    |-- <ESP8266WiFi> v1.0
    |-- <ESP Async WebServer> v1.1.1
    |   |-- <ESPAsyncTCP> v1.1.3
    |   |-- <ESP8266WiFi> v1.0
    |   |-- <Hash> v1.0
    |   |-- <ArduinoJson> v5.13.1
    |-- <ArduinoJson> v5.13.1
    |-- <DNSServer> v1.1.0
    |   |-- <ESP8266WiFi> v1.0
    |-- <Ticker> v1.0
    ....

``platformio.ini``

.. code-block:: ini

    [env:myenv]
    ; Single line
    lib_ignore = AsyncMqttClient, DNSServer

    ; Multi-line
    lib_ignore =
      AsyncMqttClient
      ESP Async WebServer