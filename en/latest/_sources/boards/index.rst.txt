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

.. _boards:

Boards
======

Rapid Embedded Development, Continuous and IDE integration in a few
steps with PlatformIO thanks to built-in project generator for the most
popular embedded boards and IDEs.

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command
    * For more detailed ``board`` information please scroll tables below by horizontal.

Aceinna IMU
-----------

.. toctree::
    :maxdepth: 1
        
    aceinna_imu/LowCostRTK
    aceinna_imu/OpenIMU335
    aceinna_imu/OpenIMU300
    aceinna_imu/OpenIMU300ZA
    aceinna_imu/OpenIMU330
    aceinna_imu/OpenRTK
    aceinna_imu/OpenRTK330L

Atmel AVR
---------

.. toctree::
    :maxdepth: 1
        
    atmelavr/AT90CAN128
    atmelavr/AT90CAN32
    atmelavr/AT90CAN64
    atmelavr/ATmega128
    atmelavr/ATmega1280
    atmelavr/ATmega1281
    atmelavr/ATmega1284
    atmelavr/ATmega1284P
    atmelavr/ATmega16
    atmelavr/ATmega162
    atmelavr/ATmega164A
    atmelavr/ATmega164P
    atmelavr/ATmega165
    atmelavr/ATmega165P
    atmelavr/ATmega168
    atmelavr/ATmega168P
    atmelavr/ATmega168PB
    atmelavr/ATmega169P
    atmelavr/ATmega169A
    atmelavr/ATmega2560
    atmelavr/ATmega2561
    atmelavr/ATmega32
    atmelavr/ATmega324A
    atmelavr/ATmega324P
    atmelavr/ATmega324PA
    atmelavr/ATmega324PB
    atmelavr/ATmega325
    atmelavr/ATmega3250
    atmelavr/ATmega3250P
    atmelavr/ATmega325P
    atmelavr/ATmega328
    atmelavr/ATmega328P
    atmelavr/ATmega328PB
    atmelavr/ATmega329
    atmelavr/ATmega3290
    atmelavr/ATmega3290P
    atmelavr/ATmega329P
    atmelavr/ATmega48
    atmelavr/ATmega48P
    atmelavr/ATmega48PB
    atmelavr/ATmega64
    atmelavr/ATmega640
    atmelavr/ATmega644A
    atmelavr/ATmega644P
    atmelavr/ATmega645
    atmelavr/ATmega6450
    atmelavr/ATmega6450P
    atmelavr/ATmega645P
    atmelavr/ATmega649
    atmelavr/ATmega6490
    atmelavr/ATmega6490P
    atmelavr/ATmega649P
    atmelavr/ATmega8
    atmelavr/ATmega8515
    atmelavr/ATmega8535
    atmelavr/ATmega88
    atmelavr/ATmega88P
    atmelavr/ATmega88PB
    atmelavr/attiny13
    atmelavr/attiny13a
    atmelavr/bluefruitmicro
    atmelavr/circuitplay_classic
    atmelavr/feather328p
    atmelavr/feather32u4
    atmelavr/flora8
    atmelavr/gemma
    atmelavr/itsybitsy32u4_3V
    atmelavr/itsybitsy32u4_5V
    atmelavr/metro
    atmelavr/protrinket3ftdi
    atmelavr/protrinket3
    atmelavr/protrinket5ftdi
    atmelavr/protrinket5
    atmelavr/trinket3
    atmelavr/trinket5
    atmelavr/alorium_hinj
    atmelavr/alorium_sno
    atmelavr/alorium_xlr8
    atmelavr/altair
    atmelavr/miniwireless
    atmelavr/arduboy
    atmelavr/arduboy_devkit
    atmelavr/btatmega168
    atmelavr/btatmega328
    atmelavr/diecimilaatmega168
    atmelavr/diecimilaatmega328
    atmelavr/esplora
    atmelavr/ethernet
    atmelavr/fio
    atmelavr/chiwawa
    atmelavr/leonardo
    atmelavr/leonardoeth
    atmelavr/lilypadatmega168
    atmelavr/lilypadatmega328
    atmelavr/LilyPadUSB
    atmelavr/megaADK
    atmelavr/megaatmega1280
    atmelavr/megaatmega2560
    atmelavr/micro
    atmelavr/miniatmega168
    atmelavr/miniatmega328
    atmelavr/atmegangatmega168
    atmelavr/atmegangatmega8
    atmelavr/nanoatmega168
    atmelavr/nanoatmega328
    atmelavr/nanoatmega328new
    atmelavr/pro8MHzatmega168
    atmelavr/pro16MHzatmega168
    atmelavr/pro8MHzatmega328
    atmelavr/pro16MHzatmega328
    atmelavr/robotControl
    atmelavr/robotMotor
    atmelavr/uno
    atmelavr/uno_mini
    atmelavr/yun
    atmelavr/yunmini
    atmelavr/at90pwm216
    atmelavr/at90pwm316
    atmelavr/zumbt328
    atmelavr/raspduino
    atmelavr/controllino_maxi
    atmelavr/controllino_maxi_automation
    atmelavr/controllino_mega
    atmelavr/controllino_mini
    atmelavr/digispark-pro
    atmelavr/digispark-pro64
    atmelavr/digispark-pro32
    atmelavr/digispark-tiny
    atmelavr/dwenguino
    atmelavr/elektor_uno_r4
    atmelavr/engduinov3
    atmelavr/mayfly
    atmelavr/fysetc_f6_13
    atmelavr/attiny1634
    atmelavr/attiny167
    atmelavr/attiny2313
    atmelavr/attiny24
    atmelavr/attiny25
    atmelavr/attiny261
    atmelavr/attiny4313
    atmelavr/attiny43
    atmelavr/attiny44
    atmelavr/attiny441
    atmelavr/attiny45
    atmelavr/attiny461
    atmelavr/attiny48
    atmelavr/attiny828
    atmelavr/attiny84
    atmelavr/attiny841
    atmelavr/attiny85
    atmelavr/attiny861
    atmelavr/attiny87
    atmelavr/attiny88
    atmelavr/lightblue-bean
    atmelavr/lightblue-beanplus
    atmelavr/lightup
    atmelavr/one
    atmelavr/smart7688
    atmelavr/lora32u4II
    atmelavr/mightyhat
    atmelavr/moteino
    atmelavr/moteino8mhz
    atmelavr/moteinomega
    atmelavr/168pa16m
    atmelavr/168pa8m
    atmelavr/328p16m
    atmelavr/328p8m
    atmelavr/32u416m
    atmelavr/1284p16m
    atmelavr/1284p8m
    atmelavr/644pa16m
    atmelavr/644pa8m
    atmelavr/emonpi
    atmelavr/prusa_mm_control
    atmelavr/panStampAVR
    atmelavr/pinoccio
    atmelavr/a-star32U4
    atmelavr/prusa_rambo
    atmelavr/quirkbot
    atmelavr/blend
    atmelavr/blendmicro16
    atmelavr/blendmicro8
    atmelavr/reprap_rambo
    atmelavr/sodaq_galora
    atmelavr/sodaq_mbili
    atmelavr/sodaq_moja
    atmelavr/sodaq_ndogo
    atmelavr/sodaq_tatu
    atmelavr/sanguino_atmega1284p
    atmelavr/sanguino_atmega1284_8m
    atmelavr/sanguino_atmega644
    atmelavr/sanguino_atmega644_8m
    atmelavr/sanguino_atmega644p
    atmelavr/sanguino_atmega644p_8m
    atmelavr/seeeduino
    atmelavr/sparkfun_satmega128rfa1
    atmelavr/sparkfun_digitalsandbox
    atmelavr/sparkfun_fiov3
    atmelavr/sparkfun_makeymakey
    atmelavr/sparkfun_megapro8MHz
    atmelavr/sparkfun_megapro16MHz
    atmelavr/sparkfun_megamini
    atmelavr/uview
    atmelavr/sparkfun_promicro8
    atmelavr/sparkfun_promicro16
    atmelavr/sparkfun_qduinomini
    atmelavr/sparkfun_redboard
    atmelavr/sparkfun_serial7seg
    atmelavr/sleepypi
    atmelavr/whispernode
    atmelavr/the_things_uno
    atmelavr/tinyduino
    atmelavr/tinylily
    atmelavr/usbasp
    atmelavr/wildfirev2
    atmelavr/wildfirev3
    atmelavr/ftduino
    atmelavr/bob3
    atmelavr/nibo2
    atmelavr/niboburger
    atmelavr/niboburger_1284
    atmelavr/nibobee
    atmelavr/nibobee_1284
    atmelavr/ardhat

