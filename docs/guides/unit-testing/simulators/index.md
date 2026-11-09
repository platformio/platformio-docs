---
description: "See a few integration examples for the popular simulation tools and frameworks:."
---

# Simulators

Simulation tools and frameworks allow you to simulate hardware systems and run unit tests in virtual environments. Simulators can significantly accelerate your project development, especially when used in pair with [Continuous Integration](../../ci/index.md).

Integration of any simulator tool to the PlatformIO [Unit Testing](../index.md) is very simple and does not require any extra software or code writing. Use [test_testing_command](../../../reference/platformio-ini/env/test-testing-command.md) project configuration option and specify a custom command to the simulation program that will be responsible for the test running. This program must output test results to the standard output or error stream.

:::note

Note that simulator tools do not require a firmware uploading stage. Use the [`pio test --without-uploading`](../../../reference/cli/pio-test.md#cmdoption-pio-test-without-uploading) command option.

:::

See a few integration examples for the popular simulation tools and frameworks:

- [QEMU](./qemu.md)
- [Renode](./renode.md)
- [SimAVR](./simavr.md)
