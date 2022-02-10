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

pio run
=======

.. contents::

Usage
-----

.. code-block:: bash

    pio run [OPTIONS]


Description
-----------

Run project targets over environments declared in :ref:`projectconf`.

Options
-------

.. program:: pio run

.. option::
    -e, --environment

Process specified environments. Multiple environments are allowed.

You can also specify which environments should be processed by default using
:ref:`projectconf_pio_default_envs` option from :ref:`projectconf`.

.. option::
    -t, --target

Process specified targets. Multiple targets are allowed.

You can configure default targets per project environment using
:ref:`projectconf_targets` option in :ref:`projectconf`.

.. option::
    --list-targets

.. versionadded:: 5.0

List available project targets. It's also possible to list targets per project
environment using :option:`pio run --environment` option.

There are also built-in system targets:

* Device

    + ``monitor`` automatically start :ref:`cmd_device_monitor` after successful
      build operation. You can configure monitor using
      :ref:`projectconf_section_env_monitor`.

* System

    + ``envdump`` dump current build environment

.. option::
    --upload-port

Custom upload port of embedded board. To print all available ports use
:ref:`cmd_device_list` command.

If upload port is not specified, PlatformIO will try to detect it automatically.

.. option::
    -d, --project-dir

Specify the path to project directory. By default, ``--project-dir`` is equal
to current working directory (``CWD``).

.. option::
    -c, --project-conf

Process project with a custom :ref:`projectconf`.

.. option::
    -j, --jobs

Control a number of parallel build jobs. Default is a number of CPUs in a system.

.. option::
    -s, --silent

Suppress progress reporting

.. option::
    -v, --verbose

Shows detailed information when processing environments.

This option can also be set globally using :ref:`setting_force_verbose` setting
or by environment variable :envvar:`PLATFORMIO_SETTING_FORCE_VERBOSE`.

.. option::
    --disable-auto-clean

Disable auto-clean of :ref:`projectconf_pio_build_dir` when :ref:`projectconf`
or :ref:`projectconf_pio_src_dir` (project structure) have been modified.

Examples
--------

1. Process `Wiring Blink Example <https://github.com/platformio/platformio-examples/tree/develop/wiring-blink>`_

