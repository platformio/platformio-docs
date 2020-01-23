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

Please make sure to read GitHub Actions `Getting Started <https://help.github.com/en/actions/automating-your-workflow-with-github-actions/getting-started-with-github-actions>`_
guide first.

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
        - uses: actions/checkout@v1
        - name: Set up Python
          uses: actions/setup-python@v1
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install platformio
        - name: Run PlatformIO
          run: platformio ci --board=<ID_1> --board=<ID_2> --board=<ID_N>
          env:
            PLATFORMIO_CI_SRC: ${{ matrix.example }}

For more details as for PlatformIO build process please look into :ref:`cmd_ci`.

Project as a library
~~~~~~~~~~~~~~~~~~~~

When project is written as a library (where own examples or testing code use
it), please use ``--lib="."`` option for :ref:`cmd_ci` command

.. code-block:: yaml

    run: platformio ci --lib="." --board=<ID_1> --board=<ID_2> --board=<ID_N>

Library dependencies
~~~~~~~~~~~~~~~~~~~~

There 2 options to test source code with dependent libraries:

Install dependent library using :ref:`librarymanager`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

    - name: Install library dependencies
      run: platformio lib -g install 1

    - name: Run PlatformIO
      run: platformio ci path/to/test/file.c --board=<ID_1> --board=<ID_2> --board=<ID_N>

Manually download dependent library and include in build process via ``--lib`` option
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

    - name: Install library dependencies
      run: |
        wget https://github.com/PaulStoffregen/OneWire/archive/master.zip -O /tmp/onewire_source.zip
        unzip /tmp/onewire_source.zip -d /tmp/

    - name: Run PlatformIO
      run: platformio ci path/to/test/file.c --lib="/tmp/OneWire-master" --board=<ID_1> --board=<ID_2> --board=<ID_N>

Custom Build Flags
~~~~~~~~~~~~~~~~~~

PlatformIO allows one to specify own build flags using :envvar:`PLATFORMIO_BUILD_FLAGS` environment

.. code-block:: yaml

    - name: Run PlatformIO
      run: platformio ci path/to/test/file.c --lib="/tmp/OneWire-master" --board=<ID_1> --board=<ID_2> --board=<ID_N>
      env:
        PLATFORMIO_BUILD_FLAGS: -D SPECIFIC_MACROS -I/extra/inc

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
        - uses: actions/checkout@v1
        - name: Set up Python
          uses: actions/setup-python@v1
        
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install platformio
            wget https://github.com/xxxajk/spi4teensy3/archive/master.zip -O /tmp/spi4teensy3.zip
            unzip /tmp/spi4teensy3.zip -d /tmp
        
        - name: Run PlatformIO
          run: platformio ci --lib="." --lib="/tmp/spi4teensy3-master" --board=uno --board=teensy31 --board=due
          env:
            PLATFORMIO_CI_SRC: ${{ matrix.example }}


