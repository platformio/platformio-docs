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

.. |PIODebug| replace:: **PlatformIO Debugging Solution**

.. _piodebug:

Debugging
=========

**It Simply Works. Easier than ever before!**

.. contents:: Contents
    :local:
    :depth: 1

|PIODebug| offers a unique debugging experience for productive embedded
development. Using our multi-board and multi-architecture programming
experience, we simplified the debugging process in the same way. A zero
debugging configuration with support for the most popular debugging probes
and compatibility between IDEs and OS.

Developers can finally forget about complex UI windows which they need to
pre-configure before a simple “Hello World!” debugging session. No need to
know any aspects about the debugging server or how to configure it. PIO
Unified Debugger does this complex work automatically having a rich
configuration database per each board and debugging probe.

Just select a board, connect debugging probe (if a board does not have
onboard debugging interface), specify it in PlatformIO project configuration
file “platformio.ini”, and a project is ready for 1-Click debugging.


* "1-click" solution, zero configuration
* Support over 300+ embedded boards (see below)
* Multiple architectures and development platforms
* Windows, MacOS, Linux
* Built-in into :ref:`ide_atom` and :ref:`ide_vscode`
* Integration with :ref:`ide_eclipse` and :ref:`ide_sublimetext`

.. hint::
  In our experience, :ref:`ide_vscode` has the best system performance,
  modern interface for |PIODebug|, and users have found it easier to get started.
  Key debugging features of :ref:`ide_vscode`:

  - Local, Global, and Static Variable Explorer
  - Conditional Breakpoints
  - Expressions and Watchpoints
  - Generic Registers
  - Peripheral Registers
  - Memory Viewer
  - Disassembly
  - Multi-thread support
  - A hot restart of an active debugging session

.. image:: ../_static/images/ide/vscode/platformio-ide-vscode.png
  :target: ../ide/vscode.html

Tutorials
---------

* `Arduino In-circuit Debugging with PlatformIO <https://medium.com/@manuel.bl/arduino-in-circuit-debugging-with-platformio-9f699da57ddc>`__
* `Use the PlatformIO Debugger on the ESP32 Using an ESP-prog <https://www.hackster.io/brian-lough/use-the-platformio-debugger-on-the-esp32-using-an-esp-prog-f633b6>`_
* `ThingForward: First steps with PlatformIO’s Unified Debugger <https://www.thingforward.io/techblog/2018-07-04-first-steps-with-platformios-unified-debugger.html>`_
* `[VIDEO] ThingForward - Intro to PIO Unified Debugger using ARM mbed OS and PlatformIO IDE for VSCode <https://www.youtube.com/watch?v=GtlsW3FDN3E>`_
* :ref:`tutorial_espressif32_arduino_debugging_unit_testing`
* :ref:`tutorial_espressif32_espidf_debugging_unit_testing_analysis`
* :ref:`tutorial_nordicnrf52_arduino_debugging_unit_testing`
* :ref:`tutorial_nordicnrf52_zephyr_debugging_unit_testing_analysis`
* :ref:`tutorial_stm32cube_debugging_unit_testing`

Configuration
-------------

|PIODebug| can be configured using :ref:`projectconf`:

.. toctree::
  :maxdepth: 2

  ../projectconf/build_configurations
  ../projectconf/section_env_debug

.. _debugging_tools:

Tools & Debug Probes
--------------------

You can switch between debugging tools using :ref:`projectconf_debug_tool`
option.

.. warning::
  You will need to install debug tool drivers depending on your operating
  system. Please check "Drivers" section for debugging tool below.

.. toctree::
  :maxdepth: 1

  debug-tools/altera-usb-blaster
  debug-tools/atmel-ice
  debug-tools/avr-stub
  debug-tools/blackmagic
  debug-tools/cmsis-dap
  debug-tools/digilent-hs1
  debug-tools/esp-prog
  debug-tools/ftdi
  debug-tools/gd-link
  debug-tools/iot-bus-jtag
  debug-tools/jlink
  debug-tools/minimodule
  debug-tools/mspdebug
  debug-tools/olimex-arm-usb-ocd-h
  debug-tools/olimex-arm-usb-ocd
  debug-tools/olimex-arm-usb-tiny-h
  debug-tools/olimex-jtag-tiny
  debug-tools/qemu
  debug-tools/renode
  debug-tools/rv-link
  debug-tools/simavr
  debug-tools/sipeed-rv-debugger
  debug-tools/stlink
  debug-tools/ti-icdi
  debug-tools/tumpa
  debug-tools/um232h
  debug-tools/verilator
  debug-tools/whisper
  debug-tools/custom

CLI Guide
---------

.. toctree::
  :maxdepth: 3

  pio debug <../core/userguide/cmd_debug>


.. _debugging_platforms:

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_aceinna_imu`
      - Open-source, embedded development platform for Aceinna IMU hardware. Run custom algorithms and navigation code on Aceinna IMU/INS hardware.

    * - :ref:`platform_atmelavr`
      - Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

    * - :ref:`platform_atmelsam`
      - Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

    * - :ref:`platform_chipsalliance`
      - The CHIPS Alliance develops high-quality, open source hardware designs relevant to silicon devices and FPGAs.

    * - :ref:`platform_espressif32`
      - Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

    * - :ref:`platform_freescalekinetis`
      - Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

    * - :ref:`platform_gd32v`
      - The GigaDevice GD32V device is a 32-bit general-purpose microcontroller based on the RISC-V core with an impressive balance of processing power, reduced power consumption and peripheral set.

    * - :ref:`platform_infineonxmc`
      - Infineon has designed the XMC microcontrollers for real-time critical applications with an industry-standard core. The XMC microcontrollers can be integrated with the Arduino platform

    * - :ref:`platform_kendryte210`
      - Kendryte K210 is an AI capable RISCV64 dual core SoC.

    * - :ref:`platform_maxim32`
      - Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

    * - :ref:`platform_nordicnrf51`
      - The Nordic nRF51 Series is a family of highly flexible, multi-protocol, system-on-chip (SoC) devices for ultra-low power wireless applications. nRF51 Series devices support a range of protocol stacks including Bluetooth Smart (previously called Bluetooth low energy), ANT and proprietary 2.4GHz protocols such as Gazell.

    * - :ref:`platform_nordicnrf52`
      - The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor and are the most capable Bluetooth Smart SoCs on the market.

    * - :ref:`platform_nuclei`
      - Find professional RISC-V Processor IP in Nuclei, first professional RISC-V IP company in Mainland China, match all your requirements in AIoT Era.

    * - :ref:`platform_nxpimxrt`
      - The i.MX RT series of crossover processors features the Arm Cortex-M core, real-time functionality and MCU usability at a cost-effective price.

    * - :ref:`platform_nxplpc`
      - The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

    * - :ref:`platform_riscv_gap`
      - GreenWaves GAP8 IoT application processor enables the cost-effective development, deployment and autonomous operation of intelligent sensing devices that capture, analyze, classify and act on the fusion of rich data sources such as images, sounds or vibrations.

    * - :ref:`platform_shakti`
      - Shakti is an open-source initiative by the RISE group at IIT-Madras, which is not only building open source, production grade processors, but also associated components like interconnect fabrics, verification tools, storage controllers, peripheral IPs and SOC tools.

    * - :ref:`platform_sifive`
      - SiFive brings the power of open source and software automation to the semiconductor industry, making it possible to develop new hardware faster and more affordably than ever before. 

    * - :ref:`platform_siliconlabsefm32`
      - Silicon Labs EFM32 Gecko 32-bit microcontroller (MCU) family includes devices that offer flash memory configurations up to 256 kB, 32 kB of RAM and CPU speeds up to 48 MHz. Based on the powerful ARM Cortex-M core, the Gecko family features innovative low energy techniques, short wake-up time from energy saving modes and a wide selection of peripherals, making it ideal for battery operated applications and other systems requiring high performance and low-energy consumption.

    * - :ref:`platform_ststm32`
      - The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

    * - :ref:`platform_ststm8`
      - The STM8 is an 8-bit microcontroller family by STMicroelectronics an extended variant of the ST7 microcontroller architecture. STM8 microcontrollers are particularly low cost for a full-featured 8-bit microcontroller.

    * - :ref:`platform_teensy`
      - Teensy is a complete USB-based microcontroller development system, in a very small footprint, capable of implementing many types of projects. All programming is done via the USB port. No special programmer is needed, only a standard USB cable and a PC or Macintosh with a USB port.

    * - :ref:`platform_timsp430`
      - MSP430 microcontrollers (MCUs) from Texas Instruments (TI) are 16-bit, RISC-based, mixed-signal processors designed for ultra-low power. These MCUs offer the lowest power consumption and the perfect mix of integrated peripherals for thousands of applications.

    * - :ref:`platform_titiva`
      - Texas Instruments TM4C12x MCUs offer the industrys most popular ARM Cortex-M4 core with scalable memory and package options, unparalleled connectivity peripherals, advanced application functions, industry-leading analog integration, and extensive software solutions.

    * - :ref:`platform_wiznet7500`
      - The IOP (Internet Offload Processor) W7500 is the one-chip solution which integrates an ARM Cortex-M0, 128KB Flash and hardwired TCP/IP core for various embedded application platform especially requiring Internet of things

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences

    * - :ref:`framework_cmsis`
      - The ARM Cortex Microcontroller Software Interface Standard (CMSIS) is a vendor-independent hardware abstraction layer for the Cortex-M processor series and specifies debugger interfaces. The CMSIS enables consistent and simple software interfaces to the processor for interface peripherals, real-time operating systems, and middleware. It simplifies software re-use, reducing the learning curve for new microcontroller developers and cutting the time-to-market for devices

    * - :ref:`framework_espidf`
      - ESP-IDF is the official development framework for the ESP32 and ESP32-S Series SoCs.

    * - :ref:`framework_freertos`
      - FreeRTOS is a real-time operating system kernel for embedded devices that has been ported to 40 microcontroller platforms

    * - :ref:`framework_freedom-e-sdk`
      - Open Source Software for Developing on the SiFive Freedom E Platform

    * - :ref:`framework_gd32vf103-sdk`
      - GigaDevice GD32VF103 Firmware Library (SDK) is a firmware function package, including programs, data structures and macro definitions, all the performance features of peripherals of GD32VF103 devices are involved in the package

    * - :ref:`framework_kendryte-freertos-sdk`
      - Kendryte SDK with FreeRTOS support

    * - :ref:`framework_kendryte-standalone-sdk`
      - Kendryte Standalone SDK without OS support

    * - :ref:`framework_mbed`
      - Arm Mbed OS is an open source embedded operating system designed specifically for the 'things' in the Internet of Things. It includes all the features you need to develop a connected product based on an Arm Cortex-M microcontroller, including security, connectivity, an RTOS and drivers for sensors and I/O devices

    * - :ref:`framework_nuclei-sdk`
      - Open Source Software Development Kit for the Nuclei N/NX processors

    * - :ref:`framework_pulp-os`
      - PULP is a silicon-proven Parallel Ultra Low Power platform targeting high energy efficiencies. The platform is organized in clusters of RISC-V cores that share a tightly-coupled data memory

    * - :ref:`framework_stm32cube`
      - STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency

    * - :ref:`framework_shakti-sdk`
      - A software development kit for developing applications on Shakti class of processors

    * - :ref:`framework_simba`
      - Simba is an RTOS and build framework with aims to make embedded programming easy and portable

    * - :ref:`framework_spl`
      - The ST Standard Peripheral Library provides a set of functions for handling the peripherals on the STM32 family of microcontrollers.

    * - :ref:`framework_wd-riscv-sdk`
      - The WD Firmware package contains firmware applications and Processor Support Package (PSP) for various cores, alongside demos which support all features

    * - :ref:`framework_zephyr`
      - The Zephyr Project is a scalable real-time operating system (RTOS) supporting multiple hardware architectures, optimized for resource constrained devices, and built with safety and security in mind

    * - :ref:`framework_libopencm3`
      - The libOpenCM3 framework aims to create a free and open-source firmware library for various ARM Cortex-M0(+)/M3/M4 microcontrollers, including ST STM32, Ti Tiva and Stellaris, NXP LPC, Atmel SAM3, Energy Micro EFM32 and others

Boards
------

.. note::
    For more detailed ``board`` information please scroll tables below by horizontal.

1BitSquared
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_1bitsy_stm32f415rgt`
      - :ref:`platform_ststm32`
      - External
      - STM32F415RGT
      - 168MHz
      - 1MB
      - 128KB