Atmel megaAVR
-------------

.. toctree::
    :maxdepth: 1
        
    atmelmegaavr/ATmega1608
    atmelmegaavr/ATmega1609
    atmelmegaavr/ATmega3208
    atmelmegaavr/ATmega3209
    atmelmegaavr/ATmega4808
    atmelmegaavr/ATmega4809
    atmelmegaavr/ATmega808
    atmelmegaavr/ATmega809
    atmelmegaavr/ATtiny1604
    atmelmegaavr/ATtiny1606
    atmelmegaavr/ATtiny1607
    atmelmegaavr/ATtiny1614
    atmelmegaavr/ATtiny1616
    atmelmegaavr/ATtiny1617
    atmelmegaavr/ATtiny1624
    atmelmegaavr/ATtiny1626
    atmelmegaavr/ATtiny1627
    atmelmegaavr/ATtiny202
    atmelmegaavr/ATtiny204
    atmelmegaavr/ATtiny212
    atmelmegaavr/ATtiny214
    atmelmegaavr/ATtiny3216
    atmelmegaavr/ATtiny3217
    atmelmegaavr/ATtiny3224
    atmelmegaavr/ATtiny3226
    atmelmegaavr/ATtiny3227
    atmelmegaavr/ATtiny402
    atmelmegaavr/ATtiny404
    atmelmegaavr/ATtiny406
    atmelmegaavr/ATtiny412
    atmelmegaavr/ATtiny414
    atmelmegaavr/ATtiny416
    atmelmegaavr/ATtiny417
    atmelmegaavr/ATtiny424
    atmelmegaavr/ATtiny426
    atmelmegaavr/ATtiny427
    atmelmegaavr/ATtiny804
    atmelmegaavr/ATtiny806
    atmelmegaavr/ATtiny807
    atmelmegaavr/ATtiny814
    atmelmegaavr/ATtiny816
    atmelmegaavr/ATtiny817
    atmelmegaavr/ATtiny824
    atmelmegaavr/ATtiny826
    atmelmegaavr/ATtiny827
    atmelmegaavr/avr_iot_wg
    atmelmegaavr/AVR128DA28
    atmelmegaavr/AVR128DA32
    atmelmegaavr/AVR128DA48
    atmelmegaavr/AVR128DA64
    atmelmegaavr/AVR128DB28
    atmelmegaavr/AVR128DB32
    atmelmegaavr/AVR128DB48
    atmelmegaavr/AVR128DB64
    atmelmegaavr/AVR32DA28
    atmelmegaavr/AVR32DA32
    atmelmegaavr/AVR32DA48
    atmelmegaavr/AVR32DB28
    atmelmegaavr/AVR32DB32
    atmelmegaavr/AVR32DB48
    atmelmegaavr/AVR64DA28
    atmelmegaavr/AVR64DA32
    atmelmegaavr/AVR64DA48
    atmelmegaavr/AVR64DA64
    atmelmegaavr/AVR64DB28
    atmelmegaavr/AVR64DB32
    atmelmegaavr/AVR64DB48
    atmelmegaavr/AVR64DB64
    atmelmegaavr/AVR64DD14
    atmelmegaavr/AVR64DD20
    atmelmegaavr/AVR64DD28
    atmelmegaavr/AVR64DD32
    atmelmegaavr/nano_every
    atmelmegaavr/uno_wifi_rev2
    atmelmegaavr/curiosity_nano_4809
    atmelmegaavr/curiosity_nano_da
    atmelmegaavr/curiosity_nano_db
    atmelmegaavr/xplained_pro_4809

Atmel SAM
---------

.. toctree::
    :maxdepth: 1
        
    atmelsam/adafruit_blm_badge
    atmelsam/adafruit_circuitplayground_m0
    atmelsam/adafruit_crickit_m0
    atmelsam/adafruit_feather_m0
    atmelsam/adafruit_feather_m0_express
    atmelsam/adafruit_feather_m4_can
    atmelsam/adafruit_feather_m4
    atmelsam/adafruit_gemma_m0
    atmelsam/adafruit_grandcentral_m4
    atmelsam/adafruit_hallowing
    atmelsam/adafruit_hallowing_m4
    atmelsam/adafruit_itsybitsy_m0
    atmelsam/adafruit_itsybitsy_m4
    atmelsam/adafruit_monster_m4sk
    atmelsam/adafruit_matrix_portal_m4
    atmelsam/adafruit_metro_m0
    atmelsam/adafruit_metro_m4
    atmelsam/adafruit_metro_m4_airliftlite
    atmelsam/adafruit_neokeytrinkey_m0
    atmelsam/adafruit_neotrinkey_m0
    atmelsam/adafruit_proxlighttrinkey_m0
    atmelsam/adafruit_pygamer_advance_m4
    atmelsam/adafruit_pygamer_m4
    atmelsam/adafruit_pyportal_m4
    atmelsam/adafruit_pyportal_m4_titano
    atmelsam/adafruit_qt_py_m0
    atmelsam/adafruit_rotarytrinkey_m0
    atmelsam/adafruit_slidetrinkey_m0
    atmelsam/adafruit_trellis_m4
    atmelsam/adafruit_trinket_m0
    atmelsam/adafruit_pirkey
    atmelsam/adafruit_pybadge_airlift_m4
    atmelsam/adafruit_pybadge_m4
    atmelsam/due
    atmelsam/dueUSB
    atmelsam/mzeroUSB
    atmelsam/mzeroproUSB
    atmelsam/mzeropro
    atmelsam/mkrfox1200
    atmelsam/mkrgsm1400
    atmelsam/mkrnb1500
    atmelsam/mkrwan1300
    atmelsam/mkrwan1310
    atmelsam/mkrwifi1010
    atmelsam/mkr1000USB
    atmelsam/mkrzero
    atmelsam/tian
    atmelsam/zero
    atmelsam/zeroUSB
    atmelsam/samr21_xpro
    atmelsam/samd21g18a
    atmelsam/samc21_xpro
    atmelsam/samd21_xpro
    atmelsam/digix
    atmelsam/current_ranger
    atmelsam/mkrvidor4000
    atmelsam/minitronics20
    atmelsam/moteino_zero
    atmelsam/nano_33_iot
    atmelsam/sodaq_autonomo
    atmelsam/sodaq_explorer
    atmelsam/sodaq_one
    atmelsam/sodaq_sara
    atmelsam/sodaq_sff
    atmelsam/sainSmartDue
    atmelsam/sainSmartDueUSB
    atmelsam/seeed_femto
    atmelsam/seeeduino_lorawan
    atmelsam/seeed_wio_lite_mg126
    atmelsam/seeed_wio_terminal
    atmelsam/seeed_xiao
    atmelsam/seeed_zero
    atmelsam/sparkfun_samd21_9dof
    atmelsam/sparkfun_qwiic_micro_samd21e
    atmelsam/sparkfun_redboard_turbo
    atmelsam/sparkfun_samd21_dev_usb
    atmelsam/sparkfun_samd21_mini_usb
    atmelsam/sparkfun_samd21_proRF
    atmelsam/sparkfun_samd51_micromod
    atmelsam/sparkfun_samd51_thing_plus
    atmelsam/tuinozero96

