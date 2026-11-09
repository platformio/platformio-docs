<a id="unit-testing-frameworks"></a>

# Testing Frameworks {#testing-frameworks}

PlatformIO supports the most popular testing frameworks and allows you to easily switch between them using the [test_framework](../../../reference/platformio-ini/env/test-framework.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

You can mix different frameworks in the same project. For example, use a more advanced C++ testing framework with Mocks for the [Native](/hardware/platforms/native) development platform to run desktop tests on a host machine and a lightweight framework, such as [Unity](./unity.md), for running tests on the target embedded device with constrained resources.

**Compatibility**

| Framework | [Test Types](../runner.md#unit-testing-runner-test-types) | [Development Platforms](../../../hardware/platforms/index.md) | Mocking |
|---|---|---|---|
| [Doctest](./doctest.md) | Native | [Native](/hardware/platforms/native) | No |
| [GoogleTest](./googletest.md) | Any | [Native](/hardware/platforms/native), [Espressif 8266](/hardware/platforms/espressif8266), [Espressif 32](/hardware/platforms/espressif32) | Yes |
| [Unity](./unity.md) | Any | Any | No |

:::tip

We highly recommend using the [Unity](./unity.md) testing framework if you plan to run tests on the target devices with constrained resources. The [Unity](./unity.md) has minimal requirements and works even on the 8-bit AVR MCUs.

:::

See supported testing frameworks:

- [Doctest](./doctest.md)
- [GoogleTest](./googletest.md)
- [Unity](./unity.md)
- [Custom](./custom/index.md)
