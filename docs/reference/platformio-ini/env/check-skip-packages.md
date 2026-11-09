---
description: "Skip checking includes from packages directory (platformio.ini option check_skip_packages)."
---

# `check_skip_packages`

- **Type:** Boolean: `yes` or `no`
- **Multiple values:** No
- **Default:** `no`

Exclude underlying third-party packages from the checking process. By default, PlatformIO passes frameworks and toolchains include paths required by internal analysis tools to properly analyze project sources. Some of the supported analysis tools use their own preprocessor which may fail to parse perfectly valid code and thus provide empty or partial check reports. This option is useful when developers have no control over this third-party code and want to perform analysis at least on project sources.

Another option for excluding third-party packages is [`pio check --skip-packages`](../../cli/pio-check.md#cmdoption-pio-check-skip-packages) command.

## Example

```ini
[env:extra_check_flags]
platform = ...
board = ...
check_tool = cppcheck, clangtidy
check_skip_packages = yes
```
