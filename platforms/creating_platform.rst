..  Copyright 2014-present PlatformIO <contact@platformio.org>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _platform_creating:

Custom Development Platform
===========================

*PlatformIO* was developed like a tool that may build the same source code
for the different development platforms via single command :ref:`cmd_run`
without any dependent software or requirements.

For this purpose *PlatformIO* uses own pre-configured platforms data:
build scripts, toolchains, the settings for the most popular embedded
boards and etc. These data are pre-built and packaged to the different
``packages``. It allows *PlatformIO* to have multiple development platforms
which can use the same packages(toolchains, frameworks), but have
different/own build scripts, uploader and etc.

.. note::
    If you want to change some build flags for the existing
    :ref:`platforms`, you don't need to create (or duplicate) own
    development platforms! Please use :ref:`projectconf_build_flags` option.

**Step-by-Step Manual**

1. Choose :ref:`platform_creating_packages` for platform
2. Create :ref:`platform_creating_manifest_file`
3. Create :ref:`platform_creating_build_script`
4. Finish with the :ref:`platform_creating_installation`.

.. contents::

.. _platform_creating_packages:

Packages
--------

*PlatformIO* has pre-built packages for the most popular operation systems:
*Mac OS*, *Linux (+ARM)* and *Windows*.

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinoavr <http://arduino.cc/en/Reference/HomePage>`__
      - Arduino Wiring-based Framework (AVR Core, 1.6)

    * - `framework-arduinoespressif32 <https://github.com/espressif/arduino-esp32>`__
      - Arduino Wiring-based Framework (ESP32 Core)

    * - `framework-arduinoespressif8266 <https://github.com/esp8266/Arduino>`__
      - Arduino Wiring-based Framework (ESP8266 Core)

    * - `framework-arduinointel <https://github.com/01org/corelibs-arduino101>`__
      - Arduino Wiring-based Framework (Intel ARC Core)

    * - `framework-arduinomicrochippic32 <https://github.com/chipKIT32/chipKIT-core>`__
      - Arduino Wiring-based Framework (PIC32 Core)

    * - `framework-arduinomsp430 <http://arduino.cc/en/Reference/HomePage>`__
      - Arduino Wiring-based Framework (MSP430 Core)

    * - `framework-arduinonordicnrf51 <https://github.com/RFduino/RFduino>`__
      - Arduino Wiring-based Framework (RFduino Core)

    * - `framework-arduinosam <http://arduino.cc/en/Reference/HomePage>`__
      - Arduino Wiring-based Framework (SAM Core, 1.6)

    * - `framework-arduinoststm32 <https://github.com/rogerclarkmelbourne/Arduino_STM32>`__
      - Arduino Wiring-based Framework (STM32 Core)

    * - `framework-arduinoteensy <http://arduino.cc/en/Reference/HomePage>`__
      - Arduino Wiring-based Framework

    * - `framework-artik-sdk <http://www.artik.io>`__
      - ARTIK SDK is a C/C++ SDK targeting Samsung ARTIK platforms

    * - `framework-cmsis <http://www.arm.com/products/processors/cortex-m/cortex-microcontroller-software-interface-standard.php>`__
      - Vendor-independent hardware abstraction layer for the Cortex-M processor series

    * - `framework-energiamsp430 <http://energia.nu/reference/>`__
      - Energia Wiring-based Framework (MSP430 Core)

    * - `framework-energiativa <http://energia.nu/reference/>`__
      - Energia Wiring-based Framework (LM4F Core)

    * - `framework-espidf <https://github.com/espressif/esp-idf>`__
      - Espressif IoT Development Framework

    * - `framework-libopencm3 <http://www.libopencm3.org/>`__
      - libOpenCM3 Framework

    * - `framework-mbed <http://mbed.org>`__
      - mbed Framework

    * - `framework-pumbaa <https://github.com/eerimoq/pumbaa>`__
      - Pumbaa Framework

    * - `framework-simba <https://github.com/eerimoq/simba>`__
      - Simba Framework

    * - `framework-spl <http://www.st.com/web/catalog/tools/FM147/CL1794/SC961/SS1743/PF257890>`__
      - Standard Peripheral Library for STM32 MCUs

    * - `framework-wiringpi <http://wiringpi.com>`__
      - GPIO Interface library for the Raspberry Pi

    * - `ldscripts <https://sourceware.org/binutils/docs/ld/Scripts.html>`__
      - Linker Scripts

    * - `sdk-esp8266 <http://bbs.espressif.com>`__
      - ESP8266 SDK

    * - `tool-arduino101load <https://github.com/01org/intel-arduino-tools>`__
      - Genuino101 uploader

    * - `tool-avrdude <http://www.nongnu.org/avrdude/>`__
      - AVRDUDE

    * - `tool-bossac <https://sourceforge.net/projects/b-o-s-s-a/>`__
      - BOSSA CLI

    * - `tool-espotapy <https://github.com/esp8266/Arduino/blob/master/tools/espota.py>`__
      - ESP8266 OTA utility

    * - `tool-esptool <https://github.com/igrr/esptool-ck>`__
      - esptool-ck

    * - `tool-esptoolpy <https://github.com/espressif/esptool>`__
      - Espressif ROM Bootloader utility

    * - `tool-lm4flash <http://www.ti.com/tool/lmflashprogrammer>`__
      - Flash Programmer

    * - `tool-micronucleus <https://github.com/micronucleus/micronucleus>`__
      - Micronucleus

    * - `tool-mkspiffs <https://github.com/igrr/mkspiffs>`__
      - Tool to build and unpack SPIFFS images

    * - `tool-mspdebug <http://mspdebug.sourceforge.net/>`__
      - MSPDebug

    * - `tool-openocd <http://openocd.org>`__
      - OpenOCD

    * - `tool-pic32prog <https://github.com/sergev/pic32prog>`__
      - pic32prog

    * - `tool-rfdloader <https://github.com/RFduino/RFduino>`__
      - rfdloader

    * - `tool-scons <http://www.scons.org>`__
      - SCons software construction tool

    * - `tool-sreccat <https://github.com/marcows/SRecord>`__
      - Merging tool

    * - `tool-stlink <https://github.com/texane/stlink>`__
      - ST-Link

    * - `tool-stm32duino <https://github.com/rogerclarkmelbourne/Arduino_STM32>`__
      - STM32Duino Tools

    * - `tool-teensy <https://www.pjrc.com/teensy/loader.html>`__
      - Teensy Loader

    * - `toolchain-atmelavr <https://gcc.gnu.org/wiki/avr-gcc>`__
      - avr-gcc

    * - `toolchain-gccarmlinuxgnueabi <https://gcc.gnu.org>`__
      - GCC for Linux ARM GNU EABI

    * - `toolchain-gccarmnoneeabi <https://launchpad.net/gcc-arm-embedded>`__
      - gcc-arm-embedded

    * - `toolchain-gcclinux32 <https://gcc.gnu.org>`__
      - GCC for Linux i686

    * - `toolchain-gcclinux64 <https://gcc.gnu.org>`__
      - GCC for Linux x86_64

    * - `toolchain-gccmingw32 <http://www.mingw.org>`__
      - MinGW

    * - `toolchain-icestorm <http://www.clifford.at/icestorm/>`__
      - Tools for analyzing and creating bitstream files for FPGA IceStorm

    * - `toolchain-intelarc32 <https://github.com/foss-for-synopsys-dwc-arc-processors/toolchain>`__
      - GCC for Intel ARC

    * - `toolchain-iverilog <http://iverilog.icarus.com>`__
      - Verilog simulation and synthesis tool

    * - `toolchain-microchippic32 <https://github.com/chipKIT32/chipKIT-cxx>`__
      - GCC for Microchip PIC32

    * - `toolchain-timsp430 <http://sourceforge.net/projects/mspgcc/>`__
      - msp-gcc

    * - `toolchain-xtensa <https://github.com/jcmvbkbc/gcc-xtensa>`__
      - xtensa-gcc

    * - `toolchain-xtensa32 <https://github.com/espressif/esp-idf>`__
      - xtensa32-gcc

