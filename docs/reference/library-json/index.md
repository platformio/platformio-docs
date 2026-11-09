# library.json {#library-json}

`library.json` is a manifest file of a library package. It allows developers to keep a project in its own structure and define:

- compatible frameworks and platforms
- external dependencies
- advanced build settings.

Information in `library.json` should be represented in [JSON-style](http://en.wikipedia.org/wiki/JSON) via [associative array](http://en.wikipedia.org/wiki/Associative_array) (name/value pairs). The order doesn't matter. The allowable fields (names from pairs) are described below.

You can validate `library.json` manifest file using the [pio pkg pack](../cli/pio-pkg/pack.md) command or [$schema](./schema.md).

- [`$schema`](./schema.md)

- [`name`](./name.md)

- [`version`](./version.md)

- [`description`](./description.md)

- [`keywords`](./keywords.md)

- [`homepage`](./homepage.md)

- [`repository`](./repository.md)

- [`authors`](./authors.md)

- [`license`](./license.md)

- [`frameworks`](./frameworks.md)

- [`platforms`](./platforms.md)

- [`headers`](./headers.md)

- [`examples`](./examples.md)

- [`dependencies`](./dependencies.md)

- [`export`](./export/index.md)

  - [`include`](./export/include.md)
  - [`exclude`](./export/exclude.md)

- [`scripts`](./scripts.md)

- [`build`](./build/index.md)

  - [`flags`](./build/flags.md)
  - [`unflags`](./build/unflags.md)
  - [`includeDir`](./build/includedir.md)
  - [`srcDir`](./build/srcdir.md)
  - [`srcFilter`](./build/srcfilter.md)
  - [`extraScript`](./build/extrascript.md)
  - [`libArchive`](./build/libarchive.md)
  - [`libLDFMode`](./build/libldfmode.md)
  - [`libCompatMode`](./build/libcompatmode.md)
  - [`builder`](./build/builder.md)
