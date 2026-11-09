---
title: "Linux i686"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The Linux i686 development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

# Linux i686

**Registry:** [https://registry.platformio.org/platforms/platformio/linux_i686](https://registry.platformio.org/platforms/platformio/linux_i686)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/linux_i686`

Linux i686 (32-bit) is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X or Linux 32-bit) you can build native application for Linux i686 platform.

Vendor website: [registry.platformio.org](https://registry.platformio.org/platforms/platformio/linux_i686?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [Linux i686 platform repository](https://github.com/platformio/platform-linux_i686/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [hello-world](https://github.com/platformio/platform-linux_i686/tree/master/examples/hello-world?utm_source=platformio.org&utm_medium=docs)

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-linux_i686/releases) of the Linux i686 platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = linux_i686

; Specific version
[env:custom_stable]
platform = linux_i686@x.y.z
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-linux_i686.git
```

## Packages

| Name | Description |
|---|---|
| [toolchain-gcclinux32](https://registry.platformio.org/tools/platformio/toolchain-gcclinux32) | GCC Toolchain for Linux i686 machines |
