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
2. Create the root ``test`` directory in the project (on the same level as ``src``)
3. Create a test ``test_blink`` directory (name must be prefixed with ``test_``)
   and place a ``test_main.cpp`` file in it (the source code is located below).
4. Run tests using the :ref:`cmd_test` command.

Project structure
-----------------

.. code-block:: bash

    project_dir
    ├── platformio.ini
    └── test
        └── test_blink
            └── test_main.cpp

Source files
------------

* :ref:`projectconf`

  .. code-block:: ini

    [env:uno]
    platform = atmelavr
    framework = arduino
    board = uno

* ``test/test_blink/test_main.cpp``

  .. code-block:: cpp

    #include <Arduino.h>
    #include <unity.h>

    void setUp(void)
    {
      // set stuff up here
    }

    void tearDown(void)
    {
      // clean stuff up here
    }

    void test_led_builtin_pin_number(void)
    {
      TEST_ASSERT_EQUAL(13, LED_BUILTIN);
    }

    void test_led_state_high(void)
    {
      digitalWrite(LED_BUILTIN, HIGH);
      TEST_ASSERT_EQUAL(HIGH, digitalRead(LED_BUILTIN));
    }

    void test_led_state_low(void)
    {
      digitalWrite(LED_BUILTIN, LOW);
      TEST_ASSERT_EQUAL(LOW, digitalRead(LED_BUILTIN));
    }

    void setup()
    {
      // NOTE!!! Wait for >2 secs
      // if board doesn't support software reset via Serial.DTR/RTS
      delay(2000);

      pinMode(LED_BUILTIN, OUTPUT);

      UNITY_BEGIN(); // IMPORTANT LINE!
      RUN_TEST(test_led_builtin_pin_number);
    }

    uint8_t i = 0;
    uint8_t max_blinks = 5;

    void loop()
    {
      if (i < max_blinks)
      {
        RUN_TEST(test_led_state_high);
        delay(500);
        RUN_TEST(test_led_state_low);
        delay(500);
        i++;
      }
      else if (i == max_blinks)
      {
        UNITY_END(); // stop unit testing
      }
    }

Test results
------------

.. code::

  > pio test

  Verbose mode can be enabled via `-v, --verbose` option
  Collected 1 tests

  Processing test_blink in uno environment
  ----------------------------------------
  Building...
  Uploading...
  Testing...
  If you don't see any output for the first 10 secs, please reset board (press reset button)

  test/test_blink/test_main.cpp:34: test_led_builtin_pin_number	[PASSED]
  test/test_blink/test_main.cpp:43: test_led_state_high	[PASSED]
  test/test_blink/test_main.cpp:45: test_led_state_low	[PASSED]
  test/test_blink/test_main.cpp:43: test_led_state_high	[PASSED]
  test/test_blink/test_main.cpp:45: test_led_state_low	[PASSED]
  test/test_blink/test_main.cpp:43: test_led_state_high	[PASSED]
  test/test_blink/test_main.cpp:45: test_led_state_low	[PASSED]
  test/test_blink/test_main.cpp:43: test_led_state_high	[PASSED]
  test/test_blink/test_main.cpp:45: test_led_state_low	[PASSED]
  test/test_blink/test_main.cpp:43: test_led_state_high	[PASSED]
  test/test_blink/test_main.cpp:45: test_led_state_low	[PASSED]
  ----------------- uno:test_blink [PASSED] Took 16.51 seconds -----------------

  Environment    Test        Status    Duration
  -------------  ----------  --------  ------------
  uno            test_blink  PASSED    00:00:16.514

  =================== 11 test cases: 11 succeeded in 00:00:16.514 ===================