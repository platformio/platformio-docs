<a id="projectconf-debug-tool"></a>

# `debug_tool` {#debug-tool}

Type: `String` | Multiple: `No`

A name of debugging tool. This option is useful when board supports more than one debugging tool (adapter, probe) or you want to create [Custom](../../../hardware/debug-probes/custom.md) debugging configuration.

See available tools in [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools).

**Example**

```ini
[env:debug]
platform = ...
board = ...
debug_tool = custom
```
