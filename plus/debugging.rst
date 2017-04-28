..  Copyright 2014-present PlatformIO <contact@platformio.org>
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

.. _debugging:

PIO Unified Debugger
====================

**It Just Works. Easier than ever before!**

.. versionadded:: 3.4 (`PlatformIO Plus <https://pioplus.com>`__)

.. note::

  `Demo, discussions, request a support for new hardware. <https://community.platformio.org/t/pio-unified-debugger/1704>`_


* 100+ boards
* Multiple architectures and development platforms
* Zero Configuration
* Compatibility with the popular IDEs: Eclipse, Atom, VSCode, Sublime Text, etc
* Windows, MacOS, Linux (+ARMv6-8)

You should have :ref:`cmd_account` to work with |PIODebug|.
A registration is **FREE**.

.. tip::
  `QUESTIONS? Chat with us! <https://pioplus.com>`_
  (chat button is located in the bottom right corner)

.. image:: ../_static/pioplus-debugger-demo.png

.. contents::

Configuration
-------------

|PIODebug| can be configured from :ref:`projectconf`

* :ref:`projectconf_debug_tool`
* :ref:`projectconf_debug_port`
* :ref:`projectconf_debug_init_cmds`
* :ref:`projectconf_debug_extra_cmds`

.. _debugging_platforms:

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

    * - :ref:`platform_nordicnrf51`
      - The Nordic nRF51 Series is a family of highly flexible, multi-protocol, system-on-chip (SoC) devices for ultra-low power wireless applications. nRF51 Series devices support a range of protocol stacks including Bluetooth Smart (previously called Bluetooth low energy), ANT and proprietary 2.4GHz protocols such as Gazell.

    * - :ref:`platform_nxplpc`
      - The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

    * - :ref:`platform_siliconlabsefm32`
      - Silicon Labs EFM32 Gecko 32-bit microcontroller (MCU) family includes devices that offer flash memory configurations up to 256 kB, 32 kB of RAM and CPU speeds up to 48 MHz. Based on the powerful ARM Cortex-M core, the Gecko family features innovative low energy techniques, short wake-up time from energy saving modes and a wide selection of peripherals, making it ideal for battery operated applications and other systems requiring high performance and low-energy consumption.

    * - :ref:`platform_ststm32`
      - The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

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

    * - :ref:`framework_libopencm3`
      - The libOpenCM3 framework aims to create a free/libre/open-source firmware library for various ARM Cortex-M0(+)/M3/M4 microcontrollers, including ST STM32, Ti Tiva and Stellaris, NXP LPC 11xx, 13xx, 15xx, 17xx parts, Atmel SAM3, Energy Micro EFM32 and others.

    * - :ref:`framework_mbed`
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.

    * - :ref:`framework_spl`
      - The ST Standard Peripheral Library provides a set of functions for handling the peripherals on the STM32 Cortex-M3 family. The idea is to save the user (the new user, in particular) having to deal directly with the registers.

Boards
------

.. note::
    For more detailed ``board`` information please scroll tables below by horizontal.

96Boards
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``b96b_f446ve``
      - `96Boards B96B-F446VE <https://developer.mbed.org/platforms/ST-B96B-F446VE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F446VET6
      - 168 MHz
      - 512 Kb
      - 128 Kb

Arduino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``mzeropro``
      - `Arduino M0 Pro (Programming/Debug Port) <http://www.arduino.org/products/boards/arduino-m0-pro>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``zero``
      - `Arduino Zero (Programming/Debug Port) <https://www.arduino.cc/en/Main/ArduinoBoardZero>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - SAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

Armstrap
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``armstrap_eagle1024``
      - `Armstrap Eagle 1024 <http://docs.armstrap.org/en/latest/hardware-overview.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F417VGT6
      - 168 MHz
      - 1024 Kb
      - 192 Kb

    * - ``armstrap_eagle2048``
      - `Armstrap Eagle 2048 <http://docs.armstrap.org/en/latest/hardware-overview.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F427VIT6
      - 168 MHz
      - 2048 Kb
      - 256 Kb

    * - ``armstrap_eagle512``
      - `Armstrap Eagle 512 <http://docs.armstrap.org/en/latest/hardware-overview.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F407VET6
      - 168 MHz
      - 512 Kb
      - 192 Kb

