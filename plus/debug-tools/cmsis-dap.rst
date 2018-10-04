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

.. image:: ../../_static/debug_probes/cmsis-dap.png
  :target: https://developer.mbed.org/handbook/CMSIS-DAP?utm_source=platformio&utm_medium=docs

CMSIS-DAP is generally implemented as an on-board interface chip, providing
direct USB connection from a development board to a debugger running on a host
computer on one side, and over JTAG (Joint Test Action Group) or SWD
(Serial Wire Debug) to the target device to access the Coresight DAP on the other.
`Vendor information... <https://developer.mbed.org/handbook/CMSIS-DAP?utm_source=platformio&utm_medium=docs>`__

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
    debug_tool = cmsis-dap

If you would like to use this tool for firmware uploading, please change
upload protocol:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    debug_tool = cmsis-dap
    upload_protocol = cmsis-dap

More options:

* :ref:`projectconf_section_env_debug`
* :ref:`projectconf_section_env_upload`

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

    * - :ref:`platform_maxim32`
      - Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

    * - :ref:`platform_nordicnrf51`
      - The Nordic nRF51 Series is a family of highly flexible, multi-protocol, system-on-chip (SoC) devices for ultra-low power wireless applications. nRF51 Series devices support a range of protocol stacks including Bluetooth Smart (previously called Bluetooth low energy), ANT and proprietary 2.4GHz protocols such as Gazell.

    * - :ref:`platform_nordicnrf52`
      - The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor and are the most capable Bluetooth Smart SoCs on the market.

    * - :ref:`platform_nxplpc`
      - The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

    * - :ref:`platform_ststm32`
      - The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

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
    * - :ref:`board_atmelsam_mzeropro`
      - :ref:`platform_atmelsam`
      - On-board
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_zero`
      - :ref:`platform_atmelsam`
      - On-board
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
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
    * - :ref:`board_nordicnrf51_bbcmicrobit`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf51_bbcmicrobit_b`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nxplpc_lpc4330_m4`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC4330
      - 204MHz
      - 8MB
      - 264KB
    * - :ref:`board_nxplpc_elektor_cocorico`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC812
      - 30MHz
      - 16KB
      - 4KB
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
    * - :ref:`board_freescalekinetis_frdm_kl26z`
      - :ref:`platform_freescalekinetis`
      - On-board
      - MKL26Z128VLH4
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
    * - :ref:`board_freescalekinetis_frdm_kw41z`
      - :ref:`platform_freescalekinetis`
      - On-board
      - MKW41Z512VHT4
      - 48MHz
      - 512KB
      - 128KB
    * - :ref:`board_freescalekinetis_hexiwear`
      - :ref:`platform_freescalekinetis`
      - External
      - MK64FN1M0VDC12
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf51_wallbot_ble`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB
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
    * - :ref:`board_maxim32_max32600mbed`
      - :ref:`platform_maxim32`
      - On-board
      - MAX32600
      - 24MHz
      - 256KB
      - 32KB
    * - :ref:`board_maxim32_maxwsnenv`
      - :ref:`platform_maxim32`
      - External
      - MAX32610
      - 24MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_mbed_connect_odin`
      - :ref:`platform_ststm32`
      - On-board
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
    * - :ref:`board_atmelsam_moteino_zero`
      - :ref:`platform_atmelsam`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_nxplpc_lpc812`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC812
      - 30MHz
      - 16KB
      - 4KB
    * - :ref:`board_nxplpc_lpc54114`
      - :ref:`platform_nxplpc`
      - On-board
      - LPC54114J256BD64
      - 100MHz
      - 256KB
      - 192KB
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
    * - :ref:`board_nordicnrf51_nrf51_dk`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
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
    * - :ref:`board_nordicnrf52_redbear_blend2`
      - :ref:`platform_nordicnrf52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf51_redBearLab`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
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
    * - :ref:`board_nordicnrf51_vbluno51`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 128KB
      - 32KB
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
    * - :ref:`board_ststm32_ublox_c030_u201`
      - :ref:`platform_ststm32`
      - External
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf51_nrf51822_y5_mbug`
      - :ref:`platform_nordicnrf51`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
