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

.. _debugging_tool_ti-icdi:

TI-ICDI
=======

:Configuration:
  :ref:`projectconf_debug_tool` = ``ti-icdi``

Tiva™ C Series evaluation and reference design kits provide an integrated
In-Circuit Debug Interface (ICDI) which allows programming and debugging of
the onboard C Series microcontroller.
`Vendor information... <http://www.ti.com/tool/stellaris_icdi_drivers?utm_source=platformio&utm_medium=docs>`__

Drivers
-------

:Windows:
  Please "USB Driver Installation" guide for your board.

:Mac:
  Not required.

:Linux:
  Please install "udev" rules :ref:`faq_udev_rules`. If you already installed
  them before, please check that your rules are up-to-date or repeat steps.

.. begin_compatible_platforms

Compatible Platforms
--------------------

* :ref:`platform_titiva`

.. end_compatible_platforms