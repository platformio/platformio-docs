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

.. _platform_espressif32:

Espressif 32
============
:ref:`projectconf_env_platform` = ``espressif32``

Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

For more detailed information please visit `vendor site <https://espressif.com/?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: espressif32_extra.rst

Examples
--------

Examples are listed from `Espressif 32 development platform repository <https://github.com/platformio/platform-espressif32/tree/master/examples?utm_source=platformio&utm_medium=docs>`_:

* `arduino-blink <https://github.com/platformio/platform-espressif32/tree/master/examples/arduino-blink?utm_source=platformio&utm_medium=docs>`_
* `arduino-wifiscan <https://github.com/platformio/platform-espressif32/tree/master/examples/arduino-wifiscan?utm_source=platformio&utm_medium=docs>`_
* `espidf-aws-iot <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-aws-iot?utm_source=platformio&utm_medium=docs>`_
* `espidf-ble-adv <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-ble-adv?utm_source=platformio&utm_medium=docs>`_
* `espidf-coap-server <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-coap-server?utm_source=platformio&utm_medium=docs>`_
* `espidf-exceptions <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-exceptions?utm_source=platformio&utm_medium=docs>`_
* `espidf-hello-world <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-hello-world?utm_source=platformio&utm_medium=docs>`_
* `espidf-http-request <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-http-request?utm_source=platformio&utm_medium=docs>`_
* `espidf-peripherals-uart <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-peripherals-uart?utm_source=platformio&utm_medium=docs>`_
* `espidf-storage-sdcard <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-storage-sdcard?utm_source=platformio&utm_medium=docs>`_
* `pumbaa-blink <https://github.com/platformio/platform-espressif32/tree/master/examples/pumbaa-blink?utm_source=platformio&utm_medium=docs>`_
* `simba-blink <https://github.com/platformio/platform-espressif32/tree/master/examples/simba-blink?utm_source=platformio&utm_medium=docs>`_

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. contents::
    :local:

.. include:: espressif32_debug.rst

Debug Tools
~~~~~~~~~~~

Supported debugging tools are listed in "Debug" column. For more detailed
information, please scroll table by horizontal.
You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` options.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further instructions.


On-Board Debug Tools
^^^^^^^^^^^^^^^^^^^^

Boards listed below have on-board debug tool and **ARE READY** for debugging!
You do not need to use/buy external debug tool.


.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp-wrover-kit``
      - `Espressif ESP-WROVER-KIT <https://espressif.com/en/products/hardware/esp-wrover-kit/overview?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_ftdi` (default, on-board), :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB


External Debug Tools
^^^^^^^^^^^^^^^^^^^^

Boards listed below are compatible with :ref:`piodebug` but **DEPEND ON**
external debug tool. See "Debug" column for compatible debug tools.


.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``alksesp32``
      - `ALKS ESP32 <https://github.com/RoboticsBrno/ArduinoLearningKitStarter.git?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32-evb``
      - `OLIMEX ESP32-EVB <https://www.olimex.com/Products/IoT/ESP32-EVB/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32-gateway``
      - `OLIMEX ESP32-GATEWAY <https://www.olimex.com/Products/IoT/ESP32-GATEWAY/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32dev``
      - `Espressif ESP32 Dev Module <https://en.wikipedia.org/wiki/ESP32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32doit-devkit-v1``
      - `DOIT ESP32 DEVKIT V1 <http://www.doit.am/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32thing``
      - `SparkFun ESP32 Thing <https://www.sparkfun.com/products/13907?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32vn-iot-uno``
      - `ESP32vn IoT Uno <https://esp32.vn/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``espectro32``
      - `ESPectro32 <https://shop.makestro.com/product/espectro32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``espino32``
      - `ESPino32 <http://thaieasyelec.com/products/development-boards/espino-wifi-development-board-detail.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``featheresp32``
      - `Adafruit ESP32 Feather <https://www.adafruit.com/product/3405?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``firebeetle32``
      - `FireBeetle-ESP32 <https://dfrobotblog.wordpress.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``hornbill32dev``
      - `Hornbill ESP32 Dev <https://hackaday.io/project/18997-hornbill?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``hornbill32minima``
      - `Hornbill ESP32 Minima <https://hackaday.io/project/18997-hornbill?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin32``
      - `WEMOS LOLIN32 <https://wiki.wemos.cc/products:lolin32:lolin32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin_d32``
      - `WEMOS LOLIN D32 <https://wiki.wemos.cc/products:d32:d32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin_d32_pro``
      - `WEMOS LOLIN D32 PRO <https://wiki.wemos.cc/products:d32:d32_pro?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``mhetesp32devkit``
      - `MH ET LIVE ESP32DevKIT <http://forum.mhetlive.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``mhetesp32minikit``
      - `MH ET LIVE ESP32MiniKit <http://forum.mhetlive.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``node32s``
      - `Node32s <http://www.ayarafun.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``nodemcu-32s``
      - `NodeMCU-32S <http://www.nodemcu.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``pocket_32``
      - `Dongsen Tech Pocket 32 <http://dong-sen.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``ttgo-lora32-v1``
      - `TTGO LoRa32-OLED V1 <https://www.google.com.ua/search?q=TTGO+LoRa32-OLED+V1&utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``wemosbat``
      - `WeMos WiFi & Bluetooth Battery <https://www.wemos.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``xinabox_cw02``
      - `XinaBox CW02 <https://xinabox.cc/products/cw02?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-espressif32/releases>`__
