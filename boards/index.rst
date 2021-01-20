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
popular embedded boards and IDE.

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by horizontal.

Aceinna IMU
-----------

.. toctree::
    :maxdepth: 1
        
    aceinna_imu/LowCostRTK
    aceinna_imu/OpenIMU300
    aceinna_imu/OpenIMU300ZA
    aceinna_imu/OpenIMU330
    aceinna_imu/OpenRTK
    aceinna_imu/OpenRTK330L

ASR Microelectronics ASR650x
----------------------------

.. toctree::
    :maxdepth: 1
        
    asrmicro650x/cubecell_capsule_solar_sensor
    asrmicro650x/cubecell_node
    asrmicro650x/cubecell_board
    asrmicro650x/cubecell_board_plus
    asrmicro650x/cubecell_capsule
    asrmicro650x/cubecell_gps
    asrmicro650x/cubecell_module
    asrmicro650x/cubecell_module_plus

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
    atmelavr/ATmega168
    atmelavr/ATmega168P
    atmelavr/ATmega168PB
    atmelavr/ATmega2560
    atmelavr/ATmega2561
    atmelavr/ATmega32
    atmelavr/ATmega324A
    atmelavr/ATmega324P
    atmelavr/ATmega324PA
    atmelavr/ATmega324PB
    atmelavr/ATmega328
    atmelavr/ATmega328P
    atmelavr/ATmega328PB
    atmelavr/ATmega48
    atmelavr/ATmega48P
    atmelavr/ATmega48PB
    atmelavr/ATmega64
    atmelavr/ATmega640
    atmelavr/ATmega644A
    atmelavr/ATmega644P
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
    atmelmegaavr/ATtiny202
    atmelmegaavr/ATtiny204
    atmelmegaavr/ATtiny212
    atmelmegaavr/ATtiny214
    atmelmegaavr/ATtiny3216
    atmelmegaavr/ATtiny3217
    atmelmegaavr/ATtiny402
    atmelmegaavr/ATtiny404
    atmelmegaavr/ATtiny406
    atmelmegaavr/ATtiny412
    atmelmegaavr/ATtiny414
    atmelmegaavr/ATtiny416
    atmelmegaavr/ATtiny417
    atmelmegaavr/ATtiny804
    atmelmegaavr/ATtiny806
    atmelmegaavr/ATtiny807
    atmelmegaavr/ATtiny814
    atmelmegaavr/ATtiny816
    atmelmegaavr/ATtiny817
    atmelmegaavr/avr_iot_wg
    atmelmegaavr/nano_every
    atmelmegaavr/uno_wifi_rev2
    atmelmegaavr/curiosity_nano_4809
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
    atmelsam/adafruit_pygamer_advance_m4
    atmelsam/adafruit_pygamer_m4
    atmelsam/adafruit_pyportal_m4
    atmelsam/adafruit_pyportal_m4_titano
    atmelsam/adafruit_qt_py_m0
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
    atmelsam/saml21_xpro_b
    atmelsam/briki_abc_samd21
    atmelsam/briki_mbcwb_samd21
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
        
    espressif32/esp32cam
    espressif32/alksesp32
    espressif32/az-delivery-devkit-v4
    espressif32/featheresp32
    espressif32/espea32
    espressif32/bpi-bit
    espressif32/briki_abc_esp32
    espressif32/briki_mbc-wb_esp32
    espressif32/d-duino-32
    espressif32/esp32doit-devkit-v1
    espressif32/pocket_32
    espressif32/fm-devkit
    espressif32/pico32
    espressif32/esp32vn-iot-uno
    espressif32/espectro32
    espressif32/espino32
    espressif32/esp320
    espressif32/esp-wrover-kit
    espressif32/esp32dev
    espressif32/firebeetle32
    espressif32/frogboard
    espressif32/heltec_wifi_kit_32
    espressif32/heltec_wifi_lora_32
    espressif32/heltec_wifi_lora_32_V2
    espressif32/heltec_wireless_stick
    espressif32/hornbill32dev
    espressif32/hornbill32minima
    espressif32/intorobot
    espressif32/iotaap_magnolia
    espressif32/m5stack-core-esp32
    espressif32/m5stack-fire
    espressif32/m5stack-grey
    espressif32/m5stick-c
    espressif32/mhetesp32devkit
    espressif32/mhetesp32minikit
    espressif32/magicbit
    espressif32/nano32
    espressif32/microduino-core-esp32
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
    espressif32/pycom_gpy
    espressif32/lopy
    espressif32/lopy4
    espressif32/qchip
    espressif32/sg-o_airMon
    espressif32/wesp32
    espressif32/esp32thing
    espressif32/sparkfun_lora_gateway_1-channel
    espressif32/ttgo-lora32-v1
    espressif32/ttgo-lora32-v2
    espressif32/ttgo-t-beam
    espressif32/ttgo-t-watch
    espressif32/ttgo-t1
    espressif32/tinypico
    espressif32/turta_iot_node
    espressif32/vintlabs-devkit-v1
    espressif32/lolin_d32
    espressif32/lolin_d32_pro
    espressif32/lolin32
    espressif32/wemos_d1_mini32
    espressif32/wemosbat
    espressif32/widora-air
    espressif32/xinabox_cw02
    espressif32/nscreen-32
    espressif32/iotbusio
    espressif32/iotbusproteus
    espressif32/nina_w10

