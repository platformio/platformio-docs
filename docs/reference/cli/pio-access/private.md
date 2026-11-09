---
description: Make a package in the PlatformIO Registry private.
---

<a id="cmd-access-private"></a>

# pio access private {#pio-access-private}

Make a resource private. Only users and teams you grant access to can use it.

## Usage {#usage}

```bash
pio access private [OPTIONS] URN
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `URN` | The resource, for example `prn:reg:pkg:8036:platform`. Find it with [`pio access list`](./list.md). |

## Options {#options}

### `--urn-type` {#cmdoption-pio-access-private-urn-type}

The type of the resource URN. The only supported value, and the default, is
`prn:reg:pkg`: a package in the PlatformIO Registry.

## Examples {#examples}

```bash
pio access private prn:reg:pkg:8036:platform
```

```text
The resource "prn:reg:pkg:8036:platform" has been successfully updated.
```

## See also {#see-also}

- [`pio access public`](./public.md)
