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

.. _platform_espressif32:

Espressif 32
============

:Registry:
  `https://registry.platformio.org/platforms/platformio/espressif32 <https://registry.platformio.org/platforms/platformio/espressif32>`__
:Configuration:
  :ref:`projectconf_env_platform` = ``espressif32``

ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and Bluetooth. ESP32 integrates an antenna switch, RF balun, power amplifier, low-noise receive amplifier, filters, and power management modules.

For more detailed information please visit `vendor site <https://espressif.com/?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: espressif32_extra.rst

Examples
--------

Examples are listed from `Espressif 32 development platform repository <https://github.com/platformio/platform-espressif32/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `espidf-storage-sdcard <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-storage-sdcard?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-usb-keyboard <https://github.com/platformio/platform-espressif32/tree/master/examples/arduino-usb-keyboard?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-coap-server <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-coap-server?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-storage-spiffs <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-storage-spiffs?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-exceptions <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-exceptions?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-blink <https://github.com/platformio/platform-espressif32/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-ble-eddystone <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-ble-eddystone?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-ulp-adc <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-ulp-adc?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-ulp-pulse <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-ulp-pulse?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-arduino-wifiscan <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-arduino-wifiscan?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-http-request <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-http-request?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-arduino-blink <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-hello-world <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-hello-world?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-aws-iot <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-aws-iot?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-ble5-advertising <https://github.com/platformio/platform-espressif32/tree/master/examples/arduino-ble5-advertising?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-peripherals-usb <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-peripherals-usb?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-briki-internal-libs <https://github.com/platformio/platform-espressif32/tree/master/examples/arduino-briki-internal-libs?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-peripherals-uart <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-peripherals-uart?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-wifiscan <https://github.com/platformio/platform-espressif32/tree/master/examples/arduino-wifiscan?utm_source=platformio.org&utm_medium=docs>`_

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. contents::
    :local:

