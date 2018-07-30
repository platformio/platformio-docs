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

.. _framework_espidf:

ESP-IDF
=======
:ref:`projectconf_env_framework` = ``espidf``

Espressif IoT Development Framework. Official development framework for ESP32.

For more detailed information please visit `vendor site <https://github.com/espressif/esp-idf?utm_source=platformio&utm_medium=docs>`_.


.. contents:: Contents
    :local:
    :depth: 1

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. contents::
    :local:


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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp-wrover-kit``
      - `Espressif ESP-WROVER-KIT <https://espressif.com/en/products/hardware/esp-wrover-kit/overview?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_ft2232h` (default, on-board), :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp32-evb``
      - `OLIMEX ESP32-EVB <https://www.olimex.com/Products/IoT/ESP32-EVB/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32-gateway``
      - `OLIMEX ESP32-GATEWAY <https://www.olimex.com/Products/IoT/ESP32-GATEWAY/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32dev``
      - `Espressif ESP32 Dev Module <https://en.wikipedia.org/wiki/ESP32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32doit-devkit-v1``
      - `DOIT ESP32 DEVKIT V1 <http://www.doit.am/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32thing``
      - `SparkFun ESP32 Thing <https://www.sparkfun.com/products/13907?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32vn-iot-uno``
      - `ESP32vn IoT Uno <https://esp32.vn/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``espectro32``
      - `ESPectro32 <https://shop.makestro.com/product/espectro32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``espino32``
      - `ESPino32 <http://thaieasyelec.com/products/development-boards/espino-wifi-development-board-detail.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``featheresp32``
      - `Adafruit ESP32 Feather <https://www.adafruit.com/product/3405?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``firebeetle32``
      - `FireBeetle-ESP32 <https://dfrobotblog.wordpress.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``hornbill32dev``
      - `Hornbill ESP32 Dev <https://hackaday.io/project/18997-hornbill?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``hornbill32minima``
      - `Hornbill ESP32 Minima <https://hackaday.io/project/18997-hornbill?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin32``
      - `WEMOS LOLIN32 <https://wiki.wemos.cc/products:lolin32:lolin32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin_d32``
      - `WEMOS LOLIN D32 <https://wiki.wemos.cc/products:d32:d32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin_d32_pro``
      - `WEMOS LOLIN D32 PRO <https://wiki.wemos.cc/products:d32:d32_pro?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``mhetesp32devkit``
      - `MH ET LIVE ESP32DevKIT <http://forum.mhetlive.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``mhetesp32minikit``
      - `MH ET LIVE ESP32MiniKit <http://forum.mhetlive.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``node32s``
      - `Node32s <http://www.ayarafun.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``nodemcu-32s``
      - `NodeMCU-32S <http://www.nodemcu.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``pocket_32``
      - `Dongsen Tech Pocket 32 <http://dong-sen.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``ttgo-lora32-v1``
      - `TTGO LoRa32-OLED V1 <https://www.google.com.ua/search?q=TTGO+LoRa32-OLED+V1&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``wemosbat``
      - `WeMos WiFi & Bluetooth Battery <https://www.wemos.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``xinabox_cw02``
      - `XinaBox CW02 <https://xinabox.cc/products/cw02?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB


Examples
--------

* `ESP-IDF for Espressif 32 <https://github.com/platformio/platform-espressif32/tree/master/examples?utm_source=platformio&utm_medium=docs>`_

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_espressif32`
      - Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by horizontal.

Adafruit
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``featheresp32``
      - `Adafruit ESP32 Feather <https://www.adafruit.com/product/3405?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``node32s``
      - `Node32s <http://www.ayarafun.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``espea32``
      - `April Brother ESPea32 <https://blog.aprbrother.com/product/espea?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``firebeetle32``
      - `FireBeetle-ESP32 <https://dfrobotblog.wordpress.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp32doit-devkit-v1``
      - `DOIT ESP32 DEVKIT V1 <http://www.doit.am/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``pocket_32``
      - `Dongsen Tech Pocket 32 <http://dong-sen.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``espectro32``
      - `ESPectro32 <https://shop.makestro.com/product/espectro32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp32vn-iot-uno``
      - `ESP32vn IoT Uno <https://esp32.vn/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp320``
      - `Electronic SweetPeas ESP320 <http://www.sweetpeas.se/controller-modules/10-esp210.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp-wrover-kit``
      - `Espressif ESP-WROVER-KIT <https://espressif.com/en/products/hardware/esp-wrover-kit/overview?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32dev``
      - `Espressif ESP32 Dev Module <https://en.wikipedia.org/wiki/ESP32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``pico32``
      - `ESP32 Pico Kit <http://esp-idf.readthedocs.io/en/latest/get-started/get-started-pico-kit.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``odroid_esp32``
      - `ODROID-GO <https://www.hardkernel.com/main/products/prdt_info.php?g_code=G152875062626&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``heltec_wifi_kit_32``
      - `Heltec WIFI Kit 32 <http://www.heltec.cn?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``heltec_wifi_lora_32``
      - `Heltec WIFI LoRa 32 <http://www.heltec.cn?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``hornbill32dev``
      - `Hornbill ESP32 Dev <https://hackaday.io/project/18997-hornbill?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``hornbill32minima``
      - `Hornbill ESP32 Minima <https://hackaday.io/project/18997-hornbill?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``intorobot``
      - `IntoRobot Fig <http://docs.intorobot.com/zh/hardware/fig/hardware/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``m5stack-core-esp32``
      - `M5Stack Core ESP32 <http://www.m5stack.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``m5stack-fire``
      - `M5Stack FIRE <http://www.m5stack.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``mhetesp32devkit``
      - `MH ET LIVE ESP32DevKIT <http://forum.mhetlive.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``mhetesp32minikit``
      - `MH ET LIVE ESP32MiniKit <http://forum.mhetlive.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``nano32``
      - `MakerAsia Nano32 <http://iot-bits.com/nano32-esp32-development-board?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``microduino-core-esp32``
      - `Microduino Core ESP32 <https://microduinoinc.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``nodemcu-32s``
      - `NodeMCU-32S <http://www.nodemcu.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``quantum``
      - `Noduino Quantum <http://wiki.jackslab.org/Noduino?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp32-evb``
      - `OLIMEX ESP32-EVB <https://www.olimex.com/Products/IoT/ESP32-EVB/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32-gateway``
      - `OLIMEX ESP32-GATEWAY <https://www.olimex.com/Products/IoT/ESP32-GATEWAY/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``onehorse32dev``
      - `Onehorse ESP32 Dev Module <https://www.tindie.com/products/onehorse/esp32-development-board/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``esp32thing``
      - `SparkFun ESP32 Thing <https://www.sparkfun.com/products/13907?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``ttgo-lora32-v1``
      - `TTGO LoRa32-OLED V1 <https://www.google.com.ua/search?q=TTGO+LoRa32-OLED+V1&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``espino32``
      - `ESPino32 <http://thaieasyelec.com/products/development-boards/espino-wifi-development-board-detail.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lolin32``
      - `WEMOS LOLIN32 <https://wiki.wemos.cc/products:lolin32:lolin32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin_d32``
      - `WEMOS LOLIN D32 <https://wiki.wemos.cc/products:d32:d32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin_d32_pro``
      - `WEMOS LOLIN D32 PRO <https://wiki.wemos.cc/products:d32:d32_pro?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`Yes <piodebug>`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``wemosbat``
      - `WeMos WiFi & Bluetooth Battery <https://www.wemos.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``widora-air``
      - `Widora AIR <http://widora.io?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``xinabox_cw02``
      - `XinaBox CW02 <https://xinabox.cc/products/cw02?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``nina_w10``
      - `u-blox NINA-W10 series <https://www.u-blox.com/en/product/nina-w10-series?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - No
      - ESP32
      - 240MHz
      - 2MB
      - 320KB
