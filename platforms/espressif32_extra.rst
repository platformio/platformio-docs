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

Tutorials
---------

* :ref:`tutorial_espressif32_arduino_debugging_unit_testing`
* :ref:`tutorial_espressif32_espidf_debugging_unit_testing_analysis`
* `Video: Free Inline Debugging for ESP32 and Arduino Sketches <https://www.youtube.com/watch?v=psMqilqlrRQ>`__

Configuration
-------------

.. contents::
    :local:

CPU Frequency
~~~~~~~~~~~~~

See :ref:`projectconf_board_build.f_cpu` option from :ref:`projectconf`

.. code-block:: ini

    [env:myenv]
    ; set frequency to 160MHz
    board_build.f_cpu = 160000000L

FLASH Frequency
~~~~~~~~~~~~~~~

Please use ``board_build.f_flash`` option from :ref:`projectconf` to change
a value. Possible values:

* ``40000000L`` (default)
* ``80000000L``

.. code-block:: ini

    [env:myenv]
    ; set frequency to 80MHz
    board_build.f_flash = 80000000L

FLASH Mode
~~~~~~~~~~

Flash chip interface mode. This parameter is stored in the binary image
header, along with the flash size and flash frequency. The ROM bootloader
in the ESP chip uses the value of these parameters in order to know how to
talk to the flash chip.

Please use ``board_build.flash_mode`` option from :ref:`projectconf` to change
a value. Possible values:

* ``qio``
* ``qout``
* ``dio``
* ``dout``

.. code-block:: ini

    [env:myenv]
    board_build.flash_mode = qio

External RAM (PSRAM)
~~~~~~~~~~~~~~~~~~~~

You can enable external RAM using the next extra :ref:`projectconf_build_flags`
in :ref:`projectconf` depending on a framework type.

Framework :ref:`framework_arduino`:

.. code-block:: ini

    [env:myenv]
    platform = espressif32
    framework = arduino
    board = ...
    build_flags =
        -DBOARD_HAS_PSRAM
        -mfix-esp32-psram-cache-issue

Framework :ref:`framework_espidf`:

.. code-block:: ini

    [env:myenv]
    platform = espressif32
    framework = espidf
    board = ...
    build_flags =
        -DCONFIG_SPIRAM_CACHE_WORKAROUND

More details are located in the official ESP-IDF documentation -
`Support for external RAM <http://esp-idf.readthedocs.io/en/latest/api-guides/external-ram.html>`_.

Debug Level
~~~~~~~~~~~

Please use one of the next :ref:`projectconf_build_flags` to change debug level.
A :ref:`projectconf_build_flags` option could be used only the one time per
build environment. If you need to specify more flags, please separate them
with a new line or space.

Actual information is available in `Arduino for ESP32 Board Manifest <https://github.com/espressif/arduino-esp32/blob/master/boards.txt#L80>`_.
Please scroll to ``esp32.menu.DebugLevel`` section.


.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    framework = arduino

    ;;;;; Possible options ;;;;;;

    ; None
    build_flags = -DCORE_DEBUG_LEVEL=0

    ; Error
    build_flags = -DCORE_DEBUG_LEVEL=1

    ; Warn
    build_flags = -DCORE_DEBUG_LEVEL=2

    ; Info
    build_flags = -DCORE_DEBUG_LEVEL=3

    ; Debug
    build_flags = -DCORE_DEBUG_LEVEL=4

    ; Verbose
    build_flags = -DCORE_DEBUG_LEVEL=5

Upload Speed
~~~~~~~~~~~~

You can set custom upload speed using  :ref:`projectconf_upload_speed` option
from :ref:`projectconf`

.. code-block:: ini

    [env:myenv]
    upload_speed = 9600

Erase Flash
~~~~~~~~~~~

Please :option:`pio run --target` the next command to erase the entire
flash chip (all data replaced with 0xFF bytes):

.. code::

    > pio run --target erase

    # or short version

    > pio run -t erase

Partition Tables
~~~~~~~~~~~~~~~~
You can create a custom partitions table (CSV) following `ESP32 Partition Tables <https://docs.espressif.com/projects/esp-idf/en/latest/api-guides/partition-tables.html>`_
documentation. PlatformIO uses **default partition tables** depending on a
:ref:`projectconf_env_framework` type:

* ``default.csv`` for :ref:`framework_arduino`
  (`show pre-configured partition tables <https://github.com/espressif/arduino-esp32/blob/master/tools/partitions>`__)
* ``partitions_singleapp.csv`` for :ref:`framework_espidf`
  (`show pre-configured partition tables <https://github.com/espressif/esp-idf/blob/master/components/partition_table>`__)

To override default table please use ``board_build.partitions`` option in
:ref:`projectconf`.

.. warning::
    SPIFFS partition **MUST** have configured "Type" as "data" and "SubType"
    as "spiffs". For example, ``spiffs, data, spiffs, 0x291000, 1M,``

Examples:

.. code-block:: ini

    ; 1) A "partitions_custom.csv" in the root of project directory
    [env:custom_table]
    board_build.partitions = partitions_custom.csv

    ; 2) Switch between built-in tables
    ; https://github.com/espressif/arduino-esp32/tree/master/tools/partitions
    ; https://github.com/espressif/esp-idf/tree/master/components/partition_table
    [env:custom_builtin_table]
    board_build.partitions = no_ota.csv

Embedding Binary Data
~~~~~~~~~~~~~~~~~~~~~

Sometimes you have a file with some binary or text data that you’d like to
make available to your program - but you don’t want to reformat the file as
C source.

There are two options ``board_build.embed_txtfiles`` and ``board_build.embed_files``
which can be used for embedding data. The only difference is that files specified
in ``board_build.embed_txtfiles`` option are null-terminated in the final binary.

.. code-block:: ini

    [env:myenv]
    platform = espressif32
    board = ...
    board_build.embed_txtfiles =
      src/private.pem.key
      src/certificate.pem.crt
      src/aws-root-ca.pem

The file contents will be added to the ``.rodata`` section in flash, and
are available via symbol names as follows:

.. code-block:: c

    extern const uint8_t aws_root_ca_pem_start[] asm("_binary_src_aws_root_ca_pem_start");
    extern const uint8_t aws_root_ca_pem_end[] asm("_binary_src_aws_root_ca_pem_end");
    extern const uint8_t certificate_pem_crt_start[] asm("_binary_src_certificate_pem_crt_start");
    extern const uint8_t certificate_pem_crt_end[] asm("_binary_src_certificate_pem_crt_end");
    extern const uint8_t private_pem_key_start[] asm("_binary_src_private_pem_key_start");
    extern const uint8_t private_pem_key_end[] asm("_binary_src_private_pem_key_end");

The names are generated from the full name of the file. Characters ``/, .``,
etc. are replaced with underscores. The ``_binary`` + ``_nested_folder`` prefix
in the symbol name is added by "objcopy" and is the same for both text and binary files.

.. note::
    With the ESP-IDF framework symbol names should not contain path to the files, for example
    ``_binary_private_pem_key_start`` instead of ``_binary_src_private_pem_key_start``.

See full example with embedding Amazon AWS certificates:

- https://github.com/platformio/platform-espressif32/tree/develop/examples/espidf-aws-iot


Uploading files to file system SPIFFS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create new project using :ref:`pioide` or initialize project using
   :ref:`piocore` and :ref:`cmd_project_init` (if you have not initialized it yet)
2. Create ``data`` folder (it should be on the same level as ``src`` folder)
   and put files here. Also, you can specify own location for
   :ref:`projectconf_pio_data_dir`
3. Run "Upload File System image" task in :ref:`pioide` or use :ref:`piocore`
   and :option:`pio run --target` command with ``uploadfs`` target.


To upload SPIFFS image using OTA update please specify ``upload_port`` /
``--upload-port`` as IP address or mDNS host name (ending with the ``*.local``).

Examples:

* `SPIFFS for Arduino <https://github.com/espressif/arduino-esp32/tree/master/libraries/SPIFFS/examples>`_
* `SPIFFS for ESP-IDF <https://github.com/espressif/esp-idf/tree/master/examples/storage/spiffs>`_


Over-the-Air (OTA) update
~~~~~~~~~~~~~~~~~~~~~~~~~