Atmel
~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``samd21_xpro``
      - `Atmel SAMD21-XPRO <https://developer.mbed.org/platforms/SAMD21-XPRO/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - ATSAMD21J18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``samd21g18a``
      - `Atmel ATSAMW25-XPRO <https://developer.mbed.org/platforms/SAMW25-XPRO/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - ATSAMD21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``saml21_xpro_b``
      - `Atmel SAML21-XPRO-B <https://developer.mbed.org/platforms/SAML21-XPRO/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - ATSAML21J18B
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``samr21_xpro``
      - `Atmel ATSAMR21-XPRO <https://developer.mbed.org/platforms/SAMR21-XPRO/>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - ATSAMR21G18A
      - 48 MHz
      - 256 Kb
      - 32 Kb

Delta
~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``dfcm_nnn40``
      - `Delta DFCM-NNN40 <https://developer.mbed.org/platforms/Delta-DFCM-NNN40/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - NRF51822
      - 32 MHz
      - 256 Kb
      - 32 Kb

Embedded Artists
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``lpc4088``
      - `Embedded Artists LPC4088 QuickStart Board <https://developer.mbed.org/platforms/EA-LPC4088/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - LPC4088
      - 120 MHz
      - 512 Kb
      - 96 Kb

    * - ``lpc4088_dm``
      - `Embedded Artists LPC4088 Display Module <https://developer.mbed.org/platforms/EA-LPC4088-Display-Module/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - LPC4088
      - 120 MHz
      - 512 Kb
      - 96 Kb

Espotel
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``elmo_f411re``
      - `Espotel LoRa Module <https://developer.mbed.org/platforms/Espotel-ELMO/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F411RET6
      - 100 MHz
      - 512 Kb
      - 128 Kb

Freescale
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``IBMEthernetKit``
      - `Ethernet IoT Starter Kit <http://developer.mbed.org/platforms/IBMEthernetKit/>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - MK64FN1M0VLL12
      - 120 MHz
      - 1024 Kb
      - 256 Kb

    * - ``frdm_k20d50m``
      - `Freescale Kinetis FRDM-K20D50M <https://developer.mbed.org/platforms/FRDM-K20D50M/>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - MK20DX128VLH5
      - 48 MHz
      - 128 Kb
      - 16 Kb

    * - ``frdm_k22f``
      - `Freescale Kinetis FRDM-K22F <https://developer.mbed.org/platforms/FRDM-K22F/>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - MK22FN512VLH12
      - 120 MHz
      - 512 Kb
      - 128 Kb

    * - ``frdm_k64f``
      - `Freescale Kinetis FRDM-K64F <https://developer.mbed.org/platforms/FRDM-K64F/>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - MK64FN1M0VLL12
      - 120 MHz
      - 1024 Kb
      - 256 Kb

    * - ``frdm_kl05z``
      - `Freescale Kinetis FRDM-KL05Z <https://developer.mbed.org/platforms/FRDM-KL05Z/>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - MKL05Z32VFM4
      - 48 MHz
      - 32 Kb
      - 4 Kb

    * - ``frdm_kl25z``
      - `Freescale Kinetis FRDM-KL25Z <https://developer.mbed.org/platforms/KL25Z/>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - MKL25Z128VLK4
      - 48 MHz
      - 128 Kb
      - 16 Kb

    * - ``frdm_kl26z``
      - `Freescale Kinetis FRDM-KL26Z <http://www.nxp.com/products/software-and-tools/hardware-development-tools/freedom-development-boards/freedom-development-platform-for-kinetis-kl16-and-kl26-mcus-up-to-128-kb-flash:FRDM-KL26Z>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - MKL26Z128VLH4
      - 48 MHz
      - 128 Kb
      - 16 Kb

    * - ``frdm_kl27z``
      - `Freescale Kinetis FRDM-KL27Z <http://www.nxp.com/products/software-and-tools/hardware-development-tools/freedom-development-boards/freedom-development-platform-for-kinetis-kl17-and-kl27-mcus:FRDM-KL27Z>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - MKL27Z64VLH4
      - 48 MHz
      - 64 Kb
      - 16 Kb

    * - ``frdm_kl43z``
      - `Freescale Kinetis FRDM-KL43Z <http://www.nxp.com/products/software-and-tools/hardware-development-tools/freedom-development-boards/freedom-development-platform-for-kinetis-kl43-kl33-kl27-kl17-and-kl13-mcus:FRDM-KL43Z>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - MKL43Z256VLH4
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``frdm_kl46z``
      - `Freescale Kinetis FRDM-KL46Z <https://developer.mbed.org/platforms/FRDM-KL46Z/>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - MKL46Z256VLL4
      - 48 MHz
      - 256 Kb
      - 32 Kb

