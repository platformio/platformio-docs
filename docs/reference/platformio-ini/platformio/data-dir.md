---
description: "A data directory to store contents which can be uploaded to file system (SPIFFS, etc.) (platformio.ini option data_dir)."
---

<a id="projectconf-pio-data-dir"></a>

# `data_dir` {#data-dir}

- **Type:** Path
- **Multiple values:** No
- **Default:** `${PROJECT_DIR}/data`
- **Environment variable:** [`PLATFORMIO_DATA_DIR`](../../environment-variables.md#envvar-PLATFORMIO_DATA_DIR), overrides the value in `platformio.ini`

Data directory to store contents and [Using Filesystem](/hardware/platforms/espressif8266#platform-espressif-uploadfs). The default value is `data` that means that folder is located in the root of the project.
