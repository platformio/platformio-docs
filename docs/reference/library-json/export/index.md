<a id="manifest-library-json-export"></a>

# `export` {#export}

*Optional* | Type: `Object`

This option is useful if you need to exclude extra data (test code, docs, images, PDFs, etc). It allows one to reduce the size of the final archive.

To check which files will be included in the final packages, please use [pio pkg pack](../../cli/pio-pkg/pack.md) command.

Possible options:

- [`include`](./include.md)
- [`exclude`](./exclude.md)
