---
description: Reference of library.json, the manifest of a PlatformIO library - metadata, dependencies, compatibility and build settings.
---

<a id="library-json-overview"></a>

# library.json {#library-json}

`library.json` is the manifest of a library package. Put it in the root folder
of the library to describe it and to control how PlatformIO uses it:

- metadata for the [PlatformIO Registry](https://registry.platformio.org):
  name, version, description, authors, license and links;
- compatibility: the frameworks and development platforms the library works
  with;
- dependencies on other packages;
- build settings: source folders, flags and Library Dependency Finder modes.

The file is a JSON object; the order of the fields does not matter. To check
it, run [`pio pkg pack`](../cli/pio-pkg/pack.md), or point your editor to the
[JSON schema](./schema.md).

## Fields {#fields}

| Field | Description |
| --- | --- |
| [`$schema`](./schema.md) | The JSON schema, for validation in editors |
| [`name`](./name.md) | The library name (required) |
| [`version`](./version.md) | The library version (required) |
| [`description`](./description.md) | A short description |
| [`keywords`](./keywords.md) | Keywords for searching the registry |
| [`homepage`](./homepage.md) | The library's home page |
| [`repository`](./repository.md) | The source code repository |
| [`authors`](./authors.md) | Authors and maintainers |
| [`license`](./license.md) | The license, as an SPDX expression |
| [`frameworks`](./frameworks.md) | Compatible frameworks |
| [`platforms`](./platforms.md) | Compatible development platforms |
| [`headers`](./headers.md) | The library's public header files |
| [`examples`](./examples.md) | Example projects |
| [`dependencies`](./dependencies.md) | Other packages the library depends on |
| [`export`](./export/index.md) | Files to [include](./export/include.md) in or [exclude](./export/exclude.md) from the package |
| [`scripts`](./scripts.md) | Scripts run after installation or before removal |
| [`build`](./build/index.md) | Build settings (see below) |

### Build settings {#build-settings}

| Field | Description |
| --- | --- |
| [`build.flags`](./build/flags.md) | Extra compiler and linker flags |
| [`build.unflags`](./build/unflags.md) | Flags to remove |
| [`build.includeDir`](./build/includedir.md) | The folder with header files |
| [`build.srcDir`](./build/srcdir.md) | The folder with source files |
| [`build.srcFilter`](./build/srcfilter.md) | Which source files to build |
| [`build.extraScript`](./build/extrascript.md) | An extra build script |
| [`build.libArchive`](./build/libarchive.md) | Build the library as a static archive |
| [`build.libLDFMode`](./build/libldfmode.md) | The Library Dependency Finder mode |
| [`build.libCompatMode`](./build/libcompatmode.md) | The library compatibility mode |
| [`build.builder`](./build/builder.md) | The builder for libraries in other formats |
