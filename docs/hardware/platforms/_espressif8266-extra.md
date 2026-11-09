## Configuration {#configuration}

### CPU Frequency {#cpu-frequency}

See [board_build.f_cpu](../../reference/platformio-ini/env/board-build-f-cpu.md) option from ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md)

```ini
[env:myenv]
; set frequency to 160MHz
board_build.f_cpu = 160000000L
```

### FLASH Frequency {#flash-frequency}

Please use `board_build.f_flash` option from ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) to change a value. Possible values:

- `20000000L`
- `26000000L`
- `40000000L` (default)
- `80000000L`

```ini
[env:myenv]
; set frequency to 80MHz
board_build.f_flash = 80000000L
```

### FLASH Mode {#flash-mode}

Flash chip interface mode. This parameter is stored in the binary image header, along with the flash size and flash frequency. The ROM bootloader in the ESP chip uses the value of these parameters in order to know how to talk to the flash chip.

Please use `board_build.flash_mode` option from ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) to change a value. Possible values:

- `qio`
- `qout`
- `dio`
- `dout`

```ini
[env:myenv]
board_build.flash_mode = qio
```

### Reset Method {#reset-method}

You can set custom reset method using [upload_resetmethod](../../reference/platformio-ini/env/upload-resetmethod.md) option from ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md).

