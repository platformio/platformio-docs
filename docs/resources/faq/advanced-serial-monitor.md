---
description: Use a serial terminal with a graphical UI, such as CoolTerm, together with PlatformIO.
---

<a id="faq-advanced-serial-monitor-ui"></a>

# Serial monitor with a graphical UI {#advanced-serial-monitor-with-ui}

PlatformIO's serial monitor, [`pio device monitor`](../../reference/cli/pio-device/monitor.md),
runs in the terminal. If you prefer a graphical serial terminal, you can use
any other one, for example the free, cross-platform
[CoolTerm](https://freeware.the-meiers.org/?utm_source=platformio&utm_medium=docs).

:::warning

Disconnect CoolTerm from the serial port before you upload firmware.
PlatformIO cannot close a port that another application holds open, so the
upload fails.

:::
