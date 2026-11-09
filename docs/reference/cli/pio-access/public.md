<a id="cmd-access-public"></a>

# pio access public {#pio-access-public}

## Usage {#usage}

```bash
pio access public [OPTIONS] URN
```

## Description {#description}

Set a resource to be either publicly accessible.

### Options {#options}

#### `--urn-type` {#cmdoption-pio-access-public-urn-type}

Resource type in [URN](https://en.wikipedia.org/wiki/Uniform_Resource_Name) form. Default is set to `prn:reg:pkg` which means to grant access to the package in the registry.

## Examples {#examples}

```bash
> pio access public prn:reg:pkg:8036:platform
The resource "prn:reg:pkg:8036:platform" has been successfully updated.
```

## See Also {#see-also}

- [pio access private](./private.md)
