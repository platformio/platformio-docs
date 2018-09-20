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

.. _debugging_tool_ftdi:

FTDI Chip
=========

:Configuration:
  :ref:`projectconf_debug_tool` = ``ftdi``

.. image:: ../../_static/debug_probes/ftdi.jpg
  :target: http://www.ftdichip.com/USB.html?utm_source=platformio&utm_medium=docs

FTDI Chip develops innovative silicon solutions that enhance interaction with
today’s technology. When a designer needs to add a USB port, rest assured that
FTDI Chip has a full range of USB solutions to get the job done.
`Vendor information...  <http://www.ftdichip.com/USB.html?utm_source=platformio&utm_medium=docs>`__

.. contents:: Contents
    :local:
    :depth: 1

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

.. begin_platforms

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_espressif32`
      - Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

    * - :ref:`platform_riscv`
      - RISC-V is an open, free ISA enabling a new era of processor innovation through open standard collaboration. Born in academia and research, RISC-V ISA delivers a new level of free, extensible software and hardware freedom on architecture, paving the way for the next 50 years of computing design and innovation.

    * - :ref:`platform_riscv_gap`
      - GreenWaves GAP8 IoT application processor enables the cost-effective development, deployment and autonomous operation of intelligent sensing devices that capture, analyze, classify and act on the fusion of rich data sources such as images, sounds or vibrations.

    * - :ref:`platform_samsung_artik`
      - The Samsung ARTIK Smart IoT platform brings hardware modules and cloud services together, with built-in security and an ecosystem of tools and partners to speed up your time-to-market.

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

    * - :ref:`framework_freedom-e-sdk`
      - Open Source Software for Developing on the SiFive Freedom E Platform

    * - :ref:`framework_simba`
      - Simba is an RTOS and build framework. It aims to make embedded programming easy and portable.

    * - :ref:`framework_tizenrt`
      - Tizen RT is a lightweight RTOS-based platform to support low-end IoT devices

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
    * - ``artik_053``
      - `Samsung ARTIK053 <http://www.artik.io?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Samsung ARTIK <platform_samsung_artik>`
      - :ref:`debugging_tool_ftdi` (on-board)
      - S5JT200
      - 320MHz
      - 8MB
      - 1.25MB
    * - ``esp-wrover-kit``
      - `Espressif ESP-WROVER-KIT <https://espressif.com/en/products/hardware/esp-wrover-kit/overview?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_ftdi` (default, on-board), :ref:`debugging_tool_esp-prog`, :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-ocd`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`, :ref:`debugging_tool_olimex-jtag-tiny`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - ``freedom-e300-hifive1``
      - `HiFive1 <https://www.sifive.com/products/hifive1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`RISC-V <platform_riscv>`
      - :ref:`debugging_tool_ftdi` (on-board)
      - FE310
      - 320MHz
      - 16MB
      - 16KB
    * - ``gapuino``
      - `GAPUINO GAP8 development board <https://greenwaves-technologies.com/product/gapduino/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`RISC-V GAP <platform_riscv_gap>`
      - :ref:`debugging_tool_ftdi` (on-board)
      - 
      - 250MHz
      - 64MB
      - 8MB
