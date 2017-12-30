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

.. _cmd_run:

platformio run
==============

.. contents::

Usage
-----

.. code-block:: bash

    platformio run [OPTIONS]
    pio run [OPTIONS]


Description
-----------

Process environments which are defined in :ref:`projectconf` file


Options
-------

.. program:: platformio run

.. option::
    -e, --environment

Process specified environments.

You can also specify which environments should be processed by default using
:ref:`projectconf_pio_env_default` option from :ref:`projectconf`.


.. option::
    -t, --target

Process specified targets.

.. note::
    You can configure default targets per project environment using
    :ref:`projectconf_targets` option in :ref:`projectconf`.

Built-in targets:

* Processing

    + ``clean`` delete compiled object files, libraries and firmware/program binaries
    + ``upload`` firmware "auto-uploading" for embedded platforms
    + ``program`` firmware "auto-uploading" for embedded platforms using external
      programmer (available only for :ref:`platform_atmelavr`)
    + ``fuses`` set fuse bits (available only for :ref:`platform_atmelavr`)
    + ``buildfs`` :ref:`platform_espressif_uploadfs`
    + ``uploadfs`` :ref:`platform_espressif_uploadfs`
    + ``size`` print the size of the sections in a firmware/program

* Device

    + ``monitor`` automatically start :ref:`cmd_device_monitor` after success
      build operation. You can configure monitor using
      :ref:`projectconf_section_env_monitor`.

* Service

    + ``envdump`` dump current build environment
    + ``idedata`` export build environment for IDE (defines, build flags, CPPPATH, etc.)

.. option::
    --upload-port

Custom upload port of embedded board. To print all available ports use
:ref:`cmd_device` command.

If upload port is not specified, PlatformIO will try to detect it automatically.

.. option::
    -d, --project-dir

Specify the path to project directory. By default, ``--project-dir`` is equal
to current working directory (``CWD``).

.. option::
    -s, --silent

Suppress progress reporting

.. option::
    -v, --verbose

Shows detailed information when processing environments.

This option can be set globally using :ref:`setting_force_verbose` setting
or by environment variable :envvar:`PLATFORMIO_SETTING_FORCE_VERBOSE`.

.. option::
    --disable-auto-clean

Disable auto-clean of :ref:`projectconf_pio_build_dir` when :ref:`projectconf`
or :ref:`projectconf_pio_src_dir` (project structure) have been modified.

Examples
--------

1. Process `Wiring Blink Example <https://github.com/platformio/platformio-examples/tree/develop/wiring-blink>`_

