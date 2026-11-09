---
description: "If you would like to change the default PlatformIO's Test Runner for the Unity, please implement your Custom Testing Framework runner extending UnityTestRunner class."
---

<a id="unit-testing-frameworks-unity"></a>

# Unity {#unity}

<dl>

<dt>

Registry

</dt>

<dd>

[https://registry.platformio.org/libraries/throwtheswitch/Unity](https://registry.platformio.org/libraries/throwtheswitch/Unity)

</dd>

<dt>

Configuration

</dt>

<dd>

[test_framework](../../../reference/platformio-ini/env/test-framework.md) = `unity`

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

Yes

</dd>

<dt>

Mocking Support

</dt>

<dd>

No

</dd>

</dl>

**Unity** is a unit test framework. The goal has been to keep it small and functional. Unity was designed to be cross-platform. It works hard to stick with C standards while still providing support for the many embedded C compilers that bend the rules. Unity has been used with many compilers, including GCC, IAR, Clang, Green Hills, Microchip, and MS Visual Studio. It's not much work to get it to work with a new target.

## Getting started {#getting-started}

Test files are C/C++ files. Most often you will create a single test file for each C/C++ component that you want to test. The test file should include `unity.h` and the header for your C/C++ component to be tested.

Next, a test file will include a `setUp()` and `tearDown()` function. The **setUp** function can contain anything you would like to run before each test. The **tearDown** function can contain anything you would like to run after each test. Both functions accept no arguments and return nothing. You may leave either or both of these blank if you have no need for them.

The majority of the file will be a series of test functions. Test functions follow the convention of starting with the word `test_` or `spec_`. You don't HAVE to name them this way, but it makes it clear what functions are tests for other developers. Test functions take no arguments and return nothing. All test accounting is handled internally in Unity.

Finally, at the bottom of your test file, you will write a `main()` function (`setup() / loop()` for [Arduino](/hardware/frameworks/arduino), `app_main()` for [Espressif IoT Development Framework](/hardware/frameworks/espidf)). This function will call `UNITY_BEGIN()`, then `RUN_TEST` for each test, and finally `UNITY_END()`. This is what will actually trigger each of those test functions to run, so it is important that each function gets its own `RUN_TEST` call. Please remember to add each test to the main function.

When you're done, your test file will look something like this:

```c
#include "unity.h"
#include "file_to_test.h"

void setUp(void) {
  // set stuff up here
}

void tearDown(void) {
  // clean stuff up here
}

void test_function_should_doBlahAndBlah(void) {
  // test stuff
}

void test_function_should_doAlsoDoBlah(void) {
  // more test stuff
}

int runUnityTests(void) {
  UNITY_BEGIN();
  RUN_TEST(test_function_should_doBlahAndBlah);
  RUN_TEST(test_function_should_doAlsoDoBlah);
  return UNITY_END();
}

// WARNING!!! PLEASE REMOVE UNNECESSARY MAIN IMPLEMENTATIONS //

/**
  * For native dev-platform or for some embedded frameworks
  */
int main(void) {
  return runUnityTests();
}

/**
  * For Arduino framework
  */
void setup() {
  // Wait ~2 seconds before the Unity test runner
  // establishes connection with a board Serial interface
  delay(2000);

  runUnityTests();
}
void loop() {}

/**
  * For ESP-IDF framework
  */
void app_main() {
  runUnityTests();
}
```

**Useful links**

- [Unity - Getting Started](https://github.com/ThrowTheSwitch/Unity/blob/master/docs/UnityGettingStartedGuide.md)
- [Unity - Assertions Reference](https://github.com/ThrowTheSwitch/Unity/blob/master/docs/UnityAssertionsReference.md)
- [Unity - Assertions CheatSheet](https://github.com/ThrowTheSwitch/Unity/blob/master/docs/UnityAssertionsCheatSheetSuitableforPrintingandPossiblyFraming.pdf)

## Configuration {#configuration}

All of Unity's configuration options are `#defines`. Most of these are simple definitions. A couple is macros with arguments. Because these options are specified via C defines, you can pass most of these options to the [build_flags](../../../reference/platformio-ini/env/build-flags.md).

See [Unity Configuration Guide](https://github.com/ThrowTheSwitch/Unity/blob/master/docs/UnityConfigurationGuide.md) for the available options.

**Example**

```ini
[env:extra_unity_options]
platform = native
build_flags =
    -D UNITY_INT_WIDTH=16
    -D UNITY_FLOAT_TYPE=float16_t
```

<a id="unit-testing-frameworks-unity-custom-config"></a>

### Custom `unity_config.h` {#custom-unity-config-h}

PlatformIO's Unity test runner comes with an already defined `UNITY_INCLUDE_CONFIG_H` macro. It looks for a custom `unity_config.h` in a current test folder. In case the `unity_config.h` is missed, PlatformIO will walk through the test hierarchy until to the root ([test_dir](../../../reference/platformio-ini/platformio/test-dir.md)).

Let's take a look at the Pizza Project from the [Test Hierarchy](../structure/hierarchy.md) example. If you run an "embedded/components/sauce/test_tomatos" test, PlatformIO will check folders for the `unity_config.h` in the following order:

1. "embedded/components/sauce/test_tomatos"
2. "embedded/components/sauce"
3. "embedded/components"
4. "embedded"
5. [test_dir](../../../reference/platformio-ini/platformio/test-dir.md) (finish).

If the `unity_config.h` is not found, PlatformIO will generate a default `unity_config.h` that routes test result output to a framework specified in the [framework](../../../reference/platformio-ini/env/framework.md). On the [Native](/hardware/platforms/native) development platform, it will be the standard input/output, whereas, on the embedded development platforms, the first available Serial interface will be used (see [UNITY_FRAMEWORK_CONFIG](https://github.com/platformio/platformio-core/blob/develop/platformio/test/runners/unity.py) for the default framework configurations).

**Useful links**

- ["unity_config.h" template](https://github.com/ThrowTheSwitch/Unity/blob/master/examples/unity_config.h)
- [STM32Cube HAL and Nucleo-F401RE: debugging and unit testing](../../../get-started/tutorials/ststm32/stm32cube-debugging-unit-testing.md)
- [STM32Cube Unit Testing](https://github.com/platformio/platformio-examples/tree/develop/unit-testing/stm32cube) example with the custom `unity_config.h`.

### Custom Unity Library {#custom-unity-library}

See [Custom Unity Library](./custom/examples/custom-unity-library.md) example.

## Test Runner {#test-runner}

Thanks to the minimum system requirements of the Unity testing framework, you can use Unity for all [Test Types](../runner.md#unit-testing-runner-test-types), including for constrained embedded devices.

If you would like to change the default PlatformIO's Test Runner for the Unity, please implement your [Custom Testing Framework](./custom/index.md) runner extending [UnityTestRunner](https://github.com/platformio/platformio-core/blob/develop/platformio/test/runners/unity.py) class. See [Custom Testing Framework](./custom/index.md) for the examples.
