<a id="cmd-pkg-unpublish"></a>

# pio pkg unpublish {#pio-pkg-unpublish}

## Usage {#usage}

```bash
pio pkg unpublish [<organization>/]<pkgname>[@<version>] [OPTIONS]
```

## Description {#description}

This removes a package version from the registry, deleting its entry and removing the tarball.

If no version is specified, or if all versions are removed then the root package entry is removed from the registry entirely.

You can only remove a package version within 72 hours from the published date.

## Options {#options}

### `--type` {#cmdoption-pio-pkg-unpublish-type}

Set the type of a package to unpublish (if you have packages with the same name). The default is set to the `library`. See supported [Package Types](./install.md#cmd-pkg-install-types).

### `--undo` {#cmdoption-pio-pkg-unpublish-undo}

Undo a remove, putting a version back into the registry.

## See Also {#see-also}

- [library.json](../../library-json/index.md)
- [pio pkg pack](./pack.md)
- [pio pkg publish](./publish.md)
