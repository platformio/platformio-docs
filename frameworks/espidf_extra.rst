..  Copyright (c) 2020-present PlatformIO <contact@platformio.org>
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

* :ref:`tutorial_espressif32_espidf_debugging_unit_testing_analysis`
* Book: `Developing IoT Projects with ESP32: Automate your home or business with inexpensive Wi-Fi devices <https://www.amazon.com/Developing-IoT-Projects-ESP32-inexpensive-ebook-dp-B093CCWGDP/dp/B093CCWGDP/>`_ (using the PlatformIO with ESP-IDF)

.. note::
  Each release of the :ref:`platform_espressif32` platform uses a specific version of ESP-IDF. The latest version of the platform only supports the latest stable version of the framework.

Configuration
-------------

.. contents::
    :local:

The general project configuration (default optimization level, bootloader configuration
partition tables, etc) is set in a single file called ``sdkconfig`` in the root folder
of the project. This configuration file can be modified via a special target called
``menuconfig`` (PlatformIO v4.3.0 greater is required):

.. code-block:: none

    pio run -t menuconfig

.. warning::
    ESP-IDF requires some extra tools to be installed in your system in order to build
    firmware for supported chips. Most of these tools are available in PlatformIO
    ecosystem as standalone packages, but in order to use configuration tool called
    ``menuconfig`` several additional packages need to be installed on Linux-based
    systems:

    .. code-block:: none

        libncurses5-dev flex bison

    More details about required packages can be found in the official ESP-IDF documentation -
    `Standard Setup of Toolchain for Linux <https://docs.espressif.com/projects/esp-idf/en/latest/get-started/linux-setup.html>`_.

.. hint::
  If menuconfig is not showed properly in the integrated VS Code terminal try changing
  the default terminal shell by clicking the dropdown menu on the top-right of the
  terminal panel and selectiing the ``Select Default Shell`` option.

.. hint::
  In case the ``UP`` and ``DOWN`` arrows don't work in menuconfig try using the ``J``
  key to move the cursor down and ``K`` to move the cursor up. Another option is to use
  ``-`` and ``+`` keys on the numeric keypad.

Project Structure
~~~~~~~~~~~~~~~~~

The ESP-IDF framework requires an unusual project structure because most of the framework
configuration is performed by the native for the ESP-IDF build system called ``CMake``.

A typical PlatformIO project for the ESP-IDF framework must have the following structure:

.. code-block:: none

    project_dir
    ├── include
    ├── src
    │    ├── CMakeLists.txt
    │    └── main.c
    ├── CMakeLists.txt
    └── platformio.ini

.. tip::
    It's also possible to use the default ESP-IDF project structure with ``main`` folder.
    To specify ``main`` as the folder with source files use :ref:`projectconf_pio_src_dir`
    option, for example:

    .. code-block:: ini

        [platformio]
        src_dir = main

        [env:esp32dev]
        platform = platformio/espressif32
        framework = espidf
        board = esp32dev


Besides the files related to PlatformIO project, there are several additional
ESP-IDF-specific files: the main ``CMakeLists.txt``, project-specific ``CMakeLists.txt``
in :ref:`projectconf_pio_src_dir` and optional default configuration file ``sdkconfig.defaults``.
``CMakeLists.txt`` files enable features supported by the ESP-IDF's build system, e.g.
ULP configuration, adding extra components, etc. A typical ``CMakeLists.txt`` file in
the root folder has the following content:

.. code-block:: cmake

    # The following lines of boilerplate have to be in your project's CMakeLists
    # in this exact order for cmake to work correctly
    cmake_minimum_required(VERSION 3.16.0)

    include($ENV{IDF_PATH}/tools/cmake/project.cmake)
    project(project-name)

The second ``CMakeLists.txt`` in :ref:`projectconf_pio_src_dir` is responsible for
controlling the build process of the component and its integration into the overall
project. The minimal component ``CMakeLists.txt`` file simply registers the component to
the build system using ``idf_component_register``:

.. code-block:: cmake

    idf_component_register(SRCS "foo.c" "bar.c")

The files specified using ``idf_component_register`` are used **ONLY** for generating
build configurations, but it's highly recommended to specify all application source
files in order to keep the project compatible with the usual ESP-IDF workflow.

