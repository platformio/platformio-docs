<a id="projectconf-test-build-src"></a>

# `test_build_src` {#test-build-src}

Type: `Bool (yes or no)` | Multiple: `No` | Default: `no`

Setting `test_build_src` to `yes` will force [Unit Testing](../../../guides/unit-testing/index.md) engine to build the main source code from [src_dir](../platformio/src-dir.md) in pair with a test code. See [Shared Code](../../../guides/unit-testing/structure/shared-code.md) for details.

**Example**

```ini
[env:myenv]
platform = ...
test_build_src = yes
```
