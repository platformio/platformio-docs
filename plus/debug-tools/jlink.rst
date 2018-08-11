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

.. _debugging_tool_jlink:

J-LINK
======

:Configuration:
  :ref:`projectconf_debug_tool` = ``jlink``

.. image:: ../../_static/debug_probes/jlink.png
  :target: https://www.segger.com/jlink-debug-probes.html?utm_source=platformio&utm_medium=docs

SEGGER J-Links are the most widely used line of debug probes available today.
They've proven their value for more than 10 years with over 400,000 units sold,
including OEM versions and on-board solutions. This popularity stems from the
unparalleled performance, extensive feature set, large number of supported
CPUs, and compatibility with all popular development environments.
`Vendor information... <https://www.segger.com/jlink-debug-probes.html?utm_source=platformio&utm_medium=docs>`__

* Install `J-Link GDB Server <https://www.segger.com/products/debug-probes/j-link/tools/j-link-gdb-server/about-j-link-gdb-server/?utm_source=platformio&utm_medium=docs>`_
* `J-Link Supported Devices <https://www.segger.com/downloads/supported_devices_jlink.php?utm_source=platformio&utm_medium=docs>`__

Also, see :ref:`debugging_tool_custom` debugging configuration with
J-Link GDB Server.

Drivers
-------

:Windows:
  1. Start debugging session using :ref:`pioide`. PlatformIO will install
     J-Link software dependencies
  2. Navigate to :ref:`projectconf_pio_home_dir`/packages/tool-jlink/USBDriver
  3. Run ``InstDrivers.exe``.

:Mac:
  Not required.

:Linux:
  Please install "udev" rules :ref:`faq_udev_rules`. If you already installed
  them before, please check that your rules are up-to-date or repeat steps.

.. begin_compatible_platforms

Compatible Platforms
--------------------

* :ref:`platform_atmelsam`
* :ref:`platform_freescalekinetis`
* :ref:`platform_infineonxmc`
* :ref:`platform_nordicnrf51`
* :ref:`platform_nordicnrf52`
* :ref:`platform_nxplpc`
* :ref:`platform_siliconlabsefm32`
* :ref:`platform_ststm32`
* :ref:`platform_teensy`
* :ref:`platform_wiznet7500`

.. end_compatible_platforms