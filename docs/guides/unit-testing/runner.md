---
description: How the PlatformIO test runner runs native, embedded and hybrid tests, locally and on remote devices.
---

# Test runner

The PlatformIO test runner finds the test suites in the project's
[`test_dir`](../../reference/platformio-ini/platformio/test-dir.md), builds
and runs them for each project environment, and reports the status of every
test suite and test case: passed, failed or skipped. It works with the
supported [testing frameworks](./frameworks/index.md).

You can run all tests, or select environments and test suites with
[glob patterns](../../reference/cli/pio-test.md#cmdoption-pio-test-f).

## Local test runner {#local-test-runner}

[`pio test`](../../reference/cli/pio-test.md) runs tests on your computer or on
a board connected to it.

<a id="unit-testing-runner-remote"></a>

## Remote test runner {#remote-test-runner}

[`pio remote test`](../../reference/cli/pio-remote/test.md) runs tests on a
board connected to another computer through
[remote development](../remote-development.md), without SSH, a VPN or open
network ports. Use it, for example, to test on a board farm from
[CI](../ci/index.md).

<a id="unit-testing-runner-test-types"></a>

## Test types {#test-types}

Decide where each test runs: on your computer or on the target device. Tests
that use the hardware usually cannot run on a computer. Group tests by type
with a [test hierarchy](./structure/hierarchy.md), and select the right group
per environment with [`test_filter`](../../reference/platformio-ini/env/test-filter.md)
or [`test_ignore`](../../reference/platformio-ini/env/test-ignore.md).

### Native {#native}

Native tests run on your computer. Use them for code that does not depend on
the hardware, optionally with mocks of the hardware layer. Build them with the
[`native`](/hardware/platforms/native) development platform, locally or on a
CI machine.

:::warning

The `native` platform does not install a toolchain. It uses the GCC (or
compatible) compiler installed on your system, which must be in your `PATH`.
See the [`native` platform](/hardware/platforms/native) page.

:::

### Embedded {#embedded}

Embedded tests run on the target device and can test every part of the
firmware, including drivers. For each test suite, the test runner:

1. builds a test firmware with the environment's development platform;
2. uploads it to the board;
3. opens the [`test_port`](../../reference/platformio-ini/env/test-port.md)
   serial port;
4. reads the test output from the board and parses the results;
5. shows the report.

To change how results are read, or to take full control of these steps, see
[Testing frameworks](./frameworks/index.md) and
[Custom testing framework](./frameworks/custom/index.md).

### Hybrid {#hybrid}

Hybrid tests run both on your computer and on the target: build them with the
`native` platform and with an embedded
[development platform](../../hardware/platforms/index.md).
