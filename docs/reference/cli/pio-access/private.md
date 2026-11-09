<a id="cmd-access-private"></a>

# pio access private {#pio-access-private}

## Usage {#usage}

```bash
pio access private [OPTIONS] URN
```

## Description {#description}

Set a resource to be either privately accessible (restricted access to particular users or team members).

### Options {#options}

#### `--urn-type` {#cmdoption-pio-access-private-urn-type}

Resource type in [URN](https://en.wikipedia.org/wiki/Uniform_Resource_Name) form. Default is set to `prn:reg:pkg` which means to grant access to the package in the registry.

## Examples {#examples}

```bash
> pio access private prn:reg:pkg:8036:platform
The resource "prn:reg:pkg:8036:platform" has been successfully updated.
```

## See Also {#see-also}

- [pio access public](./public.md)