.. include:: espressif32_debug.rst

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
    * - :ref:`board_espressif32_esp-wrover-kit`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-s3-devkitc-1`
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB


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
    * - :ref:`board_espressif32_esp32cam`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_alksesp32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_az-delivery-devkit-v4`
      - ESP32
      - 240MHz
      - 4MB
      - 520KB
    * - :ref:`board_espressif32_featheresp32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_featheresp32-s2`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_feather_esp32_v2`
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_feather_esp32s2_tft`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_feather_esp32s3`
      - ESP32S3
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_feather_esp32s3_nopsram`
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_feather_esp32s3_tft`
      - ESP32S3
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_funhouse_esp32s2`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_itsybitsy_esp32`
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_magtag29_esp32s2`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_metro_esp32s2`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_qtpy_esp32`
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_qtpy_esp32c3`
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_qtpy_esp32s2`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_qtpy_esp32s3_nopsram`
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_esp32-c3-m1i-kit`
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_nodemcu-32s2`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_airm2m_core_esp32c3`
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_bpi_leaf_s3`
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_wifiduino32s3`
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_wifiduino32c3`
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_briki_abc_esp32`
      - ESP32
      - 240MHz
      - 3.25MB
      - 320KB
    * - :ref:`board_espressif32_briki_mbc-wb_esp32`
      - ESP32
      - 240MHz
      - 3.25MB
      - 320KB
    * - :ref:`board_espressif32_connaxio_espoir`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_cytron_maker_feather_aiot_s3`
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_d-duino-32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_dfrobot_beetle_esp32c3`
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_dfrobot_firebeetle2_esp32s3`
      - ESP32S3
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32doit-devkit-v1`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32doit-espduino`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_deneyapkart`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_deneyapkart1A`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_deneyapkart1Av2`
      - ESP32S3
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_deneyapkartg`
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_deneyapmini`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_deneyapminiv2`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_minimain_esp32s2`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_pocket_32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_fm-devkit`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_pico32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32s3camlcd`
      - ESP32S3
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_esp32vn-iot-uno`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_espectro32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_espino32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_atmegazero_esp32s2`
      - ESP32S2
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_esp32dev`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-c3-devkitm-1`
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-s2-kaluga-1`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-s2-saola-1`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32s3box`
      - ESP32S3
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_firebeetle32`
      - ESP32
      - 240MHz
      - 16MB
      - 520KB
    * - :ref:`board_espressif32_franzininho_wifi_esp32s2`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-s2-franzininho`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_franzininho_wifi_msc_esp32s2`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_frogboard`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_honeylemon`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wifi_lora_32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wifi_lora_32_V2`
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wireless_stick`
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_hornbill32dev`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_hornbill32minima`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_iotaap_magnolia`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_sensesiot_weizen`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lionbit`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_mhetesp32devkit`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_mhetesp32minikit`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_kb32-ft`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_redpill_esp32s3`
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_node32s`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_nodemcu-32s`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-devkitlipo`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-evb`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-gateway`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lopy`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lopy4`
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB
    * - :ref:`board_espressif32_wipy3`
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB
    * - :ref:`board_espressif32_sg-o_airMon`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_watchy`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_seeed_xiao_esp32c3`
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wesp32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_bee_motion`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_bee_motion_mini`
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_bee_motion_s3`
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_bee_s3`
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_sparkfun_esp32_iot_redboard`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32thing`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32thing_plus`
      - ESP32
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_sparkfun_esp32s2_thing_plus_c`
      - ESP32
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_sparkfun_esp32s2_thing_plus`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_sparkfun_lora_gateway_1-channel`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_dpu_esp32`
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_tamc_termod_s3`
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-lora32-v1`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-lora32-v2`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-lora32-v21`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-t-beam`
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB
    * - :ref:`board_espressif32_ttgo-t-oi-plus`
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-t1`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-t7-v14-mini32`
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB
    * - :ref:`board_espressif32_trueverit-iot-driver`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_trueverit-iot-driver-mk2`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_trueverit-iot-driver-mk3`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_um_feathers2`
      - ESP32S2
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_um_feathers2_neo`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_um_feathers3`
      - ESP32S3
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_um_pros3`
      - ESP32S3
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_um_rmp`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_um_tinys2`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_um_tinys3`
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_vintlabs-devkit-v1`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wemos_d1_mini32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wemos_d1_uno32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_c3_mini`
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_d32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_d32_pro`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_s2_mini`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_s2_pico`
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_s3`
      - ESP32S3
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_lolin32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wemosbat`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wt32-eth01`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_xinabox_cw02`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_micros2`
      - ESP32S2
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_iotbusio`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_iotbusproteus`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_upesy_wroom`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_upesy_wrover`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_unphone7`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_unphone8`
      - ESP32S3
      - 240MHz
      - 7.94MB
      - 2.31MB
    * - :ref:`board_espressif32_unphone9`
      - ESP32S3
      - 240MHz
      - 7.94MB
      - 8.31MB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-espressif32/releases>`__
