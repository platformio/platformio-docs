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

The MSP debug stack (MSPDS) for all MSP430™ microcontrollers (MCUs) and
SimpleLink™ MSP432™ devices consists of a static library on the host system
side as well as an embedded firmware that runs on debug tools including the
MSP-FET, MSP-FET430UIF or on-board eZ debuggers. It is the bridging element
between all PC software and all MSP430 and SimpleLink MSP432 microcontroller
derivatives and handles tasks such as code download, stepping through code or
break points.
`Vendor information... <http://www.ti.com/tool/mspds?utm_source=platformio&utm_medium=docs>`__

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
    debug_tool = mspdebug

If you would like to use this tool for firmware uploading, please change
upload protocol:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    debug_tool = mspdebug
    upload_protocol = mspdebug

More options:

* :ref:`projectconf_section_env_debug`
* :ref:`projectconf_section_env_upload`

Drivers
-------

:Windows:
  Please "USB Driver Installation" guide for your board.

:Mac:
  Not required.

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

    * - :ref:`platform_timsp430`
      - MSP430 microcontrollers (MCUs) from Texas Instruments (TI) are 16-bit, RISC-based, mixed-signal processors designed for ultra-low power. These MCUs offer the lowest power consumption and the perfect mix of integrated peripherals for thousands of applications.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_energia`
      - Energia Wiring-based framework enables pretty much anyone to start easily creating microcontroller-based projects and applications. Its easy-to-use libraries and functions provide developers of all experience levels to start blinking LEDs, buzzing buzzers and sensing sensors more quickly than ever before.

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
    * - ``lpmsp430f5529``
      - `TI LaunchPad MSP-EXP430F5529LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430f5529lp.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`debugging_tool_mspdebug` (on-board)
      - MSP430F5529
      - 16MHz
      - 128KB
      - 8KB
    * - ``lpmsp430fr4133``
      - `TI LaunchPad MSP-EXP430FR4133LP <http://www.ti.com/tool/msp-exp430fr4133?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`debugging_tool_mspdebug` (on-board)
      - MSP430FR4133
      - 8MHz
      - 15KB
      - 2KB
    * - ``lpmsp430fr5739``
      - `TI FraunchPad MSP-EXP430FR5739LP <http://www.ti.com/tool/msp-exp430fr5739?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`debugging_tool_mspdebug` (on-board)
      - MSP430FR5739
      - 16MHz
      - 16KB
      - 512B
    * - ``lpmsp430fr5969``
      - `TI LaunchPad MSP-EXP430FR5969LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430fr5969.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`debugging_tool_mspdebug` (on-board)
      - MSP430FR5969
      - 8MHz
      - 64KB
      - 2KB
    * - ``lpmsp430fr6989``
      - `TI LaunchPad MSP-EXP430FR6989LP <http://www.ti.com/tool/msp-exp430fr6989?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`debugging_tool_mspdebug` (on-board)
      - MSP430FR6989
      - 8MHz
      - 127KB
      - 2KB
    * - ``lpmsp430g2553``
      - `TI LaunchPad MSP-EXP430G2553LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430g2.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - :ref:`debugging_tool_mspdebug` (on-board)
      - MSP430G2553
      - 16MHz
      - 16KB
      - 512B