.. code::

    > pio run

    [Wed Sep  7 15:48:58 2016] Processing uno (platform: atmelavr, board: uno, framework: arduino)
    -----------------------------------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    Collected 36 compatible libraries
    Looking for dependencies...
    Project does not have dependencies
    Compiling .pio/build/uno/src/main.o
    Archiving .pio/build/uno/libFrameworkArduinoVariant.a
    Indexing .pio/build/uno/libFrameworkArduinoVariant.a
    Compiling .pio/build/uno/FrameworkArduino/CDC.o
    ...
    Compiling .pio/build/uno/FrameworkArduino/wiring_shift.o
    Archiving .pio/build/uno/libFrameworkArduino.a
    Indexing .pio/build/uno/libFrameworkArduino.a
    Linking .pio/build/uno/firmware.elf
    Building .pio/build/uno/firmware.hex
    Calculating size .pio/build/uno/firmware.elf
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
    Compiling .pio/build/nodemcu/src/main.o
    Archiving .pio/build/nodemcu/libFrameworkArduinoVariant.a
    Indexing .pio/build/nodemcu/libFrameworkArduinoVariant.a
    Compiling .pio/build/nodemcu/FrameworkArduino/Esp.o
    Compiling .pio/build/nodemcu/FrameworkArduino/FS.o
    Compiling .pio/build/nodemcu/FrameworkArduino/HardwareSerial.o
    ...
    Archiving .pio/build/nodemcu/libFrameworkArduino.a
    Indexing .pio/build/nodemcu/libFrameworkArduino.a
    Linking .pio/build/nodemcu/firmware.elf
    Calculating size .pio/build/nodemcu/firmware.elf
    text       data     bss     dec     hex filename
    221240      888   29400  251528   3d688 .pio/build/nodemcu/firmware.elf
    Building .pio/build/nodemcu/firmware.bin
    =========================== [SUCCESS] Took 6.43 seconds ===========================

    [Wed Sep  7 15:49:07 2016] Processing teensy31 (platform: teensy, board: teensy31, framework: arduino)
    -----------------------------------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    Collected 96 compatible libraries
    Looking for dependencies...
    Project does not have dependencies
    Compiling .pio/build/teensy31/src/main.o
    Compiling .pio/build/teensy31/FrameworkArduino/AudioStream.o
    Compiling .pio/build/teensy31/FrameworkArduino/DMAChannel.o
    ...
    Compiling .pio/build/teensy31/FrameworkArduino/yield.o
    Archiving .pio/build/teensy31/libFrameworkArduino.a
    Indexing .pio/build/teensy31/libFrameworkArduino.a
    Linking .pio/build/teensy31/firmware.elf
    Calculating size .pio/build/teensy31/firmware.elf
    text       data     bss     dec     hex filename
    11288       168    2288   13744    35b0 .pio/build/teensy31/firmware.elf
    Building .pio/build/teensy31/firmware.hex
    =========================== [SUCCESS] Took 5.36 seconds ===========================

    [Wed Sep  7 15:49:12 2016] Processing lpmsp430g2553 (platform: timsp430, build_flags: -D LED_BUILTIN=RED_LED, board: lpmsp430g2553, framework: arduino)
    -----------------------------------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    Collected 29 compatible libraries
    Looking for dependencies...
    Project does not have dependencies
    Compiling .pio/build/lpmsp430g2553/src/main.o
    Compiling .pio/build/lpmsp430g2553/FrameworkAnergia/HardwareSerial.o
    Compiling .pio/build/lpmsp430g2553/FrameworkAnergia/IPAddress.o
    ...
    Compiling .pio/build/lpmsp430g2553/FrameworkAnergia/wiring_digital.o
    Compiling .pio/build/lpmsp430g2553/FrameworkAnergia/wiring_pulse.o
    Compiling .pio/build/lpmsp430g2553/FrameworkAnergia/wiring_shift.o
    Archiving .pio/build/lpmsp430g2553/libFrameworkAnergia.a
    Indexing .pio/build/lpmsp430g2553/libFrameworkAnergia.a
    Linking .pio/build/lpmsp430g2553/firmware.elf
    Calculating size .pio/build/lpmsp430g2553/firmware.elf
    text       data     bss     dec     hex filename
    820           0      20     840     348 .pio/build/lpmsp430g2553/firmware.elf
    Building .pio/build/lpmsp430g2553/firmware.hex
    =========================== [SUCCESS] Took 2.34 seconds ===========================

2. Process specific environment

.. code::

    > pio run -e nodemcu -e teensy31

    [Wed Sep  7 15:49:01 2016] Processing nodemcu (platform: espressif8266, board: nodemcu, framework: arduino)
    -----------------------------------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    Collected 34 compatible libraries
    Looking for dependencies...
    Project does not have dependencies
    Compiling .pio/build/nodemcu/src/main.o
    Archiving .pio/build/nodemcu/libFrameworkArduinoVariant.a
    Indexing .pio/build/nodemcu/libFrameworkArduinoVariant.a
    Compiling .pio/build/nodemcu/FrameworkArduino/Esp.o
    Compiling .pio/build/nodemcu/FrameworkArduino/FS.o
    Compiling .pio/build/nodemcu/FrameworkArduino/HardwareSerial.o
    ...
    Archiving .pio/build/nodemcu/libFrameworkArduino.a
    Indexing .pio/build/nodemcu/libFrameworkArduino.a
    Linking .pio/build/nodemcu/firmware.elf
    Calculating size .pio/build/nodemcu/firmware.elf
    text       data     bss     dec     hex filename
    221240      888   29400  251528   3d688 .pio/build/nodemcu/firmware.elf
    Building .pio/build/nodemcu/firmware.bin
    =========================== [SUCCESS] Took 6.43 seconds ===========================

    [Wed Sep  7 15:49:07 2016] Processing teensy31 (platform: teensy, board: teensy31, framework: arduino)
    -----------------------------------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    Collected 96 compatible libraries
    Looking for dependencies...
    Project does not have dependencies
    Compiling .pio/build/teensy31/src/main.o
    Compiling .pio/build/teensy31/FrameworkArduino/AudioStream.o
    Compiling .pio/build/teensy31/FrameworkArduino/DMAChannel.o
    ...
    Compiling .pio/build/teensy31/FrameworkArduino/yield.o
    Archiving .pio/build/teensy31/libFrameworkArduino.a
    Indexing .pio/build/teensy31/libFrameworkArduino.a
    Linking .pio/build/teensy31/firmware.elf
    Calculating size .pio/build/teensy31/firmware.elf
    text       data     bss     dec     hex filename
    11288       168    2288   13744    35b0 .pio/build/teensy31/firmware.elf
    Building .pio/build/teensy31/firmware.hex
    =========================== [SUCCESS] Took 5.36 seconds ===========================


