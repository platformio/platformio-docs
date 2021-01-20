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

:Configuration:
  :ref:`projectconf_env_platform` = ``ststm32``

The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

For more detailed information please visit `vendor site <http://www.st.com/web/en/catalog/mmc/FM141/SC1169?sc=stm32&utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: ststm32_extra.rst

Examples
--------

Examples are listed from `ST STM32 development platform repository <https://github.com/platformio/platform-ststm32/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `mbed-rtos-wifi <https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-wifi?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-blink <https://github.com/platformio/platform-ststm32/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs>`_
* `stm32cube-ll-blink <https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-ll-blink?utm_source=platformio.org&utm_medium=docs>`_
* `libopencm3-blink <https://github.com/platformio/platform-ststm32/tree/master/examples/libopencm3-blink?utm_source=platformio.org&utm_medium=docs>`_
* `libopencm3-usb-cdcacm <https://github.com/platformio/platform-ststm32/tree/master/examples/libopencm3-usb-cdcacm?utm_source=platformio.org&utm_medium=docs>`_
* `cmsis-blink <https://github.com/platformio/platform-ststm32/tree/master/examples/cmsis-blink?utm_source=platformio.org&utm_medium=docs>`_
* `stm32cube-hal-iap <https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-hal-iap?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-blink <https://github.com/platformio/platform-ststm32/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `stm32cube-hal-extmem-boot <https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-hal-extmem-boot?utm_source=platformio.org&utm_medium=docs>`_
* `spl-blink <https://github.com/platformio/platform-ststm32/tree/master/examples/spl-blink?utm_source=platformio.org&utm_medium=docs>`_
* `stm32cube-hal-lcd <https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-hal-lcd?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-mesh-minimal <https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-mesh-minimal?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-mxchip-sensors <https://github.com/platformio/platform-ststm32/tree/master/examples/arduino-mxchip-sensors?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-cpp-synchronization <https://github.com/platformio/platform-ststm32/tree/master/examples/zephyr-cpp-synchronization?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-net-https-client <https://github.com/platformio/platform-ststm32/tree/master/examples/zephyr-net-https-client?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-blink-baremetal <https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-blink-baremetal?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-filesystem <https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-filesystem?utm_source=platformio.org&utm_medium=docs>`_
* `stm32cube-hal-wifi-client <https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-hal-wifi-client?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-usb-keyboard <https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-usb-keyboard?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-ethernet-tls <https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-ethernet-tls?utm_source=platformio.org&utm_medium=docs>`_
* `stm32cube-hal-blink <https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-hal-blink?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-drivers-can <https://github.com/platformio/platform-ststm32/tree/master/examples/zephyr-drivers-can?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-mxchip-azureiot <https://github.com/platformio/platform-ststm32/tree/master/examples/arduino-mxchip-azureiot?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-mxchip-filesystem <https://github.com/platformio/platform-ststm32/tree/master/examples/arduino-mxchip-filesystem?utm_source=platformio.org&utm_medium=docs>`_
* `stm32cube-hal-usb-device-dfu <https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-hal-usb-device-dfu?utm_source=platformio.org&utm_medium=docs>`_
* `stm32cube-hal-blink-clangd <https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-hal-blink-clangd?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-ststm32/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-external-libs <https://github.com/platformio/platform-ststm32/tree/master/examples/arduino-external-libs?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-mxchip-wifiscan <https://github.com/platformio/platform-ststm32/tree/master/examples/arduino-mxchip-wifiscan?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-events <https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-events?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-legacy-examples <https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-legacy-examples?utm_source=platformio.org&utm_medium=docs>`_
* `libopencm3-1bitsy <https://github.com/platformio/platform-ststm32/tree/master/examples/libopencm3-1bitsy?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-subsys-usb-hid-mouse <https://github.com/platformio/platform-ststm32/tree/master/examples/zephyr-subsys-usb-hid-mouse?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-serial <https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-serial?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-custom-target <https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-custom-target?utm_source=platformio.org&utm_medium=docs>`_
* `stm32cube-hal-eeprom-emulation <https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-hal-eeprom-emulation?utm_source=platformio.org&utm_medium=docs>`_

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. contents::
    :local:


Tools & Debug Probes
~~~~~~~~~~~~~~~~~~~~

Supported debugging tools are listed in "Debug" column. For more detailed
information, please scroll table by horizontal.
You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further instructions.


On-Board Debug Tools
^^^^^^^^^^^^^^^^^^^^

Boards listed below have on-board debug probe and **ARE READY** for debugging!
You do not need to use/buy external debug probe.


