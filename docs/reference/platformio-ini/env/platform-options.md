<a id="projectconf-section-env-platform"></a>

# Platform options {#platform-options}

- [`platform`](./platform.md)
- [`platform_packages`](./platform-packages.md)
- [`framework`](./framework.md)
- [`board`](./board.md)
- [`board_build.mcu`](./board-build-mcu.md)
- [`board_build.f_cpu`](./board-build-f-cpu.md)
- [`board_build.ldscript`](./board-build-ldscript.md)

<a id="projectconf-board-more-options"></a>

## More options {#more-options}

You can override any board option declared in manifest file using the next format `board_{OBJECT.PATH}`, where `{OBJECT.PATH}` is an object path in JSON manifest. Please navigate to "boards" folder of [PlatfomIO development platforms](https://github.com/topics/platformio-platform) and open JSON file to list all available options.

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
