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

.. image:: ../../_static/debug_probes/jlink.png
  :target: https://www.segger.com/jlink-debug-probes.html?utm_source=platformio&utm_medium=docs

SEGGER J-Links are the most widely used line of debug probes available today.
They've proven their value for more than 10 years with over 400,000 units sold,
including OEM versions and on-board solutions. This popularity stems from the
unparalleled performance, extensive feature set, large number of supported
CPUs, and compatibility with all popular development environments.
`Vendor information... <https://www.segger.com/jlink-debug-probes.html?utm_source=platformio&utm_medium=docs>`__

* `J-Link Supported Devices <https://www.segger.com/downloads/supported_devices_jlink.php?utm_source=platformio&utm_medium=docs>`__

Also, see :ref:`debugging_tool_custom` debugging configuration with
J-Link GDB Server.

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
    debug_tool = jlink

If you would like to use this tool for firmware uploading, please change
upload protocol:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    debug_tool = jlink

    ; SWD interface
    upload_protocol = jlink

    ; JTAG interface
    upload_protocol = jlink-jtag

More options:

* :ref:`projectconf_section_env_debug`
* :ref:`projectconf_section_env_upload`

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

.. begin_platforms

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_atmelsam`
      - Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

    * - :ref:`platform_freescalekinetis`
      - Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

    * - :ref:`platform_infineonxmc`
      - Infineon has designed the XMC microcontrollers for real-time critical applications with an industry-standard core. The XMC microcontrollers can be integrated with the Arduino platform

    * - :ref:`platform_nordicnrf51`
      - The Nordic nRF51 Series is a family of highly flexible, multi-protocol, system-on-chip (SoC) devices for ultra-low power wireless applications. nRF51 Series devices support a range of protocol stacks including Bluetooth Smart (previously called Bluetooth low energy), ANT and proprietary 2.4GHz protocols such as Gazell.

    * - :ref:`platform_nordicnrf52`
      - The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor and are the most capable Bluetooth Smart SoCs on the market.

    * - :ref:`platform_nxplpc`
      - The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

    * - :ref:`platform_siliconlabsefm32`
      - Silicon Labs EFM32 Gecko 32-bit microcontroller (MCU) family includes devices that offer flash memory configurations up to 256 kB, 32 kB of RAM and CPU speeds up to 48 MHz. Based on the powerful ARM Cortex-M core, the Gecko family features innovative low energy techniques, short wake-up time from energy saving modes and a wide selection of peripherals, making it ideal for battery operated applications and other systems requiring high performance and low-energy consumption.

    * - :ref:`platform_ststm32`
      - The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

    * - :ref:`platform_teensy`
      - Teensy is a complete USB-based microcontroller development system, in a very small footprint, capable of implementing many types of projects. All programming is done via the USB port. No special programmer is needed, only a standard USB cable and a PC or Macintosh with a USB port.

    * - :ref:`platform_wiznet7500`
      - The IOP (Internet Offload Processor) W7500 is the one-chip solution which integrates an ARM Cortex-M0, 128KB Flash and hardwired TCP/IP core for various embedded application platform especially requiring Internet of things

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
    * - ``1bitsy_stm32f415rgt``
      - `1Bitsy <http://1bitsy.org?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F415RGT
      - 168MHz
      - 1MB
      - 128KB
    * - ``IBMEthernetKit``
      - `Ethernet IoT Starter Kit <http://developer.mbed.org/platforms/IBMEthernetKit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - MK64FN1M0VLL12
      - 120MHz
      - 1MB
      - 256KB
    * - ``Sinobit``
      - `Sino:Bit <https://github.com/sinobitorg/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
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
    * - ``adafruit_feather_m4``
      - `Adafruit Feather M4 (SAMD51) <https://www.adafruit.com/product/3857?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - ``adafruit_gemma_m0``
      - `Adafruit Gemma M0 <https://www.adafruit.com/product/3501?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_itsybitsy_m0``
      - `Adafruit ItsyBitsy M0 <https://www.adafruit.com/product/3727?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_itsybitsy_m4``
      - `Adafruit ItsyBitsy M4 (SAMD51) <https://www.adafruit.com/product/3800?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - ``adafruit_metro_m0``
      - `Adafruit Metro M0 Expresss <https://www.adafruit.com/product/3505?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``adafruit_metro_m4``
      - `Adafruit Metro M4 (SAMD51) <https://www.adafruit.com/product/3382?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - ``adafruit_pirkey``
      - `Adafruit pIRkey <https://www.adafruit.com/product/3364?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21E18A
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
    * - ``b96b_f446ve``
      - `96Boards B96B-F446VE <https://developer.mbed.org/platforms/ST-B96B-F446VE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F446VET6
      - 168MHz
      - 512KB
      - 128KB
    * - ``blueboard_lpc11u24``
      - `NGX Technologies BlueBoard-LPC11U24 <https://developer.mbed.org/platforms/BlueBoard-LPC11U24/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - ``bluepill_f103c8``
      - `BluePill F103C8 <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``bluey``
      - `Bluey nRF52832 IoT <https://electronut.in/portfolio/bluey/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``bluz_dk``
      - `BluzDK <https://bluz.io/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
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
    * - ``delta_dfbm_nq620``
      - `Delta DFBM-NQ620 <https://developer.mbed.org/platforms/Delta-DFBM-NQ620/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``digix``
      - `Digistump DigiX <http://digistump.com/products/50?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - ``dipcortexm0``
      - `Solder Splash Labs DipCortex M0 <https://developer.mbed.org/platforms/DipCortex-M0/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U24
      - 50MHz
      - 32KB
      - 8KB
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
    * - ``disco_l496ag``
      - `ST 32L496GDISCOVERY <https://www.st.com/en/evaluation-tools/32l496gdiscovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L496AGI6
      - 80MHz
      - 1MB
      - 320KB
    * - ``due``
      - `Arduino Due (Programming Port) <https://www.arduino.cc/en/Main/ArduinoBoardDue?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - ``dueUSB``
      - `Arduino Due (USB Native Port) <https://www.arduino.cc/en/Main/ArduinoBoardDue?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - ``efm32gg_stk3700``
      - `EFM32GG-STK3700 Giant Gecko <https://www.silabs.com/products/development-tools/mcu/32-bit/efm32-giant-gecko-starter-kit?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32GG990F1024
      - 48MHz
      - 1MB
      - 128KB
    * - ``efm32hg_stk3400``
      - `SLSTK3400A USB-enabled Happy Gecko <https://www.silabs.com/products/development-tools/mcu/32-bit/efm32-happy-gecko-starter-kit?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32HG322F64
      - 25MHz
      - 64KB
      - 8KB
    * - ``efm32lg_stk3600``
      - `EFM32LG-STK3600 Leopard Gecko <https://www.silabs.com/products/development-tools/mcu/32-bit/efm32-leopard-gecko-starter-kit?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32LG990F256
      - 48MHz
      - 256KB
      - 32KB
    * - ``efm32pg_stk3401``
      - `SLSTK3401A Pearl Gecko PG1 <https://www.silabs.com/products/development-tools/mcu/32-bit/efm32-pearl-gecko-starter-kit?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32PG1B200F256GM48
      - 40MHz
      - 256KB
      - 32KB
    * - ``efm32wg_stk3800``
      - `EFM32WG-STK3800 Wonder Gecko <https://www.silabs.com/products/development-tools/mcu/32-bit/efm32-wonder-gecko-starter-kit?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32WG990F256
      - 48MHz
      - 256KB
      - 32KB
    * - ``efm32zg_stk3200``
      - `EFM32ZG-STK3200 Zero Gecko <https://www.silabs.com/products/development-tools/mcu/32-bit/efm32-zero-gecko-starter-kit?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFM32ZG222F32
      - 24MHz
      - 32KB
      - 4KB
    * - ``elektor_cocorico``
      - `CoCo-ri-Co! <https://developer.mbed.org/platforms/CoCo-ri-Co/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC812
      - 30MHz
      - 16KB
      - 4KB
    * - ``elmo_f411re``
      - `Espotel LoRa Module <https://developer.mbed.org/platforms/Espotel-ELMO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink` (default)
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``eval_l073z``
      - `ST STM32L073Z-EVAL <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-eval-boards/stm32l073z-eval.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L073VZT6
      - 32MHz
      - 192KB
      - 20KB
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
    * - ``frdm_k82f``
      - `Freescale Kinetis FRDM-K82F <https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/k-seriesperformancem4/k8x-secure/freedom-development-platform-for-kinetis-k82-k81-and-k80-mcus:FRDM-K82F?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - MK82FN256VLL15
      - 150MHz
      - 256KB
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
    * - ``frdm_kl26z``
      - `Freescale Kinetis FRDM-KL26Z <https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/l-seriesultra-low-powerm0-plus/freedom-development-platform-for-kinetis-kl16-and-kl26-mcus-up-to-128-kb-flash:FRDM-KL26Z?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - MKL26Z128VLH4
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
    * - ``frdm_kl82z``
      - `Freescale Kinetis FRDM-KL82Z <https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/l-seriesultra-low-powerm0-plus/freedom-development-board-for-kinetis-ultra-low-power-kl82-mcus:FRDM-KL82Z?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_jlink`
      - MKL82Z128VLK7
      - 96MHz
      - 128KB
      - 96KB
    * - ``frdm_kw24d``
      - `Freescale Kinetis FRDM-KW24D512 <https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/w-serieswireless-conn.m0-plus-m4/freedom-development-platform-for-kinetis-kw2x-mcus:FRDM-KW24D512?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_jlink`
      - MKW24D512
      - 50MHz
      - 512KB
      - 64KB
    * - ``frdm_kw41z``
      - `Freescale Kinetis FRDM-KW41Z <https://os.mbed.com/platforms/FRDM-KW41Z/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - MKW41Z512VHT4
      - 48MHz
      - 512KB
      - 128KB
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
    * - ``genericSTM32F103T8``
      - `STM32F103T8 (20k RAM. 64k Flash) <http://www.st.com/en/microcontrollers/stm32f103t8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103T8T6
      - 72MHz
      - 20KB
      - 64KB
    * - ``genericSTM32F103TB``
      - `STM32F103TB (20k RAM. 128k Flash) <http://www.st.com/en/microcontrollers/stm32f103tb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103TBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``genericSTM32F103VB``
      - `STM32F103VB (20k RAM. 128k Flash) <http://www.st.com/en/microcontrollers/stm32f103vb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103VBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``genericSTM32F103VC``
      - `STM32F103VC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``genericSTM32F103VD``
      - `STM32F103VD (64k RAM. 384k Flash) <http://www.st.com/en/microcontrollers/stm32f103vd.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103VDT6
      - 72MHz
      - 384KB
      - 64KB
    * - ``genericSTM32F103VE``
      - `STM32F103VE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103VET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``genericSTM32F103ZC``
      - `STM32F103ZC (48k RAM. 256k Flash) <http://www.st.com/en/microcontrollers/stm32f103zc.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103ZCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``genericSTM32F103ZD``
      - `STM32F103ZD (64k RAM. 384k Flash) <http://www.st.com/en/microcontrollers/stm32f103zd.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103ZDT6
      - 72MHz
      - 384KB
      - 64KB
    * - ``genericSTM32F103ZE``
      - `STM32F103ZE (64k RAM. 512k Flash) <http://www.st.com/en/microcontrollers/stm32f103ze.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``hackaBLE``
      - `hackaBLE <https://electronut.in/portfolio/hackaBLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``hexiwear``
      - `Hexiwear <https://developer.mbed.org/platforms/Hexiwear/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap`, :ref:`debugging_tool_jlink`
      - MK64FN1M0VDC12
      - 120MHz
      - 1MB
      - 256KB
    * - ``lpc1114fn28``
      - `Switch Science mbed LPC1114FN28 <https://developer.mbed.org/platforms/LPC1114FN28/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC1114FN28
      - 48MHz
      - 32KB
      - 4KB
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
    * - ``lpc11u35``
      - `EA LPC11U35 QuickStart Board <https://developer.mbed.org/platforms/EA-LPC11U35/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
    * - ``lpc11u35_501``
      - `CQ Publishing TG-LPC11U35-501 <https://developer.mbed.org/platforms/TG-LPC11U35-501/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
    * - ``lpc11u35_y5_mbug``
      - `y5 LPC11U35 mbug <https://developer.mbed.org/platforms/Y5-LPC11U35-MBUG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
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
    * - ``lpc1347``
      - `DipCortex M3 <https://developer.mbed.org/platforms/DipCortex-M3/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_jlink`
      - LPC1347
      - 72MHz
      - 64KB
      - 12KB
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
    * - ``lpc4330_m4``
      - `Bambino-210E <https://developer.mbed.org/platforms/Micromint-Bambino-210E/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC4330
      - 204MHz
      - 8MB
      - 264KB
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
    * - ``macchina2``
      - `Macchina M2 <https://www.macchina.cc?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
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
    * - ``maple_ret6``
      - `Maple (RET6) <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103RET6
      - 72MHz
      - 256KB
      - 48KB
    * - ``mbed_connect_odin``
      - `Mbed Connect Cloud <https://os.mbed.com/platforms/mbed-Connect-Cloud/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
    * - ``microduino32_flash``
      - `Microduino Core STM32 to Flash <http://wiki.microduinoinc.com/Microduino-Module_CoreSTM32?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103CBT6
      - 72MHz
      - 105.47KB
      - 16.60KB
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
    * - ``mote_l152rc``
      - `NAMote72 <https://developer.mbed.org/platforms/NAMote-72/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32L152RC
      - 32MHz
      - 256KB
      - 32KB
    * - ``moteino_zero``
      - `Moteino M0 <https://lowpowerlab.com/shop/product/184?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``mtb_ublox_odin_w2``
      - `u-blox ODIN-W2 <https://os.mbed.com/modules/u-blox-odin-w2/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
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
    * - ``mxchip_az3166``
      - `Microsoft Azure IoT Development Kit (MXChip AZ3166) <https://microsoft.github.io/azure-iot-developer-kit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB
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
    * - ``ng_beacon``
      - `ng-beacon <https://github.com/urish/ng-beacon?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``nrf51822_y5_mbug``
      - `y5 nRF51822 mbug <https://developer.mbed.org/platforms/Y5-NRF51822-MBUG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
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
    * - ``nucleo_f439zi``
      - `ST Nucleo F439ZI <https://developer.mbed.org/platforms/ST-Nucleo-F439ZI/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F439ZIT6
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
    * - ``nucleo_f756zg``
      - `ST Nucleo F756ZG <https://www.st.com/en/evaluation-tools/nucleo-f756zg.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F756ZG
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
      - `ST Nucleo L011K4 <https://www.st.com/en/evaluation-tools/nucleo-l011k4.html?utm_source=platformio&utm_medium=docs>`_
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
    * - ``nucleo_l433rc_p``
      - `ST Nucleo L433RC-P <https://www.st.com/en/evaluation-tools/nucleo-l433rc-p.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L433RC
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
    * - ``nucleo_l486rg``
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
    * - ``nucleo_l496zg_p``
      - `ST Nucleo L496ZG-P <https://www.st.com/en/evaluation-tools/nucleo-l496zg-p.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L496ZGT6P
      - 80MHz
      - 1MB
      - 320KB
    * - ``oshchip``
      - `OSHChip <http://oshchip.org/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
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
    * - ``rfduino``
      - `RFduino <http://www.rfduino.com/product/rfd22102-rfduino-dip/index.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 128KB
      - 8KB
    * - ``sainSmartDue``
      - `SainSmart Due (Programming Port) <http://www.sainsmart.com/arduino/control-boards/sainsmart-due-atmel-sam3x8e-arm-cortex-m3-board-black.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - ``sainSmartDueUSB``
      - `SainSmart Due (USB Native Port) <http://www.sainsmart.com/arduino/control-boards/sainsmart-due-atmel-sam3x8e-arm-cortex-m3-board-black.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
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
    * - ``seeedTinyBLE``
      - `Seeed Tiny BLE <http://developer.mbed.org/platforms/Seeed-Tiny-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``silica_sensor_node``
      - `ST Sensor Node <https://www.avnet.com/shop/emea/products/avnet-engineering-services/silicastmsensornodeplus-3074457345633959668/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32L476JG
      - 80MHz
      - 1MB
      - 128KB
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
    * - ``ssci824``
      - `Switch Science mbed LPC824 <https://developer.mbed.org/platforms/Switch-Science-mbed-LPC824/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC824
      - 30MHz
      - 32KB
      - 8KB
    * - ``stct_nrf52_minidev``
      - `Taida Century nRF52 mini board <http://taida-century.com/en/index.asp?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``tb_sense_12``
      - `Thunderboard Sense 2 Sensor-to-Cloud Advanced IoT <https://www.silabs.com/products/development-tools/thunderboard/thunderboard-sense-two-kit?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`
      - EFR32MG12P432F1024
      - 40MHz
      - 1MB
      - 256KB
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
      - 255.99KB
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
    * - ``tian``
      - `Arduino Tian <https://www.arduino.cc/en/Main/ArduinoBoardTian?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``ublox_c030_n211``
      - `u-blox C030-N211 IoT Starter Kit <https://os.mbed.com/platforms/ublox-C030-N211/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_cmsis-dap`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - ``ublox_c030_r410m``
      - `u-blox C030-R410M IoT <https://os.mbed.com/platforms/ublox-C030-R410M/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
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
    * - ``waveshare_ble400``
      - `Waveshare BLE400 <http://www.waveshare.com/wiki/BLE400?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``wio_3g``
      - `Seeed Wio 3G <https://os.mbed.com/platforms/Seeed-Wio-3g/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F439VI
      - 180MHz
      - 2MB
      - 256KB
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
    * - ``xdot_l151cc``
      - `MultiTech xDot <https://developer.mbed.org/platforms/MTS-xDot-L151CC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32L151CCU6
      - 32MHz
      - 256KB
      - 32KB
    * - ``xmc1100_boot_kit``
      - `XMC1100 Boot Kit <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`debugging_tool_jlink` (on-board)
      - XMC1100
      - 32MHz
      - 64KB
      - 64KB
    * - ``xmc1100_h_bridge2go``
      - `XMC1100 H-Bridge 2Go <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`debugging_tool_jlink` (on-board)
      - XMC1100
      - 32MHz
      - 64KB
      - 64KB
    * - ``xmc1100_xmc2go``
      - `XMC1100 XMC2Go <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`debugging_tool_jlink` (on-board)
      - XMC1100
      - 32MHz
      - 64KB
      - 64KB
    * - ``xmc1300_boot_kit``
      - `XMC1300 Boot Kit <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`debugging_tool_jlink` (on-board)
      - XMC1300
      - 32MHz
      - 64KB
      - 64KB
    * - ``xmc1300_sense2gol``
      - `XMC1300 Sense2GoL <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`debugging_tool_jlink` (on-board)
      - XMC1300
      - 32MHz
      - 64KB
      - 122.23KB
    * - ``xmc4200_distance2go``
      - `XMC4200 Distance2Go <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`debugging_tool_jlink` (on-board)
      - XMC4200
      - 80MHz
      - 250KB
      - 256KB
    * - ``xmc4700_relax_kit``
      - `XMC4700 Relax Kit <https://www.infineon.com?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Infineon XMC <platform_infineonxmc>`
      - :ref:`debugging_tool_jlink` (on-board)
      - XMC4700
      - 144MHz
      - 2.00MB
      - 1.95MB
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