.. list-table::
    :header-rows:  1

    * - Name
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_disco_f412zg`
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_disco_f723ie`
      - STM32F723IEK6
      - 216MHz
      - 512KB
      - 192KB
    * - :ref:`board_ststm32_remram_v1`
      - STM32F765VIT6
      - 216MHz
      - 2MB
      - 512KB
    * - :ref:`board_ststm32_st3dp001_eval`
      - STM32F401VGT6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_b96b_f446ve`
      - STM32F446VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_armstrap_eagle1024`
      - STM32F417VGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_ststm32_armstrap_eagle2048`
      - STM32F427VIT6
      - 168MHz
      - 1.99MB
      - 256KB
    * - :ref:`board_ststm32_armstrap_eagle512`
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB
    * - :ref:`board_ststm32_rhombio_l476dmw1k`
      - STM32L476VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_mbed_connect_odin`
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
    * - :ref:`board_ststm32_mxchip_az3166`
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_nucleo_wb55rg_p`
      - STM32WB55RG
      - 64MHz
      - 512KB
      - 192.00KB
    * - :ref:`board_ststm32_cloud_jam`
      - STM32F401RET6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_cloud_jam_l4`
      - STM32L476RGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_disco_f334c8`
      - STM32F334C8T6
      - 72MHz
      - 64KB
      - 12KB
    * - :ref:`board_ststm32_disco_f401vc`
      - STM32F401VCT6
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_disco_f411ve`
      - STM32F411VET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_disco_f413zh`
      - STM32F413ZHT6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_disco_f429zi`
      - STM32F429ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - :ref:`board_ststm32_disco_f469ni`
      - STM32F469NIH6
      - 180MHz
      - 1MB
      - 384KB
    * - :ref:`board_ststm32_disco_f746ng`
      - STM32F746NGH6
      - 216MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_disco_f769ni`
      - STM32F769NIH6
      - 216MHz
      - 1MB
      - 512KB
    * - :ref:`board_ststm32_disco_l053c8`
      - STM32L053C8T6
      - 32MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_disco_l100rc`
      - STM32L100RCT6
      - 32MHz
      - 256KB
      - 16KB
    * - :ref:`board_ststm32_disco_l476vg`
      - STM32L476VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_disco_l496ag`
      - STM32L496AGI6
      - 80MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_disco_l475vg_iot01a`
      - STM32L475VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_disco_l072cz_lrwan1`
      - STM32L072CZ
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_disco_f072rb`
      - STM32F072RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f030r8`
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_nucleo_f031k6`
      - STM32F031K6T6
      - 48MHz
      - 32KB
      - 4KB
    * - :ref:`board_ststm32_nucleo_f042k6`
      - STM32F042K6T6
      - 48MHz
      - 32KB
      - 6KB
    * - :ref:`board_ststm32_nucleo_f070rb`
      - STM32F070RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f072rb`
      - STM32F072RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f091rc`
      - STM32F091RCT6
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_f103rb`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_nucleo_f207zg`
      - STM32F207ZGT6
      - 120MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f302r8`
      - STM32F302R8T6
      - 72MHz
      - 64KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f303k8`
      - STM32F303K8T6
      - 72MHz
      - 64KB
      - 12KB
    * - :ref:`board_ststm32_nucleo_f303re`
      - STM32F303RET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_f303ze`
      - STM32F303ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_f334r8`
      - STM32F334R8T6
      - 72MHz
      - 64KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f401re`
      - STM32F401RET6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_nucleo_f410rb`
      - STM32F410RBT6
      - 100MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_f411re`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f412zg`
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_nucleo_f413zh`
      - STM32F413ZHT6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f429zi`
      - STM32F429ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - :ref:`board_ststm32_nucleo_f439zi`
      - STM32F439ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - :ref:`board_ststm32_nucleo_f446re`
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f446ze`
      - STM32F446ZET6
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f722ze`
      - STM32F722ZET6
      - 216MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_nucleo_f746zg`
      - STM32F746ZGT6
      - 216MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_nucleo_f756zg`
      - STM32F756ZG
      - 216MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_nucleo_f767zi`
      - STM32F767ZIT6
      - 216MHz
      - 2MB
      - 512KB
    * - :ref:`board_ststm32_nucleo_h743zi`
      - STM32H743ZIT6
      - 400MHz
      - 2MB
      - 512KB
    * - :ref:`board_ststm32_nucleo_h745zi_q`
      - STM32H745ZIT6
      - 480MHz
      - 1MB
      - 512KB
    * - :ref:`board_ststm32_nucleo_l011k4`
      - STM32L011K4T6
      - 32MHz
      - 16KB
      - 2KB
    * - :ref:`board_ststm32_nucleo_l031k6`
      - STM32L031K6T6
      - 32MHz
      - 32KB
      - 8KB
    * - :ref:`board_ststm32_nucleo_l053r8`
      - STM32L053R8T6
      - 32MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_nucleo_l073rz`
      - STM32L073RZ
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_nucleo_l152re`
      - STM32L152RET6
      - 32MHz
      - 512KB
      - 80KB
    * - :ref:`board_ststm32_nucleo_l412kb`
      - STM32L412KBU6
      - 80MHz
      - 128KB
      - 40KB
    * - :ref:`board_ststm32_nucleo_l432kc`
      - STM32L432KCU6
      - 80MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_l433rc_p`
      - STM32L433RC
      - 80MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_l452re`
      - STM32L452RET6
      - 80MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_l476rg`
      - STM32L476RGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_l486rg`
      - STM32L486RGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_l496zg`
      - STM32L496ZGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_l496zg_p`
      - STM32L496ZGT6P
      - 80MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_nucleo_l4r5zi`
      - STM32L4R5ZIT6
      - 120MHz
      - 2MB
      - 640KB
    * - :ref:`board_ststm32_disco_f030r8`
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_disco_f051r8`
      - STM32F051R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_disco_f303vc`
      - STM32F303VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_disco_f407vg`
      - STM32F407VGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_eval_l073z`
      - STM32L073VZT6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_disco_l152rb`
      - STM32L152RBT6
      - 32MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_disco_f100rb`
      - STM32F100RBT6
      - 24MHz
      - 128KB
      - 8KB
    * - :ref:`board_ststm32_silica_sensor_node`
      - STM32L476JG
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_disco_f750n8`
      - STM32F750N8H6
      - 216MHz
      - 64KB
      - 340KB
    * - :ref:`board_ststm32_disco_h747xi`
      - STM32H747XIH6
      - 400MHz
      - 2MB
      - 512KB
    * - :ref:`board_ststm32_seeedArchMax`
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB
    * - :ref:`board_ststm32_wio_3g`
      - STM32F439VI
      - 180MHz
      - 2MB
      - 256KB
    * - :ref:`board_ststm32_sakuraio_evb_01`
      - STM32F411RET6
      - 100MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_ublox_c030_r410m`
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_mtb_ublox_odin_w2`
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB


External Debug Tools
^^^^^^^^^^^^^^^^^^^^

Boards listed below are compatible with :ref:`piodebug` but **DEPEND ON**
external debug probe. They **ARE NOT READY** for debugging.
Please click on board name for the further details.


.. list-table::
    :header-rows:  1

    * - Name
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_1bitsy_stm32f415rgt`
      - STM32F415RGT
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_armed_v1`
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB
    * - :ref:`board_ststm32_rumba32_f446ve`
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_b96b_argonkey`
      - STM32F412CG
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_b96b_aerocore2`
      - STM32F427VIT6
      - 168MHz
      - 1.99MB
      - 256KB
    * - :ref:`board_ststm32_b96b_neonkey`
      - STM32F411CE
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_adafruit_feather_f405`
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_afroflight_f103cb`
      - STM32F103CBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_black_f407ve`
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_black_f407vg`
      - STM32F407VGT6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_black_f407ze`
      - STM32F407ZET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_black_f407zg`
      - STM32F407ZGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_blackpill_f103c8`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_blackpill_f103c8_128`
      - STM32F103C8T6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_robotdyn_blackpill_f303cc`
      - STM32F303CCT6
      - 72MHz
      - 256KB
      - 40KB
    * - :ref:`board_ststm32_blackpill_f401cc`
      - STM32F401CCU6
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_blackpill_f401ce`
      - STM32F401CEU6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_blue_f407ve_mini`
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_bluepill_f103c6`
      - STM32F103C6T6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_bluepill_f103c8`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_bluepill_f103c8_128k`
      - STM32F103C8T6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_cicada_l082cz`
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_coreboard_f401rc`
      - STM32F401RCT6
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_cricket_l082cz`
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_demo_f030f4`
      - STM32F030F4P6
      - 48MHz
      - 16KB
      - 4KB
    * - :ref:`board_ststm32_econode_l082cz`
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_electrosmith_daisy`
      - STM32H750IBK6
      - 400MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_elmo_f411re`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_diymore_f407vgt`
      - STM32F407VGT6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_fk407m1`
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_fysetc_s6`
      - STM32F446VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_gnat_l082cz`
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_grasshopper_l082cz`
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_malyanm200_f070cb`
      - STM32F070CBT6
      - 48MHz
      - 120KB
      - 14.81KB
    * - :ref:`board_ststm32_malyanm300_f070cb`
      - STM32F070CBT6
      - 48MHz
      - 120KB
      - 14.81KB
    * - :ref:`board_ststm32_mkr_sharky`
      - STM32WB55CG
      - 64MHz
      - 512KB
      - 192.00KB
    * - :ref:`board_ststm32_mts_dragonfly_f411re`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_malyanm200_f103cb`
      - STM32F103CBT6
      - 72MHz
      - 120KB
      - 20KB
    * - :ref:`board_ststm32_maple`
      - STM32F103RBT6
      - 72MHz
      - 108KB
      - 17KB
    * - :ref:`board_ststm32_maple_ret6`
      - STM32F103RET6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_maple_mini_b20`
      - STM32F103CBT6
      - 72MHz
      - 120KB
      - 20KB
    * - :ref:`board_ststm32_maple_mini_origin`
      - STM32F103CBT6
      - 72MHz
      - 108KB
      - 17KB
    * - :ref:`board_ststm32_microduino32_flash`
      - STM32F103CBT6
      - 72MHz
      - 105.47KB
      - 16.60KB
    * - :ref:`board_ststm32_mts_mdot_f405rg`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_mts_mdot_f411re`
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_xdot_l151cc`
      - STM32L151CCU6
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_netduino2plus`
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_ststm32_mote_l152rc`
      - STM32L152RC
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_g071rb`
      - STM32G071RBT6
      - 64MHz
      - 128KB
      - 36KB
    * - :ref:`board_ststm32_nucleo_g431kb`
      - STM32G431KBT6
      - 170MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_g431rb`
      - STM32G431RBT6
      - 170MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_g474re`
      - STM32G474RET6
      - 170MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_olimexino`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_olimex_f103`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_olimex_p405`
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_ststm32_pybstick26_duino`
      - STM32F072RB
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_pybstick26_pro`
      - STM32F412RE
      - 100MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_pybstick26_lite`
      - STM32F401CEU6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_pybstick26_std`
      - STM32F411CEU6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_piconomix_px_her0`
      - STM32L072RB
      - 32MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_prntr_v2`
      - STM32F407RE
      - 168MHz
      - 512KB
      - 192KB
    * - :ref:`board_ststm32_rak811_tracker`
      - STM32L151RBT6
      - 32MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_rak811_tracker_32`
      - STM32L151RBT6
      - 32MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_rhf76_052`
      - STM32L051C8T6
      - 32MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_disco_g031j6`
      - STM32G031J6
      - 64MHz
      - 128KB
      - 8KB
    * - :ref:`board_ststm32_steval_fcu001v1`
      - STM32F401CCU6
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_olimex_e407`
      - STM32F407ZGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_olimex_h407`
      - STM32F407ZGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_eval_f107vc`
      - STM32F107VCT6
      - 72MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_eval_f373vc`
      - STM32F373VCT6
      - 72MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_eval_f072vb`
      - STM32F072VBT6
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_genericSTM32F103C4`
      - STM32F103C4
      - 72MHz
      - 16KB
      - 6KB
    * - :ref:`board_ststm32_genericSTM32F103C6`
      - STM32F103C6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_genericSTM32F103C8`
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103CB`
      - STM32F103CBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103R4`
      - STM32F103R4
      - 72MHz
      - 16KB
      - 6KB
    * - :ref:`board_ststm32_genericSTM32F103R6`
      - STM32F103R6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_genericSTM32F103R8`
      - STM32F103R8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103RB`
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103RC`
      - STM32F103RCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_genericSTM32F103RD`
      - STM32F103RD
      - 72MHz
      - 384KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103RE`
      - STM32F103RET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103RF`
      - STM32F103RF
      - 72MHz
      - 768KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103RG`
      - STM32F103RG
      - 72MHz
      - 1MB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103T4`
      - STM32F103T4
      - 72MHz
      - 16KB
      - 6KB
    * - :ref:`board_ststm32_genericSTM32F103T6`
      - STM32F103T6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_genericSTM32F103T8`
      - STM32F103T8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103TB`
      - STM32F103TBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103V8`
      - STM32F103V8
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103VB`
      - STM32F103VBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103VC`
      - STM32F103VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_genericSTM32F103VD`
      - STM32F103VDT6
      - 72MHz
      - 384KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103VE`
      - STM32F103VET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103VF`
      - STM32F103VF
      - 72MHz
      - 768KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103VG`
      - STM32F103VG
      - 72MHz
      - 1MB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103ZC`
      - STM32F103ZCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_genericSTM32F103ZD`
      - STM32F103ZDT6
      - 72MHz
      - 384KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103ZE`
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103ZF`
      - STM32F103ZF
      - 72MHz
      - 768KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103ZG`
      - STM32F103ZG
      - 72MHz
      - 1MB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F303CB`
      - STM32F303CBT6
      - 72MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F373RC`
      - STM32F373RCT6
      - 72MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F401CB`
      - STM32F401CB
      - 84MHz
      - 128KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401CC`
      - STM32F401CC
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401CD`
      - STM32F401CD
      - 84MHz
      - 384KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401CE`
      - STM32F401CE
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401RB`
      - STM32F401RB
      - 84MHz
      - 128KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401RC`
      - STM32F401RC
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401RD`
      - STM32F401RD
      - 84MHz
      - 384KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401RE`
      - STM32F401RE
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F405RG`
      - STM32F405RG
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F407VET6`
      - STM32F407VET6
      - 168MHz
      - 502.23KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F407VGT6`
      - STM32F407VGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_ststm32_genericSTM32F410C8`
      - STM32F410C8
      - 100MHz
      - 64KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F410CB`
      - STM32F410CB
      - 100MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F410R8`
      - STM32F410R8
      - 100MHz
      - 64KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F410RB`
      - STM32F410RB
      - 100MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F411CC`
      - STM32F411CC
      - 100MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F411CE`
      - STM32F411CE
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F411RC`
      - STM32F411RC
      - 100MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F411RE`
      - STM32F411RE
      - 100MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F412CE`
      - STM32F412CE
      - 100MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F412CG`
      - STM32F412CG
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F412RE`
      - STM32F412RE
      - 100MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F412RG`
      - STM32F412RG
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F413CG`
      - STM32F413CG
      - 100MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F413CH`
      - STM32F413CH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F413RG`
      - STM32F413RG
      - 100MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F413RH`
      - STM32F413RH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F415RG`
      - STM32F415RG
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F417VE`
      - STM32F417VE
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F417VG`
      - STM32F417VG
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F423CH`
      - STM32F423CH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F423RH`
      - STM32F423RH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F446RC`
      - STM32F446RC
      - 180MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F446RE`
      - STM32F446RE
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_stm32f4stamp`
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_ststm32_steval_mksboxv1`
      - STM32L4R9ZI
      - 120MHz
      - 2MB
      - 640KB
    * - :ref:`board_ststm32_sparky_v1`
      - STM32F303CCT6
      - 72MHz
      - 256KB
      - 40KB
    * - :ref:`board_ststm32_thunder_pack`
      - STM32L072KZ
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_thunder_pack_f411`
      - STM32F411CEU6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_hy_tinystm103tb`
      - STM32F103TBU6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_vake_v1`
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_vccgnd_f103zet6`
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_waveshare_open103z`
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_blackpill_f411ce`
      - STM32F411CEU6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_wraith32_v1`
      - STM32F051K6
      - 48MHz
      - 32KB
      - 7.75KB
    * - :ref:`board_ststm32_ublox_c030_n211`
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_ublox_c030_u201`
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_ublox_evk_odin_w2`
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-ststm32/releases>`__
of ST STM32 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = ststm32
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = ststm32@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-ststm32.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinostm32mxchip <https://microsoft.github.io/azure-iot-developer-kit/?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for the Azure MXChip IoT DevKit

    * - `framework-arduinoststm32 <https://github.com/stm32duino/Arduino_Core_STM32.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for ST STM32 microcontrollers

    * - `framework-arduinoststm32-maple <https://github.com/rogerclarkmelbourne/Arduino_STM32.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for ST STM32 microcontrollers (Maple Core)

    * - `framework-arduinoststm32l0 <https://github.com/GrumpyOldPizza/ArduinoCore-stm32l0.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for ST STM32 microcontrollers (ST STM32L0 Core)

    * - `framework-cmsis <http://www.arm.com/products/processors/cortex-m/cortex-microcontroller-software-interface-standard.php?utm_source=platformio.org&utm_medium=docs>`__
      - Vendor-independent hardware abstraction layer for the Cortex-M processor series

    * - `framework-cmsis-stm32f0 <https://github.com/STMicroelectronics/cmsis_device_f0.git?utm_source=platformio.org&utm_medium=docs>`__
      - CMSIS component for the STMicroelectronics STM32F0 series

    * - `framework-cmsis-stm32f1 <https://github.com/STMicroelectronics/cmsis_device_f1.git?utm_source=platformio.org&utm_medium=docs>`__
      - CMSIS component for the STMicroelectronics STM32F1 series

    * - `framework-cmsis-stm32f2 <https://github.com/STMicroelectronics/cmsis_device_f2.git?utm_source=platformio.org&utm_medium=docs>`__
      - CMSIS component for the STMicroelectronics STM32F2 series

    * - `framework-cmsis-stm32f3 <https://github.com/STMicroelectronics/cmsis_device_f3.git?utm_source=platformio.org&utm_medium=docs>`__
      - CMSIS component for the STMicroelectronics STM32F3 series

    * - `framework-cmsis-stm32f4 <https://github.com/STMicroelectronics/cmsis_device_f4.git?utm_source=platformio.org&utm_medium=docs>`__
      - CMSIS component for the STMicroelectronics STM32F4 series

    * - `framework-cmsis-stm32f7 <https://github.com/STMicroelectronics/cmsis_device_f7.git?utm_source=platformio.org&utm_medium=docs>`__
      - CMSIS component for the STMicroelectronics STM32F7 series

    * - `framework-cmsis-stm32g0 <https://github.com/STMicroelectronics/cmsis_device_g0.git?utm_source=platformio.org&utm_medium=docs>`__
      - CMSIS component for the STMicroelectronics STM32G0 series

    * - `framework-cmsis-stm32g4 <https://github.com/STMicroelectronics/cmsis_device_g4.git?utm_source=platformio.org&utm_medium=docs>`__
      - CMSIS component for the STMicroelectronics STM32G4 series

    * - `framework-cmsis-stm32h7 <https://github.com/STMicroelectronics/cmsis_device_h7.git?utm_source=platformio.org&utm_medium=docs>`__
      - CMSIS component for the STMicroelectronics STM32H7 series

    * - `framework-cmsis-stm32l0 <https://github.com/STMicroelectronics/cmsis_device_l0.git?utm_source=platformio.org&utm_medium=docs>`__
      - CMSIS component for the STMicroelectronics STM32L0 series

    * - `framework-cmsis-stm32l1 <https://github.com/STMicroelectronics/cmsis_device_l1.git?utm_source=platformio.org&utm_medium=docs>`__
      - CMSIS component for the STMicroelectronics STM32L1 series

    * - `framework-cmsis-stm32l4 <https://github.com/STMicroelectronics/cmsis_device_l4.git?utm_source=platformio.org&utm_medium=docs>`__
      - CMSIS component for the STMicroelectronics STM32L4 series

    * - `framework-cmsis-stm32l5 <https://github.com/STMicroelectronics/cmsis_device_l5.git?utm_source=platformio.org&utm_medium=docs>`__
      - CMSIS component for the STMicroelectronics STM32L5 series

    * - `framework-libopencm3 <http://www.libopencm3.org/?utm_source=platformio.org&utm_medium=docs>`__
      - Open source ARM Cortex-M microcontroller library

    * - `framework-mbed <http://mbed.org?utm_source=platformio.org&utm_medium=docs>`__
      - Arm Mbed OS is a platform operating system designed for the internet of things

    * - `framework-spl <http://www.st.com/web/catalog/tools/FM147/CL1794/SC961/SS1743/PF257890?utm_source=platformio.org&utm_medium=docs>`__
      - Standard Peripheral Library for ST STM32 microcontrollers

    * - `framework-stm32cubef0 <https://github.com/STMicroelectronics/STM32CubeF0?utm_source=platformio.org&utm_medium=docs>`__
      - STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeF0 MCU Firmware Package)

    * - `framework-stm32cubef1 <https://github.com/STMicroelectronics/STM32CubeF1?utm_source=platformio.org&utm_medium=docs>`__
      - STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeF1 MCU Firmware Package)

    * - `framework-stm32cubef2 <https://github.com/STMicroelectronics/STM32CubeF2?utm_source=platformio.org&utm_medium=docs>`__
      - STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeF2 MCU Firmware Package)

    * - `framework-stm32cubef3 <https://github.com/STMicroelectronics/STM32CubeF3?utm_source=platformio.org&utm_medium=docs>`__
      - STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeF3 MCU Firmware Package)

    * - `framework-stm32cubef4 <https://github.com/STMicroelectronics/STM32CubeF4?utm_source=platformio.org&utm_medium=docs>`__
      - STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeF4 MCU Firmware Package)

    * - `framework-stm32cubef7 <https://github.com/STMicroelectronics/STM32CubeF7?utm_source=platformio.org&utm_medium=docs>`__
      - STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeF7 MCU Firmware Package)

    * - `framework-stm32cubeg0 <https://github.com/STMicroelectronics/STM32CubeG0?utm_source=platformio.org&utm_medium=docs>`__
      - STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeG0 MCU Firmware Package)

    * - `framework-stm32cubeg4 <https://github.com/STMicroelectronics/STM32CubeG4?utm_source=platformio.org&utm_medium=docs>`__
      - STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeG4 MCU Firmware Package)

    * - `framework-stm32cubeh7 <https://github.com/STMicroelectronics/STM32CubeH7?utm_source=platformio.org&utm_medium=docs>`__
      - STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeH7 MCU Firmware Package)

    * - `framework-stm32cubel0 <https://github.com/STMicroelectronics/STM32CubeL0?utm_source=platformio.org&utm_medium=docs>`__
      - STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32Cubel0 MCU Firmware Package)

    * - `framework-stm32cubel1 <https://github.com/STMicroelectronics/STM32CubeL1?utm_source=platformio.org&utm_medium=docs>`__
      - STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeL1 MCU Firmware Package)

    * - `framework-stm32cubel4 <https://github.com/STMicroelectronics/STM32CubeL4?utm_source=platformio.org&utm_medium=docs>`__
      - STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeL4 MCU Firmware Package)

    * - `framework-stm32cubel5 <https://github.com/STMicroelectronics/STM32CubeL5?utm_source=platformio.org&utm_medium=docs>`__
      - STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeL5 MCU Firmware Package)

    * - `framework-zephyr <https://www.zephyrproject.org?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures

    * - `framework-zephyr-canopennode <https://github.com/zephyrproject-rtos/canopennode?utm_source=platformio.org&utm_medium=docs>`__
      - canopennode Zephyr module

    * - `framework-zephyr-civetweb <https://github.com/zephyrproject-rtos/civetweb.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for CivetWeb Embedded C/C++ web server

    * - `framework-zephyr-cmsis <https://github.com/zephyrproject-rtos/cmsis.git?utm_source=platformio.org&utm_medium=docs>`__
      - Software Interface Standard for Arm Cortex-based Microcontrollers and Zephyr framework

    * - `framework-zephyr-fatfs <https://github.com/zephyrproject-rtos/fatfs.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for FATFS filesystem

    * - `framework-zephyr-hal-st <https://github.com/zephyrproject-rtos/hal_st.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for the official libraries provided by STMicroelectronics

    * - `framework-zephyr-hal-stm32 <https://github.com/zephyrproject-rtos/hal_stm32.git?utm_source=platformio.org&utm_medium=docs>`__
      - ST STM32 HAL for Zephyr framework

    * - `framework-zephyr-libmetal <https://github.com/zephyrproject-rtos/libmetal.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for HAL abstraction layer used by open-amp

    * - `framework-zephyr-littlefs <https://github.com/zephyrproject-rtos/littlefs.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for littlefs filesystem

    * - `framework-zephyr-loramac-node <https://github.com/zephyrproject-rtos/loramac-node.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for LoRaWAN endpoint stack implementation

    * - `framework-zephyr-lvgl <https://github.com/zephyrproject-rtos/lvgl.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for LittlevGL - an Open-source Embedded GUI Library

    * - `framework-zephyr-mbedtls <https://github.com/zephyrproject-rtos/mbedtls.git?utm_source=platformio.org&utm_medium=docs>`__
      - mbedTLS module for Zephyr

    * - `framework-zephyr-mcuboot <https://github.com/zephyrproject-rtos/mcuboot.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for MCUboot - a secure bootloader for 32-bit MCUs

    * - `framework-zephyr-mcumgr <https://github.com/zephyrproject-rtos/mcumgr.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for mcumgr management library for 32-bit MCUs

    * - `framework-zephyr-mipi-sys-t <https://github.com/zephyrproject-rtos/mipi-sys-t.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for MIPI System Software Trace

    * - `framework-zephyr-open-amp <https://github.com/zephyrproject-rtos/open-amp.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for Open Asymmetric Multi Processing (OpenAMP) framework

    * - `framework-zephyr-openthread <https://github.com/zephyrproject-rtos/openthread.git?utm_source=platformio.org&utm_medium=docs>`__
      - OpenThread module for Zephyr

    * - `framework-zephyr-segger <https://github.com/zephyrproject-rtos/segger.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for Segger RTT

    * - `framework-zephyr-tinycbor <https://github.com/zephyrproject-rtos/tinycbor.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for Concise Binary Object Representation Library

    * - `framework-zephyr-tinycrypt <https://github.com/zephyrproject-rtos/tinycrypt.git?utm_source=platformio.org&utm_medium=docs>`__
      - The TinyCrypt Library provides an implementation for constrained devices of a minimal set of standard cryptography primitives for Zephyr framework

    * - `framework-zephyr-trusted-firmware-m <https://github.com/zephyrproject-rtos/trusted-firmware-m.git?utm_source=platformio.org&utm_medium=docs>`__
      - Trusted Firmware M provides a reference implementation of secure world software for ARMv8-M and Zephyr framework

    * - `tool-cmake <https://cmake.org?utm_source=platformio.org&utm_medium=docs>`__
      - CMake is an open-source, cross-platform family of tools designed to build, test and package software

    * - `tool-dfuutil <http://dfu-util.sourceforge.net/?utm_source=platformio.org&utm_medium=docs>`__
      - Device Firmware Upgrade Utilities

    * - `tool-dtc <https://git.kernel.org/pub/scm/utils/dtc/dtc.git?utm_source=platformio.org&utm_medium=docs>`__
      - Device tree compiler

    * - `tool-gperf <https://www.gnu.org/software/gperf?utm_source=platformio.org&utm_medium=docs>`__
      - GNU gperf is a perfect hash function generator

    * - `tool-jlink <https://www.segger.com/downloads/jlink/?utm_source=platformio.org&utm_medium=docs>`__
      - Software and Documentation Pack for SEGGER J-Link debug probes

    * - `tool-ldscripts-ststm32 <https://www.st.com/en/development-tools/stm32cubemx.html?utm_source=platformio.org&utm_medium=docs>`__
      - Linker scripts pack for STMicroelectronics STM32 platform

    * - `tool-ninja <https://ninja-build.org?utm_source=platformio.org&utm_medium=docs>`__
      - Ninja is a small build system with a focus on speed

    * - `tool-openocd <http://openocd.org?utm_source=platformio.org&utm_medium=docs>`__
      - Open On-Chip Debugger. Free and Open On-Chip Debugging, In-System Programming and Boundary-Scan Testing

    * - `tool-stm32duino <https://www.stm32duino.com?utm_source=platformio.org&utm_medium=docs>`__
      - STM32Duino Tools

    * - `toolchain-gccarmnoneeabi <https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm?utm_source=platformio.org&utm_medium=docs>`__
      - GNU toolchain for Arm Cortex-M and Cortex-R processors