CHIPS Alliance
--------------

.. toctree::
    :maxdepth: 1
        
    chipsalliance/swervolf_nexys

Espressif 32
------------

.. toctree::
    :maxdepth: 1
        
    espressif32/4d_systems_esp32s3_gen4_r8n16
    espressif32/esp32cam
    espressif32/alksesp32
    espressif32/az-delivery-devkit-v4
    espressif32/featheresp32
    espressif32/featheresp32-s2
    espressif32/adafruit_feather_esp32_v2
    espressif32/adafruit_feather_esp32s2
    espressif32/adafruit_feather_esp32s2_reversetft
    espressif32/adafruit_feather_esp32s2_tft
    espressif32/adafruit_feather_esp32s3
    espressif32/adafruit_feather_esp32s3_nopsram
    espressif32/adafruit_feather_esp32s3_reversetft
    espressif32/adafruit_feather_esp32s3_tft
    espressif32/adafruit_funhouse_esp32s2
    espressif32/adafruit_itsybitsy_esp32
    espressif32/adafruit_magtag29_esp32s2
    espressif32/adafruit_matrixportal_esp32s3
    espressif32/adafruit_metro_esp32s2
    espressif32/adafruit_metro_esp32s3
    espressif32/adafruit_qtpy_esp32
    espressif32/adafruit_qtpy_esp32c3
    espressif32/adafruit_qtpy_esp32s2
    espressif32/adafruit_qtpy_esp32s3_n4r2
    espressif32/adafruit_qtpy_esp32s3_nopsram
    espressif32/adafruit_qualia_s3_rgb666
    espressif32/adafruit_camera_esp32s3
    espressif32/esp32-c3-m1i-kit
    espressif32/nodemcu-32s2
    espressif32/airm2m_core_esp32c3
    espressif32/espea32
    espressif32/arduino_nano_esp32
    espressif32/atd147_s3
    espressif32/ioxesp32
    espressif32/ioxesp32ps
    espressif32/aventen_s3_sync
    espressif32/bpi-bit
    espressif32/bpi_leaf_s3
    espressif32/wifiduino32
    espressif32/wifiduino32s3
    espressif32/wifiduino32c3
    espressif32/cnrs_aw2eth
    espressif32/connaxio_espoir
    espressif32/cytron_maker_feather_aiot_s3
    espressif32/d-duino-32
    espressif32/dfrobot_beetle_esp32c3
    espressif32/dfrobot_firebeetle2_esp32e
    espressif32/dfrobot_firebeetle2_esp32s3
    espressif32/dfrobot_romeo_esp32s3
    espressif32/esp32doit-devkit-v1
    espressif32/esp32doit-espduino
    espressif32/deneyapkart
    espressif32/deneyapkart1A
    espressif32/deneyapkart1Av2
    espressif32/deneyapkartg
    espressif32/deneyapmini
    espressif32/deneyapminiv2
    espressif32/denky_d4
    espressif32/denky32
    espressif32/minimain_esp32s2
    espressif32/pocket_32
    espressif32/fm-devkit
    espressif32/pico32
    espressif32/esp32s3_powerfeather
    espressif32/esp32s3camlcd
    espressif32/esp32vn-iot-uno
    espressif32/espectro32
    espressif32/espino32
    espressif32/etboard
    espressif32/esp320
    espressif32/atmegazero_esp32s2
    espressif32/esp-wrover-kit
    espressif32/esp32dev
    espressif32/esp32-c3-devkitc-02
    espressif32/esp32-c3-devkitm-1
    espressif32/esp32-c6-devkitc-1
    espressif32/esp32-c6-devkitm-1
    espressif32/esp32-pico-devkitm-2
    espressif32/esp32-s2-kaluga-1
    espressif32/esp32-s2-saola-1
    espressif32/esp32s3box
    espressif32/esp32-s3-devkitc-1
    espressif32/esp32-s3-devkitm-1
    espressif32/esp32s3usbotg
    espressif32/firebeetle32
    espressif32/piranha_esp32
    espressif32/franzininho_wifi_esp32s2
    espressif32/esp32-s2-franzininho
    espressif32/franzininho_wifi_msc_esp32s2
    espressif32/freenove_esp32_s3_wroom
    espressif32/freenove_esp32_wrover
    espressif32/frogboard
    espressif32/honeylemon
    espressif32/heltec_wifi_kit_32
    espressif32/heltec_wifi_kit_32_v2
    espressif32/heltec_wifi_kit_32_V3
    espressif32/heltec_wifi_lora_32
    espressif32/heltec_wifi_lora_32_V2
    espressif32/heltec_wifi_lora_32_V3
    espressif32/heltec_wireless_stick
    espressif32/heltec_wireless_stick_lite
    espressif32/hornbill32dev
    espressif32/hornbill32minima
    espressif32/inex_openkb
    espressif32/imbrios-logsens-v1p1
    espressif32/intorobot
    espressif32/iotaap_magnolia
    espressif32/kits-edu
    espressif32/nebulas3
    espressif32/sensesiot_weizen
    espressif32/labplus_mpython
    espressif32/lilka_v2
    espressif32/lilygo-t-display
    espressif32/lilygo-t-display-s3
    espressif32/lilygo-t3-s3
    espressif32/lionbit
    espressif32/lionbits3
    espressif32/m5stack-atoms3
    espressif32/m5stack-core-esp32
    espressif32/m5stack-core-esp32-16M
    espressif32/m5stack-core2
    espressif32/m5stack-cores3
    espressif32/m5stack-fire
    espressif32/m5stack-grey
    espressif32/m5stack-stamps3
    espressif32/m5stack-station
    espressif32/m5stack-timer-cam
    espressif32/m5stack-atom
    espressif32/m5stack-coreink
    espressif32/m5stamp-pico
    espressif32/m5stick-c
    espressif32/mgbot-iotik32a
    espressif32/mgbot-iotik32b
    espressif32/mhetesp32devkit
    espressif32/mhetesp32minikit
    espressif32/magicbit
    espressif32/kb32-ft
    espressif32/nano32
    espressif32/microduino-core-esp32
    espressif32/motorgo_mini_1
    espressif32/redpill_esp32s3
    espressif32/namino_arancio
    espressif32/namino_rosso
    espressif32/node32s
    espressif32/nodemcu-32s
    espressif32/quantum
    espressif32/odroid_esp32
    espressif32/esp32-devkitlipo
    espressif32/esp32-evb
    espressif32/esp32-gateway
    espressif32/esp32-pro
    espressif32/esp32-poe
    espressif32/esp32-poe-iso
    espressif32/oroca_edubot
    espressif32/onehorse32dev
    espressif32/healthypi4
    espressif32/pycom_gpy
    espressif32/lopy
    espressif32/lopy4
    espressif32/wipy3
    espressif32/qchip
    espressif32/rymcu-esp32-c3-devkitm-1
    espressif32/rymcu-esp32-devkitc
    espressif32/rymcu-esp32-s3-devkitc-1
    espressif32/roboheart_hercules
    espressif32/s_odi_ultra
    espressif32/sg-o_airMon
    espressif32/watchy
    espressif32/edgebox-esp-100
    espressif32/seeed_xiao_esp32c3
    espressif32/seeed_xiao_esp32s3
    espressif32/wesp32
    espressif32/bee_data_logger
    espressif32/bee_motion
    espressif32/bee_motion_mini
    espressif32/bee_motion_s3
    espressif32/bee_s3
    espressif32/sparkfun_esp32_iot_redboard
    espressif32/sparkfun_esp32micromod
    espressif32/esp32thing
    espressif32/esp32thing_plus
    espressif32/sparkfun_esp32s2_thing_plus_c
    espressif32/sparkfun_esp32s2_thing_plus
    espressif32/sparkfun_lora_gateway_1-channel
    espressif32/dpu_esp32
    espressif32/tamc_termod_s3
    espressif32/ttgo-lora32-v1
    espressif32/ttgo-lora32-v2
    espressif32/ttgo-lora32-v21
    espressif32/ttgo-t-beam
    espressif32/ttgo-t-oi-plus
    espressif32/ttgo-t-watch
    espressif32/ttgo-t1
    espressif32/ttgo-t7-v13-mini32
    espressif32/ttgo-t7-v14-mini32
    espressif32/trueverit-iot-driver
    espressif32/trueverit-iot-driver-mk2
    espressif32/trueverit-iot-driver-mk3
    espressif32/turta_iot_node
    espressif32/um_feathers2
    espressif32/um_feathers2_neo
    espressif32/um_feathers3
    espressif32/um_nanos3
    espressif32/um_pros3
    espressif32/um_rmp
    espressif32/tinypico
    espressif32/um_tinys2
    espressif32/um_tinys3
    espressif32/valtrack_v4_mfw_esp32_c3
    espressif32/valtrack_v4_vts_esp32_c3
    espressif32/vintlabs-devkit-v1
    espressif32/wemos_d1_mini32
    espressif32/wemos_d1_uno32
    espressif32/lolin_c3_mini
    espressif32/lolin_d32
    espressif32/lolin_d32_pro
    espressif32/lolin_s2_mini
    espressif32/lolin_s2_pico
    espressif32/lolin_s3
    espressif32/lolin_s3_mini
    espressif32/lolin_s3_pro
    espressif32/lolin32
    espressif32/lolin32_lite
    espressif32/weactstudio_esp32c3coreboard
    espressif32/wemosbat
    espressif32/widora-air
    espressif32/wt32-eth01
    espressif32/xinabox_cw02
    espressif32/nscreen-32
    espressif32/micros2
    espressif32/iotbusio
    espressif32/iotbusproteus
    espressif32/sensebox_mcu_esp32s2
    espressif32/nina_w10
    espressif32/upesy_wroom
    espressif32/upesy_wrover
    espressif32/unphone7
    espressif32/unphone8
    espressif32/unphone9

