<a id="ci-appveyor"></a>

# AppVeyor {#appveyor}

[AppVeyor](http://www.appveyor.com/about) is an open-source hosted, distributed continuous integration service used to build and test projects hosted at [GitHub](http://en.wikipedia.org/wiki/GitHub) on Windows family systems.

AppVeyor is configured by adding a file named `appveyor.yml`, which is a [YAML](http://en.wikipedia.org/wiki/YAML) format text file, to the root directory of the GitHub repository.

AppVeyor automatically detects when a commit has been made and pushed to a repository that is using AppVeyor, and each time this happens, it will try to build the project using [pio ci](../../reference/cli/pio-ci.md) command. This includes commits to all branches, not just to the master branch. AppVeyor will also build and run pull requests. When that process has completed, it will notify a developer in the way it has been configured to do so — for example, by sending an email containing the build results (showing success or failure), or by posting a message on an IRC channel. It can be configured to build project on a range of different [Development Platforms](../../hardware/platforms/index.md).

## Integration {#integration}

Put `appveyor.yml` to the root directory of the GitHub repository. The contents of this file depends on the project you want to add. There are two possible ways of running PlatformIO in CI services:

### Using [pio run](../../reference/cli/pio-run.md) command {#using-cmd-run-command}

This variant is default choice for native PlatformIO projects:

```yaml
build: off
environment:

install:
    - cmd: git submodule update --init --recursive
    - cmd: SET PATH=%PATH%;C:\Python27\Scripts
    - cmd: pip install -U platformio

test_script:
    - cmd: pio run -e <ID_1> -e <ID_2> -e <ID_N>
```

### Using [pio ci](../../reference/cli/pio-ci.md) command {#using-cmd-ci-command}

This variant is more convenient when project is written as a library (when there are examples or testing code) as it has additional options for specifying extra libraries and boards from command line interface:

```yaml
build: off
environment:

  matrix:
    - PLATFORMIO_CI_SRC: "path\\to\\source\\file.c"
    - PLATFORMIO_CI_SRC: "path\\to\\source\\file.ino"
    - PLATFORMIO_CI_SRC: "path\\to\\source\\directory"

install:
    - cmd: git submodule update --init --recursive
    - cmd: SET PATH=%PATH%;C:\Python27\Scripts
    - cmd: pip install -U platformio

test_script:
    - cmd: pio ci --board=<ID_1> --board=<ID_2> --board=<ID_N>
```

## Examples {#examples}

1. Integration for [USB_Host_Shield_2.0](https://github.com/felis/USB_Host_Shield_2.0) project. The `appveyor.yml` configuration file:

```yaml
build: off
environment:

  matrix:
    - PLATFORMIO_CI_SRC: "examples\\Bluetooth\\PS3SPP\\PS3SPP.ino"
    - PLATFORMIO_CI_SRC: "examples\\pl2303\\pl2303_gps\\pl2303_gps.ino"

install:
    - cmd: git submodule update --init --recursive
    - cmd: SET PATH=%PATH%;C:\Python27\Scripts
    - cmd: pip install -U platformio
    - cmd: git clone https://github.com/xxxajk/spi4teensy3.git C:\spi4teensy

test_script:
    - cmd: pio ci --lib="." --lib="C:\\spi4teensy" --board=uno --board=teensy31 --board=due
```
