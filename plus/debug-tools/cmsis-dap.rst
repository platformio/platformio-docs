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

.. _debugging_tool_cmsis-dap:

CMSIS-DAP
=========

:Configuration:
  :ref:`projectconf_debug_tool` = ``cmsis-dap``

.. image:: ../../_static/debug_probes/cmsis-dap.png
  :target: https://developer.mbed.org/handbook/CMSIS-DAP?utm_source=platformio&utm_medium=docs

CMSIS-DAP is generally implemented as an on-board interface chip, providing
direct USB connection from a development board to a debugger running on a host
computer on one side, and over JTAG (Joint Test Action Group) or SWD
(Serial Wire Debug) to the target device to access the Coresight DAP on the other.
`Vendor information... <https://developer.mbed.org/handbook/CMSIS-DAP?utm_source=platformio&utm_medium=docs>`__

Drivers
-------

:Windows:
  Please install `Windows serial driver <https://os.mbed.com/docs/latest/tutorials/windows-serial-driver.html>`_ and check "USB Driver Installation" guide
  for your board.

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
* :ref:`platform_maxim32`
* :ref:`platform_nordicnrf51`
* :ref:`platform_nordicnrf52`
* :ref:`platform_nxplpc`
* :ref:`platform_ststm32`
* :ref:`platform_wiznet7500`

.. end_compatible_platforms