96Boards
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_b96b_argonkey`
      - :ref:`platform_ststm32`
      - External
      - STM32F412CG
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_b96b_f446ve`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F446VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_b96b_aerocore2`
      - :ref:`platform_ststm32`
      - External
      - STM32F427VIT6
      - 168MHz
      - 1.99MB
      - 256KB
    * - :ref:`board_ststm32_b96b_neonkey`
      - :ref:`platform_ststm32`
      - External
      - STM32F411CE
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_nordicnrf52_96b_nitrogen`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

AI Thinker
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32cam`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

AZ-Delivery
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_az-delivery-devkit-v4`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 16MB
      - 520KB

Aceinna
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_aceinna_imu_LowCostRTK`
      - :ref:`platform_aceinna_imu`
      - On-board
      - STM32F469NIH6
      - 180MHz
      - 1MB
      - 384KB
    * - :ref:`board_aceinna_imu_OpenIMU300`
      - :ref:`platform_aceinna_imu`
      - External
      - STM32F405RG
      - 120MHz
      - 1MB
      - 128KB
    * - :ref:`board_aceinna_imu_OpenIMU300ZA`
      - :ref:`platform_aceinna_imu`
      - External
      - STM32F405RG
      - 120MHz
      - 1MB
      - 128KB
    * - :ref:`board_aceinna_imu_OpenIMU330`
      - :ref:`platform_aceinna_imu`
      - External
      - STM32L431CB
      - 80MHz
      - 128KB
      - 64KB
    * - :ref:`board_aceinna_imu_OpenRTK`
      - :ref:`platform_aceinna_imu`
      - External
      - STM32F469IG
      - 180MHz
      - 1MB
      - 384KB
    * - :ref:`board_aceinna_imu_OpenRTK330L`
      - :ref:`platform_aceinna_imu`
      - External
      - STM32F469IG
      - 180MHz
      - 1MB
      - 384KB

Adafruit
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_adafruit_blm_badge`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelavr_bluefruitmicro`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52832`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_adafruit_clue_nrf52840`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_atmelavr_circuitplay_classic`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelsam_adafruit_circuitplayground_m0`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_crickit_m0`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_espressif32_featheresp32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_atmelavr_feather328p`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_feather32u4`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52840_sense`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_atmelsam_adafruit_feather_m0`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_feather_m0_express`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_feather_m4_can`
      - :ref:`platform_atmelsam`
      - External
      - SAME51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_feather_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_ststm32_adafruit_feather_f405`
      - :ref:`platform_ststm32`
      - External
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52840`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_atmelavr_flora8`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_gemma`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelsam_adafruit_gemma_m0`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_grandcentral_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51P20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_hallowing`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_hallowing_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelavr_itsybitsy32u4_3V`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_itsybitsy32u4_5V`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelsam_adafruit_itsybitsy_m0`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_itsybitsy_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51G19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_monster_m4sk`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51G19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_matrix_portal_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelavr_metro`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelsam_adafruit_metro_m0`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_metro_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_metro_m4_airliftlite`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelavr_protrinket3ftdi`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 12MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket3`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 12MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket5ftdi`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_protrinket5`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelsam_adafruit_pygamer_advance_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_pygamer_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_pyportal_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_pyportal_m4_titano`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_qt_py_m0`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_trellis_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelavr_trinket3`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_trinket5`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY85
      - 16MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelsam_adafruit_trinket_m0`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_pirkey`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_pybadge_airlift_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J20A
      - 120MHz
      - 1008KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_pybadge_m4`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_nordicnrf52_adafruit_cplaynrf52840`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_itsybitsy_nrf52840`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_metro_nrf52840`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB

AfroFlight
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_afroflight_f103cb`
      - :ref:`platform_ststm32`
      - External
      - STM32F103CBT6
      - 72MHz
      - 128KB
      - 20KB

Airbot
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_wraith32_v1`
      - :ref:`platform_ststm32`
      - External
      - STM32F051K6
      - 48MHz
      - 32KB
      - 7.75KB

Aiyarafun
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_node32s`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Alorium Technology
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_alorium_hinj`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_alorium_sno`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_alorium_xlr8`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

Anarduino
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_miniwireless`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

Arduboy
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_arduboy`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_arduboy_devkit`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

Arduino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_btatmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_btatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelsam_due`
      - :ref:`platform_atmelsam`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_dueUSB`
      - :ref:`platform_atmelsam`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelavr_diecimilaatmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_diecimilaatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_esplora`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_ethernet`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_fio`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_chiwawa`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_leonardo`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_leonardoeth`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_lilypadatmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 8MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_lilypadatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_LilyPadUSB`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelsam_mzeroUSB`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mzeroproUSB`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mzeropro`
      - :ref:`platform_atmelsam`
      - On-board
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrfox1200`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrgsm1400`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrnb1500`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrwan1300`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrwan1310`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrwifi1010`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkr1000USB`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrzero`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelavr_megaADK`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_megaatmega1280`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1280
      - 16MHz
      - 124KB
      - 8KB
    * - :ref:`board_atmelavr_megaatmega2560`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_micro`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_miniatmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_miniatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB
    * - :ref:`board_atmelavr_atmegangatmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_atmegangatmega8`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA8
      - 16MHz
      - 7KB
      - 1KB
    * - :ref:`board_nordicnrf52_nano33ble`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 960KB
      - 256KB
    * - :ref:`board_atmelavr_nanoatmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_nanoatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_nanoatmega328new`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_pro8MHzatmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 8MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_pro16MHzatmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 16MHz
      - 14KB
      - 1KB
    * - :ref:`board_atmelavr_pro8MHzatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_pro16MHzatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_robotControl`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_robotMotor`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelsam_tian`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelavr_uno`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_yun`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_yunmini`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelsam_zero`
      - :ref:`platform_atmelsam`
      - On-board
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_zeroUSB`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrvidor4000`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_nano_33_iot`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

