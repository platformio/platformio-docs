<a id="cmd-project-metadata"></a>

# pio project metadata {#pio-project-metadata}

## Usage {#usage}

```bash
pio project metadata [OPTIONS]
```

## Description {#description}

Dump a build metadata intended for IDE extensions/plugins:

- Toolchain type and location
- Compiler flags
- Defines/Macros
- CPP Preprocessor includes/paths
- Program path
- SVD path if available for [Development Platforms](../../../hardware/platforms/index.md)
- Targets by [Development Platforms](../../../hardware/platforms/index.md) (see [`pio run --list-targets`](../pio-run.md#cmdoption-pio-run-list-targets) for details)
- Extra information.

### Options {#options}

<a id="cmdoption-pio-project-metadata-project-dir"></a>

#### `-d, --project-dir` {#cmdoption-pio-project-metadata-d}

Specify the path to project directory. By default, `--project-dir` is equal to current working directory (`CWD`).

<a id="cmdoption-pio-project-metadata-environment"></a>

#### `-e, --environment` {#cmdoption-pio-project-metadata-e}

Dump specified environments. Multiple environments are allowed.

#### `--json-output` {#cmdoption-pio-project-metadata-json-output}

Return the output in [JSON](http://en.wikipedia.org/wiki/JSON) format.

#### `--json-output-path` {#cmdoption-pio-project-metadata-json-output-path}

Dump metadata in [JSON](https://en.wikipedia.org/wiki/JSON) format and save it to the specified path. If the only folder path is provided, the file name will be generated automatically. Please note that the parent folder must exist before.
