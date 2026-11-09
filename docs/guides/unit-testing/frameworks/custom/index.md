<a id="unit-testing-frameworks-custom"></a>

# Custom Testing Framework {#custom-testing-framework}

<dl>

<dt>

Configuration

</dt>

<dd>

[test_framework](../../../../reference/platformio-ini/env/test-framework.md) = `custom`

</dd>

</dl>

:::info[See also]

We welcome you to provide a PR to the [https://github.com/platformio/platformio-core/pulls](https://github.com/platformio/platformio-core/pulls) with support for the missing testing framework or file a new request at [https://github.com/platformio/platformio-core/issues](https://github.com/platformio/platformio-core/issues)

:::

If you found a testing framework that is not supported by PlatformIO or the existing runner has limitations, this guide will help you to implement a custom Unit Test Runner and get full control of the testing process.

- [Custom Test Runner](./runner.md)

- [Test Runner API](./api.md)

  - [TestStatus](./api.md#teststatus)
  - [TestCase](./api.md#testcase)
  - [TestCaseSource](./api.md#testcasesource)
  - [CustomTestRunner](./api.md#customtestrunner)

- [Examples](./examples/index.md)

  - [Custom Unity Library](./examples/custom-unity-library.md)
