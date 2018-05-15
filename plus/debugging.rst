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

.. |PIODebug| replace:: **PIO Unified Debugger**

.. _piodebug:

PIO Unified Debugger
====================

**It Simply Works. Easier than ever before!**

.. versionadded:: 3.4 (`PlatformIO Plus <https://pioplus.com>`__)

.. note::

  `Demo, discussions, request a support for new hardware. <https://community.platformio.org/t/finally-pio-unified-debugger-comes-to-vscode/4091>`_

* "1-click" solution, zero configuration
* Support for 200+ embedded boards (see below)
* Multiple architectures and development platforms
* Windows, MacOS, Linux (+ARMv6-8)
* Built-in into :ref:`ide_atom` and :ref:`ide_vscode`
* Integration with :ref:`ide_eclipse` and :ref:`ide_sublimetext`

You should have :ref:`pioaccount` to work with |PIODebug|.
A registration is **FREE**.


.. hint::
  In our experience, :ref:`ide_vscode` has the best system performance,
  modern interface for |PIODebug|, and users have found it easier to get started.
  Key debugging features of :ref:`ide_vscode`:

  - Conditional Breakpoints
  - Expressions and Watchpoints
  - Generic Registers
  - Peripheral Registers
  - Memory Viewer
  - Disassembly
  - Multi-thread support
  - A hot restart of an active debugging session

.. image:: ../_static/ide/vscode/platformio-ide-vscode.png
  :target: ../ide/vscode.html

.. contents:: Contents
    :local:
    :depth: 1

Tutorials
---------

* :ref:`tutorial_stm32cube_debugging_unit_testing`

Configuration
-------------

.. warning::

  For the JTAG probes implemented as USB devices (actually most of them), you
  need to configure the UDEV subsystem:

  **Linux Users**: Install "udev" rules :ref:`faq_udev_rules`

  **Windows Users**: Please check that you have a correctly installed USB
  driver from board manufacturer

|PIODebug| can be configured from :ref:`projectconf`:

* :ref:`projectconf_debug_tool`
* :ref:`projectconf_debug_init_break`
* :ref:`projectconf_debug_init_cmds`
* :ref:`projectconf_debug_extra_cmds` (conditional project breakpoints, extra
  configuration, etc.)
* :ref:`projectconf_debug_load_cmd`
* :ref:`projectconf_debug_load_mode`
* :ref:`projectconf_debug_server`
* :ref:`projectconf_debug_port`
* :ref:`projectconf_debug_svd_path`

.. _debugging_tools:

Tools
-----

You can switch between debugging tools using :ref:`projectconf_debug_tool`
option.

.. contents::
    :local:

.. _debugging_tool_atmel-ice:

Atmel-ICE
~~~~~~~~~

:ref:`projectconf_debug_tool` = ``atmel-ice``

Atmel-ICE is a powerful development tool for debugging and programming ARM®
Cortex®-M based SAM and AVR microcontrollers with on-chip debug capability.

`More details <https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=atatmel-ice&utm_source=platformio&utm_medium=docs>`__

.. _debugging_tool_blackmagic:

Black Magic Probe
~~~~~~~~~~~~~~~~~

:ref:`projectconf_debug_tool` = ``blackmagic``

The Black Magic Probe is a modern, in-application debugging tool for embedded
microprocessors. It is able to control and examine the state of the target
microprocessor using a JTAG or Serial Wire Debugging (SWD) port and on-chip
debug logic provided by the microprocessor. The probe connects to a host
computer using a standard USB interface.

Also, see :ref:`debugging_tool_custom` debugging configuration with
Black Magic Probe.

`More details <https://github.com/blacksphere/blackmagic/wiki?utm_source=platformio&utm_medium=docs>`__

.. _debugging_tool_cmsis-dap:

CMSIS-DAP
~~~~~~~~~

:ref:`projectconf_debug_tool` = ``cmsis-dap``

CMSIS-DAP is generally implemented as an on-board interface chip, providing
direct USB connection from a development board to a debugger running on a host
computer on one side, and over JTAG (Joint Test Action Group) or SWD
(Serial Wire Debug) to the target device to access the Coresight DAP on the other.

`More details <https://developer.mbed.org/handbook/CMSIS-DAP?utm_source=platformio&utm_medium=docs>`__

.. _debugging_tool_ft2232h:

FTDI FT2232H
~~~~~~~~~~~~

:ref:`projectconf_debug_tool` = ``ft2232h``

The FT2232H is a USB 2.0 Hi-Speed (480Mb/s) to UART/FIFO IC. It has the
capability of being configured in a variety of industry standard serial or
parallel interfaces.

Building on the innovative features of the FT2232, the FT2232H has two
multi-protocol synchronous serial engines (MPSSEs) which allow for
communication using JTAG, I2C and SPI on two channels simultaneously.

`More details <http://www.ftdichip.com/Products/ICs/FT2232H.html?utm_source=platformio&utm_medium=docs>`__

.. _debugging_tool_jlink:

J-LINK
~~~~~~

:ref:`projectconf_debug_tool` = ``jlink``

SEGGER J-Links are the most widely used line of debug probes available today.
They've proven their value for more than 10 years with over 400,000 units sold,
including OEM versions and on-board solutions. This popularity stems from the
unparalleled performance, extensive feature set, large number of supported
CPUs, and compatibility with all popular development environments.

* Install `J-Link GDB Server <https://www.segger.com/products/debug-probes/j-link/tools/j-link-gdb-server/about-j-link-gdb-server/?utm_source=platformio&utm_medium=docs>`_
* `J-Link Supported Devices <https://www.segger.com/downloads/supported_devices_jlink.php?utm_source=platformio&utm_medium=docs>`__

Also, see :ref:`debugging_tool_custom` debugging configuration with
J-Link GDB Server.

`More details <https://www.segger.com/jlink-debug-probes.html?utm_source=platformio&utm_medium=docs>`__

.. _debugging_tool_minimodule:

Mini-Module
~~~~~~~~~~~

The FT2232H Mini Module is a USB to dual channel serial/MPSSE/FIFO interface
converter module based on the FT2232H USB Hi-Speed IC. The FT2232H handles all
the USB signalling and protocol handling. The module provides access to device
I/O interfaces via 2 double row 0.1" pitch male connectors.  The module is
ideal for development purposes to quickly prove functionality of adding USB
to a target design.

`More details <http://www.ftdichip.com/Products/Modules/DevelopmentModules.htm?utm_source=platformio&utm_medium=docs#FT2232H_Mini>`__

.. _debugging_tool_mspdebug:

MSP Debug
~~~~~~~~~

:ref:`projectconf_debug_tool` = ``mspdebug``

The MSP debug stack (MSPDS) for all MSP430™ microcontrollers (MCUs) and
SimpleLink™ MSP432™ devices consists of a static library on the host system
side as well as an embedded firmware that runs on debug tools including the
MSP-FET, MSP-FET430UIF or on-board eZ debuggers. It is the bridging element
between all PC software and all MSP430 and SimpleLink MSP432 microcontroller
derivatives and handles tasks such as code download, stepping through code or
break points

`More details <http://www.ti.com/tool/mspds?utm_source=platformio&utm_medium=docs>`__

.. _debugging_tool_olimex-arm-usb-ocd-h:

Olimex ARM-USB-OCD-H
~~~~~~~~~~~~~~~~~~~~~

:ref:`projectconf_debug_tool` = ``olimex-arm-usb-ocd-h``

