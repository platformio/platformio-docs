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

.. _framework_stm32cube:

STM32Cube
=========
:ref:`projectconf_env_framework` = ``stm32cube``

STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency.

For more detailed information please visit `vendor site <http://www.st.com/en/embedded-software/stm32cube-embedded-software.html?querycriteria=productId=LN1897>`_.


.. contents:: Contents
    :local:

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_ststm32`
      - The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by horizontal.

96Boards
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``b96b_f446ve``
      - `96Boards B96B-F446VE <https://developer.mbed.org/platforms/ST-B96B-F446VE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F446VET6
      - 168 MHz
      - 512 Kb
      - 128 Kb

Armstrap
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``armstrap_eagle1024``
      - `Armstrap Eagle 1024 <http://docs.armstrap.org/en/latest/hardware-overview.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F417VGT6
      - 168 MHz
      - 1024 Kb
      - 192 Kb

    * - ``armstrap_eagle2048``
      - `Armstrap Eagle 2048 <http://docs.armstrap.org/en/latest/hardware-overview.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F427VIT6
      - 168 MHz
      - 2048 Kb
      - 256 Kb

    * - ``armstrap_eagle512``
      - `Armstrap Eagle 512 <http://docs.armstrap.org/en/latest/hardware-overview.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F407VET6
      - 168 MHz
      - 512 Kb
      - 192 Kb

Espotel
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``elmo_f411re``
      - `Espotel LoRa Module <https://developer.mbed.org/platforms/Espotel-ELMO/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100 MHz
      - 512 Kb
      - 128 Kb

Generic
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``bluepill_f103c8``
      - `BluePill F103C8 <http://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32f1-series/stm32f103/stm32f103c8.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103C8T6
      - 72 MHz
      - 64 Kb
      - 20 Kb

MultiTech
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``xdot_l151cc``
      - `MultiTech xDot <https://developer.mbed.org/platforms/MTS-xDot-L151CC/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      -
      - STM32L151CCU6
      - 32 MHz
      - 256 Kb
      - 32 Kb

