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

Configuration
-------------

.. contents::
    :local:

CPU Frequency
~~~~~~~~~~~~~

See :ref:`projectconf_board_f_cpu` option from :ref:`projectconf`

.. code-block:: ini

    [env:myenv]
    ; set frequency to 160MHz
    board_f_cpu = 160000000L

FLASH Frequency
~~~~~~~~~~~~~~~

See :ref:`projectconf_board_f_flash` option from :ref:`projectconf`. Possible
values:

* ``20000000L``
* ``26000000L``
* ``40000000L`` (default)
* ``80000000L``

.. code-block:: ini

    [env:myenv]
    ; set frequency to 80MHz
    board_f_flash = 80000000L

FLASH Mode
~~~~~~~~~~

Flash chip interface mode. This parameter is stored in the binary image
header, along with the flash size and flash frequency. The ROM bootloader
in the ESP chip uses the value of these parameters in order to know how to
talk to the flash chip.

See :ref:`projectconf_board_flash_mode` option from :ref:`projectconf`. Possible
values:

* ``qio``
* ``qout``
* ``dio``
* ``dout``

.. code-block:: ini

    [env:myenv]
    board_flash_mode = qio

Reset Method
~~~~~~~~~~~~

You can set custom reset method using :ref:`projectconf_upload_resetmethod`
option from :ref:`projectconf`.

The `possible values <https://github.com/igrr/esptool-ck#supported-boards>`_ are:

* ``ck`` - RTS controls RESET or CH_PD, DTR controls GPIO0
* ``wifio`` - TXD controls GPIO0 via PNP transistor and DTR controls RESET via a capacitor
* ``nodemcu`` - GPIO0 and RESET controlled using two NPN transistors as in NodeMCU devkit.

See `default reset methods per board <https://github.com/platformio/platform-espressif8266/search?p=1&q=resetmethod>`_.

.. code-block:: ini

    [env:myenv]
    upload_resetmethod = ck

.. _platform_espressif_customflash:

Flash Size
~~~~~~~~~~

.. warning::
    Please make sure to read `ESP8266 Flash layout <https://arduino-esp8266.readthedocs.io/en/latest/filesystem.html#flash-layout>`_
    information first.

Available LD-scripts:
https://github.com/esp8266/Arduino/tree/master/tools/sdk/ld

* ``eagle.flash.512k0.ld`` 512K (no SPIFFS)
* ``eagle.flash.512k64.ld`` 512K (64K SPIFFS)
* ``eagle.flash.512k128.ld`` 512K (128K SPIFFS)
* ``eagle.flash.1m0.ld`` 1M (no SPIFFS)
* ``eagle.flash.1m64.ld`` 1M (64K SPIFFS)
* ``eagle.flash.1m128.ld`` 1M (128K SPIFFS)
* ``eagle.flash.1m144.ld`` 1M (144K SPIFFS)
* ``eagle.flash.1m160.ld`` 1M (160K SPIFFS)
* ``eagle.flash.1m192.ld`` 1M (192K SPIFFS)
* ``eagle.flash.1m256.ld`` 1M (256K SPIFFS)
* ``eagle.flash.1m512.ld`` 1M (512K SPIFFS)
* ``eagle.flash.2m.ld`` 2M (1M SPIFFS)
* ``eagle.flash.4m1m.ld`` 4M (1M SPIFFS)
* ``eagle.flash.4m.ld`` 4M (3M SPIFFS)
* ``eagle.flash.8m.ld`` 8M (7M SPIFFS)
* ``eagle.flash.16m.ld`` 16M (15M SPIFFS)

To override default LD script please use :ref:`projectconf_build_flags` from
:ref:`projectconf`.

.. code-block:: ini

    [env:myenv]
    build_flags = -Wl,-Teagle.flash.4m.ld

Upload Speed
~~~~~~~~~~~~

You can set custom upload speed using  :ref:`projectconf_upload_speed` option
from :ref:`projectconf`

.. code-block:: ini

    [env:myenv]
    upload_speed = 9600

lwIP Variant
~~~~~~~~~~~~

Available variants (macros):

* ``-D PIO_FRAMEWORK_ARDUINO_LWIP_HIGHER_BANDWIDTH`` v1.4 Higher Bandwidth (default)
* ``-D PIO_FRAMEWORK_ARDUINO_LWIP2_LOW_MEMORY`` v2 Lower Memory
* ``-D PIO_FRAMEWORK_ARDUINO_LWIP2_HIGHER_BANDWIDTH`` v2 Higher Bandwidth

You can change lwIP Variant passing a custom macro using project
:ref:`projectconf_build_flags`.

For example, switch to lwIP v2 Lower Memory

.. code-block:: ini

    [env:myenv]
    ...
    build_flags = -D PIO_FRAMEWORK_ARDUINO_LWIP2_LOW_MEMORY


.. _platform_espressif8266_serial_debug:

Serial Debug
~~~~~~~~~~~~

Please use the next :ref:`projectconf_build_flags` to enable Serial debug:

