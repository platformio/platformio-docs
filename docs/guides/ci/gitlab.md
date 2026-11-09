<a id="ci-gitlab"></a>

# GitLab {#gitlab}

[GitLab](https://about.gitlab.com/features/gitlab-ci-cd/) is a hosted cloud platform that can help you build, test, deploy, and monitor your code from GitLab repositories.

GitLab CI is enabled by default on new projects, so you can start using its features right away. All you need is [pio ci](../../reference/cli/pio-ci.md) command, a file called `.gitlab-ci.yml` (where you describe how the build should run) placed in the root directory of your git project, and a configured Runner to perform the actual build (Gitlab has some pre-configured public runners so your CI script should work out of the box). Each project comes with a Builds page where you can follow the output of each build, see the commit that introduced it and other useful information such as the time the build started, how long it lasted and the commiter's name. The statuses for each build are exposed in the GitLab UI, and you can see whether a build succeeded, failed, got canceled or skipped.

## Integration {#integration}

Put `.gitlab-ci.yml` to the root directory of your repository. The contents of this file depends on the project you want to add. There are two possible ways of running PlatformIO in CI services:

### Using [pio run](../../reference/cli/pio-run.md) command {#using-cmd-run-command}

This variant is default choice for native PlatformIO projects:

```yaml
image: python:3.11

# Change cache directories to be inside the project directory since GitLab can only cache local items.
variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"
  PLATFORMIO_CACHE_DIR: "$CI_PROJECT_DIR/.cache/platformio"

cache:
  paths:
    - .cache/pip
    - .cache/platformio

stages:
 - test

before_script:
  - "pip install -U platformio"

job:
  stage: test
  script: "pio run -e <ID_1> -e <ID_2> -e <ID_N>"
```

### Using [pio ci](../../reference/cli/pio-ci.md) command {#using-cmd-ci-command}

This variant is more convenient when project is written as a library (when there are examples or testing code) as it has additional options for specifying extra libraries and boards from command line interface:

```yaml
image: python:3.11

# Change cache directories to be inside the project directory since GitLab can only cache local items.
variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"
  PLATFORMIO_CACHE_DIR: "$CI_PROJECT_DIR/.cache/platformio"

cache:
  paths:
    - .cache/pip
    - .cache/platformio

stages:
 - test

before_script:
  - "pip install -U platformio"

job:
  stage: test
  script: "pio ci --board=<ID_1> --board=<ID_2> --board=<ID_N>"
  variables: {PLATFORMIO_CI_SRC: "path/to/test/file.c"}
```

## Examples {#examples}

1. Integration for [ArduinoJson](https://github.com/bblanchon/ArduinoJson/) library project. The `.gitlab-ci.yml` configuration file:

```yaml
image: python:3.11

# Change cache directories to be inside the project directory since GitLab can only cache local items.
variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"
  PLATFORMIO_CACHE_DIR: "$CI_PROJECT_DIR/.cache/platformio"

cache:
  paths:
    - .cache/pip
    - .cache/platformio

stages:
 - test

.job_template: &pio_run
  script:
    - "pio ci --lib='.' --board=uno --board=teensy31 --board=nodemcuv2 $PLATFORMIO_CI_EXTRA_ARGS"

before_script:
  - "pip install -U platformio"

JsonGeneratorExample:
  <<: *pio_run
  variables:
    PLATFORMIO_CI_EXTRA_ARGS: "--board=due"
    PLATFORMIO_CI_SRC: examples/JsonGeneratorExample

JsonHttpClient:
  <<: *pio_run
  variables:
    PLATFORMIO_CI_SRC: examples/JsonHttpClient

JsonParserExample:
  <<: *pio_run
  variables:
    PLATFORMIO_CI_SRC: examples/JsonParserExample

JsonServer:
  <<: *pio_run
  variables:
    PLATFORMIO_CI_SRC: examples/JsonServer

JsonUdpBeacon:
  <<: *pio_run
  variables:
    PLATFORMIO_CI_SRC: examples/JsonUdpBeacon

ProgmemExample:
  stage: test
  <<: *pio_run
  variables:
    PLATFORMIO_CI_SRC: examples/ProgmemExample

StringExample:
  stage: test
  <<: *pio_run
  variables:
    PLATFORMIO_CI_SRC: examples/StringExample
```