ST
~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``disco_f030r8``
      - `ST STM32F0308DISCOVERY <http://www.st.com/en/evaluation-tools/32f0308discovery.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F030R8T6
      - 48 MHz
      - 64 Kb
      - 8 Kb

    * - ``disco_f051r8``
      - `ST STM32F0DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF253215>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F051R8T6
      - 48 MHz
      - 64 Kb
      - 8 Kb

    * - ``disco_f100rb``
      - `ST STM32VLDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF250863>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F100RBT6
      - 24 MHz
      - 128 Kb
      - 8 Kb

    * - ``disco_f303vc``
      - `ST STM32F3DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF254044>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F303VCT6
      - 72 MHz
      - 256 Kb
      - 48 Kb

    * - ``disco_f334c8``
      - `ST 32F3348DISCOVERY <http://www.st.com/web/en/catalog/tools/PF260318>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F334C8T6
      - 72 MHz
      - 64 Kb
      - 12 Kb

    * - ``disco_f401vc``
      - `ST 32F401CDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF259098>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F401VCT6
      - 84 MHz
      - 256 Kb
      - 64 Kb

    * - ``disco_f407vg``
      - `ST STM32F4DISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF252419>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F407VGT6
      - 168 MHz
      - 1024 Kb
      - 128 Kb

    * - ``disco_f429zi``
      - `ST 32F429IDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF259090>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F429ZIT6
      - 180 MHz
      - 2048 Kb
      - 256 Kb

    * - ``disco_f469ni``
      - `ST 32F469IDISCOVERY <http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF262395>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F469NIH6
      - 180 MHz
      - 1024 Kb
      - 384 Kb

    * - ``disco_f746ng``
      - `ST 32F746GDISCOVERY <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/32f746gdiscovery.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F746NGH6
      - 216 MHz
      - 1024 Kb
      - 320 Kb

    * - ``disco_f769ni``
      - `ST 32F769IDISCOVERY <http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/32f769idiscovery.html>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F769NIH6
      - 80 MHz
      - 1024 Kb
      - 512 Kb

    * - ``disco_l053c8``
      - `ST 32L0538DISCOVERY <http://www.st.com/web/en/catalog/tools/PF260319>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L053C8T6
      - 32 MHz
      - 64 Kb
      - 8 Kb

    * - ``disco_l152rb``
      - `ST STM32LDISCOVERY <http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1848/PF258515>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L152RBT6
      - 32 MHz
      - 128 Kb
      - 16 Kb

    * - ``disco_l476vg``
      - `ST 32L476GDISCOVERY <http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF261635>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L476VGT6
      - 80 MHz
      - 1024 Kb
      - 128 Kb

    * - ``nucleo_f030r8``
      - `ST Nucleo F030R8 <https://developer.mbed.org/platforms/ST-Nucleo-F030R8/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F030R8T6
      - 48 MHz
      - 64 Kb
      - 8 Kb

    * - ``nucleo_f031k6``
      - `ST Nucleo F031K6 <https://developer.mbed.org/platforms/ST-Nucleo-F031K6/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F031K6T6
      - 48 MHz
      - 32 Kb
      - 4 Kb

    * - ``nucleo_f042k6``
      - `ST Nucleo F042K6 <https://developer.mbed.org/platforms/ST-Nucleo-F042K6/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F042K6T6
      - 48 MHz
      - 32 Kb
      - 6 Kb

    * - ``nucleo_f070rb``
      - `ST Nucleo F070RB <https://developer.mbed.org/platforms/ST-Nucleo-F070RB/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F070RBT6
      - 48 MHz
      - 128 Kb
      - 16 Kb

    * - ``nucleo_f072rb``
      - `ST Nucleo F072RB <https://developer.mbed.org/platforms/ST-Nucleo-F072RB/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F072RBT6
      - 48 MHz
      - 128 Kb
      - 16 Kb

    * - ``nucleo_f091rc``
      - `ST Nucleo F091RC <https://developer.mbed.org/platforms/ST-Nucleo-F091RC/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F091RCT6
      - 48 MHz
      - 256 Kb
      - 32 Kb

    * - ``nucleo_f103rb``
      - `ST Nucleo F103RB <https://developer.mbed.org/platforms/ST-Nucleo-F103RB/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F103RBT6
      - 72 MHz
      - 128 Kb
      - 20 Kb

    * - ``nucleo_f207zg``
      - `ST Nucleo F207ZG <https://developer.mbed.org/platforms/ST-Nucleo-F207ZG/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F207ZGT6
      - 120 MHz
      - 1024 Kb
      - 128 Kb

    * - ``nucleo_f302r8``
      - `ST Nucleo F302R8 <https://developer.mbed.org/platforms/ST-Nucleo-F302R8/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F302R8T6
      - 72 MHz
      - 64 Kb
      - 16 Kb

    * - ``nucleo_f303k8``
      - `ST Nucleo F303K8 <https://developer.mbed.org/platforms/ST-Nucleo-F303K8/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F303K8T6
      - 72 MHz
      - 64 Kb
      - 16 Kb

    * - ``nucleo_f303re``
      - `ST Nucleo F303RE <http://developer.mbed.org/platforms/ST-Nucleo-F303RE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F303RET6
      - 72 MHz
      - 512 Kb
      - 64 Kb

    * - ``nucleo_f303ze``
      - `ST Nucleo F303ZE <https://developer.mbed.org/platforms/ST-Nucleo-F303ZE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F303ZET6
      - 72 MHz
      - 512 Kb
      - 64 Kb

    * - ``nucleo_f334r8``
      - `ST Nucleo F334R8 <https://developer.mbed.org/platforms/ST-Nucleo-F334R8/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F334R8T6
      - 72 MHz
      - 64 Kb
      - 16 Kb

    * - ``nucleo_f401re``
      - `ST Nucleo F401RE <https://developer.mbed.org/platforms/ST-Nucleo-F401RE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F401RET6
      - 84 MHz
      - 512 Kb
      - 96 Kb

    * - ``nucleo_f410rb``
      - `ST Nucleo F410RB <https://developer.mbed.org/platforms/ST-Nucleo-F410RB/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F410RBT6
      - 100 MHz
      - 128 Kb
      - 32 Kb

    * - ``nucleo_f411re``
      - `ST Nucleo F411RE <https://developer.mbed.org/platforms/ST-Nucleo-F411RE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F411RET6
      - 100 MHz
      - 512 Kb
      - 128 Kb

    * - ``nucleo_f429zi``
      - `ST Nucleo F429ZI <https://developer.mbed.org/platforms/ST-Nucleo-F429ZI/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F429ZIT6
      - 180 MHz
      - 2048 Kb
      - 256 Kb

    * - ``nucleo_f446re``
      - `ST Nucleo F446RE <https://developer.mbed.org/platforms/ST-Nucleo-F446RE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F446RET6
      - 180 MHz
      - 512 Kb
      - 128 Kb

    * - ``nucleo_f446ze``
      - `ST Nucleo F446ZE <https://developer.mbed.org/platforms/ST-Nucleo-F446ZE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F446ZET6
      - 180 MHz
      - 512 Kb
      - 128 Kb

    * - ``nucleo_f746zg``
      - `ST Nucleo F746ZG <https://developer.mbed.org/platforms/ST-Nucleo-F446ZE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F746ZGT6
      - 216 MHz
      - 1024 Kb
      - 320 Kb

    * - ``nucleo_f767zi``
      - `ST Nucleo F767ZI <https://developer.mbed.org/platforms/ST-Nucleo-F767ZI/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F767ZIT6
      - 216 MHz
      - 2048 Kb
      - 512 Kb

    * - ``nucleo_l031k6``
      - `ST Nucleo L031K6 <https://developer.mbed.org/platforms/ST-Nucleo-L031K6/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L031K6T6
      - 32 MHz
      - 32 Kb
      - 8 Kb

    * - ``nucleo_l053r8``
      - `ST Nucleo L053R8 <https://developer.mbed.org/platforms/ST-Nucleo-L053R8/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L053R8T6
      - 48 MHz
      - 64 Kb
      - 8 Kb

    * - ``nucleo_l073rz``
      - `ST Nucleo L073RZ <https://developer.mbed.org/platforms/ST-Nucleo-L073RZ/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L073RZ
      - 32 MHz
      - 192 Kb
      - 20 Kb

    * - ``nucleo_l152re``
      - `ST Nucleo L152RE <https://developer.mbed.org/platforms/ST-Nucleo-L152RE/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L152RET6
      - 32 MHz
      - 512 Kb
      - 80 Kb

    * - ``nucleo_l432kc``
      - `ST Nucleo L432KC <https://developer.mbed.org/platforms/ST-Nucleo-L432KC/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L432KCU6
      - 80 MHz
      - 256 Kb
      - 64 Kb

    * - ``nucleo_l476rg``
      - `ST Nucleo L476RG <https://developer.mbed.org/platforms/ST-Nucleo-L476RG/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
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
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``seeedArchMax``
      - `Seeed Arch Max <https://developer.mbed.org/platforms/Seeed-Arch-Max/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32F407VET6
      - 168 MHz
      - 512 Kb
      - 192 Kb

Semtech
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``mote_l152rc``
      - `NAMote72 <https://developer.mbed.org/platforms/NAMote-72/>`_
      - :ref:`ST STM32 <platform_ststm32>`
      - :ref:`Yes <piodebug>`
      - STM32L152RC
      - 32 MHz
      - 256 Kb
      - 32 Kb

.. include:: stm32cube_extra.rst