Armed
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_armed_v1`
      - :ref:`platform_ststm32`
      - External
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB

Armstrap
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_armstrap_eagle1024`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F417VGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_ststm32_armstrap_eagle2048`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F427VIT6
      - 168MHz
      - 1.99MB
      - 256KB
    * - :ref:`board_ststm32_armstrap_eagle512`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB

Atmel
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_samr21_xpro`
      - :ref:`platform_atmelsam`
      - On-board
      - SAMR21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_samd21g18a`
      - :ref:`platform_atmelsam`
      - On-board
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_samc21_xpro`
      - :ref:`platform_atmelsam`
      - On-board
      - SAMC21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_samd21_xpro`
      - :ref:`platform_atmelsam`
      - On-board
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_saml21_xpro_b`
      - :ref:`platform_atmelsam`
      - On-board
      - SAML21J18B
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelavr_attiny2313`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY2313
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny24`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY24
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny25`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY25
      - 8MHz
      - 2KB
      - 128B
    * - :ref:`board_atmelavr_attiny4313`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY4313
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny44`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY44
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny45`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY45
      - 8MHz
      - 4KB
      - 256B
    * - :ref:`board_atmelavr_attiny84`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY84
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_attiny85`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY85
      - 8MHz
      - 8KB
      - 512B
    * - :ref:`board_atmelavr_usbasp`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA8
      - 12MHz
      - 8KB
      - 1KB

Avnet Silica
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_silica_sensor_node`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L476JG
      - 80MHz
      - 1MB
      - 128KB

BBC
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_bbcmicrobit`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf52_bbcmicrobit_v2`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52833
      - 64MHz
      - 512KB
      - 64KB

BQ
~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_zumbt328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 28KB
      - 2KB

BSFrance
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_lora32u4II`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB

BitWizard
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_raspduino`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB

BluzDK
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_bluz_dk`
      - :ref:`platform_nordicnrf51`
      - External
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

CQ Publishing
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc11u35_501`
      - :ref:`platform_nxplpc`
      - External
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB

Calliope
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_calliope_mini`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

Controllino
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_controllino_maxi`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_maxi_automation`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_mega`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_controllino_mini`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

DFRobot
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_firebeetle32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

DOIT
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32doit-devkit-v1`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

DSTIKE
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_d-duino-32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Delta
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_delta_dfbm_nq620`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf51_dfcm_nnn40`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_delta_dfcm_nnn50`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 16KB

Digilent
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_chipsalliance_swervolf_nexys`
      - :ref:`platform_chipsalliance`
      - On-board
      - 
      - 320MHz
      - 16MB
      - 1.16MB

Digistump
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_digispark-tiny`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY85
      - 16MHz
      - 5.87KB
      - 512B
    * - :ref:`board_atmelsam_digix`
      - :ref:`platform_atmelsam`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB

Diymore
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_diymore_f407vgt`
      - :ref:`platform_ststm32`
      - External
      - STM32F407VGT6
      - 168MHz
      - 512KB
      - 128KB

Dongsen Technology
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_pocket_32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

DycodeX
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_espectro32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

ESP32vn
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32vn-iot-uno`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Econode
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_econode_l082cz`
      - :ref:`platform_ststm32`
      - External
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB

Electronut Labs
~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_bluey`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_hackaBLE`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

ElectronutLabs
~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_electronut_blip`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_electronut_papyr`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB

Electrosmith
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_electrosmith_daisy`
      - :ref:`platform_ststm32`
      - External
      - STM32H750IBK6
      - 400MHz
      - 512KB
      - 128KB

Elektor Labs
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_elektor_cocorico`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC812
      - 30MHz
      - 16KB
      - 4KB

Embedded Artists
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc11u35`
      - :ref:`platform_nxplpc`
      - External
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
    * - :ref:`board_nxplpc_lpc4088_dm`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC4088
      - 120MHz
      - 512KB
      - 96KB
    * - :ref:`board_nxplpc_lpc4088`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC4088
      - 120MHz
      - 512KB
      - 96KB

Engduino
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_engduinov3`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB

EnviroDIY
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_mayfly`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB

Espotel
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_elmo_f411re`
      - :ref:`platform_ststm32`
      - External
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB

Espressif
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_pico32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp-wrover-kit`
      - :ref:`platform_espressif32`
      - On-board
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32dev`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

FYSETC
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_fysetc_f6_13`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB
    * - :ref:`board_ststm32_fysetc_s6`
      - :ref:`platform_ststm32`
      - External
      - STM32F446VET6
      - 168MHz
      - 512KB
      - 128KB

Fred
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_frogboard`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Freescale
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_freescalekinetis_IBMEthernetKit`
      - :ref:`platform_freescalekinetis`
      - On-board
      - MK64FN1M0VLL12
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_freescalekinetis_frdm_k20d50m`
      - :ref:`platform_freescalekinetis`
      - On-board
      - MK20DX128VLH5
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_freescalekinetis_frdm_k22f`
      - :ref:`platform_freescalekinetis`
      - On-board
      - MK22FN512VLH12
      - 120MHz
      - 512KB
      - 128KB
    * - :ref:`board_freescalekinetis_frdm_k64f`
      - :ref:`platform_freescalekinetis`
      - On-board
      - MK64FN1M0VLL12
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_freescalekinetis_frdm_k66f`
      - :ref:`platform_freescalekinetis`
      - On-board
      - MK66FN2M0VMD18
      - 180MHz
      - 2MB
      - 256KB
    * - :ref:`board_freescalekinetis_frdm_k82f`
      - :ref:`platform_freescalekinetis`
      - On-board
      - MK82FN256VLL15
      - 150MHz
      - 256KB
      - 256KB
    * - :ref:`board_freescalekinetis_frdm_kl05z`
      - :ref:`platform_freescalekinetis`
      - On-board
      - MKL05Z32VFM4
      - 48MHz
      - 32KB
      - 4KB
    * - :ref:`board_freescalekinetis_frdm_kl25z`
      - :ref:`platform_freescalekinetis`
      - On-board
      - MKL25Z128VLK4
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_freescalekinetis_frdm_kl27z`
      - :ref:`platform_freescalekinetis`
      - On-board
      - MKL27Z64VLH4
      - 48MHz
      - 64KB
      - 16KB
    * - :ref:`board_freescalekinetis_frdm_kl43z`
      - :ref:`platform_freescalekinetis`
      - On-board
      - MKL43Z256VLH4
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_freescalekinetis_frdm_kl46z`
      - :ref:`platform_freescalekinetis`
      - On-board
      - MKL46Z256VLL4
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_freescalekinetis_frdm_kl82z`
      - :ref:`platform_freescalekinetis`
      - External
      - MKL82Z128VLK7
      - 96MHz
      - 128KB
      - 96KB
    * - :ref:`board_freescalekinetis_frdm_kw24d`
      - :ref:`platform_freescalekinetis`
      - External
      - MKW24D512
      - 50MHz
      - 512KB
      - 64KB
    * - :ref:`board_freescalekinetis_frdm_kw41z`
      - :ref:`platform_freescalekinetis`
      - On-board
      - MKW41Z512VHT4
      - 48MHz
      - 512KB
      - 128KB