.. warning::
    **Linux Users**:

        * Install "udev" rules :ref:`faq_udev_rules`
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
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences

    * - :ref:`framework_cmsis`
      - The ARM Cortex Microcontroller Software Interface Standard (CMSIS) is a vendor-independent hardware abstraction layer for the Cortex-M processor series and specifies debugger interfaces. The CMSIS enables consistent and simple software interfaces to the processor for interface peripherals, real-time operating systems, and middleware. It simplifies software re-use, reducing the learning curve for new microcontroller developers and cutting the time-to-market for devices

    * - :ref:`framework_mbed`
      - Arm Mbed OS is an open source embedded operating system designed specifically for the 'things' in the Internet of Things. It includes all the features you need to develop a connected product based on an Arm Cortex-M microcontroller, including security, connectivity, an RTOS and drivers for sensors and I/O devices

    * - :ref:`framework_stm32cube`
      - STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency

    * - :ref:`framework_spl`
      - The ST Standard Peripheral Library provides a set of functions for handling the peripherals on the STM32 family of microcontrollers.

    * - :ref:`framework_zephyr`
      - The Zephyr Project is a scalable real-time operating system (RTOS) supporting multiple hardware architectures, optimized for resource constrained devices, and built with safety and security in mind

    * - :ref:`framework_libopencm3`
      - The libOpenCM3 framework aims to create a free and open-source firmware library for various ARM Cortex-M0(+)/M3/M4 microcontrollers, including ST STM32, Ti Tiva and Stellaris, NXP LPC, Atmel SAM3, Energy Micro EFM32 and others

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

