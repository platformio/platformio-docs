---
description: "Publish a package to the PlatformIO Registry so that it can be installed by name."
---

<a id="cmd-pkg-publish"></a>

# pio pkg publish {#pio-pkg-publish}

## Usage {#usage}

```bash
pio pkg publish [<source directory, tar.gz or zip>] [OPTIONS]
```

## Description {#description}

Publish a package to the [PlatformIO Registry](https://registry.platformio.org/) so that it can be installed by name. All files in the package directory are included if `export` field is not declared in a package manifest (for example, see [export](../../library-json/export/index.md)). The [next items](https://github.com/platformio/platformio-core/blob/develop/platformio/package/pack.py) are automatically excluded.

Check which files will be included in the final package using the [pio pkg pack](./pack.md) command.

Once a package is published with a given name and version, that specific name and version combination can never be used again, even if it is removed with the [pio pkg unpublish](./unpublish.md) command.

If no arguments are supplied, then PlatformIO packs the current package folder.

To list published packages, please use the [pio access list](../pio-access/list.md) command.

## Options {#options}

### `--owner` {#cmdoption-pio-pkg-publish-owner}

[PlatformIO Account](../../../get-started/platformio-account.md) username (can be organization username). The default is set to a username of the authorized [PlatformIO Account](../../../get-started/platformio-account.md).

### `--type` {#cmdoption-pio-pkg-publish-type}

Set a custom package type. See supported [Package Types](./install.md#cmd-pkg-install-types).

### `--released-at` {#cmdoption-pio-pkg-publish-released-at}

Custom release date and time in the next format (UTC): 2014-06-13 17:08:52

The permission to set custom release dates and times is only available in the [Enterprises](https://registry.platformio.org/pricing) plan.

### `--private` {#cmdoption-pio-pkg-publish-private}

Restrict access to a package (will not be available publicly). The default is to publish a package publicly.

Check [PlatformIO Registry Plans](https://registry.platformio.org/pricing) where private packages are allowed.

<a id="cmdoption-pio-pkg-publish-notify"></a>

### `--notify, --no-notify` {#cmdoption-pio-pkg-publish-no-notify}

Whether to send you an email when the registry has processed the package.
Default: `--notify`.

### `--no-interactive` {#cmdoption-pio-pkg-publish-no-interactive}

Do not show an interactive prompt.

## See also {#see-also}

- [library.json](../../library-json/index.md)
- [pio pkg pack](./pack.md)
- [pio access list](../pio-access/list.md)
- [pio pkg unpublish](./unpublish.md)
