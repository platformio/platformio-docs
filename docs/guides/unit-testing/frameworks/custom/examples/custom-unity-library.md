<a id="unit-testing-frameworks-custom-examples-unity-library"></a>

# Custom Unity Library {#custom-unity-library}

There are frameworks such as [Arduino](/hardware/frameworks/arduino) with Mbed core and [Espressif IoT Development Framework](/hardware/frameworks/espidf) that contain a prebuilt library of [Unity](../../unity.md) testing framework. Using PlatformIO's version of [Unity](../../unity.md) will lead to compilation issues ("multiple definitions"). See [issue #3980](https://github.com/platformio/platformio-core/issues/3980).

The example below allows you to use PlatformIO's [Unity](../../unity.md) Test Runner and your custom Unity library. It can be a part of [Frameworks](../../../../../hardware/frameworks/index.md) or as a project dependency declared in [lib_deps](../../../../../reference/platformio-ini/env/lib-deps.md).

## Project example {#project-example}

We have a project based on Arduino Mbed-core that ships with a custom prebuilt "libunity.a". Let's leverage from the existing [Unity](../../unity.md) Test Runner and disable the default [throwtheswitch/Unity](https://registry.platformio.org/libraries/throwtheswitch/Unity) package.

### Structure {#structure}

```text
/project
├── platformio.ini
└── test
    ├── test_blink
    │   └── test_main.cpp
    └── test_custom_runner.py

2 directories, 3 files
```

### File contents {#file-contents}

`platformio.ini`

```ini
[env:nano33ble]
platform = nordicnrf52
board = nano33ble
framework = arduino
test_framework = custom
```

`test/test_custom_runner.py`

[Custom Test Runner](../runner.md) based on [UnityTestRunner](https://github.com/platformio/platformio-core/blob/develop/platformio/test/runners/unity.py).

```python
from platformio.public import UnityTestRunner

class CustomTestRunner(UnityTestRunner):

    # Ignore "throwtheswitch/Unity" package
    EXTRA_LIB_DEPS = None

    # Do not add default Unity to the build process
    def configure_build_env(self, env):
        pass
```

`test/test_blink/test_main.cpp`

```cpp
#include <Arduino.h>
#include <unity.h>

void setUp(void) {
    // set stuff up here
}

void tearDown(void) {
    // clean stuff up here
}

void simple_test(void)
{
    TEST_ASSERT_EQUAL(33, 33);
}

void setup()
{
    delay(2000);

    UNITY_BEGIN();
    RUN_TEST(simple_test);
    UNITY_END();
}

void loop()
{
    delay(1000);
}
```