.. code-block:: ini

    [env:myenv]
    ...
    build_flags = -DDEBUG_ESP_PORT=Serial

    ; or for Serial1
    build_flags = -DDEBUG_ESP_PORT=Serial1


Debug Level
~~~~~~~~~~~

Please use one of the next :ref:`projectconf_build_flags` to change debug level.
A :ref:`projectconf_build_flags` option could be used only the one time per
build environment. If you need to specify more flags, please separate them
with a new line or space.

Also, please note that you will need to extend :ref:`projectconf_build_flags`
with :ref:`platform_espressif8266_serial_debug` macro. For example,
``build_flags = -DDEBUG_ESP_PORT=Serial -DDEBUG_ESP_SSL ...``.

Actual information is available in `Arduino for ESP8266 Board Manifest <https://github.com/esp8266/Arduino/blob/master/boards.txt#L286>`_.
Please scroll to ``generic.menu.DebugLevel`` section.


.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    framework = arduino

    ;;;;; Possible options ;;;;;;

    ; SSL
    build_flags = -DDEBUG_ESP_SSL

    ; TLS_MEM
    build_flags = -DDEBUG_ESP_TLS_MEM

    ; HTTP_CLIENT
    build_flags = -DDEBUG_ESP_HTTP_CLIENT

    ; HTTP_SERVER
    build_flags = -DDEBUG_ESP_HTTP_SERVER

    ; SSL+TLS_MEM
    build_flags =
      -DDEBUG_ESP_SSL
      -DDEBUG_ESP_TLS_MEM

    ; SSL+HTTP_CLIENT
    build_flags =
      -DDEBUG_ESP_SSL
      -DDEBUG_ESP_HTTP_CLIENT

    ; SSL+HTTP_SERVER
    build_flags =
      -DDEBUG_ESP_SSL
      -DDEBUG_ESP_HTTP_SERVER

    ; TLS_MEM+HTTP_CLIENT
    build_flags =
      -DDEBUG_ESP_TLS_MEM
      -DDEBUG_ESP_HTTP_CLIENT

    ; TLS_MEM+HTTP_SERVER
    build_flags =
      -DDEBUG_ESP_TLS_MEM
      -DDEBUG_ESP_HTTP_SERVER

    ; HTTP_CLIENT+HTTP_SERVER
    build_flags =
      -DDEBUG_ESP_HTTP_CLIENT
      -DDEBUG_ESP_HTTP_SERVER

    ; SSL+TLS_MEM+HTTP_CLIENT
    build_flags =
      -DDEBUG_ESP_SSL
      -DDEBUG_ESP_TLS_MEM
      -DDEBUG_ESP_HTTP_CLIENT

    ; SSL+TLS_MEM+HTTP_SERVER
    build_flags =
      -DDEBUG_ESP_SSL
      -DDEBUG_ESP_TLS_MEM
      -DDEBUG_ESP_HTTP_SERVER

    ; SSL+HTTP_CLIENT+HTTP_SERVER
    build_flags =
      -DDEBUG_ESP_SSL
      -DDEBUG_ESP_HTTP_CLIENT
      -DDEBUG_ESP_HTTP_SERVER

    ; TLS_MEM+HTTP_CLIENT+HTTP_SERVER
    build_flags =
      -DDEBUG_ESP_TLS_MEM
      -DDEBUG_ESP_HTTP_CLIENT
      -DDEBUG_ESP_HTTP_SERVER

    ; SSL+TLS_MEM+HTTP_CLIENT+HTTP_SERVER
    build_flags =
      -DDEBUG_ESP_SSL
      -DDEBUG_ESP_TLS_MEM
      -DDEBUG_ESP_HTTP_CLIENT
      -DDEBUG_ESP_HTTP_SERVER

    ; CORE
    build_flags = -DDEBUG_ESP_CORE

    ; WIFI
    build_flags = -DDEBUG_ESP_WIFI

    ; HTTP_UPDATE
    build_flags = -DDEBUG_ESP_HTTP_UPDATE

    ; UPDATER
    build_flags = -DDEBUG_ESP_UPDATER

    ; OTA
    build_flags = -DDEBUG_ESP_OTA

    ; OOM
    build_flags =
      -DDEBUG_ESP_OOM
      -include "umm_malloc/umm_malloc_cfg.h"

    ; CORE+WIFI+HTTP_UPDATE+UPDATER+OTA+OOM
    build_flags =
      -DDEBUG_ESP_CORE
      -DDEBUG_ESP_WIFI
      -DDEBUG_ESP_HTTP_UPDATE
      -DDEBUG_ESP_UPDATER
      -DDEBUG_ESP_OTA
      -DDEBUG_ESP_OOM -include "umm_malloc/umm_malloc_cfg.h"

    ; SSL+TLS_MEM+HTTP_CLIENT+HTTP_SERVER+CORE+WIFI+HTTP_UPDATE+UPDATER+OTA+OOM
    build_flags =
      -DDEBUG_ESP_SSL
      -DDEBUG_ESP_TLS_MEM
      -DDEBUG_ESP_HTTP_CLIENT
      -DDEBUG_ESP_HTTP_SERVER
      -DDEBUG_ESP_CORE
      -DDEBUG_ESP_WIFI
      -DDEBUG_ESP_HTTP_UPDATE
      -DDEBUG_ESP_UPDATER
      -DDEBUG_ESP_OTA
      -DDEBUG_ESP_OOM -include "umm_malloc/umm_malloc_cfg.h"

    ; NoAssert-NDEBUG
    build_flags = -DNDEBUG


