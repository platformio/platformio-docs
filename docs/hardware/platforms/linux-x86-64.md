---
title: "Linux x86_64"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-linux-x86-64"></a>

# Linux x86_64

**Registry:** [https://registry.platformio.org/platforms/platformio/linux_x86_64](https://registry.platformio.org/platforms/platformio/linux_x86_64)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/linux_x86_64`

Linux x86_64 (64-bit) is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X or Linux 64-bit) you can build native application for Linux x86_64 platform.

For more detailed information please visit [vendor site](https://registry.platformio.org/platforms/platformio/linux_x86_64?utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [Linux x86_64 development platform repository](https://github.com/platformio/platform-linux_x86_64/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [hello-world](https://github.com/platformio/platform-linux_x86_64/tree/master/examples/hello-world?utm_source=platformio.org&utm_medium=docs)

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-linux_x86_64/releases) of Linux x86_64 development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = linux_x86_64

; Specific version
[env:custom_stable]
platform = linux_x86_64@x.y.z
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-linux_x86_64.git
```

## Packages

| Name | Description |
|---|---|
| [toolchain-gcclinux64](https://registry.platformio.org/tools/platformio/toolchain-gcclinux64) | GCC Toolchain for Linux x86_64 machines |
