---
description: Grant a user or a team access to a package in the PlatformIO Registry.
---

<a id="cmd-access-grant"></a>

# pio access grant {#pio-access-grant}

Grant a user or a team an access level to a resource.

## Usage {#usage}

```bash
pio access grant [OPTIONS] LEVEL <ORGNAME:TEAMNAME>|<USERNAME> URN
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `LEVEL` | The access level: `admin`, `maintainer` or `guest` (see below) |
| `ORGNAME:TEAMNAME` or `USERNAME` | The team (as `organization:team`) or the user to grant access to |
| `URN` | The resource, for example `prn:reg:pkg:8036:platform`. Find it with [`pio access list`](./list.md). |

Access levels:

| Level | Permissions |
| --- | --- |
| `admin` | All operations on the resource, including managing its access |
| `maintainer` | Read and write: update the resource, publish and unpublish versions. Cannot manage access. |
| `guest` | Read only. Granted to everyone automatically for public resources. |

## Options {#options}

### `--urn-type` {#cmdoption-pio-access-grant-urn-type}

The type of the resource URN. The only supported value, and the default, is
`prn:reg:pkg`: a package in the PlatformIO Registry.

## Examples {#examples}

Grant the user `bob` maintainer access to a package:

```bash
pio access grant maintainer bob prn:reg:pkg:8036:platform
```

```text
Access for resource "prn:reg:pkg:8036:platform" has been granted for "bob"
```

Grant the `developers` team of the `platformio` organization admin access to a
package:

```bash
pio access grant admin platformio:developers prn:reg:pkg:8036:platform
```

```text
Access for resource "prn:reg:pkg:8036:platform" has been granted for "platformio:developers"
```

## See also {#see-also}

- [`pio access revoke`](./revoke.md)
