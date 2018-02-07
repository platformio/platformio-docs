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

.. _platform_ststm32:

ST STM32
========
:ref:`projectconf_env_platform` = ``ststm32``

The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

For more detailed information please visit `vendor site <http://www.st.com/web/en/catalog/mmc/FM141/SC1169?sc=stm32&utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: ststm32_extra.rst

Examples
--------

Examples are listed from `ST STM32 development platform repository <https://github.com/platformio/platform-ststm32/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_:

* `arduino-blink <https://github.com/platformio/platform-ststm32/tree/develop/examples/arduino-blink?utm_source=platformio&utm_medium=docs>`_
* `arduino-external-libs <https://github.com/platformio/platform-ststm32/tree/develop/examples/arduino-external-libs?utm_source=platformio&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-ststm32/tree/develop/examples/arduino-internal-libs?utm_source=platformio&utm_medium=docs>`_
* `arduino-mxchip-azureiot <https://github.com/platformio/platform-ststm32/tree/develop/examples/arduino-mxchip-azureiot?utm_source=platformio&utm_medium=docs>`_
* `arduino-mxchip-filesystem <https://github.com/platformio/platform-ststm32/tree/develop/examples/arduino-mxchip-filesystem?utm_source=platformio&utm_medium=docs>`_
* `arduino-mxchip-sensors <https://github.com/platformio/platform-ststm32/tree/develop/examples/arduino-mxchip-sensors?utm_source=platformio&utm_medium=docs>`_
* `arduino-mxchip-wifiscan <https://github.com/platformio/platform-ststm32/tree/develop/examples/arduino-mxchip-wifiscan?utm_source=platformio&utm_medium=docs>`_
* `cmsis-blink <https://github.com/platformio/platform-ststm32/tree/develop/examples/cmsis-blink?utm_source=platformio&utm_medium=docs>`_
* `libopencm3-blink <https://github.com/platformio/platform-ststm32/tree/develop/examples/libopencm3-blink?utm_source=platformio&utm_medium=docs>`_
* `mbed-blink <https://github.com/platformio/platform-ststm32/tree/develop/examples/mbed-blink?utm_source=platformio&utm_medium=docs>`_
* `mbed-dsp <https://github.com/platformio/platform-ststm32/tree/develop/examples/mbed-dsp?utm_source=platformio&utm_medium=docs>`_
* `mbed-events <https://github.com/platformio/platform-ststm32/tree/develop/examples/mbed-events?utm_source=platformio&utm_medium=docs>`_
* `mbed-filesystem <https://github.com/platformio/platform-ststm32/tree/develop/examples/mbed-filesystem?utm_source=platformio&utm_medium=docs>`_
* `mbed-rtos <https://github.com/platformio/platform-ststm32/tree/develop/examples/mbed-rtos?utm_source=platformio&utm_medium=docs>`_
* `mbed-rtos-ethernet <https://github.com/platformio/platform-ststm32/tree/develop/examples/mbed-rtos-ethernet?utm_source=platformio&utm_medium=docs>`_
* `mbed-rtos-ethernet-tls <https://github.com/platformio/platform-ststm32/tree/develop/examples/mbed-rtos-ethernet-tls?utm_source=platformio&utm_medium=docs>`_
* `mbed-rtos-semaphore <https://github.com/platformio/platform-ststm32/tree/develop/examples/mbed-rtos-semaphore?utm_source=platformio&utm_medium=docs>`_
* `mbed-serial <https://github.com/platformio/platform-ststm32/tree/develop/examples/mbed-serial?utm_source=platformio&utm_medium=docs>`_
* `spl-blink <https://github.com/platformio/platform-ststm32/tree/develop/examples/spl-blink?utm_source=platformio&utm_medium=docs>`_
* `stm32cube-hal-blink <https://github.com/platformio/platform-ststm32/tree/develop/examples/stm32cube-hal-blink?utm_source=platformio&utm_medium=docs>`_
* `stm32cube-ll-blink <https://github.com/platformio/platform-ststm32/tree/develop/examples/stm32cube-ll-blink?utm_source=platformio&utm_medium=docs>`_

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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``armstrap_eagle1024``
      - `Armstrap Eagle 1024 <http://docs.armstrap.org/en/latest/hardware-overview.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F417VGT6
      - 168MHz
      - 1MB
      - 192KB
    * - ``armstrap_eagle2048``
      - `Armstrap Eagle 2048 <http://docs.armstrap.org/en/latest/hardware-overview.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F427VIT6
      - 168MHz
      - 1.99MB
      - 256KB
    * - ``armstrap_eagle512``
      - `Armstrap Eagle 512 <http://docs.armstrap.org/en/latest/hardware-overview.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB
    * - ``b96b_f446ve``
      - `96Boards B96B-F446VE <https://developer.mbed.org/platforms/ST-B96B-F446VE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F446VET6
      - 168MHz
      - 512KB
      - 128KB
    * - ``cloud_jam``
      - `RushUp Cloud-JAM <https://developer.mbed.org/platforms/ST-Nucleo-F401RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F401RET6
      - 84MHz
      - 512KB
      - 96KB
    * - ``cloud_jam_l4``
      - `RushUp Cloud-JAM L4 <https://developer.mbed.org/platforms/ST-Nucleo-L476RG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32L476RGT6
      - 80MHz
      - 1MB
      - 128KB
    * - ``disco_f030r8``
      - `ST STM32F0308DISCOVERY <http://www.st.com/en/evaluation-tools/32f0308discovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (on-board)
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - ``disco_f051r8``
      - `ST STM32F0DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF253215?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (on-board)
      - STM32F051R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - ``disco_f100rb``
      - `ST STM32VLDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF250863?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v1` (on-board)
      - STM32F100RBT6
      - 24MHz
      - 128KB
      - 8KB
    * - ``disco_f303vc``
      - `ST STM32F3DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF254044?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (on-board)
      - STM32F303VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``disco_f334c8``
      - `ST 32F3348DISCOVERY <http://www.st.com/web/en/catalog/tools/PF260318?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F334C8T6
      - 72MHz
      - 64KB
      - 12KB
    * - ``disco_f401vc``
      - `ST 32F401CDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF259098?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (on-board)
      - STM32F401VCT6
      - 84MHz
      - 256KB
      - 64KB
    * - ``disco_f407vg``
      - `ST STM32F4DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF252419?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (on-board)
      - STM32F407VGT6
      - 168MHz
      - 1MB
      - 128KB
    * - ``disco_f411ve``
      - `ST 32F411EDISCOVERY <http://www.st.com/en/evaluation-tools/32f411ediscovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F411VET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``disco_f413zh``
      - `ST 32F413HDISCOVERY <https://os.mbed.com/platforms/ST-Discovery-F413H/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F413ZHT6
      - 100MHz
      - 512KB
      - 128KB
    * - ``disco_f429zi``
      - `ST 32F429IDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF259090?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (on-board)
      - STM32F429ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - ``disco_f469ni``
      - `ST 32F469IDISCOVERY <http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF262395?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (on-board)
      - STM32F469NIH6
      - 180MHz
      - 1MB
      - 384KB
    * - ``disco_f746ng``
      - `ST 32F746GDISCOVERY <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/32f746gdiscovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F746NGH6
      - 216MHz
      - 1MB
      - 320KB
    * - ``disco_f769ni``
      - `ST 32F769IDISCOVERY <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/32f769idiscovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F769NIH6
      - 80MHz
      - 1MB
      - 512KB
    * - ``disco_l053c8``
      - `ST 32L0538DISCOVERY <http://www.st.com/web/en/catalog/tools/PF260319?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32L053C8T6
      - 32MHz
      - 64KB
      - 8KB
    * - ``disco_l072cz_lrwan1``
      - `ST DISCO-L072CZ-LRWAN1 <https://developer.mbed.org/platforms/ST-Discovery-LRWAN1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32L072CZ
      - 32MHz
      - 192KB
      - 20KB
    * - ``disco_l152rb``
      - `ST STM32LDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF258515?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32L152RBT6
      - 32MHz
      - 128KB
      - 16KB
    * - ``disco_l475vg_iot01a``
      - `ST DISCO-L475VG-IOT01A <https://developer.mbed.org/platforms/ST-Discovery-L475E-IOT01A/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32L475VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - ``disco_l476vg``
      - `ST 32L476GDISCOVERY <http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF261635?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32L476VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - ``eval_l073z``
      - `ST STM32L073Z-EVAL <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-eval-boards/stm32l073z-eval.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board), :ref:`debugging_tool_jlink`
      - STM32L073VZT6
      - 32MHz
      - 192KB
      - 20KB
    * - ``mxchip_az3166``
      - `Microsoft Azure IoT Development Kit (MXChip AZ3166) <https://microsoft.github.io/azure-iot-developer-kit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB
    * - ``nucleo_f030r8``
      - `ST Nucleo F030R8 <https://developer.mbed.org/platforms/ST-Nucleo-F030R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - ``nucleo_f031k6``
      - `ST Nucleo F031K6 <https://developer.mbed.org/platforms/ST-Nucleo-F031K6/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F031K6T6
      - 48MHz
      - 32KB
      - 4KB
    * - ``nucleo_f042k6``
      - `ST Nucleo F042K6 <https://developer.mbed.org/platforms/ST-Nucleo-F042K6/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F042K6T6
      - 48MHz
      - 32KB
      - 6KB
    * - ``nucleo_f070rb``
      - `ST Nucleo F070RB <https://developer.mbed.org/platforms/ST-Nucleo-F070RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F070RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - ``nucleo_f072rb``
      - `ST Nucleo F072RB <https://developer.mbed.org/platforms/ST-Nucleo-F072RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F072RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - ``nucleo_f091rc``
      - `ST Nucleo F091RC <https://developer.mbed.org/platforms/ST-Nucleo-F091RC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F091RCT6
      - 48MHz
      - 256KB
      - 32KB
    * - ``nucleo_f103rb``
      - `ST Nucleo F103RB <https://developer.mbed.org/platforms/ST-Nucleo-F103RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``nucleo_f207zg``
      - `ST Nucleo F207ZG <https://developer.mbed.org/platforms/ST-Nucleo-F207ZG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F207ZGT6
      - 120MHz
      - 1MB
      - 128KB
    * - ``nucleo_f302r8``
      - `ST Nucleo F302R8 <https://developer.mbed.org/platforms/ST-Nucleo-F302R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F302R8T6
      - 72MHz
      - 64KB
      - 16KB
    * - ``nucleo_f303k8``
      - `ST Nucleo F303K8 <https://developer.mbed.org/platforms/ST-Nucleo-F303K8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F303K8T6
      - 72MHz
      - 64KB
      - 16KB
    * - ``nucleo_f303re``
      - `ST Nucleo F303RE <http://developer.mbed.org/platforms/ST-Nucleo-F303RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F303RET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``nucleo_f303ze``
      - `ST Nucleo F303ZE <https://developer.mbed.org/platforms/ST-Nucleo-F303ZE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F303ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``nucleo_f334r8``
      - `ST Nucleo F334R8 <https://developer.mbed.org/platforms/ST-Nucleo-F334R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F334R8T6
      - 72MHz
      - 64KB
      - 16KB
    * - ``nucleo_f401re``
      - `ST Nucleo F401RE <https://developer.mbed.org/platforms/ST-Nucleo-F401RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F401RET6
      - 84MHz
      - 512KB
      - 96KB
    * - ``nucleo_f410rb``
      - `ST Nucleo F410RB <https://developer.mbed.org/platforms/ST-Nucleo-F410RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F410RBT6
      - 100MHz
      - 128KB
      - 32KB
    * - ``nucleo_f411re``
      - `ST Nucleo F411RE <https://developer.mbed.org/platforms/ST-Nucleo-F411RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``nucleo_f412zg``
      - `ST Nucleo F412ZG <https://developer.mbed.org/platforms/ST-Nucleo-F411RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB
    * - ``nucleo_f429zi``
      - `ST Nucleo F429ZI <https://developer.mbed.org/platforms/ST-Nucleo-F429ZI/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F429ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - ``nucleo_f446re``
      - `ST Nucleo F446RE <https://developer.mbed.org/platforms/ST-Nucleo-F446RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB
    * - ``nucleo_f446ze``
      - `ST Nucleo F446ZE <https://developer.mbed.org/platforms/ST-Nucleo-F446ZE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F446ZET6
      - 180MHz
      - 512KB
      - 128KB
    * - ``nucleo_f746zg``
      - `ST Nucleo F746ZG <https://developer.mbed.org/platforms/ST-Nucleo-F446ZE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F746ZGT6
      - 216MHz
      - 1MB
      - 320KB
    * - ``nucleo_f767zi``
      - `ST Nucleo F767ZI <https://developer.mbed.org/platforms/ST-Nucleo-F767ZI/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F767ZIT6
      - 216MHz
      - 2MB
      - 512KB
    * - ``nucleo_l011k4``
      - `ST Nucleo L011K4 <https://developer.mbed.org/platforms/ST-Nucleo-L011K4/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32L011K4T6
      - 32MHz
      - 16KB
      - 2KB
    * - ``nucleo_l031k6``
      - `ST Nucleo L031K6 <https://developer.mbed.org/platforms/ST-Nucleo-L031K6/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32L031K6T6
      - 32MHz
      - 32KB
      - 8KB
    * - ``nucleo_l053r8``
      - `ST Nucleo L053R8 <https://developer.mbed.org/platforms/ST-Nucleo-L053R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32L053R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - ``nucleo_l073rz``
      - `ST Nucleo L073RZ <https://developer.mbed.org/platforms/ST-Nucleo-L073RZ/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32L073RZ
      - 32MHz
      - 192KB
      - 20KB
    * - ``nucleo_l152re``
      - `ST Nucleo L152RE <https://developer.mbed.org/platforms/ST-Nucleo-L152RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32L152RET6
      - 32MHz
      - 512KB
      - 80KB
    * - ``nucleo_l432kc``
      - `ST Nucleo L432KC <https://developer.mbed.org/platforms/ST-Nucleo-L432KC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32L432KCU6
      - 80MHz
      - 256KB
      - 64KB
    * - ``nucleo_l476rg``
      - `ST Nucleo L476RG <https://developer.mbed.org/platforms/ST-Nucleo-L476RG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32L476RGT6
      - 80MHz
      - 1MB
      - 128KB
    * - ``seeedArchMax``
      - `Seeed Arch Max <https://developer.mbed.org/platforms/Seeed-Arch-Max/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1` (on-board)
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB


