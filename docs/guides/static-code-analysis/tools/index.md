---
description: "Detailed information about supported check tools and their configuration process can be found on these pages:."
---

# Check tools {#check-tools}

You can switch between or specify multiple tools used for finding defects using [check_tool](../../../reference/platformio-ini/env/check-tool.md) option:

```ini
[env:myenv]
platform = ...
board = ...
check_tool = cppcheck, clangtidy
```

Detailed information about supported check tools and their configuration process can be found on these pages:

- [Clang-Tidy](./clang-tidy.md)
- [Cppcheck](./cppcheck.md)
