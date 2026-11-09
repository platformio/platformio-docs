<a id="faq-advanced-serial-monitor-ui"></a>

# Advanced Serial Monitor with UI {#advanced-serial-monitor-with-ui}

PlatformIO Core provides CLI version ([pio device monitor](../../reference/cli/pio-device/monitor.md)) of Serial Monitor. If you need advanced instrument with a rich UI, we recommend free and multi-platform [CoolTerm](https://freeware.the-meiers.org/?utm_source=platformio&utm_medium=docs) serial port terminal application.

:::warning

Please note that you need to **manually disconnect (close serial port connection)** in CoolTerm **before doing uploading** in PlatformIO. PlatformIO can not disconnect/connect to a target device automatically when CoolTerm is used.

:::
