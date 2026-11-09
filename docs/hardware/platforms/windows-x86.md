---
title: "Windows x86"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-windows-x86"></a>

# Windows x86

**Registry:** [https://registry.platformio.org/platforms/platformio/windows_x86](https://registry.platformio.org/platforms/platformio/windows_x86)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/windows_x86`

Windows x86 (32-bit) is a metafamily of graphical operating systems developed and marketed by Microsoft. Using host OS (Windows, Linux 32/64 or Mac OS X) you can build native application for Windows x86 platform.

For more detailed information please visit [vendor site](https://registry.platformio.org/platforms/platformio/windows_x86?utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [Windows x86 development platform repository](https://github.com/platformio/platform-windows_x86/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [hello-world](https://github.com/platformio/platform-windows_x86/tree/master/examples/hello-world?utm_source=platformio.org&utm_medium=docs)

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-windows_x86/releases) of Windows x86 development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = windows_x86

; Specific version
[env:custom_stable]
platform = windows_x86@x.y.z
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-windows_x86.git
```

## Packages

| Name | Description |
|---|---|
| [toolchain-gccmingw32](https://registry.platformio.org/tools/platformio/toolchain-gccmingw32) | MinGW - Minimalist GNU for Windows |