External tools
~~~~~~~~~~~~~~

Boards listed below are compatible with :ref:`piodebug` but depend on external
debugging tools. See "Debug" column for compatible debugging tools.


.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``1bitsy_stm32f415rgt``
      - `1Bitsy <http://1bitsy.org?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic` (default)
      - STM32F415RGT
      - 168MHz
      - 1MB
      - 128KB
    * - ``bluepill_f103c8``
      - `BluePill F103C8 <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``elmo_f411re``
      - `Espotel LoRa Module <https://developer.mbed.org/platforms/Espotel-ELMO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``genericSTM32F103C8``
      - `STM32F103C8 (20k RAM. 64k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``genericSTM32F103CB``
      - `STM32F103CB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103cb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103CBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``genericSTM32F103R8``
      - `STM32F103R8 (20k RAM. 64 Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103r8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103R8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``genericSTM32F103RB``
      - `STM32F103RB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``genericSTM32F103RC``
      - `STM32F103RC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rc.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103RCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``genericSTM32F103RE``
      - `STM32F103RE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103re.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103RET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``genericSTM32F103VC``
      - `STM32F103VC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``genericSTM32F103VE``
      - `STM32F103VE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2` (default), :ref:`debugging_tool_stlink-v2-1`
      - STM32F103VET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``maple``
      - `Maple <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`
      - STM32F103RBT6
      - 72MHz
      - 108KB
      - 17KB
    * - ``maple_mini_b20``
      - `Maple Mini Bootloader 2.0 <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`
      - STM32F103CBT6
      - 72MHz
      - 120KB
      - 20KB
    * - ``maple_mini_origin``
      - `Maple Mini Original <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`
      - STM32F103CBT6
      - 72MHz
      - 108KB
      - 17KB
    * - ``mote_l152rc``
      - `NAMote72 <https://developer.mbed.org/platforms/NAMote-72/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1`
      - STM32L152RC
      - 32MHz
      - 256KB
      - 32KB
    * - ``mts_dragonfly_f411re``
      - `MTS Dragonfly <https://developer.mbed.org/platforms/MTS-Dragonfly/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``mts_mdot_f405rg``
      - `MultiTech mDot <https://developer.mbed.org/platforms/MTS-mDot-F411/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``mts_mdot_f411re``
      - `MultiTech mDot F411 <https://developer.mbed.org/platforms/MTS-mDot-F411/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``ublox_c030_n211``
      - `u-blox C030-N211 IoT Starter Kit <https://os.mbed.com/platforms/ublox-C030-N211/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1`
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - ``ublox_c030_u201``
      - `u-blox C030-U201 IoT Starter Kit <https://os.mbed.com/platforms/ublox-C030-N211/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1`
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - ``ublox_evk_odin_w2``
      - `u-blox EVK-ODIN-W2 <https://developer.mbed.org/platforms/ublox-EVK-ODIN-W2/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`, :ref:`debugging_tool_stlink-v2-1`
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
    * - ``xdot_l151cc``
      - `MultiTech xDot <https://developer.mbed.org/platforms/MTS-xDot-L151CC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_blackmagic`
      - STM32L151CCU6
      - 32MHz
      - 256KB
      - 32KB


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinostm32mxchip <https://microsoft.github.io/azure-iot-developer-kit/?utm_source=platformio&utm_medium=docs>`__
      - Arduino Wiring-based Framework (ST STM32 MXChip Core)

    * - `framework-arduinoststm32 <https://github.com/rogerclarkmelbourne/Arduino_STM32?utm_source=platformio&utm_medium=docs>`__
      - Arduino Wiring-based Framework (STM32 Core)

    * - `framework-cmsis <http://www.arm.com/products/processors/cortex-m/cortex-microcontroller-software-interface-standard.php?utm_source=platformio&utm_medium=docs>`__
      - Vendor-independent hardware abstraction layer for the Cortex-M processor series

    * - `framework-libopencm3 <http://www.libopencm3.org/?utm_source=platformio&utm_medium=docs>`__
      - libOpenCM3 Framework

    * - `framework-mbed <http://mbed.org?utm_source=platformio&utm_medium=docs>`__
      - mbed Framework

    * - `framework-spl <http://www.st.com/web/catalog/tools/FM147/CL1794/SC961/SS1743/PF257890?utm_source=platformio&utm_medium=docs>`__
      - Standard Peripheral Library for STM32 MCUs

    * - `framework-stm32cube <http://www.st.com/en/embedded-software/stm32cube-embedded-software.html?querycriteria=productId=LN1897&utm_source=platformio&utm_medium=docs>`__
      - STM32Cube embedded software libraries

    * - `tool-openocd <http://openocd.org?utm_source=platformio&utm_medium=docs>`__
      - OpenOCD

    * - `tool-stlink <https://github.com/texane/stlink?utm_source=platformio&utm_medium=docs>`__
      - ST-Link

    * - `tool-stm32duino <https://github.com/rogerclarkmelbourne/Arduino_STM32?utm_source=platformio&utm_medium=docs>`__
      - STM32Duino Tools

    * - `toolchain-gccarmnoneeabi <https://launchpad.net/gcc-arm-embedded?utm_source=platformio&utm_medium=docs>`__
      - gcc-arm-embedded

