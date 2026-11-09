# Shippable

:::warning

Shippable has been discontinued. This page is kept for reference only.

:::

[Shippable](http://en.wikipedia.org/wiki/Shippable) is a hosted cloud platform that provides hosted continuous integration, deployment, and testing to [GitHub](http://en.wikipedia.org/wiki/GitHub) and [BitBucket](http://en.wikipedia.org/wiki/Bitbucket) repositories. Shippable's continuous integration service is built using Docker.

Shippable is configured by adding a file named `shippable.yml`, which is a [YAML](http://en.wikipedia.org/wiki/YAML) format text file, to the root directory of the GitHub repository or you can use your Travis CI configuration file `.travis.yml`.

Shippable automatically detects when a commit has been made and pushed to a repository that is using Shippable, and each time this happens, it will try to build the project using [pio ci](../../reference/cli/pio-ci.md) command. This includes commits to all branches, not just to the master branch. Shippable will also build and run pull requests. When that process has completed, it will notify a developer in the way it has been configured to do so — for example, by sending an email containing the build results (showing success or failure), or by posting a message on an IRC channel. It can be configured to build project on a range of different [Development Platforms](../../hardware/platforms/index.md).

## Integration {#integration}

Put `shippable.yml` or `.travis.yml` to the root directory of your repository. The contents of this file depends on the project you want to add. There are two possible ways of running PlatformIO in CI services:

### Using [pio run](../../reference/cli/pio-run.md) command {#using-cmd-run-command}

This variant is default choice for native PlatformIO projects:

```yaml
language: python
python:
    - "3.11"

install:
    - pip install -U platformio

script:
    - pio run -e <ID_1> -e <ID_2> -e <ID_N>
```

### Using [pio ci](../../reference/cli/pio-ci.md) command {#using-cmd-ci-command}

This variant is more convenient when project is written as a library (when there are examples or testing code) as it has additional options for specifying extra libraries and boards from command line interface:

```yaml
language: python
python:
    - "3.11"

env:
    - PLATFORMIO_CI_SRC=path/to/source/file.c
    - PLATFORMIO_CI_SRC=path/to/source/file.ino
    - PLATFORMIO_CI_SRC=path/to/source/directory

install:
    - pip install -U platformio

script:
    - pio ci --board=<ID_1> --board=<ID_2> --board=<ID_N>
```

## Examples {#examples}

Integration for [USB_Host_Shield_2.0](https://github.com/felis/USB_Host_Shield_2.0) project. The `shippable.yml` or `.travis.yml` configuration file:

```yaml
language: python
python:
    - "3.11"

env:
    - PLATFORMIO_CI_SRC=examples/Bluetooth/PS3SPP/PS3SPP.ino
    - PLATFORMIO_CI_SRC=examples/pl2303/pl2303_gps/pl2303_gps.ino

install:
    - pip install -U platformio
    - wget https://github.com/xxxajk/spi4teensy3/archive/master.zip -O /tmp/spi4teensy3.zip
    - unzip /tmp/spi4teensy3.zip -d /tmp

script:
    - pio ci --lib="." --lib="/tmp/spi4teensy3-master" --board=uno --board=teensy31 --board=due
```