Generic
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_blackpill_f103c8`
      - :ref:`platform_ststm32`
      - External
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_blackpill_f103c8_128`
      - :ref:`platform_ststm32`
      - External
      - STM32F103C8T6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_bluepill_f103c6`
      - :ref:`platform_ststm32`
      - External
      - STM32F103C6T6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_bluepill_f103c8`
      - :ref:`platform_ststm32`
      - External
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_bluepill_f103c8_128k`
      - :ref:`platform_ststm32`
      - External
      - STM32F103C8T6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_demo_f030f4`
      - :ref:`platform_ststm32`
      - External
      - STM32F030F4P6
      - 48MHz
      - 16KB
      - 4KB
    * - :ref:`board_ststm32_fk407m1`
      - :ref:`platform_ststm32`
      - External
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F103C4`
      - :ref:`platform_ststm32`
      - External
      - STM32F103C4
      - 72MHz
      - 16KB
      - 6KB
    * - :ref:`board_ststm32_genericSTM32F103C6`
      - :ref:`platform_ststm32`
      - External
      - STM32F103C6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_genericSTM32F103C8`
      - :ref:`platform_ststm32`
      - External
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103CB`
      - :ref:`platform_ststm32`
      - External
      - STM32F103CBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103R4`
      - :ref:`platform_ststm32`
      - External
      - STM32F103R4
      - 72MHz
      - 16KB
      - 6KB
    * - :ref:`board_ststm32_genericSTM32F103R6`
      - :ref:`platform_ststm32`
      - External
      - STM32F103R6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_genericSTM32F103R8`
      - :ref:`platform_ststm32`
      - External
      - STM32F103R8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103RB`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103RC`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_genericSTM32F103RD`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RD
      - 72MHz
      - 384KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103RE`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103RF`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RF
      - 72MHz
      - 768KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103RG`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RG
      - 72MHz
      - 1MB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103T4`
      - :ref:`platform_ststm32`
      - External
      - STM32F103T4
      - 72MHz
      - 16KB
      - 6KB
    * - :ref:`board_ststm32_genericSTM32F103T6`
      - :ref:`platform_ststm32`
      - External
      - STM32F103T6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_genericSTM32F103T8`
      - :ref:`platform_ststm32`
      - External
      - STM32F103T8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103TB`
      - :ref:`platform_ststm32`
      - External
      - STM32F103TBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103V8`
      - :ref:`platform_ststm32`
      - External
      - STM32F103V8
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103VB`
      - :ref:`platform_ststm32`
      - External
      - STM32F103VBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103VC`
      - :ref:`platform_ststm32`
      - External
      - STM32F103VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_genericSTM32F103VD`
      - :ref:`platform_ststm32`
      - External
      - STM32F103VDT6
      - 72MHz
      - 384KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103VE`
      - :ref:`platform_ststm32`
      - External
      - STM32F103VET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103VF`
      - :ref:`platform_ststm32`
      - External
      - STM32F103VF
      - 72MHz
      - 768KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103VG`
      - :ref:`platform_ststm32`
      - External
      - STM32F103VG
      - 72MHz
      - 1MB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103ZC`
      - :ref:`platform_ststm32`
      - External
      - STM32F103ZCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_genericSTM32F103ZD`
      - :ref:`platform_ststm32`
      - External
      - STM32F103ZDT6
      - 72MHz
      - 384KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103ZE`
      - :ref:`platform_ststm32`
      - External
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103ZF`
      - :ref:`platform_ststm32`
      - External
      - STM32F103ZF
      - 72MHz
      - 768KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103ZG`
      - :ref:`platform_ststm32`
      - External
      - STM32F103ZG
      - 72MHz
      - 1MB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F303CB`
      - :ref:`platform_ststm32`
      - External
      - STM32F303CBT6
      - 72MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F373RC`
      - :ref:`platform_ststm32`
      - External
      - STM32F373RCT6
      - 72MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F401CB`
      - :ref:`platform_ststm32`
      - External
      - STM32F401CB
      - 84MHz
      - 128KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401CC`
      - :ref:`platform_ststm32`
      - External
      - STM32F401CC
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401CD`
      - :ref:`platform_ststm32`
      - External
      - STM32F401CD
      - 84MHz
      - 384KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401CE`
      - :ref:`platform_ststm32`
      - External
      - STM32F401CE
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401RB`
      - :ref:`platform_ststm32`
      - External
      - STM32F401RB
      - 84MHz
      - 128KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401RC`
      - :ref:`platform_ststm32`
      - External
      - STM32F401RC
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401RD`
      - :ref:`platform_ststm32`
      - External
      - STM32F401RD
      - 84MHz
      - 384KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401RE`
      - :ref:`platform_ststm32`
      - External
      - STM32F401RE
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F405RG`
      - :ref:`platform_ststm32`
      - External
      - STM32F405RG
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F407VET6`
      - :ref:`platform_ststm32`
      - External
      - STM32F407VET6
      - 168MHz
      - 502.23KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F407VGT6`
      - :ref:`platform_ststm32`
      - External
      - STM32F407VGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_ststm32_genericSTM32F410C8`
      - :ref:`platform_ststm32`
      - External
      - STM32F410C8
      - 100MHz
      - 64KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F410CB`
      - :ref:`platform_ststm32`
      - External
      - STM32F410CB
      - 100MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F410R8`
      - :ref:`platform_ststm32`
      - External
      - STM32F410R8
      - 100MHz
      - 64KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F410RB`
      - :ref:`platform_ststm32`
      - External
      - STM32F410RB
      - 100MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F411CC`
      - :ref:`platform_ststm32`
      - External
      - STM32F411CC
      - 100MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F411CE`
      - :ref:`platform_ststm32`
      - External
      - STM32F411CE
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F411RC`
      - :ref:`platform_ststm32`
      - External
      - STM32F411RC
      - 100MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F411RE`
      - :ref:`platform_ststm32`
      - External
      - STM32F411RE
      - 100MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F412CE`
      - :ref:`platform_ststm32`
      - External
      - STM32F412CE
      - 100MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F412CG`
      - :ref:`platform_ststm32`
      - External
      - STM32F412CG
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F412RE`
      - :ref:`platform_ststm32`
      - External
      - STM32F412RE
      - 100MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F412RG`
      - :ref:`platform_ststm32`
      - External
      - STM32F412RG
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F413CG`
      - :ref:`platform_ststm32`
      - External
      - STM32F413CG
      - 100MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F413CH`
      - :ref:`platform_ststm32`
      - External
      - STM32F413CH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F413RG`
      - :ref:`platform_ststm32`
      - External
      - STM32F413RG
      - 100MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F413RH`
      - :ref:`platform_ststm32`
      - External
      - STM32F413RH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F415RG`
      - :ref:`platform_ststm32`
      - External
      - STM32F415RG
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F417VE`
      - :ref:`platform_ststm32`
      - External
      - STM32F417VE
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F417VG`
      - :ref:`platform_ststm32`
      - External
      - STM32F417VG
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F423CH`
      - :ref:`platform_ststm32`
      - External
      - STM32F423CH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F423RH`
      - :ref:`platform_ststm32`
      - External
      - STM32F423RH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F446RC`
      - :ref:`platform_ststm32`
      - External
      - STM32F446RC
      - 180MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F446RE`
      - :ref:`platform_ststm32`
      - External
      - STM32F446RE
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_stm32f4stamp`
      - :ref:`platform_ststm32`
      - External
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 192KB

GigaDevice
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nuclei_gd32vf103v_eval`
      - :ref:`platform_nuclei`
      - External
      - GD32VF103VBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_nuclei_gd32vf103c_longan_nano`
      - :ref:`platform_nuclei`
      - External
      - GD32VF103CBT6
      - 108MHz
      - 128KB
      - 32KB

Gimasi
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_tuinozero96`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

GreenWaves Technologies
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_riscv_gap_gapuino`
      - :ref:`platform_riscv_gap`
      - On-board
      - GAP8
      - 250MHz
      - 64MB
      - 8MB

HY
~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_hy_tinystm103tb`
      - :ref:`platform_ststm32`
      - External
      - STM32F103TBU6
      - 72MHz
      - 128KB
      - 20KB

Heltec Automation
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_heltec_wifi_lora_32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wifi_lora_32_V2`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wireless_stick`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 8MB
      - 320KB

Holyiot
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_holyiot_yj16019`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

Hornbill
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_hornbill32dev`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_hornbill32minima`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Infineon
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_infineonxmc_xmc1100_boot_kit`
      - :ref:`platform_infineonxmc`
      - On-board
      - XMC1100
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1100_h_bridge2go`
      - :ref:`platform_infineonxmc`
      - On-board
      - XMC1100
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1100_xmc2go`
      - :ref:`platform_infineonxmc`
      - On-board
      - XMC1100
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1300_boot_kit`
      - :ref:`platform_infineonxmc`
      - On-board
      - XMC1300
      - 32MHz
      - 64KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1300_sense2gol`
      - :ref:`platform_infineonxmc`
      - On-board
      - XMC1300
      - 32MHz
      - 32KB
      - 16KB
    * - :ref:`board_infineonxmc_xmc1400_boot_kit`
      - :ref:`platform_infineonxmc`
      - On-board
      - XMC1400
      - 48MHz
      - 1.95MB
      - 16KB
    * - :ref:`board_infineonxmc_xmc4200_distance2go`
      - :ref:`platform_infineonxmc`
      - On-board
      - XMC4200
      - 80MHz
      - 256KB
      - 40KB
    * - :ref:`board_infineonxmc_xmc4700_relax_kit`
      - :ref:`platform_infineonxmc`
      - On-board
      - XMC4700
      - 144MHz
      - 2.00MB
      - 1.95MB

IoTaaP
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_iotaap_magnolia`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

JKSoft
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_wallbot_ble`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB

Laird Connectivity
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_laird_bl652_dvk`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_laird_bl654_dvk`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_laird_pinnacle_100_dvk`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB

LeafLabs
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_maple`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RBT6
      - 72MHz
      - 108KB
      - 17KB
    * - :ref:`board_ststm32_maple_ret6`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RET6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_maple_mini_b20`
      - :ref:`platform_ststm32`
      - External
      - STM32F103CBT6
      - 72MHz
      - 120KB
      - 20KB
    * - :ref:`board_ststm32_maple_mini_origin`
      - :ref:`platform_ststm32`
      - External
      - STM32F103CBT6
      - 72MHz
      - 108KB
      - 17KB

LightUp
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_lightup`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB

Linino
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_one`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

LowPowerLab
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_mightyhat`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31KB
      - 2KB
    * - :ref:`board_atmelavr_moteino`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_moteino8mhz`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_moteinomega`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelsam_moteino_zero`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

MH-ET Live
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_mhetesp32devkit`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_mhetesp32minikit`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

MXChip
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_mxchip_az3166`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB

Makerdiary
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_nrf52832_mdk`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52840_mdk`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB

Malyan
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_malyanm200_f070cb`
      - :ref:`platform_ststm32`
      - External
      - STM32F070CBT6
      - 48MHz
      - 120KB
      - 14.81KB
    * - :ref:`board_ststm32_malyanm300_f070cb`
      - :ref:`platform_ststm32`
      - External
      - STM32F070CBT6
      - 48MHz
      - 120KB
      - 14.81KB
    * - :ref:`board_ststm32_malyanm200_f103cb`
      - :ref:`platform_ststm32`
      - External
      - STM32F103CBT6
      - 72MHz
      - 120KB
      - 20KB

Maxim
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_maxim32_max32620fthr`
      - :ref:`platform_maxim32`
      - External
      - MAX32620FTHR
      - 96MHz
      - 2MB
      - 256KB
    * - :ref:`board_maxim32_max32600mbed`
      - :ref:`platform_maxim32`
      - On-board
      - MAX32600
      - 24MHz
      - 256KB
      - 32KB
    * - :ref:`board_maxim32_max32620hsp`
      - :ref:`platform_maxim32`
      - External
      - MAX32620
      - 96MHz
      - 2MB
      - 256KB
    * - :ref:`board_maxim32_maxwsnenv`
      - :ref:`platform_maxim32`
      - External
      - MAX32610
      - 24MHz
      - 256KB
      - 32KB

MediaTek Labs
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_smart7688`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB

Microchip
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_ATmega128`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA128
      - 16MHz
      - 128KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega1280`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1280
      - 16MHz
      - 128KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega1281`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1281
      - 16MHz
      - 128KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega1284`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_ATmega1284P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_ATmega16`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA16
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega164P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA164P
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega168`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega168P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168P
      - 16MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega2560`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 256KB
      - 8KB
    * - :ref:`board_atmelavr_ATmega324A`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA324A
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega324P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA324P
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega324PA`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA324PA
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega328P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_atmelavr_ATmega48`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA48
      - 16MHz
      - 4KB
      - 512B
    * - :ref:`board_atmelavr_ATmega48P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA48P
      - 16MHz
      - 4KB
      - 512B
    * - :ref:`board_atmelavr_ATmega644P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA644P
      - 16MHz
      - 64KB
      - 4KB
    * - :ref:`board_atmelavr_ATmega8`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA8
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega88`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA88
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_ATmega88P`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA88P
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_attiny13`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY13
      - 9MHz
      - 1KB
      - 64B
    * - :ref:`board_atmelavr_attiny13a`
      - :ref:`platform_atmelavr`
      - On-board
      - ATTINY13A
      - 9MHz
      - 1KB
      - 64B

Microduino
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_168pa16m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168P
      - 16MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_168pa8m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA168P
      - 8MHz
      - 15.50KB
      - 1KB
    * - :ref:`board_atmelavr_328p16m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_328p8m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_ststm32_microduino32_flash`
      - :ref:`platform_ststm32`
      - External
      - STM32F103CBT6
      - 72MHz
      - 105.47KB
      - 16.60KB
    * - :ref:`board_atmelavr_32u416m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_1284p16m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_1284p8m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_644pa16m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_644pa8m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA644P
      - 8MHz
      - 63KB
      - 4KB

Micromint
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc4330_m4`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC4330
      - 204MHz
      - 8MB
      - 264KB

Midatronics
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_mkr_sharky`
      - :ref:`platform_ststm32`
      - External
      - STM32WB55CG
      - 64MHz
      - 512KB
      - 192.00KB

MikroElektronika
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_freescalekinetis_hexiwear`
      - :ref:`platform_freescalekinetis`
      - External
      - MK64FN1M0VDC12
      - 120MHz
      - 1MB
      - 256KB

MultiTech
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_mts_dragonfly_f411re`
      - :ref:`platform_ststm32`
      - External
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_mts_mdot_f405rg`
      - :ref:`platform_ststm32`
      - External
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_mts_mdot_f411re`
      - :ref:`platform_ststm32`
      - External
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_xdot_l151cc`
      - :ref:`platform_ststm32`
      - External
      - STM32L151CCU6
      - 32MHz
      - 256KB
      - 32KB

NGX Technologies
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_blueboard_lpc11u24`
      - :ref:`platform_nxplpc`
      - External
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB

NXP
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc11u24_301`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11u68`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC11U68
      - 50MHz
      - 256KB
      - 36KB
    * - :ref:`board_nxplpc_lpc824`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC824
      - 30MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11c24`
      - :ref:`platform_nxplpc`
      - External
      - LPC11C24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11u34_421`
      - :ref:`platform_nxplpc`
      - External
      - LPC11U34
      - 48MHz
      - 40KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11u37_501`
      - :ref:`platform_nxplpc`
      - External
      - LPC11U37
      - 48MHz
      - 128KB
      - 10KB
    * - :ref:`board_nxplpc_lpc812`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC812
      - 30MHz
      - 16KB
      - 4KB
    * - :ref:`board_nxplpc_lpc1549`
      - :ref:`platform_nxplpc`
      - External
      - LPC1549
      - 72MHz
      - 256KB
      - 36KB
    * - :ref:`board_nxplpc_lpc54114`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC54114J256BD64
      - 100MHz
      - 256KB
      - 192KB
    * - :ref:`board_nxplpc_lpc546xx`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC54608ET512
      - 180MHz
      - 512KB
      - 200KB
    * - :ref:`board_nxplpc_lpcxpresso55s16`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC55S16
      - 150MHz
      - 256KB
      - 96KB
    * - :ref:`board_nxplpc_lpcxpresso55s69`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC55S69
      - 150MHz
      - 640KB
      - 320KB
    * - :ref:`board_nxpimxrt_mimxrt1010_evk`
      - :ref:`platform_nxpimxrt`
      - On-board
      - MIMXRT1011DAE5A
      - 500MHz
      - 64KB
      - 128KB
    * - :ref:`board_nxpimxrt_mimxrt1015_evk`
      - :ref:`platform_nxpimxrt`
      - On-board
      - MIMXRT1015DAF5A
      - 500MHz
      - 96KB
      - 128KB
    * - :ref:`board_nxpimxrt_mimxrt1020_evk`
      - :ref:`platform_nxpimxrt`
      - On-board
      - MIMXRT1021DAG5A
      - 500MHz
      - 64MB
      - 256MB
    * - :ref:`board_nxpimxrt_mimxrt1050_evk`
      - :ref:`platform_nxpimxrt`
      - On-board
      - MIMXRT1052DVL6B
      - 600MHz
      - 64MB
      - 512KB
    * - :ref:`board_nxpimxrt_mimxrt1060_evk`
      - :ref:`platform_nxpimxrt`
      - On-board
      - MIMXRT1062DVL6A
      - 600MHz
      - 64MB
      - 1MB
    * - :ref:`board_nxpimxrt_mimxrt1064_evk`
      - :ref:`platform_nxpimxrt`
      - On-board
      - MIMXRT1064DVL6A
      - 600MHz
      - 4MB
      - 1MB
    * - :ref:`board_nxplpc_lpc11u24`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc1768`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB

Netduino
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_netduino2plus`
      - :ref:`platform_ststm32`
      - External
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 192KB

NodeMCU
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_nodemcu-32s`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Nordic
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_nrf51_beacon`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf52_thingy_52`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf51_nrf51_dongle`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_nrf51_mkit`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_nordicnrf51_nrf51_dk`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf52_nrf52_dk`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52840_dk`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_nrf52840_dk_adafruit`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB

Nuclei
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nuclei_gd32vf103v_rvstar`
      - :ref:`platform_nuclei`
      - On-board
      - GD32VF103VBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_nuclei_hbird_eval`
      - :ref:`platform_nuclei`
      - On-board
      - HUMMINGBIRD
      - 5MHz
      - 64KB
      - 64KB

OLIMEX
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32-devkitlipo`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-evb`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-gateway`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

OSHChip
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_oshchip`
      - :ref:`platform_nordicnrf51`
      - External
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

Olimex
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_olimexino`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_olimex_f103`
      - :ref:`platform_ststm32`
      - External
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_olimex_p405`
      - :ref:`platform_ststm32`
      - External
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_ststm32_olimex_e407`
      - :ref:`platform_ststm32`
      - External
      - STM32F407ZGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_olimex_h407`
      - :ref:`platform_ststm32`
      - External
      - STM32F407ZGT6
      - 168MHz
      - 1MB
      - 128KB

OpenEnergyMonitor
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_emonpi`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB

PHYTEC
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_reel_board`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_reel_board_v2`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB

PYBStick
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_pybstick26_duino`
      - :ref:`platform_ststm32`
      - External
      - STM32F072RB
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_pybstick26_pro`
      - :ref:`platform_ststm32`
      - External
      - STM32F412RE
      - 100MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_pybstick26_lite`
      - :ref:`platform_ststm32`
      - External
      - STM32F401CEU6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_pybstick26_std`
      - :ref:`platform_ststm32`
      - External
      - STM32F411CEU6
      - 100MHz
      - 512KB
      - 128KB

