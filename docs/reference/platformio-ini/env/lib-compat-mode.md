---
description: "Configure a strictness (compatibility mode by frameworks, development platforms) of Library Dependency Finder (LDF) (platformio.ini option lib_compat_mode)."
---

<a id="projectconf-lib-compat-mode"></a>

# `lib_compat_mode` {#lib-compat-mode}

:::info[See also]

Read [Library Dependency Finder (LDF)](../../../guides/libraries/ldf.md) guide first.

:::

- **Type:** String: `off`, `soft`, `strict`
- **Multiple values:** No
- **Default:** `soft`

Library compatibility mode allows one to control strictness of Library Dependency Finder. See [Compatibility Mode](../../../guides/libraries/ldf.md#ldf-compat-mode) for details and available options.

By default, this value is set to `lib_compat_mode = soft` and means that LDF will check only for framework compatibility.

## Example

```ini
[env:myenv]
; Checks for the compatibility with frameworks and dev/platforms
lib_compat_mode = strict
```