Espressif 8266
--------------

.. toctree::
    :maxdepth: 1
        
    espressif8266/gen4iod
    espressif8266/huzzah
    espressif8266/oak
    espressif8266/espmxdevkit
    espressif8266/esp_wroom_02
    espressif8266/espduino
    espressif8266/espectro
    espressif8266/espino
    espressif8266/espresso_lite_v1
    espressif8266/espresso_lite_v2
    espressif8266/esp12e
    espressif8266/esp01_1m
    espressif8266/esp01
    espressif8266/esp07
    espressif8266/esp07s
    espressif8266/esp8285
    espressif8266/heltec_wifi_kit_8
    espressif8266/inventone
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
    freescalekinetis/frdm_k20d50m
    freescalekinetis/frdm_k22f
    freescalekinetis/frdm_k64f
    freescalekinetis/frdm_k66f
    freescalekinetis/frdm_k82f
    freescalekinetis/frdm_kl05z
    freescalekinetis/frdm_kl25z
    freescalekinetis/frdm_kl27z
    freescalekinetis/frdm_kl43z
    freescalekinetis/frdm_kl46z
    freescalekinetis/frdm_kl82z
    freescalekinetis/frdm_kw24d
    freescalekinetis/frdm_kw41z
    freescalekinetis/hexiwear
    freescalekinetis/segger_ip_switch

GigaDevice GD32V
----------------

.. toctree::
    :maxdepth: 1
        
    gd32v/gd32vf103v-eval
    gd32v/sipeed-longan-nano
    gd32v/sipeed-longan-nano-lite
    gd32v/wio_lite_risc-v

Infineon XMC
------------

.. toctree::
    :maxdepth: 1
        
    infineonxmc/xmc1100_boot_kit
    infineonxmc/xmc1100_h_bridge2go
    infineonxmc/xmc1100_xmc2go
    infineonxmc/xmc1300_boot_kit
    infineonxmc/xmc1300_sense2gol
    infineonxmc/xmc1400_boot_kit
    infineonxmc/xmc4200_distance2go
    infineonxmc/xmc4700_relax_kit

Intel ARC32
-----------

.. toctree::
    :maxdepth: 1
        
    intel_arc32/genuino101

Intel MCS-51 (8051)
-------------------

.. toctree::
    :maxdepth: 1
        
    intel_mcs51/n79e8432
    intel_mcs51/n79e844
    intel_mcs51/n79e845
    intel_mcs51/n79e854
    intel_mcs51/n79e855
    intel_mcs51/stc15f204ea
    intel_mcs51/stc15f2k60s2
    intel_mcs51/stc15w204s
    intel_mcs51/stc15w404as
    intel_mcs51/stc15w408as
    intel_mcs51/stc89c52rc

Kendryte K210
-------------

.. toctree::
    :maxdepth: 1
        
    kendryte210/sipeed-maix-bit
    kendryte210/sipeed-maix-bit-mic
    kendryte210/sipeed-maix-go
    kendryte210/sipeed-maix-one-dock
    kendryte210/sipeed-maixduino
    kendryte210/sipeed-MF1

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
    maxim32/max32625nexpaq
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
    nordicnrf51/dfcm_nnn40
    nordicnrf51/delta_dfcm_nnn50
    nordicnrf51/wallbot_ble
    nordicnrf51/nrf51_beacon
    nordicnrf51/nrf51_dongle
    nordicnrf51/nrf51_mkit
    nordicnrf51/nrf51_dk
    nordicnrf51/oshchip
    nordicnrf51/redBearLabBLENano
    nordicnrf51/redBearLab
    nordicnrf51/seeedArchBLE
    nordicnrf51/seeedArchLink
    nordicnrf51/seeedTinyBLE
    nordicnrf51/Sinobit
    nordicnrf51/hrm1017
    nordicnrf51/ty51822r3
    nordicnrf51/vbluno51
    nordicnrf51/waveshare_ble400
    nordicnrf51/ng_beacon
    nordicnrf51/nrf51822_y5_mbug

Nordic nRF52
------------

.. toctree::
    :maxdepth: 1
        
    nordicnrf52/96b_nitrogen
    nordicnrf52/adafruit_feather_nrf52832
    nordicnrf52/adafruit_clue_nrf52840
    nordicnrf52/adafruit_feather_nrf52840_sense
    nordicnrf52/adafruit_feather_nrf52840
    nordicnrf52/nano33ble
    nordicnrf52/bbcmicrobit_v2
    nordicnrf52/laird_bl652_dvk
    nordicnrf52/laird_bl654_dvk
    nordicnrf52/bluey
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
    nordicnrf52/ublox_evk_nina_b1

Nuclei
------

