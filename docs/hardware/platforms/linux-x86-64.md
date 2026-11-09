---
title: "Linux x86_64"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The Linux x86_64 development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

<a id="platform-linux-x86-64"></a>

# Linux x86_64

**Registry:** [https://registry.platformio.org/platforms/platformio/linux_x86_64](https://registry.platformio.org/platforms/platformio/linux_x86_64)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/linux_x86_64`

Linux x86_64 (64-bit) is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X or Linux 64-bit) you can build native application for Linux x86_64 platform.

Vendor website: [registry.platformio.org](https://registry.platformio.org/platforms/platformio/linux_x86_64?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [Linux x86_64 platform repository](https://github.com/platformio/platform-linux_x86_64/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [hello-world](https://github.com/platformio/platform-linux_x86_64/tree/master/examples/hello-world?utm_source=platformio.org&utm_medium=docs)

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-linux_x86_64/releases) of the Linux x86_64 platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

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
