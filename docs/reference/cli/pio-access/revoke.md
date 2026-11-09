---
description: Revoke a user's or a team's access to a package in the PlatformIO Registry.
---

<a id="cmd-access-revoke"></a>

# pio access revoke {#pio-access-revoke}

Revoke a user's or a team's access to a resource.

## Usage {#usage}

```bash
pio access revoke [OPTIONS] <ORGNAME:TEAMNAME>|<USERNAME> URN
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `ORGNAME:TEAMNAME` or `USERNAME` | The team (as `organization:team`) or the user whose access to revoke |
| `URN` | The resource, for example `prn:reg:pkg:8036:platform`. Find it with [`pio access list`](./list.md). |

## Options {#options}

### `--urn-type` {#cmdoption-pio-access-revoke-urn-type}

The type of the resource URN. The only supported value, and the default, is
`prn:reg:pkg`: a package in the PlatformIO Registry.

## Examples {#examples}

Revoke the access of the user `bob`:

```bash
pio access revoke bob prn:reg:pkg:8036:platform
```

```text
Access for resource "prn:reg:pkg:8036:platform" has been revoked for "bob"
```

Revoke the access of the `developers` team of the `platformio` organization:

```bash
pio access revoke platformio:developers prn:reg:pkg:8036:platform
```

```text
Access for resource "prn:reg:pkg:8036:platform" has been revoked for "platformio:developers"
```

## See also {#see-also}

- [`pio access grant`](./grant.md)
