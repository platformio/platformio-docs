<a id="ci-travis"></a>

# Travis CI {#travis-ci}

[![](./img/ci-travis-logo.png)](https://docs.travis-ci.com/user/integration/platformio/)

**Travis CI** [officially supports](https://docs.travis-ci.com/user/integration/platformio/) **PlatformIO for Embedded Builds.**

[Travis CI](http://en.wikipedia.org/wiki/Travis_CI) is an open-source hosted, distributed continuous integration service used to build and test projects hosted at [GitHub](http://en.wikipedia.org/wiki/GitHub).

Travis CI is configured by adding a file named `.travis.yml`, which is a [YAML](http://en.wikipedia.org/wiki/YAML) format text file, to the root directory of the GitHub repository.

Travis CI automatically detects when a commit has been made and pushed to a repository that is using Travis CI, and each time this happens, it will try to build the project using [pio ci](../../reference/cli/pio-ci.md) command. This includes commits to all branches, not just to the master branch. Travis CI will also build and run pull requests. When that process has completed, it will notify a developer in the way it has been configured to do so — for example, by sending an email containing the build results (showing success or failure), or by posting a message on an IRC channel. It can be configured to build project on a range of different [Development Platforms](../../hardware/platforms/index.md).

## Integration {#integration}

Read Travis CI [Getting Started](http://docs.travis-ci.com/user/getting-started/) and [general build configuration](http://docs.travis-ci.com/user/customizing-the-build/) guides first.

:::note

If you are going to use PlatformIO [Unit Testing](../unit-testing/index.md) or [Remote Development](../remote-development.md) you will need to define [`PLATFORMIO_AUTH_TOKEN`](../../reference/environment-variables.md#envvar-PLATFORMIO_AUTH_TOKEN) environment variable in project settings. See [Defining Variables in Repository Settings](https://docs.travis-ci.com/user/environment-variables/#Defining-Variables-in-Repository-Settings) guide.

:::

PlatformIO is written in Python and is recommended to be run within [Travis CI Python isolated environment](http://docs.travis-ci.com/user/languages/python/#Travis-CI-Uses-Isolated-virtualenvs). There are two possible ways of running PlatformIO in CI services:

### Using [pio run](../../reference/cli/pio-run.md) command {#using-cmd-run-command}

This variant is default choice for native PlatformIO projects:

```yaml
language: python
python:
    - "3.11"

# Cache PlatformIO packages using Travis CI container-based infrastructure
sudo: false
cache:
    directories:
        - "~/.platformio"
        - $HOME/.cache/pip

install:
    - pip install -U platformio
    - pio update

script:
    - pio run -e <ID_1> -e <ID_2> -e <ID_N>
```

### Using [pio ci](../../reference/cli/pio-ci.md) command {#using-cmd-ci-command}

This variant is more convenient when project is written as a library (when there are examples or testing code) as it has additional options for specifying extra libraries and boards from command line interface:

```yaml
language: python
python:
    - "3.11"

# Cache PlatformIO packages using Travis CI container-based infrastructure
sudo: false
cache:
    directories:
        - "~/.platformio"
        - $HOME/.cache/pip

env:
    - PLATFORMIO_CI_SRC=path/to/test/file.c
    - PLATFORMIO_CI_SRC=examples/file.ino
    - PLATFORMIO_CI_SRC=path/to/test/directory

install:
    - pip install -U platformio
    - pio update

script:
    - pio ci --board=<ID_1> --board=<ID_2> --board=<ID_N>
```

Then perform steps 1, 2 and 4 from [http://docs.travis-ci.com/user/getting-started/](http://docs.travis-ci.com/user/getting-started/)

## Library dependencies {#library-dependencies}

There 2 options to test source code with dependent libraries:

### Install dependent library using [Library management](../libraries/index.md) {#install-dependent-library-using-librarymanager}

```yaml
install:
    - pip install -U platformio

    #
    # Libraries from PlatformIO Library Registry:
    #
    # https://platformio.org/lib/show/1/OneWire
    - pio lib -g install 1
```

### Manually download dependent library and include in build process via `--lib` option {#manually-download-dependent-library-and-include-in-build-process-via-lib-option}

```yaml
install:
    - pip install -U platformio

    # download library to the temporary directory
    - wget https://github.com/PaulStoffregen/OneWire/archive/master.zip -O /tmp/onewire_source.zip
    - unzip /tmp/onewire_source.zip -d /tmp/

script:
    - pio ci --lib="/tmp/OneWire-master" --board=<ID_1> --board=<ID_2> --board=<ID_N>
```

## Custom build flags {#custom-build-flags}

PlatformIO allows one to specify own build flags using [`PLATFORMIO_BUILD_FLAGS`](../../reference/environment-variables.md#envvar-PLATFORMIO_BUILD_FLAGS) environment

```yaml
env:
    - PLATFORMIO_CI_SRC=path/to/test/file.c PLATFORMIO_BUILD_FLAGS="-D SPECIFIC_MACROS_PER_TEST_ENV -I/extra/inc"
    - PLATFORMIO_CI_SRC=examples/file.ino
    - PLATFORMIO_CI_SRC=path/to/test/directory

install:
    - pip install -U platformio
    - export PLATFORMIO_BUILD_FLAGS="-D GLOBAL_MACROS_FOR_ALL_TEST_ENV"
```

For the more details, see [available build flags/options](../../reference/platformio-ini/env/build-flags.md).

## Advanced configuration {#advanced-configuration}

PlatformIO allows one to configure multiple build environments for the single source code using [`platformio.ini`](../../reference/platformio-ini/index.md).

Instead of `--board` option, please use [`pio ci --project-conf`](../../reference/cli/pio-ci.md#cmdoption-pio-ci-c)

```yaml
script:
    - pio ci --project-conf=/path/to/platoformio.ini
```

## Examples {#examples}

Custom build flags:

```yaml
os: linux
dist: focal
language: python
python:
    - "3.11"

# Cache PlatformIO packages using Travis CI container-based infrastructure
cache:
    directories:
        - "~/.platformio"
        - $HOME/.cache/pip

env:
    - PLATFORMIO_CI_SRC=examples/acm/acm_terminal
    - PLATFORMIO_CI_SRC=examples/Bluetooth/WiiIRCamera PLATFORMIO_BUILD_FLAGS="-DWIICAMERA"
    - PLATFORMIO_CI_SRC=examples/ftdi/USBFTDILoopback
    - PLATFORMIO_CI_SRC=examples/Xbox/XBOXUSB
    # - ...

install:
    - pip install -U platformio
    - pio update

    #
    # Libraries from PlatformIO Library Registry:
    #
    # https://platformio.org/lib/show/416/TinyGPS
    # https://platformio.org/lib/show/417/SPI4Teensy3
    - pio lib -g install 416 417

script:
    - pio ci --board=uno --board=teensy31 --board=due --lib="."
```

- Configuration file: [https://github.com/felis/USB_Host_Shield_2.0/blob/master/.travis.yml](https://github.com/felis/USB_Host_Shield_2.0/blob/master/.travis.yml)
- Build History: [https://travis-ci.org/felis/USB_Host_Shield_2.0](https://travis-ci.org/felis/USB_Host_Shield_2.0)

Dependency on external libraries:

```yaml
os: linux
dist: focal
language: python
python:
    - "3.11"

# Cache PlatformIO packages using Travis CI container-based infrastructure
cache:
    directories:
        - "~/.platformio"
        - $HOME/.cache/pip

env:
    - PLATFORMIO_CI_SRC=examples/backSoon/backSoon.ino
    - PLATFORMIO_CI_SRC=examples/etherNode/etherNode.ino
    # -

install:
    - pip install -U platformio
    - pio update

    - wget https://github.com/jcw/jeelib/archive/master.zip -O /tmp/jeelib.zip
    - unzip /tmp/jeelib.zip -d /tmp

    - wget https://github.com/Rodot/Gamebuino/archive/master.zip  -O /tmp/gamebuino.zip
    - unzip /tmp/gamebuino.zip -d /tmp

script:
    - pio ci --lib="." --lib="/tmp/jeelib-master" --lib="/tmp/Gamebuino-master/libraries/tinyFAT" --board=uno --board=megaatmega2560
```

- Configuration file: [https://github.com/jcw/ethercard/blob/master/.travis.yml](https://github.com/jcw/ethercard/blob/master/.travis.yml)
- Build History: [https://travis-ci.org/jcw/ethercard](https://travis-ci.org/jcw/ethercard)

Dynamic testing of the boards:

```yaml
os: linux
dist: focal
language: python
python:
    - "3.11"

# Cache PlatformIO packages using Travis CI container-based infrastructure
cache:
    directories:
        - "~/.platformio"
        - $HOME/.cache/pip

env:
    - PLATFORMIO_CI_SRC=examples/TimeArduinoDue PLATFORMIO_CI_EXTRA_ARGS="--board=due"
    - PLATFORMIO_CI_SRC=examples/TimeGPS
    - PLATFORMIO_CI_SRC=examples/TimeNTP
    - PLATFORMIO_CI_SRC=examples/TimeTeensy3 PLATFORMIO_CI_EXTRA_ARGS="--board=teensy31"
    # - ...

install:
    - pip install -U platformio
    - pio update
    - rm -rf ./linux

    #
    # Libraries from PlatformIO Library Registry:
    #
    # https://platformio.org/lib/show/416/TinyGPS
    - pio lib -g install 416 421 422

script:
    - pio ci --lib="." --board=uno --board=teensy20pp $PLATFORMIO_CI_EXTRA_ARGS
```

- Configuration file: [https://github.com/ivankravets/Time/blob/master/.travis.yml](https://github.com/ivankravets/Time/blob/master/.travis.yml)
- Build History: [https://travis-ci.org/ivankravets/Time](https://travis-ci.org/ivankravets/Time)

Advanced configuration with extra project options and libraries:

```yaml
os: linux
dist: focal
language: python
python:
    - "3.11"

# Cache PlatformIO packages using Travis CI container-based infrastructure
cache:
    directories:
        - "~/.platformio"
        - $HOME/.cache/pip

env:
    - PLATFORMIO_CI_SRC=examples/Boards_Bluetooth/Adafruit_Bluefruit_LE
    - PLATFORMIO_CI_SRC=examples/Boards_Bluetooth/Arduino_101_BLE PLATFORMIO_CI_EXTRA_ARGS="--board=genuino101"
    - PLATFORMIO_CI_SRC=examples/Boards_USB_Serial/Blue_Pill_STM32F103C PLATFORMIO_CI_EXTRA_ARGS="--board=bluepill_f103c8 --project-option='framework=arduino'"
    - PLATFORMIO_CI_SRC=examples/Export_Demo/myPlant_ESP8266 PLATFORMIO_CI_EXTRA_ARGS="--board=nodemcuv2 --project-option='lib_ignore=WiFi101'"
    # - ...

install:
    - pip install -U platformio
    - pio update

    #
    # Libraries from PlatformIO Library Registry:
    #
    # https://platformio.org/lib/show/44/Time
    # https://platformio.org/lib/show/419/SimpleTimer
    #
    # https://platformio.org/lib/show/17/Adafruit-CC3000
    # https://platformio.org/lib/show/28/SPI4Teensy3
    # https://platformio.org/lib/show/91/UIPEthernet
    # https://platformio.org/lib/show/418/WildFireCore
    # https://platformio.org/lib/show/420/WildFire-CC3000
    # https://platformio.org/lib/show/65/WiFlyHQ
    # https://platformio.org/lib/show/19/Adafruit-DHT
    # https://platformio.org/lib/show/299/WiFi101
    # https://platformio.org/lib/show/259/BLEPeripheral
    # https://platformio.org/lib/show/177/Adafruit_BluefruitLE_nRF51

    - pio lib -g install 17 28 91 418 419 420 65 44 19 299 259 177 https://github.com/vshymanskyy/BlynkESP8266.git https://github.com/cmaglie/FlashStorage.git https://github.com/michael71/Timer5.git

script:
    - make travis-build
```

- Configuration file: [https://github.com/blynkkk/blynk-library/blob/master/.travis.yml](https://github.com/blynkkk/blynk-library/blob/master/.travis.yml)
- Build History: [https://travis-ci.org/blynkkk/blynk-library](https://travis-ci.org/blynkkk/blynk-library)
