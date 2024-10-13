..  Copyright (c) 2020-present PlatformIO <contact@platformio.org>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _ci_github_actions:

GitHub Actions
==============

`GitHub Actions <https://github.com/features/actions>`_ enables you to create custom
software development life cycle (SDLC) workflows directly in your GitHub repository.

You need to configure GitHub Actions using `YAML <http://en.wikipedia.org/wiki/YAML>`_
syntax, and save them as workflow files in your repository. Workflows are custom
automated processes that you can set up in your repository to build, test, package,
release, or deploy any code project on GitHub. You can write individual tasks, called
actions, and combine them to create a custom workflow. Once you've successfully created
aYAML workflow file and triggered the workflow, you will see the build logs, tests
results, artifacts, and statuses for each step of your workflow. It can be configured to
build project on a range of different :ref:`platforms`.

GitHub Actions help you automate your software development workflows in the same place
you store code and collaborate on pull requests and issues and each time this happens,
it will try to build the project using :ref:`cmd_ci` command.

.. contents::

Integration
-----------

.. note::
    Please make sure to read GitHub Actions `Quickstart <https://docs.github.com/en/actions/writing-workflows/quickstart>`_
    guide first.

There are two possible ways of running PlatformIO in CI services:

Using :ref:`cmd_run` command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This variant is default choice for native PlatformIO projects:

.. code-block:: yaml

  name: PlatformIO CI

  on: [push]

  jobs:
    build:
      runs-on: ubuntu-latest

      steps:
        - uses: actions/checkout@v4
        - uses: actions/cache@v4
          with:
            path: |
              ~/.cache/pip
              ~/.platformio/.cache
            key: ${{ runner.os }}-pio
        - uses: actions/setup-python@v5
          with:
            python-version: '3.11'
        - name: Install PlatformIO Core
          run: pip install --upgrade platformio

        - name: Build PlatformIO Project
          run: pio run

Using :ref:`cmd_ci` command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This variant is more convenient when project is written as a library (when there are
examples or testing code) as it has additional options for specifying extra libraries
and boards from command line interface:

.. code-block:: yaml

  name: PlatformIO CI

    on: [push]

    jobs:
      build:
        runs-on: ubuntu-latest
        strategy:
          matrix:
            example: [path/to/test/file.c, examples/file.ino, path/to/test/directory]

        steps:
          - uses: actions/checkout@v4
          - uses: actions/cache@v4
            with:
              path: |
                ~/.cache/pip
                ~/.platformio/.cache
              key: ${{ runner.os }}-pio
          - uses: actions/setup-python@v5
            with:
              python-version: '3.11'
          - name: Install PlatformIO Core
            run: pip install --upgrade platformio

          - name: Build PlatformIO examples
            run: pio ci --board=<ID_1> --board=<ID_2> --board=<ID_N>
            env:
              PLATFORMIO_CI_SRC: ${{ matrix.example }}

Custom Build Flags
~~~~~~~~~~~~~~~~~~

PlatformIO allows one to specify own build flags using :envvar:`PLATFORMIO_BUILD_FLAGS` environment

.. code-block:: yaml

    - name: Run PlatformIO
      run: pio ci path/to/test/file.c --board=<ID_1> --board=<ID_2> --board=<ID_N>
      env:
        PLATFORMIO_BUILD_FLAGS: -D SPECIFIC_MACRO -I/extra/inc

For the more details, please follow to
:ref:`available build flags/options <projectconf_build_flags>`.

Examples
--------

Integration for USB_Host_Shield_2.0 project. The ``workflow.yml`` configuration file:

.. code-block:: yaml

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
        - uses: actions/checkout@v4
        - uses: actions/cache@v4
          with:
            path: |
              ~/.cache/pip
              ~/.platformio/.cache
            key: ${{ runner.os }}-pio
        - uses: actions/setup-python@v5
          with:
            python-version: '3.11'
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