Espressif 8266
--------------

.. toctree::
    :maxdepth: 1
        
    espressif8266/gen4iod
    espressif8266/huzzah
    espressif8266/oak
    espressif8266/espmxdevkit
    espressif8266/espduino
    espressif8266/espectro
    espressif8266/espino
    espressif8266/espresso_lite_v1
    espressif8266/espresso_lite_v2
    espressif8266/esp_wroom_02
    espressif8266/esp12e
    espressif8266/esp01_1m
    espressif8266/esp01
    espressif8266/esp07
    espressif8266/esp07s
    espressif8266/esp8285
    espressif8266/heltec_wifi_kit_8
    espressif8266/inventone
    espressif8266/agruminolemon
    espressif8266/nodemcu
    espressif8266/nodemcuv2
    espressif8266/modwifi
    espressif8266/phoenix_v1
    espressif8266/phoenix_v2
    espressif8266/eduinowifi
    espressif8266/sonoff_basic
    espressif8266/sonoff_s20
    espressif8266/sonoff_sv
    espressif8266/sonoff_th
    espressif8266/sparkfunBlynk
    espressif8266/thing
    espressif8266/thingdev
    espressif8266/esp210
    espressif8266/espinotee
    espressif8266/d1
    espressif8266/d1_wroom_02
    espressif8266/d1_mini
    espressif8266/d1_mini_lite
    espressif8266/d1_mini_pro
    espressif8266/wifi_slot
    espressif8266/wifiduino
    espressif8266/wifinfo
    espressif8266/wio_link
    espressif8266/wio_node
    espressif8266/xinabox_cw01

Freescale Kinetis
-----------------

.. toctree::
    :maxdepth: 1
        
    freescalekinetis/IBMEthernetKit
    freescalekinetis/frdm_k22f
    freescalekinetis/frdm_k64f
    freescalekinetis/frdm_k66f
    freescalekinetis/frdm_k82f
    freescalekinetis/frdm_kl25z
    freescalekinetis/frdm_kl43z
    freescalekinetis/frdm_kl46z
    freescalekinetis/frdm_kw24d
    freescalekinetis/frdm_kw41z
    freescalekinetis/hexiwear
    freescalekinetis/segger_ip_switch

Heltec CubeCell
---------------

.. toctree::
    :maxdepth: 1
        
    heltec-cubecell/cubecell_capsule_solar_sensor
    heltec-cubecell/cubecell_node
    heltec-cubecell/cubecell_board
    heltec-cubecell/cubecell_board_pro
    heltec-cubecell/cubecell_board_plus
    heltec-cubecell/cubecell_board_v2
    heltec-cubecell/cubecell_capsule
    heltec-cubecell/cubecell_gps
    heltec-cubecell/cubecell_module
    heltec-cubecell/cubecell_module_plus
    heltec-cubecell/cubecell_module_v2

Intel ARC32
-----------

.. toctree::
    :maxdepth: 1
        
    intel_arc32/genuino101

Intel MCS-51 (8051)
-------------------

