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

.. _cmd_test:

pio test
========

Helper command for local :ref:`unit_testing`.

.. contents::

Usage
-----

.. code-block:: bash

    pio test [OPTIONS]

Description
-----------

Run locally tests from PlatformIO based project. More details about PlatformIO
:ref:`unit_testing`.

This command allows you to apply the tests for the environments specified
in :ref:`projectconf`.

Options
-------

.. program:: pio test

.. option::
    -e, --environment

Process specified environments. More details :option:`pio run --environment`

.. option::
    -f, --filter

Process only the tests where the name matches specified patterns. More than one
pattern is allowed. If you need to filter some tests for a specific
environment, please take a look at :ref:`projectconf_test_filter` option from
:ref:`projectconf`.

.. list-table::
    :header-rows:  1

    * - Pattern
      - Meaning

    * - ``*``
      - matches everything

    * - ``?``
      - matches any single character

    * - ``[seq]``
      - matches any character in seq

    * - ``[!seq]``
      - matches any character not in seq

For example, ``pio test --filter "mytest*" -i "test[13]"``

.. option::
    -i, --ignore

Ignore tests where the name matches specified patterns. More than one
pattern is allowed. If you need to ignore some tests for a specific
environment, please take a look at :ref:`projectconf_test_ignore` option from
:ref:`projectconf`.

.. list-table::
    :header-rows:  1

    * - Pattern
      - Meaning

    * - ``*``
      - matches everything

    * - ``?``
      - matches any single character

    * - ``[seq]``
      - matches any character in seq

    * - ``[!seq]``
      - matches any character not in seq

For example, ``pio test --ignore "mytest*" -i "test[13]"``

.. option::
    --upload-port

A port that is intended for firmware uploading. To list available ports
please use :ref:`cmd_device_list` command.

If upload port is not specified, PlatformIO will try to detect it automatically.

.. option::
    --test-port

A Serial/UART port that PlatformIO uses as communication interface between
PlatformIO Unit Test Engine and target device. To list available ports
please use :ref:`cmd_device_list` command.

If test port is not specified, PlatformIO will try to detect it automatically.

.. option::
    -d, --project-dir

Specify the path to project directory. By default, ``--project-dir`` is equal
to current working directory (``CWD``).

.. option::
    -c, --project-conf

Process project with a custom :ref:`projectconf`.

.. option::
    --without-building

Skip building stage.

.. option::
    --without-uploading

Skip uploading stage.

.. option::
    --without-testing

Skip testing stage.

.. option::
    --no-reset

Disable software reset via ``Serial.DTR/RST`` before test running. In this case,
need to press "reset" button manually after firmware uploading.

.. warning::
  If board does not support software reset via ``Serial.DTR/RTS`` you
  should add >2 seconds delay before ``UNITY_BEGIN()`.
  We need that time to establish a ``Serial`` communication between host
  machine and target device. See :ref:`unit_testing`.

.. option::
    --monitor-rts

Set initial ``RTS`` line state for Serial Monitor (``0`` or ``1``),
default ``1``. We use it to gather test results via Serial connection.

.. option::
    --monitor-dtr

Set initial ``DTR`` line state for Serial Monitor (``0`` or ``1``),
default ``1``. We use it to gather test results via Serial connection.

.. option::
    -v, --verbose

Shows detailed information when processing environments.

This option can also be set globally using :ref:`setting_force_verbose` setting
or by environment variable :envvar:`PLATFORMIO_SETTING_FORCE_VERBOSE`.

Examples
--------

For the examples please follow to :ref:`unit_testing` page.
