---
description: "A list of dependent libraries that will be automatically installed."
---

# `dependencies`

- **Required:** No
- **Type:** Array or object

A list of dependent libraries that will be automatically installed.

Allowed requirements for dependent library:

- `owner` | Type: `String` – an owner name (username) from the [PlatformIO Registry](https://registry.platformio.org)
- `name` | Type: `String` – library name
- `version` | Type: `String` – [Version Requirements](../cli/pio-pkg/install.md#cmd-pkg-install-requirements) or [Package Specifications](../cli/pio-pkg/install.md#cmd-pkg-install-specifications)
- `frameworks` | Type: `String` or `Array` – project compatible [Frameworks](../../hardware/frameworks/index.md)
- `platforms` | Type: `String` or `Array` – project compatible [Development Platforms](../../hardware/platforms/index.md)

## Example

```javascript
"dependencies":
{
    "bblanchon/ArduinoJson": "^6.16.1",
    "me-no-dev/AsyncTCP": "*",
    "external-repo": "https://github.com/user/package.git#1.2.3",
    "external-zip": "https://github.com/me-no-dev/AsyncTCP/archive/master.zip"
}
```

More advanced usage:

```javascript
"dependencies":
[
    {
        "owner": "bblanchon",
        "name": "ArduinoJson",
        "version": "^6.16.1"
    },
    {
        "owner": "me-no-dev",
        "name": "AsyncTCP",
        "version": "*",
        "platforms": ["espressif32"]
    },
    {
        "name": "external-repo",
        "version": "https://github.com/user/package.git#1.2.3"
    },
    {
        "name": "external-zip",
        "version": "https://github.com/me-no-dev/AsyncTCP/archive/master.zip"
    }
]
```
