---
description: List the PlatformIO Registry packages you can access and your access level.
---

<a id="cmd-access-list"></a>

# pio access list {#pio-access-list}

List the resources (packages) that you, or a given owner, can access, with
the access level. Public resources with read-only access are not listed.

## Usage {#usage}

```bash
pio access list [OPTIONS] [OWNER]
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `OWNER` | Optional. List only the resources of this owner (a user or an organization name). |

## Options {#options}

### `--urn-type` {#cmdoption-pio-access-list-urn-type}

The type of the resource URN. The only supported value, and the default, is
`prn:reg:pkg`: packages in the PlatformIO Registry.

### `--json-output` {#cmdoption-pio-access-list-json-output}

Print the result in [JSON](https://en.wikipedia.org/wiki/JSON) format.

## Examples {#examples}

List all resources you can access:

```bash
pio access list
```

```text
...

atmelsam
--------
URN:              prn:reg:pkg:8007:platform
Owner:            platformio
Access level(s):  Admin

espressif8266
-------------
URN:              prn:reg:pkg:8008:platform
Owner:            platformio
Access level(s):  Admin

chipsalliance
-------------
URN:              prn:reg:pkg:8036:platform
Owner:            platformio
Access level(s):  Admin

contrib-piohome
---------------
URN:              prn:reg:pkg:8037:tool
Owner:            platformio
Access level(s):  Admin

...
```

List the resources of the `platformio` owner:

```bash
pio access list platformio
```

```text
...

tool-scons
----------
URN:              prn:reg:pkg:8192:tool
Owner:            platformio
Access level(s):  Admin

tool-simavr
-----------
URN:              prn:reg:pkg:8193:tool
Owner:            platformio
Access level(s):  Admin

...
```
