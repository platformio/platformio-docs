<a id="projectconf-lib-compat-mode"></a>

# `lib_compat_mode` {#lib-compat-mode}

:::info[See also]

Please make sure to read [Library Dependency Finder (LDF)](../../../guides/libraries/ldf.md) guide first.

:::

Type: `String` | Multiple: `No` | Default: `soft`

Library compatibility mode allows one to control strictness of Library Dependency Finder. See [Compatibility Mode](../../../guides/libraries/ldf.md#ldf-compat-mode) for details and available options..

By default, this value is set to `lib_compat_mode = soft` and means that LDF will check only for framework compatibility.

Example:

```ini
[env:myenv]
; Checks for the compatibility with frameworks and dev/platforms
lib_compat_mode = strict
```
