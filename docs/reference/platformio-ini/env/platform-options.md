---
description: Platform options of the platformio.ini [env] section.
---

# Platform options

Select the development platform, framework and board, and override board settings.

| Option | Description |
| --- | --- |
| [`platform`](./platform.md) | A name or specification of development platform |
| [`platform_packages`](./platform-packages.md) | Custom packages and specifications |
| [`framework`](./framework.md) | A list of project dependent frameworks |
| [`board`](./board.md) | A board ID |
| [`board_build.mcu`](./board-build-mcu.md) | A custom board MCU |
| [`board_build.f_cpu`](./board-build-f-cpu.md) | A custom MCU frequency |
| [`board_build.f_flash`](./board-build-f-flash.md) | A custom flash frequency |
| [`board_build.flash_mode`](./board-build-flash-mode.md) | A custom flash mode |
| [`board_build.ldscript`](./board-build-ldscript.md) | A custom linker script |

Board settings not listed here can also be overridden: see [More options](#more-options).

<a id="projectconf-board-more-options"></a>

## More options {#more-options}

You can override any setting of the board's JSON manifest with an option named `board_<object.path>`, where `<object.path>` is the setting's path in the manifest. The manifests are in the `boards` folder of each [development platform](https://github.com/topics/platformio-platform) repository.

For example, [Manifest: Espressif ESP32 Dev Module](https://github.com/platformio/platform-espressif32/blob/develop/boards/esp32dev.json):

```ini
[env:custom_board_options]
; Custom CPU Frequency
board_build.f_cpu = 160000000L

; Custom FLASH Frequency
board_build.f_flash = 80000000L

; Custom FLASH Mode
board_build.flash_mode = qio

; Custom linker script
board_build.ldscript = /path/to/ldscript.ld

; Custom maximum program size
board_upload.maximum_size = 1310720
```