.. _platform_creating_manifest_file:

Manifest File ``platform.json``
-------------------------------

.. code-block:: json

    {
      "name": "myplatform",
      "title": "My Platform",
      "description": "My custom development platform",
      "url": "http://example.com",
      "homepage": "http://platformio.org/platforms/myplatform",
      "license": "Apache-2.0",
      "engines": {
        "platformio": "~3.0.0",
        "scons": ">=2.3.0,<2.6.0"
      },
      "repository": {
        "type": "git",
        "url": "https://github.com/platformio/platform-myplatform.git"
      },
      "version": "0.0.0",
      "packageRepositories": [
        "https://dl.bintray.com/platformio/dl-packages/manifest.json",
        "https://sourceforge.net/projects/platformio-storage/files/packages/manifest.json/download",
        "http://dl.platformio.org/packages/manifest.json",
        {
          "framework-%FRAMEWORK_NAME_1%": [
            {
              "url": "http://dl.example.com/packages/framework-%FRAMEWORK_NAME_1%-1.10607.0.tar.gz",
              "sha1": "adce2cd30a830d71cb6572575bf08461b7b73c07",
              "version": "1.10607.0",
              "system": "*"
            }
          ]
        }
      ],
      "frameworks": {
        "%FRAMEWORK_NAME_1%": {
          "package": "framework-%FRAMEWORK_NAME_1%",
          "script": "builder/frameworks/%FRAMEWORK_NAME_1%.py"
        },
        "%FRAMEWORK_NAME_N%": {
          "package": "framework-%FRAMEWORK_NAME_N%",
          "script": "builder/frameworks/%FRAMEWORK_NAME_N%.py"
        }
      },
      "packages": {
        "toolchain-gccarmnoneeabi": {
          "type": "toolchain",
          "version": ">=1.40803.0,<1.40805.0"
        },
        "framework-%FRAMEWORK_NAME_1%": {
          "type": "framework",
          "optional": true,
          "version": "~1.10607.0"
        },
        "framework-%FRAMEWORK_NAME_N%": {
          "type": "framework",
          "optional": true,
          "version": "~1.117.0"
        },
        "tool-direct-vcs-url": {
          "type": "framework",
          "optional": true,
          "version": "https://github.com/user/repo.git"
        }
      }
    }

