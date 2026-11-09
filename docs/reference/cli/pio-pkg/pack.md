---
description: "Create a tarball from a package (library, Development Platforms, or tool)."
---

# pio pkg pack

## Usage {#usage}

```bash
pio pkg pack [<source directory, tar.gz or zip>] [OPTIONS]
```

## Description {#description}

Create a tarball from a package (library, [Development Platforms](../../../hardware/platforms/index.md), or tool). If no arguments are supplied, then platformio packs the current package folder.

A source of a package must contain a manifest (should be located in a root of a package) depending on a package type:

<dl>

<dt>

Library

</dt>

<dd>

A [library.json](../../library-json/index.md) is a manifest file of a library package.

</dd>

<dt>

Platform

</dt>

<dd>

A `platform.json` is a manifest file of a development platform package. See [Manifest File platform.json](../../../guides/custom-platforms-and-boards/creating-platform.md#platform-creating-manifest-file).

</dd>

<dt>

Tool

</dt>

<dd>

A `package.json` is a manifest file of a tool package. It is intended for toolchains, flashers, debugging servers, simulators, and other tools.

</dd>

</dl>

See a [manifest validation scheme](https://github.com/platformio/platformio-core/blob/develop/platformio/package/manifest/schema.py).

## Options {#options}

<a id="cmdoption-pio-pkg-pack-output"></a>

### `-o, --output` {#cmdoption-pio-pkg-pack-o}

Specify a destination path (folder or a full path to file) where to store a tarball. The default is to create a tarball in the current working directory.

## Files included in package {#files-included-in-package}

All files are included by default, with the following exceptions:

- Certain files that are relevant to package installation and distribution are always included. For example, `library.json`, `README.md`, `LICENSE`, etc.
- If the [export](../../library-json/export/index.md) field is not declared in the manifest, the [next default filters](https://github.com/platformio/platformio-core/blob/develop/platformio/package/pack.py#L35) will be applied
- If the [export](../../library-json/export/index.md) field is not declared in the manifest and there is a `.gitignore` file, then ignored files in that and all child directories will be excluded from the package.

## See also {#see-also}

- [library.json](../../library-json/index.md)
- [pio pkg publish](./publish.md)
