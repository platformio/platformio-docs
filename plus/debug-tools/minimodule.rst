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

.. _debugging_tool_minimodule:

Mini-Module FT2232H
===================

.. image:: ../../_static/debug_probes/minimodule.jpg
  :target: http://www.ftdichip.com/Products/Modules/DevelopmentModules.htm?utm_source=platformio&utm_medium=docs#FT2232H_Mini

The FT2232H Mini Module is a USB to dual channel serial/MPSSE/FIFO interface
converter module based on the FT2232H USB Hi-Speed IC. The FT2232H handles all
the USB signalling and protocol handling. The module provides access to device
I/O interfaces via 2 double row 0.1" pitch male connectors.  The module is
ideal for development purposes to quickly prove functionality of adding USB
to a target design.
`Vendor information... <http://www.ftdichip.com/Products/Modules/DevelopmentModules.htm?utm_source=platformio&utm_medium=docs#FT2232H_Mini>`__

.. contents:: Contents
    :local:
    :depth: 1

Configuration
-------------

You can configure debugging tool using :ref:`projectconf_debug_tool` option in
:ref:`projectconf`:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    debug_tool = minimodule

If you would like to use this tool for firmware uploading, please change
upload protocol:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    debug_tool = minimodule
    upload_protocol = minimodule

More options:

* :ref:`projectconf_section_env_debug`
* :ref:`projectconf_section_env_upload`

Drivers
-------

:Windows:
  See https://community.platformio.org/t/esp32-pio-unified-debugger/4541/20

:Mac:
  macOS contains default FTDIUSBSerialDriver driver which conflicts with
  debug tools which are based on this chip. FTDI Chip company recommends
  removing this default driver from a system. Everything should work after system rebooting. See detailed instruction in official application note
  (Page 16, Section 4: Uninstalling FTDI Drivers on OS X)
  `AN134: FTDI Drivers Installation guide for MAC OS X <http://www.ftdichip.com/Support/Documents/AppNotes/AN_134_FTDI_Drivers_Installation_Guide_for_MAC_OSX.pdf>`__

:Linux:
  Please install "udev" rules :ref:`faq_udev_rules`. If you already installed
  them before, please check that your rules are up-to-date or repeat steps.

Wiring Connections
------------------

.. list-table::
  :header-rows:  1

  * - FT2232H Mini-Module Pin
    - Board JTAG Pin
  * - AD0 [CN2-7]
    - TCK
  * - AD1 [CN2-10]
    - TDI
  * - AD2 [CN2-9]
    - TDO
  * - AD3 [CN2-12]
    - TMS
  * - AC2 [CN2-20]
    - RST
  * - GND [CN2-2]
    - GND

You will also need to connect Vbus [CN3-1] to Vcc [CN3-3] of FT2232H Mini-Module
to power the FTDI chip. See `FT2232H Mini-Module Datasheet <http://www.ftdichip.com/Support/Documents/DataSheets/Modules/DS_FT2232H_Mini_Module.pdf>`_

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
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_espidf`
      - Espressif IoT Development Framework. Official development framework for ESP32.

    * - :ref:`framework_simba`
      - Simba is an RTOS and build framework. It aims to make embedded programming easy and portable.

Boards
------

.. note::
    For more detailed ``board`` information please scroll tables below by horizontal.


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
    * - ``alksesp32``
      - `ALKS ESP32 <https://github.com/RoboticsBrno/ArduinoLearningKitStarter.git?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp-wrover-kit``
      - `Espressif ESP-WROVER-KIT <https://espressif.com/en/products/hardware/esp-wrover-kit/overview?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_ftdi` (default, on-board), :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32-evb``
      - `OLIMEX ESP32-EVB <https://www.olimex.com/Products/IoT/ESP32-EVB/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32-gateway``
      - `OLIMEX ESP32-GATEWAY <https://www.olimex.com/Products/IoT/ESP32-GATEWAY/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32dev``
      - `Espressif ESP32 Dev Module <https://en.wikipedia.org/wiki/ESP32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32doit-devkit-v1``
      - `DOIT ESP32 DEVKIT V1 <http://www.doit.am/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32thing``
      - `SparkFun ESP32 Thing <https://www.sparkfun.com/products/13907?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``esp32vn-iot-uno``
      - `ESP32vn IoT Uno <https://esp32.vn/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``espectro32``
      - `ESPectro32 <https://shop.makestro.com/product/espectro32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``espino32``
      - `ESPino32 <http://thaieasyelec.com/products/development-boards/espino-wifi-development-board-detail.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``featheresp32``
      - `Adafruit ESP32 Feather <https://www.adafruit.com/product/3405?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``firebeetle32``
      - `FireBeetle-ESP32 <https://dfrobotblog.wordpress.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``hornbill32dev``
      - `Hornbill ESP32 Dev <https://hackaday.io/project/18997-hornbill?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``hornbill32minima``
      - `Hornbill ESP32 Minima <https://hackaday.io/project/18997-hornbill?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin32``
      - `WEMOS LOLIN32 <https://wiki.wemos.cc/products:lolin32:lolin32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin_d32``
      - `WEMOS LOLIN D32 <https://wiki.wemos.cc/products:d32:d32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``lolin_d32_pro``
      - `WEMOS LOLIN D32 PRO <https://wiki.wemos.cc/products:d32:d32_pro?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``mhetesp32devkit``
      - `MH ET LIVE ESP32DevKIT <http://forum.mhetlive.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``mhetesp32minikit``
      - `MH ET LIVE ESP32MiniKit <http://forum.mhetlive.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``node32s``
      - `Node32s <http://www.ayarafun.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``nodemcu-32s``
      - `NodeMCU-32S <http://www.nodemcu.com/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``pocket_32``
      - `Dongsen Tech Pocket 32 <http://dong-sen.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``ttgo-lora32-v1``
      - `TTGO LoRa32-OLED V1 <https://www.google.com.ua/search?q=TTGO+LoRa32-OLED+V1&utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``wemosbat``
      - `WeMos WiFi & Bluetooth Battery <https://www.wemos.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``xinabox_cw02``
      - `XinaBox CW02 <https://xinabox.cc/products/cw02?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
