---
description: Test firmware components on your computer, on the target device, or in a simulator with PlatformIO unit testing.
---

# Unit testing {#unit-testing}

PlatformIO runs unit tests of your firmware on your computer, on boards
connected to it, in simulators, or on [remote devices](../remote-development.md).
For tests on a board, PlatformIO builds a test firmware, uploads it, collects
the results over the serial port, and shows a report on your computer. The
same tests run in [CI](../ci/index.md).

## Quick start {#quick-start}

1. Create a folder for a test suite in the project's `test` folder. Its name
   must start with `test_`, for example `test/test_calculator`.
2. Add a test file, such as `test/test_calculator/test_main.c`, using the
   default [Unity](./frameworks/unity.md) framework.
3. Run the tests:

   ```bash
   pio test
   ```

For a complete walkthrough, see the tutorial
[Unit testing a "Blink" project](../../get-started/tutorials/unit-testing-blink.md).

## Guides {#guides}

| Guide | What it covers |
| --- | --- |
| [Test runner](./runner.md) | Running tests locally and remotely; native, embedded and hybrid tests |
| [Project structure](./structure/index.md) | [Test hierarchy](./structure/hierarchy.md), [shared code](./structure/shared-code.md) and [best practices](./structure/best-practices.md) |
| [Testing frameworks](./frameworks/index.md) | [Unity](./frameworks/unity.md), [GoogleTest](./frameworks/googletest.md), [Doctest](./frameworks/doctest.md) and [custom frameworks](./frameworks/custom/index.md) |
| [Simulators](./simulators/index.md) | Running embedded tests in [QEMU](./simulators/qemu.md), [Renode](./simulators/renode.md) and [SimAVR](./simulators/simavr.md) |
| [Semihosting](./semihosting.md) | Reporting results through the debug probe instead of a serial port |

<a id="configuration"></a>

## Configuration {#unit-testing-configuration}

Configure testing per project environment with these
[`platformio.ini` options](../../reference/platformio-ini/env/test-options.md):

| Option | Purpose |
| --- | --- |
| [`test_framework`](../../reference/platformio-ini/env/test-framework.md) | The testing framework |
| [`test_filter`](../../reference/platformio-ini/env/test-filter.md) | Run only the matching test suites |
| [`test_ignore`](../../reference/platformio-ini/env/test-ignore.md) | Skip the matching test suites |
| [`test_port`](../../reference/platformio-ini/env/test-port.md) | The serial port that receives the results |
| [`test_speed`](../../reference/platformio-ini/env/test-speed.md) | The baud rate of that port |
| [`test_build_src`](../../reference/platformio-ini/env/test-build-src.md) | Also build the project's `src` folder |
| [`test_testing_command`](../../reference/platformio-ini/env/test-testing-command.md) | A custom command that runs the test program |

<a id="cli"></a>

## Command line {#unit-testing-cli}

- [`pio test`](../../reference/cli/pio-test.md) runs tests locally. Its options
  override the `platformio.ini` options for one run.
- [`pio remote test`](../../reference/cli/pio-remote/test.md) runs tests on a
  device connected to a [remote agent](../remote-development.md).

<a id="learn-more"></a>

## Learn more {#unit-testing-learn-more}

The article series *Unit Testing with PlatformIO*:

1. [The basics](https://piolabs.com/blog/insights/unit-testing-part-1.html)
2. [Running tests on an embedded target](https://piolabs.com/blog/insights/unit-testing-part-2.html)
3. [Continuous integration and remote testing](https://piolabs.com/blog/insights/unit-testing-part-3.html)

Tutorials with unit tests on real hardware are listed in
[Tutorials](../../get-started/tutorials/index.md). Example projects:
[calculator (native and embedded)](https://github.com/platformio/platformio-examples/tree/develop/unit-testing/calculator),
[Arduino mock](https://github.com/platformio/platformio-examples/tree/develop/unit-testing/arduino-mock),
and [more](https://github.com/platformio/platformio-examples/tree/develop/unit-testing).
