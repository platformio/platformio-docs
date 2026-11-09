---
description: "A list of library names which should be ignored by Library Dependency Finder (LDF) (platformio.ini option lib_ignore)."
---

<a id="projectconf-lib-ignore"></a>

# `lib_ignore` {#lib-ignore}

:::info[See also]

Read [Library Dependency Finder (LDF)](../../../guides/libraries/ldf.md) guide first.

:::

- **Type:** String
- **Multiple values:** Yes

Specify libraries which should be ignored by Library Dependency Finder.

The correct value for this option is a library name (not folder name). You will see these names in "Library Dependency Graph" when building a project between `<` and `>` symbols.

**Example:**

`Build output`

```text
...
Library Dependency Finder -> https://bit.ly/configure-pio-ldf
LDF MODES: FINDER(chain+) COMPATIBILITY(soft)
Collected 54 compatible libraries
Scanning dependencies...
Dependency Graph
|-- <Hash> v1.0
|-- <AsyncMqttClient> v0.8.2
|   |-- <ESPAsyncTCP> v1.1.3
|-- <ESP8266WiFi> v1.0
|-- <ESP Async WebServer> v1.1.1
|   |-- <ESPAsyncTCP> v1.1.3
|   |-- <ESP8266WiFi> v1.0
|   |-- <Hash> v1.0
|   |-- <ArduinoJson> v5.13.1
|-- <ArduinoJson> v5.13.1
|-- <DNSServer> v1.1.0
|   |-- <ESP8266WiFi> v1.0
|-- <Ticker> v1.0
....
```

`platformio.ini`

```ini
[env:myenv]
; Single line
lib_ignore = AsyncMqttClient, DNSServer

; Multi-line
lib_ignore =
  AsyncMqttClient
  ESP Async WebServer
```
