---
description: Make a package in the PlatformIO Registry public.
---

<a id="cmd-access-public"></a>

# pio access public {#pio-access-public}

Make a resource public. Anyone can find and use it.

## Usage {#usage}

```bash
pio access public [OPTIONS] URN
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `URN` | The resource, for example `prn:reg:pkg:8036:platform`. Find it with [`pio access list`](./list.md). |

## Options {#options}

### `--urn-type` {#cmdoption-pio-access-public-urn-type}

The type of the resource URN. The only supported value, and the default, is
`prn:reg:pkg`: a package in the PlatformIO Registry.

## Examples {#examples}

```bash
pio access public prn:reg:pkg:8036:platform
```

```text
The resource "prn:reg:pkg:8036:platform" has been successfully updated.
```

## See also {#see-also}

- [`pio access private`](./private.md)
