---
description: "Process tests where the name matches specified patterns (platformio.ini option test_filter)."
---

<a id="projectconf-test-filter"></a>

# `test_filter` {#test-filter}

- **Type:** String
- **Multiple values:** Yes

Process only test suites whose path relative to the [test_dir](../platformio/test-dir.md) matches the specified pattern. See [Test Hierarchy](../../../guides/unit-testing/structure/hierarchy.md) for more details.

Also, you can override this option using the [`pio test --filter`](../../cli/pio-test.md#cmdoption-pio-test-f) command.

| Pattern | Meaning |
|---|---|
| `*` | matches everything |
| `?` | matches any single character |
| `[seq]` | matches any character in seq |
| `[!seq]` | matches any character not in seq |

## Example

```ini
[env:myenv]
platform = native
test_filter =
  test_common
  native/*
```