.. warning::
    By default PlatformIO expects source files to be located in the ``src`` folder. At
    the same time, the default location for source files within the ESP-IDF build system
    is a special folder with the name ``main``. Renaming the main component may require
    users to manually specify additional dependencies:

    .. code-block:: cmake

        idf_component_register(SRCS "main.c" REQUIRES idf::mbedtls)

    More details in the official ESP-IDF documentation -
    `Renaming main component <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/build-system.html?highlight=rename#renaming-main-component>`_.

Due to the current limitations of CMake file-based API, there is no way of generating
build configuration for source files written in various programming languages if they
are not specified in  ``idf_component_register`` command. If your project contains
libraries written in languages that differ from the language used for the main
application you need to create an empty file with the desired extension (e.g. ``*.cpp``
for ``C++``) in order to force CMake generate build configuration for this language.

.. note::
    Build configuration generated for source files specified in ``idf_component_register``
    is also used as the base build environment for project sources (including libraries).


ESP-IDF components
~~~~~~~~~~~~~~~~~~

ESP-IDF modules as modular pieces of standalone code might be useful for structuring
reusable code or including third party components that aren’t part of ESP-IDF.

These components contain either a single ``CMakeLists.txt`` file which controls the
build process of the component and its integration into the overall project. An
optional ``Kconfig`` file defines the component configuration options that can be set
via ``menuconfig``. Some components may also include ``Kconfig.projbuild`` and
``project_include.cmake`` files, which are special files for overriding parts of the
project. All valid components will be compiled as static libraries and linked to the
final firmware. There are two possible ways of adding extra components to PlatformIO
project:

* By adding a new component to an optional folder called ``components`` in the root of
  your project. This folder will be automatically scanned for valid components.
* Using ``EXTRA_COMPONENT_DIRS`` option in the root ``CMakeLists.txt`` file. This option
  represents a list of extra directories to search for components.

An example of specifying ``esp-aws-iot`` as an extra component:

.. code-block:: cmake

    # The following lines of boilerplate have to be in your project's CMakeLists
    # in this exact order for cmake to work correctly
    cmake_minimum_required(VERSION 3.16)

    include($ENV{IDF_PATH}/tools/cmake/project.cmake)
    list(APPEND EXTRA_COMPONENT_DIRS esp-aws-iot)
    project(subscribe_publish)

.. warning::
    Since :ref:`projectconf_pio_src_dir` is also passed to CMake as an extra component,
    you should only append to ``EXTRA_COMPONENT_DIRS`` variable in order not to override
    the default package.

Since the build may not work correctly if the full path to sources is greater than 250
characters (see ``CMAKE_OBJECT_PATH_MAX``) it might be a good idea to keep modules close
to the project files.

ULP coprocessor programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to take measurements using ADC, internal temperature sensor or external
I2C sensors, while the main processors are in deep sleep mode you need to use ULP
coprocessor. At the moment ULP can be used only with the :ref:`framework_espidf`.

All ULP code, usually written in assembly in files with ``.S`` extension,
must be placed into a separate directory with the name ``ulp`` in the root folder
of your project. So your project structure should look like this:

.. code-block:: none

    project_dir
    ├── include
    ├── src
    │    ├── CMakeLists.txt
    │    └── main.c
    ├── ulp
    │    └── ulp_code.S
    ├── CMakeLists.txt
    └── platformio.ini

Since PlatformIO uses the code model generated by CMake it's mandatory to specify ULP
source files in ``CMakeLists.txt`` as well. An example of typical ``CMakeLists.txt``
for ULP:

.. code-block:: cmake

    idf_component_register(SRCS "ulp_adc_example_main.c")
    #
    # ULP support additions to component CMakeLists.txt.
    #
    # 1. The ULP app name must be "ulp_main"
    set(ulp_app_name ulp_main)
    #
    # 2. Specify all assembly source files.
    #    Paths are relative because ULP files are placed into a special directory "ulp"
    #    in the root of the project
    set(ulp_s_sources "../ulp/adc.S")
    #
    # 3. List all the component source files which include automatically
    #    generated ULP export file, ${ulp_app_name}.h:
    set(ulp_exp_dep_srcs "ulp_adc_example_main.c")
    #
    # 4. Call function to build ULP binary and embed in project using the argument
    #    values above.
    ulp_embed_binary(${ulp_app_name} ${ulp_s_sources} ${ulp_exp_dep_srcs})