3. Process specific target (clean project)

.. code:: bash

    > pio run -t clean
    [Wed Sep  7 15:53:26 2016] Processing uno (platform: atmelavr, board: uno, framework: arduino)
    -----------------------------------------------------------------------------------------------------
    Removed .pio/build/uno/firmware.elf
    Removed .pio/build/uno/firmware.hex
    Removed .pio/build/uno/libFrameworkArduino.a
    Removed .pio/build/uno/libFrameworkArduinoVariant.a
    Removed .pio/build/uno/FrameworkArduino/_wiring_pulse.o
    Removed .pio/build/uno/FrameworkArduino/abi.o
    Removed .pio/build/uno/FrameworkArduino/CDC.o
    Removed .pio/build/uno/FrameworkArduino/HardwareSerial.o
    Removed .pio/build/uno/FrameworkArduino/HardwareSerial0.o
    Removed .pio/build/uno/FrameworkArduino/HardwareSerial1.o
    Removed .pio/build/uno/FrameworkArduino/HardwareSerial2.o
    Removed .pio/build/uno/FrameworkArduino/HardwareSerial3.o
    Removed .pio/build/uno/FrameworkArduino/hooks.o
    Removed .pio/build/uno/FrameworkArduino/IPAddress.o
    Removed .pio/build/uno/FrameworkArduino/main.o
    Removed .pio/build/uno/FrameworkArduino/new.o
    Removed .pio/build/uno/FrameworkArduino/PluggableUSB.o
    Removed .pio/build/uno/FrameworkArduino/Print.o
    Removed .pio/build/uno/FrameworkArduino/Stream.o
    Removed .pio/build/uno/FrameworkArduino/Tone.o
    Removed .pio/build/uno/FrameworkArduino/USBCore.o
    Removed .pio/build/uno/FrameworkArduino/WInterrupts.o
    Removed .pio/build/uno/FrameworkArduino/wiring.o
    Removed .pio/build/uno/FrameworkArduino/wiring_analog.o
    Removed .pio/build/uno/FrameworkArduino/wiring_digital.o
    Removed .pio/build/uno/FrameworkArduino/wiring_pulse.o
    Removed .pio/build/uno/FrameworkArduino/wiring_shift.o
    Removed .pio/build/uno/FrameworkArduino/WMath.o
    Removed .pio/build/uno/FrameworkArduino/WString.o
    Removed .pio/build/uno/src/main.o
    Done cleaning
    ======================= [SUCCESS] Took 0.49 seconds =======================

    [Wed Sep  7 15:53:27 2016] Processing nodemcu (platform: espressif8266, board: nodemcu, framework: arduino)
    -----------------------------------------------------------------------------------------------------
    Removed .pio/build/nodemcu/firmware.bin
    Removed .pio/build/nodemcu/firmware.elf
    Removed .pio/build/nodemcu/libFrameworkArduino.a
    Removed .pio/build/nodemcu/libFrameworkArduinoVariant.a
    ...
    Removed .pio/build/nodemcu/FrameworkArduino/spiffs/spiffs_nucleus.o
    Removed .pio/build/nodemcu/FrameworkArduino/umm_malloc/umm_malloc.o
    Removed .pio/build/nodemcu/src/main.o
    Done cleaning
    ======================= [SUCCESS] Took 0.50 seconds =======================

    [Wed Sep  7 15:53:27 2016] Processing teensy31 (platform: teensy, board: teensy31, framework: arduino)
    -----------------------------------------------------------------------------------------------------
    Removed .pio/build/teensy31/firmware.elf
    Removed .pio/build/teensy31/firmware.hex
    Removed .pio/build/teensy31/libFrameworkArduino.a
    Removed .pio/build/teensy31/FrameworkArduino/analog.o
    Removed .pio/build/teensy31/FrameworkArduino/AudioStream.o
    ...
    Removed .pio/build/teensy31/FrameworkArduino/WString.o
    Removed .pio/build/teensy31/FrameworkArduino/yield.o
    Removed .pio/build/teensy31/src/main.o
    Done cleaning
    ======================= [SUCCESS] Took 0.50 seconds =======================

    [Wed Sep  7 15:53:28 2016] Processing lpmsp430g2553 (platform: timsp430, build_flags: -D LED_BUILTIN=RED_LED, board: lpmsp430g2553, framework: energia)
    -----------------------------------------------------------------------------------------------------
    Removed .pio/build/lpmsp430g2553/firmware.elf
    Removed .pio/build/lpmsp430g2553/firmware.hex
    Removed .pio/build/lpmsp430g2553/libFrameworkAnergia.a
    Removed .pio/build/lpmsp430g2553/FrameworkAnergia/atof.o
    ...
    Removed .pio/build/lpmsp430g2553/FrameworkAnergia/avr/dtostrf.o
    Removed .pio/build/lpmsp430g2553/src/main.o
    Done cleaning
    ======================= [SUCCESS] Took 0.49 seconds =======================


