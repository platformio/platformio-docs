---
description: "A name of a unit test to be debugged (platformio.ini option debug_test)."
---

# `debug_test`

- **Type:** String
- **Multiple values:** No

A name of a unit test to be debugged. See [Unit Testing](../../../guides/unit-testing/index.md) for further details.

If a source file of a test is located in the root of [test_dir](../platformio/test-dir.md), the `debug_test` option should be set to `*`.

## Examples

```ini
[env:debug_a_test]
...

debug_test = test_calculator
```