1BitSquared
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_1bitsy_stm32f415rgt`
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_b96b_argonkey`
      - External
      - STM32F412CG
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_b96b_f446ve`
      - On-board
      - STM32F446VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_b96b_aerocore2`
      - External
      - STM32F427VIT6
      - 168MHz
      - 1.99MB
      - 256KB
    * - :ref:`board_ststm32_b96b_neonkey`
      - External
      - STM32F411CE
      - 100MHz
      - 512KB
      - 128KB

Adafruit
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_adafruit_feather_f405`
      - External
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 128KB

AfroFlight
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_afroflight_f103cb`
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_wraith32_v1`
      - External
      - STM32F051K6
      - 48MHz
      - 32KB
      - 7.75KB

Armed
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_armed_v1`
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_armstrap_eagle1024`
      - On-board
      - STM32F417VGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_ststm32_armstrap_eagle2048`
      - On-board
      - STM32F427VIT6
      - 168MHz
      - 1.99MB
      - 256KB
    * - :ref:`board_ststm32_armstrap_eagle512`
      - On-board
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB

Avnet Silica
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_silica_sensor_node`
      - On-board
      - STM32L476JG
      - 80MHz
      - 1MB
      - 128KB

Diymore
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_diymore_f407vgt`
      - External
      - STM32F407VGT6
      - 168MHz
      - 512KB
      - 128KB

