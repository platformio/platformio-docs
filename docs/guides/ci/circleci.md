---
description: "Integration for USB_Host_Shield_2.0 project."
---

<a id="ci-circleci"></a>

# CircleCI {#circleci}

[CircleCI](https://circleci.com/about) is a hosted cloud platform that provides hosted continuous integration, deployment, and testing to [GitHub](http://en.wikipedia.org/wiki/GitHub) repositories.

CircleCI is configured by adding a file named `circle.yml`, which is a [YAML](http://en.wikipedia.org/wiki/YAML) format text file, to the root directory of the GitHub repository.

CircleCI automatically detects when a commit has been made and pushed to a repository that is using CircleCI, and each time this happens, it will try to build the project using [pio ci](../../reference/cli/pio-ci.md) command. This includes commits to all branches, not just to the master branch. CircleCI will also build and run pull requests. When that process has completed, it will notify a developer in the way it has been configured to do so — for example, by sending an email containing the build results (showing success or failure), or by posting a message on an IRC channel. It can be configured to build project on a range of different [Development Platforms](../../hardware/platforms/index.md).

## Integration {#integration}

:::note

Read CircleCI [Getting Started](https://circleci.com/docs/getting-started) guide first.

:::

There are two possible ways of running PlatformIO in CI services:

### Using [pio run](../../reference/cli/pio-run.md) command {#using-cmd-run-command}

This variant is default choice for native PlatformIO projects:

```yaml
version: 2.1
orbs:
  python: circleci/python@1.4.0

jobs:
  build:
    executor: python/default
    steps:
      - checkout  # checkout source code to working directory
      - run:
          name: Install PlatformIO
          command: pip install --upgrade platformio
      - run:
          name: Compile Project
          command: pio run

workflows:
  main:
    jobs:
      - build
```

### Using [pio ci](../../reference/cli/pio-ci.md) command {#using-cmd-ci-command}

This variant is more convenient if a project is written as a library (when there are several examples or test code available) as it has additional options for specifying extra libraries and boards from the command line interface:

```yaml
version: 2.1
orbs:
  python: circleci/python@1.4.0

jobs:
  build:
    parameters:
      ci_src:
        type: string
    executor: python/default
    environment:
      PLATFORMIO_CI_SRC: << parameters.ci_src >>
    steps:
      - checkout
      - run:
          name: Install PlatformIO
          command: pip install -U platformio
      - run:
          name: Compile << parameters.ci_src >>
          command: pio ci --board=<ID_1> --board=<ID_2> --board=<ID_N>

workflows:
  main:
    jobs:
      - build:
          matrix:
            parameters:
              ci_src: ["path/to/test/file.c", "examples/file.ino", "path/to/test/directory"]
```

#### Library dependencies {#library-dependencies}

There 2 options to test source code with dependent libraries:

### Install dependent library using [Library management](../libraries/index.md) {#install-dependent-library-using-librarymanager}

```yaml
- run:
  name: Install library
  command: pio lib -g install 1
```

### Manually download dependent library and include in build process via `--lib` option {#manually-download-dependent-library-and-include-in-build-process-via-lib-option}

```yaml
- run:
    name: Install library
    command: |
      wget https://github.com/PaulStoffregen/OneWire/archive/master.zip -O /tmp/onewire_source.zip
      unzip /tmp/onewire_source.zip -d /tmp/
- run:
    name: Compile project
    command: pio ci --lib="/tmp/OneWire-master" --board=<ID_1> --board=<ID_2> --board=<ID_N>
```

#### Custom build flags {#custom-build-flags}

PlatformIO allows you to specify your own build flags using [`PLATFORMIO_BUILD_FLAGS`](../../reference/environment-variables.md#envvar-PLATFORMIO_BUILD_FLAGS) environment:

```yaml
jobs:
  build:
    executor: python/default
    environment:
        PLATFORMIO_BUILD_FLAGS: -D SPECIFIC_MACROS -I/extra/inc
```

For the more details, see [available build flags/options](../../reference/platformio-ini/env/build-flags.md).

#### Advanced configuration {#advanced-configuration}

PlatformIO allows you to configure multiple build environments for the single source code using [`platformio.ini`](../../reference/platformio-ini/index.md).

Instead of `--board`, please use the `--project-conf` option:

```yaml
- run:
    name: Compile project
    command: pio ci /path/to/test/file.c --project-conf=/path/to/platoformio.ini
```

## Examples {#examples}

Integration for USB_Host_Shield_2.0 project. The `config.yml` configuration file:

```yaml
version: 2.1
orbs:
  python: circleci/python@1.4.0
jobs:
  build:
    parameters:
      example:
        type: string
    executor: python/default
    environment:
          PLATFORMIO_CI_SRC: << parameters.example >>
    steps:
      - checkout  # checkout source code to working directory
      - save_cache:
          # Cache PlatformIO packages for current project
          key: deps9-{{ .Branch }}-{{ arch }}
          paths:
            - "~/.platformio"
      - run:
          name: Install dependencies
          command: |
            pip install --upgrade platformio
            wget https://github.com/xxxajk/spi4teensy3/archive/master.zip -O /tmp/spi4teensy3.zip
            unzip /tmp/spi4teensy3.zip -d /tmp
      - run:
          name: Run PlatformIO
          command: pio ci --lib="." --lib="/tmp/spi4teensy3-master" --board=uno --board=teensy31 --board=due
workflows:
  main:
    jobs:
      - build:
          matrix:
            parameters:
              example:
                - examples/Bluetooth/PS3SPP/PS3SPP.ino
                - examples/pl2303/pl2303_gps/pl2303_gps.ino
```