See full examples with ULP coprocessor programming:

- https://github.com/platformio/platform-espressif32/tree/develop/examples/espidf-ulp-adc
- https://github.com/platformio/platform-espressif32/tree/develop/examples/espidf-ulp-pulse

More details are located in the official ESP-IDF documentation -
`ULP coprocessor programming <https://docs.espressif.com/projects/esp-idf/en/latest/api-guides/ulp.html#accessing-ulp-program-variable>`_.

Security Features
~~~~~~~~~~~~~~~~~

.. warning::

    This functionality can **brick your device** if used incorrectly.

    **Proceed with extreme caution. Everything you do is at your own risk.**

.. warning::

    By default, enabling Flash Encryption and/or Secure Boot will disable JTAG debugging.
    On first boot, the bootloader will burn an eFuse bit to permanently disable JTAG at the
    same time it enables the other features.

.. tip::

    It's strongly recommended to test the security features using
    the vendor-provided QEMU emulator.

.. note::

    When enabling the Flash Encryption and Secure Boot v2 together, the
    Flash Encryption should be enabled first.

.. note::

    To use this functionality, the version of the `espressif32 <https://registry.platformio.org/platforms/platformio/espressif32>`_ development platform must be **v6.12.0 or later**.

Before you begin working with these security features, make sure to carefully
read the official documentation provided by the vendor. Here are several useful
pages to get started:

- `Security Features Overview <https://docs.espressif.com/projects/esp-idf/en/release-v5.4/esp32/security/security.html>`_
- `Flash Encryption <https://docs.espressif.com/projects/esp-idf/en/release-v5.4/esp32/security/flash-encryption.html>`_
- `Flash Encryption section from ESP-IDF Programming Guide <https://espressif-docs.readthedocs-hosted.com/projects/esp-idf/en/latest/security/flash-encryption.html>`_
- `Secure Boot v2 <https://docs.espressif.com/projects/esp-idf/en/stable/esp32/security/secure-boot-v2.html>`_
- `Secure Boot section from ESP-IDF Programming Guide <https://espressif-docs.readthedocs-hosted.com/projects/esp-idf/en/latest/security/secure-boot.html>`_
- `Vulnerabilities <https://docs.espressif.com/projects/esp-idf/en/stable/esp32/security/vulnerabilities.html>`_

Flash Encryption
^^^^^^^^^^^^^^^^

.. warning::

    Enabling flash encryption limits the options for further updates of your device.
    Before using this feature, make sure to read the entire page and fully
    understand the implications.

.. warning::

    Enabling flash encryption will increase the size of the bootloader, which might
    require updating partition table offset.


Flash encryption is intended for encrypting the contents of the ESP32's off-chip flash memory. Once this feature is enabled, firmware is flashed as plaintext, and then the data is encrypted in place on the first boot. As a result, physical readout of flash will not be sufficient to recover most flash contents.

It's recommended to read the official `Flash Encryption Programming Guide <https://docs.espressif.com/projects/esp-idf/en/v5.4.1/esp32/security/flash-encryption.html>`_ to understand the overall workflow before getting started. Here's an adapted version of that page that uses PlatformIO packages to enable the Flash Encryption Feature on ESP32 ECO V3 target:

1. Ensure that you have an ESP32 device with default Flash Encryption eFuse settings as shown in `Relevant eFuses <https://docs.espressif.com/projects/esp-idf/en/v5.4.1/esp32/security/flash-encryption.html#flash-encryption-efuse>`_. At this point, the Flash Encryption must not be already enabled on the chip.

2. Generate a Flash Encryption key

A random Flash Encryption key can be generated by running:

.. code-block:: bash

    pio pkg exec --package "platformio/tool-esptoolpy" -- espsecure.py generate_flash_encryption_key my_flash_encryption_key.bin

Set the ``board_build.encryption_key`` option in your ``platformio.ini`` file to
the name of the key:

.. code-block:: ini

    [env:esp32dev]
    platform = platformio/espressif32
    framework = espidf
    ...
    board_build.encryption_key = my_flash_encryption_key.bin

3. Burn the Flash Encryption key into eFuse

.. warning::

    Burning this key into eFuse is a permanent action and cannot be undone.

Where ``$PORT`` is the serial port of your target device:

.. code-block:: bash

    pio pkg exec --package "platformio/tool-esptoolpy" -- espefuse.py --port $PORT burn_key flash_encryption my_flash_encryption_key.bin

4. Burn the ``FLASH_CRYPT_CNT`` eFuse

If you only want to enable Flash Encryption in Development mode and want to keep the ability to disable it in the future, Update the ``FLASH_CRYPT_CNT`` value in the below command from ``127`` to ``0x1`` (not recommended for production).

.. code-block:: bash

    pio pkg exec --package "platformio/tool-esptoolpy" -- espefuse.py --port $PORT --chip esp32 burn_efuse FLASH_CRYPT_CNT 127

In the case of ESP32, you also need to burn the ``FLASH_CRYPT_CONFIG`` fuse. It can be done by running:

.. code-block:: bash

    pio pkg exec --package "platformio/tool-esptoolpy" -- espefuse.py --port $PORT --chip esp32 burn_efuse FLASH_CRYPT_CONFIG 0xF

5. Burn Flash Encryption-related security eFuses

.. note::

    For production use cases, it is highly recommended to burn all the eFuses listed below.

- ``DISABLE_DL_ENCRYPT`` - Disable the UART bootloader encryption access
- ``DISABLE_DL_DECRYPT`` - Disable the UART bootloader decryption access
- ``DISABLE_DL_CACHE`` - Disable the UART bootloader flash cache access
- ``JTAG_DISABLE`` - Disable the JTAG

The respective eFuses can be burned by running:

.. code-block:: bash

    pio pkg exec --package "platformio/tool-esptoolpy" -- espefuse.py burn_efuse --port $PORT EFUSE_NAME 0x1

6. Write protect security eFuses

After burning the respective eFuses, we need to ``write_protect`` the security configurations.
It can be done by burning following eFuse:

.. code-block:: bash

    pio pkg exec --package "platformio/tool-esptoolpy" -- espefuse.py --port $PORT write_protect_efuse DIS_CACHE

.. warning::

    The write protection of above eFuse also write protects multiple other eFuses. Please refer to the ESP32 eFuse table for more details.

7. Configure the project

Flash Encryption release mode can be set in the your ``sdkconfig.defaults`` as follows:

.. code-block:: bash

    # Enable Flash Encryption on boot
    CONFIG_SECURE_FLASH_ENC_ENABLED=y

    # Select the RELEASE mode
    CONFIG_SECURE_FLASH_ENCRYPTION_MODE_RELEASE=y

    # Select UART ROM download mode (permanently disabled (recommended))
    CONFIG_SECURE_DISABLE_ROM_DL_MODE=y

    # Select the appropriate bootloader log verbosity (for example info)
    CONFIG_BOOTLOADER_LOG_LEVEL_INFO=y

.. warning::

    Note that once release mode is selected, the ``DISABLE_DL_ENCRYPT`` and ``DISABLE_DL_DECRYPT`` eFuse bits will be burned to disable Flash Encryption hardware in ROM download mode

8. Add extra upload flags

Since the Flash Encryption feature was enabled in advance and we're uploading pre-encrypted binaries, we need to add a special ``--force`` flag to the upload process using an extra script:

.. code-block:: ini

    [env:esp32dev]
    platform = platformio/espressif32
    framework = espidf
    ...
    extra_scripts = force_upload.py
    ...

The ``force_upload.py`` file should contain the following:

.. code-block:: python

    Import ("env")

    env.Append(UPLOADCMD=" ".join(["$UPLOADCMD", "--force"]))

9. Build, Encrypt and Upload the binaries

The project can be built via the usual ``run`` command.

.. code-block:: bash

    pio run

The encrypted binaries can be generated by running the ``encrypt`` target:

.. code-block:: bash

    pio run -t encrypt

To upload the encrypted binaries run the combination of the ``encrypt`` and ``upload`` targets:

.. code-block:: bash

    pio run -t encrypt -t upload