Generic
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``bluepill_f103c8``
      - `BluePill F103C8 <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F103C8T6
      - 72 MHz
      - 64 Kb
      - 20 Kb

    * - ``genericSTM32F103C8``
      - `STM32F103C8 (20k RAM. 64k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F103C8
      - 72 MHz
      - 64 Kb
      - 20 Kb

    * - ``genericSTM32F103CB``
      - `STM32F103CB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103cb.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F103CB
      - 72 MHz
      - 128 Kb
      - 20 Kb

    * - ``genericSTM32F103R8``
      - `STM32F103R8 (20k RAM. 64 Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103r8.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F103R8
      - 72 MHz
      - 64 Kb
      - 20 Kb

    * - ``genericSTM32F103RB``
      - `STM32F103RB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rb.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F103RB
      - 72 MHz
      - 128 Kb
      - 20 Kb

    * - ``genericSTM32F103RC``
      - `STM32F103RC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rc.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F103RC
      - 72 MHz
      - 256 Kb
      - 48 Kb

    * - ``genericSTM32F103RE``
      - `STM32F103RE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103re.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F103RE
      - 72 MHz
      - 512 Kb
      - 64 Kb

JKSoft
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``wallbot_ble``
      - `JKSoft Wallbot BLE <https://developer.mbed.org/platforms/JKSoft-Wallbot-BLE/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - NRF51822
      - 16 MHz
      - 128 Kb
      - 16 Kb

Micromint
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``lpc4330_m4``
      - `Bambino-210E <https://developer.mbed.org/platforms/Micromint-Bambino-210E/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - LPC4330
      - 204 MHz
      - 8192 Kb
      - 264 Kb

MikroElektronika
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``hexiwear``
      - `Hexiwear <https://developer.mbed.org/platforms/Hexiwear/>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - MK64FN1M0VDC12
      - 120 MHz
      - 1024 Kb
      - 256 Kb

MultiTech
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``mts_dragonfly_f411re``
      - `MTS Dragonfly <https://developer.mbed.org/platforms/MTS-Dragonfly/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F411RET6
      - 100 MHz
      - 512 Kb
      - 128 Kb

    * - ``mts_mdot_f405rg``
      - `MultiTech mDot <https://developer.mbed.org/platforms/MTS-mDot-F411/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F411RET6
      - 100 MHz
      - 512 Kb
      - 128 Kb

    * - ``mts_mdot_f411re``
      - `MultiTech mDot F411 <https://developer.mbed.org/platforms/MTS-mDot-F411/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F411RET6
      - 100 MHz
      - 512 Kb
      - 128 Kb

Nordic
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``nrf51_dk``
      - `Nordic nRF51-DK <https://developer.mbed.org/platforms/Nordic-nRF51-DK/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - NRF51822
      - 32 MHz
      - 256 Kb
      - 32 Kb

    * - ``nrf51_dongle``
      - `Nordic nRF51-Dongle <https://developer.mbed.org/platforms/Nordic-nRF51-Dongle/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - NRF51822
      - 32 MHz
      - 256 Kb
      - 32 Kb

    * - ``nrf51_mkit``
      - `Nordic nRF51822-mKIT <http://developer.mbed.org/platforms/Nordic-nRF51822/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - NRF51822
      - 16 MHz
      - 128 Kb
      - 16 Kb

RedBearLab
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``redBearLab``
      - `RedBearLab nRF51822 <https://developer.mbed.org/platforms/RedBearLab-nRF51822/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - NRF51822
      - 16 MHz
      - 256 Kb
      - 16 Kb

    * - ``redBearLabBLENano``
      - `RedBearLab BLE Nano <https://developer.mbed.org/platforms/RedBearLab-BLE-Nano/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - NRF51822
      - 16 MHz
      - 256 Kb
      - 32 Kb

ST
~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``disco_f030r8``
      - `ST STM32F0308DISCOVERY <http://www.st.com/en/evaluation-tools/32f0308discovery.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F030R8T6
      - 48 MHz
      - 64 Kb
      - 8 Kb

    * - ``disco_f051r8``
      - `ST STM32F0DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF253215>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F051R8T6
      - 48 MHz
      - 64 Kb
      - 8 Kb

    * - ``disco_f100rb``
      - `ST STM32VLDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF250863>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F100RBT6
      - 24 MHz
      - 128 Kb
      - 8 Kb

    * - ``disco_f303vc``
      - `ST STM32F3DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF254044>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F303VCT6
      - 72 MHz
      - 256 Kb
      - 48 Kb

    * - ``disco_f334c8``
      - `ST 32F3348DISCOVERY <http://www.st.com/web/en/catalog/tools/PF260318>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F334C8T6
      - 72 MHz
      - 64 Kb
      - 12 Kb

    * - ``disco_f401vc``
      - `ST 32F401CDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF259098>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F401VCT6
      - 84 MHz
      - 256 Kb
      - 64 Kb

    * - ``disco_f407vg``
      - `ST STM32F4DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF252419>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F407VGT6
      - 168 MHz
      - 1024 Kb
      - 128 Kb

    * - ``disco_f429zi``
      - `ST 32F429IDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF259090>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F429ZIT6
      - 180 MHz
      - 2048 Kb
      - 256 Kb

    * - ``disco_f469ni``
      - `ST 32F469IDISCOVERY <http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF262395>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F469NIH6
      - 180 MHz
      - 1024 Kb
      - 384 Kb

    * - ``disco_f746ng``
      - `ST 32F746GDISCOVERY <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/32f746gdiscovery.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F746NGH6
      - 216 MHz
      - 1024 Kb
      - 320 Kb

    * - ``disco_f769ni``
      - `ST 32F769IDISCOVERY <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/32f769idiscovery.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F769NIH6
      - 80 MHz
      - 1024 Kb
      - 512 Kb

    * - ``disco_l053c8``
      - `ST 32L0538DISCOVERY <http://www.st.com/web/en/catalog/tools/PF260319>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32L053C8T6
      - 32 MHz
      - 64 Kb
      - 8 Kb

    * - ``disco_l152rb``
      - `ST STM32LDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF258515>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32L152RBT6
      - 32 MHz
      - 128 Kb
      - 16 Kb

    * - ``disco_l476vg``
      - `ST 32L476GDISCOVERY <http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF261635>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32L476VGT6
      - 80 MHz
      - 1024 Kb
      - 128 Kb

    * - ``nucleo_f030r8``
      - `ST Nucleo F030R8 <https://developer.mbed.org/platforms/ST-Nucleo-F030R8/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F030R8T6
      - 48 MHz
      - 64 Kb
      - 8 Kb

    * - ``nucleo_f031k6``
      - `ST Nucleo F031K6 <https://developer.mbed.org/platforms/ST-Nucleo-F031K6/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F031K6T6
      - 48 MHz
      - 32 Kb
      - 4 Kb

    * - ``nucleo_f042k6``
      - `ST Nucleo F042K6 <https://developer.mbed.org/platforms/ST-Nucleo-F042K6/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F042K6T6
      - 48 MHz
      - 32 Kb
      - 6 Kb

    * - ``nucleo_f070rb``
      - `ST Nucleo F070RB <https://developer.mbed.org/platforms/ST-Nucleo-F070RB/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F070RBT6
      - 48 MHz
      - 128 Kb
      - 16 Kb

    * - ``nucleo_f072rb``
      - `ST Nucleo F072RB <https://developer.mbed.org/platforms/ST-Nucleo-F072RB/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F072RBT6
      - 48 MHz
      - 128 Kb
      - 16 Kb

    * - ``nucleo_f091rc``
      - `ST Nucleo F091RC <https://developer.mbed.org/platforms/ST-Nucleo-F091RC/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F091RCT6
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``nucleo_f103rb``
      - `ST Nucleo F103RB <https://developer.mbed.org/platforms/ST-Nucleo-F103RB/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F103RBT6
      - 72 MHz
      - 128 Kb
      - 20 Kb

    * - ``nucleo_f207zg``
      - `ST Nucleo F207ZG <https://developer.mbed.org/platforms/ST-Nucleo-F207ZG/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F207ZGT6
      - 120 MHz
      - 1024 Kb
      - 128 Kb

    * - ``nucleo_f302r8``
      - `ST Nucleo F302R8 <https://developer.mbed.org/platforms/ST-Nucleo-F302R8/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F302R8T6
      - 72 MHz
      - 64 Kb
      - 16 Kb

    * - ``nucleo_f303k8``
      - `ST Nucleo F303K8 <https://developer.mbed.org/platforms/ST-Nucleo-F303K8/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F303K8T6
      - 72 MHz
      - 64 Kb
      - 16 Kb

    * - ``nucleo_f303re``
      - `ST Nucleo F303RE <http://developer.mbed.org/platforms/ST-Nucleo-F303RE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F303RET6
      - 72 MHz
      - 512 Kb
      - 64 Kb

    * - ``nucleo_f303ze``
      - `ST Nucleo F303ZE <https://developer.mbed.org/platforms/ST-Nucleo-F303ZE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F303ZET6
      - 72 MHz
      - 512 Kb
      - 64 Kb

    * - ``nucleo_f334r8``
      - `ST Nucleo F334R8 <https://developer.mbed.org/platforms/ST-Nucleo-F334R8/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F334R8T6
      - 72 MHz
      - 64 Kb
      - 16 Kb

    * - ``nucleo_f401re``
      - `ST Nucleo F401RE <https://developer.mbed.org/platforms/ST-Nucleo-F401RE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F401RET6
      - 84 MHz
      - 512 Kb
      - 96 Kb

    * - ``nucleo_f410rb``
      - `ST Nucleo F410RB <https://developer.mbed.org/platforms/ST-Nucleo-F410RB/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F410RBT6
      - 100 MHz
      - 128 Kb
      - 32 Kb

    * - ``nucleo_f411re``
      - `ST Nucleo F411RE <https://developer.mbed.org/platforms/ST-Nucleo-F411RE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F411RET6
      - 100 MHz
      - 512 Kb
      - 128 Kb

    * - ``nucleo_f429zi``
      - `ST Nucleo F429ZI <https://developer.mbed.org/platforms/ST-Nucleo-F429ZI/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F429ZIT6
      - 180 MHz
      - 2048 Kb
      - 256 Kb

    * - ``nucleo_f446re``
      - `ST Nucleo F446RE <https://developer.mbed.org/platforms/ST-Nucleo-F446RE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F446RET6
      - 180 MHz
      - 512 Kb
      - 128 Kb

    * - ``nucleo_f446ze``
      - `ST Nucleo F446ZE <https://developer.mbed.org/platforms/ST-Nucleo-F446ZE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F446ZET6
      - 180 MHz
      - 512 Kb
      - 128 Kb

    * - ``nucleo_f746zg``
      - `ST Nucleo F746ZG <https://developer.mbed.org/platforms/ST-Nucleo-F446ZE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F746ZGT6
      - 216 MHz
      - 1024 Kb
      - 320 Kb

    * - ``nucleo_f767zi``
      - `ST Nucleo F767ZI <https://developer.mbed.org/platforms/ST-Nucleo-F767ZI/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F746ZGT6
      - 216 MHz
      - 2048 Kb
      - 512 Kb

    * - ``nucleo_l011k4``
      - `ST Nucleo L011K4 <https://developer.mbed.org/platforms/ST-Nucleo-L011K4/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32L011K4T6
      - 32 MHz
      - 16 Kb
      - 2 Kb

    * - ``nucleo_l031k6``
      - `ST Nucleo L031K6 <https://developer.mbed.org/platforms/ST-Nucleo-L031K6/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32L031K6T6
      - 32 MHz
      - 32 Kb
      - 8 Kb

    * - ``nucleo_l053r8``
      - `ST Nucleo L053R8 <https://developer.mbed.org/platforms/ST-Nucleo-L053R8/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32L053R8T6
      - 48 MHz
      - 64 Kb
      - 8 Kb

    * - ``nucleo_l073rz``
      - `ST Nucleo L073RZ <https://developer.mbed.org/platforms/ST-Nucleo-L073RZ/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32L073RZ
      - 32 MHz
      - 192 Kb
      - 20 Kb

    * - ``nucleo_l152re``
      - `ST Nucleo L152RE <https://developer.mbed.org/platforms/ST-Nucleo-L152RE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32L152RET6
      - 32 MHz
      - 512 Kb
      - 80 Kb

    * - ``nucleo_l432kc``
      - `ST Nucleo L432KC <https://developer.mbed.org/platforms/ST-Nucleo-L432KC/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32L432KCU6
      - 80 MHz
      - 256 Kb
      - 64 Kb

    * - ``nucleo_l476rg``
      - `ST Nucleo L476RG <https://developer.mbed.org/platforms/ST-Nucleo-L476RG/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32L476RGT6
      - 80 MHz
      - 1024 Kb
      - 128 Kb

SeeedStudio
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``seeedArchBLE``
      - `Seeed Arch BLE <https://developer.mbed.org/platforms/Seeed-Arch-BLE/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - NRF51822
      - 16 MHz
      - 128 Kb
      - 16 Kb

    * - ``seeedArchLink``
      - `Seeed Arch Link <https://developer.mbed.org/platforms/Seeed-Arch-Link/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - NRF51822
      - 16 MHz
      - 256 Kb
      - 16 Kb

    * - ``seeedArchMax``
      - `Seeed Arch Max <https://developer.mbed.org/platforms/Seeed-Arch-Max/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F407VET6
      - 168 MHz
      - 512 Kb
      - 192 Kb

    * - ``seeedArchPro``
      - `Seeed Arch Pro <https://developer.mbed.org/platforms/Seeeduino-Arch-Pro/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - LPC1768
      - 96 MHz
      - 512 Kb
      - 64 Kb

    * - ``seeedTinyBLE``
      - `Seeed Tiny BLE <http://developer.mbed.org/platforms/Seeed-Tiny-BLE/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - NRF51822
      - 16 MHz
      - 256 Kb
      - 16 Kb

Semtech
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``mote_l152rc``
      - `NAMote72 <https://developer.mbed.org/platforms/NAMote-72/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32L152RC
      - 32 MHz
      - 256 Kb
      - 32 Kb

Silicon Labs
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``efm32gg_stk3700``
      - `Silicon Labs EFM32GG-STK3700 (Giant Gecko) <https://developer.mbed.org/platforms/EFM32-Giant-Gecko/>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - EFM32GG990F1024
      - 48 MHz
      - 1024 Kb
      - 128 Kb

    * - ``efm32hg_stk3400``
      - `Silicon Labs SLSTK3400A USB-enabled (Happy Gecko) <https://developer.mbed.org/platforms/EFM32-Happy-Gecko/>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - EFM32HG322F64
      - 24 MHz
      - 64 Kb
      - 8 Kb

    * - ``efm32lg_stk3600``
      - `Silicon Labs EFM32LG-STK3600 (Leopard Gecko) <https://developer.mbed.org/platforms/EFM32-Leopard-Gecko/>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - EFM32LG990F256
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``efm32pg_stk3401``
      - `Silicon Labs SLSTK3401A (Pearl Gecko) <https://developer.mbed.org/platforms/EFM32-Pearl-Gecko/>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - EFM32PG1B200F256
      - 40 MHz
      - 256 Kb
      - 32 Kb

    * - ``efm32wg_stk3800``
      - `Silicon Labs EFM32WG-STK3800 (Wonder Gecko) <https://developer.mbed.org/platforms/EFM32-Wonder-Gecko/>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - EFM32WG990F256
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``efm32zg_stk3200``
      - `Silicon Labs EFM32ZG-STK3200 (Zero Gecko) <https://developer.mbed.org/platforms/EFM32-Zero-Gecko/>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - EFM2ZG222F32
      - 24 MHz
      - 32 Kb
      - 4 Kb

Switch Science
~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``hrm1017``
      - `Switch Science mbed HRM1017 <https://developer.mbed.org/platforms/mbed-HRM1017/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - NRF51822
      - 16 MHz
      - 256 Kb
      - 16 Kb

    * - ``ssci824``
      - `Switch Science mbed LPC824 <https://developer.mbed.org/platforms/Switch-Science-mbed-LPC824/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - LPC824
      - 30 MHz
      - 32 Kb
      - 8 Kb

    * - ``ty51822r3``
      - `Switch Science mbed TY51822r3 <https://developer.mbed.org/platforms/Switch-Science-mbed-TY51822r3/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - NRF51822
      - 32 MHz
      - 256 Kb
      - 32 Kb

TI
~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``lplm4f120h5qr``
      - `TI LaunchPad (Stellaris) w/ lm4f120 (80MHz) <http://www.ti.com/tool/ek-lm4f120xl>`_
      - :ref:`TI TIVA <platform_titiva>`
      - LPLM4F120H5QR
      - 80 MHz
      - 256 Kb
      - 32 Kb

    * - ``lpmsp430f5529``
      - `TI LaunchPad MSP-EXP430F5529LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430f5529lp.html>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - MSP430F5529
      - 16 MHz
      - 128 Kb
      - 8 Kb

    * - ``lpmsp430fr4133``
      - `TI LaunchPad MSP-EXP430FR4133LP <http://www.ti.com/tool/msp-exp430fr4133>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - MSP430FR4133
      - 8 MHz
      - 16 Kb
      - 2 Kb

    * - ``lpmsp430fr5739``
      - `TI FraunchPad MSP-EXP430FR5739LP <http://www.ti.com/tool/msp-exp430fr5739>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - MSP430FR5739
      - 16 MHz
      - 16 Kb
      - 0.5 Kb

    * - ``lpmsp430fr5969``
      - `TI LaunchPad MSP-EXP430FR5969LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430fr5969.html>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - MSP430FR5969
      - 8 MHz
      - 64 Kb
      - 2 Kb

    * - ``lpmsp430fr6989``
      - `TI LaunchPad MSP-EXP430FR6989LP <http://www.ti.com/tool/msp-exp430fr6989>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - MSP430FR6989
      - 8 MHz
      - 128 Kb
      - 2 Kb

    * - ``lpmsp430g2553``
      - `TI LaunchPad MSP-EXP430G2553LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430g2.html>`_
      - :ref:`TI MSP430 <platform_timsp430>`
      - MSP430G2553
      - 16 MHz
      - 16 Kb
      - 0.5 Kb

    * - ``lptm4c1230c3pm``
      - `TI LaunchPad (Tiva C) w/ tm4c123 (80MHz) <http://www.ti.com/ww/en/launchpad/launchpads-connected-ek-tm4c123gxl.html>`_
      - :ref:`TI TIVA <platform_titiva>`
      - LPTM4C1230C3PM
      - 80 MHz
      - 256 Kb
      - 32 Kb

    * - ``lptm4c1294ncpdt``
      - `TI LaunchPad (Tiva C) w/ tm4c129 (120MHz) <http://www.ti.com/ww/en/launchpad/launchpads-connected-ek-tm4c1294xl.html>`_
      - :ref:`TI TIVA <platform_titiva>`
      - LPTM4C1294NCPDT
      - 120 MHz
      - 1024 Kb
      - 256 Kb

u-blox
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``ublox_evk_odin_w2``
      - `u-blox EVK-ODIN-W2 <https://developer.mbed.org/platforms/ublox-EVK-ODIN-W2/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - STM32F439ZIY6
      - 168 MHz
      - 2048 Kb
      - 256 Kb

    * - ``ubloxc027``
      - `u-blox C027 <https://developer.mbed.org/platforms/u-blox-C027/>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - LPC1768
      - 96 MHz
      - 512 Kb
      - 64 Kb

y5 design
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``nrf51822_y5_mbug``
      - `y5 nRF51822 mbug <https://developer.mbed.org/platforms/Y5-NRF51822-MBUG/>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - NRF51822
      - 16 MHz
      - 256 Kb
      - 16 Kb
