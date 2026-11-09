<a id="unit-testing-shared-code"></a>

# Shared Code {#shared-code}

By default, PlatformIO does not build the main source code from the [src_dir](../../../reference/platformio-ini/platformio/src-dir.md) folder in pair with a test source code. If you have a shared/common code between your "main" and "test" programs, you have 2 options:

1. We recommend splitting the source code into multiple components and placing them into the [lib_dir](../../../reference/platformio-ini/platformio/lib-dir.md) (project's private libraries and components). [Library Dependency Finder (LDF)](../../libraries/ldf.md) will find and include these libraries automatically in the build process. You can include any library/component header file in your test or main application source code using `#include <MyComponent.h>`.

   See [Local & Embedded: Calculator](https://github.com/platformio/platformio-examples/tree/develop/unit-testing/calculator) for an example, where we have a "calculator" component in the [lib_dir](../../../reference/platformio-ini/platformio/lib-dir.md) folder and include it in the tests and the main application using `#include <calculator.h>`.

2. **NOT RECOMMENDED**. Manually instruct PlatformIO to build the main source code from the [src_dir](../../../reference/platformio-ini/platformio/src-dir.md) folder in pair with a test source code using the [test_build_src](../../../reference/platformio-ini/env/test-build-src.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

   ```ini
   [env:myenv]
   platform = ...
   test_build_src = true
   ```

   This is very useful if you unit test independent libraries where you can't split source code.

   :::warning

   Please note that you will need to use `#ifndef PIO_UNIT_TESTING` and `#endif` guard to hide non-test related source code. For example, own `main()`, `setup() / loop()`, or `app_main()` functions.

   :::