High-speed 3-IN-1 fast USB ARM/ESP32 JTAG, USB-to-RS232 virtual port and power
 supply 5VDC device.

`More details <https://www.olimex.com/Products/ARM/JTAG/ARM-USB-OCD-H/?utm_source=platformio&utm_medium=docs>`__

.. _debugging_tool_olimex-arm-usb-tiny-h:

Olimex ARM-USB-TINY-H
~~~~~~~~~~~~~~~~~~~~~

:ref:`projectconf_debug_tool` = ``olimex-arm-usb-tiny-h``

Low-cost and high-speed ARM/ESP32 USB JTAG

`More details <https://www.olimex.com/Products/ARM/JTAG/ARM-USB-TINY-H/?utm_source=platformio&utm_medium=docs>`__

.. _debugging_tool_ti-icdi:

TI-ICDI
~~~~~~~

:ref:`projectconf_debug_tool` = ``ti-icdi``

Tiva™ C Series evaluation and reference design kits provide an integrated
In-Circuit Debug Interface (ICDI) which allows programming and debugging of
the onboard C Series microcontroller

`More details <http://www.ti.com/tool/stellaris_icdi_drivers?utm_source=platformio&utm_medium=docs>`__

.. _debugging_tool_stlink:

ST-LINK
~~~~~~~

:ref:`projectconf_debug_tool` = ``stlink``

The ST-LINK is an in-circuit debugger and programmer for the STM8 and STM32
microcontroller families. The single wire interface module (SWIM) and
JTAG/serial wire debugging (SWD) interfaces are used to communicate with any
STM8 or STM32 microcontroller located on an application board.

`More details <http://www.st.com/en/development-tools/st-link-v2.1.html?utm_source=platformio&utm_medium=docs>`__

.. _debugging_tool_custom:

Custom
~~~~~~

:ref:`projectconf_debug_tool` = ``custom``

Custom debugging configuration:

* :ref:`projectconf_debug_init_break`
* :ref:`projectconf_debug_init_cmds`
* :ref:`projectconf_debug_extra_cmds` (conditional project breakpoints, extra
  configuration, etc.)
* :ref:`projectconf_debug_load_cmd`
* :ref:`projectconf_debug_server`
* :ref:`projectconf_debug_port`


Examples
^^^^^^^^

.. contents::
    :local:

