<a id="cmd-pkg-show"></a>

# pio pkg show {#pio-pkg-show}

## Usage {#usage}

```bash
pio pkg show [OPTIONS] [<owner>/]<pkg>[@<version>]
```

## Description {#description}

Show package information from the [PlatformIO Registry](https://registry.platformio.org).

## Options {#options}

<a id="cmdoption-pio-pkg-show-type"></a>

### `-t, --type` {#cmdoption-pio-pkg-show-t}

Set the type of a package if there is a conflict name. See supported [Package Types](./install.md#cmd-pkg-install-types).

## Examples {#examples}

Show information about [ArduinoJson](https://registry.platformio.org/libraries/bblanchon/ArduinoJson) package

```text
> pio pkg show bblanchon/ArduinoJson

bblanchon/ArduinoJson
Library • 6.19.3 • Public • Published Tue Mar  8 16:24:14 2022

https://registry.platformio.org/libraries/bblanchon/ArduinoJson

A simple and efficient JSON library for embedded C++. ...

---------------------  ----------------------------------------------------------------
Homepage               https://arduinojson.org/?utm_source=meta&utm_medium=library.json
Repository             https://github.com/bblanchon/ArduinoJson.git
License                MIT
Popularity             2
Stars                  5599
Examples               10
Installed Size         385.83KB
Used By                134
Compatible Platforms   *
Compatible Frameworks  *
Keywords               json, rest, http, web
---------------------  ----------------------------------------------------------------

Version    Size      Published
---------  --------  -------------------
6.19.3     85.04KB   2022-03-08 16:24:14
6.19.2     84.82KB   2022-02-14 08:06:06
...
```

## See Also {#see-also}

- [pio pkg search](./search.md)
- [pio pkg list](./list.md)
- [pio pkg install](./install.md)
