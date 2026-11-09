<a id="projectconf-build-unflags"></a>

# `build_unflags` {#build-unflags}

Type: `String` | Multiple: `Yes`

Selectively remove base/initial flags that were set by the development platform.

```ini
[env:unflags]
build_unflags = -Os -std=gnu++11
build_flags = -O2
```