.. toctree::
    :maxdepth: 1
        
    nuclei/gd32vf103v_eval
    nuclei/gd32vf103v_rvstar
    nuclei/hbird_eval
    nuclei/gd32vf103c_longan_nano

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
        
    nxplpc/lpc11u24_301
    nxplpc/lpc4330_m4
    nxplpc/lpc11u35_501
    nxplpc/elektor_cocorico
    nxplpc/lpc1347
    nxplpc/lpc11u35
    nxplpc/lpc4088_dm
    nxplpc/lpc4088
    nxplpc/lpc11u68
    nxplpc/lpc824
    nxplpc/micronfcboard
    nxplpc/blueboard_lpc11u24
    nxplpc/lpc11c24
    nxplpc/lpc11u34_421
    nxplpc/lpc11u37_501
    nxplpc/lpc812
    nxplpc/lpc1549
    nxplpc/lpc54114
    nxplpc/lpc546xx
    nxplpc/lpcxpresso55s16
    nxplpc/lpcxpresso55s69
    nxplpc/lpc11u24
    nxplpc/lpc1768
    nxplpc/mbuino
    nxplpc/seeedArchGPRS
    nxplpc/seeedArchPro
    nxplpc/xadow_m0
    nxplpc/xbed_lpc1768
    nxplpc/dipcortexm0
    nxplpc/lpc1114fn28
    nxplpc/ssci824
    nxplpc/oc_mbuino
    nxplpc/ubloxc027
    nxplpc/lpc11u35_y5_mbug

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
    siliconlabsefm32/efm32lg_stk3600
    siliconlabsefm32/efm32wg_stk3800
    siliconlabsefm32/efm32zg_stk3200
    siliconlabsefm32/efm32hg_stk3400
    siliconlabsefm32/efm32pg_stk3401
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
    ststm32/adafruit_feather_f405
    ststm32/afroflight_f103cb
    ststm32/armstrap_eagle1024
    ststm32/armstrap_eagle2048
    ststm32/armstrap_eagle512
    ststm32/black_f407ve
    ststm32/black_f407vg
    ststm32/black_f407ze
    ststm32/black_f407zg
    ststm32/blackpill_f103c8
    ststm32/blackpill_f103c8_128
    ststm32/robotdyn_blackpill_f303cc
    ststm32/blackpill_f401cc
    ststm32/blackpill_f401ce
    ststm32/blue_f407ve_mini
    ststm32/bluepill_f103c6
    ststm32/bluepill_f103c8
    ststm32/bluepill_f103c8_128k
    ststm32/cicada_l082cz
    ststm32/coreboard_f401rc
    ststm32/cricket_l082cz
    ststm32/demo_f030f4
    ststm32/econode_l082cz
    ststm32/electrosmith_daisy
    ststm32/elmo_f411re
    ststm32/diymore_f407vgt
    ststm32/fk407m1
    ststm32/fysetc_s6
    ststm32/gnat_l082cz
    ststm32/grasshopper_l082cz
    ststm32/rhombio_l476dmw1k
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
    ststm32/nucleo_g071rb
    ststm32/nucleo_g431kb
    ststm32/nucleo_g431rb
    ststm32/nucleo_g474re
    ststm32/olimexino
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
    ststm32/disco_l475vg_iot01a
    ststm32/disco_l072cz_lrwan1
    ststm32/disco_f072rb
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
    ststm32/nucleo_h743zi
    ststm32/nucleo_h745zi_q
    ststm32/nucleo_l011k4
    ststm32/nucleo_l031k6
    ststm32/nucleo_l053r8
    ststm32/nucleo_l073rz
    ststm32/nucleo_l152re
    ststm32/nucleo_l412kb
    ststm32/nucleo_l432kc
    ststm32/nucleo_l433rc_p
    ststm32/nucleo_l452re
    ststm32/nucleo_l476rg
    ststm32/nucleo_l486rg
    ststm32/nucleo_l496zg
    ststm32/nucleo_l496zg_p
    ststm32/nucleo_l4r5zi
    ststm32/disco_f030r8
    ststm32/disco_f051r8
    ststm32/disco_f303vc
    ststm32/disco_f407vg
    ststm32/disco_g031j6
    ststm32/eval_l073z
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
    ststm32/disco_h747xi
    ststm32/seeedArchMax
    ststm32/wio_3g
    ststm32/steval_mksboxv1
    ststm32/sparky_v1
    ststm32/thunder_pack
    ststm32/thunder_pack_f411
    ststm32/hy_tinystm103tb
    ststm32/vake_v1
    ststm32/vccgnd_f103zet6
    ststm32/waveshare_open103z
    ststm32/blackpill_f411ce
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
        
    ststm8/stm8sdisco
    ststm8/stm8sblue
    ststm8/stm8sblack
    ststm8/mb208
    ststm8/s8uno

Teensy
------

.. toctree::
    :maxdepth: 1
        
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
    timsp430/lpmsp430fr2433
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
    titiva/lptm4c1230c3pm
    titiva/lptm4c1294ncpdt

WIZNet W7500
------------

.. toctree::
    :maxdepth: 1
        
    wiznet7500/wizwiki_w7500
    wiznet7500/wizwiki_w7500eco
    wiznet7500/wizwiki_w7500p