The [possible values](https://github.com/igrr/esptool-ck#supported-boards) are:

- `ck` - RTS controls RESET or CH_PD, DTR controls GPIO0
- `wifio` - TXD controls GPIO0 via PNP transistor and DTR controls RESET via a capacitor
- `nodemcu` - GPIO0 and RESET controlled using two NPN transistors as in NodeMCU devkit.

See [default reset methods per board](https://github.com/platformio/platform-espressif8266/search?p=1&q=resetmethod).

```ini
[env:myenv]
upload_resetmethod = ck
```

<a id="platform-espressif-customflash"></a>

### Flash Size {#flash-size}

:::warning

Please make sure to read [ESP8266 Flash layout](https://arduino-esp8266.readthedocs.io/en/latest/filesystem.html#flash-layout) information first.

:::

Available LD-scripts: [https://github.com/esp8266/Arduino/tree/master/tools/sdk/ld](https://github.com/esp8266/Arduino/tree/master/tools/sdk/ld)

Please open `eagle.flash.***.ld` file to check how flash is split.

To override default LD script please use [board_build.ldscript](../../reference/platformio-ini/env/board-build-ldscript.md) option from ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md).

```ini
[env:myenv]
board_build.ldscript = eagle.flash.4m.ld
```

### Upload Speed {#upload-speed}

You can set custom upload speed using [upload_speed](../../reference/platformio-ini/env/upload-speed.md) option from ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md)

```ini
[env:myenv]
upload_speed = 9600
```

### lwIP Variant {#lwip-variant}

Available variants (macros):

- `-D PIO_FRAMEWORK_ARDUINO_LWIP2_LOW_MEMORY` v2 Lower Memory **(default)**
- `-D PIO_FRAMEWORK_ARDUINO_LWIP2_HIGHER_BANDWIDTH` v2 Higher Bandwidth
- `-D PIO_FRAMEWORK_ARDUINO_LWIP2_LOW_MEMORY_LOW_FLASH` v2 Lower Memory (no features)
- `-D PIO_FRAMEWORK_ARDUINO_LWIP2_HIGHER_BANDWIDTH_LOW_FLASH` v2 Higher Bandwidth (no features)
- `-D PIO_FRAMEWORK_ARDUINO_LWIP2_IPV6_LOW_MEMORY` v2 IPv6 Lower Memory
- `-D PIO_FRAMEWORK_ARDUINO_LWIP2_IPV6_HIGHER_BANDWIDTH` v2 IPv6 Higher Bandwidth
- `-D PIO_FRAMEWORK_ARDUINO_LWIP_HIGHER_BANDWIDTH` v1.4 Higher Bandwidth

You can change lwIP Variant by passing a custom macro using project [build_flags](../../reference/platformio-ini/env/build-flags.md).

For example, to switch to lwIP v1.4

```ini
[env:myenv]
...
build_flags = -D PIO_FRAMEWORK_ARDUINO_LWIP_HIGHER_BANDWIDTH
```

### SDK Version {#sdk-version}

Available versions (macros):

- `-D PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK305` NonOS SDK-3.0.5 (available since [Arduino core for ESP8266 3.1.0](https://github.com/esp8266/Arduino/releases/tag/3.1.0))
- `-D PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK3` NonOS SDK-pre-3.0 as of Jun 26, 2018 (removed in Arduino core for ESP8266 3.1.0)
- `-D PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK221` NonOS SDK v2.2.1 (legacy) as of Jun 8, 2018
- `-D PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK22x_190313` NonOS SDK v2.2.x branch as of Mar 13, 2019
- `-D PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK22x_190703` NonOS SDK v2.2.x branch as of Jul 03, 2019 **(default)**
- `-D PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK22x_191024` NonOS SDK v2.2.x branch as of Oct 24, 2019
- `-D PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK22x_191105` NonOS SDK v2.2.x branch as of to Nov 05, 2019
- `-D PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK22x_191122` NonOS SDK v2.2.x branch as of to Nov 22, 2019

You can change SDK version by passing a custom macro using project [build_flags](../../reference/platformio-ini/env/build-flags.md).

For example, to switch to SDK-pre-3.0:

```ini
[env:myenv]
...
build_flags = -D PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK3
```

### SSL Support {#ssl-support}

By default, all SSL ciphers (most compatible) are supported.

You can control SSL support passing a custom macro using project [build_flags](../../reference/platformio-ini/env/build-flags.md).

For example, use basic SSL ciphers (lower ROM use):

```ini
[env:myenv]
...
build_flags = -D BEARSSL_SSL_BASIC
```

<a id="platform-espressif8266-serial-debug"></a>

### Serial Debug {#serial-debug}

Please use the next [build_flags](../../reference/platformio-ini/env/build-flags.md) to enable Serial debug:

```ini
[env:myenv]
...
build_flags = -DDEBUG_ESP_PORT=Serial

; or for Serial1
build_flags = -DDEBUG_ESP_PORT=Serial1
```

### Debug Level {#debug-level}

Please use one of the next [build_flags](../../reference/platformio-ini/env/build-flags.md) to change debug level. A [build_flags](../../reference/platformio-ini/env/build-flags.md) option could be used only the one time per build environment. If you need to specify more flags, please separate them with a new line or space.

Also, please note that you will need to extend [build_flags](../../reference/platformio-ini/env/build-flags.md) with [Serial Debug](/hardware/platforms/espressif8266#platform-espressif8266-serial-debug) macro. For example, `build_flags = -DDEBUG_ESP_PORT=Serial -DDEBUG_ESP_SSL ...`.

Actual information is available in [Arduino for ESP8266 Board Manifest](https://github.com/esp8266/Arduino/blob/master/boards.txt#L286). Please scroll to `generic.menu.lvl` section.

```ini
[env:myenv]
platform = ...
board = ...
framework = arduino

;;;;; Possible options ;;;;;;

; SSL
build_flags = -DDEBUG_ESP_SSL

; TLS_MEM
build_flags = -DDEBUG_ESP_TLS_MEM

; HTTP_CLIENT
build_flags = -DDEBUG_ESP_HTTP_CLIENT

; HTTP_SERVER
build_flags = -DDEBUG_ESP_HTTP_SERVER

; SSL+TLS_MEM
build_flags =
  -DDEBUG_ESP_SSL
  -DDEBUG_ESP_TLS_MEM

; SSL+HTTP_CLIENT
build_flags =
  -DDEBUG_ESP_SSL
  -DDEBUG_ESP_HTTP_CLIENT

; SSL+HTTP_SERVER
build_flags =
  -DDEBUG_ESP_SSL
  -DDEBUG_ESP_HTTP_SERVER

; TLS_MEM+HTTP_CLIENT
build_flags =
  -DDEBUG_ESP_TLS_MEM
  -DDEBUG_ESP_HTTP_CLIENT

; TLS_MEM+HTTP_SERVER
build_flags =
  -DDEBUG_ESP_TLS_MEM
  -DDEBUG_ESP_HTTP_SERVER

; HTTP_CLIENT+HTTP_SERVER
build_flags =
  -DDEBUG_ESP_HTTP_CLIENT
  -DDEBUG_ESP_HTTP_SERVER

; SSL+TLS_MEM+HTTP_CLIENT
build_flags =
  -DDEBUG_ESP_SSL
  -DDEBUG_ESP_TLS_MEM
  -DDEBUG_ESP_HTTP_CLIENT

; SSL+TLS_MEM+HTTP_SERVER
build_flags =
  -DDEBUG_ESP_SSL
  -DDEBUG_ESP_TLS_MEM
  -DDEBUG_ESP_HTTP_SERVER

; SSL+HTTP_CLIENT+HTTP_SERVER
build_flags =
  -DDEBUG_ESP_SSL
  -DDEBUG_ESP_HTTP_CLIENT
  -DDEBUG_ESP_HTTP_SERVER

; TLS_MEM+HTTP_CLIENT+HTTP_SERVER
build_flags =
  -DDEBUG_ESP_TLS_MEM
  -DDEBUG_ESP_HTTP_CLIENT
  -DDEBUG_ESP_HTTP_SERVER

; SSL+TLS_MEM+HTTP_CLIENT+HTTP_SERVER
build_flags =
  -DDEBUG_ESP_SSL
  -DDEBUG_ESP_TLS_MEM
  -DDEBUG_ESP_HTTP_CLIENT
  -DDEBUG_ESP_HTTP_SERVER

; CORE
build_flags = -DDEBUG_ESP_CORE

; WIFI
build_flags = -DDEBUG_ESP_WIFI

; HTTP_UPDATE
build_flags = -DDEBUG_ESP_HTTP_UPDATE

; UPDATER
build_flags = -DDEBUG_ESP_UPDATER

; OTA
build_flags = -DDEBUG_ESP_OTA

; OOM
build_flags =
  -DDEBUG_ESP_OOM
  -include "umm_malloc/umm_malloc_cfg.h"

; CORE+WIFI+HTTP_UPDATE+UPDATER+OTA+OOM
build_flags =
  -DDEBUG_ESP_CORE
  -DDEBUG_ESP_WIFI
  -DDEBUG_ESP_HTTP_UPDATE
  -DDEBUG_ESP_UPDATER
  -DDEBUG_ESP_OTA
  -DDEBUG_ESP_OOM -include "umm_malloc/umm_malloc_cfg.h"

; SSL+TLS_MEM+HTTP_CLIENT+HTTP_SERVER+CORE+WIFI+HTTP_UPDATE+UPDATER+OTA+OOM
build_flags =
  -DDEBUG_ESP_SSL
  -DDEBUG_ESP_TLS_MEM
  -DDEBUG_ESP_HTTP_CLIENT
  -DDEBUG_ESP_HTTP_SERVER
  -DDEBUG_ESP_CORE
  -DDEBUG_ESP_WIFI
  -DDEBUG_ESP_HTTP_UPDATE
  -DDEBUG_ESP_UPDATER
  -DDEBUG_ESP_OTA
  -DDEBUG_ESP_OOM -include "umm_malloc/umm_malloc_cfg.h"

; NoAssert-NDEBUG
build_flags = -DNDEBUG
```

### VTables {#vtables}

Please use one of the next [build_flags](../../reference/platformio-ini/env/build-flags.md):

```ini
[env:myenv]
...

; Flash (default)
build_flags = -DVTABLES_IN_FLASH

; Heap
build_flags = -DVTABLES_IN_DRAM

; IRAM
build_flags = -DVTABLES_IN_IRAM
```

### MMU - Adjusting ICACHE to IRAM ratio {#mmu-adjusting-icache-to-iram-ratio}

By default the balanced ratio (32KB cache + 32KB IRAM) configuration is used. Alternative configurations can be enabled using the [build_flags](../../reference/platformio-ini/env/build-flags.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md):

**MMU Configuration Options**

| Name | Description |
|---|---|
| `PIO_FRAMEWORK_ARDUINO_MMU_CACHE16_IRAM48` | 16KB cache + 48KB IRAM (IRAM) |
| `PIO_FRAMEWORK_ARDUINO_MMU_CACHE16_IRAM48_SECHEAP_SHARED` | 16KB cache + 48KB IRAM and 2nd Heap (shared) |
| `PIO_FRAMEWORK_ARDUINO_MMU_CACHE16_IRAM32_SECHEAP_NOTSHARED` | 16KB cache + 32KB IRAM + 16KB 2nd Heap (not shared) |
| `PIO_FRAMEWORK_ARDUINO_MMU_EXTERNAL_128K` | 128K External 23LC1024 |
| `PIO_FRAMEWORK_ARDUINO_MMU_EXTERNAL_1024K` | 1M External 64 MBit PSRAM |
| `PIO_FRAMEWORK_ARDUINO_MMU_CUSTOM` | Disables default configuration and expects user-specified flags |

Examples:

```ini
[env:espduino]
platform = espressif8266
framework = arduino
board = espduino
build_flags =
    -D PIO_FRAMEWORK_ARDUINO_MMU_CACHE16_IRAM48

[env:espino]
platform = espressif8266
framework = arduino
board = espino
build_flags =
    -D PIO_FRAMEWORK_ARDUINO_MMU_CACHE16_IRAM32_SECHEAP_NOTSHARED

[env:d1_mini]
platform = espressif8266
framework = arduino
board = d1_mini
build_flags =
    -D PIO_FRAMEWORK_ARDUINO_MMU_CUSTOM
    -D MMU_IRAM_SIZE=0xC000
    -D MMU_ICACHE_SIZE=0x4000
    -D MMU_IRAM_HEAP
```

More detailed information on this matter can be found in the [official documentation](https://arduino-esp8266.readthedocs.io/en/latest/mmu.html).

### Exceptions {#exceptions}

Exceptions are disabled by default. To enable exceptions, use the `PIO_FRAMEWORK_ARDUINO_ENABLE_EXCEPTIONS` macro in [build_flags](../../reference/platformio-ini/env/build-flags.md). That macro will add the `-fexceptions` flag and will link the final firmware against the `stdc++-exc` library with enabled exceptions. For example:

```ini
[env:myenv]
...

; Enable exceptions
build_flags = -D PIO_FRAMEWORK_ARDUINO_ENABLE_EXCEPTIONS
```

<a id="platform-espressif-uploadfs"></a>

### Using Filesystem {#using-filesystem}

#### Selecting appropriate Filesystem {#selecting-appropriate-filesystem}

There are two file systems for utilizing the on-board flash on the ESP8266: `SPIFFS` and `LittleFS`. They provide a compatible API but have incompatible on-flash implementations, so it is important to choose one or the other per project as attempting to mount a SPIFFS volume under LittleFS may result in a format operation and definitely will not preserve any files, and vice-versa.

:::warning

SPIFFS is currently deprecated and may be removed in future releases of the core. Please consider moving your code to LittleFS.

:::

The `SPIFFS` file system is used by default in order to keep legacy project compatible. To choose `LittleFS` as the file system, it should be explicitly specified using `board_build.filesystem` option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md), for example:

```ini
[env:myenv]
platform = espressif8266
framework = arduino
board = ...
board_build.filesystem = littlefs
```

More information about pros and cons of each file system can be found in [the official documentation](https://arduino-esp8266.readthedocs.io/en/latest/filesystem.html#filesystem).

#### Uploading files to Filesystem {#uploading-files-to-filesystem}

:::warning

Please make sure to read [ESP8266 Flash layout](https://arduino-esp8266.readthedocs.io/en/latest/filesystem.html#flash-layout) information first.

:::

1. Create a new project using [PlatformIO IDE](../../get-started/platformio-ide.md) or initialize project using [PlatformIO Core (CLI)](../../get-started/platformio-core.md) and [pio project init](../../reference/cli/pio-project/init.md) (if you have not initialized it yet)
2. Create the `data` folder (it should be on the same level as the `src` folder) and put files there. Also, you can specify your own location for [data_dir](../../reference/platformio-ini/platformio/data-dir.md)
3. Run the "Upload File System image" task in [PlatformIO IDE](../../get-started/platformio-ide.md) or use [PlatformIO Core (CLI)](../../get-started/platformio-core.md) and the [`pio run --target`](../../reference/cli/pio-run.md#cmdoption-pio-run-t) command with the `uploadfs` target.

To upload file system image using OTA update please specify `upload_port` / `--upload-port` as IP address or mDNS host name (ending with the `*.local`). For the details please follow to [Over-the-Air (OTA) update](/hardware/platforms/espressif8266#platform-espressif-ota).

By default, will be used default LD Script for the board where is specified file system offsets (start, end, page, block). You can override it using [Flash Size](/hardware/platforms/espressif8266#platform-espressif-customflash).

Active discussion is located in [issue #382](https://github.com/platformio/platformio-core/issues/382).

#### Overriding Filesystem image name {#overriding-filesystem-image-name}

By default, the image file name is set according to the used file system: `spiffs.bin` or `littlefs.bin`. You can change the file name using [a PRE extra script](../../reference/scripting-api/actions.md), for example:

```ini
[env:d1]
platform = espressif8266
framework = arduino
board = d1
board_build.filesystem = littlefs
extra_scripts =
    pre:extra_script.py
```

Where a special variable `ESP8266_FS_IMAGE_NAME` can be overridden:

```python
Import("env")
env.Replace(ESP8266_FS_IMAGE_NAME="custom_image_name")
```

<a id="platform-espressif-ota"></a>

### Over-the-Air (OTA) update {#over-the-air-ota-update}

:::warning

Please make sure to read the theory behind the OTA updates in the [What is OTA? How to use it?](https://arduino-esp8266.readthedocs.io/en/latest/ota_updates/readme.html) article first.

:::

1. Create a new project using [PlatformIO Home](../../get-started/platformio-home.md) or initialize a project via [PlatformIO Core (CLI)](../../get-started/platformio-core.md) and [pio project init](../../reference/cli/pio-project/init.md) (if you have not initialized it yet)
2. Copy the [basicOTA](https://github.com/esp8266/Arduino/blob/master/libraries/ArduinoOTA/examples/BasicOTA/BasicOTA.ino) example to [src_dir](../../reference/platformio-ini/platformio/src-dir.md) and configure your WiFi credentials (SSID and password).
3. Compile the project to ensure there are no syntax errors in the code.

To upload the binary you can either specify the upload address directly in the CLI command using the [`pio run --upload-port`](../../reference/cli/pio-run.md#cmdoption-pio-run-upload-port) option:

```bash
pio run --target upload --upload-port IP_ADDRESS_HERE or mDNS_NAME.local
```

For example:

```text
pio run -t upload --upload-port 192.168.0.255
pio run -t upload --upload-port myesp8266.local
```

Or use the `upload_port` option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md). Please note that you also need to set [upload_protocol](../../reference/platformio-ini/env/upload-protocol.md) to `espota`:

```ini
[env:myenv]
upload_protocol = espota
upload_port = IP_ADDRESS_HERE or mDNS_NAME.local
```

For example:

```ini
[env:myenv]
platform = espressif8266
board = nodemcuv2
framework = arduino
upload_protocol = espota
upload_port = 192.168.0.255
```

#### Authentication and upload options {#authentication-and-upload-options}

You can pass additional options/flags to OTA uploader using `upload_flags` option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md)

```ini
[env:myenv]
upload_protocol = espota
; each flag in a new line
upload_flags =
  --port=8266
```

Available flags

- `--port=ESP_PORT` ESP8266 OTA Port. Default 8266
- `--auth=AUTH` Set authentication password
- `--spiffs` Use this option to transmit a SPIFFS image and do not flash the module

For the full list with available options please run

```bash
~/.platformio/packages/framework-arduinoespressif8266/tools/espota.py --help

Usage: espota.py [options]

Transmit image over the air to the esp8266 module with OTA support.

Options:
  -h, --help            show this help message and exit

  Destination:
    -i ESP_IP, --ip=ESP_IP
                        ESP8266 IP Address.
    -I HOST_IP, --host_ip=HOST_IP
                        Host IP Address.
    -p ESP_PORT, --port=ESP_PORT
                        ESP8266 ota Port. Default 8266
    -P HOST_PORT, --host_port=HOST_PORT
                        Host server ota Port. Default random 10000-60000

  Authentication:
    -a AUTH, --auth=AUTH
                        Set authentication password.

  Image:
    -f FILE, --file=FILE
                        Image file.
    -s, --spiffs        Use this option to transmit a SPIFFS image and do not
                        flash the module.

  Output:
    -d, --debug         Show debug output. And override loglevel with debug.
    -r, --progress      Show progress output. Does not work for ArduinoIDE
```

### Using Arduino Framework with Staging version {#using-arduino-framework-with-staging-version}

PlatformIO will install the latest Arduino Core for ESP8266 from [https://github.com/esp8266/Arduino](https://github.com/esp8266/Arduino). The [Git](https://git-scm.com) should be installed in a system. To update Arduino Core to the latest revision, please open [PlatformIO IDE](../../get-started/platformio-ide.md) and navigate to `PlatformIO Home > Platforms > Updates`.

1. Please install [PlatformIO IDE](../../get-started/platformio-ide.md)

2. Initialize a new project, open ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) and specify the link to the framework repository in [platform_packages](../../reference/platformio-ini/env/platform-packages.md) section. For example,

   ```ini
   [env:nodemcuv2]
   platform = espressif8266
   board = nodemcuv2
   framework = arduino
   platform_packages =
       platformio/framework-arduinoespressif8266 @ https://github.com/esp8266/Arduino.git
   ```

3. Try to build the project

4. If you see build errors, then try to build this project using the same `stage` with Arduino IDE

5. If it works with Arduino IDE but doesn't work with PlatformIO, then please [file a new issue](https://github.com/platformio/platform-espressif8266/issuess) with attached information:

   - test project/files
   - detailed log of build process from Arduino IDE (please copy it from console to [https://hastebin.com](https://hastebin.com))
   - detailed log of build process from PlatformIO Build System (please copy it from console to [https://hastebin.com](https://hastebin.com))
