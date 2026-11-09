---
description: "The unity_config.h and unity_config.cpp files are located in the embedded folder and are common for the embedded/components/sauce/test_tomatos, embedded/stove/test_humidity, and embedded/stove/test_temperature tests."
---

<a id="unit-testing-test-hierarchy"></a>

# Test hierarchy {#test-hierarchy}

PlatformIO looks for the tests in the project [test_dir](../../../reference/platformio-ini/platformio/test-dir.md). The only folder with a name prefixed by `test_` is nominated for unit testing and should be an independent test/application with its own `main()` function (`setup() / loop()` for [Arduino](/hardware/frameworks/arduino), `app_main()` for [Espressif IoT Development Framework](/hardware/frameworks/espidf)). Nested folders are supported and will help you to organize your tests.

The root [test_dir](../../../reference/platformio-ini/platformio/test-dir.md) and a folder of the active test are automatically added to the `CPPPATH` scope (C Preprocessor Search Path). Also, C/C++ files located in the root of [test_dir](../../../reference/platformio-ini/platformio/test-dir.md) will be compiled together with the active test source files. The root [test_dir](../../../reference/platformio-ini/platformio/test-dir.md) is useful for placing configuration and extra C/C++ files related to the [Testing Frameworks](../frameworks/index.md).

---

- If you have a single test application, you can place the source code files directly in the [test_dir](../../../reference/platformio-ini/platformio/test-dir.md) folder

- If you want several test applications, you can organize them in subfolders under [test_dir](../../../reference/platformio-ini/platformio/test-dir.md):

  - each test application goes into a subfolder with a name **starting** with `test_`
  - additional levels of folders are allowed to properly organize your tests - see the example **Pizza Project** below
  - the [test_filter](../../../reference/platformio-ini/env/test-filter.md) option in [`platformio.ini`](../../../reference/platformio-ini/index.md) or the [`pio test --filter`](../../../reference/cli/pio-test.md#cmdoption-pio-test-f) option on the CLI will restrict the tests to only those test suites whose path is relative to the [test_dir](../../../reference/platformio-ini/platformio/test-dir.md) and matches the filter
  - the [test_ignore](../../../reference/platformio-ini/env/test-ignore.md) option in [`platformio.ini`](../../../reference/platformio-ini/index.md) or the [`pio test --ignore`](../../../reference/cli/pio-test.md#cmdoption-pio-test-i) option on the CLI will ignore test suites whose path is relative to the [test_dir](../../../reference/platformio-ini/platformio/test-dir.md) and matches the filter.

Example of using the filter / ignore option in [`platformio.ini`](../../../reference/platformio-ini/index.md) for the **Pizza Project** below:

```ini
[env:myenv]
test_filter = embedded/*
test_ignore = embedded/components/*
```

will only execute the `embedded/stove/test_humidity`, `embedded/stove/test_temperature` test suites and will ignore the `embedded/components/sauce/test_tomatos` test suite.

**Example of Pizza Project**

Let's demystify how PlatformIO handles unit tests using a virtual "Pizza Project" having the following structure:

```text
project_dir
├── include
│   └── pizza_config.h
├── lib
│   ├── Cheese
│   │   ├── include
│   │   │   └── cheese.h
│   │   └── src
│   │       └── cheese.cpp
│   ├── Dough
│   │   ├── include
│   │   │   └── dough.h
│   │   └── src
│   │       └── dough.cpp
│   └── Sauce
│       ├── include
│       │   └── sauce.h
│       └── src
│           └── sauce.cpp
├── platformio.ini
├── src
│   └── baking.cpp
└── test
   ├── embedded
   │   ├── components
   │   │   └── sauce
   │   │       └── test_tomatos
   │   │           └── prepare.cpp
   │   ├── stove
   │   │   ├── test_humidity
   │   │   │   ├── measure.cpp
   │   │   │   └── sensor.cpp
   │   │   └── test_temperature
   │   │       ├── measure.cpp
   │   │       └── sensor
   │   │           ├── sensor.cpp
   │   │           └── sensor.h
   │   ├── unity_config.cpp
   │   └── unity_config.h
   └── test_ingredients
      ├── include
      │   ├── cheese.h
      │   ├── vegetables.h
      │   ├── water.h
      │   ├── wheat.h
      │   └── yeast.h
      └── weighing.cpp
```

The main source code ("pizza baking") is located in the `src` folder. This is a production code. A cooking process consists of multiple subprocesses and depends on the components located in the `lib` folder. Each pizza's component can be tested independently using unit testing.

The Pizza Project consists of 4 independent tests:

1. `embedded/components/sauce/test_tomatos`
2. `embedded/stove/test_humidity`
3. `embedded/stove/test_temperature`
4. `test_ingredients`

PlatformIO treats each test as an independent micro project with its own source files and subfolders. You can include local header files using the relative paths. For example, the `test_ingredients/weighing.cpp` source file includes `cheese.h` as `#include <include/cheese.h>`.

The `unity_config.h` and `unity_config.cpp` files are located in the `embedded` folder and are common for the `embedded/components/sauce/test_tomatos`, `embedded/stove/test_humidity`, and `embedded/stove/test_temperature` tests. This allows you to run a group of tests only on the embedded target and route a test result output to the custom Serial/UART interface. On the other hand, the `test_ingredients` test uses the default Unity configuration provided by PlatformIO. For more details, please check the documentation for the [Unity](../frameworks/unity.md) testing framework.
