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

.. _board_espressif32_seeed_xiao_esp32c6:

Seeed Studio XIAO ESP32C6
=========================

.. contents::

Hardware
--------

Seeed Studio XIAO ESP32C6 pairs Espressif's dual-core RISC-V SoC (HP core up to 160MHz, LP core up to 20MHz) with Wi-Fi 6, Bluetooth LE 5.3, and IEEE 802.15.4 for Thread/Zigbee. It keeps the thumb-sized XIAO footprint and offers both on-board and external (U.FL) antenna options.

.. list-table::

  * - **Microcontroller**
    - ESP32-C6
  * - **CPU**
    - Dual RISC-V (HP up to 160MHz, LP up to 20MHz)
  * - **Wireless**
    - 2.4GHz Wi-Fi 6, Bluetooth LE 5.3 (Mesh), IEEE 802.15.4 (Thread/Zigbee)
  * - **Flash**
    - 4MB
  * - **RAM**
    - 512KB SRAM
  * - **Vendor**
    - `Seeed Studio <https://wiki.seeedstudio.com/XIAO_ESP32C6_Getting_Started/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``seeed_xiao_esp32c6`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:seeed_xiao_esp32c6]
  platform = espressif32
  board = seeed_xiao_esp32c6

You can override default Seeed Studio XIAO ESP32C6 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `seeed_xiao_esp32c6.json <https://github.com/platformio/platform-espressif32/blob/master/boards/seeed_xiao_esp32c6.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:seeed_xiao_esp32c6]
  platform = espressif32
  board = seeed_xiao_esp32c6

  ; change microcontroller
  board_build.mcu = esp32c6

  ; change MCU frequency
  board_build.f_cpu = 160000000L

RF switch and antenna
---------------------

The XIAO ESP32C6 boots with its RF switch disabled. Without the RF switch on, the 2.4GHz radio will have a very weak connection.
Connect an antenna by pulling ``GPIO3`` (``RF_SWITCH_EN``) low to enable the RF switch, use ``GPIO14`` (``RF_ANT_SELECT``) to select the antenna to use: 

* GPIO14 low selects the on-board antenna
* GPIO14 high selects the external connector

Example for ESP-IDF:

.. code-block:: c

  #include "driver/gpio.h"

  void app_main(void) {
      gpio_config_t cfg = {
          .pin_bit_mask = (1ULL << GPIO_NUM_3) | (1ULL << GPIO_NUM_14),
          .mode = GPIO_MODE_OUTPUT,
      };
      gpio_config(&cfg);

      // enable RF switch (active-low)
      gpio_set_level(GPIO_NUM_3, 0);
      
      // select on-board antenna 
      gpio_set_level(GPIO_NUM_14, 0);
  }

Pinout
------

.. list-table::
  :header-rows: 1

  * - Label
    - GPIO
    - Notes
  * - D0
    - GPIO0
    - A0 / LP_GPIO0
  * - D1
    - GPIO1
    - A1 / LP_GPIO1
  * - D2
    - GPIO2
    - A2 / LP_GPIO2
  * - D3
    - GPIO21
    - SDIO_DATA1
  * - D4
    - GPIO22
    - SDA / SDIO_DATA2
  * - D5
    - GPIO23
    - SCL / SDIO_DATA3
  * - D6
    - GPIO16
    - UART TX
  * - D7
    - GPIO17
    - UART RX
  * - D8
    - GPIO19
    - SCK / SDIO_CLK
  * - D9
    - GPIO20
    - MISO / SDIO_DATA0
  * - D10
    - GPIO18
    - MOSI / SDIO_CMD
  * - MTDO
    - GPIO7
    - LP_GPIO7 / LP_I2C_SCL (back pad)
  * - MTCK
    - GPIO6
    - A6 / LP_GPIO6 / LP_I2C_SDA (back pad)
  * - MTDI
    - GPIO5
    - A5 / LP_GPIO5 / LP_UART_TXD (back pad)
  * - MTMS
    - GPIO4
    - A4 / LP_GPIO4 / LP_UART_RXD (back pad)
  * - BOOT
    - GPIO9
    - Boot button
  * - LED / LED_BUILTIN
    - GPIO8
    - On-board user LED
  * - RF_SWITCH_EN
    - GPIO3
    - Drive low (inverted) to enable RF switch
  * - RF_ANT_SELECT
    - GPIO14
    - Low selects on-board antenna; high selects external connector


Uploading
---------
Seeed Studio XIAO ESP32C6 supports the following uploading protocols:

* ``cmsis-dap``
* ``esp-bridge``
* ``esp-builtin``
* ``esp-prog``
* ``espota``
* ``esptool``
* ``iot-bus-jtag``
* ``jlink``
* ``minimodule``
* ``olimex-arm-usb-ocd``
* ``olimex-arm-usb-ocd-h``
* ``olimex-arm-usb-tiny-h``
* ``olimex-jtag-tiny``
* ``tumpa``

Default protocol is ``esptool``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:seeed_xiao_esp32c6]
  platform = espressif32
  board = seeed_xiao_esp32c6

  upload_protocol = esptool

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

Seeed Studio XIAO ESP32C6 does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_cmsis-dap`
    - 
    - 
  * - ``esp-bridge``
    - 
    - 
  * - ``esp-builtin``
    - 
    - 
  * - :ref:`debugging_tool_esp-prog`
    - 
    - 
  * - :ref:`debugging_tool_iot-bus-jtag`
    - 
    - 
  * - :ref:`debugging_tool_jlink`
    - 
    - 
  * - :ref:`debugging_tool_minimodule`
    - 
    - 
  * - :ref:`debugging_tool_olimex-arm-usb-ocd`
    - 
    - 
  * - :ref:`debugging_tool_olimex-arm-usb-ocd-h`
    - 
    - 
  * - :ref:`debugging_tool_olimex-arm-usb-tiny-h`
    - 
    - 
  * - :ref:`debugging_tool_olimex-jtag-tiny`
    - 
    - 
  * - :ref:`debugging_tool_tumpa`
    - 
    - 

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_espidf`
      - Espressif IoT Development Framework. Official development framework for ESP32 chip