.. toctree::
    :maxdepth: 1
        
    intel_mcs51/CH559
    intel_mcs51/Generic8051
    intel_mcs51/Generic8052
    intel_mcs51/AT89S51
    intel_mcs51/AT89S52
    intel_mcs51/IAP12C5A62S2
    intel_mcs51/IAP15F106
    intel_mcs51/IAP15F206A
    intel_mcs51/IAP15F2K61S
    intel_mcs51/IAP15F2K61S2
    intel_mcs51/IAP15F413AD
    intel_mcs51/IAP15W105
    intel_mcs51/IAP15W1K29S
    intel_mcs51/IAP15W205S
    intel_mcs51/IAP15W413AS
    intel_mcs51/IAP15W413S
    intel_mcs51/IAP15W4K58S4
    intel_mcs51/IAP15W4K61S4
    intel_mcs51/IAP15W4K63S4
    intel_mcs51/IRC15F107W
    intel_mcs51/IRC15F2K63S2
    intel_mcs51/IRC15W107
    intel_mcs51/IRC15W1K31S
    intel_mcs51/IRC15W207S
    intel_mcs51/IRC15W415AS
    intel_mcs51/IRC15W415S
    intel_mcs51/ML51BB9AE
    intel_mcs51/ML51DB9AE
    intel_mcs51/ML51EB9AE
    intel_mcs51/ML51EC0AE
    intel_mcs51/ML51FB9AE
    intel_mcs51/ML51LD1AE
    intel_mcs51/ML51OB9AE
    intel_mcs51/ML51PB9AE
    intel_mcs51/ML51PC0AE
    intel_mcs51/ML51SD1AE
    intel_mcs51/ML51TB9AE
    intel_mcs51/ML51TC0AE
    intel_mcs51/ML51TC1AE
    intel_mcs51/ML51TD1AE
    intel_mcs51/ML51UB9AE
    intel_mcs51/ML51UC0AE
    intel_mcs51/ML51XB9AE
    intel_mcs51/ML54LD1AE
    intel_mcs51/ML54MD1AE
    intel_mcs51/ML54SD1AE
    intel_mcs51/ML56LD1AE
    intel_mcs51/ML56MD1AE
    intel_mcs51/ML56SD1AE
    intel_mcs51/MS51BA9AE
    intel_mcs51/MS51DA9AE
    intel_mcs51/MS51EC0AE
    intel_mcs51/MS51FB9AE
    intel_mcs51/MS51FC0AE
    intel_mcs51/MS51IA9AE
    intel_mcs51/MS51PC0AE
    intel_mcs51/MS51TC0AE
    intel_mcs51/MS51XB9AE
    intel_mcs51/MS51XB9BE
    intel_mcs51/MS51XC0BE
    intel_mcs51/N76E003
    intel_mcs51/N76E616
    intel_mcs51/N76E885
    intel_mcs51/N78E055
    intel_mcs51/N78E059
    intel_mcs51/N78E366
    intel_mcs51/N78E517
    intel_mcs51/N79E352
    intel_mcs51/N79E715
    intel_mcs51/N79E813
    intel_mcs51/N79E8132
    intel_mcs51/N79E814
    intel_mcs51/N79E815
    intel_mcs51/N79E822
    intel_mcs51/N79E823
    intel_mcs51/N79E824
    intel_mcs51/N79E825
    intel_mcs51/N79E843
    intel_mcs51/N79E8432
    intel_mcs51/N79E844
    intel_mcs51/N79E845
    intel_mcs51/N79E854
    intel_mcs51/N79E855
    intel_mcs51/N79E875
    intel_mcs51/STC12C5A08S2
    intel_mcs51/STC12C5A16S2
    intel_mcs51/STC12C5A32S2
    intel_mcs51/STC12C5A40S2
    intel_mcs51/STC12C5A48S2
    intel_mcs51/STC12C5A52S2
    intel_mcs51/STC12C5A56S2
    intel_mcs51/STC12C5A60S2
    intel_mcs51/STC15F100
    intel_mcs51/STC15F100W
    intel_mcs51/STC15F101
    intel_mcs51/STC15F101E
    intel_mcs51/STC15F101W
    intel_mcs51/STC15F102
    intel_mcs51/STC15F102E
    intel_mcs51/STC15F102W
    intel_mcs51/STC15F103
    intel_mcs51/STC15F103E
    intel_mcs51/STC15F103W
    intel_mcs51/STC15F104
    intel_mcs51/STC15F104E
    intel_mcs51/STC15F104W
    intel_mcs51/STC15F105
    intel_mcs51/STC15F105E
    intel_mcs51/STC15F105W
    intel_mcs51/STC15F201A
    intel_mcs51/STC15F201EA
    intel_mcs51/STC15F202A
    intel_mcs51/STC15F202EA
    intel_mcs51/STC15F203A
    intel_mcs51/STC15F203EA
    intel_mcs51/STC15F204A
    intel_mcs51/STC15F204EA
    intel_mcs51/STC15F205A
    intel_mcs51/STC15F205EA
    intel_mcs51/STC15F2K08S2
    intel_mcs51/STC15F2K16S2
    intel_mcs51/STC15F2K24AS
    intel_mcs51/STC15F2K24S2
    intel_mcs51/STC15F2K32S2
    intel_mcs51/STC15F2K40S2
    intel_mcs51/STC15F2K48S2
    intel_mcs51/STC15F2K52S2
    intel_mcs51/STC15F2K56S2
    intel_mcs51/STC15F2K60S2
    intel_mcs51/STC15F408AD
    intel_mcs51/STC15W100
    intel_mcs51/STC15W101
    intel_mcs51/STC15W102
    intel_mcs51/STC15W103
    intel_mcs51/STC15W104
    intel_mcs51/STC15W1K16S
    intel_mcs51/STC15W1K20S
    intel_mcs51/STC15W1K24S
    intel_mcs51/STC15W201S
    intel_mcs51/STC15W202S
    intel_mcs51/STC15W203S
    intel_mcs51/STC15W204S
    intel_mcs51/STC15W401AS
    intel_mcs51/STC15W402AS
    intel_mcs51/STC15W404AS
    intel_mcs51/STC15W404S
    intel_mcs51/STC15W408AS
    intel_mcs51/STC15W408S
    intel_mcs51/STC15W410S
    intel_mcs51/STC15W4K16S4
    intel_mcs51/STC15W4K32S4
    intel_mcs51/STC15W4K40S4
    intel_mcs51/STC15W4K48S4
    intel_mcs51/STC15W4K56S4
    intel_mcs51/STC89C516RD+
    intel_mcs51/STC89C51RC
    intel_mcs51/STC89C52RC
    intel_mcs51/STC89C53RC
    intel_mcs51/STC89C54RD+
    intel_mcs51/STC89C58RD+
    intel_mcs51/STC8A4K16S2A12
    intel_mcs51/STC8A4K32S2A12
    intel_mcs51/STC8A4K60S2A12
    intel_mcs51/STC8A4K64S2A12
    intel_mcs51/STC8A8K16D4
    intel_mcs51/STC8A8K16S4A12
    intel_mcs51/STC8A8K32D4
    intel_mcs51/STC8A8K32S4A12
    intel_mcs51/STC8A8K60D4
    intel_mcs51/STC8A8K60S4A12
    intel_mcs51/STC8A8K64D4
    intel_mcs51/STC8A8K64S4A12
    intel_mcs51/STC8C1K08
    intel_mcs51/STC8C1K12
    intel_mcs51/STC8C2K16S2
    intel_mcs51/STC8C2K16S4
    intel_mcs51/STC8C2K32S2
    intel_mcs51/STC8C2K32S4
    intel_mcs51/STC8C2K60S2
    intel_mcs51/STC8C2K60S4
    intel_mcs51/STC8C2K64S2
    intel_mcs51/STC8C2K64S4
    intel_mcs51/STC8F1K08
    intel_mcs51/STC8F1K08S
    intel_mcs51/STC8F1K08S2
    intel_mcs51/STC8F1K08S2A10
    intel_mcs51/STC8F1K17
    intel_mcs51/STC8F1K17S2
    intel_mcs51/STC8F2K08S2
    intel_mcs51/STC8F2K16S2
    intel_mcs51/STC8F2K16S4
    intel_mcs51/STC8F2K32S2
    intel_mcs51/STC8F2K32S4
    intel_mcs51/STC8F2K60S2
    intel_mcs51/STC8F2K60S4
    intel_mcs51/STC8F2K64S2
    intel_mcs51/STC8F2K64S4
    intel_mcs51/STC8G1K08
    intel_mcs51/STC8G1K08A
    intel_mcs51/STC8G1K08T
    intel_mcs51/STC8G1K12
    intel_mcs51/STC8G1K12A
    intel_mcs51/STC8G1K17
    intel_mcs51/STC8G1K17A
    intel_mcs51/STC8G1K17T
    intel_mcs51/STC8G2K16S2
    intel_mcs51/STC8G2K16S4
    intel_mcs51/STC8G2K32S2
    intel_mcs51/STC8G2K32S4
    intel_mcs51/STC8G2K60S2
    intel_mcs51/STC8G2K60S4
    intel_mcs51/STC8G2K64S2
    intel_mcs51/STC8G2K64S4
    intel_mcs51/STC8H04
    intel_mcs51/STC8H04A10
    intel_mcs51/STC8H1K08
    intel_mcs51/STC8H1K08S2
    intel_mcs51/STC8H1K08S2A10
    intel_mcs51/STC8H1K12
    intel_mcs51/STC8H1K16
    intel_mcs51/STC8H1K16S2
    intel_mcs51/STC8H1K16S2A10
    intel_mcs51/STC8H1K17
    intel_mcs51/STC8H1K24
    intel_mcs51/STC8H1K28
    intel_mcs51/STC8H1K32S2
    intel_mcs51/STC8H1K32S2A10
    intel_mcs51/STC8H1K33
    intel_mcs51/STC8H1K64S2A10
    intel_mcs51/STC8H2K32T
    intel_mcs51/STC8H2K48T
    intel_mcs51/STC8H2K60T
    intel_mcs51/STC8H2K64T
    intel_mcs51/STC8H3K32S2
    intel_mcs51/STC8H3K32S4
    intel_mcs51/STC8H3K48S2
    intel_mcs51/STC8H3K48S4
    intel_mcs51/STC8H3K60S2
    intel_mcs51/STC8H3K60S4
    intel_mcs51/STC8H3K64S2
    intel_mcs51/STC8H3K64S4
    intel_mcs51/STC8H4K32LCD
    intel_mcs51/STC8H4K32TLCD
    intel_mcs51/STC8H4K32TLR
    intel_mcs51/STC8H4K48LCD
    intel_mcs51/STC8H4K48TLCD
    intel_mcs51/STC8H4K48TLR
    intel_mcs51/STC8H4K60LCD
    intel_mcs51/STC8H4K60TLCD
    intel_mcs51/STC8H4K60TLR
    intel_mcs51/STC8H4K64LCD
    intel_mcs51/STC8H4K64TLCD
    intel_mcs51/STC8H4K64TLR
    intel_mcs51/STC8H8K32U
    intel_mcs51/STC8H8K48U
    intel_mcs51/STC8H8K60U
    intel_mcs51/STC8H8K64U
    intel_mcs51/W79E2051
    intel_mcs51/W79E4051
    intel_mcs51/W79E632
    intel_mcs51/W79E633
    intel_mcs51/W79E658
    intel_mcs51/W79E659
    intel_mcs51/W79E8213

