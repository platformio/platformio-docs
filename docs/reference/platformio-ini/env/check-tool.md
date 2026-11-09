---
description: "A list of check tools used for analysis (platformio.ini option check_tool)."
---

# `check_tool`

- **Type:** String: `cppcheck`, `clangtidy`
- **Multiple values:** Yes
- **Default:** `cppcheck`

A name of the check tool used for analysis. This option is useful when you want to check source code with two or more tools.

See available tools in [Check tools](../../../guides/static-code-analysis/tools/index.md).

## Example

```ini
[env:myenv]
platform = ...
board = ...
check_tool = cppcheck, clangtidy
```