Econode
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_econode_l082cz`
      - External
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB

Electrosmith
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_electrosmith_daisy`
      - External
      - STM32H750IBK6
      - 400MHz
      - 512KB
      - 128KB

Espotel
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_elmo_f411re`
      - External
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB

FYSETC
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_fysetc_s6`
      - External
      - STM32F446VET6
      - 168MHz
      - 512KB
      - 128KB

Generic
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_blackpill_f103c8`
      - External
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_blackpill_f103c8_128`
      - External
      - STM32F103C8T6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_bluepill_f103c6`
      - External
      - STM32F103C6T6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_bluepill_f103c8`
      - External
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_bluepill_f103c8_128k`
      - External
      - STM32F103C8T6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_demo_f030f4`
      - External
      - STM32F030F4P6
      - 48MHz
      - 16KB
      - 4KB
    * - :ref:`board_ststm32_fk407m1`
      - External
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F103C4`
      - External
      - STM32F103C4
      - 72MHz
      - 16KB
      - 6KB
    * - :ref:`board_ststm32_genericSTM32F103C6`
      - External
      - STM32F103C6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_genericSTM32F103C8`
      - External
      - STM32F103C8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103CB`
      - External
      - STM32F103CBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103R4`
      - External
      - STM32F103R4
      - 72MHz
      - 16KB
      - 6KB
    * - :ref:`board_ststm32_genericSTM32F103R6`
      - External
      - STM32F103R6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_genericSTM32F103R8`
      - External
      - STM32F103R8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103RB`
      - External
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103RC`
      - External
      - STM32F103RCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_genericSTM32F103RD`
      - External
      - STM32F103RD
      - 72MHz
      - 384KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103RE`
      - External
      - STM32F103RET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103RF`
      - External
      - STM32F103RF
      - 72MHz
      - 768KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103RG`
      - External
      - STM32F103RG
      - 72MHz
      - 1MB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103T4`
      - External
      - STM32F103T4
      - 72MHz
      - 16KB
      - 6KB
    * - :ref:`board_ststm32_genericSTM32F103T6`
      - External
      - STM32F103T6
      - 72MHz
      - 32KB
      - 10KB
    * - :ref:`board_ststm32_genericSTM32F103T8`
      - External
      - STM32F103T8T6
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103TB`
      - External
      - STM32F103TBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103V8`
      - External
      - STM32F103V8
      - 72MHz
      - 64KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103VB`
      - External
      - STM32F103VBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_genericSTM32F103VC`
      - External
      - STM32F103VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_genericSTM32F103VD`
      - External
      - STM32F103VDT6
      - 72MHz
      - 384KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103VE`
      - External
      - STM32F103VET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103VF`
      - External
      - STM32F103VF
      - 72MHz
      - 768KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103VG`
      - External
      - STM32F103VG
      - 72MHz
      - 1MB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103ZC`
      - External
      - STM32F103ZCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_genericSTM32F103ZD`
      - External
      - STM32F103ZDT6
      - 72MHz
      - 384KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103ZE`
      - External
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F103ZF`
      - External
      - STM32F103ZF
      - 72MHz
      - 768KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F103ZG`
      - External
      - STM32F103ZG
      - 72MHz
      - 1MB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F303CB`
      - External
      - STM32F303CBT6
      - 72MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F373RC`
      - External
      - STM32F373RCT6
      - 72MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F401CB`
      - External
      - STM32F401CB
      - 84MHz
      - 128KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401CC`
      - External
      - STM32F401CC
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401CD`
      - External
      - STM32F401CD
      - 84MHz
      - 384KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401CE`
      - External
      - STM32F401CE
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401RB`
      - External
      - STM32F401RB
      - 84MHz
      - 128KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401RC`
      - External
      - STM32F401RC
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_genericSTM32F401RD`
      - External
      - STM32F401RD
      - 84MHz
      - 384KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F401RE`
      - External
      - STM32F401RE
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_genericSTM32F405RG`
      - External
      - STM32F405RG
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F407VET6`
      - External
      - STM32F407VET6
      - 168MHz
      - 502.23KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F407VGT6`
      - External
      - STM32F407VGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_ststm32_genericSTM32F410C8`
      - External
      - STM32F410C8
      - 100MHz
      - 64KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F410CB`
      - External
      - STM32F410CB
      - 100MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F410R8`
      - External
      - STM32F410R8
      - 100MHz
      - 64KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F410RB`
      - External
      - STM32F410RB
      - 100MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_genericSTM32F411CC`
      - External
      - STM32F411CC
      - 100MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F411CE`
      - External
      - STM32F411CE
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F411RC`
      - External
      - STM32F411RC
      - 100MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F411RE`
      - External
      - STM32F411RE
      - 100MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F412CE`
      - External
      - STM32F412CE
      - 100MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F412CG`
      - External
      - STM32F412CG
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F412RE`
      - External
      - STM32F412RE
      - 100MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F412RG`
      - External
      - STM32F412RG
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_genericSTM32F413CG`
      - External
      - STM32F413CG
      - 100MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F413CH`
      - External
      - STM32F413CH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F413RG`
      - External
      - STM32F413RG
      - 100MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F413RH`
      - External
      - STM32F413RH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F415RG`
      - External
      - STM32F415RG
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F417VE`
      - External
      - STM32F417VE
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F417VG`
      - External
      - STM32F417VG
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F423CH`
      - External
      - STM32F423CH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F423RH`
      - External
      - STM32F423RH
      - 100MHz
      - 1.50MB
      - 320KB
    * - :ref:`board_ststm32_genericSTM32F446RC`
      - External
      - STM32F446RC
      - 180MHz
      - 256KB
      - 128KB
    * - :ref:`board_ststm32_genericSTM32F446RE`
      - External
      - STM32F446RE
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_stm32f4stamp`
      - External
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 192KB

