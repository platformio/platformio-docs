<a id="tutorial-unit-testing-blink"></a>

# Unit Testing of a "Blink" Project {#unit-testing-of-a-blink-project}

The goal of this tutorial is to demonstrate how simple it is to use [Unit Testing](../../guides/unit-testing/index.md).

- **Level:** Beginner
- **Platforms:** Windows, macOS, Linux

## Setting Up the Project {#setting-up-the-project}

1. Please navigate to the [Quick Start](../quick-start.md) section and create the "Blink Project".
2. Create the root `test` directory in the project (on the same level as `src`)
3. Create a test `test_blink` directory (name must be prefixed with `test_`) and place a `test_main.cpp` file in it (the source code is located below).
4. Run tests using the [pio test](../../reference/cli/pio-test.md) command.

## Project structure {#project-structure}

```bash
project_dir
├── platformio.ini
└── test
    └── test_blink
        └── test_main.cpp
```

## Source files {#source-files}

- ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md)

  ```ini
  [env:uno]
  platform = atmelavr
  framework = arduino
  board = uno
  ```

- `test/test_blink/test_main.cpp`

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

## Test results {#test-results}

```text
> pio test

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
