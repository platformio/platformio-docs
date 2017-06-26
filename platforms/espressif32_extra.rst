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


Over-the-Air (OTA) update
-------------------------

There are 2 options:

* Directly specify :option:`platformio run --upload-port` in command line

.. code-block:: bash

    platformio run --target upload --upload-port IP_ADDRESS_HERE or mDNS_NAME.local

* Specify ``upload_port`` option in :ref:`projectconf`

.. code-block:: ini

   [env:myenv]
   upload_port = IP_ADDRESS_HERE or mDNS_NAME.local

For example,

* ``platformio run -t upload --upload-port 192.168.0.255``
* ``platformio run -t upload --upload-port myesp8266.local``

Authentication and upload options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can pass additional options/flags to OTA uploader using
``upload_flags`` option in :ref:`projectconf`

.. code-block:: ini

    [env:myenv]
    upload_flags = --port=8266

Available flags

* ``--port=ESP_PORT`` ESP8266 OTA Port. Default 8266
* ``--auth=AUTH`` Set authentication password
* ``--spiffs`` Use this option to transmit a SPIFFS image and do not flash
  the module

For the full list with available options please run

.. code-block:: bash

    ~/.platformio/packages/tool-espotapy/espota.py -h

    Usage: espota.py [options]

    Transmit image over the air to the esp8266 module with OTA support.

    Options:
      -h, --help            show this help message and exit

      Destination:
        -i ESP_IP, --ip=ESP_IP
                            ESP8266 IP Address.
        -p ESP_PORT, --port=ESP_PORT
                            ESP8266 ota Port. Default 8266

      Authentication:
        -a AUTH, --auth=AUTH
                            Set authentication password.

      Image:
        -f FILE, --file=FILE
                            Image file.
        -s, --spiffs        Use this option to transmit a SPIFFS image and do not
                            flash the module.

      Output:
        -d, --debug         Show debug output. And override loglevel with debug.
        -r, --progress      Show progress output. Does not work for ArduinoIDE

Using Arduino Framework with Staging version
--------------------------------------------

PlatformIO will install the latest Arduino Core for ESP32 from
https://github.com/espressif/arduino-esp32. The `Git <https://git-scm.com>`_
should be installed in a system. To update Arduino Core to the latest revision,
please use :ref:`cmd_platform_update` command.

1. 	Install Espressif 32 (Stage) development platform

    .. code::

        platformio platform install https://github.com/platformio/platform-espressif32.git#feature/stage

2.  Set :ref:`projectconf_env_platform` to ``espressif32_stage`` in
    :ref:`projectconf`. For example,

    .. code-block:: ini

        [env:esp32dev]
        platform = espressif32_stage
        board = esp32dev
        framework = arduino

3.  Try to build project
4.  If you see build errors, then try to build this project using the same
    ``stage`` with Arduino IDE
5.  If it works with Arduino IDE but doesn't work with PlatformIO, then please
    `file new issue <https://github.com/platformio/platform-espressif32/issuess>`_
    with attached information:

    - test project/files
    - detailed log of build process from Arduino IDE (please copy it from
      console to http://pastebin.com)
    - detailed log of build process from PlatformIO Build System (
      please copy it from console to http://pastebin.com)

Examples
--------

All project examples are located in PlatformIO repository
`Examples for Espressif 32 platform <https://github.com/platformio/platformio-examples/tree/develop/espressif>`_.

* `Arduino Blink <https://github.com/platformio/platformio-examples/tree/develop/espressif/esp32-arduino-blink>`_
* `Arduino WiFiScan <https://github.com/platformio/platformio-examples/tree/develop/espressif/esp32-arduino-wifiscan>`_
* `ESP-IDF Hello World <https://github.com/platformio/platformio-examples/tree/develop/espressif/esp32-espidf-hello-world>`_
* `ESP-IDF HTTP Request <https://github.com/platformio/platformio-examples/tree/develop/espressif/esp32-espidf-http-request>`_
