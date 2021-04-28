..  Copyright (c) 2014-present PlatformIO <contact@platformio.org>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _ci_gitlab:

GitLab
======

`GitLab <https://about.gitlab.com/features/gitlab-ci-cd/>`_ is a hosted cloud
platform that can help you build, test, deploy, and monitor your code from
GitLab repositories.

GitLab CI is enabled by default on new projects, so you can start using its
features right away. All you need is :ref:`cmd_ci` command, a file
called ``.gitlab-ci.yml`` (where you describe how the build should run) placed
in the root directory of your git project, and a configured Runner to
perform the actual build (Gitlab has some pre-configured public runners
so your CI script should work out of the box). Each project comes with a
Builds page where you can follow the output of each build, see the commit
that introduced it and other useful information such as the time the build
started, how long it lasted and the commiter's name. The statuses for each
build are exposed in the GitLab UI, and you can see whether a build
succeeded, failed, got canceled or skipped.

.. contents::

Integration
-----------

Put ``.gitlab-ci.yml`` to the root directory of your repository. The contents of this
file depends on the project you want to add. There are two possible ways of running
PlatformIO in CI services:

Using :ref:`cmd_run` command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This variant is default choice for native PlatformIO projects:

.. code-block:: yaml

    image: python:2.7

    stages:
     - test

    before_script:
      - "pip install -U platformio"

    job:
      stage: test
      script: "pio run -e <ID_1> -e <ID_2> -e <ID_N>"


Using :ref:`cmd_ci` command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This variant is more convenient when project is written as a library (when there are
examples or testing code) as it has additional options for specifying extra libraries
and boards from command line interface:

.. code-block:: yaml

    image: python:2.7

    stages:
     - test

    before_script:
      - "pip install -U platformio"

    job:
      stage: test
      script: "pio ci --board=<ID_1> --board=<ID_2> --board=<ID_N>"
      variables: {PLATFORMIO_CI_SRC: "path/to/test/file.c"}


Examples
--------

1. Integration for `ArduinoJson <https://github.com/bblanchon/ArduinoJson/>`_ library
   project. The ``.gitlab-ci.yml`` configuration file:

.. code-block:: yaml

    image: python:2.7

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
