---
description: "An extra flags to be passed to a check tool (platformio.ini option check_flags)."
---

<a id="projectconf-check-flags"></a>

# `check_flags` {#check-flags}

- **Type:** String
- **Multiple values:** Yes

Additional flags to be passed to the tool command line. This option is useful when you want to adjust the check process to fit your project requirements. By default, the flags are passed to all tools specified in [check_tool](./check-tool.md) section. To set individual flags, define tool name at the beginning of the line.

Another option for adding flags is [`pio check --flags`](../../cli/pio-check.md#cmdoption-pio-check-flags) command.

## Example

```ini
[env:extra_check_flags]
platform = ...
board = ...
check_tool = cppcheck, clangtidy
check_flags =
  --common-flag
  cppcheck: --enable=performance --inline-suppr
  clangtidy: -fix-errors -format-style=mozilla
```