4. Mix environments and targets

.. code::

    > pio run -e uno -t upload

    [Wed Sep  7 15:55:11 2016] Processing uno (platform: atmelavr, board: uno, framework: arduino)
    --------------------------------------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    Collected 36 compatible libraries
    Looking for dependencies...
    Project does not have dependencies
    Compiling .pio/build/uno/src/main.o
    Archiving .pio/build/uno/libFrameworkArduinoVariant.a
    Indexing .pio/build/uno/libFrameworkArduinoVariant.a
    Compiling .pio/build/uno/FrameworkArduino/CDC.o
    ...
    Compiling .pio/build/uno/FrameworkArduino/wiring_shift.o
    Archiving .pio/build/uno/libFrameworkArduino.a
    Indexing .pio/build/uno/libFrameworkArduino.a
    Linking .pio/build/uno/firmware.elf
    Checking program size .pio/build/uno/firmware.elf
    text       data     bss     dec     hex filename
    1034          0       9    1043     413 .pio/build/uno/firmware.elf
    Building .pio/build/uno/firmware.hex
    Looking for upload port...
    Auto-detected: /dev/cu.usbmodemFA141
    Uploading .pio/build/uno/firmware.hex

    avrdude: AVR device initialized and ready to accept instructions

    Reading | ################################################## | 100% 0.01s

    avrdude: Device signature = 0x1e950f
    avrdude: reading input file ".pio/build/uno/firmware.hex"
    avrdude: writing flash (1034 bytes):

    Writing | ################################################## | 100% 0.18s

    avrdude: 1034 bytes of flash written
    avrdude: verifying flash memory against .pio/build/uno/firmware.hex:
    avrdude: load data flash data from input file .pio/build/uno/firmware.hex:
    avrdude: input file .pio/build/uno/firmware.hex contains 1034 bytes
    avrdude: reading on-chip flash data:

    Reading | ################################################## | 100% 0.15s

    avrdude: verifying ...
    avrdude: 1034 bytes of flash verified

    avrdude: safemode: Fuses OK (H:00, E:00, L:00)

    avrdude done.  Thank you.

    ======================== [SUCCESS] Took 4.14 seconds ========================
