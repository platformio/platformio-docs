---
description: "List of defect severity types for analysis (platformio.ini option check_severity)."
---

<a id="projectconf-check-severity"></a>

# `check_severity` {#check-severity}

- **Type:** String: `low`, `medium`, `high`
- **Multiple values:** Yes
- **Default:** `low`, `medium`, `high`

This option allows specifying the [Defect severity](../../../guides/static-code-analysis/severity.md) types which will be reported by the [Check tools](../../../guides/static-code-analysis/tools/index.md).

Another option for filtering source files is [`pio check --severity`](../../cli/pio-check.md#cmdoption-pio-check-severity) command.

## Example

```ini
[env:detect_only_medium_or_high_defects]
platform = ...
board = ...
check_severity = medium, high
```