Lattice iCE40
-------------

.. toctree::
    :maxdepth: 1
        
    lattice_ice40/icezum
    lattice_ice40/icestick

Linux ARM
---------

.. toctree::
    :maxdepth: 1
        
    linux_arm/raspberrypi_1b
    linux_arm/raspberrypi_2b
    linux_arm/raspberrypi_3b
    linux_arm/raspberrypi_zero

Maxim 32
--------

.. toctree::
    :maxdepth: 1
        
    maxim32/max32620fthr
    maxim32/max32625mbed
    maxim32/max32625pico
    maxim32/max32600mbed
    maxim32/max32620hsp
    maxim32/max32630fthr
    maxim32/maxwsnenv
    maxim32/sdt32620b
    maxim32/sdt32625b

Microchip PIC32
---------------

.. toctree::
    :maxdepth: 1
        
    microchippic32/picadillo_35t
    microchippic32/dsmini
    microchippic32/cerebot32mx4
    microchippic32/cerebot32mx7
    microchippic32/openscope
    microchippic32/chipkit_cmod
    microchippic32/chipkit_dp32
    microchippic32/mega_pic32
    microchippic32/chipkit_mx3
    microchippic32/chipkit_pro_mx4
    microchippic32/chipkit_pro_mx7
    microchippic32/uno_pic32
    microchippic32/chipkit_wf32
    microchippic32/chipkit_wifire
    microchippic32/chipkit_uc32
    microchippic32/chipkit_pi
    microchippic32/fubarino_mini
    microchippic32/fubarino_sd
    microchippic32/helvepic32
    microchippic32/helvepic32_breadboardside
    microchippic32/helvepic32_smd
    microchippic32/helvepic32_mx270
    microchippic32/helvepic32_robot
    microchippic32/helvepic32_smd_mx270
    microchippic32/clicker2
    microchippic32/flipnclickmz
    microchippic32/fubarino_mini_20
    microchippic32/pinguino32
    microchippic32/openbci
    microchippic32/usbono_pic32
    microchippic32/cui32
    microchippic32/nofire
    microchippic32/quick240_usb
    microchippic32/rgb_station
    microchippic32/cui32stem
    microchippic32/ubw32_mx460
    microchippic32/ubw32_mx795
    microchippic32/lenny
    microchippic32/chipkit_wifire_revc

Nordic nRF51
------------

.. toctree::
    :maxdepth: 1
        
    nordicnrf51/bbcmicrobit
    nordicnrf51/bluz_dk
    nordicnrf51/calliope_mini
    nordicnrf51/nrf51_beacon
    nordicnrf51/nrf51_dongle
    nordicnrf51/nrf51_dk
    nordicnrf51/oshchip
    nordicnrf51/redBearLabBLENano
    nordicnrf51/redBearLab
    nordicnrf51/seeedTinyBLE
    nordicnrf51/Sinobit
    nordicnrf51/vbluno51
    nordicnrf51/waveshare_ble400
    nordicnrf51/ng_beacon

Nordic nRF52
------------

.. toctree::
    :maxdepth: 1
        
    nordicnrf52/96b_nitrogen
    nordicnrf52/adafruit_feather_nrf52832
    nordicnrf52/adafruit_clue_nrf52840
    nordicnrf52/adafruit_feather_nrf52840_sense
    nordicnrf52/adafruit_feather_nrf52840
    nordicnrf52/adafruit_ledglasses_nrf52840
    nordicnrf52/nano33ble
    nordicnrf52/nicla_sense_me
    nordicnrf52/bbcmicrobit_v2
    nordicnrf52/laird_bl652_dvk
    nordicnrf52/laird_bl653_dvk
    nordicnrf52/laird_bl654_dvk
    nordicnrf52/bluey
    nordicnrf52/calliopemini_v3
    nordicnrf52/adafruit_cplaynrf52840
    nordicnrf52/delta_dfbm_nq620
    nordicnrf52/electronut_blip
    nordicnrf52/electronut_papyr
    nordicnrf52/holyiot_yj16019
    nordicnrf52/adafruit_itsybitsy_nrf52840
    nordicnrf52/laird_pinnacle_100_dvk
    nordicnrf52/nrf52832_mdk
    nordicnrf52/nrf52840_mdk
    nordicnrf52/adafruit_metro_nrf52840
    nordicnrf52/thingy_52
    nordicnrf52/nrf52_dk
    nordicnrf52/nrf52833_dk
    nordicnrf52/nrf52840_dk
    nordicnrf52/nrf52840_dk_adafruit
    nordicnrf52/reel_board
    nordicnrf52/reel_board_v2
    nordicnrf52/particle_argon
    nordicnrf52/particle_boron
    nordicnrf52/particle_xenon
    nordicnrf52/raytac_mdbt50q_rx
    nordicnrf52/redbear_blenano2
    nordicnrf52/redbear_blend2
    nordicnrf52/ruuvitag
    nordicnrf52/sdt52832b
    nordicnrf52/stct_nrf52_minidev
    nordicnrf52/vbluno52
    nordicnrf52/dwm1001_dev
    nordicnrf52/hackaBLE
    nordicnrf52/ublox_bmd345eval_nrf52840
    nordicnrf52/ublox_evk_nina_b1

