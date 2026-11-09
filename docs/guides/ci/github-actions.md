<a id="ci-github-actions"></a>

# GitHub Actions {#github-actions}

[GitHub Actions](https://github.com/features/actions) enables you to create custom software development life cycle (SDLC) workflows directly in your GitHub repository.

You need to configure GitHub Actions using [YAML](http://en.wikipedia.org/wiki/YAML) syntax, and save them as workflow files in your repository. Workflows are custom automated processes that you can set up in your repository to build, test, package, release, or deploy any code project on GitHub. You can write individual tasks, called actions, and combine them to create a custom workflow. Once you've successfully created aYAML workflow file and triggered the workflow, you will see the build logs, tests results, artifacts, and statuses for each step of your workflow. It can be configured to build project on a range of different [Development Platforms](../../hardware/platforms/index.md).

GitHub Actions help you automate your software development workflows in the same place you store code and collaborate on pull requests and issues and each time this happens, it will try to build the project using [pio ci](../../reference/cli/pio-ci.md) command.

## Integration {#integration}

:::note

Please make sure to read GitHub Actions [Quickstart](https://docs.github.com/en/actions/writing-workflows/quickstart) guide first.

:::

There are two possible ways of running PlatformIO in CI services:

### Using [pio run](../../reference/cli/pio-run.md) command {#using-cmd-run-command}

This variant is default choice for native PlatformIO projects:

```yaml
name: PlatformIO CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v7
      - uses: actions/cache@v4
        with:
          path: |
            ~/.cache/pip
            ~/.platformio/.cache
          key: ${{ runner.os }}-pio
      - uses: actions/setup-python@v7
        with:
          python-version: '3.14'
      - name: Install PlatformIO Core
        run: pip install --upgrade platformio

      - name: Build PlatformIO Project
        run: pio run
```

### Using [pio ci](../../reference/cli/pio-ci.md) command {#using-cmd-ci-command}

This variant is more convenient when project is written as a library (when there are examples or testing code) as it has additional options for specifying extra libraries and boards from command line interface:

```yaml
name: PlatformIO CI

  on: [push]

  jobs:
    build:
      runs-on: ubuntu-latest
      strategy:
        matrix:
          example: [path/to/test/file.c, examples/file.ino, path/to/test/directory]

      steps:
        - uses: actions/checkout@v7
        - uses: actions/cache@v4
          with:
            path: |
              ~/.cache/pip
              ~/.platformio/.cache
            key: ${{ runner.os }}-pio
        - uses: actions/setup-python@v7
          with:
            python-version: '3.14'
        - name: Install PlatformIO Core
          run: pip install --upgrade platformio

        - name: Build PlatformIO examples
          run: pio ci --board=<ID_1> --board=<ID_2> --board=<ID_N>
          env:
            PLATFORMIO_CI_SRC: ${{ matrix.example }}
```

#### Custom Build Flags {#custom-build-flags}

PlatformIO allows one to specify own build flags using [`PLATFORMIO_BUILD_FLAGS`](../../reference/environment-variables.md#envvar-PLATFORMIO_BUILD_FLAGS) environment

```yaml
- name: Run PlatformIO
  run: pio ci path/to/test/file.c --board=<ID_1> --board=<ID_2> --board=<ID_N>
  env:
    PLATFORMIO_BUILD_FLAGS: -D SPECIFIC_MACRO -I/extra/inc
```

For the more details, please follow to [available build flags/options](../../reference/platformio-ini/env/build-flags.md).

## Examples {#examples}

Integration for USB_Host_Shield_2.0 project. The `workflow.yml` configuration file:

```yaml
name: PlatformIO CI

on: [push]

jobs:
  build:

    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        example: [examples/Bluetooth/PS3SPP/PS3SPP.ino, examples/pl2303/pl2303_gps/pl2303_gps.ino]

    steps:
      - uses: actions/checkout@v7
      - uses: actions/cache@v4
        with:
          path: |
            ~/.cache/pip
            ~/.platformio/.cache
          key: ${{ runner.os }}-pio
      - uses: actions/setup-python@v7
        with:
          python-version: '3.14'
      - name: Install PlatformIO Core
        run: pip install --upgrade platformio

      - name: Download external library
        run: |
          wget https://github.com/xxxajk/spi4teensy3/archive/master.zip -O /tmp/spi4teensy3.zip
          unzip /tmp/spi4teensy3.zip -d /tmp

      - name: Run PlatformIO
        run: pio ci --lib="." --lib="/tmp/spi4teensy3-master" --board=uno --board=teensy31 --board=due
        env:
          PLATFORMIO_CI_SRC: ${{ matrix.example }}
```
