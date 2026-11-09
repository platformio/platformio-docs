<a id="projectconf-lib-ldf-mode"></a>

# `lib_ldf_mode` {#lib-ldf-mode}

:::info[See also]

Please make sure to read [Library Dependency Finder (LDF)](../../../guides/libraries/ldf.md) guide first.

:::

Type: `String` | Multiple: `No` | Default: `chain`

This option specifies how does Library Dependency Finder should analyze dependencies (`#include` directives). See [Dependency Finder Mode](../../../guides/libraries/ldf.md#ldf-mode) for details and available options.

Example:

```ini
[env:myenv]
; evaluate C/C++ Preprocessor conditional syntax
lib_ldf_mode = chain+
```