Black Magic Probe
'''''''''''''''''

Black Magic Probe with a custom :ref:`projectconf_debug_port` (list ports
with :ref:`cmd_device_list`)

.. code-block:: ini

  [env:debug]
  platform = ...
  board = ...
  framework = ...
  debug_tool = custom
  ; set here a valid port...
  debug_port = /dev/cu.usbmodem7BB07991
  debug_init_cmds =
    target extended-remote $DEBUG_PORT
    monitor swdp_scan
    attach 1
    set mem inaccessible-by-default off
    $INIT_BREAK
    $LOAD_CMD

J-Link and ST Nucleo
''''''''''''''''''''

Segger J-Link probe and ST Nucleo F446RE board in pair with J-Link GDB Server:

* Install `J-Link GDB Server <https://www.segger.com/products/debug-probes/j-link/tools/j-link-gdb-server/about-j-link-gdb-server/?utm_source=platformio&utm_medium=docs>`_
* `Convert ST-LINK On-Board Into a J-Link <https://www.segger.com/products/debug-probes/j-link/models/other-j-links/st-link-on-board/?utm_source=platformio&utm_medium=docs>`_

.. note::

  You can use configuration below in pair with other boards, not only with ST
  Nucleo F446RE. In this case, please replace ``STM32F446RE`` with
  your own device name in ``debug_server`` option.

  See full list with `J-Link Supported Devices <https://www.segger.com/downloads/supported_devices_jlink.php?utm_source=platformio&utm_medium=docs>`__.


.. code-block:: ini

    [env:debug_jlink]
    platform = ststm32
    framework = mbed
    board = nucleo_f446re
    debug_tool = custom
    debug_server =
      /full/path/to/JLinkGDBServerCL
      -singlerun
      -if
      SWD
      -select
      USB
      -port
      2331
      -device
      STM32F446RE

J-Link as debugger and uploader
'''''''''''''''''''''''''''''''

Segger J-Link probe as debugger and uploader for a custom Teensy-based board.
If you plan to use with other board, please change device ``MK20DX256xxx7``
to a valid identifier. See supported J-Link devices at :ref:`debugging_tool_jlink`.

* Install `J-Link GDB Server <https://www.segger.com/products/debug-probes/j-link/tools/j-link-gdb-server/about-j-link-gdb-server/?utm_source=platformio&utm_medium=docs>`_


.. code-block:: ini

    [env:jlink_debug_and_upload]
    platform = teensy
    framework = arduino
    board = teensy31
    extra_scripts = extra_script.py
    upload_protocol = custom
    debug_tool = custom
    debug_server =
      /full/path/to/JLinkGDBServerCL
      -singlerun
      -if
      SWD
      -select
      USB
      -port
      2331
      -device
      MK20DX256xxx7

**extra_script.py**

Place this file on the same level as :ref:`projectconf`.

.. code-block:: py

    from os import makedirs
    from os.path import isdir, join
    Import('env')


    # Optional block, only for Teensy
    env.AddPostAction(
        "$BUILD_DIR/firmware.hex",
        env.VerboseAction(" ".join([
            "sed", "-i.bak",
            "s/:10040000FFFFFFFFFFFFFFFFFFFFFFFFDEF9FFFF23/:10040000FFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFD/",
            "$BUILD_DIR/firmware.hex"
        ]), "Fixing $BUILD_DIR/firmware.hex secure flash flags"))


    def _jlink_cmd_script(env, source):
        build_dir = env.subst("$BUILD_DIR")
        if not isdir(build_dir):
            makedirs(build_dir)
        script_path = join(build_dir, "upload.jlink")
        commands = ["h", "loadbin %s,0x0" % source, "r", "q"]
        with open(script_path, "w") as fp:
            fp.write("\n".join(commands))
        return script_path

    env.Replace(
        __jlink_cmd_script=_jlink_cmd_script,
        UPLOADER="/full/path/to/JLink",
        UPLOADERFLAGS=[
            "-device", "MK20DX256xxx7",
            "-speed", "4000",
            "-if", "swd",
            "-autoconnect", "1"
        ],
        UPLOADCMD='"$UPLOADER" $UPLOADERFLAGS -CommanderScript ${__jlink_cmd_script(__env__, SOURCE)}'
    )


ST-Util and ST-Link
'''''''''''''''''''

On-board ST-Link V2/V2-1 in pair with `ST-Util GDB Server <https://github.com/texane/stlink>`_:

.. code-block:: ini

    [env:debug]
    platform = ststm32
    framework = mbed
    board = ...
    debug_tool = custom
    debug_port = :4242
    debug_server = $PLATFORMIO_HOME_DIR/packages/tool-stlink/bin/st-util

OpenOCD and ST-Link
'''''''''''''''''''

On-board ST-Link V2/V2-1 in pair with `OpenOCD GDB Server <http://openocd.org>`_:

.. code-block:: ini

    [env:debug]
    platform = ststm32
    framework = mbed
    board = ...
    debug_tool = custom
    debug_server =
      $PLATFORMIO_HOME_DIR/packages/tool-openocd/bin/openocd
      -f
      $PLATFORMIO_HOME_DIR/packages/tool-openocd/scripts/board/st_nucleo_f4.cfg

pyOCD and CMSIS-DAP
'''''''''''''''''''

Using pyOCD for CMSIS-DAP based boards

Firstly, please install `pyOCD <https://github.com/mbedmicro/pyOCD>`__ and
check that ``pyocd-gdbserver --version`` command works.

.. code-block:: ini

    [env:debug]
    platform = ...
    board = ...
    framework = mbed
    debug_tool = custom
    debug_server = pyocd-gdbserver


User Guide (CLI)
----------------

.. toctree::
    :maxdepth: 3

    platformio debug <../userguide/cmd_debug>


.. _debugging_platforms:

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_atmelsam`
      - Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

    * - :ref:`platform_espressif32`
      - Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

    * - :ref:`platform_freescalekinetis`
      - Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

    * - :ref:`platform_maxim32`
      - Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

    * - :ref:`platform_nordicnrf51`
      - The Nordic nRF51 Series is a family of highly flexible, multi-protocol, system-on-chip (SoC) devices for ultra-low power wireless applications. nRF51 Series devices support a range of protocol stacks including Bluetooth Smart (previously called Bluetooth low energy), ANT and proprietary 2.4GHz protocols such as Gazell.

    * - :ref:`platform_nordicnrf52`
      - The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor and are the most capable Bluetooth Smart SoCs on the market. 

    * - :ref:`platform_nxplpc`
      - The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

    * - :ref:`platform_wiznet7500`
      - The IOP (Internet Offload Processor) W7500 is the one-chip solution which integrates an ARM Cortex-M0, 128KB Flash and hardwired TCP/IP core for various embedded application platform especially requiring Internet of things

    * - :ref:`platform_riscv`
      - RISC-V is an open, free ISA enabling a new era of processor innovation through open standard collaboration. Born in academia and research, RISC-V ISA delivers a new level of free, extensible software and hardware freedom on architecture, paving the way for the next 50 years of computing design and innovation.

    * - :ref:`platform_samsung_artik`
      - The Samsung ARTIK Smart IoT platform brings hardware modules and cloud services together, with built-in security and an ecosystem of tools and partners to speed up your time-to-market.

    * - :ref:`platform_siliconlabsefm32`
      - Silicon Labs EFM32 Gecko 32-bit microcontroller (MCU) family includes devices that offer flash memory configurations up to 256 kB, 32 kB of RAM and CPU speeds up to 48 MHz. Based on the powerful ARM Cortex-M core, the Gecko family features innovative low energy techniques, short wake-up time from energy saving modes and a wide selection of peripherals, making it ideal for battery operated applications and other systems requiring high performance and low-energy consumption.

    * - :ref:`platform_ststm32`
      - The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

    * - :ref:`platform_teensy`
      - Teensy is a complete USB-based microcontroller development system, in a very small footprint, capable of implementing many types of projects. All programming is done via the USB port. No special programmer is needed, only a standard USB cable and a PC or Macintosh with a USB port.

    * - :ref:`platform_timsp430`
      - MSP430 microcontrollers (MCUs) from Texas Instruments (TI) are 16-bit, RISC-based, mixed-signal processors designed for ultra-low power. These MCUs offer the lowest power consumption and the perfect mix of integrated peripherals for thousands of applications.

    * - :ref:`platform_titiva`
      - Texas Instruments TM4C12x MCUs offer the industrys most popular ARM Cortex-M4 core with scalable memory and package options, unparalleled connectivity peripherals, advanced application functions, industry-leading analog integration, and extensive software solutions.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_cmsis`
      - The ARM Cortex Microcontroller Software Interface Standard (CMSIS) is a vendor-independent hardware abstraction layer for the Cortex-M processor series and specifies debugger interfaces. The CMSIS enables consistent and simple software interfaces to the processor for interface peripherals, real-time operating systems, and middleware. It simplifies software re-use, reducing the learning curve for new microcontroller developers and cutting the time-to-market for devices.

    * - :ref:`framework_energia`
      - Energia Wiring-based framework enables pretty much anyone to start easily creating microcontroller-based projects and applications. Its easy-to-use libraries and functions provide developers of all experience levels to start blinking LEDs, buzzing buzzers and sensing sensors more quickly than ever before.

    * - :ref:`framework_espidf`
      - Espressif IoT Development Framework. Official development framework for ESP32.

    * - :ref:`framework_freedom-e-sdk`
      - Open Source Software for Developing on the SiFive Freedom E Platform

    * - :ref:`framework_libopencm3`
      - The libOpenCM3 framework aims to create a free/libre/open-source firmware library for various ARM Cortex-M0(+)/M3/M4 microcontrollers, including ST STM32, Ti Tiva and Stellaris, NXP LPC 11xx, 13xx, 15xx, 17xx parts, Atmel SAM3, Energy Micro EFM32 and others.

    * - :ref:`framework_mbed`
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.

    * - :ref:`framework_simba`
      - Simba is an RTOS and build framework. It aims to make embedded programming easy and portable.

    * - :ref:`framework_spl`
      - The ST Standard Peripheral Library provides a set of functions for handling the peripherals on the STM32 Cortex-M3 family. The idea is to save the user (the new user, in particular) having to deal directly with the registers.

    * - :ref:`framework_stm32cube`
      - STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency.

    * - :ref:`framework_tizenrt`
      - Tizen RT is a lightweight RTOS-based platform to support low-end IoT devices

Boards
------

.. note::
    For more detailed ``board`` information please scroll tables below by horizontal.

1BitSquared
~~~~~~~~~~~

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
    * - ``1bitsy_stm32f415rgt``
      - `1Bitsy <http://1bitsy.org?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F415RGT
      - 168MHz
      - 1MB
      - 128KB

96Boards
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
    * - ``b96b_f446ve``
      - `96Boards B96B-F446VE <https://developer.mbed.org/platforms/ST-B96B-F446VE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F446VET6
      - 168MHz
      - 512KB
      - 128KB

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
    * - ``adafruit_circuitplayground_m0``
      - `Adafruit Circuit Playground Express <https://www.adafruit.com/product/3333?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_feather_m0``
      - `Adafruit Feather M0 <https://www.adafruit.com/product/2772?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_feather_m0_express``
      - `Adafruit Feather M0 Express <https://www.adafruit.com/product/3403?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_gemma_m0``
      - `Adafruit Gemma M0 <https://www.adafruit.com/product/3501?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_metro_m0``
      - `Adafruit Metro M0 Expresss <https://www.adafruit.com/product/3505?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_trinket_m0``
      - `Adafruit Trinket M0 <https://www.adafruit.com/product/3500?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``featheresp32``
      - `Adafruit ESP32 Feather <https://www.adafruit.com/product/3405?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB

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
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB

Arduino
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
    * - ``due``
      - `Arduino Due (Programming Port) <https://www.arduino.cc/en/Main/ArduinoBoardDue?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 32KB
    * - ``dueUSB``
      - `Arduino Due (USB Native Port) <https://www.arduino.cc/en/Main/ArduinoBoardDue?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 32KB
    * - ``mkr1000USB``
      - `Arduino MKR1000 <https://www.arduino.cc/en/Main/ArduinoMKR1000?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrfox1200``
      - `Arduino MKR FOX 1200 <https://www.arduino.cc/en/Main.ArduinoBoardMKRFox1200?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrgsm1400``
      - `Arduino MKR GSM 1400 <https://store.arduino.cc/mkr-gsm-1400?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrwan1300``
      - `Arduino MKR WAN 1300 <https://store.arduino.cc/mkr-wan-1300?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mkrzero``
      - `Arduino MKRZERO <https://www.arduino.cc/en/Main/ArduinoBoardMKRZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mzeroUSB``
      - `Arduino M0 <https://www.arduino.cc/en/Main/ArduinoBoardM0?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mzeropro``
      - `Arduino M0 Pro (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardM0PRO?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mzeroproUSB``
      - `Arduino M0 Pro (Native USB Port) <https://www.arduino.cc/en/Main/ArduinoBoardM0PRO?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``tian``
      - `Arduino Tian <https://www.arduino.cc/en/Main/ArduinoBoardTian?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``zero``
      - `Arduino Zero (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``zeroUSB``
      - `Arduino Zero (USB Native Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

Armstrap
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
    * - ``armstrap_eagle1024``
      - `Armstrap Eagle 1024 <http://docs.armstrap.org/en/latest/hardware-overview.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F417VGT6
      - 168MHz
      - 1MB
      - 192KB
    * - ``armstrap_eagle2048``
      - `Armstrap Eagle 2048 <http://docs.armstrap.org/en/latest/hardware-overview.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F427VIT6
      - 168MHz
      - 1.99MB
      - 256KB
    * - ``armstrap_eagle512``
      - `Armstrap Eagle 512 <http://docs.armstrap.org/en/latest/hardware-overview.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB

Atmel
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
    * - ``samd21_xpro``
      - `Atmel SAMD21-XPRO <https://developer.mbed.org/platforms/SAMD21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``samd21g18a``
      - `Atmel ATSAMW25-XPRO <https://developer.mbed.org/platforms/SAMW25-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``saml21_xpro_b``
      - `Atmel SAML21-XPRO-B <https://developer.mbed.org/platforms/SAML21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAML21J18B
      - 48MHz
      - 256KB
      - 32KB
    * - ``samr21_xpro``
      - `Atmel ATSAMR21-XPRO <https://developer.mbed.org/platforms/SAMR21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMR21G18A
      - 48MHz
      - 256KB
      - 32KB

BBC
~~~

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
    * - ``bbcmicrobit``
      - `BBC micro:bit <https://developer.mbed.org/platforms/Microbit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``bbcmicrobit_b``
      - `BBC micro:bit B(S130) <https://developer.mbed.org/platforms/Microbit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

BluzDK
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
    * - ``bluz_dk``
      - `BluzDK <https://bluz.io/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

CQ Publishing
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
    * - ``lpc11u35_501``
      - `CQ Publishing TG-LPC11U35-501 <https://developer.mbed.org/platforms/TG-LPC11U35-501/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB

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
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB

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
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB

Delta
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
    * - ``delta_dfbm_nq620``
      - `Delta DFBM-NQ620 <https://developer.mbed.org/platforms/Delta-DFBM-NQ620/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``delta_dfcm_nnn50``
      - `Delta DFCM-NNN50 <https://os.mbed.com/platforms/Delta-DFCM-NNN50/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 32MHz
      - 256KB
      - 16KB
    * - ``dfcm_nnn40``
      - `Delta DFCM-NNN40 <https://developer.mbed.org/platforms/Delta-DFCM-NNN40/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

Digistump
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
    * - ``digix``
      - `Digistump DigiX <http://digistump.com/products/50?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 28KB

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
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB

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
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB

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
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB

Elektor Labs
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
    * - ``elektor_cocorico``
      - `CoCo-ri-Co! <https://developer.mbed.org/platforms/CoCo-ri-Co/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC812
      - 30MHz
      - 16KB
      - 4KB

Embedded Artists
~~~~~~~~~~~~~~~~

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
    * - ``lpc11u35``
      - `EA LPC11U35 QuickStart Board <https://developer.mbed.org/platforms/EA-LPC11U35/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
    * - ``lpc4088``
      - `Embedded Artists LPC4088 QuickStart Board <https://developer.mbed.org/platforms/EA-LPC4088/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - LPC4088
      - 120MHz
      - 512KB
      - 96KB
    * - ``lpc4088_dm``
      - `Embedded Artists LPC4088 Display Module <https://developer.mbed.org/platforms/EA-LPC4088-Display-Module/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - LPC4088
      - 120MHz
      - 512KB
      - 96KB

Espotel
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
    * - ``elmo_f411re``
      - `Espotel LoRa Module <https://developer.mbed.org/platforms/Espotel-ELMO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink` (default)
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB

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
      - :ref:`debugging_tool_ft2232h` (default, on-board), :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB
    * - ``esp32dev``
      - `Espressif ESP32 Dev Module <https://en.wikipedia.org/wiki/ESP32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB

Freescale
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
    * - ``IBMEthernetKit``
      - `Ethernet IoT Starter Kit <http://developer.mbed.org/platforms/IBMEthernetKit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - MK64FN1M0VLL12
      - 120MHz
      - 1MB
      - 256KB
    * - ``frdm_k20d50m``
      - `Freescale Kinetis FRDM-K20D50M <https://developer.mbed.org/platforms/FRDM-K20D50M/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - MK20DX128VLH5
      - 48MHz
      - 128KB
      - 16KB
    * - ``frdm_k22f``
      - `Freescale Kinetis FRDM-K22F <https://developer.mbed.org/platforms/FRDM-K22F/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - MK22FN512VLH12
      - 120MHz
      - 512KB
      - 128KB
    * - ``frdm_k64f``
      - `Freescale Kinetis FRDM-K64F <https://developer.mbed.org/platforms/FRDM-K64F/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - MK64FN1M0VLL12
      - 120MHz
      - 1MB
      - 256KB
    * - ``frdm_k66f``
      - `Freescale Kinetis FRDM-K66F <https://developer.mbed.org/platforms/FRDM-K66F/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - MK66FN2M0VMD18
      - 180MHz
      - 2MB
      - 256KB
    * - ``frdm_kl05z``
      - `Freescale Kinetis FRDM-KL05Z <https://developer.mbed.org/platforms/FRDM-KL05Z/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - MKL05Z32VFM4
      - 48MHz
      - 32KB
      - 4KB
    * - ``frdm_kl25z``
      - `Freescale Kinetis FRDM-KL25Z <https://developer.mbed.org/platforms/KL25Z/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - MKL25Z128VLK4
      - 48MHz
      - 128KB
      - 16KB
    * - ``frdm_kl27z``
      - `Freescale Kinetis FRDM-KL27Z <https://os.mbed.com/platforms/FRDM-KL27Z/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - MKL27Z64VLH4
      - 48MHz
      - 64KB
      - 16KB
    * - ``frdm_kl43z``
      - `Freescale Kinetis FRDM-KL43Z <https://os.mbed.com/platforms/FRDM-KL43Z/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - MKL43Z256VLH4
      - 48MHz
      - 256KB
      - 32KB
    * - ``frdm_kl46z``
      - `Freescale Kinetis FRDM-KL46Z <https://developer.mbed.org/platforms/FRDM-KL46Z/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - MKL46Z256VLL4
      - 48MHz
      - 256KB
      - 32KB
    * - ``frdm_kw41z``
      - `Freescale Kinetis FRDM-KW41Z <https://os.mbed.com/platforms/FRDM-KW41Z/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - MKW41Z512VHT4
      - 48MHz
      - 512KB
      - 128KB

Generic
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
    * - ``bluepill_f103c8``
      - `BluePill F103C8 <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``genericSTM32F103C8``
      - `STM32F103C8 (20k RAM. 64k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``genericSTM32F103CB``
      - `STM32F103CB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103cb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103CBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``genericSTM32F103R8``
      - `STM32F103R8 (20k RAM. 64 Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103r8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103R8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``genericSTM32F103RB``
      - `STM32F103RB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``genericSTM32F103RC``
      - `STM32F103RC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rc.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103RCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``genericSTM32F103RE``
      - `STM32F103RE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103re.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103RET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``genericSTM32F103VC``
      - `STM32F103VC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``genericSTM32F103VE``
      - `STM32F103VE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103VET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``genericSTM32F407VET6``
      - `STM32F407VE (192k RAM. 512k Flash) <http://www.st.com/en/microcontrollers/stm32f407ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink`
      - STM32F407VET6
      - 168MHz
      - 502.23KB
      - 128KB

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
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB
    * - ``hornbill32minima``
      - `Hornbill ESP32 Minima <https://hackaday.io/project/18997-hornbill?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB

JKSoft
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
    * - ``wallbot_ble``
      - `JKSoft Wallbot BLE <https://developer.mbed.org/platforms/JKSoft-Wallbot-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB

LeafLabs
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
    * - ``maple``
      - `Maple <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103RBT6
      - 72MHz
      - 108KB
      - 17KB
    * - ``maple_mini_b20``
      - `Maple Mini Bootloader 2.0 <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103CBT6
      - 72MHz
      - 120KB
      - 20KB
    * - ``maple_mini_origin``
      - `Maple Mini Original <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103CBT6
      - 72MHz
      - 108KB
      - 17KB

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
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB
    * - ``mhetesp32minikit``
      - `MH ET LIVE ESP32MiniKit <http://forum.mhetlive.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB

MXChip
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
    * - ``mxchip_az3166``
      - `Microsoft Azure IoT Development Kit (MXChip AZ3166) <https://microsoft.github.io/azure-iot-developer-kit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB

Macchina
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
    * - ``macchina2``
      - `Macchina M2 <https://www.macchina.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 32KB

Maxim
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
    * - ``max32600mbed``
      - `Maxim ARM mbed Enabled Development Platform for MAX32600 <https://developer.mbed.org/platforms/MAX32600mbed/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - MAX32600
      - 24MHz
      - 256KB
      - 32KB
    * - ``maxwsnenv``
      - `Maxim Wireless Sensor Node Demonstrator <https://developer.mbed.org/platforms/MAXWSNENV/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - :ref:`debugging_tool_cmsis-dap`
      - MAX32610
      - 24MHz
      - 256KB
      - 32KB

Micromint
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
    * - ``lpc4330_m4``
      - `Bambino-210E <https://developer.mbed.org/platforms/Micromint-Bambino-210E/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC4330
      - 204MHz
      - 8MB
      - 264KB

MikroElektronika
~~~~~~~~~~~~~~~~

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
    * - ``hexiwear``
      - `Hexiwear <https://developer.mbed.org/platforms/Hexiwear/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap`, :ref:`debugging_tool_jlink`
      - MK64FN1M0VDC12
      - 120MHz
      - 1MB
      - 256KB

MultiTech
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
    * - ``mts_dragonfly_f411re``
      - `MTS Dragonfly <https://developer.mbed.org/platforms/MTS-Dragonfly/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``mts_mdot_f405rg``
      - `MultiTech mDot <https://developer.mbed.org/platforms/MTS-mDot-F411/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``mts_mdot_f411re``
      - `MultiTech mDot F411 <https://developer.mbed.org/platforms/MTS-mDot-F411/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``xdot_l151cc``
      - `MultiTech xDot <https://developer.mbed.org/platforms/MTS-xDot-L151CC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32L151CCU6
      - 32MHz
      - 256KB
      - 32KB

NGX Technologies
~~~~~~~~~~~~~~~~

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
    * - ``blueboard_lpc11u24``
      - `NGX Technologies BlueBoard-LPC11U24 <https://developer.mbed.org/platforms/BlueBoard-LPC11U24/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB

NXP
~~~

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
    * - ``lpc11c24``
      - `NXP LPC11C24 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-m0-cores:LPC11C24FBD48?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11C24
      - 48MHz
      - 32KB
      - 8KB
    * - ``lpc11u24``
      - `NXP mbed LPC11U24 <https://developer.mbed.org/platforms/mbed-LPC11U24/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - ``lpc11u24_301``
      - `ARM mbed LPC11U24 (+CAN) <https://developer.mbed.org/handbook/mbed-NXP-LPC11U24?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - ``lpc11u34_421``
      - `NXP LPC11U34 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/40kb-flash-8kb-sram-lqfp48-package:LPC11U34FBD48?lang_cd=en&utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U34
      - 48MHz
      - 40KB
      - 8KB
    * - ``lpc11u37_501``
      - `NXP LPC11U37 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/128kb-flash-10kb-sram-lqfp48-package:LPC11U37FBD48?lang_cd=en&utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U37
      - 48MHz
      - 128KB
      - 10KB
    * - ``lpc11u68``
      - `LPCXpresso11U68 <https://developer.mbed.org/platforms/LPCXpresso11U68/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U68
      - 50MHz
      - 256KB
      - 36KB
    * - ``lpc1549``
      - `NXP LPCXpresso1549 <https://developer.mbed.org/platforms/LPCXpresso1549/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC1549
      - 72MHz
      - 256KB
      - 36KB
    * - ``lpc1768``
      - `NXP mbed LPC1768 <http://developer.mbed.org/platforms/mbed-LPC1768/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB
    * - ``lpc54114``
      - `NXP LPCXpresso54114 <https://os.mbed.com/platforms/LPCXpresso54114/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - LPC54114J256BD64
      - 100MHz
      - 256KB
      - 192KB
    * - ``lpc546xx``
      - `NXP LPCXpresso54608 <https://os.mbed.com/platforms/LPCXpresso54608/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_jlink` (on-board)
      - LPC54608ET512
      - 180MHz
      - 512KB
      - 200KB
    * - ``lpc812``
      - `NXP LPC800-MAX <https://developer.mbed.org/platforms/NXP-LPC800-MAX/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC812
      - 30MHz
      - 16KB
      - 4KB
    * - ``lpc824``
      - `LPCXpresso824-MAX <https://developer.mbed.org/platforms/LPCXpresso824-MAX/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC824
      - 30MHz
      - 32KB
      - 8KB

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
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB

Nordic
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
    * - ``nrf51_dk``
      - `Nordic nRF51-DK <https://developer.mbed.org/platforms/Nordic-nRF51-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``nrf51_dongle``
      - `Nordic nRF51-Dongle <https://developer.mbed.org/platforms/Nordic-nRF51-Dongle/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink` (on-board)
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``nrf51_mkit``
      - `Nordic nRF51822-mKIT <http://developer.mbed.org/platforms/Nordic-nRF51822/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB
    * - ``nrf52840_dk``
      - `Nordic nRF52840-DK <https://os.mbed.com/platforms/Nordic-nRF52840-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - ``nrf52_dk``
      - `Nordic nRF52-DK <https://developer.mbed.org/platforms/Nordic-nRF52-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

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
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB
    * - ``esp32-gateway``
      - `OLIMEX ESP32-GATEWAY <https://www.olimex.com/Products/IoT/ESP32-GATEWAY/open-source-hardware?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB

OSHChip
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
    * - ``oshchip``
      - `OSHChip <http://oshchip.org/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

RFduino
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
    * - ``rfduino``
      - `RFduino <http://www.rfduino.com/product/rfd22102-rfduino-dip/index.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 128KB
      - 8KB

RedBearLab
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
    * - ``redBearLab``
      - `RedBearLab nRF51822 <https://developer.mbed.org/platforms/RedBearLab-nRF51822/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``redBearLabBLENano``
      - `RedBearLab BLE Nano 1.5 <https://developer.mbed.org/platforms/RedBearLab-BLE-Nano/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB
    * - ``redbear_blenano2``
      - `RedBearLab BLE Nano 2 <https://redbear.cc/product/ble-nano-2-soldered.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``redbear_blend2``
      - `RedBearLab Blend 2 <https://redbear.cc/product/ble/blend-2.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

RushUp
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
    * - ``cloud_jam``
      - `RushUp Cloud-JAM <https://developer.mbed.org/platforms/ST-Nucleo-F401RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F401RET6
      - 84MHz
      - 512KB
      - 96KB
    * - ``cloud_jam_l4``
      - `RushUp Cloud-JAM L4 <https://developer.mbed.org/platforms/ST-Nucleo-L476RG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L476RGT6
      - 80MHz
      - 1MB
      - 128KB

SODAQ
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
    * - ``sodaq_autonomo``
      - `SODAQ Autonomo <http://support.sodaq.com/sodaq-one/autonomo/getting-started-autonomo/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sodaq_explorer``
      - `SODAQ ExpLoRer <http://support.sodaq.com/sodaq-one/explorer/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sodaq_one``
      - `SODAQ ONE <http://support.sodaq.com/sodaq-one/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

ST
~~

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
    * - ``disco_f030r8``
      - `ST STM32F0308DISCOVERY <http://www.st.com/en/evaluation-tools/32f0308discovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - ``disco_f051r8``
      - `ST STM32F0DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF253215?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F051R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - ``disco_f100rb``
      - `ST STM32VLDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF250863?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F100RBT6
      - 24MHz
      - 128KB
      - 8KB
    * - ``disco_f303vc``
      - `ST STM32F3DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF254044?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F303VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``disco_f334c8``
      - `ST 32F3348DISCOVERY <http://www.st.com/web/en/catalog/tools/PF260318?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F334C8T6
      - 72MHz
      - 64KB
      - 12KB
    * - ``disco_f401vc``
      - `ST 32F401CDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF259098?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F401VCT6
      - 84MHz
      - 256KB
      - 64KB
    * - ``disco_f407vg``
      - `ST STM32F4DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF252419?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F407VGT6
      - 168MHz
      - 1MB
      - 128KB
    * - ``disco_f411ve``
      - `ST 32F411EDISCOVERY <http://www.st.com/en/evaluation-tools/32f411ediscovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F411VET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``disco_f413zh``
      - `ST 32F413HDISCOVERY <https://os.mbed.com/platforms/ST-Discovery-F413H/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F413ZHT6
      - 100MHz
      - 512KB
      - 128KB
    * - ``disco_f429zi``
      - `ST 32F429IDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF259090?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F429ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - ``disco_f469ni``
      - `ST 32F469IDISCOVERY <http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF262395?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F469NIH6
      - 180MHz
      - 1MB
      - 384KB
    * - ``disco_f746ng``
      - `ST 32F746GDISCOVERY <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/32f746gdiscovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F746NGH6
      - 216MHz
      - 1MB
      - 320KB
    * - ``disco_f769ni``
      - `ST 32F769IDISCOVERY <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/32f769idiscovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F769NIH6
      - 80MHz
      - 1MB
      - 512KB
    * - ``disco_l053c8``
      - `ST 32L0538DISCOVERY <http://www.st.com/web/en/catalog/tools/PF260319?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L053C8T6
      - 32MHz
      - 64KB
      - 8KB
    * - ``disco_l072cz_lrwan1``
      - `ST DISCO-L072CZ-LRWAN1 <https://developer.mbed.org/platforms/ST-Discovery-LRWAN1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L072CZ
      - 32MHz
      - 192KB
      - 20KB
    * - ``disco_l152rb``
      - `ST STM32LDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF258515?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L152RBT6
      - 32MHz
      - 128KB
      - 16KB
    * - ``disco_l475vg_iot01a``
      - `ST DISCO-L475VG-IOT01A <https://developer.mbed.org/platforms/ST-Discovery-L475E-IOT01A/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L475VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - ``disco_l476vg``
      - `ST 32L476GDISCOVERY <http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF261635?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L476VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - ``eval_l073z``
      - `ST STM32L073Z-EVAL <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-eval-boards/stm32l073z-eval.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L073VZT6
      - 32MHz
      - 192KB
      - 20KB
    * - ``nucleo_f030r8``
      - `ST Nucleo F030R8 <https://developer.mbed.org/platforms/ST-Nucleo-F030R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - ``nucleo_f031k6``
      - `ST Nucleo F031K6 <https://developer.mbed.org/platforms/ST-Nucleo-F031K6/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F031K6T6
      - 48MHz
      - 32KB
      - 4KB
    * - ``nucleo_f042k6``
      - `ST Nucleo F042K6 <https://developer.mbed.org/platforms/ST-Nucleo-F042K6/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F042K6T6
      - 48MHz
      - 32KB
      - 6KB
    * - ``nucleo_f070rb``
      - `ST Nucleo F070RB <https://developer.mbed.org/platforms/ST-Nucleo-F070RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F070RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - ``nucleo_f072rb``
      - `ST Nucleo F072RB <https://developer.mbed.org/platforms/ST-Nucleo-F072RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F072RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - ``nucleo_f091rc``
      - `ST Nucleo F091RC <https://developer.mbed.org/platforms/ST-Nucleo-F091RC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F091RCT6
      - 48MHz
      - 256KB
      - 32KB
    * - ``nucleo_f103rb``
      - `ST Nucleo F103RB <https://developer.mbed.org/platforms/ST-Nucleo-F103RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``nucleo_f207zg``
      - `ST Nucleo F207ZG <https://developer.mbed.org/platforms/ST-Nucleo-F207ZG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F207ZGT6
      - 120MHz
      - 1MB
      - 128KB
    * - ``nucleo_f302r8``
      - `ST Nucleo F302R8 <https://developer.mbed.org/platforms/ST-Nucleo-F302R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F302R8T6
      - 72MHz
      - 64KB
      - 16KB
    * - ``nucleo_f303k8``
      - `ST Nucleo F303K8 <https://developer.mbed.org/platforms/ST-Nucleo-F303K8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F303K8T6
      - 72MHz
      - 64KB
      - 16KB
    * - ``nucleo_f303re``
      - `ST Nucleo F303RE <http://developer.mbed.org/platforms/ST-Nucleo-F303RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F303RET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``nucleo_f303ze``
      - `ST Nucleo F303ZE <https://developer.mbed.org/platforms/ST-Nucleo-F303ZE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F303ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``nucleo_f334r8``
      - `ST Nucleo F334R8 <https://developer.mbed.org/platforms/ST-Nucleo-F334R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F334R8T6
      - 72MHz
      - 64KB
      - 16KB
    * - ``nucleo_f401re``
      - `ST Nucleo F401RE <https://developer.mbed.org/platforms/ST-Nucleo-F401RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F401RET6
      - 84MHz
      - 512KB
      - 96KB
    * - ``nucleo_f410rb``
      - `ST Nucleo F410RB <https://developer.mbed.org/platforms/ST-Nucleo-F410RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F410RBT6
      - 100MHz
      - 128KB
      - 32KB
    * - ``nucleo_f411re``
      - `ST Nucleo F411RE <https://developer.mbed.org/platforms/ST-Nucleo-F411RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``nucleo_f412zg``
      - `ST Nucleo F412ZG <https://developer.mbed.org/platforms/ST-Nucleo-F411RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB
    * - ``nucleo_f413zh``
      - `ST Nucleo F413ZH <https://os.mbed.com/platforms/ST-Nucleo-F413ZH/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F413ZHT6
      - 100MHz
      - 512KB
      - 128KB
    * - ``nucleo_f429zi``
      - `ST Nucleo F429ZI <https://developer.mbed.org/platforms/ST-Nucleo-F429ZI/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F429ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - ``nucleo_f446re``
      - `ST Nucleo F446RE <https://developer.mbed.org/platforms/ST-Nucleo-F446RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB
    * - ``nucleo_f446ze``
      - `ST Nucleo F446ZE <https://developer.mbed.org/platforms/ST-Nucleo-F446ZE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F446ZET6
      - 180MHz
      - 512KB
      - 128KB
    * - ``nucleo_f746zg``
      - `ST Nucleo F746ZG <https://developer.mbed.org/platforms/ST-Nucleo-F446ZE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F746ZGT6
      - 216MHz
      - 1MB
      - 320KB
    * - ``nucleo_f767zi``
      - `ST Nucleo F767ZI <https://developer.mbed.org/platforms/ST-Nucleo-F767ZI/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F767ZIT6
      - 216MHz
      - 2MB
      - 512KB
    * - ``nucleo_l011k4``
      - `ST Nucleo L011K4 <https://developer.mbed.org/platforms/ST-Nucleo-L011K4/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L011K4T6
      - 32MHz
      - 16KB
      - 2KB
    * - ``nucleo_l031k6``
      - `ST Nucleo L031K6 <https://developer.mbed.org/platforms/ST-Nucleo-L031K6/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L031K6T6
      - 32MHz
      - 32KB
      - 8KB
    * - ``nucleo_l053r8``
      - `ST Nucleo L053R8 <https://developer.mbed.org/platforms/ST-Nucleo-L053R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L053R8T6
      - 32MHz
      - 64KB
      - 8KB
    * - ``nucleo_l073rz``
      - `ST Nucleo L073RZ <https://developer.mbed.org/platforms/ST-Nucleo-L073RZ/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L073RZ
      - 32MHz
      - 192KB
      - 20KB
    * - ``nucleo_l152re``
      - `ST Nucleo L152RE <https://developer.mbed.org/platforms/ST-Nucleo-L152RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L152RET6
      - 32MHz
      - 512KB
      - 80KB
    * - ``nucleo_l432kc``
      - `ST Nucleo L432KC <https://developer.mbed.org/platforms/ST-Nucleo-L432KC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L432KCU6
      - 80MHz
      - 256KB
      - 64KB
    * - ``nucleo_l476rg``
      - `ST Nucleo L476RG <https://developer.mbed.org/platforms/ST-Nucleo-L476RG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L476RGT6
      - 80MHz
      - 1MB
      - 128KB
    * - ``nucleo_l496zg``
      - `ST Nucleo L496ZG <https://developer.mbed.org/platforms/ST-Nucleo-L476RG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L496ZGT6
      - 80MHz
      - 1MB
      - 128KB

SainSmart
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
    * - ``sainSmartDue``
      - `SainSmart Due (Programming Port) <http://www.sainsmart.com/arduino/control-boards/sainsmart-due-atmel-sam3x8e-arm-cortex-m3-board-black.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 32KB
    * - ``sainSmartDueUSB``
      - `SainSmart Due (USB Native Port) <http://www.sainsmart.com/arduino/control-boards/sainsmart-due-atmel-sam3x8e-arm-cortex-m3-board-black.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 32KB

Samsung
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
    * - ``artik_053``
      - `Samsung ARTIK053 <http://www.artik.io?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Samsung ARTIK <platform_samsung_artik>`
      - :ref:`debugging_tool_custom` (default)
      - S5JT200
      - 320MHz
      - 8MB
      - 1.25MB

SeeedStudio
~~~~~~~~~~~

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
    * - ``seeedArchBLE``
      - `Seeed Arch BLE <https://developer.mbed.org/platforms/Seeed-Arch-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB
    * - ``seeedArchLink``
      - `Seeed Arch Link <https://developer.mbed.org/platforms/Seeed-Arch-Link/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``seeedArchMax``
      - `Seeed Arch Max <https://developer.mbed.org/platforms/Seeed-Arch-Max/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB
    * - ``seeedArchPro``
      - `Seeed Arch Pro <https://developer.mbed.org/platforms/Seeeduino-Arch-Pro/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB
    * - ``seeedTinyBLE``
      - `Seeed Tiny BLE <http://developer.mbed.org/platforms/Seeed-Tiny-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

Semtech
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
    * - ``mote_l152rc``
      - `NAMote72 <https://developer.mbed.org/platforms/NAMote-72/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32L152RC
      - 32MHz
      - 256KB
      - 32KB

SiFive
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
    * - ``freedom-e300-hifive1``
      - `HiFive1 <https://www.sifive.com/products/hifive1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`RISC-V <platform_riscv>`
      - :ref:`debugging_tool_ft2232h` (on-board)
      - FE310
      - 320MHz
      - 16MB
      - 16KB

Silicon Labs
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
    * - ``efm32gg_stk3700``
      - `Silicon Labs EFM32GG-STK3700 (Giant Gecko) <https://developer.mbed.org/platforms/EFM32-Giant-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32GG990F1024
      - 48MHz
      - 1MB
      - 128KB
    * - ``efm32hg_stk3400``
      - `Silicon Labs SLSTK3400A USB-enabled (Happy Gecko) <https://developer.mbed.org/platforms/EFM32-Happy-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32HG322F64
      - 24MHz
      - 64KB
      - 8KB
    * - ``efm32lg_stk3600``
      - `Silicon Labs EFM32LG-STK3600 (Leopard Gecko) <https://developer.mbed.org/platforms/EFM32-Leopard-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32LG990F256
      - 48MHz
      - 256KB
      - 32KB
    * - ``efm32pg_stk3401``
      - `Silicon Labs SLSTK3401A (Pearl Gecko) <https://developer.mbed.org/platforms/EFM32-Pearl-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32PG1B200F256
      - 40MHz
      - 256KB
      - 32KB
    * - ``efm32wg_stk3800``
      - `Silicon Labs EFM32WG-STK3800 (Wonder Gecko) <https://developer.mbed.org/platforms/EFM32-Wonder-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32WG990F256
      - 48MHz
      - 256KB
      - 32KB
    * - ``efm32zg_stk3200``
      - `Silicon Labs EFM32ZG-STK3200 (Zero Gecko) <https://developer.mbed.org/platforms/EFM32-Zero-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32ZG222F32
      - 24MHz
      - 32KB
      - 4KB

Solder Splash Labs
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
    * - ``dipcortexm0``
      - `Solder Splash Labs DipCortex M0 <https://developer.mbed.org/platforms/DipCortex-M0/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U24
      - 50MHz
      - 32KB
      - 8KB
    * - ``lpc1347``
      - `DipCortex M3 <https://developer.mbed.org/platforms/DipCortex-M3/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_jlink`
      - LPC1347
      - 72MHz
      - 64KB
      - 12KB

SparkFun
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
    * - ``sparkfun_samd21_dev_usb``
      - `SparkFun SAMD21 Dev Breakout <https://www.sparkfun.com/products/13672?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``sparkfun_samd21_mini_usb``
      - `SparkFun SAMD21 Mini Breakout <https://www.sparkfun.com/products/13664?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

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
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB

Switch Science
~~~~~~~~~~~~~~

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
    * - ``hrm1017``
      - `Switch Science mbed HRM1017 <https://developer.mbed.org/platforms/mbed-HRM1017/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``lpc1114fn28``
      - `Switch Science mbed LPC1114FN28 <https://developer.mbed.org/platforms/LPC1114FN28/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC1114FN28
      - 48MHz
      - 32KB
      - 4KB
    * - ``ssci824``
      - `Switch Science mbed LPC824 <https://developer.mbed.org/platforms/Switch-Science-mbed-LPC824/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC824
      - 30MHz
      - 32KB
      - 8KB
    * - ``ty51822r3``
      - `Switch Science mbed TY51822r3 <https://developer.mbed.org/platforms/Switch-Science-mbed-TY51822r3/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

TI
~~

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
    * - ``lplm4f120h5qr``
      - `TI LaunchPad (Stellaris) w/ lm4f120 (80MHz) <http://www.ti.com/tool/ek-lm4f120xl?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI TIVA <platform_titiva>`
      - :ref:`debugging_tool_ti-icdi` (on-board)
      - LPLM4F120H5QR
      - 80MHz
      - 256KB
      - 32KB
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
    * - ``lptm4c1230c3pm``
      - `TI LaunchPad (Tiva C) w/ tm4c123 (80MHz) <http://www.ti.com/ww/en/launchpad/launchpads-connected-ek-tm4c123gxl.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI TIVA <platform_titiva>`
      - :ref:`debugging_tool_ti-icdi` (on-board)
      - LPTM4C1230C3PM
      - 80MHz
      - 256KB
      - 32KB
    * - ``lptm4c1294ncpdt``
      - `TI LaunchPad (Tiva C) w/ tm4c129 (120MHz) <http://www.ti.com/ww/en/launchpad/launchpads-connected-ek-tm4c1294xl.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI TIVA <platform_titiva>`
      - :ref:`debugging_tool_ti-icdi` (on-board)
      - LPTM4C1294NCPDT
      - 120MHz
      - 1MB
      - 256KB

Taida Century
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
    * - ``stct_nrf52_minidev``
      - `Taida Century nRF52 mini board <http://taida-century.com/en/index.asp?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

Teensy
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
    * - ``teensy31``
      - `Teensy 3.1 / 3.2 <https://www.pjrc.com/store/teensy31.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`debugging_tool_jlink`
      - MK20DX256
      - 72MHz
      - 256KB
      - 64KB
    * - ``teensy35``
      - `Teensy 3.5 <https://www.pjrc.com/store/teensy35.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`debugging_tool_jlink`
      - MK64FX512
      - 120MHz
      - 512KB
      - 192KB
    * - ``teensy36``
      - `Teensy 3.6 <https://www.pjrc.com/store/teensy36.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`debugging_tool_jlink`
      - MK66FX1M0
      - 180MHz
      - 1MB
      - 256KB
    * - ``teensylc``
      - `Teensy LC <http://www.pjrc.com/teensy/teensyLC.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`debugging_tool_jlink`
      - MKL26Z64
      - 48MHz
      - 62KB
      - 8KB

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
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB

VNG
~~~

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
    * - ``vbluno51``
      - `VNG VBLUNO51 <https://os.mbed.com/platforms/VBLUNO51/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 16MHz
      - 128KB
      - 32KB

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
      - `WEMOS LOLIN32 <https://wemos.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB
    * - ``wemosbat``
      - `WeMos WiFi & Bluetooth Battery <https://www.wemos.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - :ref:`debugging_tool_minimodule`, :ref:`debugging_tool_olimex-arm-usb-ocd-h`, :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - ESP32
      - 240MHz
      - 1.25MB
      - 288KB

WIZNet
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
    * - ``wizwiki_w7500``
      - `WIZwiki-W7500 <https://developer.mbed.org/platforms/WIZwiki-W7500/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`WIZNet W7500 <platform_wiznet7500>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - WIZNET7500
      - 48MHz
      - 128KB
      - 48KB
    * - ``wizwiki_w7500eco``
      - `WIZwiki-W7500ECO <https://developer.mbed.org/platforms/WIZwiki-W7500ECO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`WIZNet W7500 <platform_wiznet7500>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - WIZNET7500ECO
      - 48MHz
      - 128KB
      - 48KB
    * - ``wizwiki_w7500p``
      - `WIZwiki-W7500P <https://developer.mbed.org/platforms/WIZwiki-W7500P/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`WIZNet W7500 <platform_wiznet7500>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - WIZNET7500P
      - 48MHz
      - 128KB
      - 48KB

Waveshare
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
    * - ``waveshare_ble400``
      - `Waveshare BLE400 <http://www.waveshare.com/wiki/BLE400?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

Xilinx
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
    * - ``coreplexip-e31-arty``
      - `Freedom E310 Arty (Artix-7) FPGA Dev Kit <http://www.xilinx.com/products/boards-and-kits/arty.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`RISC-V <platform_riscv>`
      - :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - E31
      - 320MHz
      - 16MB
      - 256MB
    * - ``coreplexip-e51-arty``
      - `E51 Arty (Artix-7) FPGA Dev Kit <http://www.xilinx.com/products/boards-and-kits/arty.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`RISC-V <platform_riscv>`
      - :ref:`debugging_tool_olimex-arm-usb-tiny-h`
      - E51
      - 1500MHz
      - 16MB
      - 256MB

ng-beacon
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
    * - ``ng_beacon``
      - `ng-beacon <https://github.com/urish/ng-beacon?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

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
    * - ``mbed_connect_odin``
      - `Mbed Connect Cloud <https://os.mbed.com/platforms/mbed-Connect-Cloud/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
    * - ``mtb_ublox_odin_w2``
      - `u-blox ODIN-W2 <https://os.mbed.com/modules/u-blox-odin-w2/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
    * - ``ublox_c030_n211``
      - `u-blox C030-N211 IoT Starter Kit <https://os.mbed.com/platforms/ublox-C030-N211/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - ``ublox_c030_u201``
      - `u-blox C030-U201 IoT Starter Kit <https://os.mbed.com/platforms/ublox-C030-N211/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - ``ublox_evk_nina_b1``
      - `u-blox EVK-NINA-B1 <https://os.mbed.com/platforms/u-blox-EVK-NINA-B1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``ublox_evk_odin_w2``
      - `u-blox EVK-ODIN-W2 <https://developer.mbed.org/platforms/ublox-EVK-ODIN-W2/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
    * - ``ubloxc027``
      - `u-blox C027 <https://developer.mbed.org/platforms/u-blox-C027/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB

y5 design
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
    * - ``lpc11u35_y5_mbug``
      - `y5 LPC11U35 mbug <https://developer.mbed.org/platforms/Y5-LPC11U35-MBUG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
    * - ``nrf51822_y5_mbug``
      - `y5 nRF51822 mbug <https://developer.mbed.org/platforms/Y5-NRF51822-MBUG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
