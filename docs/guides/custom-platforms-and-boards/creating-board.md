---
description: "Please take a look at the source code of PlatformIO Development Platforms and navigate to boards folder of the repository."
---

# Custom embedded boards

*PlatformIO* has pre-built settings for many popular embedded boards. The list of these boards is available as a web page at [PlatformIO Boards Explorer](https://platformio.org/boards) or through the CLI command [pio boards](../../reference/cli/pio-boards.md).

Custom boards can also be defined from scratch or by overriding settings of existing boards. All data is declared using the [JSON syntax](http://en.wikipedia.org/wiki/JSON) via [associative array](http://en.wikipedia.org/wiki/Associative_array) name/value pairs.

## JSON structure {#json-structure}

The key fields are:

- `build` data is handed over to the [Development Platforms](../../hardware/platforms/index.md) and [Frameworks](../../hardware/frameworks/index.md) builders
- `frameworks` is the list with supported [Frameworks](../../hardware/frameworks/index.md). Each working environment for each project that uses the board will choose one of the frameworks declared here.
- `platform` name of [Development Platforms](../../hardware/platforms/index.md)
- `upload` upload settings which depend on the `platform`

For details, see existing boards as examples, available under `.platformio/platforms/*/boards/`.

```json
{
  "build": {
    "extra_flags": "-DHELLO_PLATFORMIO",
    "f_cpu": "16000000L",
    "hwids": [
      [
        "0x1234",
        "0x0013"
      ],
      [
        "0x4567",
        "0x0013"
      ]
    ],
    "mcu": "%MCU_TYPE_HERE%"
  },
  "frameworks": ["%LIST_WITH_SUPPORTED_FRAMEWORKS%"],
  "platforms": ["%LIST_WITH_COMPATIBLE_PLATFORMS%"],
  "name": "My Test Board",
  "upload": {
    "maximum_ram_size": 2048,
    "maximum_size": 32256
  },
  "url": "http://example.com",
  "vendor": "MyCompany"
}
```

## Installation {#installation}

1. Create `boards` directory in [core_dir](../../reference/platformio-ini/platformio/core-dir.md) if it doesn't exist.
2. Create `myboard.json` file in this `boards` directory.
3. Search available boards via [pio boards](../../reference/cli/pio-boards.md) command. You should see `myboard` board.

Now, you can use `myboard` for the [board](../../reference/platformio-ini/env/board.md) option in [`platformio.ini`](../../reference/platformio-ini/index.md).

:::note

You can have custom boards per project. In this case, please put your board's JSON files to [boards_dir](../../reference/platformio-ini/platformio/boards-dir.md).

:::

## Examples {#examples}

Please take a look at the source code of [PlatformIO Development Platforms](https://github.com/platformio?query=platform-) and navigate to `boards` folder of the repository.