PanStamp
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_panStampAVR`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB

Particle
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_particle_argon`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_particle_boron`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_particle_xenon`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB

Piconomix
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_piconomix_px_her0`
      - :ref:`platform_ststm32`
      - External
      - STM32L072RB
      - 32MHz
      - 128KB
      - 20KB

Pololu Corporation
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_a-star32U4`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

PrntrBoard
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_prntr_v2`
      - :ref:`platform_ststm32`
      - External
      - STM32F407RE
      - 168MHz
      - 512KB
      - 192KB

Prusa 3D
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_prusa_mm_control`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_prusa_rambo`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB

Punch Through
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_lightblue-bean`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_lightblue-beanplus`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

Pycom Ltd.
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_lopy`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lopy4`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB

Quirkbot
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_quirkbot`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB

RAK
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_rak811_tracker`
      - :ref:`platform_ststm32`
      - External
      - STM32L151RBT6
      - 32MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_rak811_tracker_32`
      - :ref:`platform_ststm32`
      - External
      - STM32L151RBT6
      - 32MHz
      - 128KB
      - 32KB

RUMBA
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_rumba32_f446ve`
      - :ref:`platform_ststm32`
      - External
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB

Raytac
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_raytac_mdbt50q_rx`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB

RedBearLab
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_redBearLabBLENano`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf52_redbear_blenano2`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_atmelavr_blend`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_nordicnrf52_redbear_blend2`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_atmelavr_blendmicro16`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_blendmicro8`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_nordicnrf51_redBearLab`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

RemRam
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_remram_v1`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F765VIT6
      - 216MHz
      - 2MB
      - 512KB

RepRap
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_reprap_rambo`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 252KB
      - 8KB

ReprapWorld
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_minitronics20`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB

RobotDyn
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_robotdyn_blackpill_f303cc`
      - :ref:`platform_ststm32`
      - External
      - STM32F303CCT6
      - 72MHz
      - 256KB
      - 40KB

RoboticsBrno
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_alksesp32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

RushUp
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_cloud_jam`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F401RET6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_cloud_jam_l4`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L476RGT6
      - 80MHz
      - 1MB
      - 128KB

Ruuvi
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_ruuvitag`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

SEGGER
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_freescalekinetis_segger_ip_switch`
      - :ref:`platform_freescalekinetis`
      - External
      - MK66FN2M0VMD18
      - 180MHz
      - 2MB
      - 256KB

SG-O
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_sg-o_airMon`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

SODAQ
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_sodaq_autonomo`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_explorer`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelavr_sodaq_galora`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_mbili`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sodaq_moja`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sodaq_ndogo`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelsam_sodaq_one`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_sara`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_sff`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelavr_sodaq_tatu`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB

ST
~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_disco_f412zg`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_disco_f723ie`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F723IEK6
      - 216MHz
      - 512KB
      - 192KB
    * - :ref:`board_ststm32_st3dp001_eval`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F401VGT6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_black_f407ve`
      - :ref:`platform_ststm32`
      - External
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_black_f407vg`
      - :ref:`platform_ststm32`
      - External
      - STM32F407VGT6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_black_f407ze`
      - :ref:`platform_ststm32`
      - External
      - STM32F407ZET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_black_f407zg`
      - :ref:`platform_ststm32`
      - External
      - STM32F407ZGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_blackpill_f401cc`
      - :ref:`platform_ststm32`
      - External
      - STM32F401CCU6
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_blackpill_f401ce`
      - :ref:`platform_ststm32`
      - External
      - STM32F401CEU6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_blue_f407ve_mini`
      - :ref:`platform_ststm32`
      - External
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_coreboard_f401rc`
      - :ref:`platform_ststm32`
      - External
      - STM32F401RCT6
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_g071rb`
      - :ref:`platform_ststm32`
      - External
      - STM32G071RBT6
      - 64MHz
      - 128KB
      - 36KB
    * - :ref:`board_ststm32_nucleo_g431kb`
      - :ref:`platform_ststm32`
      - External
      - STM32G431KBT6
      - 170MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_g431rb`
      - :ref:`platform_ststm32`
      - External
      - STM32G431RBT6
      - 170MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_g474re`
      - :ref:`platform_ststm32`
      - External
      - STM32G474RET6
      - 170MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_wb55rg_p`
      - :ref:`platform_ststm32`
      - On-board
      - STM32WB55RG
      - 64MHz
      - 512KB
      - 192.00KB
    * - :ref:`board_ststm32_rhf76_052`
      - :ref:`platform_ststm32`
      - External
      - STM32L051C8T6
      - 32MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_disco_f334c8`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F334C8T6
      - 72MHz
      - 64KB
      - 12KB
    * - :ref:`board_ststm32_disco_f401vc`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F401VCT6
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_disco_f411ve`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F411VET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_disco_f413zh`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F413ZHT6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_disco_f429zi`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F429ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - :ref:`board_ststm32_disco_f469ni`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F469NIH6
      - 180MHz
      - 1MB
      - 384KB
    * - :ref:`board_ststm32_disco_f746ng`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F746NGH6
      - 216MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_disco_f769ni`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F769NIH6
      - 216MHz
      - 1MB
      - 512KB
    * - :ref:`board_ststm32_disco_l053c8`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L053C8T6
      - 32MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_disco_l100rc`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L100RCT6
      - 32MHz
      - 256KB
      - 16KB
    * - :ref:`board_ststm32_disco_l476vg`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L476VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_disco_l496ag`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L496AGI6
      - 80MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_disco_l475vg_iot01a`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L475VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_disco_l072cz_lrwan1`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L072CZ
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_disco_f072rb`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F072RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f030r8`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_nucleo_f031k6`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F031K6T6
      - 48MHz
      - 32KB
      - 4KB
    * - :ref:`board_ststm32_nucleo_f042k6`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F042K6T6
      - 48MHz
      - 32KB
      - 6KB
    * - :ref:`board_ststm32_nucleo_f070rb`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F070RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f072rb`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F072RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f091rc`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F091RCT6
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_f103rb`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_nucleo_f207zg`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F207ZGT6
      - 120MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f302r8`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F302R8T6
      - 72MHz
      - 64KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f303k8`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F303K8T6
      - 72MHz
      - 64KB
      - 12KB
    * - :ref:`board_ststm32_nucleo_f303re`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F303RET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_f303ze`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F303ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_f334r8`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F334R8T6
      - 72MHz
      - 64KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f401re`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F401RET6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_nucleo_f410rb`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F410RBT6
      - 100MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_f411re`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f412zg`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_nucleo_f413zh`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F413ZHT6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f429zi`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F429ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - :ref:`board_ststm32_nucleo_f439zi`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F439ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - :ref:`board_ststm32_nucleo_f446re`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f446ze`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F446ZET6
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f722ze`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F722ZET6
      - 216MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_nucleo_f746zg`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F746ZGT6
      - 216MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_nucleo_f756zg`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F756ZG
      - 216MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_nucleo_f767zi`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F767ZIT6
      - 216MHz
      - 2MB
      - 512KB
    * - :ref:`board_ststm32_nucleo_h743zi`
      - :ref:`platform_ststm32`
      - On-board
      - STM32H743ZIT6
      - 400MHz
      - 2MB
      - 512KB
    * - :ref:`board_ststm32_nucleo_h745zi_q`
      - :ref:`platform_ststm32`
      - On-board
      - STM32H745ZIT6
      - 480MHz
      - 1MB
      - 512KB
    * - :ref:`board_ststm32_nucleo_l011k4`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L011K4T6
      - 32MHz
      - 16KB
      - 2KB
    * - :ref:`board_ststm32_nucleo_l031k6`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L031K6T6
      - 32MHz
      - 32KB
      - 8KB
    * - :ref:`board_ststm32_nucleo_l053r8`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L053R8T6
      - 32MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_nucleo_l073rz`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L073RZ
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_nucleo_l152re`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L152RET6
      - 32MHz
      - 512KB
      - 80KB
    * - :ref:`board_ststm32_nucleo_l412kb`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L412KBU6
      - 80MHz
      - 128KB
      - 40KB
    * - :ref:`board_ststm32_nucleo_l432kc`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L432KCU6
      - 80MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_l433rc_p`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L433RC
      - 80MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_l452re`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L452RET6
      - 80MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_l476rg`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L476RGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_l486rg`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L486RGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_l496zg`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L496ZGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_l496zg_p`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L496ZGT6P
      - 80MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_nucleo_l4r5zi`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L4R5ZIT6
      - 120MHz
      - 2MB
      - 640KB
    * - :ref:`board_ststm32_disco_f030r8`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_disco_f051r8`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F051R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_disco_f303vc`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F303VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_disco_f407vg`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F407VGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_disco_g031j6`
      - :ref:`platform_ststm32`
      - External
      - STM32G031J6
      - 64MHz
      - 128KB
      - 8KB
    * - :ref:`board_ststm32_eval_l073z`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L073VZT6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_disco_l152rb`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L152RBT6
      - 32MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_disco_f100rb`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F100RBT6
      - 24MHz
      - 128KB
      - 8KB
    * - :ref:`board_ststm8_stm8sdisco`
      - :ref:`platform_ststm8`
      - On-board
      - STM8S105C6T6
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_ststm32_steval_fcu001v1`
      - :ref:`platform_ststm32`
      - External
      - STM32F401CCU6
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_eval_f107vc`
      - :ref:`platform_ststm32`
      - External
      - STM32F107VCT6
      - 72MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_eval_f373vc`
      - :ref:`platform_ststm32`
      - External
      - STM32F373VCT6
      - 72MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_eval_f072vb`
      - :ref:`platform_ststm32`
      - External
      - STM32F072VBT6
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_disco_f750n8`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F750N8H6
      - 216MHz
      - 64KB
      - 340KB
    * - :ref:`board_ststm32_disco_h747xi`
      - :ref:`platform_ststm32`
      - On-board
      - STM32H747XIH6
      - 400MHz
      - 2MB
      - 512KB
    * - :ref:`board_ststm32_steval_mksboxv1`
      - :ref:`platform_ststm32`
      - External
      - STM32L4R9ZI
      - 120MHz
      - 2MB
      - 640KB

SainSmart
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_sainSmartDue`
      - :ref:`platform_atmelsam`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_sainSmartDueUSB`
      - :ref:`platform_atmelsam`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB

Sanguino
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_sanguino_atmega1284p`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sanguino_atmega1284_8m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 8MHz
      - 127KB
      - 16KB
    * - :ref:`board_atmelavr_sanguino_atmega644`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA644
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644_8m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA644
      - 8MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644p`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA644P
      - 16MHz
      - 63KB
      - 4KB
    * - :ref:`board_atmelavr_sanguino_atmega644p_8m`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA644P
      - 8MHz
      - 63KB
      - 4KB

Seeed
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_seeed_femto`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeeduino_lorawan`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeed_wio_lite_mg126`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeed_wio_terminal`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51P19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_seeed_xiao`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeed_zero`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

SeeedStudio
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_seeedArchBLE`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_nordicnrf51_seeedArchLink`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_ststm32_seeedArchMax`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB
    * - :ref:`board_nxplpc_seeedArchPro`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf51_seeedTinyBLE`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_ststm32_wio_3g`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F439VI
      - 180MHz
      - 2MB
      - 256KB
    * - :ref:`board_atmelavr_seeeduino`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_gd32v_wio_lite_risc-v`
      - :ref:`platform_gd32v`
      - External
      - GD32VF103CBT6
      - 108MHz
      - 128KB
      - 32KB

Semtech
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_mote_l152rc`
      - :ref:`platform_ststm32`
      - External
      - STM32L152RC
      - 32MHz
      - 256KB
      - 32KB

