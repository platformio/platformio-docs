---
sidebar_label: "Unit testing \"Blink\""
description: Write and run unit tests on an Arduino Uno with PlatformIO and the Unity test framework.
---

# Unit testing a "Blink" project

In this tutorial you add a unit test to the "Blink" project and run it on an
Arduino Uno. The test checks the LED pin number and that the pin follows the
values you write to it.

- **Level:** beginner
- **Host:** Windows, macOS or Linux
- **Hardware:** Arduino Uno (or another Arduino board; adjust the
  [project environment](../../reference/platformio-ini/env/index.md))

For an introduction to testing in PlatformIO, see
[Unit testing](../../guides/unit-testing/index.md).

## Before you begin {#setting-up-the-project}

Create the "Blink" project from the [Quick start](../quick-start.md). You only
need the `uno` environment in `platformio.ini`:

```ini
[env:uno]
platform = atmelavr
framework = arduino
board = uno
```

## Add the test {#source-files}

1. In the project's `test` folder, create a folder named `test_blink`. Test
   folder names must start with `test_`; PlatformIO ignores other folders.
2. Create `test/test_blink/test_main.cpp` with the following content:

   ```cpp
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
   ```

   The test uses the [Unity](../../guides/unit-testing/frameworks/unity.md)
   framework: `UNITY_BEGIN()` starts the test run, `RUN_TEST()` runs one test
   function, and `UNITY_END()` reports the results.

The project now looks like this:

```text
project_dir
├── platformio.ini
├── src
│   └── main.cpp
└── test
    └── test_blink
        └── test_main.cpp
```

## Run the test {#test-results}

Connect the board and run [`pio test`](../../reference/cli/pio-test.md):

```bash
pio test
```

PlatformIO builds the test, uploads it to the board, and reads the results
over the serial port:

```text
Verbose mode can be enabled via `-v, --verbose` option
Collected 1 tests

Processing test_blink in uno environment
----------------------------------------
Building...
Uploading...
Testing...
If you don't see any output for the first 10 secs, please reset board (press reset button)

test/test_blink/test_main.cpp:34: test_led_builtin_pin_number [PASSED]
test/test_blink/test_main.cpp:43: test_led_state_high [PASSED]
test/test_blink/test_main.cpp:45: test_led_state_low  [PASSED]
test/test_blink/test_main.cpp:43: test_led_state_high [PASSED]
test/test_blink/test_main.cpp:45: test_led_state_low  [PASSED]
test/test_blink/test_main.cpp:43: test_led_state_high [PASSED]
test/test_blink/test_main.cpp:45: test_led_state_low  [PASSED]
test/test_blink/test_main.cpp:43: test_led_state_high [PASSED]
test/test_blink/test_main.cpp:45: test_led_state_low  [PASSED]
test/test_blink/test_main.cpp:43: test_led_state_high [PASSED]
test/test_blink/test_main.cpp:45: test_led_state_low  [PASSED]
----------------- uno:test_blink [PASSED] Took 16.51 seconds -----------------

Environment    Test        Status    Duration
-------------  ----------  --------  ------------
uno            test_blink  PASSED    00:00:16.514

=================== 11 test cases: 11 succeeded in 00:00:16.514 ===================
```

## Next steps {#next-steps}

- Run tests on your computer instead of the board: see
  [Test runner](../../guides/unit-testing/runner.md) and the
  [`native` platform](/hardware/platforms/native).
- Learn how to organize tests:
  [Project structure](../../guides/unit-testing/structure/index.md).
