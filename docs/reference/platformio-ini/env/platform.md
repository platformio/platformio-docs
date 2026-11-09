---
description: "A name or specification of development platform (platformio.ini option platform)."
---

# `platform`

- **Type:** String
- **Multiple values:** No

Specify a development platform that provides integration of vendor-specific boards (development kits, MCUs), high-level frameworks, and SDKs. See [Package Specifications](../../cli/pio-pkg/install.md#cmd-pkg-install-specifications) for details.

[PlatformIO Registry](https://registry.platformio.org) allows you to explore supported development platforms, boards, frameworks, and toolchains.

For the advanced platform configuration, please check the [Development Platforms](../../../hardware/platforms/index.md) documentation.

Example of using a [Espressif 32 development platform](https://registry.platformio.org/platforms/platformio/espressif32):

```ini
[env:recommended_specification]
; allow backwards-compatible new functionality and bug-fixes
platform = platformio/espressif32@^6.1.0

[env:allow_only_bug_fixes]
platform = platformio/espressif32@~6.1.0

[env:exact_version]
platform = platformio/espressif32@6.1.0

[env:latest_version]
; not recommended as it does not ensure that
; - builds are repeatable
; - all developers who checkout the project will build against the same platform version
platform = platformio/espressif32

[env:development_verion_by_git]
platform = https://github.com/platformio/platform-espressif32.git

[env:custom_git_branch]
platform = https://github.com/platformio/platform-espressif32.git#master

[env:specific_git_commit]
platform = https://github.com/platformio/platform-espressif32.git#f8340a2081a31c2ac8ed2b16907f2a21dc8897d4
```

:::note

We highly recommend pinning the platform to a version. See [Version Requirements](../../cli/pio-pkg/install.md#cmd-pkg-install-requirements) for details.

:::
