---
description: "If you would like to change the default PlatformIO's Test Runner for the GoogleTest, please implement your Custom Testing Framework runner extending GooglestTestRunner class."
---

# GoogleTest

<dl>

<dt>

Registry

</dt>

<dd>

[https://registry.platformio.org/libraries/google/googletest](https://registry.platformio.org/libraries/google/googletest)

</dd>

<dt>

Configuration

</dt>

<dd>

[test_framework](../../../reference/platformio-ini/env/test-framework.md) = `googletest`

</dd>

<dt>

Native Tests

</dt>

<dd>

Yes

</dd>

<dt>

Embedded Tests

</dt>

<dd>

Yes\* (only for [Espressif 8266](/hardware/platforms/espressif8266) and [Espressif 32](/hardware/platforms/espressif32))

</dd>

<dt>

Mocking Support

</dt>

<dd>

Yes

</dd>

</dl>

**GoogleTest** is a testing framework developed by the Testing Technology team with Google's specific requirements and constraints in mind. Whether you work on Linux, Windows, or a Mac, if you write C++ code, GoogleTest can help you.

## Getting started {#getting-started}

To get started with the GoogleTest all you need is to set the [test_framework](../../../reference/platformio-ini/env/test-framework.md) option in your [`platformio.ini`](../../../reference/platformio-ini/index.md) to the `googletest` and implement your own `main()` function:

`platformio.ini`

```ini
[env]
test_framework = googletest

[env:native]
platform = native

[env:esp32dev]
platform = espressif32
framework = arduino
test_framework = googletest
```

`test/test_dummy/test_dummy.cpp`

```cpp
#include <gtest/gtest.h>
// uncomment line below if you plan to use GMock
// #include <gmock/gmock.h>

// TEST(...)
// TEST_F(...)

#if defined(ARDUINO)
#include <Arduino.h>

void setup()
{
    // should be the same value as for the `test_speed` option in "platformio.ini"
    // default value is test_speed=115200
    Serial.begin(115200);

    ::testing::InitGoogleTest();
    // if you plan to use GMock, replace the line above with
    // ::testing::InitGoogleMock();
}

void loop()
{
  // Run tests
  if (RUN_ALL_TESTS())
  ;

  // sleep for 1 sec
  delay(1000);
}

#else
int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    // if you plan to use GMock, replace the line above with
    // ::testing::InitGoogleMock(&argc, argv);

    if (RUN_ALL_TESTS())
    ;

    // Always return zero-code and allow PlatformIO to parse results
    return 0;
}
#endif
```

Now, you can run tests using the [pio test](../../../reference/cli/pio-test.md) command. If you need a full output from the GoogleTest, please use [`pio test --verbose`](../../../reference/cli/pio-test.md#cmdoption-pio-test-v) option.

**Example**

Check the complete [GoogleTest example](https://github.com/platformio/platformio-examples/tree/develop/unit-testing/googletest) using GTest, GMock, and PlatformIO.

**Useful links**

- [GoogleTest Primer](https://google.github.io/googletest/primer.html) - Teaches you how to write simple tests using GoogleTest. Read this first if you are new to GoogleTest
- [GoogleTest Advanced](https://google.github.io/googletest/advanced.html) - Read this when you've finished the Primer and want to utilize GoogleTest to its full potential
- [GoogleTest Samples](https://google.github.io/googletest/samples.html) - Describes some GoogleTest samples
- [GoogleTest FAQ](https://google.github.io/googletest/faq.html) - Have a question? Want some tips? Check here first
- [Mocking for Dummies](https://google.github.io/googletest/gmock_for_dummies.html) - Teaches you how to create mock objects and use them in tests
- [Mocking Cookbook](https://google.github.io/googletest/gmock_cook_book.html) - Includes tips and approaches to common mocking use cases
- [Mocking Cheat Sheet](https://google.github.io/googletest/gmock_cheat_sheet.html) - A handy reference for matchers, actions, invariants, and more
- [Mocking FAQ](https://google.github.io/googletest/gmock_faq.html) - Contains answers to some mocking-specific questions.

## Configuration {#configuration}

The GoogleTest can be configured using system environment variables. See supported [GoogleTest environment variables](https://google.github.io/googletest/advanced.html#running-test-programs-advanced-options).

## GoogleTest CLI {#googletest-cli}

The GoogleTest works quite nicely without any command-line options at all - but for more control a few of them are available. See [GoogleTest CLI guide](https://google.github.io/googletest/advanced.html#running-test-programs-advanced-options).

There are two options for how to pass extra arguments to the testing program:

1. Using PlatformIO Core CLI and [`pio test --program-arg`](../../../reference/cli/pio-test.md#cmdoption-pio-test-a) option
2. Overriding [test_testing_command](../../../reference/platformio-ini/env/test-testing-command.md) with a custom command.

**Example**

Let's run everything in a test suite `FooTest` except `FooTest.Bar`.

Stop executing test cases after the first error and include  successful assertions in the output. We will use the `--gtest_filter` GoogleTest's CLI option.

1. Using CLI and [`pio test --program-arg`](../../../reference/cli/pio-test.md#cmdoption-pio-test-a) option:

   ```bash
   > pio test --program-arg "--gtest_filter=FooTest.*-FooTest.Bar"
   # or short format
   > pio test -a "--gtest_filter=FooTest.*-FooTest.Bar"
   ```

2. Overriding [test_testing_command](../../../reference/platformio-ini/env/test-testing-command.md) with custom command.

   ```ini
   [env:myenv]
   platform = native
   test_testing_command =
     ${platformio.build_dir}/${this.__env__}/program
     --gtest_filter=FooTest.*-FooTest.Bar
   ```

## Test Runner {#test-runner}

If you would like to change the default PlatformIO's Test Runner for the GoogleTest, please implement your [Custom Testing Framework](./custom/index.md) runner extending [GooglestTestRunner](https://github.com/platformio/platformio-core/blob/develop/platformio/test/runners/googletest.py) class. See [Custom Testing Framework](./custom/index.md) for examples.
