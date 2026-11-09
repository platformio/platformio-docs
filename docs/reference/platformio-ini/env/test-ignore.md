---
description: "Ignore tests where the name matches specified patterns (platformio.ini option test_ignore)."
---

<a id="projectconf-test-ignore"></a>

# `test_ignore` {#test-ignore}

- **Type:** String
- **Multiple values:** Yes

Ignore test suites whose path relative to the [test_dir](../platformio/test-dir.md) matches the specified pattern. See [Test Hierarchy](../../../guides/unit-testing/structure/hierarchy.md) for more details.

Also, you can override this option using the [`pio test --ignore`](../../cli/pio-test.md#cmdoption-pio-test-i) command.

| Pattern | Meaning |
|---|---|
| `*` | matches everything |
| `?` | matches any single character |
| `[seq]` | matches any character in seq |
| `[!seq]` | matches any character not in seq |

## Example

```ini
[env:myenv]
platform = embedded
test_ignore =
  embedded/*
  test_suite[13]
```