.. warning::
    **Linux Users**:

        * Install "udev" rules file `99-platformio-udev.rules <https://github.com/platformio/platformio-core/blob/develop/scripts/99-platformio-udev.rules>`_
          (an instruction is located inside a file).
        * Raspberry Pi users, please read this article
          `Enable serial port on Raspberry Pi <https://hallard.me/enable-serial-port-on-raspberry-pi/>`__.


    **Windows Users:**

        Please check that you have a correctly installed USB driver from board
        manufacturer


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

    * - :ref:`framework_spl`
      - The ST Standard Peripheral Library provides a set of functions for handling the peripherals on the STM32 Cortex-M3 family. The idea is to save the user (the new user, in particular) having to deal directly with the registers.

    * - :ref:`framework_stm32cube`
      - STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

1BitSquared
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``1bitsy_stm32f415rgt``
      - `1Bitsy <http://1bitsy.org?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``b96b_f446ve``
      - `96Boards B96B-F446VE <https://developer.mbed.org/platforms/ST-B96B-F446VE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F446VET6
      - 168MHz
      - 512KB
      - 128KB

Armstrap
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``armstrap_eagle1024``
      - `Armstrap Eagle 1024 <http://docs.armstrap.org/en/latest/hardware-overview.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F417VGT6
      - 168MHz
      - 1MB
      - 192KB
    * - ``armstrap_eagle2048``
      - `Armstrap Eagle 2048 <http://docs.armstrap.org/en/latest/hardware-overview.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F427VIT6
      - 168MHz
      - 1.99MB
      - 256KB
    * - ``armstrap_eagle512``
      - `Armstrap Eagle 512 <http://docs.armstrap.org/en/latest/hardware-overview.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB

Espotel
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``elmo_f411re``
      - `Espotel LoRa Module <https://developer.mbed.org/platforms/Espotel-ELMO/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB

