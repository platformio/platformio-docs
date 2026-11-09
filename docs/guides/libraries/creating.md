---
description: Structure, manifest and publishing of a PlatformIO library.
---

<a id="library-creating"></a>

# Create a library {#creating-library}

Move code you share between projects into a library: other projects can then
depend on it, and PlatformIO installs, builds and updates it for them.

A library needs only one thing: a manifest in its root folder. PlatformIO
reads [`library.json`](../../reference/library-json/index.md), and also the
Arduino [`library.properties`](https://arduino.github.io/arduino-cli/latest/library-specification/#libraryproperties-file-format)
and the legacy `module.json`. Use `library.json`: it supports all PlatformIO
features, such as dependencies and build settings.

## Structure {#structure}

Put source files in `src` and public headers in `include`; both can contain
subfolders. Put example projects in `examples`.

```text
├── examples
│   └── echo
├── include
│   └── HelloWorld.h
├── library.json
└── src
    └── HelloWorld.cpp
```

## Manifest {#manifest}

A minimal `library.json` with metadata, dependencies and compatibility:

```javascript
{
  "name": "HelloWorld",
  "version": "1.0.0",
  "description": "A \"Hello world\" program is a computer program that outputs \"Hello World\" (or some variant) on a display device",
  "keywords": "planet, happiness, people",
  "repository":
  {
    "type": "git",
    "url": "https://github.com/username/hello-world.git"
  },
  "authors":
  [
    {
      "name": "John Smith",
      "email": "me@john-smith.com",
      "url": "https://www.john-smith/contact"
    },
    {
      "name": "Andrew Smith",
      "email": "me@andrew-smith.com",
      "url": "https://www.andrew-smith/contact",
      "maintainer": true
    }
  ],
  "license": "MIT",
  "homepage": "https://www.helloworld.org/",
  "dependencies": {
    "ownername/print": "~1.3.0"
  },
  "frameworks": "*",
  "platforms": "*"
}
```

See the [`library.json` reference](../../reference/library-json/index.md) for
all fields. To check the manifest and see which files go into the package, run
[`pio pkg pack`](../../reference/cli/pio-pkg/pack.md).

## Publish {#publishing}

Publish the library to the [PlatformIO Registry](https://registry.platformio.org)
with [`pio pkg publish`](../../reference/cli/pio-pkg/publish.md). You need a
[PlatformIO Account](../../get-started/platformio-account.md).

Each published version is immutable: to publish changes, increase `version` in
`library.json` and publish again. To remove a version, use
[`pio pkg unpublish`](../../reference/cli/pio-pkg/unpublish.md).

## Examples {#examples}

Browse the libraries in the [PlatformIO Registry](https://registry.platformio.org/search?t=library)
to see how others structure them.
