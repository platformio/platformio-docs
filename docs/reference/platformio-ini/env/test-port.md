<a id="projectconf-test-port"></a>

# `test_port` {#test-port}

Type: `String (Pattern)` | Multiple: `No`

This option specifies communication interface between PlatformIO [Unit Testing](../../../guides/unit-testing/index.md) Test Runner and the target device. The possible values are the same as documented for [monitor_port](./monitor-port.md) option.

If `test_port` isn't specified, the PlatformIO [Unit Testing](../../../guides/unit-testing/index.md) runner will try to detect it automatically.

To print all available serial ports use the [pio device list](../../cli/pio-device/list.md) command.