10. Secure the ROM download mode

.. warning::

    Please perform the following step at the very end after enabling Flash Encryption and Secure Boot features.
    Once this eFuse is burned, the espefuse tool can no longer be used to burn additional eFuses.

Disable UART ROM DL mode:

.. code-block:: bash

    pio pkg exec --package "platformio/tool-esptoolpy" -- espefuse.py --port $PORT burn_efuse UART_DOWNLOAD_DIS

11. Delete Flash Encryption key on host

Once the Flash Encryption has been enabled for the device, the key must be deleted immediately. This ensures that the host can't produce encrypted binaries for the same device going forward. This step is important to reduce the vulnerability of the Flash Encryption key.

Secure Bootloader
^^^^^^^^^^^^^^^^^

Secure Boot protects a device from running any unauthorized (i.e., unsigned) code by checking that each piece of software that is being booted is signed. On an ESP32, these pieces of software include the second stage bootloader and each application binary. Note that the first stage (ROM) bootloader does not require signing as it is ROM code and thus cannot be changed.

.. warning::

    Only Secure Boot v2 is supported

.. warning::

    The Secure Boot v2 option is available on ESP32 chips starting from
    revision v3.0. To enable this option in ``menuconfig``,
    set ``CONFIG_ESP32_REV_MIN`` to v3.0 or higher.

.. warning::

    If Secure Boot or Flash Encryption is enabled, the reset method is set
    to ``no_reset`` to stay in the bootloader after uploading.

.. note::

    Turning on Secure Boot increases the bootloader size,
    which may require adjusting the partition table offset.

.. note::

    By default, the bootloader binary is not programmed unless the
    ``CONFIG_SECURE_BOOT_FLASH_BOOTLOADER_DEFAULT`` option is explicitly enabled
    in your ``sdkconfig`` file.

It's recommended to read the official `Secure Boot Programming Guide <https://docs.espressif.com/projects/esp-idf/en/stable/esp32/security/secure-boot-v2.html>`_ to understand the overall workflow before getting started. Here's an adapted version of that page that uses PlatformIO packages to build,
sign and upload binaries:

.. warning::

    The instructions below are intended for ESP32 targets. For other variants open `Secure Boot Programming Guide <https://docs.espressif.com/projects/esp-idf/en/stable/esp32/security/secure-boot-v2.html>`_ and select your target from the menu on the left.

1. Generate Secure Boot Signing Private Key:

.. code-block:: bash

    pio pkg exec --package "platformio/tool-esptoolpy" -- espsecure.py generate_signing_key --version 2 --scheme rsa3072 secure_boot_signing_key.pem

.. hint::

    For production environments, we recommend generating the key pair using OpenSSL or another industry-standard encryption program.

.. note::

    ``secure_boot_signing_key.pem``  is the default key name. If you change it, don't forget to update your project configuration accordingly. For example,
    by adding the ``CONFIG_SECURE_BOOT_SIGNING_KEY="my_sb_signing_key.pem"``
    option to your ``sdkconfig.defaults``.

2. Generate Public Key Digest:

.. code-block:: bash

    pio pkg exec --package "platformio/tool-esptoolpy" -- espsecure.py digest_sbv2_public_key --keyfile secure_boot_signing_key.pem --output digest.bin

3. Burn the key digest in eFuse:

Where ``$PORT`` is the serial port of your target device:

.. code-block:: bash

    pio pkg exec --package "platformio/tool-esptoolpy" -- espefuse.py --port $PORT --chip esp32 burn_key secure_boot_v2 digest.bin

4. Enable Secure Boot:

.. code-block:: bash

    pio pkg exec --package "platformio/tool-esptoolpy" -- espefuse.py --port $PORT --chip esp32 burn_efuse ABS_DONE_1


5. Burn security eFuses:

- ``JTAG_DISABLE``: Disable the JTAG.

.. code-block:: bash

    pio pkg exec --package "platformio/tool-esptoolpy" -- espefuse.py burn_efuse --port $PORT JTAG_DISABLE 0x1

6. Burn Secure Boot related eFuses

The Secure Boot digest burned in the eFuse must be kept readable otherwise the Secure Boot operation would result in a failure. To prevent the accidental enabling of read protection for this key block, the following eFuse needs to be burned:

.. code-block:: bash

    pio pkg exec --package "platformio/tool-esptoolpy" -- espefuse.py -p $PORT write_protect_efuse RD_DIS

.. warning::

    After burning above-mentioned eFuse, the read protection can't be enabled for any key. For example, if Flash Encryption which requires read protection for its key is not enabled at this point, then it can't be enabled afterwards. Please ensure that no eFuse keys are going to need read protection after completing this step.

7. Configure the project:

The Secure Boot can be enabled either by running the ``pio run -t menuconfig``
target and setting ``Security features -> Enable hardware Secure Boot`` option.

.. note::

    For ESP32, Secure Boot v2 is available only for ESP32 ECO3 onwards.
    To view the Secure Boot v2 option the chip revision should be changed to
    revision v3.0 (ECO3). To change the chip revision, run the ``menuconfig``
    target and set ``Minimum Supported ESP32 Revision`` to ``Rev 3.0 (ECO3)`` in ``Component Config -> Hardware Settings -> Chip Revision``

or directly in the ``sdkconfig.defaults`` file:

.. code-block:: bash

    # ESP32-specific settings
    CONFIG_ESP32_REV_MIN_3=y

    # Secure Boot settings
    CONFIG_SECURE_BOOT=y
    CONFIG_SECURE_BOOT_V2_ENABLED=y

.. note::

    By default PlatformIO won't automatically sign any built binaries,
    unless the ``CONFIG_SECURE_BOOT_BUILD_SIGNED_BINARIES`` option is set.

8. Build, Sign and Upload the binaries:

The project can be built via the usual ``run`` command.

.. code-block:: bash

    pio run

Signed binaries will be generated automatically if the ``CONFIG_SECURE_BOOT_BUILD_SIGNED_BINARIES`` option is enabled.
Alternatively, they can be generated by running the ``sign`` target:

.. code-block:: bash

    pio run -t sign

To upload the signed binaries run the usual ``upload`` target
(if the ``CONFIG_SECURE_BOOT_BUILD_SIGNED_BINARIES`` option is enabled)
or use the combination of the ``sign`` and ``upload`` targets:

.. code-block:: bash

    pio run -t sign -t upload

.. note::

    By default the bootloader binary is not uploaded when Secure Boot is enabled
    unless the ``SECURE_BOOT_FLASH_BOOTLOADER_DEFAULT`` is enabled.
    As an alternative, there is a special target ``pio run -t sign -t upload-bootloader`` that can be used to upload only the signed bootloader binary.

9. Secure the ROM download mode:

.. warning::

    Please perform the following step at the very end.
    After this eFuse is burned, the ``espefuse`` tool can no longer
    be used to burn additional eFuses.

Burn the fuse that disables the UART ROM download mode

.. code-block:: bash

    pio pkg exec --package "platformio/tool-esptoolpy" -- espefuse.py --port $PORT burn_efuse UART_DOWNLOAD_DIS

.. note::

    It is recommended to store the Secure Boot key in a highly secure place. A physical or a cloud HSM may be used for secure storage of the Secure Boot private key.

NVS Encryption: Flash Encryption-Based Scheme
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::

    The instructions below are intended for ESP32 targets. For other variants open `Secure Boot Programming Guide <https://docs.espressif.com/projects/esp-idf/en/v5.4.1/esp32/security/security-features-enablement-workflows.html#enable-nvs-encryption-externally>`_ and select your target from the menu on the left.

.. note::

    In this scheme, the keys required for NVS encryption are stored in yet another partition, which is protected using Flash Encryption. Therefore, enabling Flash Encryption becomes a prerequisite for NVS encryption here.

.. note::

    An application requiring NVS encryption support (using the Flash Encryption-based scheme) needs to be compiled with a key-partition of the type data and subtype ``nvs_keys``. This partition should be marked as encrypted and its size should be the minimum partition size (4 KB).

.. note::

    NVS encryption is enabled by default when Flash Encryption is enabled. This is done because Wi-Fi driver stores credentials (like SSID and passphrase) in the default NVS partition. It is important to encrypt them as default choice if platform-level encryption is already enabled.

