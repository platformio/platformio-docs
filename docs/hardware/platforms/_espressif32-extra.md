## Tutorials {#tutorials}

- [Get started with Arduino and ESP32-DevKitC: debugging and unit testing](../../get-started/tutorials/espressif32/arduino-debugging-unit-testing.md)
- [Get started with ESP-IDF and ESP32-DevKitC: debugging, unit testing, project analysis](../../get-started/tutorials/espressif32/espidf-debugging-unit-testing-analysis.md)
- [Video: Free Inline Debugging for ESP32 and Arduino Sketches](https://www.youtube.com/watch?v=psMqilqlrRQ)

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

### External RAM (PSRAM) {#external-ram-psram}

You can enable external RAM using the next extra [build_flags](../../reference/platformio-ini/env/build-flags.md) in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) depending on a framework type.

Framework [Arduino](/hardware/frameworks/arduino):

```ini
[env:myenv]
platform = platformio/espressif32
framework = arduino
board = ...
build_flags =
    -DBOARD_HAS_PSRAM
    -mfix-esp32-psram-cache-issue
```

Framework [Espressif IoT Development Framework](/hardware/frameworks/espidf):

```ini
[env:myenv]
platform = platformio/espressif32
framework = espidf
board = ...
build_flags =
    -DCONFIG_SPIRAM_CACHE_WORKAROUND
```