HY
~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_hy_tinystm103tb`
      - External
      - STM32F103TBU6
      - 72MHz
      - 128KB
      - 20KB

LeafLabs
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_maple`
      - External
      - STM32F103RBT6
      - 72MHz
      - 108KB
      - 17KB
    * - :ref:`board_ststm32_maple_ret6`
      - External
      - STM32F103RET6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_maple_mini_b20`
      - External
      - STM32F103CBT6
      - 72MHz
      - 120KB
      - 20KB
    * - :ref:`board_ststm32_maple_mini_origin`
      - External
      - STM32F103CBT6
      - 72MHz
      - 108KB
      - 17KB

MXChip
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_mxchip_az3166`
      - On-board
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB

Malyan
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_malyanm200_f070cb`
      - External
      - STM32F070CBT6
      - 48MHz
      - 120KB
      - 14.81KB
    * - :ref:`board_ststm32_malyanm300_f070cb`
      - External
      - STM32F070CBT6
      - 48MHz
      - 120KB
      - 14.81KB
    * - :ref:`board_ststm32_malyanm200_f103cb`
      - External
      - STM32F103CBT6
      - 72MHz
      - 120KB
      - 20KB

Microduino
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_microduino32_flash`
      - External
      - STM32F103CBT6
      - 72MHz
      - 105.47KB
      - 16.60KB

