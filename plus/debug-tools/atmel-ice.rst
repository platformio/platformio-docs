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

.. _debugging_tool_atmel-ice:

Atmel-ICE
=========

:Configuration:
  :ref:`projectconf_debug_tool` = ``atmel-ice``

.. image:: ../../_static/debug_probes/atmel-ice.jpg
  :target: https://www.microchip.com/DevelopmentTools/ProductDetails/PartNo/atatmel-ice?PartNO=atatmel-ice&utm_source=platformio&utm_medium=docs

Atmel-ICE is a powerful development tool for debugging and programming ARM®
Cortex®-M based SAM and AVR microcontrollers with on-chip debug capability.
`Vendor information... <https://www.microchip.com/DevelopmentTools/ProductDetails/PartNo/atatmel-ice?PartNO=atatmel-ice&utm_source=platformio&utm_medium=docs>`__

Drivers
-------

:Windows:
  When installing the Atmel-ICE on a computer running Microsoft Windows,
  the USB driver is loaded when the Atmel-ICE is first plugged in.

:Mac:
  Not required.

:Linux:
  Please install "udev" rules :ref:`faq_udev_rules`. If you already installed
  them before, please check that your rules are up-to-date or repeat steps.

.. begin_compatible_platforms

Compatible Platforms
--------------------

* :ref:`platform_atmelsam`

.. end_compatible_platforms
