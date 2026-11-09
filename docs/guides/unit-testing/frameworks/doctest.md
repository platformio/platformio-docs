---
description: "If you would like to change the default PlatformIO's Test Runner for the Doctest, please implement your Custom Testing Framework runner extending DoctestTestRunner class."
---

# Doctest

<dl>

<dt>

Registry

</dt>

<dd>

[https://registry.platformio.org/libraries/doctest/doctest](https://registry.platformio.org/libraries/doctest/doctest)

</dd>

<dt>

Configuration

</dt>

<dd>

[test_framework](../../../reference/platformio-ini/env/test-framework.md) = `doctest`

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

No

</dd>

<dt>

Mocking Support

</dt>

<dd>

No

</dd>

</dl>

**Doctest** is a new C++ testing framework but is by far the fastest both in compile times and runtime compared to other feature-rich alternatives.

## Getting started {#getting-started}

To get started with the Doctest all you need is to set the [test_framework](../../../reference/platformio-ini/env/test-framework.md) option in your [`platformio.ini`](../../../reference/platformio-ini/index.md) to the `doctest` and implement your own `main()` function that forces the Doctest to report successful test cases:

`platformio.ini`

```ini
[env:native]
platform = native
test_framework = doctest
```

`test/test_dummy/test_main.cpp`

```cpp
#define DOCTEST_CONFIG_IMPLEMENT  // REQUIRED: Enable custom main()
#include <doctest.h>

// TEST_CASE ...
// TEST_SUITE ...

int main(int argc, char **argv)
{
  doctest::Context context;

  // BEGIN:: PLATFORMIO REQUIRED OPTIONS
  context.setOption("success", true);     // Report successful tests
  context.setOption("no-exitcode", true); // Do not return non-zero code on failed test case
  // END:: PLATFORMIO REQUIRED OPTIONS

  // YOUR CUSTOM DOCTEST OPTIONS

  context.applyCommandLine(argc, argv);
  return context.run();
}
```

Now, you can run tests using the [pio test](../../../reference/cli/pio-test.md) command. If you need a full output from the Doctest, please use [`pio test --verbose`](../../../reference/cli/pio-test.md#cmdoption-pio-test-v) option.

**Useful links**

- [Doctest - Tutorial](https://github.com/doctest/doctest/blob/master/doc/markdown/tutorial.md)
- [Doctest - Assertion macros](https://github.com/doctest/doctest/blob/master/doc/markdown/assertions.md)
- [Doctest - Logging macros](https://github.com/doctest/doctest/blob/master/doc/markdown/logging.md)
- [Doctest - Test cases, subcases and test fixtures](https://github.com/doctest/doctest/blob/master/doc/markdown/testcases.md)

## Configuration {#configuration}

The Doctest can be configured in two ways: using identifiers (macros) or `doctest::Context`.

### Using identifiers {#using-identifiers}

The Doctest is designed to "just work" as much as possible. It also allows configuring how it is built with a set of identifiers.

See [Doctest Configuration Guide](https://github.com/doctest/doctest/blob/master/doc/markdown/configuration.md) for the available identifiers.

**Example**

```ini
[env:extra_doctest_identifiers]
platform = native
test_framework = doctest
build_flags =
    -D DOCTEST_CONFIG_SUPER_FAST_ASSERTS
    -D DOCTEST_CONFIG_NO_COMPARISON_WARNING_SUPPRESSION
```

### Using `doctest::Context` {#using-doctest-context}

If you need more control and want to set options with code to the execution context, then the custom implementation of `main()` function will give you access to the `doctest::Context`.

See [The "main()" entry point](https://github.com/doctest/doctest/blob/master/doc/markdown/main.md) docs for details.

**Example**

```cpp
int main(int argc, char **argv)
{
  doctest::Context context;

  // BEGIN:: PLATFORMIO REQUIRED OPTIONS
  context.setOption("success", true);     // Reports successful tests
  context.setOption("no-exitcode", true); // Do not return non-zero code on failed test case
  // END:: PLATFORMIO REQUIRED OPTIONS

  // YOUR CUSTOM DOCTEST OPTIONS
  context.setOption("abort-after", 5);    // stop test execution after 5 failed assertions
  context.setOption("order-by", "name");  // sort the test cases by their name

  context.applyCommandLine(argc, argv);
  return context.run();
}
```

## Doctest CLI {#doctest-cli}

The Doctest works quite nicely without any command-line options at all - but for more control a few of them are available. See [Doctest CLI guide](https://github.com/doctest/doctest/blob/master/doc/markdown/commandline.md).

There are two options for how to pass extra arguments to the testing program:

1. Using PlatformIO Core CLI and [`pio test --program-arg`](../../../reference/cli/pio-test.md#cmdoption-pio-test-a) option
2. Overriding [test_testing_command](../../../reference/platformio-ini/env/test-testing-command.md) with a custom command.

**Example**

Stop executing test cases after the first error and include  successful assertions in the output. We will use the `-aa, --abort-after=<int>` and `-s,--success=<bool>` Doctest's CLI option.

1. Using CLI and [`pio test --program-arg`](../../../reference/cli/pio-test.md#cmdoption-pio-test-a) option:

   ```bash
   > pio test --program-arg "--abort-after=1" --program-arg="-s"
   # or short format
   > pio test -a "-aa=1" -a "-s"
   ```

2. Overriding [test_testing_command](../../../reference/platformio-ini/env/test-testing-command.md) with custom command.

   ```ini
   [env:myenv]
   platform = native
   test_testing_command =
     ${platformio.build_dir}/${this.__env__}/program
     -aa=1
     -s
   ```

## Test Runner {#test-runner}

If you would like to change the default PlatformIO's Test Runner for the Doctest, please implement your [Custom Testing Framework](./custom/index.md) runner extending [DoctestTestRunner](https://github.com/platformio/platformio-core/blob/develop/platformio/test/runners/doctest.py) class. See [Custom Testing Framework](./custom/index.md) for examples.