of Espressif 32 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version, NOT recommended
    ; Pin the version as shown below
    [env:latest_stable]
    platform = espressif32
    board = ...

    ; Specific version
    [env:custom_stable]
    platform = espressif32@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-espressif32.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduino-mbcwb <https://registry.platformio.org/tools/meteca/framework-arduino-mbcwb>`__
      - Fork of Arduino Framework for briki MBC-WB boards

    * - `framework-arduinoespressif32 <https://registry.platformio.org/tools/platformio/framework-arduinoespressif32>`__
      - Arduino Wiring-based Framework for the Espressif ESP32, ESP32-S and ESP32-C series of SoCs

    * - `framework-espidf <https://registry.platformio.org/tools/platformio/framework-espidf>`__
      - ESP-IDF is Espressif's official IoT Development Framework for the ESP32, ESP32-S, ESP32-C and ESP32-H series of SoCs. It provides a self-sufficient SDK for any generic application development on these platforms, using programming languages such as C and C++.

    * - `tool-cmake <https://registry.platformio.org/tools/platformio/tool-cmake>`__
      - CMake is an open-source, cross-platform family of tools designed to build, test and package software.

    * - `tool-esptoolpy <https://registry.platformio.org/tools/platformio/tool-esptoolpy>`__
      - A Python-based, open-source, platform-independent utility to communicate with the ROM bootloader in Espressif chips

    * - `tool-idf <https://registry.platformio.org/tools/platformio/tool-idf>`__
      - idf is a top-level config/build command line tool for ESP-IDF

    * - `tool-mbctool <https://registry.platformio.org/tools/meteca/tool-mbctool>`__
      - MBC-WB Uploader Application

    * - `tool-mconf <https://registry.platformio.org/tools/platformio/tool-mconf>`__
      - Fork of kconfig-frontends project with some modifications for use with ESP-IDF

    * - `tool-mkfatfs <https://registry.platformio.org/tools/platformio/tool-mkfatfs>`__
      - Utility for creating FFat images

    * - `tool-mklittlefs <https://registry.platformio.org/tools/platformio/tool-mklittlefs>`__
      - Utility for creating littlefs images for upload on the ESP8266

    * - `tool-mkspiffs <https://registry.platformio.org/tools/platformio/tool-mkspiffs>`__
      - Tool to build and unpack SPIFFS images

    * - `tool-ninja <https://registry.platformio.org/tools/platformio/tool-ninja>`__
      - Ninja is a small build system with a focus on speed

    * - `tool-openocd-esp32 <https://registry.platformio.org/tools/platformio/tool-openocd-esp32>`__
      - Open On-Chip Debugger for Espressif ESP32

    * - `toolchain-esp32ulp <https://registry.platformio.org/tools/platformio/toolchain-esp32ulp>`__
      - Binutils fork with support for the Espressif ESP32 ULP co-processor

    * - `toolchain-riscv32-esp <https://registry.platformio.org/tools/espressif/toolchain-riscv32-esp>`__
      - GCC Toolchain for Espressif 32-bit RISC-V based MCUs

    * - `toolchain-xtensa-esp32 <https://registry.platformio.org/tools/espressif/toolchain-xtensa-esp32>`__
      - GCC Toolchain for Espressif ESP32 Xtensa MCUs

    * - `toolchain-xtensa-esp32s2 <https://registry.platformio.org/tools/espressif/toolchain-xtensa-esp32s2>`__
      - GCC Toolchain for Espressif ESP32-S2 Xtensa MCUs

    * - `toolchain-xtensa-esp32s3 <https://registry.platformio.org/tools/espressif/toolchain-xtensa-esp32s3>`__
      - GCC Toolchain for Espressif ESP32-S3 Xtensa MCUs

.. warning::
    **Linux Users**:

        * Install "udev" rules :ref:`platformio_udev_rules`
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

    * - :ref:`framework_espidf`
      - ESP-IDF is the official development framework for the ESP32 and ESP32-S Series SoCs.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

AI Thinker
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32cam`
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_az-delivery-devkit-v4`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 520KB

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
    * - :ref:`board_espressif32_featheresp32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_featheresp32-s2`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_feather_esp32_v2`
      - External
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_feather_esp32s2_tft`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_feather_esp32s3`
      - External
      - ESP32S3
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_feather_esp32s3_nopsram`
      - External
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_feather_esp32s3_tft`
      - External
      - ESP32S3
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_funhouse_esp32s2`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_itsybitsy_esp32`
      - External
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_magtag29_esp32s2`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_metro_esp32s2`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_qtpy_esp32`
      - External
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_qtpy_esp32c3`
      - External
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_qtpy_esp32s2`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_adafruit_qtpy_esp32s3_nopsram`
      - External
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB

Ai-Thinker
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32-c3-m1i-kit`
      - External
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_nodemcu-32s2`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB

AirM2M
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_airm2m_core_esp32c3`
      - External
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB

Aiyarafun
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_node32s`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

April Brother
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_espea32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

BPI Tech
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_bpi-bit`
      - No
      - ESP32
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_bpi_leaf_s3`
      - External
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB

Blinker
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_wifiduino32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wifiduino32s3`
      - External
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_wifiduino32c3`
      - External
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB

CNRS
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_cnrs_aw2eth`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Connaxio
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_connaxio_espoir`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Cytron Technologies
~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_cytron_maker_feather_aiot_s3`
      - External
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB

DFRobot
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_dfrobot_beetle_esp32c3`
      - External
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_dfrobot_firebeetle2_esp32s3`
      - External
      - ESP32S3
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_firebeetle32`
      - External
      - ESP32
      - 240MHz
      - 16MB
      - 520KB

DOIT
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32doit-devkit-v1`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32doit-espduino`
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_d-duino-32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Deneyap
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_deneyapkart`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_deneyapkart1A`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_deneyapkart1Av2`
      - External
      - ESP32S3
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_deneyapkartg`
      - External
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_deneyapmini`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_deneyapminiv2`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB

Denky
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_denky_d4`
      - No
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_denky32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Deparment of Alchemy
~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_minimain_esp32s2`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB

Dongsen Technology
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_pocket_32`
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_espectro32`
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32vn-iot-uno`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

ETBoard
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_etboard`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Electronic SweetPeas
~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp320`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

EspinalLab
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_atmegazero_esp32s2`
      - External
      - ESP32S2
      - 240MHz
      - 16MB
      - 320KB

Espressif
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_pico32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32s3camlcd`
      - External
      - ESP32S3
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_esp-wrover-kit`
      - On-board
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32dev`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-c3-devkitm-1`
      - External
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-s2-kaluga-1`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-s2-saola-1`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32s3box`
      - External
      - ESP32S3
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_esp32-s3-devkitc-1`
      - On-board
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB

Fishino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_piranha_esp32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Franzininho
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_franzininho_wifi_esp32s2`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-s2-franzininho`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_franzininho_wifi_msc_esp32s2`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB

Fred
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_frogboard`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

HONEYLemon
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_honeylemon`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Hardkernel
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_odroid_esp32`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

Heltec Automation
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_heltec_wifi_kit_32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wifi_kit_32_v2`
      - No
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wifi_lora_32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wifi_lora_32_V2`
      - External
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wireless_stick`
      - External
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wireless_stick_lite`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Hornbill
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_hornbill32dev`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_hornbill32minima`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

INEX
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_inex_openkb`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Imbrios
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_imbrios-logsens-v1p1`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

IntoRobot
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_intorobot`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

IoTaaP
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_iotaap_magnolia`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

KITS
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_kits-edu`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

LOGISENSES
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_sensesiot_weizen`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Labplus
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_labplus_mpython`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Lion:Bit
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_lionbit`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

M5Stack
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_m5stack-core-esp32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_m5stack-core2`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 4.31MB
    * - :ref:`board_espressif32_m5stack-fire`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 4.31MB
    * - :ref:`board_espressif32_m5stack-grey`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 520KB
    * - :ref:`board_espressif32_m5stack-station`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 4.31MB
    * - :ref:`board_espressif32_m5stack-timer-cam`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_m5stack-atom`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_m5stack-coreink`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_m5stick-c`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

MGBOT
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_mgbot-iotik32a`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_mgbot-iotik32b`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

MH-ET Live
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_mhetesp32devkit`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_mhetesp32minikit`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Magicblocks.io
~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_magicbit`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