Midatronics
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_mkr_sharky`
      - External
      - STM32WB55CG
      - 64MHz
      - 512KB
      - 192.00KB

MultiTech
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_mts_dragonfly_f411re`
      - External
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_mts_mdot_f405rg`
      - External
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_mts_mdot_f411re`
      - External
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_xdot_l151cc`
      - External
      - STM32L151CCU6
      - 32MHz
      - 256KB
      - 32KB

Netduino
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_netduino2plus`
      - External
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 192KB

Olimex
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_olimexino`
      - External
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_olimex_f103`
      - External
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_olimex_p405`
      - External
      - STM32F405RGT6
      - 168MHz
      - 1MB
      - 192KB
    * - :ref:`board_ststm32_olimex_e407`
      - External
      - STM32F407ZGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_olimex_h407`
      - External
      - STM32F407ZGT6
      - 168MHz
      - 1MB
      - 128KB

PYBStick
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_pybstick26_duino`
      - External
      - STM32F072RB
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_pybstick26_pro`
      - External
      - STM32F412RE
      - 100MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_pybstick26_lite`
      - External
      - STM32F401CEU6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_pybstick26_std`
      - External
      - STM32F411CEU6
      - 100MHz
      - 512KB
      - 128KB

Piconomix
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_piconomix_px_her0`
      - External
      - STM32L072RB
      - 32MHz
      - 128KB
      - 20KB

PrntrBoard
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_prntr_v2`
      - External
      - STM32F407RE
      - 168MHz
      - 512KB
      - 192KB

RAK
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_rak811_tracker`
      - External
      - STM32L151RBT6
      - 32MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_rak811_tracker_32`
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_rumba32_f446ve`
      - External
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB

RemRam
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_remram_v1`
      - On-board
      - STM32F765VIT6
      - 216MHz
      - 2MB
      - 512KB