More details are located in the official ESP-IDF documentation - [Support for external RAM](http://esp-idf.readthedocs.io/en/latest/api-guides/external-ram.html).

### Debug Level {#debug-level}

Please use one of the next [build_flags](../../reference/platformio-ini/env/build-flags.md) to change debug level. A [build_flags](../../reference/platformio-ini/env/build-flags.md) option could be used only the one time per build environment. If you need to specify more flags, please separate them with a new line or space.

Actual information is available in [Arduino for ESP32 Board Manifest](https://github.com/espressif/arduino-esp32/blob/master/boards.txt#L80). Please scroll to `esp32.menu.DebugLevel` section.

```ini
[env:myenv]
platform = ...
board = ...
framework = arduino

;;;;; Possible options ;;;;;;

; None
build_flags = -DCORE_DEBUG_LEVEL=0

; Error
build_flags = -DCORE_DEBUG_LEVEL=1

; Warn
build_flags = -DCORE_DEBUG_LEVEL=2

; Info
build_flags = -DCORE_DEBUG_LEVEL=3

; Debug
build_flags = -DCORE_DEBUG_LEVEL=4

; Verbose
build_flags = -DCORE_DEBUG_LEVEL=5
```

### Upload Speed {#upload-speed}

You can set custom upload speed using  [upload_speed](../../reference/platformio-ini/env/upload-speed.md) option from ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md)

```ini
[env:myenv]
upload_speed = 9600
```

### Erase Flash {#erase-flash}

Please [`pio run --target`](../../reference/cli/pio-run.md#cmdoption-pio-run-t) the next command to erase the entire flash chip (all data replaced with 0xFF bytes):

```text
> pio run --target erase

# or short version

> pio run -t erase
```

### Partition Tables {#partition-tables}

You can create a custom partitions table (CSV) following [ESP32 Partition Tables](https://docs.espressif.com/projects/esp-idf/en/latest/api-guides/partition-tables.html) documentation. PlatformIO uses **default partition tables** depending on a [framework](../../reference/platformio-ini/env/framework.md) type:

- `default.csv` for [Arduino](/hardware/frameworks/arduino) ([show pre-configured partition tables](https://github.com/espressif/arduino-esp32/blob/master/tools/partitions))
- `partitions_singleapp.csv` for [Espressif IoT Development Framework](/hardware/frameworks/espidf) ([show pre-configured partition tables](https://github.com/espressif/esp-idf/blob/master/components/partition_table))

To override default table please use `board_build.partitions` option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md).

:::warning

SPIFFS partition **MUST** have configured "Type" as "data" and "SubType" as "spiffs". For example, `spiffs, data, spiffs, 0x291000, 1M,`

:::

Examples:

```ini
; 1) A "partitions_custom.csv" in the root of project directory
[env:custom_table]
board_build.partitions = partitions_custom.csv

; 2) Switch between built-in tables
; https://github.com/espressif/arduino-esp32/tree/master/tools/partitions
; https://github.com/espressif/esp-idf/tree/master/components/partition_table
[env:custom_builtin_table]
board_build.partitions = no_ota.csv
```

### sdkconfig Configuration (ESP-IDF) {#sdkconfig-configuration-esp-idf}

ESP-IDF projects use `sdkconfig` files to configure the SDK. By default, PlatformIO generates `sdkconfig.<env>` (e.g. `sdkconfig.esp32dev` for `[env:esp32dev]`). This file contains the full merged configuration and is a build artifact, not a source file.

**Custom sdkconfig path**

Use `board_build.esp-idf.sdkconfig_path` to control where the generated sdkconfig is written:

```ini
[env:myenv]
board_build.esp-idf.sdkconfig_path = sdkconfig.custom
```

**SDKCONFIG_DEFAULTS layering**

Instead of checking in the full generated `sdkconfig.<env>`, you can maintain small defaults files containing only intentional overrides. Multiple files are separated by semicolons — later files override earlier ones:

```ini
[env:myenv]
board_build.cmake_extra_args =
    -DSDKCONFIG_DEFAULTS="sdkconfig.common;sdkconfig.board"
```

This enables patterns like:

- `sdkconfig.common` — shared across all environments (committed)
- `sdkconfig.board` — board-specific overrides (committed)
- `sdkconfig.local` — developer-specific tweaks (gitignored)

Add `sdkconfig.*` to `.gitignore` and only check in the defaults files. This keeps diffs clean and makes your configuration intent explicit.

See the [espidf-sdkconfig-defaults](https://github.com/platformio/platform-espressif32/tree/develop/examples/espidf-sdkconfig-defaults) and [espidf-sdkconfig-custom-path](https://github.com/platformio/platform-espressif32/tree/develop/examples/espidf-sdkconfig-custom-path) examples for working projects.

### Embedding Binary Data {#embedding-binary-data}

Sometimes you have a file with some binary or text data that you’d like to make available to your program - but you don’t want to reformat the file as C source.

There are two options `board_build.embed_txtfiles` and `board_build.embed_files` which can be used for embedding data. The only difference is that files specified in `board_build.embed_txtfiles` option are null-terminated in the final binary.

```ini
[env:myenv]
platform = platformio/espressif32
board = ...
board_build.embed_txtfiles =
  src/private.pem.key
  src/certificate.pem.crt
  src/aws-root-ca.pem
```

:::note

In case with ESP-IDF, these files also need to be specified in `CMakeLists.txt` using the `target_add_binary_data` function.

:::

The file contents will be added to the `.rodata` section in flash, and are available via symbol names as follows:

```c
extern const uint8_t aws_root_ca_pem_start[] asm("_binary_src_aws_root_ca_pem_start");
extern const uint8_t aws_root_ca_pem_end[] asm("_binary_src_aws_root_ca_pem_end");
extern const uint8_t certificate_pem_crt_start[] asm("_binary_src_certificate_pem_crt_start");
extern const uint8_t certificate_pem_crt_end[] asm("_binary_src_certificate_pem_crt_end");
extern const uint8_t private_pem_key_start[] asm("_binary_src_private_pem_key_start");
extern const uint8_t private_pem_key_end[] asm("_binary_src_private_pem_key_end");
```

The names are generated from the full name of the file. Characters `/, .`, etc. are replaced with underscores. The `_binary` + `_nested_folder` prefix in the symbol name is added by "objcopy" and is the same for both text and binary files.

:::note

With the ESP-IDF framework symbol names should not contain path to the files, for example `_binary_private_pem_key_start` instead of `_binary_src_private_pem_key_start`.

:::

See full example with embedding Amazon AWS certificates:

- [https://github.com/platformio/platform-espressif32/tree/develop/examples/espidf-aws-iot](https://github.com/platformio/platform-espressif32/tree/develop/examples/espidf-aws-iot)

### Uploading files to file system {#uploading-files-to-file-system}

1. Create new project using [PlatformIO IDE](../../get-started/platformio-ide.md) or initialize project using [PlatformIO Core (CLI)](../../get-started/platformio-core.md) and [pio project init](../../reference/cli/pio-project/init.md) (if you have not initialized it yet)
2. Create `data` folder (it should be on the same level as `src` folder) and put files here. Also, you can specify own location for [data_dir](../../reference/platformio-ini/platformio/data-dir.md)
3. Run "Upload File System image" task in [PlatformIO IDE](../../get-started/platformio-ide.md) or use [PlatformIO Core (CLI)](../../get-started/platformio-core.md) and [`pio run --target`](../../reference/cli/pio-run.md#cmdoption-pio-run-t) command with `uploadfs` target.

The `SPIFFS` file system is used by default in order to keep legacy project compatible. To choose `LittleFS` or `FFat` as the file system, it should be explicitly specified using `board_build.filesystem` option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md), for example:

```ini
[env:myenv]
platform = platformio/espressif32
framework = arduino
board = ...
board_build.filesystem = littlefs
```

Possible  values for `board_build.filesystem` are `spiffs` (default), `littlefs` and `fatfs`.

To upload SPIFFS image using OTA update please specify `upload_port` / `--upload-port` as IP address or mDNS host name (ending with the `*.local`).

Examples:

- [SPIFFS for Arduino](https://github.com/espressif/arduino-esp32/tree/master/libraries/SPIFFS/examples)
- [LittleFS for Arduino](https://github.com/espressif/arduino-esp32/tree/master/libraries/LittleFS/examples)
- [FFat for Arduino](https://github.com/espressif/arduino-esp32/tree/master/libraries/FFat/examples)
- [SPIFFS for ESP-IDF](https://github.com/espressif/esp-idf/tree/master/examples/storage/spiffs)

### Over-the-Air (OTA) update {#over-the-air-ota-update}

:::warning

Please make sure to read the theory behind the OTA updates in the [Over The Air Updates (OTA)](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/ota.html) article.

:::

1. Create a new project using [PlatformIO Home](../../get-started/platformio-home.md) or initialize a project via [PlatformIO Core (CLI)](../../get-started/platformio-core.md) and [pio project init](../../reference/cli/pio-project/init.md) (if you have not initialized it yet)
2. Copy the [basicOTA](https://github.com/espressif/arduino-esp32/tree/master/libraries/ArduinoOTA/examples/BasicOTA) example for Arduino or [Simple OTA](https://github.com/espressif/esp-idf/tree/master/examples/system/ota/simple_ota_example) example for ESP-IDF to [src_dir](../../reference/platformio-ini/platformio/src-dir.md) and configure your WiFi credentials (SSID and password).
3. Compile the project to ensure there are no syntax errors in the code.

To upload the binary you can either specify the upload address directly in the CLI command using the [`pio run --upload-port`](../../reference/cli/pio-run.md#cmdoption-pio-run-upload-port) option:

```bash
pio run --target upload --upload-port IP_ADDRESS_HERE or mDNS_NAME.local
```

For example:

```text
pio run -t upload --upload-port 192.168.0.255
pio run -t upload --upload-port myesp32.local
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
platform = platformio/espressif32
board = esp32dev
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
    --port=3232
```

Available flags

- `--port=ESP_PORT` ESP32 OTA Port. **Default 8266**
- `--auth=AUTH` Set authentication password
- `--spiffs` Use this option to transmit a SPIFFS image and do not flash the module

For the full list with available options please run

```bash
~/.platformio/packages/framework-arduinoespressif32/tools/espota.py --help

Usage: espota.py [options]

Transmit image over the air to the esp32 module with OTA support.

Options:
  -h, --help            show this help message and exit

  Destination:
    -i ESP_IP, --ip=ESP_IP
                        ESP32 IP Address.
    -I HOST_IP, --host_ip=HOST_IP
                        Host IP Address.
    -p ESP_PORT, --port=ESP_PORT
                        ESP32 ota Port. Default 3232
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
    -t TIMEOUT, --timeout=TIMEOUT
                        Timeout to wait for the ESP32 to accept invitation
```

:::warning

For windows users. To manage OTA check the ESP wifi network profile isn't checked on public be sure it's on private mode\`\`

:::

### Using Arduino Framework with Staging version {#using-arduino-framework-with-staging-version}

PlatformIO will install the latest Arduino Core for ESP32 from [https://github.com/espressif/arduino-esp32](https://github.com/espressif/arduino-esp32). The [Git](https://git-scm.com) should be installed in a system. To update Arduino Core to the latest revision, please open [PlatformIO IDE](../../get-started/platformio-ide.md) and navigate to `PlatformIO Home > Platforms > Updates`.

1. Please install [PlatformIO IDE](../../get-started/platformio-ide.md)

2. Initialize a new project, open ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) and specify the link to the framework repository in [platform_packages](../../reference/platformio-ini/env/platform-packages.md) section. For example,

   ```ini
   [env:esp32dev]
   platform = platformio/espressif32
   board = esp32dev
   framework = arduino
   platform_packages =
       platformio/framework-arduinoespressif32 @ https://github.com/espressif/arduino-esp32.git
   ```

3. Try to build the project

4. If you see build errors, then try to build this project using the same `stage` with Arduino IDE

5. If it works with Arduino IDE but doesn't work with PlatformIO, then please [file a new issue](https://github.com/platformio/platform-espressif32/issuess) with attached information:

   - test project/files
   - detailed log of build process from Arduino IDE (please copy it from console to [https://hastebin.com](https://hastebin.com))
   - detailed log of build process from PlatformIO Build System (please copy it from console to [https://hastebin.com](https://hastebin.com))

### Arduino Core Wiki {#arduino-core-wiki}

Tips, tricks and common problems: [http://desire.giesecke.tk/index.php/2018/01/30/esp32-wiki-entries/](http://desire.giesecke.tk/index.php/2018/01/30/esp32-wiki-entries/)
