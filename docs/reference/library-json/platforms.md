---
description: "A list with compatible development platforms."
---

# `platforms`

- **Required:** No
- **Type:** String or array of strings
- **Limits:** Each value: a development platform name or `*`; at most 50 characters, only lowercase letters, digits, `-` and `_`.

A list with compatible development platforms. The available platform name are defined in [Development Platforms](../../hardware/platforms/index.md) section.

## Example

```javascript
"platforms": ["atmelavr", "espressif8266"]
```

If the library is compatible with the all platforms, then do not declare this field or use `*` symbol:

```javascript
"platforms": "*"
```

:::note

PlatformIO does not check platforms for compatibility in default mode. See [Compatibility Mode](../../guides/libraries/ldf.md#ldf-compat-mode) for details. If you need a strict checking for compatible platforms for a library, please set [libCompatMode](./build/libcompatmode.md) to `strict`.

:::
