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

.. _framework_mbed:

mbed
====
:ref:`projectconf_env_framework` = ``mbed``

The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.

For more detailed information please visit `vendor site <http://mbed.org/?utm_source=platformio&utm_medium=docs>`_.


.. contents:: Contents
    :local:
    :depth: 1
.. include:: mbed_extra.rst

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

Supported debugging tools are listed in "Debug" column. For more detailed
information, please scroll table by horizontal.
You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` options.


On-Board tools
~~~~~~~~~~~~~~

Boards listed below have on-board debugging tools and **ARE READY** for debugging!
You do not need to use/buy external debugger.


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
    * - ``b96b_f446ve``
      - `96Boards B96B-F446VE <https://developer.mbed.org/platforms/ST-B96B-F446VE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_stlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - STM32F446VET6
      - 168MHz
      - 512KB
      - 128KB
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
    * - ``elektor_cocorico``
      - `CoCo-ri-Co! <https://developer.mbed.org/platforms/CoCo-ri-Co/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC812
      - 30MHz
      - 16KB
      - 4KB
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
    * - ``frdm_kl26z``
      - `Freescale Kinetis FRDM-KL26Z <http://www.nxp.com/products/software-and-tools/hardware-development-tools/freedom-development-boards/freedom-development-platform-for-kinetis-kl16-and-kl26-mcus-up-to-128-kb-flash:FRDM-KL26Z?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink`
      - MKL26Z128VLH4
      - 48MHz
      - 128KB
      - 16KB
    * - ``frdm_kl27z``
      - `Freescale Kinetis FRDM-KL27Z <http://www.nxp.com/products/software-and-tools/hardware-development-tools/freedom-development-boards/freedom-development-platform-for-kinetis-kl17-and-kl27-mcus:FRDM-KL27Z?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - MKL27Z64VLH4
      - 48MHz
      - 64KB
      - 16KB
    * - ``frdm_kl43z``
      - `Freescale Kinetis FRDM-KL43Z <http://www.nxp.com/products/software-and-tools/hardware-development-tools/freedom-development-boards/freedom-development-platform-for-kinetis-kl43-kl33-kl27-kl17-and-kl13-mcus:FRDM-KL43Z?utm_source=platformio&utm_medium=docs>`_
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
    * - ``lpc11u68``
      - `LPCXpresso11U68 <https://developer.mbed.org/platforms/LPCXpresso11U68/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U68
      - 50MHz
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
    * - ``max32600mbed``
      - `Maxim ARM mbed Enabled Development Platform for MAX32600 <https://developer.mbed.org/platforms/MAX32600mbed/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - MAX32600
      - 24MHz
      - 256KB
      - 32KB
    * - ``mbed_connect_odin``
      - `Mbed Connect Cloud <https://os.mbed.com/platforms/mbed-Connect-Cloud/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
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
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``nrf51_dongle``
      - `Nordic nRF51-Dongle <https://developer.mbed.org/platforms/Nordic-nRF51-Dongle/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink` (default, on-board)
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
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - ``nrf52_dk``
      - `Nordic nRF52-DK <https://developer.mbed.org/platforms/Nordic-nRF52-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_jlink` (default, on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink`
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
      - 48MHz
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
    * - ``samd21_xpro``
      - `Atmel SAMD21-XPRO <https://developer.mbed.org/platforms/SAMD21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - ATSAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``samd21g18a``
      - `Atmel ATSAMW25-XPRO <https://developer.mbed.org/platforms/SAMW25-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - ATSAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``saml21_xpro_b``
      - `Atmel SAML21-XPRO-B <https://developer.mbed.org/platforms/SAML21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - ATSAML21J18B
      - 48MHz
      - 256KB
      - 32KB
    * - ``samr21_xpro``
      - `Atmel ATSAMR21-XPRO <https://developer.mbed.org/platforms/SAMR21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_atmel-ice`, :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - ATSAMR21G18A
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
    * - ``ublox_evk_nina_b1``
      - `u-blox EVK-NINA-B1 <https://os.mbed.com/platforms/u-blox-EVK-NINA-B1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`debugging_tool_jlink` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``ubloxc027``
      - `u-blox C027 <https://developer.mbed.org/platforms/u-blox-C027/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_cmsis-dap` (on-board), :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB
    * - ``vbluno51``
      - `VNG VBLUNO51 <https://os.mbed.com/platforms/VBLUNO51/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 16MHz
      - 128KB
      - 32KB
    * - ``wallbot_ble``
      - `JKSoft Wallbot BLE <https://developer.mbed.org/platforms/JKSoft-Wallbot-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`debugging_tool_cmsis-dap` (on-board)
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB
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


External tools
~~~~~~~~~~~~~~

Boards listed below are compatible with :ref:`piodebug` but depend on external
debugging tools. See "Debug" column for compatible debugging tools.


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
    * - ``bluepill_f103c8``
      - `BluePill F103C8 <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``dipcortexm0``
      - `Solder Splash Labs DipCortex M0 <https://developer.mbed.org/platforms/DipCortex-M0/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11U24
      - 50MHz
      - 32KB
      - 8KB
    * - ``elmo_f411re``
      - `Espotel LoRa Module <https://developer.mbed.org/platforms/Espotel-ELMO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink` (default)
      - STM32F411RET6
      - 100MHz
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
    * - ``genericSTM32F103RB``
      - `STM32F103RB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``hexiwear``
      - `Hexiwear <https://developer.mbed.org/platforms/Hexiwear/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`debugging_tool_cmsis-dap`, :ref:`debugging_tool_jlink`
      - MK64FN1M0VDC12
      - 120MHz
      - 1MB
      - 256KB
    * - ``lpc11c24``
      - `NXP LPC11C24 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-m0-cores:LPC11C24FBD48?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`
      - LPC11C24
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
    * - ``maxwsnenv``
      - `Maxim Wireless Sensor Node Demonstrator <https://developer.mbed.org/platforms/MAXWSNENV/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - :ref:`debugging_tool_cmsis-dap`
      - MAX32610
      - 24MHz
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
    * - ``teensy31``
      - `Teensy 3.1 / 3.2 <https://www.pjrc.com/store/teensy31.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Teensy <platform_teensy>`
      - :ref:`debugging_tool_jlink`
      - MK20DX256
      - 72MHz
      - 256KB
      - 64KB
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
    * - ``ublox_evk_odin_w2``
      - `u-blox EVK-ODIN-W2 <https://developer.mbed.org/platforms/ublox-EVK-ODIN-W2/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
    * - ``xdot_l151cc``
      - `MultiTech xDot <https://developer.mbed.org/platforms/MTS-xDot-L151CC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_jlink`, :ref:`debugging_tool_stlink`
      - STM32L151CCU6
      - 32MHz
      - 256KB
      - 32KB


Examples
--------

* `mbed for Atmel SAM <https://github.com/platformio/platform-atmelsam/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `mbed for Freescale Kinetis <https://github.com/platformio/platform-freescalekinetis/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `mbed for Maxim 32 <https://github.com/platformio/platform-maxim32/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `mbed for Nordic nRF51 <https://github.com/platformio/platform-nordicnrf51/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `mbed for Nordic nRF52 <https://github.com/platformio/platform-nordicnrf52/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `mbed for NXP LPC <https://github.com/platformio/platform-nxplpc/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `mbed for WIZNet W7500 <https://github.com/platformio/platform-wiznet7500/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `mbed for Silicon Labs EFM32 <https://github.com/platformio/platform-siliconlabsefm32/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `mbed for ST STM32 <https://github.com/platformio/platform-ststm32/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_
* `mbed for Teensy <https://github.com/platformio/platform-teensy/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_

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

    * - :ref:`platform_wiznet7500`
      - The IOP (Internet Offload Processor) W7500 is the one-chip solution which integrates an ARM Cortex-M0, 128KB Flash and hardwired TCP/IP core for various embedded application platform especially requiring Internet of things

    * - :ref:`platform_siliconlabsefm32`
      - Silicon Labs EFM32 Gecko 32-bit microcontroller (MCU) family includes devices that offer flash memory configurations up to 256 kB, 32 kB of RAM and CPU speeds up to 48 MHz. Based on the powerful ARM Cortex-M core, the Gecko family features innovative low energy techniques, short wake-up time from energy saving modes and a wide selection of peripherals, making it ideal for battery operated applications and other systems requiring high performance and low-energy consumption.

    * - :ref:`platform_ststm32`
      - The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

    * - :ref:`platform_teensy`
      - Teensy is a complete USB-based microcontroller development system, in a very small footprint, capable of implementing many types of projects. All programming is done via the USB port. No special programmer is needed, only a standard USB cable and a PC or Macintosh with a USB port.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by horizontal.

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
      - :ref:`Yes <piodebug>`
      - STM32F446VET6
      - 168MHz
      - 512KB
      - 128KB

AppNearMe
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
    * - ``micronfcboard``
      - `MicroNFCBoard <https://os.mbed.com/platforms/MicroNFCBoard/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - No
      - LPC11U34
      - 48MHz
      - 48KB
      - 10KB

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
      - :ref:`Yes <piodebug>`
      - ATSAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``samd21g18a``
      - `Atmel ATSAMW25-XPRO <https://developer.mbed.org/platforms/SAMW25-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - ATSAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - ``saml21_xpro_b``
      - `Atmel SAML21-XPRO-B <https://developer.mbed.org/platforms/SAML21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - ATSAML21J18B
      - 48MHz
      - 256KB
      - 32KB
    * - ``samr21_xpro``
      - `Atmel ATSAMR21-XPRO <https://developer.mbed.org/platforms/SAMR21-XPRO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - :ref:`Yes <piodebug>`
      - ATSAMR21G18A
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
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``bbcmicrobit_b``
      - `BBC micro:bit B(S130) <https://developer.mbed.org/platforms/Microbit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

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
      - :ref:`Yes <piodebug>`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB

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
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``delta_dfcm_nnn50``
      - `Delta DFCM-NNN50 <https://os.mbed.com/platforms/Delta-DFCM-NNN50/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 16KB
    * - ``dfcm_nnn40``
      - `Delta DFCM-NNN40 <https://developer.mbed.org/platforms/Delta-DFCM-NNN40/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

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
      - :ref:`Yes <piodebug>`
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
      - :ref:`Yes <piodebug>`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
    * - ``lpc4088``
      - `Embedded Artists LPC4088 QuickStart Board <https://developer.mbed.org/platforms/EA-LPC4088/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC4088
      - 120MHz
      - 512KB
      - 96KB
    * - ``lpc4088_dm``
      - `Embedded Artists LPC4088 Display Module <https://developer.mbed.org/platforms/EA-LPC4088-Display-Module/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
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
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB

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
      - :ref:`Yes <piodebug>`
      - MK64FN1M0VLL12
      - 120MHz
      - 1MB
      - 256KB
    * - ``frdm_k20d50m``
      - `Freescale Kinetis FRDM-K20D50M <https://developer.mbed.org/platforms/FRDM-K20D50M/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MK20DX128VLH5
      - 48MHz
      - 128KB
      - 16KB
    * - ``frdm_k22f``
      - `Freescale Kinetis FRDM-K22F <https://developer.mbed.org/platforms/FRDM-K22F/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MK22FN512VLH12
      - 120MHz
      - 512KB
      - 128KB
    * - ``frdm_k64f``
      - `Freescale Kinetis FRDM-K64F <https://developer.mbed.org/platforms/FRDM-K64F/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MK64FN1M0VLL12
      - 120MHz
      - 1MB
      - 256KB
    * - ``frdm_k66f``
      - `Freescale Kinetis FRDM-K66F <https://developer.mbed.org/platforms/FRDM-K66F/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MK66FN2M0VMD18
      - 180MHz
      - 2MB
      - 256KB
    * - ``frdm_kl05z``
      - `Freescale Kinetis FRDM-KL05Z <https://developer.mbed.org/platforms/FRDM-KL05Z/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL05Z32VFM4
      - 48MHz
      - 32KB
      - 4KB
    * - ``frdm_kl25z``
      - `Freescale Kinetis FRDM-KL25Z <https://developer.mbed.org/platforms/KL25Z/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL25Z128VLK4
      - 48MHz
      - 128KB
      - 16KB
    * - ``frdm_kl26z``
      - `Freescale Kinetis FRDM-KL26Z <http://www.nxp.com/products/software-and-tools/hardware-development-tools/freedom-development-boards/freedom-development-platform-for-kinetis-kl16-and-kl26-mcus-up-to-128-kb-flash:FRDM-KL26Z?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL26Z128VLH4
      - 48MHz
      - 128KB
      - 16KB
    * - ``frdm_kl27z``
      - `Freescale Kinetis FRDM-KL27Z <http://www.nxp.com/products/software-and-tools/hardware-development-tools/freedom-development-boards/freedom-development-platform-for-kinetis-kl17-and-kl27-mcus:FRDM-KL27Z?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL27Z64VLH4
      - 48MHz
      - 64KB
      - 16KB
    * - ``frdm_kl43z``
      - `Freescale Kinetis FRDM-KL43Z <http://www.nxp.com/products/software-and-tools/hardware-development-tools/freedom-development-boards/freedom-development-platform-for-kinetis-kl43-kl33-kl27-kl17-and-kl13-mcus:FRDM-KL43Z?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL43Z256VLH4
      - 48MHz
      - 256KB
      - 32KB
    * - ``frdm_kl46z``
      - `Freescale Kinetis FRDM-KL46Z <https://developer.mbed.org/platforms/FRDM-KL46Z/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKL46Z256VLL4
      - 48MHz
      - 256KB
      - 32KB
    * - ``frdm_kw41z``
      - `Freescale Kinetis FRDM-KW41Z <https://os.mbed.com/platforms/FRDM-KW41Z/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Freescale Kinetis <platform_freescalekinetis>`
      - :ref:`Yes <piodebug>`
      - MKW41Z512VHT4
      - 48MHz
      - 512KB
      - 128KB

GHI Electronics
~~~~~~~~~~~~~~~

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
    * - ``oc_mbuino``
      - `mBuino <https://developer.mbed.org/platforms/mBuino/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - No
      - LPC11U24
      - 50MHz
      - 32KB
      - 10KB

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
      - :ref:`Yes <piodebug>`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``genericSTM32F103C8``
      - `STM32F103C8 (20k RAM. 64k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``genericSTM32F103RB``
      - `STM32F103RB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB

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
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB

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
      - :ref:`Yes <piodebug>`
      - MAX32600
      - 24MHz
      - 256KB
      - 32KB
    * - ``max32620hsp``
      - `Maxim Health Sensor Platform <https://developer.mbed.org/platforms/MAX32620HSP/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - No
      - MAX32620
      - 96MHz
      - 2MB
      - 256KB
    * - ``max32625mbed``
      - `MAX32625MBED <https://os.mbed.com/platforms/MAX32625MBED/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - No
      - MAX32625
      - 96MHz
      - 512KB
      - 160KB
    * - ``max32625nexpaq``
      - `MAX32625NEXPAQ <https://os.mbed.com/platforms/max32625nexpaq/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - No
      - MAX32625
      - 96MHz
      - 512KB
      - 160KB
    * - ``max32630fthr``
      - `Maxim MAX32630FTHR Application Platform <https://developer.mbed.org/platforms/MAX32630FTHR/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - No
      - MAX32630
      - 96MHz
      - 2MB
      - 512KB
    * - ``maxwsnenv``
      - `Maxim Wireless Sensor Node Demonstrator <https://developer.mbed.org/platforms/MAXWSNENV/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - :ref:`Yes <piodebug>`
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
      - :ref:`Yes <piodebug>`
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
      - :ref:`Yes <piodebug>`
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
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``mts_mdot_f405rg``
      - `MultiTech mDot <https://developer.mbed.org/platforms/MTS-mDot-F411/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``mts_mdot_f411re``
      - `MultiTech mDot F411 <https://developer.mbed.org/platforms/MTS-mDot-F411/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``xdot_l151cc``
      - `MultiTech xDot <https://developer.mbed.org/platforms/MTS-xDot-L151CC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
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
      - :ref:`Yes <piodebug>`
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
      - :ref:`Yes <piodebug>`
      - LPC11C24
      - 48MHz
      - 32KB
      - 8KB
    * - ``lpc11u24``
      - `NXP mbed LPC11U24 <https://developer.mbed.org/platforms/mbed-LPC11U24/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - ``lpc11u24_301``
      - `ARM mbed LPC11U24 (+CAN) <https://developer.mbed.org/handbook/mbed-NXP-LPC11U24?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - ``lpc11u34_421``
      - `NXP LPC11U34 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/40kb-flash-8kb-sram-lqfp48-package:LPC11U34FBD48?lang_cd=en&utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U34
      - 48MHz
      - 40KB
      - 8KB
    * - ``lpc11u37_501``
      - `NXP LPC11U37 <http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/lpc-cortex-m-mcus/lpc-cortex-m0-plus-m0/lpc1100-cortex-m0-plus-m0/128kb-flash-10kb-sram-lqfp48-package:LPC11U37FBD48?lang_cd=en&utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U37
      - 48MHz
      - 128KB
      - 10KB
    * - ``lpc11u68``
      - `LPCXpresso11U68 <https://developer.mbed.org/platforms/LPCXpresso11U68/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC11U68
      - 50MHz
      - 256KB
      - 36KB
    * - ``lpc1549``
      - `NXP LPCXpresso1549 <https://developer.mbed.org/platforms/LPCXpresso1549/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC1549
      - 72MHz
      - 256KB
      - 36KB
    * - ``lpc1768``
      - `NXP mbed LPC1768 <http://developer.mbed.org/platforms/mbed-LPC1768/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB
    * - ``lpc54114``
      - `NXP LPCXpresso54114 <https://os.mbed.com/platforms/LPCXpresso54114/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC54114J256BD64
      - 100MHz
      - 256KB
      - 192KB
    * - ``lpc546xx``
      - `NXP LPCXpresso54608 <https://os.mbed.com/platforms/LPCXpresso54608/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC54608ET512
      - 180MHz
      - 512KB
      - 200KB
    * - ``lpc812``
      - `NXP LPC800-MAX <https://developer.mbed.org/platforms/NXP-LPC800-MAX/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC812
      - 30MHz
      - 16KB
      - 4KB
    * - ``lpc824``
      - `LPCXpresso824-MAX <https://developer.mbed.org/platforms/LPCXpresso824-MAX/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC824
      - 30MHz
      - 32KB
      - 8KB

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
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``nrf51_dongle``
      - `Nordic nRF51-Dongle <https://developer.mbed.org/platforms/Nordic-nRF51-Dongle/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - ``nrf51_mkit``
      - `Nordic nRF51822-mKIT <http://developer.mbed.org/platforms/Nordic-nRF51822/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB
    * - ``nrf52840_dk``
      - `Nordic nRF52840-DK <https://os.mbed.com/platforms/Nordic-nRF52840-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - ``nrf52_dk``
      - `Nordic nRF52-DK <https://developer.mbed.org/platforms/Nordic-nRF52-DK/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

Outrageous Circuits
~~~~~~~~~~~~~~~~~~~

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
    * - ``mbuino``
      - `Outrageous Circuits mBuino <https://developer.mbed.org/platforms/Outrageous-Circuits-mBuino/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - No
      - LPC11U24
      - 48MHz
      - 32KB
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
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``redBearLabBLENano``
      - `RedBearLab BLE Nano 1.5 <https://developer.mbed.org/platforms/RedBearLab-BLE-Nano/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB

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
      - :ref:`Yes <piodebug>`
      - STM32F401RET6
      - 84MHz
      - 512KB
      - 96KB
    * - ``cloud_jam_l4``
      - `RushUp Cloud-JAM L4 <https://developer.mbed.org/platforms/ST-Nucleo-L476RG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L476RGT6
      - 80MHz
      - 1MB
      - 128KB

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
      - :ref:`Yes <piodebug>`
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - ``disco_f051r8``
      - `ST STM32F0DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF253215?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F051R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - ``disco_f100rb``
      - `ST STM32VLDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF250863?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F100RBT6
      - 24MHz
      - 128KB
      - 8KB
    * - ``disco_f303vc``
      - `ST STM32F3DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF254044?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F303VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``disco_f334c8``
      - `ST 32F3348DISCOVERY <http://www.st.com/web/en/catalog/tools/PF260318?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F334C8T6
      - 72MHz
      - 64KB
      - 12KB
    * - ``disco_f401vc``
      - `ST 32F401CDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF259098?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F401VCT6
      - 84MHz
      - 256KB
      - 64KB
    * - ``disco_f407vg``
      - `ST STM32F4DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF252419?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F407VGT6
      - 168MHz
      - 1MB
      - 128KB
    * - ``disco_f413zh``
      - `ST 32F413HDISCOVERY <https://os.mbed.com/platforms/ST-Discovery-F413H/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F413ZHT6
      - 100MHz
      - 512KB
      - 128KB
    * - ``disco_f429zi``
      - `ST 32F429IDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF259090?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F429ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - ``disco_f469ni``
      - `ST 32F469IDISCOVERY <http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF262395?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F469NIH6
      - 180MHz
      - 1MB
      - 384KB
    * - ``disco_f746ng``
      - `ST 32F746GDISCOVERY <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/32f746gdiscovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F746NGH6
      - 216MHz
      - 1MB
      - 320KB
    * - ``disco_f769ni``
      - `ST 32F769IDISCOVERY <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/32f769idiscovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F769NIH6
      - 80MHz
      - 1MB
      - 512KB
    * - ``disco_l053c8``
      - `ST 32L0538DISCOVERY <http://www.st.com/web/en/catalog/tools/PF260319?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L053C8T6
      - 32MHz
      - 64KB
      - 8KB
    * - ``disco_l072cz_lrwan1``
      - `ST DISCO-L072CZ-LRWAN1 <https://developer.mbed.org/platforms/ST-Discovery-LRWAN1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L072CZ
      - 32MHz
      - 192KB
      - 20KB
    * - ``disco_l475vg_iot01a``
      - `ST DISCO-L475VG-IOT01A <https://developer.mbed.org/platforms/ST-Discovery-L475E-IOT01A/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L475VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - ``disco_l476vg``
      - `ST 32L476GDISCOVERY <http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF261635?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L476VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - ``nucleo_f030r8``
      - `ST Nucleo F030R8 <https://developer.mbed.org/platforms/ST-Nucleo-F030R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - ``nucleo_f031k6``
      - `ST Nucleo F031K6 <https://developer.mbed.org/platforms/ST-Nucleo-F031K6/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F031K6T6
      - 48MHz
      - 32KB
      - 4KB
    * - ``nucleo_f042k6``
      - `ST Nucleo F042K6 <https://developer.mbed.org/platforms/ST-Nucleo-F042K6/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F042K6T6
      - 48MHz
      - 32KB
      - 6KB
    * - ``nucleo_f070rb``
      - `ST Nucleo F070RB <https://developer.mbed.org/platforms/ST-Nucleo-F070RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F070RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - ``nucleo_f072rb``
      - `ST Nucleo F072RB <https://developer.mbed.org/platforms/ST-Nucleo-F072RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F072RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - ``nucleo_f091rc``
      - `ST Nucleo F091RC <https://developer.mbed.org/platforms/ST-Nucleo-F091RC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F091RCT6
      - 48MHz
      - 256KB
      - 32KB
    * - ``nucleo_f103rb``
      - `ST Nucleo F103RB <https://developer.mbed.org/platforms/ST-Nucleo-F103RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``nucleo_f207zg``
      - `ST Nucleo F207ZG <https://developer.mbed.org/platforms/ST-Nucleo-F207ZG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F207ZGT6
      - 120MHz
      - 1MB
      - 128KB
    * - ``nucleo_f302r8``
      - `ST Nucleo F302R8 <https://developer.mbed.org/platforms/ST-Nucleo-F302R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F302R8T6
      - 72MHz
      - 64KB
      - 16KB
    * - ``nucleo_f303k8``
      - `ST Nucleo F303K8 <https://developer.mbed.org/platforms/ST-Nucleo-F303K8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F303K8T6
      - 72MHz
      - 64KB
      - 16KB
    * - ``nucleo_f303re``
      - `ST Nucleo F303RE <http://developer.mbed.org/platforms/ST-Nucleo-F303RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F303RET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``nucleo_f303ze``
      - `ST Nucleo F303ZE <https://developer.mbed.org/platforms/ST-Nucleo-F303ZE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F303ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``nucleo_f334r8``
      - `ST Nucleo F334R8 <https://developer.mbed.org/platforms/ST-Nucleo-F334R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F334R8T6
      - 72MHz
      - 64KB
      - 16KB
    * - ``nucleo_f401re``
      - `ST Nucleo F401RE <https://developer.mbed.org/platforms/ST-Nucleo-F401RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F401RET6
      - 84MHz
      - 512KB
      - 96KB
    * - ``nucleo_f410rb``
      - `ST Nucleo F410RB <https://developer.mbed.org/platforms/ST-Nucleo-F410RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F410RBT6
      - 100MHz
      - 128KB
      - 32KB
    * - ``nucleo_f411re``
      - `ST Nucleo F411RE <https://developer.mbed.org/platforms/ST-Nucleo-F411RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``nucleo_f412zg``
      - `ST Nucleo F412ZG <https://developer.mbed.org/platforms/ST-Nucleo-F411RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB
    * - ``nucleo_f413zh``
      - `ST Nucleo F413ZH <https://os.mbed.com/platforms/ST-Nucleo-F413ZH/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F413ZHT6
      - 100MHz
      - 512KB
      - 128KB
    * - ``nucleo_f429zi``
      - `ST Nucleo F429ZI <https://developer.mbed.org/platforms/ST-Nucleo-F429ZI/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F429ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - ``nucleo_f446re``
      - `ST Nucleo F446RE <https://developer.mbed.org/platforms/ST-Nucleo-F446RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB
    * - ``nucleo_f446ze``
      - `ST Nucleo F446ZE <https://developer.mbed.org/platforms/ST-Nucleo-F446ZE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F446ZET6
      - 180MHz
      - 512KB
      - 128KB
    * - ``nucleo_f746zg``
      - `ST Nucleo F746ZG <https://developer.mbed.org/platforms/ST-Nucleo-F446ZE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F746ZGT6
      - 216MHz
      - 1MB
      - 320KB
    * - ``nucleo_f767zi``
      - `ST Nucleo F767ZI <https://developer.mbed.org/platforms/ST-Nucleo-F767ZI/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F767ZIT6
      - 216MHz
      - 2MB
      - 512KB
    * - ``nucleo_l011k4``
      - `ST Nucleo L011K4 <https://developer.mbed.org/platforms/ST-Nucleo-L011K4/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L011K4T6
      - 32MHz
      - 16KB
      - 2KB
    * - ``nucleo_l031k6``
      - `ST Nucleo L031K6 <https://developer.mbed.org/platforms/ST-Nucleo-L031K6/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L031K6T6
      - 32MHz
      - 32KB
      - 8KB
    * - ``nucleo_l053r8``
      - `ST Nucleo L053R8 <https://developer.mbed.org/platforms/ST-Nucleo-L053R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L053R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - ``nucleo_l073rz``
      - `ST Nucleo L073RZ <https://developer.mbed.org/platforms/ST-Nucleo-L073RZ/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L073RZ
      - 32MHz
      - 192KB
      - 20KB
    * - ``nucleo_l152re``
      - `ST Nucleo L152RE <https://developer.mbed.org/platforms/ST-Nucleo-L152RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L152RET6
      - 32MHz
      - 512KB
      - 80KB
    * - ``nucleo_l432kc``
      - `ST Nucleo L432KC <https://developer.mbed.org/platforms/ST-Nucleo-L432KC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L432KCU6
      - 80MHz
      - 256KB
      - 64KB
    * - ``nucleo_l476rg``
      - `ST Nucleo L476RG <https://developer.mbed.org/platforms/ST-Nucleo-L476RG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L476RGT6
      - 80MHz
      - 1MB
      - 128KB
    * - ``nucleo_l496zg``
      - `ST Nucleo L496ZG <https://developer.mbed.org/platforms/ST-Nucleo-L476RG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L496ZGT6
      - 80MHz
      - 1MB
      - 128KB

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
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB
    * - ``seeedArchGPRS``
      - `Seeed Arch GPRS V2 <https://www.seeedstudio.com/Arch-GPRS-V2-p-2026.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - No
      - LPC11U37
      - 48MHz
      - 128KB
      - 10KB
    * - ``seeedArchLink``
      - `Seeed Arch Link <https://developer.mbed.org/platforms/Seeed-Arch-Link/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``seeedArchMax``
      - `Seeed Arch Max <https://developer.mbed.org/platforms/Seeed-Arch-Max/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB
    * - ``seeedArchPro``
      - `Seeed Arch Pro <https://developer.mbed.org/platforms/Seeeduino-Arch-Pro/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB
    * - ``seeedTinyBLE``
      - `Seeed Tiny BLE <http://developer.mbed.org/platforms/Seeed-Tiny-BLE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``xadow_m0``
      - `Seeed Xadow M0 <https://developer.mbed.org/platforms/Seeed-Xadow-M0/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - No
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB

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
      - :ref:`Yes <piodebug>`
      - STM32L152RC
      - 32MHz
      - 256KB
      - 32KB

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
      - :ref:`Yes <piodebug>`
      - EFM32GG990F1024
      - 48MHz
      - 1MB
      - 128KB
    * - ``efm32hg_stk3400``
      - `Silicon Labs SLSTK3400A USB-enabled (Happy Gecko) <https://developer.mbed.org/platforms/EFM32-Happy-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM32HG322F64
      - 24MHz
      - 64KB
      - 8KB
    * - ``efm32lg_stk3600``
      - `Silicon Labs EFM32LG-STK3600 (Leopard Gecko) <https://developer.mbed.org/platforms/EFM32-Leopard-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM32LG990F256
      - 48MHz
      - 256KB
      - 32KB
    * - ``efm32pg_stk3401``
      - `Silicon Labs SLSTK3401A (Pearl Gecko) <https://developer.mbed.org/platforms/EFM32-Pearl-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM32PG1B200F256
      - 40MHz
      - 256KB
      - 32KB
    * - ``efm32wg_stk3800``
      - `Silicon Labs EFM32WG-STK3800 (Wonder Gecko) <https://developer.mbed.org/platforms/EFM32-Wonder-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM32WG990F256
      - 48MHz
      - 256KB
      - 32KB
    * - ``efm32zg_stk3200``
      - `Silicon Labs EFM32ZG-STK3200 (Zero Gecko) <https://developer.mbed.org/platforms/EFM32-Zero-Gecko/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Silicon Labs EFM32 <platform_siliconlabsefm32>`
      - :ref:`Yes <piodebug>`
      - EFM32ZG222F32
      - 24MHz
      - 32KB
      - 4KB

Smeshlink
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
    * - ``xbed_lpc1768``
      - `Smeshlink xbed LPC1768 <https://developer.mbed.org/platforms/xbed-LPC1768/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - No
      - LPC1768
      - 96MHz
      - 512KB
      - 32KB

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
      - :ref:`Yes <piodebug>`
      - LPC11U24
      - 50MHz
      - 32KB
      - 8KB
    * - ``lpc1347``
      - `DipCortex M3 <https://developer.mbed.org/platforms/DipCortex-M3/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC1347
      - 72MHz
      - 64KB
      - 12KB

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
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - ``lpc1114fn28``
      - `Switch Science mbed LPC1114FN28 <https://developer.mbed.org/platforms/LPC1114FN28/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC1114FN28
      - 48MHz
      - 32KB
      - 4KB
    * - ``ssci824``
      - `Switch Science mbed LPC824 <https://developer.mbed.org/platforms/Switch-Science-mbed-LPC824/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
      - LPC824
      - 30MHz
      - 32KB
      - 8KB
    * - ``ty51822r3``
      - `Switch Science mbed TY51822r3 <https://developer.mbed.org/platforms/Switch-Science-mbed-TY51822r3/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

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
      - :ref:`Yes <piodebug>`
      - MK20DX256
      - 72MHz
      - 256KB
      - 64KB

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
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 128KB
      - 32KB

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
      - :ref:`Yes <piodebug>`
      - WIZNET7500
      - 48MHz
      - 128KB
      - 48KB
    * - ``wizwiki_w7500eco``
      - `WIZwiki-W7500ECO <https://developer.mbed.org/platforms/WIZwiki-W7500ECO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`WIZNet W7500 <platform_wiznet7500>`
      - :ref:`Yes <piodebug>`
      - WIZNET7500ECO
      - 48MHz
      - 128KB
      - 48KB
    * - ``wizwiki_w7500p``
      - `WIZwiki-W7500P <https://developer.mbed.org/platforms/WIZwiki-W7500P/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`WIZNet W7500 <platform_wiznet7500>`
      - :ref:`Yes <piodebug>`
      - WIZNET7500P
      - 48MHz
      - 128KB
      - 48KB

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
      - :ref:`Yes <piodebug>`
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
    * - ``mtb_ublox_odin_w2``
      - `u-blox ODIN-W2 <https://os.mbed.com/modules/u-blox-odin-w2/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
    * - ``ublox_c030_n211``
      - `u-blox C030-N211 IoT Starter Kit <https://os.mbed.com/platforms/ublox-C030-N211/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - ``ublox_c030_u201``
      - `u-blox C030-U201 IoT Starter Kit <https://os.mbed.com/platforms/ublox-C030-N211/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - ``ublox_evk_nina_b1``
      - `u-blox EVK-NINA-B1 <https://os.mbed.com/platforms/u-blox-EVK-NINA-B1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF52 <platform_nordicnrf52>`
      - :ref:`Yes <piodebug>`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - ``ublox_evk_odin_w2``
      - `u-blox EVK-ODIN-W2 <https://developer.mbed.org/platforms/ublox-EVK-ODIN-W2/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
    * - ``ubloxc027``
      - `u-blox C027 <https://developer.mbed.org/platforms/u-blox-C027/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`NXP LPC <platform_nxplpc>`
      - :ref:`Yes <piodebug>`
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
      - :ref:`Yes <piodebug>`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
    * - ``nrf51822_y5_mbug``
      - `y5 nRF51822 mbug <https://developer.mbed.org/platforms/Y5-NRF51822-MBUG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Nordic nRF51 <platform_nordicnrf51>`
      - :ref:`Yes <piodebug>`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
