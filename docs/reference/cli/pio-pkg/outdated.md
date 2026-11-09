<a id="cmd-pkg-outdated"></a>

# pio pkg outdated {#pio-pkg-outdated}

## Usage {#usage}

```bash
pio pkg outdated [OPTIONS]
```

## Description {#description}

Check for outdated project packages and list version information for all dependencies. This information includes the currently installed version, the desired version based on [Semantic Versioning](https://semver.org/), and the latest available version.

## Options {#options}

<a id="cmdoption-pio-pkg-outdated-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-pkg-outdated-d}

Specify the path to project directory. By default, `--project-dir` is equal to current working directory (`CWD`).

<a id="cmdoption-pio-pkg-outdated-environment"></a>

### `-e, --environment` {#cmdoption-pio-pkg-outdated-e}

Check for outdated packages only for the specified environments. Multiple environments are allowed.

## Examples {#examples}

Check outdated packages for [ESPHome](https://github.com/esphome/esphome) project

```text
> pio pkg outdated -e esp8266-arduino
Checking  [####################################]  100%

Semantic Versioning color legend:
<Major Update>  backward-incompatible updates
<Minor Update>  backward-compatible features
<Patch Update>  backward-compatible bug fixes

Package      Current    Wanted    Latest    Type     Environments
-----------  ---------  --------  --------  -------  ---------------
ArduinoJson  6.18.5     6.18.5    6.19.1    Library  esp8266-arduino
FastLED      3.3.2      3.3.2     3.5.0     Library  esp8266-arduino
TinyGPSPlus  1.0.2      1.0.2     1.0.3     Library  esp8266-arduino
```
