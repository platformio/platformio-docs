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

:Configuration:
  :ref:`projectconf_debug_tool` = ``minimodule``

.. image:: ../../_static/debug_probes/minimodule.jpg
  :target: http://www.ftdichip.com/Products/Modules/DevelopmentModules.htm?utm_source=platformio&utm_medium=docs#FT2232H_Mini

The FT2232H Mini Module is a USB to dual channel serial/MPSSE/FIFO interface
converter module based on the FT2232H USB Hi-Speed IC. The FT2232H handles all
the USB signalling and protocol handling. The module provides access to device
I/O interfaces via 2 double row 0.1" pitch male connectors.  The module is
ideal for development purposes to quickly prove functionality of adding USB
to a target design.
`Vendor information... <http://www.ftdichip.com/Products/Modules/DevelopmentModules.htm?utm_source=platformio&utm_medium=docs#FT2232H_Mini>`__

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

.. begin_compatible_platforms

Compatible Platforms
--------------------

* :ref:`platform_espressif32`

.. end_compatible_platforms