Using JFrog Bintray (free and secure Cloud solution)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Video and presentation - `swampUP: Over-The-Air (OTA) firmware upgrades for Internet of Things devices with PlatformIO and JFrog Bintray <https://www.slideshare.net/ivankravets/swampup-overtheair-ota-firmware-upgrades-for-internet-of-things-devices-with-platformio-and-jfrog-bintray>`_
* Demo source code: https://github.com/platformio/bintray-secure-ota

Using built-in Local solution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Demo code for:

* `Arduino <https://github.com/espressif/arduino-esp32/tree/master/libraries/ArduinoOTA/examples/BasicOTA>`_
* `ESP-IDF <https://github.com/espressif/esp-idf/tree/master/examples/system/ota>`_

There are 2 options:

* Directly specify :option:`pio run --upload-port` in command line

.. code-block:: bash

    pio run --target upload --upload-port IP_ADDRESS_HERE or mDNS_NAME.local

* Specify ``upload_port`` option in :ref:`projectconf`


You also need to set :ref:`projectconf_upload_protocol` to ``espota``.

.. code-block:: ini

   [env:myenv]
   upload_protocol = espota
   upload_port = IP_ADDRESS_HERE or mDNS_NAME.local

For example,

* ``pio run -t upload --upload-port 192.168.0.255``
* ``pio run -t upload --upload-port myesp8266.local``

Authentication and upload options
'''''''''''''''''''''''''''''''''

You can pass additional options/flags to OTA uploader using
``upload_flags`` option in :ref:`projectconf`

.. code-block:: ini

    [env:myenv]
    upload_protocol = espota
    ; each flag in a new line
    upload_flags =
        --port=3232

Available flags

* ``--port=ESP_PORT`` ESP32 OTA Port. **Default 8266**
* ``--auth=AUTH`` Set authentication password
* ``--spiffs`` Use this option to transmit a SPIFFS image and do not flash
  the module

For the full list with available options please run

.. code-block:: bash

    ~/.platformio/packages/framework-arduinoespressif32/tools/espota.py --help

    Usage: espota.py [options]

    Transmit image over the air to the esp32 module with OTA support.

    Options:
      -h, --help            show this help message and exit

      Destination:
        -i ESP_IP, --ip=ESP_IP
                            ESP32 IP Address.
        -I HOST_IP, --host_ip=HOST_IP
                            Host IP Address.
        -p ESP_PORT, --port=ESP_PORT
                            ESP32 ota Port. Default 3232
        -P HOST_PORT, --host_port=HOST_PORT
                            Host server ota Port. Default random 10000-60000

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
        -t TIMEOUT, --timeout=TIMEOUT
                            Timeout to wait for the ESP32 to accept invitation

.. warning::
    For windows users. To manage OTA check the ESP wifi network profile isn't checked on public
    be sure it's on private mode``


Using Arduino Framework with Staging version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PlatformIO will install the latest Arduino Core for ESP32 from
https://github.com/espressif/arduino-esp32. The `Git <https://git-scm.com>`_
should be installed in a system. To update Arduino Core to the latest revision,
please open :ref:`pioide` and navigate to ``PlatformIO Home > Platforms > Updates``.

1.  Please install :ref:`pioide`
2.  Initialize a new project, open :ref:`projectconf` and specify the link to the
    framework repository in :ref:`projectconf_env_platform_packages` section.
    For example,

    .. code-block:: ini

        [env:esp32dev]
        platform = espressif32
        board = esp32dev
        framework = arduino
        platform_packages =
            platformio/framework-arduinoespressif32 @ https://github.com/espressif/arduino-esp32.git

3.  Try to build the project
4.  If you see build errors, then try to build this project using the same
    ``stage`` with Arduino IDE
5.  If it works with Arduino IDE but doesn't work with PlatformIO, then please
    `file a new issue <https://github.com/platformio/platform-espressif32/issuess>`_
    with attached information:

    - test project/files
    - detailed log of build process from Arduino IDE (please copy it from
      console to https://hastebin.com)
    - detailed log of build process from PlatformIO Build System (please copy
      it from console to https://hastebin.com)

Arduino Core Wiki
~~~~~~~~~~~~~~~~~

Tips, tricks and common problems: http://desire.giesecke.tk/index.php/2018/01/30/esp32-wiki-entries/