SiFive
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_sifive_hifive-unleashed`
      - :ref:`platform_sifive`
      - On-board
      - FU540
      - 1500MHz
      - 32MB
      - 8GB
    * - :ref:`board_sifive_hifive1`
      - :ref:`platform_sifive`
      - On-board
      - FE310
      - 320MHz
      - 16MB
      - 16KB
    * - :ref:`board_sifive_hifive1-revb`
      - :ref:`platform_sifive`
      - On-board
      - FE310
      - 320MHz
      - 16MB
      - 16KB

Sigma Delta Technologies
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_sdt52832b`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

Silicognition
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_wesp32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Silicon Labs
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_siliconlabsefm32_efm32gg_stk3700`
      - :ref:`platform_siliconlabsefm32`
      - On-board
      - EFM32GG990F1024
      - 48MHz
      - 1MB
      - 128KB
    * - :ref:`board_siliconlabsefm32_efm32lg_stk3600`
      - :ref:`platform_siliconlabsefm32`
      - On-board
      - EFM32LG990F256
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_siliconlabsefm32_efm32wg_stk3800`
      - :ref:`platform_siliconlabsefm32`
      - On-board
      - EFM32WG990F256
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_siliconlabsefm32_efm32zg_stk3200`
      - :ref:`platform_siliconlabsefm32`
      - On-board
      - EFM32ZG222F32
      - 24MHz
      - 32KB
      - 4KB
    * - :ref:`board_siliconlabsefm32_efm32hg_stk3400`
      - :ref:`platform_siliconlabsefm32`
      - On-board
      - EFM32HG322F64
      - 25MHz
      - 64KB
      - 8KB
    * - :ref:`board_siliconlabsefm32_efm32pg_stk3401`
      - :ref:`platform_siliconlabsefm32`
      - On-board
      - EFM32PG1B200F256GM48
      - 40MHz
      - 256KB
      - 32KB
    * - :ref:`board_siliconlabsefm32_efm32gg11_stk3701`
      - :ref:`platform_siliconlabsefm32`
      - On-board
      - EFM32GG11B820F2048GL192
      - 48MHz
      - 2MB
      - 512KB
    * - :ref:`board_siliconlabsefm32_tb_sense_12`
      - :ref:`platform_siliconlabsefm32`
      - On-board
      - EFR32MG12P432F1024
      - 40MHz
      - 1MB
      - 256KB

Sipeed
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_gd32v_gd32vf103v-eval`
      - :ref:`platform_gd32v`
      - External
      - GD32VF103VBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_gd32v_sipeed-longan-nano`
      - :ref:`platform_gd32v`
      - External
      - GD32VF103CBT6
      - 108MHz
      - 128KB
      - 32KB
    * - :ref:`board_gd32v_sipeed-longan-nano-lite`
      - :ref:`platform_gd32v`
      - External
      - GD32VF103C8T6
      - 108MHz
      - 64KB
      - 20KB
    * - :ref:`board_kendryte210_sipeed-maix-bit`
      - :ref:`platform_kendryte210`
      - External
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-maix-bit-mic`
      - :ref:`platform_kendryte210`
      - External
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-maix-go`
      - :ref:`platform_kendryte210`
      - External
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-maix-one-dock`
      - :ref:`platform_kendryte210`
      - External
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-maixduino`
      - :ref:`platform_kendryte210`
      - External
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-MF1`
      - :ref:`platform_kendryte210`
      - External
      - K210
      - 400MHz
      - 16MB
      - 6MB

Solder Splash Labs
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc1347`
      - :ref:`platform_nxplpc`
      - External
      - LPC1347
      - 72MHz
      - 64KB
      - 12KB
    * - :ref:`board_nxplpc_dipcortexm0`
      - :ref:`platform_nxplpc`
      - External
      - LPC11U24
      - 50MHz
      - 32KB
      - 8KB

SparkFun
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_sparkfun_samd21_9dof`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelavr_sparkfun_satmega128rfa1`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA128RFA1
      - 16MHz
      - 16KB
      - 124KB
    * - :ref:`board_atmelavr_sparkfun_digitalsandbox`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_fiov3`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_espressif32_sparkfun_lora_gateway_1-channel`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_atmelavr_sparkfun_makeymakey`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_megapro8MHz`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 8MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_sparkfun_megapro16MHz`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_sparkfun_megamini`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 8MHz
      - 252KB
      - 8KB
    * - :ref:`board_atmelavr_uview`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_sparkfun_promicro8`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_promicro16`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelavr_sparkfun_qduinomini`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 8MHz
      - 28KB
      - 2.50KB
    * - :ref:`board_atmelsam_sparkfun_qwiic_micro_samd21e`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_sifive_sparkfun_redboard_v`
      - :ref:`platform_sifive`
      - On-board
      - FE310
      - 320MHz
      - 16MB
      - 16KB
    * - :ref:`board_sifive_sparkfun_thing_plus_v`
      - :ref:`platform_sifive`
      - On-board
      - FE310
      - 320MHz
      - 16MB
      - 16KB
    * - :ref:`board_atmelavr_sparkfun_redboard`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelsam_sparkfun_redboard_turbo`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd21_dev_usb`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd21_mini_usb`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd21_proRF`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd51_thing_plus`
      - :ref:`platform_atmelsam`
      - External
      - SAMD51J20A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelavr_sparkfun_serial7seg`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 31.50KB
      - 2KB

SparkFun Electronics
~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32thing`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

