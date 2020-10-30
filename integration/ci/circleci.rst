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

.. _ci_circleci:

CircleCI
========

`CircleCI <https://circleci.com/about>`_ is a hosted cloud
platform that provides hosted continuous integration, deployment, and testing
to `GitHub <http://en.wikipedia.org/wiki/GitHub>`_ repositories.

CircleCI is configured by adding a file named ``circle.yml``, which is a
`YAML <http://en.wikipedia.org/wiki/YAML>`_ format text file, to the root
directory of the GitHub repository.

CircleCI automatically detects when a commit has been made and pushed to a
repository that is using CircleCI, and each time this happens, it will
try to build the project using :ref:`cmd_ci` command. This includes commits to
all branches, not just to the master branch. CircleCI will also build and run
pull requests. When that process has completed, it will notify a developer in
the way it has been configured to do so — for example, by sending an email
containing the build results (showing success or failure), or by posting a
message on an IRC channel. It can be configured to build project on a range of
different :ref:`platforms`.

.. contents::

Integration
-----------

.. note::
    Please make sure to read CircleCI `Getting Started <https://circleci.com/docs/getting-started>`_
    guide first.

There are two possible ways of running PlatformIO in CI services:

Using :ref:`cmd_run` command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This variant is default choice for native PlatformIO projects:

.. code-block:: yaml

    dependencies:
        pre:
            # Install the latest stable PlatformIO
            - sudo pip install -U platformio

    test:
        override:
            - pio run -e <ID_1> -e <ID_2> -e <ID_N>


Using :ref:`cmd_ci` command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This variant is more convenient when project is written as a library (when there are
examples or testing code) as it has additional options for specifying extra libraries
and boards from command line interface:

.. code-block:: yaml

    dependencies:
        pre:
            # Install the latest stable PlatformIO
            - sudo pip install -U platformio

    test:
        override:
            - pio ci path/to/test/file.c --board=<ID_1> --board=<ID_2> --board=<ID_N>
            - pio ci examples/file.ino --board=<ID_1> --board=<ID_2> --board=<ID_N>
            - pio ci path/to/test/directory --board=<ID_1> --board=<ID_2> --board=<ID_N>


Library dependencies
~~~~~~~~~~~~~~~~~~~~

There 2 options to test source code with dependent libraries:

Install dependent library using :ref:`librarymanager`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

    dependencies:
        pre:
            # Install the latest stable PlatformIO
            - sudo pip install -U platformio

            # OneWire Library with ID=1 https://platformio.org/lib/show/1/OneWire
            - pio lib -g install 1

    test:
        override:
            - pio ci path/to/test/file.c --board=<ID_1> --board=<ID_2> --board=<ID_N>

Manually download dependent library and include in build process via ``--lib`` option
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

    dependencies:
        pre:
            # Install the latest stable PlatformIO
            - sudo pip install -U platformio

            # download library to the temporary directory
            - wget https://github.com/PaulStoffregen/OneWire/archive/master.zip -O /tmp/onewire_source.zip
            - unzip /tmp/onewire_source.zip -d /tmp/

    test:
        override:
            - pio ci path/to/test/file.c --lib="/tmp/OneWire-master" --board=<ID_1> --board=<ID_2> --board=<ID_N>

Custom Build Flags
~~~~~~~~~~~~~~~~~~

PlatformIO allows one to specify own build flags using :envvar:`PLATFORMIO_BUILD_FLAGS` environment

.. code-block:: yaml

    machine:
        environment:
            PLATFORMIO_BUILD_FLAGS: -D SPECIFIC_MACROS -I/extra/inc


For the more details, please follow to
:ref:`available build flags/options <projectconf_build_flags>`.


Advanced configuration
~~~~~~~~~~~~~~~~~~~~~~

PlatformIO allows one to configure multiple build environments for the single
source code using :ref:`projectconf`.

Instead of ``--board`` option, please use :option:`pio ci --project-conf`

.. code-block:: yaml

    test:
        override:
            - pio ci path/to/test/file.c --project-conf=/path/to/platoformio.ini

Examples
--------

1. Custom build flags

.. code-block:: yaml

    dependencies:
        cache_directories:
            - "~/.platformio"

        pre:
            - sudo pip install -U platformio

            # pre-install PlatformIO development platforms, they will be cached
            - pio platform install atmelavr atmelsam teensy

            #
            # Libraries from PlatformIO Library Registry:
            #
            # https://platformio.org/lib/show/416/TinyGPS
            # https://platformio.org/lib/show/417/SPI4Teensy3
            - pio lib -g install 416 417

    test:
        override:
            - pio ci examples/acm/acm_terminal --board=uno --board=teensy31 --board=due --lib="."
            - pio ci examples/adk/adk_barcode --board=uno --board=teensy31 --board=due --lib="."
            - pio ci examples/adk/ArduinoBlinkLED --board=uno --board=teensy31 --board=due --lib="."
            - pio ci examples/adk/demokit_20 --board=uno --board=teensy31 --board=due --lib="."
            # ...
            - pio ci examples/Xbox/XBOXUSB --board=uno --board=teensy31 --board=due --lib="."


2. Dependency on external libraries

.. code-block:: yaml

    dependencies:
        pre:
            # Install the latest stable PlatformIO
            - sudo pip install -U platformio

            # download dependent libraries
            - wget https://github.com/jcw/jeelib/archive/master.zip -O /tmp/jeelib.zip
            - unzip /tmp/jeelib.zip -d /tmp

            - wget https://github.com/Rodot/Gamebuino/archive/master.zip  -O /tmp/gamebuino.zip
            - unzip /tmp/gamebuino.zip -d /tmp

    test:
        override:
            -  pio ci examples/backSoon/backSoon.ino --lib="." --lib="/tmp/jeelib-master" --lib="/tmp/Gamebuino-master/libraries/tinyFAT" --board=uno --board=megaatmega2560
            -  pio ci examples/etherNode/etherNode.ino --lib="." --lib="/tmp/jeelib-master" --lib="/tmp/Gamebuino-master/libraries/tinyFAT" --board=uno --board=megaatmega2560
            -  pio ci examples/getDHCPandDNS/getDHCPandDNS.ino --lib="." --lib="/tmp/jeelib-master" --lib="/tmp/Gamebuino-master/libraries/tinyFAT" --board=uno --board=megaatmega2560
            -  pio ci examples/getStaticIP/getStaticIP.ino --lib="." --lib="/tmp/jeelib-master" --lib="/tmp/Gamebuino-master/libraries/tinyFAT" --board=uno --board=megaatmega2560
            # ...
            -  pio ci examples/twitter/twitter.ino --lib="." --lib="/tmp/jeelib-master" --lib="/tmp/Gamebuino-master/libraries/tinyFAT" --board=uno --board=megaatmega2560
            -  pio ci examples/udpClientSendOnly/udpClientSendOnly.ino --lib="." --lib="/tmp/jeelib-master" --lib="/tmp/Gamebuino-master/libraries/tinyFAT" --board=uno --board=megaatmega2560
            -  pio ci examples/udpListener/udpListener.ino --lib="." --lib="/tmp/jeelib-master" --lib="/tmp/Gamebuino-master/libraries/tinyFAT" --board=uno --board=megaatmega2560
            -  pio ci examples/webClient/webClient.ino --lib="." --lib="/tmp/jeelib-master" --lib="/tmp/Gamebuino-master/libraries/tinyFAT" --board=uno --board=megaatmega2560

* Configuration file: https://github.com/ivankravets/ethercard/blob/master/circle.yml
* Build History: https://circleci.com/gh/ivankravets/ethercard/tree/master
