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

.. _tutorial_unit_testing_blink:

Unit Testing of a "Blink" Project
=================================

The goal of this tutorial is to demonstrate how simple it is to use :ref:`unit_testing`.

* **Level:** Beginner
* **Platforms:** Windows, macOS, Linux

.. contents:: Contents
    :local:

Setting Up the Project
----------------------

1. Please navigate to the :ref:`core_quickstart` section and create the "Blink Project".
2. Create a ``test`` directory in the project (on the same level as ``src``)
   and place a ``test_main.cpp`` file in it (the source code is located below).
3. Run tests using the :ref:`cmd_test` command.

Project structure
-----------------

.. code-block:: bash

    project_dir
    ├── lib
    │   └── README
    ├── platformio.ini
    ├── src
    │   └── ...
    └── test
        └── test_main.cpp

Source files
------------

* ``platformio.ini``

  .. code-block:: ini

      ; PlatformIO Project Configuration File
      ;
      ;   Build options: build flags, source filter, extra scripting
      ;   Upload options: custom port, speed and extra flags
      ;   Library options: dependencies, extra library storages
      ;
      ; Please visit documentation for the other options and examples
      ; https://docs.platformio.org/page/projectconf.html


      [env:uno]
      platform = atmelavr
      framework = arduino
      board = uno

      [env:teensy31]
      platform = teensy
      framework = arduino
      board = teensy31

* ``test/test_main.cpp``

  .. code-block:: cpp

      #include <Arduino.h>
      #include <unity.h>

      // void setUp(void) {
      // // set stuff up here
      // }

      // void tearDown(void) {
      // // clean stuff up here
      // }

      void test_led_builtin_pin_number(void) {
          TEST_ASSERT_EQUAL(13, LED_BUILTIN);
      }

      void test_led_state_high(void) {
          digitalWrite(LED_BUILTIN, HIGH);
          TEST_ASSERT_EQUAL(HIGH, digitalRead(LED_BUILTIN));
      }

      void test_led_state_low(void) {
          digitalWrite(LED_BUILTIN, LOW);
          TEST_ASSERT_EQUAL(LOW, digitalRead(LED_BUILTIN));
      }

      void setup() {
          // NOTE!!! Wait for >2 secs
          // if board doesn't support software reset via Serial.DTR/RTS
          delay(2000);

          UNITY_BEGIN();    // IMPORTANT LINE!
          RUN_TEST(test_led_builtin_pin_number);

          pinMode(LED_BUILTIN, OUTPUT);
      }

      uint8_t i = 0;
      uint8_t max_blinks = 5;

      void loop() {
          if (i < max_blinks)
          {
              RUN_TEST(test_led_state_high);
              delay(500);
              RUN_TEST(test_led_state_low);
              delay(500);
              i++;
          }
          else if (i == max_blinks) {
            UNITY_END(); // stop unit testing
          }
      }


Test results
------------

