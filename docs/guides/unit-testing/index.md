# Unit Testing {#unit-testing}

Unit Testing is a software testing technique that reduces defects in the newly developed features or reduces bugs when changing the existing functionality.

**PlatformIO Unit Testing** allows you to segregate each part of the firmware/program and test that the individual parts are working correctly. Using PlatformIO you can execute the same tests on the local host machine (native), on the multiple local embedded devices/boards (connected to local host machine), or on both. When testing both, PlatformIO builds firmware on the host machine, uploads it into a target device, starts tests and collects the test results into test reports. The final information will be shown on the host side with informative output and statistics.

Using [Remote Development](../remote-development.md) you can start unit tests on the **Remote Device** from anywhere in the world or integrate with [Continuous Integration](../ci/index.md) systems.

- [Introduction](./introduction.md)

- [Test Runner](./runner.md)

  - [Local Test Runner](./runner.md#local-test-runner)
  - [Remote Test Runner](./runner.md#remote-test-runner)
  - [Test Types](./runner.md#test-types)

- [Project Structure](./structure/index.md)

  - [Best Practices](./structure/best-practices.md)
  - [Test Hierarchy](./structure/hierarchy.md)
  - [Shared Code](./structure/shared-code.md)

- [Configuration](./configuration.md)

  - [Testing options](../../reference/platformio-ini/env/test-options.md)

- [Testing Frameworks](./frameworks/index.md)

  - [Doctest](./frameworks/doctest.md)
  - [GoogleTest](./frameworks/googletest.md)
  - [Unity](./frameworks/unity.md)
  - [Custom](./frameworks/custom/index.md)

- [Simulators](./simulators/index.md)

  - [QEMU](./simulators/qemu.md)
  - [Renode](./simulators/renode.md)
  - [SimAVR](./simulators/simavr.md)

- [Semihosting](./semihosting.md)

  - [Introduction](./semihosting.md#introduction)
  - [Configuration](./semihosting.md#configuration)
  - [Example](./semihosting.md#example)
  - [Testing](./semihosting.md#testing)

- [CLI Guide](./cli.md)

  - [pio test](../../reference/cli/pio-test.md)
  - [pio remote test](../../reference/cli/pio-remote/test.md)
