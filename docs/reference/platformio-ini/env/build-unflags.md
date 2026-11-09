---
description: "A list with flags/option which should be removed (platformio.ini option build_unflags)."
---

<a id="projectconf-build-unflags"></a>

# `build_unflags` {#build-unflags}

- **Type:** String
- **Multiple values:** Yes
- **Environment variable:** [`PLATFORMIO_BUILD_UNFLAGS`](../../environment-variables.md#envvar-PLATFORMIO_BUILD_UNFLAGS), appended to the values in `platformio.ini`

Selectively remove base/initial flags that were set by the development platform.

```ini
[env:unflags]
build_unflags = -Os -std=gnu++11
build_flags = -O2
```
