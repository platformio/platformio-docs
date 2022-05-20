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

.. _debugging_tool_esp-usb-bridge:

ESP USB Bridge
==============

.. image:: ../../_static/images/debug_probes/esp-usb-bridge.png
   :target: https://github.com/espressif/esp-usb-bridge?utm_source=platformio&utm_medium=docs

The ESP USB Bridge is an ESP-IDF project utilizing an ESP32-S2 (or optionally,
an ESP32-S3) chip to create a bridge between a computer (PC) and a target
microcontroller (MCU). It can serve as a replacement for USB-to-UART chips
(e.g. CP210x).
Official reference can be found `here <https://github.com/espressif/esp-usb-bridge?utm_source=platformio&utm_medium=docs>`__.

.. contents:: Contents
    :local:

Configuration
-------------

You can configure debugging tool using :ref:`projectconf_debug_tool` option in
:ref:`projectconf`:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    debug_tool = esp-usb-bridge

If you would like to use this tool for firmware uploading, please change
upload protocol:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    debug_tool = esp-usb-bridge
    upload_protocol = esp-usb-bridge

More options:

* :ref:`projectconf_section_env_debug`
* :ref:`projectconf_section_env_upload`


Tutorials
---------

* `Use the PlatformIO Debugger on the ESP32 Using an ESP-prog <https://www.hackster.io/brian-lough/use-the-platformio-debugger-on-the-esp32-using-an-esp-prog-f633b6>`_

.. begin_platforms

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_espressif32`
      - Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences

    * - :ref:`framework_espidf`
      - ESP-IDF is the official development framework for the ESP32 and ESP32-S Series SoCs.