of Espressif 32 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = espressif32
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = espressif32@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-espressif32.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinoespressif32 <https://github.com/espressif/arduino-esp32?utm_source=platformio&utm_medium=docs>`__
      - Arduino Wiring-based Framework (ESP32 Core)

    * - `framework-espidf <https://github.com/espressif/esp-idf?utm_source=platformio&utm_medium=docs>`__
      - Espressif IoT Development Framework

    * - `framework-pumbaa <https://github.com/eerimoq/pumbaa?utm_source=platformio&utm_medium=docs>`__
      - Pumbaa Framework

    * - `framework-simba <https://github.com/eerimoq/simba?utm_source=platformio&utm_medium=docs>`__
      - Simba Framework

    * - `tool-espotapy <https://github.com/esp8266/Arduino/blob/master/tools/espota.py?utm_source=platformio&utm_medium=docs>`__
      - ESP8266 OTA utility

    * - `tool-esptoolpy <https://github.com/espressif/esptool?utm_source=platformio&utm_medium=docs>`__
      - ESP8266 and ESP32 serial bootloader utility

    * - `tool-mkspiffs <https://github.com/igrr/mkspiffs?utm_source=platformio&utm_medium=docs>`__
      - Tool to build and unpack SPIFFS images

    * - `tool-openocd-esp32 <https://github.com/espressif/openocd-esp32?utm_source=platformio&utm_medium=docs>`__
      - OpenOCD for Espressif 32

    * - `toolchain-xtensa32 <https://github.com/espressif/esp-idf?utm_source=platformio&utm_medium=docs>`__
      - xtensa32-gcc

.. warning::
    **Linux Users**:

        * Install "udev" rules :ref:`faq_udev_rules`
        * Raspberry Pi users, please read this article
          `Enable serial port on Raspberry Pi <https://hallard.me/enable-serial-port-on-raspberry-pi/>`__.


    **Windows Users:**

        Please check that you have a correctly installed USB driver from board
        manufacturer


Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_espidf`
      - Espressif IoT Development Framework. Official development framework for ESP32.

    * - :ref:`framework_pumbaa`
      - Pumbaa is Python on top of Simba. The implementation is a port of MicroPython, designed for embedded devices with limited amount of RAM and code memory.

    * - :ref:`framework_simba`
      - Simba is an RTOS and build framework. It aims to make embedded programming easy and portable.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

Adafruit
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``featheresp32``
      - `Adafruit ESP32 Feather <https://www.adafruit.com/product/3405?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Aiyarafun
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``node32s``
      - `Node32s <http://www.ayarafun.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

April Brother
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``espea32``
      - `April Brother ESPea32 <https://blog.aprbrother.com/product/espea?utm_source=platformio&utm_medium=docs>`_
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

DFRobot
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``firebeetle32``
      - `FireBeetle-ESP32 <https://dfrobotblog.wordpress.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

DOIT
~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp32doit-devkit-v1``
      - `DOIT ESP32 DEVKIT V1 <http://www.doit.am/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Dongsen Technology
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``pocket_32``
      - `Dongsen Tech Pocket 32 <http://dong-sen.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

DycodeX
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``espectro32``
      - `ESPectro32 <https://shop.makestro.com/product/espectro32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

ESP32vn
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp32vn-iot-uno``
      - `ESP32vn IoT Uno <https://esp32.vn/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Electronic SweetPeas
~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp320``
      - `Electronic SweetPeas ESP320 <http://www.sweetpeas.se/controller-modules/10-esp210.html?utm_source=platformio&utm_medium=docs>`_
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Espressif
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp-wrover-kit``
      - `Espressif ESP-WROVER-KIT <https://espressif.com/en/products/hardware/esp-wrover-kit/overview?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32dev``
      - `Espressif ESP32 Dev Module <https://en.wikipedia.org/wiki/ESP32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``pico32``
      - `ESP32 Pico Kit <http://esp-idf.readthedocs.io/en/latest/get-started/get-started-pico-kit.html?utm_source=platformio&utm_medium=docs>`_
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Hardkernel
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``odroid_esp32``
      - `ODROID-GO <https://www.hardkernel.com/main/products/prdt_info.php?g_code=G152875062626&utm_source=platformio&utm_medium=docs>`_
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

