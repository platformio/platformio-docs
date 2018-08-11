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

.. _debugging_tool_mspdebug:

MSP Debug
=========

:Configuration:
  :ref:`projectconf_debug_tool` = ``mspdebug``

The MSP debug stack (MSPDS) for all MSP430™ microcontrollers (MCUs) and
SimpleLink™ MSP432™ devices consists of a static library on the host system
side as well as an embedded firmware that runs on debug tools including the
MSP-FET, MSP-FET430UIF or on-board eZ debuggers. It is the bridging element
between all PC software and all MSP430 and SimpleLink MSP432 microcontroller
derivatives and handles tasks such as code download, stepping through code or
break points.
`Vendor information... <http://www.ti.com/tool/mspds?utm_source=platformio&utm_medium=docs>`__

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

* :ref:`platform_timsp430`

.. end_compatible_platforms