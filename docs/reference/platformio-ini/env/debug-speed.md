---
description: "A debug adapter speed (JTAG speed) (platformio.ini option debug_speed)."
---

<a id="projectconf-debug-speed"></a>

# `debug_speed` {#debug-speed}

- **Type:** String
- **Multiple values:** No

The debug adapter speed. The value format depends on the type of [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools).

:::note

Note that this option takes effect only if [Development Platforms](../../../hardware/platforms/index.md) implement it.

:::

## Examples

```ini
[env:custom_debug_speed_examples]
...

; fixed speed in kHz
debug_speed = 500

; automatic speed (only J-Link)
debug_speed = auto

; adaptive clocking instead of fixed JTAG speed (only J-Link)
debug_speed = adaptive
```