Heltec Automation
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``heltec_wifi_kit_32``
      - `Heltec WIFI Kit 32 <http://www.heltec.cn?utm_source=platformio&utm_medium=docs>`_
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``heltec_wifi_lora_32``
      - `Heltec WIFI LoRa 32 <http://www.heltec.cn?utm_source=platformio&utm_medium=docs>`_
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Hornbill
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``hornbill32dev``
      - `Hornbill ESP32 Dev <https://hackaday.io/project/18997-hornbill?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``hornbill32minima``
      - `Hornbill ESP32 Minima <https://hackaday.io/project/18997-hornbill?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

IntoRobot
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``intorobot``
      - `IntoRobot Fig <http://docs.intorobot.com/zh/hardware/fig/hardware/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

M5Stack
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``m5stack-core-esp32``
      - `M5Stack Core ESP32 <http://www.m5stack.com?utm_source=platformio&utm_medium=docs>`_
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``m5stack-fire``
      - `M5Stack FIRE <http://www.m5stack.com?utm_source=platformio&utm_medium=docs>`_
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

MH-ET Live
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``mhetesp32devkit``
      - `MH ET LIVE ESP32DevKIT <http://forum.mhetlive.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``mhetesp32minikit``
      - `MH ET LIVE ESP32MiniKit <http://forum.mhetlive.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

MakerAsia
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``nano32``
      - `MakerAsia Nano32 <http://iot-bits.com/nano32-esp32-development-board?utm_source=platformio&utm_medium=docs>`_
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Microduino
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``microduino-core-esp32``
      - `Microduino Core ESP32 <https://microduinoinc.com?utm_source=platformio&utm_medium=docs>`_
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

NodeMCU
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``nodemcu-32s``
      - `NodeMCU-32S <http://www.nodemcu.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Noduino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``quantum``
      - `Noduino Quantum <http://wiki.jackslab.org/Noduino?utm_source=platformio&utm_medium=docs>`_
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

OLIMEX
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp32-evb``
      - `OLIMEX ESP32-EVB <https://www.olimex.com/Products/IoT/ESP32-EVB/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32-gateway``
      - `OLIMEX ESP32-GATEWAY <https://www.olimex.com/Products/IoT/ESP32-GATEWAY/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Onehorse
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``onehorse32dev``
      - `Onehorse ESP32 Dev Module <https://www.tindie.com/products/onehorse/esp32-development-board/?utm_source=platformio&utm_medium=docs>`_
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

RoboticsBrno
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``alksesp32``
      - `ALKS ESP32 <https://github.com/RoboticsBrno/ArduinoLearningKitStarter.git?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

SparkFun Electronics
~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp32thing``
      - `SparkFun ESP32 Thing <https://www.sparkfun.com/products/13907?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

TTGO
~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``ttgo-lora32-v1``
      - `TTGO LoRa32-OLED V1 <https://www.google.com.ua/search?q=TTGO+LoRa32-OLED+V1&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

ThaiEasyElec
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``espino32``
      - `ESPino32 <http://thaieasyelec.com/products/development-boards/espino-wifi-development-board-detail.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

WEMOS
~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lolin32``
      - `WEMOS LOLIN32 <https://wiki.wemos.cc/products:lolin32:lolin32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin_d32``
      - `WEMOS LOLIN D32 <https://wiki.wemos.cc/products:d32:d32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin_d32_pro``
      - `WEMOS LOLIN D32 PRO <https://wiki.wemos.cc/products:d32:d32_pro?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``wemosbat``
      - `WeMos WiFi & Bluetooth Battery <https://www.wemos.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Widora
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``widora-air``
      - `Widora AIR <http://widora.io?utm_source=platformio&utm_medium=docs>`_
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

XinaBox
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``xinabox_cw02``
      - `XinaBox CW02 <https://xinabox.cc/products/cw02?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

u-blox
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``nina_w10``
      - `u-blox NINA-W10 series <https://www.u-blox.com/en/product/nina-w10-series?utm_source=platformio&utm_medium=docs>`_
      - No
      - ESP32
      - 240MHz
      - 2MB
      - 320KB