NXP i.MX RT
-----------

.. toctree::
    :maxdepth: 1
        
    nxpimxrt/mimxrt1010_evk
    nxpimxrt/mimxrt1015_evk
    nxpimxrt/mimxrt1020_evk
    nxpimxrt/mimxrt1050_evk
    nxpimxrt/mimxrt1060_evk
    nxpimxrt/mimxrt1064_evk

NXP LPC
-------

.. toctree::
    :maxdepth: 1
        
    nxplpc/lpc11u68
    nxplpc/lpc54114
    nxplpc/lpc546xx
    nxplpc/lpcxpresso55s16
    nxplpc/lpc1768
    nxplpc/seeedArchPro

OpenHW Group
------------

.. toctree::
    :maxdepth: 1
        
    openhw/nexys_a7

Raspberry Pi RP2040
-------------------

.. toctree::
    :maxdepth: 1
        
    raspberrypi/nanorp2040connect
    raspberrypi/pico

Renesas RA
----------

.. toctree::
    :maxdepth: 1
        
    renesas-ra/portenta_c33
    renesas-ra/uno_r4_minima
    renesas-ra/uno_r4_wifi

RISC-V GAP
----------

.. toctree::
    :maxdepth: 1
        
    riscv_gap/gapuino

Shakti
------

.. toctree::
    :maxdepth: 1
        
    shakti/artix7_35t
    shakti/artix7_100t
    shakti/parashu
    shakti/pinaka
    shakti/vajra

SiFive
------

.. toctree::
    :maxdepth: 1
        
    sifive/e310-arty
    sifive/hifive-unleashed
    sifive/hifive1
    sifive/hifive1-revb
    sifive/sparkfun_redboard_v
    sifive/sparkfun_thing_plus_v

Silicon Labs EFM32
------------------

.. toctree::
    :maxdepth: 1
        
    siliconlabsefm32/efm32gg_stk3700
    siliconlabsefm32/efm32wg_stk3800
    siliconlabsefm32/efm32hg_stk3400
    siliconlabsefm32/efm32gg11_stk3701
    siliconlabsefm32/tb_sense_12

ST STM32
--------

