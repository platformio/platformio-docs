<a id="cmd-check"></a>

# pio check {#pio-check}

Helper command for [Static Code Analysis](../../guides/static-code-analysis/index.md).

## Usage {#usage}

```bash
pio check [OPTIONS]
```

## Description {#description}

Perform static analysis check on PlatformIO based project. By default [Cppcheck](../../guides/static-code-analysis/tools/cppcheck.md) analysis tool is used.

More details about PlatformIO [Static Code Analysis](../../guides/static-code-analysis/index.md).

## Options {#options}

<a id="cmdoption-pio-check-environment"></a>

### `-e, --environment` {#cmdoption-pio-check-e}

Process specified environments.

<a id="cmdoption-pio-check-src-filters"></a>

### `-f, --src-filters` {#cmdoption-pio-check-f}

:::info

Added in version 6.1.7.

:::

You can specify which source files or folders should be included/excluded from check process. By default only [src_dir](../platformio-ini/platformio/src-dir.md) and [include_dir](../platformio-ini/platformio/include-dir.md) are checked. Multiple `--src-filters` options and [GLOB Patterns](http://en.wikipedia.org/wiki/Glob_%28programming%29) are allowed.

Example: `pio check --src-filters="+<src/app/>" --src-filters="-<src/app/uart/>"`

### `--flags` {#cmdoption-pio-check-flags}

Specify additional flags that need to be passed to the analysis tool. If multiple tools set in [check_tool](../platformio-ini/env/check-tool.md) option, the flags are passed to all of them. Individual flags for each tool can be added using a special suffix with the tool name.

| Flag | Meaning |
|---|---|
| `--addon=<addon>` | Execute addon. i.e. cert. |
| `-D<ID>` | Define preprocessor symbol. |

Multiple `--flags` options are allowed.

Example: `pio check --flags "-DDEBUG cppcheck: --std=c++11 --platform=avr8"`

### `--severity` {#cmdoption-pio-check-severity}

Specify the [Defect severity](../../guides/static-code-analysis/severity.md) types which will be reported by the [Check tools](../../guides/static-code-analysis/tools/index.md). Possible values described in [Defect severity](../../guides/static-code-analysis/severity.md) section. Multiple `--severity` options are allowed.

Example: `pio check --severity=high`

<a id="cmdoption-pio-check-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-check-d}

Specify the path to project directory. By default, `--project-dir` is equal to the current working directory (`CWD`).

<a id="cmdoption-pio-check-project-conf"></a>

### `-c, --project-conf` {#cmdoption-pio-check-c}

Process project with a custom ["platformio.ini" (Project Configuration File)](../platformio-ini/index.md).

### `--json-output` {#cmdoption-pio-check-json-output}

Return the output in [JSON](http://en.wikipedia.org/wiki/JSON) format.

### `--fail-on-defect` {#cmdoption-pio-check-fail-on-defect}

Fail (exit with non-zero code) if there is a defect found with specified severity. By default exit code is the same as the exit code returned by a tool selected for performing check. Possible values described in [Defect severity](../../guides/static-code-analysis/severity.md) section. Multiple `--fail-on-defect` options are allowed.

Example: `pio check --fail-on-defect=low --fail-on-defect=medium`

### `--skip-packages` {#cmdoption-pio-check-skip-packages}

Exclude underlying third-party packages from the checking process. By default, PlatformIO passes frameworks and toolchains include paths required by internal analysis tools to properly analyze project sources. Some of the supported analysis tools use their own preprocessor which may fail to parse perfectly valid code and thus provide empty or partial check reports. This option is useful when developers have no control over this third-party code and want to perform analysis at least on project sources.

Example: `pio check --skip-packages`

<a id="cmdoption-pio-check-silent"></a>

### `-s, --silent` {#cmdoption-pio-check-s}

Suppress progress reporting and show only defects with `high` severity. See [Defect severity](../../guides/static-code-analysis/severity.md).

<a id="cmdoption-pio-check-verbose"></a>

### `-v, --verbose` {#cmdoption-pio-check-v}

Show detailed information when processing environments.

This option can also be set globally using [force_verbose](./pio-settings.md#setting-force-verbose) setting or by environment variable [`PLATFORMIO_SETTING_FORCE_VERBOSE`](../environment-variables.md#envvar-PLATFORMIO_SETTING_FORCE_VERBOSE).

## Examples {#examples}

For the examples please follow to [Static Code Analysis](../../guides/static-code-analysis/index.md) page.