Generic
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``bluepill_f103c8``
      - `BluePill F103C8 <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``genericSTM32F103C8``
      - `STM32F103C8 (20k RAM. 64k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``genericSTM32F103CB``
      - `STM32F103CB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103cb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F103CBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``genericSTM32F103R8``
      - `STM32F103R8 (20k RAM. 64 Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103r8.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F103R8T6
      - 72MHz
      - 64KB
      - 20KB
    * - ``genericSTM32F103RB``
      - `STM32F103RB (20k RAM. 128k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rb.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``genericSTM32F103RC``
      - `STM32F103RC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103rc.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F103RCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``genericSTM32F103RE``
      - `STM32F103RE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103re.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F103RET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``genericSTM32F103VC``
      - `STM32F103VC (48k RAM. 256k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F103VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``genericSTM32F103VE``
      - `STM32F103VE (64k RAM. 512k Flash) <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103ve.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F103VET6
      - 72MHz
      - 512KB
      - 64KB

LeafLabs
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``maple``
      - `Maple <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F103RBT6
      - 72MHz
      - 108KB
      - 17KB
    * - ``maple_mini_b20``
      - `Maple Mini Bootloader 2.0 <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F103CBT6
      - 72MHz
      - 120KB
      - 20KB
    * - ``maple_mini_origin``
      - `Maple Mini Original <http://www.leaflabs.com/maple/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F103CBT6
      - 72MHz
      - 108KB
      - 17KB

MXChip
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``mxchip_az3166``
      - `Microsoft Azure IoT Development Kit (MXChip AZ3166) <https://microsoft.github.io/azure-iot-developer-kit/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB

MultiTech
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``mts_dragonfly_f411re``
      - `MTS Dragonfly <https://developer.mbed.org/platforms/MTS-Dragonfly/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``mts_mdot_f405rg``
      - `MultiTech mDot <https://developer.mbed.org/platforms/MTS-mDot-F411/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``mts_mdot_f411re``
      - `MultiTech mDot F411 <https://developer.mbed.org/platforms/MTS-mDot-F411/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``xdot_l151cc``
      - `MultiTech xDot <https://developer.mbed.org/platforms/MTS-xDot-L151CC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32L151CCU6
      - 32MHz
      - 256KB
      - 32KB

RushUp
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``cloud_jam``
      - `RushUp Cloud-JAM <https://developer.mbed.org/platforms/ST-Nucleo-F401RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F401RET6
      - 84MHz
      - 512KB
      - 96KB
    * - ``cloud_jam_l4``
      - `RushUp Cloud-JAM L4 <https://developer.mbed.org/platforms/ST-Nucleo-L476RG/?utm_source=platformio&utm_medium=docs>`_
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``disco_f030r8``
      - `ST STM32F0308DISCOVERY <http://www.st.com/en/evaluation-tools/32f0308discovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - ``disco_f051r8``
      - `ST STM32F0DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF253215?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F051R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - ``disco_f100rb``
      - `ST STM32VLDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF250863?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F100RBT6
      - 24MHz
      - 128KB
      - 8KB
    * - ``disco_f303vc``
      - `ST STM32F3DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF254044?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F303VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - ``disco_f334c8``
      - `ST 32F3348DISCOVERY <http://www.st.com/web/en/catalog/tools/PF260318?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F334C8T6
      - 72MHz
      - 64KB
      - 12KB
    * - ``disco_f401vc``
      - `ST 32F401CDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF259098?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F401VCT6
      - 84MHz
      - 256KB
      - 64KB
    * - ``disco_f407vg``
      - `ST STM32F4DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF252419?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F407VGT6
      - 168MHz
      - 1MB
      - 128KB
    * - ``disco_f411ve``
      - `ST 32F411EDISCOVERY <http://www.st.com/en/evaluation-tools/32f411ediscovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F411VET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``disco_f413zh``
      - `ST 32F413HDISCOVERY <https://os.mbed.com/platforms/ST-Discovery-F413H/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F413ZHT6
      - 100MHz
      - 512KB
      - 128KB
    * - ``disco_f429zi``
      - `ST 32F429IDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF259090?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F429ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - ``disco_f469ni``
      - `ST 32F469IDISCOVERY <http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF262395?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F469NIH6
      - 180MHz
      - 1MB
      - 384KB
    * - ``disco_f746ng``
      - `ST 32F746GDISCOVERY <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/32f746gdiscovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F746NGH6
      - 216MHz
      - 1MB
      - 320KB
    * - ``disco_f769ni``
      - `ST 32F769IDISCOVERY <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/32f769idiscovery.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F769NIH6
      - 80MHz
      - 1MB
      - 512KB
    * - ``disco_l053c8``
      - `ST 32L0538DISCOVERY <http://www.st.com/web/en/catalog/tools/PF260319?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32L053C8T6
      - 32MHz
      - 64KB
      - 8KB
    * - ``disco_l072cz_lrwan1``
      - `ST DISCO-L072CZ-LRWAN1 <https://developer.mbed.org/platforms/ST-Discovery-LRWAN1/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32L072CZ
      - 32MHz
      - 192KB
      - 20KB
    * - ``disco_l152rb``
      - `ST STM32LDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF258515?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32L152RBT6
      - 32MHz
      - 128KB
      - 16KB
    * - ``disco_l475vg_iot01a``
      - `ST DISCO-L475VG-IOT01A <https://developer.mbed.org/platforms/ST-Discovery-L475E-IOT01A/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32L475VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - ``disco_l476vg``
      - `ST 32L476GDISCOVERY <http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF261635?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32L476VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - ``eval_l073z``
      - `ST STM32L073Z-EVAL <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-eval-boards/stm32l073z-eval.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32L073VZT6
      - 32MHz
      - 192KB
      - 20KB
    * - ``nucleo_f030r8``
      - `ST Nucleo F030R8 <https://developer.mbed.org/platforms/ST-Nucleo-F030R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - ``nucleo_f031k6``
      - `ST Nucleo F031K6 <https://developer.mbed.org/platforms/ST-Nucleo-F031K6/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F031K6T6
      - 48MHz
      - 32KB
      - 4KB
    * - ``nucleo_f042k6``
      - `ST Nucleo F042K6 <https://developer.mbed.org/platforms/ST-Nucleo-F042K6/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F042K6T6
      - 48MHz
      - 32KB
      - 6KB
    * - ``nucleo_f070rb``
      - `ST Nucleo F070RB <https://developer.mbed.org/platforms/ST-Nucleo-F070RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F070RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - ``nucleo_f072rb``
      - `ST Nucleo F072RB <https://developer.mbed.org/platforms/ST-Nucleo-F072RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F072RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - ``nucleo_f091rc``
      - `ST Nucleo F091RC <https://developer.mbed.org/platforms/ST-Nucleo-F091RC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F091RCT6
      - 48MHz
      - 256KB
      - 32KB
    * - ``nucleo_f103rb``
      - `ST Nucleo F103RB <https://developer.mbed.org/platforms/ST-Nucleo-F103RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - ``nucleo_f207zg``
      - `ST Nucleo F207ZG <https://developer.mbed.org/platforms/ST-Nucleo-F207ZG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F207ZGT6
      - 120MHz
      - 1MB
      - 128KB
    * - ``nucleo_f302r8``
      - `ST Nucleo F302R8 <https://developer.mbed.org/platforms/ST-Nucleo-F302R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F302R8T6
      - 72MHz
      - 64KB
      - 16KB
    * - ``nucleo_f303k8``
      - `ST Nucleo F303K8 <https://developer.mbed.org/platforms/ST-Nucleo-F303K8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F303K8T6
      - 72MHz
      - 64KB
      - 16KB
    * - ``nucleo_f303re``
      - `ST Nucleo F303RE <http://developer.mbed.org/platforms/ST-Nucleo-F303RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F303RET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``nucleo_f303ze``
      - `ST Nucleo F303ZE <https://developer.mbed.org/platforms/ST-Nucleo-F303ZE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F303ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - ``nucleo_f334r8``
      - `ST Nucleo F334R8 <https://developer.mbed.org/platforms/ST-Nucleo-F334R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F334R8T6
      - 72MHz
      - 64KB
      - 16KB
    * - ``nucleo_f401re``
      - `ST Nucleo F401RE <https://developer.mbed.org/platforms/ST-Nucleo-F401RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F401RET6
      - 84MHz
      - 512KB
      - 96KB
    * - ``nucleo_f410rb``
      - `ST Nucleo F410RB <https://developer.mbed.org/platforms/ST-Nucleo-F410RB/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F410RBT6
      - 100MHz
      - 128KB
      - 32KB
    * - ``nucleo_f411re``
      - `ST Nucleo F411RE <https://developer.mbed.org/platforms/ST-Nucleo-F411RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - ``nucleo_f412zg``
      - `ST Nucleo F412ZG <https://developer.mbed.org/platforms/ST-Nucleo-F411RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB
    * - ``nucleo_f429zi``
      - `ST Nucleo F429ZI <https://developer.mbed.org/platforms/ST-Nucleo-F429ZI/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F429ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - ``nucleo_f446re``
      - `ST Nucleo F446RE <https://developer.mbed.org/platforms/ST-Nucleo-F446RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB
    * - ``nucleo_f446ze``
      - `ST Nucleo F446ZE <https://developer.mbed.org/platforms/ST-Nucleo-F446ZE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F446ZET6
      - 180MHz
      - 512KB
      - 128KB
    * - ``nucleo_f746zg``
      - `ST Nucleo F746ZG <https://developer.mbed.org/platforms/ST-Nucleo-F446ZE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F746ZGT6
      - 216MHz
      - 1MB
      - 320KB
    * - ``nucleo_f767zi``
      - `ST Nucleo F767ZI <https://developer.mbed.org/platforms/ST-Nucleo-F767ZI/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F767ZIT6
      - 216MHz
      - 2MB
      - 512KB
    * - ``nucleo_l011k4``
      - `ST Nucleo L011K4 <https://developer.mbed.org/platforms/ST-Nucleo-L011K4/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32L011K4T6
      - 32MHz
      - 16KB
      - 2KB
    * - ``nucleo_l031k6``
      - `ST Nucleo L031K6 <https://developer.mbed.org/platforms/ST-Nucleo-L031K6/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32L031K6T6
      - 32MHz
      - 32KB
      - 8KB
    * - ``nucleo_l053r8``
      - `ST Nucleo L053R8 <https://developer.mbed.org/platforms/ST-Nucleo-L053R8/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32L053R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - ``nucleo_l073rz``
      - `ST Nucleo L073RZ <https://developer.mbed.org/platforms/ST-Nucleo-L073RZ/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32L073RZ
      - 32MHz
      - 192KB
      - 20KB
    * - ``nucleo_l152re``
      - `ST Nucleo L152RE <https://developer.mbed.org/platforms/ST-Nucleo-L152RE/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32L152RET6
      - 32MHz
      - 512KB
      - 80KB
    * - ``nucleo_l432kc``
      - `ST Nucleo L432KC <https://developer.mbed.org/platforms/ST-Nucleo-L432KC/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32L432KCU6
      - 80MHz
      - 256KB
      - 64KB
    * - ``nucleo_l476rg``
      - `ST Nucleo L476RG <https://developer.mbed.org/platforms/ST-Nucleo-L476RG/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32L476RGT6
      - 80MHz
      - 1MB
      - 128KB

SeeedStudio
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``seeedArchMax``
      - `Seeed Arch Max <https://developer.mbed.org/platforms/Seeed-Arch-Max/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB

Semtech
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``mote_l152rc``
      - `NAMote72 <https://developer.mbed.org/platforms/NAMote-72/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32L152RC
      - 32MHz
      - 256KB
      - 32KB

u-blox
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``ublox_c030_n211``
      - `u-blox C030-N211 IoT Starter Kit <https://os.mbed.com/platforms/ublox-C030-N211/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - ``ublox_c030_u201``
      - `u-blox C030-U201 IoT Starter Kit <https://os.mbed.com/platforms/ublox-C030-N211/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - ``ublox_evk_odin_w2``
      - `u-blox EVK-ODIN-W2 <https://developer.mbed.org/platforms/ublox-EVK-ODIN-W2/?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