MakerAsia
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_kb32-ft`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_nano32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
    * - :ref:`board_espressif32_microduino-core-esp32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Munich Labs
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_redpill_esp32s3`
      - External
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB

NodeMCU
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_nodemcu-32s`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Noduino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_quantum`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

OLIMEX
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32-devkitlipo`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-evb`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-gateway`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-pro`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-poe`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-poe-iso`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

OROCA
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_oroca_edubot`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Onehorse
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_onehorse32dev`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

ProtoCentral
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_healthypi4`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Pycom Ltd.
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_pycom_gpy`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lopy`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lopy4`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB
    * - :ref:`board_espressif32_wipy3`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB

Qmobot LLP
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_qchip`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

RoboticsBrno
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_alksesp32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

S.ODI
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_s_odi_ultra`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

SG-O
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_sg-o_airMon`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

SQFMI
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_watchy`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Seeed Studio
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_seeed_xiao_esp32c3`
      - External
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB

Silicognition
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_wesp32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Smart Bee
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_bee_motion`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_bee_motion_mini`
      - External
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_bee_motion_s3`
      - External
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_bee_s3`
      - External
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB

SparkFun
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_sparkfun_esp32_iot_redboard`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_sparkfun_esp32micromod`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_sparkfun_esp32s2_thing_plus_c`
      - External
      - ESP32
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_sparkfun_esp32s2_thing_plus`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_sparkfun_lora_gateway_1-channel`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

SparkFun Electronics
~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32thing`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32thing_plus`
      - External
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

TAMC
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_dpu_esp32`
      - External
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_tamc_termod_s3`
      - External
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB

TTGO
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_ttgo-lora32-v1`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-lora32-v2`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-lora32-v21`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-t-beam`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB
    * - :ref:`board_espressif32_ttgo-t-oi-plus`
      - External
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-t-watch`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-t1`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-t7-v13-mini32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB
    * - :ref:`board_espressif32_ttgo-t7-v14-mini32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB

ThaiEasyElec
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_espino32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Trueverit
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_trueverit-iot-driver`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_trueverit-iot-driver-mk2`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_trueverit-iot-driver-mk3`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Turta
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_turta_iot_node`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Unexpected Maker
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_um_feathers2`
      - External
      - ESP32S2
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_um_feathers2_neo`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_um_feathers3`
      - External
      - ESP32S3
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_um_pros3`
      - External
      - ESP32S3
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_um_rmp`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_tinypico`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_um_tinys2`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_um_tinys3`
      - External
      - ESP32S3
      - 240MHz
      - 8MB
      - 320KB

University of Sheffield
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_unphone7`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_unphone8`
      - External
      - ESP32S3
      - 240MHz
      - 7.94MB
      - 2.31MB
    * - :ref:`board_espressif32_unphone9`
      - External
      - ESP32S3
      - 240MHz
      - 7.94MB
      - 8.31MB

Unknown
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_fm-devkit`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

VintLabs
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_vintlabs-devkit-v1`
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
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_wemos_d1_mini32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wemos_d1_uno32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_c3_mini`
      - External
      - ESP32C3
      - 160MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_d32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_d32_pro`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_s2_mini`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_s2_pico`
      - External
      - ESP32S2
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_s3`
      - External
      - ESP32S3
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_lolin32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin32_lite`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wemosbat`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Widora
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_widora-air`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

Wireless-Tag
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_wt32-eth01`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

XinaBox
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_xinabox_cw02`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

YeaCreate
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_nscreen-32`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

meteca
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_briki_abc_esp32`
      - External
      - ESP32
      - 240MHz
      - 3.25MB
      - 320KB
    * - :ref:`board_espressif32_briki_mbc-wb_esp32`
      - External
      - ESP32
      - 240MHz
      - 3.25MB
      - 320KB

microS2
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_micros2`
      - External
      - ESP32S2
      - 240MHz
      - 16MB
      - 320KB

oddWires
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_iotbusio`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_iotbusproteus`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
    * - :ref:`board_espressif32_nina_w10`
      - No
      - ESP32
      - 240MHz
      - 2MB
      - 320KB

uPesy
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_upesy_wroom`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_upesy_wrover`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