.. code::

    > platformio run

    [Wed Sep  7 15:48:58 2016] Processing uno (platform: atmelavr, board: uno, framework: arduino)
    -----------------------------------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    Collected 36 compatible libraries
    Looking for dependencies...
    Project does not have dependencies
    Compiling build/uno/src/main.o
    Archiving build/uno/libFrameworkArduinoVariant.a
    Indexing build/uno/libFrameworkArduinoVariant.a
    Compiling build/uno/FrameworkArduino/CDC.o
    ...
    Compiling build/uno/FrameworkArduino/wiring_shift.o
    Archiving build/uno/libFrameworkArduino.a
    Indexing build/uno/libFrameworkArduino.a
    Linking build/uno/firmware.elf
    Building build/uno/firmware.hex
    Calculating size build/uno/firmware.elf
    AVR Memory Usage
    ----------------
    Device: atmega328p

    Program:    1034 bytes (3.2% Full)
    (.text + .data + .bootloader)

    Data:          9 bytes (0.4% Full)
    (.data + .bss + .noinit)


    =========================== [SUCCESS] Took 2.47 seconds ===========================

    [Wed Sep  7 15:49:01 2016] Processing nodemcu (platform: espressif8266, board: nodemcu, framework: arduino)
    -----------------------------------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    Collected 34 compatible libraries
    Looking for dependencies...
    Project does not have dependencies
    Compiling build/nodemcu/src/main.o
    Archiving build/nodemcu/libFrameworkArduinoVariant.a
    Indexing build/nodemcu/libFrameworkArduinoVariant.a
    Compiling build/nodemcu/FrameworkArduino/Esp.o
    Compiling build/nodemcu/FrameworkArduino/FS.o
    Compiling build/nodemcu/FrameworkArduino/HardwareSerial.o
    ...
    Archiving build/nodemcu/libFrameworkArduino.a
    Indexing build/nodemcu/libFrameworkArduino.a
    Linking build/nodemcu/firmware.elf
    Calculating size build/nodemcu/firmware.elf
    text       data     bss     dec     hex filename
    221240      888   29400  251528   3d688 build/nodemcu/firmware.elf
    Building build/nodemcu/firmware.bin
    =========================== [SUCCESS] Took 6.43 seconds ===========================

    [Wed Sep  7 15:49:07 2016] Processing teensy31 (platform: teensy, board: teensy31, framework: arduino)
    -----------------------------------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    Collected 96 compatible libraries
    Looking for dependencies...
    Project does not have dependencies
    Compiling build/teensy31/src/main.o
    Compiling build/teensy31/FrameworkArduino/AudioStream.o
    Compiling build/teensy31/FrameworkArduino/DMAChannel.o
    ...
    Compiling build/teensy31/FrameworkArduino/yield.o
    Archiving build/teensy31/libFrameworkArduino.a
    Indexing build/teensy31/libFrameworkArduino.a
    Linking build/teensy31/firmware.elf
    Calculating size build/teensy31/firmware.elf
    text       data     bss     dec     hex filename
    11288       168    2288   13744    35b0 build/teensy31/firmware.elf
    Building build/teensy31/firmware.hex
    =========================== [SUCCESS] Took 5.36 seconds ===========================

    [Wed Sep  7 15:49:12 2016] Processing lpmsp430g2553 (platform: timsp430, build_flags: -D LED_BUILTIN=RED_LED, board: lpmsp430g2553, framework: energia)
    -----------------------------------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    Collected 29 compatible libraries
    Looking for dependencies...
    Project does not have dependencies
    Compiling build/lpmsp430g2553/src/main.o
    Compiling build/lpmsp430g2553/FrameworkEnergia/HardwareSerial.o
    Compiling build/lpmsp430g2553/FrameworkEnergia/IPAddress.o
    ...
    Compiling build/lpmsp430g2553/FrameworkEnergia/wiring_digital.o
    Compiling build/lpmsp430g2553/FrameworkEnergia/wiring_pulse.o
    Compiling build/lpmsp430g2553/FrameworkEnergia/wiring_shift.o
    Archiving build/lpmsp430g2553/libFrameworkEnergia.a
    Indexing build/lpmsp430g2553/libFrameworkEnergia.a
    Linking build/lpmsp430g2553/firmware.elf
    Calculating size build/lpmsp430g2553/firmware.elf
    text       data     bss     dec     hex filename
    820           0      20     840     348 build/lpmsp430g2553/firmware.elf
    Building build/lpmsp430g2553/firmware.hex
    =========================== [SUCCESS] Took 2.34 seconds ===========================

2. Process specific environment

