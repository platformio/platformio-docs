<a id="unit-testing-test-runner"></a>

# Test Runner {#test-runner}

**PlatformIO Test Runner** is a powerful unit testing tool. It runs your unit tests located in the [test_dir](../../reference/platformio-ini/platformio/test-dir.md), navigates through tests, and facilitates the processing of test results. Test Runner supports the most popular [Testing Frameworks](./frameworks/index.md).

Test Runner allows you to run specific project environments or filter tests using the "Glob patterns". Once tests are finished, Test Runner provides a rich report with the status of all test suites and test cases (passed, failed, ignored/skipped).

## Local Test Runner {#local-test-runner}

**Local Test Runner** allows you to run a test on a local host machine or on a local target device (board). In this case, you need to use the [pio test](../../reference/cli/pio-test.md) command.

<a id="unit-testing-runner-remote"></a>

## Remote Test Runner {#remote-test-runner}

**Remote Test Runner** allows you to run test on the remote machine or on the remote target device (board) without having to depend on OS software, extra software, SSH, VPN or opening network ports. Remote Unit Testing works in pair with [Remote Development](../remote-development.md). In this case, you need to use the special command [pio remote test](../../reference/cli/pio-remote/test.md).

PlatformIO supports multiple [Continuous Integration](../ci/index.md) systems where you can run unit tests at each integration stage.

<a id="unit-testing-runner-test-types"></a>

## Test Types {#test-types}

Before writing a test, you need to decide where it will be executed later: on the host machine or on the target device connected to the host machine. Tests that are written for the target device typically will not work on your host machine due to the missing peripheral and other connectivity.

Using the [Test Hierarchy](./structure/hierarchy.md) allows you to organize tests by types and later skip an incompatible group of tests using [test_filter](../../reference/platformio-ini/env/test-filter.md) or [test_ignore](../../reference/platformio-ini/env/test-ignore.md) options in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md).

### Native {#native}

Native tests are intended for the project components that are independent of physical hardware. You can also use them in pair with Mocking frameworks.

PlatformIO provides you a [Native](/hardware/platforms/native) development platform to build and run tests on the local host machine or using [Continuous Integration](../ci/index.md) VM instance.

:::warning

PlatformIO does not install automatically any toolchains for the [Native](/hardware/platforms/native) development platform. It depends on the system `GCC` toolchain that must be added to the `PATH` system environment variable.

Please check the "Installation" guide for the [Native](/hardware/platforms/native) development platform.

:::

### Embedded {#embedded}

Embedded tests are intended for the target devices (boards, hardware). They allow you to deeply test all project components that are part of your firmware.

How does PlatformIO Unit Testing Runner process embedded tests?

1. It builds a special firmware intended for your target using a compatible embedded development platform
2. Uploads a firmware to the end target (flashes device)
3. Connects to the target using a Serial interface and [test_port](../../reference/platformio-ini/env/test-port.md)
4. Gathers Serial output from the target and parses test result on the host machine
5. Provides test results.

Please check [Testing Frameworks](./frameworks/index.md) documentation and learn how to provide a custom configuration or to get full control of PlatformIO Unit Testing Runner using [Custom Testing Framework](./frameworks/custom/index.md) implementation.

### Hybrid {#hybrid}

The tests that work on a host machine and on the embedded target are hybrid tests. You can run them using [Native](/hardware/platforms/native) development platform or embedded development [Development Platforms](../../hardware/platforms/index.md).
