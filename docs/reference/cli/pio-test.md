<a id="cmd-test"></a>

# pio test {#pio-test}

Helper command for local [Unit Testing](../../guides/unit-testing/index.md).

## Usage {#usage}

```bash
pio test [OPTIONS]
```

## Description {#description}

Run project tests on host (local) machine using PlatformIO [Unit Testing](../../guides/unit-testing/index.md).

## Options {#options}

<a id="cmdoption-pio-test-environment"></a>

### `-e, --environment` {#cmdoption-pio-test-e}

Process specified project environment. Multiple environments are allowed.

<a id="cmdoption-pio-test-filter"></a>

### `-f, --filter` {#cmdoption-pio-test-f}

Process only test suites whose path relative to the [test_dir](../platformio-ini/platformio/test-dir.md) matches the specified pattern. See documentation for the [test_filter](../platformio-ini/env/test-filter.md) project configuration option for more details.

Example, `pio test --filter "test_common" -f "native/*"`

<a id="cmdoption-pio-test-ignore"></a>

### `-i, --ignore` {#cmdoption-pio-test-i}

Ignore test suites whose path relative to the [test_dir](../platformio-ini/platformio/test-dir.md) matches the specified pattern. See documentation for the [test_ignore](../platformio-ini/env/test-ignore.md) project configuration option for more details.

For example, `pio test --ignore "embedded/*" -i "test_suite[13]"`

### `--upload-port` {#cmdoption-pio-test-upload-port}

A port that is intended for firmware uploading. To list available ports please use the [pio device list](./pio-device/list.md) command.

If the upload port is not specified, PlatformIO will try to detect it automatically.

### `--test-port` {#cmdoption-pio-test-test-port}

A Serial/UART port that PlatformIO uses as a communication interface between PlatformIO Unit Test Engine and target device. To list available ports please use [pio device list](./pio-device/list.md) command.

If test port is not specified, PlatformIO will try to detect it automatically.

<a id="cmdoption-pio-test-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-test-d}

Specify the path to the project directory. By default, `--project-dir` is equal to a current working directory (`CWD`).

<a id="cmdoption-pio-test-project-conf"></a>

### `-c, --project-conf` {#cmdoption-pio-test-c}

Process project with a custom ["platformio.ini" (Project Configuration File)](../platformio-ini/index.md).

### `--without-building` {#cmdoption-pio-test-without-building}

Skip the building stage.

### `--without-uploading` {#cmdoption-pio-test-without-uploading}

Skip the uploading stage.

### `--without-testing` {#cmdoption-pio-test-without-testing}

Skip the testing stage.

### `--no-reset` {#cmdoption-pio-test-no-reset}

Disable software reset via `Serial.DTR/RST` before test running. In this case, need to press the "reset" button manually after firmware uploading.

:::warning

If the board does not support software reset via `Serial.DTR/RTS` you should add >2 seconds delay before `UNITY_BEGIN()`. We need that time to establish a `Serial` communication between the host machine and the target device. See [Unit Testing](../../guides/unit-testing/index.md).

:::

### `--monitor-rts` {#cmdoption-pio-test-monitor-rts}

Set initial `RTS` line state for Serial Monitor (`0` or `1`), default `1`. We use it to gather test results via a Serial connection.

### `--monitor-dtr` {#cmdoption-pio-test-monitor-dtr}

Set initial `DTR` line state for Serial Monitor (`0` or `1`), default `1`. We use it to gather test results via a Serial connection.

<a id="cmdoption-pio-test-program-arg"></a>

### `-a, --program-arg` {#cmdoption-pio-test-a}

Pass an extra argument to the testing program. Multiple arguments are allowed.

If you need to pass extra arguments permanently per a testing environment, please take a look at the [test_testing_command](../platformio-ini/env/test-testing-command.md).

**Example**

```bash
> pio test --program-arg "--abort-after=1" --program-arg="-s"
# or short format
> pio test -a "-aa=1" -a "-s"
```

### `--list-tests` {#cmdoption-pio-test-list-tests}

List project tests without processing. The [`pio test --json-output-path`](#cmdoption-pio-test-json-output-path) or [`pio test --junit-output-path`](#cmdoption-pio-test-junit-output-path) options can be used for dumping available test suites.

### `--json-output` {#cmdoption-pio-test-json-output}

Return the output in [JSON](http://en.wikipedia.org/wiki/JSON) format.

### `--json-output-path` {#cmdoption-pio-test-json-output-path}

Generate a unit testing report in the [JSON](https://en.wikipedia.org/wiki/JSON) format and save it to the specified path. If the only folder path is provided, the file name will be generated automatically. Please note that the parent folder must exist before.

### `--junit-output-path` {#cmdoption-pio-test-junit-output-path}

The same as [`pio test --json-output-path`](#cmdoption-pio-test-json-output-path) but generates a report in the [JUnit XML](https://www.ibm.com/docs/en/developer-for-zos/14.1.0?topic=formats-junit-xml-format) format.

<a id="cmdoption-pio-test-verbose"></a>

### `-v, --verbose` {#cmdoption-pio-test-v}

Control verbosity level.

| Level | Description |
|---|---|
| (none) | Normal verbosity (**default**) |
| `-v` | Show a raw output from a testing framework |
| `-vv` | Base verbosity for building and uploading stages |
| `-vvv` | Extra verbosity for building and uploading stages |

## Examples {#examples}

For the examples please follow to [Unit Testing](../../guides/unit-testing/index.md) page.