.. toctree::
    :maxdepth: 1
        
    ststm32/1bitsy_stm32f415rgt
    ststm32/disco_f412zg
    ststm32/disco_f723ie
    ststm32/armed_v1
    ststm32/rumba32_f446ve
    ststm32/remram_v1
    ststm32/st3dp001_eval
    ststm32/b96b_argonkey
    ststm32/b96b_f446ve
    ststm32/b96b_aerocore2
    ststm32/b96b_neonkey
    ststm32/acsip_s76s
    ststm32/adafruit_feather_f405
    ststm32/afroflight_f103cb
    ststm32/giga_r1_m4
    ststm32/giga_r1_m7
    ststm32/nicla_vision
    ststm32/nicla_vision_m4
    ststm32/opta
    ststm32/opta_m4
    ststm32/portenta_h7_m4
    ststm32/portenta_h7_m7
    ststm32/armstrap_eagle1024
    ststm32/armstrap_eagle2048
    ststm32/armstrap_eagle512
    ststm32/btt_ebb42_v1_1
    ststm32/black_f407ve
    ststm32/black_f407vg
    ststm32/black_f407ze
    ststm32/black_f407zg
    ststm32/blackpill_f103c8
    ststm32/blackpill_f103c8_128
    ststm32/robotdyn_blackpill_f303cc
    ststm32/blue_f407ve_mini
    ststm32/bluepill_f103c6
    ststm32/bluepill_f103c8
    ststm32/bluepill_f103c8_128k
    ststm32/blues_cygnet
    ststm32/blues_swan_r5
    ststm32/bw_swan_r5
    ststm32/cicada_l082cz
    ststm32/coreboard_f401rc
    ststm32/cricket_l082cz
    ststm32/demo_f030f4
    ststm32/devebox_h743vitx
    ststm32/devebox_h750vbtx
    ststm32/econode_l082cz
    ststm32/electrosmith_daisy
    ststm32/electrosmith_daisy_patch_sm
    ststm32/electrosmith_daisy_petal_sm
    ststm32/elektor_f072cb
    ststm32/elektor_f072c8
    ststm32/elmo_f411re
    ststm32/diymore_f407vgt
    ststm32/fk407m1
    ststm32/fysetc_s6
    ststm32/gnat_l082cz
    ststm32/grasshopper_l082cz
    ststm32/rhombio_l476dmw1k
    ststm32/leafony_ap03
    ststm32/malyanm200_f070cb
    ststm32/malyanm300_f070cb
    ststm32/mkr_sharky
    ststm32/mts_dragonfly_f411re
    ststm32/malyanm200_f103cb
    ststm32/maple
    ststm32/maple_ret6
    ststm32/maple_mini_b20
    ststm32/maple_mini_origin
    ststm32/mbed_connect_odin
    ststm32/microduino32_flash
    ststm32/mxchip_az3166
    ststm32/mts_mdot_f405rg
    ststm32/mts_mdot_f411re
    ststm32/xdot_l151cc
    ststm32/netduino2plus
    ststm32/mote_l152rc
    ststm32/nucleo_g070rb
    ststm32/nucleo_g071rb
    ststm32/nucleo_g431kb
    ststm32/nucleo_g431rb
    ststm32/nucleo_g474re
    ststm32/olimexino
    ststm32/olimexino_stm32f3
    ststm32/olimex_f103
    ststm32/olimex_p405
    ststm32/nucleo_wb55rg_p
    ststm32/pybstick26_duino
    ststm32/pybstick26_pro
    ststm32/pybstick26_lite
    ststm32/pybstick26_std
    ststm32/piconomix_px_her0
    ststm32/prntr_v2
    ststm32/rak811_tracker
    ststm32/rak811_tracker_32
    ststm32/rhf76_052
    ststm32/rymcu_nebulapi_f103ve
    ststm32/rymcu_f407ve
    ststm32/cloud_jam
    ststm32/cloud_jam_l4
    ststm32/disco_f334c8
    ststm32/disco_f401vc
    ststm32/disco_f411ve
    ststm32/disco_f413zh
    ststm32/disco_f429zi
    ststm32/disco_f469ni
    ststm32/disco_f746ng
    ststm32/disco_f769ni
    ststm32/disco_l053c8
    ststm32/disco_l100rc
    ststm32/disco_l476vg
    ststm32/disco_l496ag
    ststm32/disco_b_g431b_esc1
    ststm32/disco_l475vg_iot01a
    ststm32/disco_b_u585i_iot02a
    ststm32/disco_l072cz_lrwan1
    ststm32/disco_f072rb
    ststm32/nucleo_g031k8
    ststm32/nucleo_f030r8
    ststm32/nucleo_f031k6
    ststm32/nucleo_f042k6
    ststm32/nucleo_f070rb
    ststm32/nucleo_f072rb
    ststm32/nucleo_f091rc
    ststm32/nucleo_f103rb
    ststm32/nucleo_f207zg
    ststm32/nucleo_f302r8
    ststm32/nucleo_f303k8
    ststm32/nucleo_f303re
    ststm32/nucleo_f303ze
    ststm32/nucleo_f334r8
    ststm32/nucleo_f401re
    ststm32/nucleo_f410rb
    ststm32/nucleo_f411re
    ststm32/nucleo_f412zg
    ststm32/nucleo_f413zh
    ststm32/nucleo_f429zi
    ststm32/nucleo_f439zi
    ststm32/nucleo_f446re
    ststm32/nucleo_f446ze
    ststm32/nucleo_f722ze
    ststm32/nucleo_f746zg
    ststm32/nucleo_f756zg
    ststm32/nucleo_f767zi
    ststm32/nucleo_g0b1re
    ststm32/nucleo_h723zg
    ststm32/nucleo_h743zi
    ststm32/nucleo_h745zi_q
    ststm32/nucleo_h753zi
    ststm32/nucleo_l010rb
    ststm32/nucleo_l011k4
    ststm32/nucleo_l031k6
    ststm32/nucleo_l053r8
    ststm32/nucleo_l073rz
    ststm32/nucleo_l152re
    ststm32/nucleo_l412kb
    ststm32/nucleo_l412rb_p
    ststm32/nucleo_l432kc
    ststm32/nucleo_l433rc_p
    ststm32/nucleo_l452re
    ststm32/nucleo_l476rg
    ststm32/nucleo_l486rg
    ststm32/nucleo_l496zg
    ststm32/nucleo_l496zg_p
    ststm32/nucleo_l4r5zi
    ststm32/nucleo_l552ze_q
    ststm32/nucleo_u575zi_q
    ststm32/nucleo_wl55jc
    ststm32/disco_f030r8
    ststm32/disco_f051r8
    ststm32/disco_f303vc
    ststm32/disco_f407vg
    ststm32/disco_g031j6
    ststm32/disco_g071rb
    ststm32/eval_l073z
    ststm32/disco_l4s5i_iot01a
    ststm32/disco_l152rb
    ststm32/disco_f100rb
    ststm32/silica_sensor_node
    ststm32/steval_fcu001v1
    ststm32/olimex_e407
    ststm32/olimex_h407
    ststm32/eval_f107vc
    ststm32/eval_f373vc
    ststm32/eval_f072vb
    ststm32/genericSTM32F103C4
    ststm32/genericSTM32F103C6
    ststm32/genericSTM32F103C8
    ststm32/genericSTM32F103CB
    ststm32/genericSTM32F103R4
    ststm32/genericSTM32F103R6
    ststm32/genericSTM32F103R8
    ststm32/genericSTM32F103RB
    ststm32/genericSTM32F103RC
    ststm32/genericSTM32F103RD
    ststm32/genericSTM32F103RE
    ststm32/genericSTM32F103RF
    ststm32/genericSTM32F103RG
    ststm32/genericSTM32F103T4
    ststm32/genericSTM32F103T6
    ststm32/genericSTM32F103T8
    ststm32/genericSTM32F103TB
    ststm32/genericSTM32F103V8
    ststm32/genericSTM32F103VB
    ststm32/genericSTM32F103VC
    ststm32/genericSTM32F103VD
    ststm32/genericSTM32F103VE
    ststm32/genericSTM32F103VF
    ststm32/genericSTM32F103VG
    ststm32/genericSTM32F103ZC
    ststm32/genericSTM32F103ZD
    ststm32/genericSTM32F103ZE
    ststm32/genericSTM32F103ZF
    ststm32/genericSTM32F103ZG
    ststm32/genericSTM32F303CB
    ststm32/genericSTM32F373RC
    ststm32/genericSTM32F401CB
    ststm32/genericSTM32F401CC
    ststm32/genericSTM32F401CD
    ststm32/genericSTM32F401CE
    ststm32/genericSTM32F401RB
    ststm32/genericSTM32F401RC
    ststm32/genericSTM32F401RD
    ststm32/genericSTM32F401RE
    ststm32/genericSTM32F405RG
    ststm32/genericSTM32F407IGT6
    ststm32/genericSTM32F407VET6
    ststm32/genericSTM32F407VGT6
    ststm32/genericSTM32F410C8
    ststm32/genericSTM32F410CB
    ststm32/genericSTM32F410R8
    ststm32/genericSTM32F410RB
    ststm32/genericSTM32F411CC
    ststm32/genericSTM32F411CE
    ststm32/genericSTM32F411RC
    ststm32/genericSTM32F411RE
    ststm32/genericSTM32F412CE
    ststm32/genericSTM32F412CG
    ststm32/genericSTM32F412RE
    ststm32/genericSTM32F412RG
    ststm32/genericSTM32F413CG
    ststm32/genericSTM32F413CH
    ststm32/genericSTM32F413RG
    ststm32/genericSTM32F413RH
    ststm32/genericSTM32F415RG
    ststm32/genericSTM32F417VE
    ststm32/genericSTM32F417VG
    ststm32/genericSTM32F423CH
    ststm32/genericSTM32F423RH
    ststm32/genericSTM32F446RC
    ststm32/genericSTM32F446RE
    ststm32/stm32f4stamp
    ststm32/disco_f750n8
    ststm32/genericSTM32G431CB
    ststm32/disco_h735ig
    ststm32/disco_h747xi
    ststm32/genericSTM32H750VB
    ststm32/storm32_v1_31_rc
    ststm32/seeedArchMax
    ststm32/wio_3g
    ststm32/lora_e5_dev_board
    ststm32/lora_e5_mini
    ststm32/steval_mksboxv1
    ststm32/agafia_sg0
    ststm32/sparkfun_micromod_f405
    ststm32/sparky_v1
    ststm32/thunder_pack
    ststm32/thunder_pack_f411
    ststm32/hy_tinystm103tb
    ststm32/vake_v1
    ststm32/vccgnd_f103zet6
    ststm32/vccgnd_f407zg_mini
    ststm32/waveshare_open103z
    ststm32/blackpill_f401cc
    ststm32/blackpill_f411ce
    ststm32/blackpill_f401ce
    ststm32/weact_mini_h743vitx
    ststm32/weact_mini_h750vbtx
    ststm32/wraith32_v1
    ststm32/sakuraio_evb_01
    ststm32/ublox_c030_n211
    ststm32/ublox_c030_r410m
    ststm32/ublox_c030_u201
    ststm32/ublox_evk_odin_w2
    ststm32/mtb_ublox_odin_w2

ST STM8
-------

.. toctree::
    :maxdepth: 1
        
    ststm8/nucleo_8s207k8
    ststm8/nucleo_8s208rb
    ststm8/stm8sdisco
    ststm8/stm8s003f3
    ststm8/stm8sblue
    ststm8/stm8sblack
    ststm8/mb208
    ststm8/s8uno

Teensy
------

.. toctree::
    :maxdepth: 1
        
    teensy/teensymm
    teensy/teensy2
    teensy/teensy30
    teensy/teensy31
    teensy/teensy35
    teensy/teensy36
    teensy/teensy40
    teensy/teensy41
    teensy/teensylc
    teensy/teensy2pp

TI MSP430
---------

.. toctree::
    :maxdepth: 1
        
    timsp430/lpmsp430fr5739
    timsp430/lpmsp430f5529
    timsp430/lpmsp430fr2311
    timsp430/lpmsp430fr2355
    timsp430/lpmsp430fr2433
    timsp430/lpmsp430fr2476
    timsp430/lpmsp430fr4133
    timsp430/lpmsp430fr5969
    timsp430/lpmsp430fr5994
    timsp430/lpmsp430fr6989
    timsp430/lpmsp430g2231
    timsp430/lpmsp430g2452
    timsp430/lpmsp430g2553

TI TIVA
-------

.. toctree::
    :maxdepth: 1
        
    titiva/lplm4f120h5qr
    titiva/lptm4c123gh6pm
    titiva/lptm4c1294ncpdt