.. code::

    > platformio run -e nodemcu -e teensy31

    [Wed Sep  7 15:49:01 2016] Processing nodemcu (platform: espressif8266, board: nodemcu, framework: arduino)
    -----------------------------------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    Collected 34 compatible libraries
    Looking for dependencies...
    Project does not have dependencies
    Compiling build/nodemcu/src/main.o
    Archiving build/nodemcu/libFrameworkArduinoVariant.a
    Indexing build/nodemcu/libFrameworkArduinoVariant.a
    Compiling build/nodemcu/FrameworkArduino/Esp.o
    Compiling build/nodemcu/FrameworkArduino/FS.o
    Compiling build/nodemcu/FrameworkArduino/HardwareSerial.o
    ...
    Archiving build/nodemcu/libFrameworkArduino.a
    Indexing build/nodemcu/libFrameworkArduino.a
    Linking build/nodemcu/firmware.elf
    Calculating size build/nodemcu/firmware.elf
    text       data     bss     dec     hex filename
    221240      888   29400  251528   3d688 build/nodemcu/firmware.elf
    Building build/nodemcu/firmware.bin
    =========================== [SUCCESS] Took 6.43 seconds ===========================

    [Wed Sep  7 15:49:07 2016] Processing teensy31 (platform: teensy, board: teensy31, framework: arduino)
    -----------------------------------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    Collected 96 compatible libraries
    Looking for dependencies...
    Project does not have dependencies
    Compiling build/teensy31/src/main.o
    Compiling build/teensy31/FrameworkArduino/AudioStream.o
    Compiling build/teensy31/FrameworkArduino/DMAChannel.o
    ...
    Compiling build/teensy31/FrameworkArduino/yield.o
    Archiving build/teensy31/libFrameworkArduino.a
    Indexing build/teensy31/libFrameworkArduino.a
    Linking build/teensy31/firmware.elf
    Calculating size build/teensy31/firmware.elf
    text       data     bss     dec     hex filename
    11288       168    2288   13744    35b0 build/teensy31/firmware.elf
    Building build/teensy31/firmware.hex
    =========================== [SUCCESS] Took 5.36 seconds ===========================


3. Process specific target (clean project)

.. code:: bash

    > platformio run -t clean
    [Wed Sep  7 15:53:26 2016] Processing uno (platform: atmelavr, board: uno, framework: arduino)
    -----------------------------------------------------------------------------------------------------
    Removed build/uno/firmware.elf
    Removed build/uno/firmware.hex
    Removed build/uno/libFrameworkArduino.a
    Removed build/uno/libFrameworkArduinoVariant.a
    Removed build/uno/FrameworkArduino/_wiring_pulse.o
    Removed build/uno/FrameworkArduino/abi.o
    Removed build/uno/FrameworkArduino/CDC.o
    Removed build/uno/FrameworkArduino/HardwareSerial.o
    Removed build/uno/FrameworkArduino/HardwareSerial0.o
    Removed build/uno/FrameworkArduino/HardwareSerial1.o
    Removed build/uno/FrameworkArduino/HardwareSerial2.o
    Removed build/uno/FrameworkArduino/HardwareSerial3.o
    Removed build/uno/FrameworkArduino/hooks.o
    Removed build/uno/FrameworkArduino/IPAddress.o
    Removed build/uno/FrameworkArduino/main.o
    Removed build/uno/FrameworkArduino/new.o
    Removed build/uno/FrameworkArduino/PluggableUSB.o
    Removed build/uno/FrameworkArduino/Print.o
    Removed build/uno/FrameworkArduino/Stream.o
    Removed build/uno/FrameworkArduino/Tone.o
    Removed build/uno/FrameworkArduino/USBCore.o
    Removed build/uno/FrameworkArduino/WInterrupts.o
    Removed build/uno/FrameworkArduino/wiring.o
    Removed build/uno/FrameworkArduino/wiring_analog.o
    Removed build/uno/FrameworkArduino/wiring_digital.o
    Removed build/uno/FrameworkArduino/wiring_pulse.o
    Removed build/uno/FrameworkArduino/wiring_shift.o
    Removed build/uno/FrameworkArduino/WMath.o
    Removed build/uno/FrameworkArduino/WString.o
    Removed build/uno/src/main.o
    Done cleaning
    ======================= [SUCCESS] Took 0.49 seconds =======================

    [Wed Sep  7 15:53:27 2016] Processing nodemcu (platform: espressif8266, board: nodemcu, framework: arduino)
    -----------------------------------------------------------------------------------------------------
    Removed build/nodemcu/firmware.bin
    Removed build/nodemcu/firmware.elf
    Removed build/nodemcu/libFrameworkArduino.a
    Removed build/nodemcu/libFrameworkArduinoVariant.a
    ...
    Removed build/nodemcu/FrameworkArduino/spiffs/spiffs_nucleus.o
    Removed build/nodemcu/FrameworkArduino/umm_malloc/umm_malloc.o
    Removed build/nodemcu/src/main.o
    Done cleaning
    ======================= [SUCCESS] Took 0.50 seconds =======================

    [Wed Sep  7 15:53:27 2016] Processing teensy31 (platform: teensy, board: teensy31, framework: arduino)
    -----------------------------------------------------------------------------------------------------
    Removed build/teensy31/firmware.elf
    Removed build/teensy31/firmware.hex
    Removed build/teensy31/libFrameworkArduino.a
    Removed build/teensy31/FrameworkArduino/analog.o
    Removed build/teensy31/FrameworkArduino/AudioStream.o
    ...
    Removed build/teensy31/FrameworkArduino/WString.o
    Removed build/teensy31/FrameworkArduino/yield.o
    Removed build/teensy31/src/main.o
    Done cleaning
    ======================= [SUCCESS] Took 0.50 seconds =======================

    [Wed Sep  7 15:53:28 2016] Processing lpmsp430g2553 (platform: timsp430, build_flags: -D LED_BUILTIN=RED_LED, board: lpmsp430g2553, framework: energia)
    -----------------------------------------------------------------------------------------------------
    Removed build/lpmsp430g2553/firmware.elf
    Removed build/lpmsp430g2553/firmware.hex
    Removed build/lpmsp430g2553/libFrameworkEnergia.a
    Removed build/lpmsp430g2553/FrameworkEnergia/atof.o
    ...
    Removed build/lpmsp430g2553/FrameworkEnergia/avr/dtostrf.o
    Removed build/lpmsp430g2553/src/main.o
    Done cleaning
    ======================= [SUCCESS] Took 0.49 seconds =======================