.. code::

    > pio test -e uno --verbose

    Verbose mode can be enabled via `-v, --verbose` option
    Collected 1 items

    ===================== [test/*] Building... (1/3) =======================
    Processing uno (platform: atmelavr; board: uno; framework: arduino)
    -------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    PLATFORM: Atmel AVR > Arduino Uno
    SYSTEM: ATMEGA328P 16MHz 2KB RAM (31.50KB Flash)
    Library Dependency Finder -> http://bit.ly/configure-pio-ldf
    LDF MODES: FINDER(chain) COMPATIBILITY(soft)
    Collected 24 compatible libraries
    Scanning dependencies...
    No dependencies
    Compiling .pio\build\uno\test\output_export.cpp.o
    Compiling .pio\build\uno\test\test_main.cpp.o
    Archiving .pio\build\uno\libFrameworkArduinoVariant.a
    Compiling .pio\build\uno\FrameworkArduino\CDC.cpp.o
    Indexing .pio\build\uno\libFrameworkArduinoVariant.a
    Compiling .pio\build\uno\FrameworkArduino\HardwareSerial.cpp.o
    Compiling .pio\build\uno\FrameworkArduino\HardwareSerial0.cpp.o
    Compiling .pio\build\uno\FrameworkArduino\HardwareSerial1.cpp.o
    Compiling .pio\build\uno\FrameworkArduino\HardwareSerial2.cpp.o
    Compiling .pio\build\uno\FrameworkArduino\HardwareSerial3.cpp.o
    Compiling .pio\build\uno\FrameworkArduino\IPAddress.cpp.o
    Compiling .pio\build\uno\FrameworkArduino\PluggableUSB.cpp.o
    Compiling .pio\build\uno\FrameworkArduino\Print.cpp.o
    Compiling .pio\build\uno\FrameworkArduino\Stream.cpp.o
    Compiling .pio\build\uno\FrameworkArduino\Tone.cpp.o
    Compiling .pio\build\uno\FrameworkArduino\USBCore.cpp.o
    Compiling .pio\build\uno\FrameworkArduino\WInterrupts.c.o
    Compiling .pio\build\uno\FrameworkArduino\WMath.cpp.o
    Compiling .pio\build\uno\FrameworkArduino\WString.cpp.o
    Compiling .pio\build\uno\FrameworkArduino\abi.cpp.o
    Compiling .pio\build\uno\FrameworkArduino\hooks.c.o
    Compiling .pio\build\uno\FrameworkArduino\main.cpp.o
    Compiling .pio\build\uno\FrameworkArduino\new.cpp.o
    Compiling .pio\build\uno\FrameworkArduino\wiring.c.o
    Compiling .pio\build\uno\FrameworkArduino\wiring_analog.c.o
    Compiling .pio\build\uno\FrameworkArduino\wiring_digital.c.o
    Compiling .pio\build\uno\FrameworkArduino\wiring_pulse.S.o
    Compiling .pio\build\uno\FrameworkArduino\wiring_pulse.c.o
    Compiling .pio\build\uno\FrameworkArduino\wiring_shift.c.o
    Compiling .pio\build\uno\UnityTestLib\unity.o
    Archiving .pio\build\uno\libFrameworkArduino.a
    Indexing .pio\build\uno\libFrameworkArduino.a
    Archiving .pio\build\uno\libUnityTestLib.a
    Indexing .pio\build\uno\libUnityTestLib.a
    Linking .pio\build\uno\firmware.elf
    Checking size .pio\build\uno\firmware.elf
    Building .pio\build\uno\firmware.hex
    Memory Usage -> http://bit.ly/pio-memory-usage
    DATA:    [==        ]  20.0% (used 410 bytes from 2048 bytes)
    PROGRAM: [=         ]  12.6% (used 4060 bytes from 32256 bytes)

    ========================================== [SUMMARY] ==========================================
    Environment uno                 [SUCCESS]
    Environment teensy31            [SKIP]
    ================================= [SUCCESS] Took 2.54 seconds =================================

    ================================= [test/*] Uploading... (2/3) =================================
    Processing uno (platform: atmelavr; board: uno; framework: arduino)
    -------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    PLATFORM: Atmel AVR > Arduino Uno
    SYSTEM: ATMEGA328P 16MHz 2KB RAM (31.50KB Flash)
    Library Dependency Finder -> http://bit.ly/configure-pio-ldf
    LDF MODES: FINDER(chain) COMPATIBILITY(soft)
    Collected 24 compatible libraries
    Scanning dependencies...
    No dependencies
    Checking size .pio\build\uno\firmware.elf
    Memory Usage -> http://bit.ly/pio-memory-usage
    DATA:    [==        ]  20.0% (used 410 bytes from 2048 bytes)
    PROGRAM: [=         ]  12.6% (used 4060 bytes from 32256 bytes)
    Configuring upload protocol...
    AVAILABLE: arduino
    CURRENT: upload_protocol = arduino
    Looking for upload port...
    Auto-detected: COM18
    Uploading .pio\build\uno\firmware.hex

    avrdude: AVR device initialized and ready to accept instructions

    Reading | ################################################## | 100% 0.00s

    avrdude: Device signature = 0x1e950f (probably m328p)
    avrdude: reading input file ".pio\build\uno\firmware.hex"
    avrdude: writing flash (4060 bytes):

    Writing | ################################################## | 100% 0.76s

    avrdude: 4060 bytes of flash written
    avrdude: verifying flash memory against .pio\build\uno\firmware.hex:
    avrdude: load data flash data from input file .pio\build\uno\firmware.hex:
    avrdude: input file .pio\build\uno\firmware.hex contains 4060 bytes
    avrdude: reading on-chip flash data:

    Reading | ################################################## | 100% 0.48s

    avrdude: verifying ...
    avrdude: 4060 bytes of flash verified

    avrdude: safemode: Fuses OK (E:00, H:00, L:00)

    avrdude done.  Thank you.


    =============================== [SUMMARY] ================================
    Environment uno                 [SUCCESS]
    Environment teensy31            [SKIP]
     ====================== [SUCCESS] Took 4.45 seconds ======================

    ================================== [test/*] Testing... (3/3) ==================================
    If you don't see any output for the first 10 secs, please reset board (press reset button)

    test\test_main.cpp:30:test_led_builtin_pin_number       [PASSED]
    test\test_main.cpp:41:test_led_state_high       [PASSED]
    test\test_main.cpp:43:test_led_state_low        [PASSED]
    test\test_main.cpp:41:test_led_state_high       [PASSED]
    test\test_main.cpp:43:test_led_state_low        [PASSED]
    test\test_main.cpp:41:test_led_state_high       [PASSED]
    test\test_main.cpp:43:test_led_state_low        [PASSED]
    test\test_main.cpp:41:test_led_state_high       [PASSED]
    test\test_main.cpp:43:test_led_state_low        [PASSED]
    test\test_main.cpp:41:test_led_state_high       [PASSED]
    test\test_main.cpp:43:test_led_state_low        [PASSED]
    -----------------------
    11 Tests 0 Failures 0 Ignored

    ============================ [TEST SUMMARY] ==============================
    test/*/env:uno  [PASSED]
    test/*/env:teensy31     [IGNORED]
    ==================== [PASSED] Took 12.99 seconds =========================