.. _platform_espressif_uploadfs:

Uploading files to file system SPIFFS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::
    Please make sure to read `ESP8266 Flash layout <https://arduino-esp8266.readthedocs.io/en/latest/filesystem.html#flash-layout>`_
    information first.

1. Initialize project :ref:`cmd_init` (if you have not initialized yet)
2. Create ``data`` folder (it should be on the same level as ``src`` folder)
   and put files here. Also, you can specify own location for :ref:`projectconf_pio_data_dir`
3. Run ``buildfs`` or ``uploadfs`` target using :option:`platformio run --target` command.

To upload SPIFFS image using OTA update please specify ``upload_port`` /
``--upload-port`` as IP address or mDNS host name (ending with the ``*.local``).
For the details please follow to :ref:`platform_espressif_ota`.

By default, will be used default LD Script for the board where is specified
SPIFFS offsets (start, end, page, block). You can override it using
:ref:`platform_espressif_customflash`.

Active discussion is located in `issue #382 <https://github.com/platformio/platformio-core/issues/382>`_.

.. _platform_espressif_ota:

Over-the-Air (OTA) update
~~~~~~~~~~~~~~~~~~~~~~~~~

Firstly, please read `What is OTA? How to use it? <https://arduino-esp8266.readthedocs.io/en/latest/ota_updates/readme.html>`_

There are 2 options:

* Directly specify :option:`platformio run --upload-port` in command line

.. code-block:: bash

    platformio run --target upload --upload-port IP_ADDRESS_HERE or mDNS_NAME.local

* Specify ``upload_port`` option in :ref:`projectconf`

.. code-block:: ini

   [env:myenv]
   upload_port = IP_ADDRESS_HERE or mDNS_NAME.local

For example,

* ``platformio run -t upload --upload-port 192.168.0.255``
* ``platformio run -t upload --upload-port myesp8266.local``

Authentication and upload options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can pass additional options/flags to OTA uploader using
``upload_flags`` option in :ref:`projectconf`

.. code-block:: ini

    [env:myenv]
    upload_flags = --port=8266

Available flags

* ``--port=ESP_PORT`` ESP8266 OTA Port. Default 8266
* ``--auth=AUTH`` Set authentication password
* ``--spiffs`` Use this option to transmit a SPIFFS image and do not flash
  the module

For the full list with available options please run

.. code-block:: bash

    ~/.platformio/packages/tool-espotapy/espota.py -h

    Usage: espota.py [options]

    Transmit image over the air to the esp8266 module with OTA support.

    Options:
      -h, --help            show this help message and exit

      Destination:
        -i ESP_IP, --ip=ESP_IP
                            ESP8266 IP Address.
        -p ESP_PORT, --port=ESP_PORT
                            ESP8266 ota Port. Default 8266

      Authentication:
        -a AUTH, --auth=AUTH
                            Set authentication password.

      Image:
        -f FILE, --file=FILE
                            Image file.
        -s, --spiffs        Use this option to transmit a SPIFFS image and do not
                            flash the module.

      Output:
        -d, --debug         Show debug output. And override loglevel with debug.
        -r, --progress      Show progress output. Does not work for ArduinoIDE

Demo
~~~~

.. image:: ../_static/platformio-demo-ota-esp8266.jpg
    :target: https://www.youtube.com/watch?v=lXchL3hpDO4


Using Arduino Framework with Staging version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PlatformIO will install the latest Arduino Core for ESP8266 from
https://github.com/esp8266/Arduino. The `Git <https://git-scm.com>`_
should be installed in a system. To update Arduino Core to the latest revision,
please open :ref:`pioide` and navigate to ``PIO Home > Platforms > Updates``.

1.  Please install :ref:`pioide`
2.  Initialize a new project, open :ref:`projectconf` and set
    :ref:`projectconf_env_platform` to
    ``https://github.com/platformio/platform-espressif8266.git#feature/stage``.
    For example,

    .. code-block:: ini

        [env:nodemcuv2]
        platform = https://github.com/platformio/platform-espressif8266.git#feature/stage
        board = nodemcuv2
        framework = arduino

3.  Try to build project
4.  If you see build errors, then try to build this project using the same
    ``stage`` with Arduino IDE
5.  If it works with Arduino IDE but doesn't work with PlatformIO, then please
    `file new issue <https://github.com/platformio/platform-espressif32/issuess>`_
    with attached information:

    - test project/files
    - detailed log of build process from Arduino IDE (please copy it from
      console to https://hastebin.com)
    - detailed log of build process from PlatformIO Build System (please copy
      it from console to https://hastebin.com)