4. Mix environments and targets

.. code::

    > platformio run -e uno -t upload

    [Wed Sep  7 15:55:11 2016] Processing uno (platform: atmelavr, board: uno, framework: arduino)
    --------------------------------------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    Collected 36 compatible libraries
    Looking for dependencies...
    Project does not have dependencies
    Compiling build/uno/src/main.o
    Archiving build/uno/libFrameworkArduinoVariant.a
    Indexing build/uno/libFrameworkArduinoVariant.a
    Compiling build/uno/FrameworkArduino/CDC.o
    ...
    Compiling build/uno/FrameworkArduino/wiring_shift.o
    Archiving build/uno/libFrameworkArduino.a
    Indexing build/uno/libFrameworkArduino.a
    Linking build/uno/firmware.elf
    Checking program size build/uno/firmware.elf
    text       data     bss     dec     hex filename
    1034          0       9    1043     413 build/uno/firmware.elf
    Building build/uno/firmware.hex
    Looking for upload port...
    Auto-detected: /dev/cu.usbmodemFA141
    Uploading build/uno/firmware.hex

    avrdude: AVR device initialized and ready to accept instructions

    Reading | ################################################## | 100% 0.01s

    avrdude: Device signature = 0x1e950f
    avrdude: reading input file "build/uno/firmware.hex"
    avrdude: writing flash (1034 bytes):

    Writing | ################################################## | 100% 0.18s

    avrdude: 1034 bytes of flash written
    avrdude: verifying flash memory against build/uno/firmware.hex:
    avrdude: load data flash data from input file build/uno/firmware.hex:
    avrdude: input file build/uno/firmware.hex contains 1034 bytes
    avrdude: reading on-chip flash data:

    Reading | ################################################## | 100% 0.15s

    avrdude: verifying ...
    avrdude: 1034 bytes of flash verified

    avrdude: safemode: Fuses OK (H:00, E:00, L:00)

    avrdude done.  Thank you.

    ======================== [SUCCESS] Took 4.14 seconds ========================