It's recommended to read the official `NVS Encryption Guide <https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/storage/nvs_encryption.html>`_ to understand the overall workflow before getting started. Here's an adapted version of that page that uses PlatformIO packages to build,
sign and upload binaries:

1. Generate the NVS encryption key

The NVS Encryption key can be generated using the following command. This key is then flashed on the chip and protected with the help of Flash Encryption features

.. code-block:: bash

    pio pkg exec --package "platformio/framework-espidf" -- components/nvs_flash/nvs_partition_generator/nvs_partition_gen.py generate-key --keyfile nvs_encr_key.bin

This command will generate the respective key in the ``keys`` folder.

2. Generate an encrypted NVS partition

On this step we need to generate an encrypted NVS partition from a special CSV file. Please refer to `Generate Encrypted NVS Partition <https://docs.espressif.com/projects/esp-idf/en/v5.4.1/esp32/api-reference/storage/nvs_partition_gen.html#generate-encrypted-nvs-partition>`_ and `CSV File Format <https://docs.espressif.com/projects/esp-idf/en/v5.4.1/esp32/api-reference/storage/nvs_partition_gen.html#nvs-csv-file-format>`_ for more details.

.. code-block:: bash

    pio pkg exec --package "platformio/framework-espidf" -- components/nvs_flash/nvs_partition_generator/nvs_partition_gen.py encrypt nvs_data.csv nvs_encr_partition.bin 0x121000 --inputkey keys/nvs_encr_key.bin

- ``nvs_data.csv`` - a CSV file which contains the NVS data
- ``0x121000`` is the NVS partition offset according to your partition table
- ``keys/nvs_encr_key.bin`` is an encryption key generated on the previous step


3. Configure the project

The NVS encryption using Flash Encryption can be enabled in your ``sdkconfig.defaults`` as follows:

.. code-block:: bash

    CONFIG_NVS_ENCRYPTION=y
    CONFIG_NVS_SEC_KEY_PROTECT_USING_FLASH_ENC=y

4. Flash NVS partition and NVS encryption keys

.. note::

    If Flash Encryption is enabled, the ``nvs_key`` partition need to be encrypted using Flash Encryption key before flashing.

.. code-block:: bash

    pio pkg exec --package "platformio/tool-esptoolpy" -- espsecure.py encrypt_flash_data --keyfile my_flash_encryption_key.bin --address 0x120000
    --output keys/nvs_encr_key-encrypted.bin keys/nvs_encr_key.bin

- ``my_flash_encryption_key.bin`` - is your Flash Encryption Key
- ``0x120000`` is the NVS Key partition offset according to your partition table
- ``keys/nvs_encr_key.bin`` is an encryption key generated on the previous step

The final binaries can be uploaded via the ``esptool.py`` tool with corresponding offsets. You can change generic hardware parameters according to your target:

.. code-block:: bash

    pio pkg exec --package "platformio/tool-esptoolpy" -- esptool.py --chip esp32 -p $PORT --before=default_reset --after=no_reset write_flash --flash_mode dio --flash_freq 80m --flash_size 4MB 0x120000 keys/nvs_encr_key-encrypted.bin 0x121000 nvs_encr_partition-encrypted.bin --force

- ``$PORT`` is the serial port of your target device
- ``0x120000`` is the NVS Key partition offset according to your partition table
- ``0x121000`` is the NVS partition offset according to your partition table
- ``keys/nvs_encr_key.bin`` is an encryption key generated on the previous step

Limitations
-----------

At the moment several limitations are present:

* No whitespace characters allowed in project paths. This limitation is imposed by the
  `native ESP-IDF build system <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html?highlight=spaces#step-2-get-esp-idf>`_.
  This affects users that have a whitespace in their username or added a whitespace to
  the project name. As a workaround, it's recommended to move :ref:`projectconf_pio_core_dir`
  to a folder without spaces. For example:

  .. code-block:: ini

        [platformio]
        core_dir = C:/.platformio

        [env:esp32dev]
        platform = platformio/espressif32
        framework = espidf
        board = esp32dev

* The ``src_filter`` option cannot be used. It's done to preserve compatibility with
  existing ESP-IDF projects. List of source files is specified in the project
  ``CMakeLists.txt`` file.
