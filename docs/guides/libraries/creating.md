<a id="library-creating"></a>

# Creating Library {#creating-library}

Managing components between the projects is a historical issue. A common code is duplicated between different projects that lead to project complexity. A good practice is to organize interdependent components as the separate libraries where other projects can depend on them.

PlatformIO has a built-in [Library Management](./index.md) where developers can declare project dependencies and PlatformIO will automatically manage them (install, build, update). It doesn't have any requirements for a library source code structure. The only requirement is a library manifest file - [library.json](../../reference/library-json/index.md), [library.properties](https://github.com/arduino/Arduino/wiki/Arduino-IDE-1.5:-Library-specification#library-metadata), or [module.json](http://docs.yottabuild.org/reference/module.html). It must be located in the root of a library.

We highly recommend using [library.json](../../reference/library-json/index.md) for better compatibility and avoiding any issues.

## Structure {#structure}

We recommend to use `src` folder for your C/C++ source files and `include` folder for your headers. You can also have nested sub-folders in `src` or `include`.

**Example**

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

A library package must contain a manifest. We recommend using [library.json](../../reference/library-json/index.md).

**Example**

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

## Publishing {#publishing}

You can publish a library to the [PlatformIO Registry](https://platformio.org/lib) using [pio pkg publish](../../reference/cli/pio-pkg/publish.md) command. Every time when you modify a source code of a library you will need to increment the "version" field in [library.json](../../reference/library-json/index.md) manifest and re-publish again.

If the published library has an issue and you would like to remove it from the PlatformIO Registry, please use [pio pkg unpublish](../../reference/cli/pio-pkg/unpublish.md) command.

## Examples {#examples}

See the published libraries in [PlatformIO Registry](https://platformio.org/lib).
