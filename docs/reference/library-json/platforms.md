# `platforms` {#platforms}

*Optional* | Type: `String` or `Array`

A list with compatible development platforms. The available platform name are defined in [Development Platforms](../../hardware/platforms/index.md) section.

**Example**

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
