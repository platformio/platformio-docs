---
description: "Build main source code in pair with a test code (platformio.ini option test_build_src)."
---

# `test_build_src`

- **Type:** Boolean: `yes` or `no`
- **Multiple values:** No
- **Default:** `no`
- **Deprecated name:** `test_build_project_src` (still accepted, with a warning)

Setting `test_build_src` to `yes` will force [Unit Testing](../../../guides/unit-testing/index.md) engine to build the main source code from [src_dir](../platformio/src-dir.md) in pair with a test code. See [Shared Code](../../../guides/unit-testing/structure/shared-code.md) for details.

## Example

```ini
[env:myenv]
platform = ...
test_build_src = yes
```