RobotDyn
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_robotdyn_blackpill_f303cc`
      - External
      - STM32F303CCT6
      - 72MHz
      - 256KB
      - 40KB

RushUp
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_cloud_jam`
      - On-board
      - STM32F401RET6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_cloud_jam_l4`
      - On-board
      - STM32L476RGT6
      - 80MHz
      - 1MB
      - 128KB

ST
~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_disco_f412zg`
      - On-board
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_disco_f723ie`
      - On-board
      - STM32F723IEK6
      - 216MHz
      - 512KB
      - 192KB
    * - :ref:`board_ststm32_st3dp001_eval`
      - On-board
      - STM32F401VGT6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_black_f407ve`
      - External
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_black_f407vg`
      - External
      - STM32F407VGT6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_black_f407ze`
      - External
      - STM32F407ZET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_black_f407zg`
      - External
      - STM32F407ZGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_blackpill_f401cc`
      - External
      - STM32F401CCU6
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_blackpill_f401ce`
      - External
      - STM32F401CEU6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_blue_f407ve_mini`
      - External
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_coreboard_f401rc`
      - External
      - STM32F401RCT6
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_g071rb`
      - External
      - STM32G071RBT6
      - 64MHz
      - 128KB
      - 36KB
    * - :ref:`board_ststm32_nucleo_g431kb`
      - External
      - STM32G431KBT6
      - 170MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_g431rb`
      - External
      - STM32G431RBT6
      - 170MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_g474re`
      - External
      - STM32G474RET6
      - 170MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_wb55rg_p`
      - On-board
      - STM32WB55RG
      - 64MHz
      - 512KB
      - 192.00KB
    * - :ref:`board_ststm32_rhf76_052`
      - External
      - STM32L051C8T6
      - 32MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_disco_f334c8`
      - On-board
      - STM32F334C8T6
      - 72MHz
      - 64KB
      - 12KB
    * - :ref:`board_ststm32_disco_f401vc`
      - On-board
      - STM32F401VCT6
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_disco_f411ve`
      - On-board
      - STM32F411VET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_disco_f413zh`
      - On-board
      - STM32F413ZHT6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_disco_f429zi`
      - On-board
      - STM32F429ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - :ref:`board_ststm32_disco_f469ni`
      - On-board
      - STM32F469NIH6
      - 180MHz
      - 1MB
      - 384KB
    * - :ref:`board_ststm32_disco_f746ng`
      - On-board
      - STM32F746NGH6
      - 216MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_disco_f769ni`
      - On-board
      - STM32F769NIH6
      - 216MHz
      - 1MB
      - 512KB
    * - :ref:`board_ststm32_disco_l053c8`
      - On-board
      - STM32L053C8T6
      - 32MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_disco_l100rc`
      - On-board
      - STM32L100RCT6
      - 32MHz
      - 256KB
      - 16KB
    * - :ref:`board_ststm32_disco_l476vg`
      - On-board
      - STM32L476VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_disco_l496ag`
      - On-board
      - STM32L496AGI6
      - 80MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_disco_l475vg_iot01a`
      - On-board
      - STM32L475VGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_disco_l072cz_lrwan1`
      - On-board
      - STM32L072CZ
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_disco_f072rb`
      - On-board
      - STM32F072RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f030r8`
      - On-board
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_nucleo_f031k6`
      - On-board
      - STM32F031K6T6
      - 48MHz
      - 32KB
      - 4KB
    * - :ref:`board_ststm32_nucleo_f042k6`
      - On-board
      - STM32F042K6T6
      - 48MHz
      - 32KB
      - 6KB
    * - :ref:`board_ststm32_nucleo_f070rb`
      - On-board
      - STM32F070RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f072rb`
      - On-board
      - STM32F072RBT6
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f091rc`
      - On-board
      - STM32F091RCT6
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_f103rb`
      - On-board
      - STM32F103RBT6
      - 72MHz
      - 128KB
      - 20KB
    * - :ref:`board_ststm32_nucleo_f207zg`
      - On-board
      - STM32F207ZGT6
      - 120MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f302r8`
      - On-board
      - STM32F302R8T6
      - 72MHz
      - 64KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f303k8`
      - On-board
      - STM32F303K8T6
      - 72MHz
      - 64KB
      - 12KB
    * - :ref:`board_ststm32_nucleo_f303re`
      - On-board
      - STM32F303RET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_f303ze`
      - On-board
      - STM32F303ZET6
      - 72MHz
      - 512KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_f334r8`
      - On-board
      - STM32F334R8T6
      - 72MHz
      - 64KB
      - 16KB
    * - :ref:`board_ststm32_nucleo_f401re`
      - On-board
      - STM32F401RET6
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_ststm32_nucleo_f410rb`
      - On-board
      - STM32F410RBT6
      - 100MHz
      - 128KB
      - 32KB
    * - :ref:`board_ststm32_nucleo_f411re`
      - On-board
      - STM32F411RET6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f412zg`
      - On-board
      - STM32F412ZGT6
      - 100MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_nucleo_f413zh`
      - On-board
      - STM32F413ZHT6
      - 100MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f429zi`
      - On-board
      - STM32F429ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - :ref:`board_ststm32_nucleo_f439zi`
      - On-board
      - STM32F439ZIT6
      - 180MHz
      - 2MB
      - 256KB
    * - :ref:`board_ststm32_nucleo_f446re`
      - On-board
      - STM32F446RET6
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f446ze`
      - On-board
      - STM32F446ZET6
      - 180MHz
      - 512KB
      - 128KB
    * - :ref:`board_ststm32_nucleo_f722ze`
      - On-board
      - STM32F722ZET6
      - 216MHz
      - 512KB
      - 256KB
    * - :ref:`board_ststm32_nucleo_f746zg`
      - On-board
      - STM32F746ZGT6
      - 216MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_nucleo_f756zg`
      - On-board
      - STM32F756ZG
      - 216MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_nucleo_f767zi`
      - On-board
      - STM32F767ZIT6
      - 216MHz
      - 2MB
      - 512KB
    * - :ref:`board_ststm32_nucleo_h743zi`
      - On-board
      - STM32H743ZIT6
      - 400MHz
      - 2MB
      - 512KB
    * - :ref:`board_ststm32_nucleo_h745zi_q`
      - On-board
      - STM32H745ZIT6
      - 480MHz
      - 1MB
      - 512KB
    * - :ref:`board_ststm32_nucleo_l011k4`
      - On-board
      - STM32L011K4T6
      - 32MHz
      - 16KB
      - 2KB
    * - :ref:`board_ststm32_nucleo_l031k6`
      - On-board
      - STM32L031K6T6
      - 32MHz
      - 32KB
      - 8KB
    * - :ref:`board_ststm32_nucleo_l053r8`
      - On-board
      - STM32L053R8T6
      - 32MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_nucleo_l073rz`
      - On-board
      - STM32L073RZ
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_nucleo_l152re`
      - On-board
      - STM32L152RET6
      - 32MHz
      - 512KB
      - 80KB
    * - :ref:`board_ststm32_nucleo_l412kb`
      - On-board
      - STM32L412KBU6
      - 80MHz
      - 128KB
      - 40KB
    * - :ref:`board_ststm32_nucleo_l432kc`
      - On-board
      - STM32L432KCU6
      - 80MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_l433rc_p`
      - On-board
      - STM32L433RC
      - 80MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_l452re`
      - On-board
      - STM32L452RET6
      - 80MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_nucleo_l476rg`
      - On-board
      - STM32L476RGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_l486rg`
      - On-board
      - STM32L486RGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_l496zg`
      - On-board
      - STM32L496ZGT6
      - 80MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_nucleo_l496zg_p`
      - On-board
      - STM32L496ZGT6P
      - 80MHz
      - 1MB
      - 320KB
    * - :ref:`board_ststm32_nucleo_l4r5zi`
      - On-board
      - STM32L4R5ZIT6
      - 120MHz
      - 2MB
      - 640KB
    * - :ref:`board_ststm32_disco_f030r8`
      - On-board
      - STM32F030R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_disco_f051r8`
      - On-board
      - STM32F051R8T6
      - 48MHz
      - 64KB
      - 8KB
    * - :ref:`board_ststm32_disco_f303vc`
      - On-board
      - STM32F303VCT6
      - 72MHz
      - 256KB
      - 48KB
    * - :ref:`board_ststm32_disco_f407vg`
      - On-board
      - STM32F407VGT6
      - 168MHz
      - 1MB
      - 128KB
    * - :ref:`board_ststm32_disco_g031j6`
      - External
      - STM32G031J6
      - 64MHz
      - 128KB
      - 8KB
    * - :ref:`board_ststm32_eval_l073z`
      - On-board
      - STM32L073VZT6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_disco_l152rb`
      - On-board
      - STM32L152RBT6
      - 32MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_disco_f100rb`
      - On-board
      - STM32F100RBT6
      - 24MHz
      - 128KB
      - 8KB
    * - :ref:`board_ststm32_steval_fcu001v1`
      - External
      - STM32F401CCU6
      - 84MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_eval_f107vc`
      - External
      - STM32F107VCT6
      - 72MHz
      - 256KB
      - 64KB
    * - :ref:`board_ststm32_eval_f373vc`
      - External
      - STM32F373VCT6
      - 72MHz
      - 256KB
      - 32KB
    * - :ref:`board_ststm32_eval_f072vb`
      - External
      - STM32F072VBT6
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_ststm32_disco_f750n8`
      - On-board
      - STM32F750N8H6
      - 216MHz
      - 64KB
      - 340KB
    * - :ref:`board_ststm32_disco_h747xi`
      - On-board
      - STM32H747XIH6
      - 400MHz
      - 2MB
      - 512KB
    * - :ref:`board_ststm32_steval_mksboxv1`
      - External
      - STM32L4R9ZI
      - 120MHz
      - 2MB
      - 640KB

SeeedStudio
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_seeedArchMax`
      - On-board
      - STM32F407VET6
      - 168MHz
      - 512KB
      - 192KB
    * - :ref:`board_ststm32_wio_3g`
      - On-board
      - STM32F439VI
      - 180MHz
      - 2MB
      - 256KB

Semtech
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_mote_l152rc`
      - External
      - STM32L152RC
      - 32MHz
      - 256KB
      - 32KB

TauLabs
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_sparky_v1`
      - External
      - STM32F303CCT6
      - 72MHz
      - 256KB
      - 40KB

ThunderPack
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_thunder_pack`
      - External
      - STM32L072KZ
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_thunder_pack_f411`
      - External
      - STM32F411CEU6
      - 100MHz
      - 512KB
      - 128KB

Tlera Corporation
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_cicada_l082cz`
      - External
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_cricket_l082cz`
      - External
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_gnat_l082cz`
      - External
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB
    * - :ref:`board_ststm32_grasshopper_l082cz`
      - External
      - STM32L082CZY6
      - 32MHz
      - 192KB
      - 20KB

VAE
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_vake_v1`
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_vccgnd_f103zet6`
      - External
      - STM32F103ZET6
      - 72MHz
      - 512KB
      - 64KB

Waveshare
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_waveshare_open103z`
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_blackpill_f411ce`
      - External
      - STM32F411CEU6
      - 100MHz
      - 512KB
      - 128KB

rhomb.io
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_rhombio_l476dmw1k`
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_sakuraio_evb_01`
      - On-board
      - STM32F411RET6
      - 100MHz
      - 1MB
      - 128KB

u-blox
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm32_mbed_connect_odin`
      - On-board
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
    * - :ref:`board_ststm32_ublox_c030_n211`
      - External
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_ublox_c030_r410m`
      - On-board
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_ublox_c030_u201`
      - External
      - STM32F437VG
      - 180MHz
      - 1MB
      - 256KB
    * - :ref:`board_ststm32_ublox_evk_odin_w2`
      - External
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
    * - :ref:`board_ststm32_mtb_ublox_odin_w2`
      - On-board
      - STM32F439ZIY6
      - 168MHz
      - 2MB
      - 256KB