.. _platform_creating_build_script:

Build Script ``main.py``
------------------------

Platform's build script is based on a next-generation build tool named
`SCons <http://www.scons.org>`_. PlatformIO has own built-in firmware builder
``env.BuildProgram`` with the deep libraries search. Please look into a
base template of ``main.py``.

.. code-block:: python

    """
        Build script for test.py
        test-builder.py
    """

    from os.path import join
    from SCons.Script import AlwaysBuild, Builder, Default, DefaultEnvironment

    env = DefaultEnvironment()

    # A full list with the available variables
    # http://www.scons.org/doc/production/HTML/scons-user.html#app-variables
    env.Replace(
        AR="ar",
        AS="gcc",
        CC="gcc",
        CXX="g++",
        OBJCOPY="objcopy",
        RANLIB="ranlib",

        ARFLAGS=["..."],

        ASFLAGS=["flag1", "flag2", "flagN"],
        CCFLAGS=["flag1", "flag2", "flagN"],
        CXXFLAGS=["flag1", "flag2", "flagN"],
        LINKFLAGS=["flag1", "flag2", "flagN"],

        CPPDEFINES=["DEFINE_1", "DEFINE=2", "DEFINE_N"],

        LIBS=["additional", "libs", "here"],

        UPLOADER=join("$PIOPACKAGES_DIR", "tool-bar", "uploader"),
        UPLOADCMD="$UPLOADER $SOURCES"
    )

    env.Append(
        BUILDERS=dict(
            ElfToBin=Builder(
                action=" ".join([
                    "$OBJCOPY",
                    "-O",
                    "binary",
                    "$SOURCES",
                    "$TARGET"]),
                suffix=".bin"
            )
        )
    )

    # The source code of "platformio-build-tool" is here
    # https://github.com/platformio/platformio-core/blob/develop/platformio/builder/tools/platformio.py

    #
    # Target: Build executable and linkable firmware
    #
    target_elf = env.BuildProgram()

    #
    # Target: Build the .bin file
    #
    target_bin = env.ElfToBin(join("$BUILD_DIR", "firmware"), target_elf)

    #
    # Target: Upload firmware
    #
    upload = env.Alias(["upload"], target_bin, "$UPLOADCMD")
    AlwaysBuild(upload)

    #
    # Target: Define targets
    #
    Default(target_bin)


.. _platform_creating_installation:

Installation
------------

1. Create ``platforms`` directory in :ref:`projectconf_pio_home_dir` if it
   doesn't exist.
2. Create ``myplatform`` directory in ``platforms``
3. Copy ``platform.json`` and ``builder/main.py`` files to ``myplatform`` directory.
4. Search available platforms via :ref:`cmd_platform_search` command. You
   should see ``myplatform`` platform.
5. Install ``myplatform`` platform via :ref:`cmd_platform_install` command.

Now, you can use ``myplatform`` for the :ref:`projectconf_env_platform`
option in :ref:`projectconf`.

Examples
--------

Please take a look at the source code of
`PlatformIO Development Platforms <https://github.com/platformio?query=platform->`_.
