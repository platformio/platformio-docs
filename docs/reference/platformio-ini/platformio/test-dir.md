---
description: "A location where PlatformIO Unit Testing engine looks for test source files (platformio.ini option test_dir)."
---

<a id="projectconf-pio-test-dir"></a>

# `test_dir` {#test-dir}

- **Type:** Path
- **Multiple values:** No
- **Default:** `${PROJECT_DIR}/test`
- **Environment variable:** [`PLATFORMIO_TEST_DIR`](../../environment-variables.md#envvar-PLATFORMIO_TEST_DIR), overrides the value in `platformio.ini`

The directory where [Unit Testing](../../../guides/unit-testing/index.md) engine will look for the tests.  The default value is `test`, meaning a `test` directory located in the root of the project.