SpellFoundry
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_sleepypi`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB

Switch Science
~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_hrm1017`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nxplpc_lpc1114fn28`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC1114FN28
      - 48MHz
      - 32KB
      - 4KB
    * - :ref:`board_nxplpc_ssci824`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC824
      - 30MHz
      - 32KB
      - 8KB
    * - :ref:`board_nordicnrf51_ty51822r3`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

TI
~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_timsp430_lpmsp430fr5739`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430FR5739
      - 16MHz
      - 15.37KB
      - 1KB
    * - :ref:`board_titiva_lplm4f120h5qr`
      - :ref:`platform_titiva`
      - On-board
      - LPLM4F120H5QR
      - 80MHz
      - 256KB
      - 32KB
    * - :ref:`board_titiva_lptm4c1230c3pm`
      - :ref:`platform_titiva`
      - On-board
      - LPTM4C1230C3PM
      - 80MHz
      - 256KB
      - 32KB
    * - :ref:`board_titiva_lptm4c1294ncpdt`
      - :ref:`platform_titiva`
      - On-board
      - LPTM4C1294NCPDT
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_timsp430_lpmsp430f5529`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430F5529
      - 25MHz
      - 47KB
      - 8KB
    * - :ref:`board_timsp430_lpmsp430fr2311`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430FR2311
      - 16MHz
      - 3.75KB
      - 1KB
    * - :ref:`board_timsp430_lpmsp430fr2433`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430FR2433
      - 8MHz
      - 15KB
      - 4KB
    * - :ref:`board_timsp430_lpmsp430fr4133`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430FR4133
      - 8MHz
      - 15KB
      - 2KB
    * - :ref:`board_timsp430_lpmsp430fr5969`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430FR5969
      - 8MHz
      - 47KB
      - 2KB
    * - :ref:`board_timsp430_lpmsp430fr5994`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430FR5994
      - 16MHz
      - 256KB
      - 4KB
    * - :ref:`board_timsp430_lpmsp430fr6989`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430FR6989
      - 8MHz
      - 47KB
      - 2KB
    * - :ref:`board_timsp430_lpmsp430g2231`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430G2231
      - 1MHz
      - 2KB
      - 256B
    * - :ref:`board_timsp430_lpmsp430g2452`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430G2452
      - 16MHz
      - 8KB
      - 256B
    * - :ref:`board_timsp430_lpmsp430g2553`
      - :ref:`platform_timsp430`
      - On-board
      - MSP430G2553
      - 16MHz
      - 16KB
      - 512B

TTGO
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_ttgo-lora32-v1`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-lora32-v2`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-t-beam`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB
    * - :ref:`board_espressif32_ttgo-t1`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Taida Century
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_stct_nrf52_minidev`
      - :ref:`platform_nordicnrf52`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

TauLabs
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_sparky_v1`
      - :ref:`platform_ststm32`
      - External
      - STM32F303CCT6
      - 72MHz
      - 256KB
      - 40KB

Teensy
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_teensy_teensy31`
      - :ref:`platform_teensy`
      - External
      - MK20DX256
      - 72MHz
      - 256KB
      - 64KB
    * - :ref:`board_teensy_teensy35`
      - :ref:`platform_teensy`
      - External
      - MK64FX512
      - 120MHz
      - 512KB
      - 255.99KB
    * - :ref:`board_teensy_teensy36`
      - :ref:`platform_teensy`
      - External
      - MK66FX1M0
      - 180MHz
      - 1MB
      - 256KB
    * - :ref:`board_teensy_teensy40`
      - :ref:`platform_teensy`
      - External
      - IMXRT1062
      - 600MHz
      - 1.94MB
      - 512KB
    * - :ref:`board_teensy_teensy41`
      - :ref:`platform_teensy`
      - External
      - IMXRT1062
      - 600MHz
      - 7.75MB
      - 512KB
    * - :ref:`board_teensy_teensylc`
      - :ref:`platform_teensy`
      - External
      - MKL26Z64
      - 48MHz
      - 62KB
      - 8KB

ThaiEasyElec
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_espino32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

The Things Network
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_the_things_uno`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

ThunderPack
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_thunder_pack`
      - :ref:`platform_ststm32`
      - External
      - STM32L072KZ
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_thunder_pack_f411`
      - :ref:`platform_ststm32`
      - External
      - STM32F411CEU6
      - 100MHz
      - 512KB
      - 128KB

Till Harbaum
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_ftduino`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA32U4
      - 16MHz
      - 28KB
      - 2.50KB

TinyCircuits
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_tinyduino`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_tinylily`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 8MHz
      - 30KB
      - 2KB

Tlera Corporation
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_cicada_l082cz`
      - :ref:`platform_ststm32`
      - External
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_cricket_l082cz`
      - :ref:`platform_ststm32`
      - External
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_gnat_l082cz`
      - :ref:`platform_ststm32`
      - External
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_grasshopper_l082cz`
      - :ref:`platform_ststm32`
      - External
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB

Unknown
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_fm-devkit`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

VAE
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_vake_v1`
      - :ref:`platform_ststm32`
      - External
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB

VCCGND
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_vccgnd_f103zet6`
      - :ref:`platform_ststm32`
      - External
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB

VNG
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_vbluno51`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 128KB
      - 32KB
    * - :ref:`board_nordicnrf52_vbluno52`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

VintLabs
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_vintlabs-devkit-v1`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

WEMOS
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_lolin_d32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_d32_pro`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wemos_d1_mini32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wemosbat`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

WIZNet
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_wiznet7500_wizwiki_w7500`
      - :ref:`platform_wiznet7500`
      - On-board
      - WIZNET7500
      - 48MHz
      - 128KB
      - 48KB
    * - :ref:`board_wiznet7500_wizwiki_w7500eco`
      - :ref:`platform_wiznet7500`
      - On-board
      - WIZNET7500ECO
      - 48MHz
      - 128KB
      - 48KB
    * - :ref:`board_wiznet7500_wizwiki_w7500p`
      - :ref:`platform_wiznet7500`
      - On-board
      - WIZNET7500P
      - 48MHz
      - 128KB
      - 48KB

Waveshare
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_waveshare_ble400`
      - :ref:`platform_nordicnrf51`
      - External
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_waveshare_open103z`
      - :ref:`platform_ststm32`
      - External
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB

WeAct
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_blackpill_f411ce`
      - :ref:`platform_ststm32`
      - External
      - STM32F411CEU6
      - 100MHz
      - 512KB
      - 128KB

Wicked Device
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_wildfirev2`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 16MHz
      - 120.00KB
      - 16KB
    * - :ref:`board_atmelavr_wildfirev3`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 16MHz
      - 127KB
      - 16KB

Wisen
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_whispernode`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

Xilinx
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_shakti_artix7_35t`
      - :ref:`platform_shakti`
      - On-board
      - E-CLASS
      - 50MHz
      - 0B
      - 128KB
    * - :ref:`board_shakti_artix7_100t`
      - :ref:`platform_shakti`
      - On-board
      - C-CLASS
      - 50MHz
      - 0B
      - 128MB
    * - :ref:`board_sifive_e310-arty`
      - :ref:`platform_sifive`
      - On-board
      - FE310
      - 450MHz
      - 16MB
      - 256MB
    * - :ref:`board_shakti_parashu`
      - :ref:`platform_shakti`
      - On-board
      - E-CLASS
      - 50MHz
      - 0B
      - 128KB
    * - :ref:`board_shakti_pinaka`
      - :ref:`platform_shakti`
      - On-board
      - E-CLASS
      - 50MHz
      - 0B
      - 128KB
    * - :ref:`board_shakti_vajra`
      - :ref:`platform_shakti`
      - On-board
      - C-CLASS
      - 50MHz
      - 0B
      - 128MB

XinaBox
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_xinabox_cw02`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

decaWave
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_dwm1001_dev`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

meteca
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_briki_abc_esp32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 3.25MB
      - 320KB
    * - :ref:`board_atmelsam_briki_abc_samd21`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_espressif32_briki_mbc-wb_esp32`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 3.25MB
      - 320KB
    * - :ref:`board_atmelsam_briki_mbcwb_samd21`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

ng-beacon
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_ng_beacon`
      - :ref:`platform_nordicnrf51`
      - External
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB

nicai-systems
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_bob3`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA88
      - 8MHz
      - 8KB
      - 1KB
    * - :ref:`board_atmelavr_nibo2`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA128
      - 16MHz
      - 128KB
      - 4KB
    * - :ref:`board_atmelavr_niboburger`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA16
      - 15MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_niboburger_1284`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 20MHz
      - 128KB
      - 16KB
    * - :ref:`board_atmelavr_nibobee`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA16
      - 15MHz
      - 16KB
      - 1KB
    * - :ref:`board_atmelavr_nibobee_1284`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA1284P
      - 20MHz
      - 128KB
      - 16KB

oddWires
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_iotbusio`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_iotbusproteus`
      - :ref:`platform_espressif32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

rhomb.io
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_rhombio_l476dmw1k`
      - :ref:`platform_ststm32`
      - On-board
      - STM32L476VGT6
      - 80MHz
      - 1MB
      - 128KB

sakura.io
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_sakuraio_evb_01`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F411RET6
      - 100MHz
      - 1MB
      - 128KB

sino:bit
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_Sinobit`
      - :ref:`platform_nordicnrf51`
      - External
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

u-blox
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_mbed_connect_odin`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
    * - :ref:`board_nxplpc_ubloxc027`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_ublox_c030_n211`
      - :ref:`platform_ststm32`
      - External
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_ublox_c030_r410m`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_ublox_c030_u201`
      - :ref:`platform_ststm32`
      - External
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_ublox_evk_nina_b1`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_ublox_evk_odin_w2`
      - :ref:`platform_ststm32`
      - External
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
    * - :ref:`board_ststm32_mtb_ublox_odin_w2`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB

ubIQio
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_ardhat`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

y5 design
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc11u35_y5_mbug`
      - :ref:`platform_nxplpc`
      - External
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
    * - :ref:`board_nordicnrf51_nrf51822_y5_mbug`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
