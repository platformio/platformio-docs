..  Copyright (c) 2019-present PlatformIO <contact@platformio.org>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _cmd_check:

platformio check
================

Helper command for :ref:`code_analysis`.

.. contents::

Usage
-----

.. code-block:: bash

    platformio check [OPTIONS]
    pio check [OPTIONS]

Description
-----------

Perform static analysis check on PlatformIO based project. More details about 
PlatformIO :ref:`code_analysis`. By default ``CppCheck`` analysis tool is used.

This command allows you to run checks for the environments specified
in :ref:`projectconf`.

Options
-------

.. program:: platformio check

.. option::
    -e, --environment

Process specified environments. More details :option:`platformio check --environment`

.. option::
    --filter

Normally a program has many source files. By default only :ref:`projectconf_pio_src_dir`
and :ref:`projectconf_pio_include_dir` are checked. You can specify which source
files should be included/excluded from check process. The paths in filter should
be **relative to the root** of the project.

For example, ``platformio check --filter "-<*> +<src/> +<tests/>"``

.. option::
    --flags

Specify additional flags that need to be passed to the analysis tool. If multiple tools
set in :ref:`projectconf_check_tool` option, the flags are passed to all of them. 
Individual flags for each tool can be added using a special suffix with the tool name.

.. list-table::
    :header-rows:  1

    * - Flag
      - Meaning

    * - ``--addon=<addon>``
      - Execute addon. i.e. cert.

    * - ``-D<ID>``
      - Define preprocessor symbol.

For example, ``platformio check --flags "-DDEBUG cppcheck: --std=c++11  --platform=avr8"``

.. option::
    --severity

    Selects which severity level of the messages to be displayed. 
    The possible severity levels for found defects are:

.. list-table::
    :header-rows:  1

    * - Severity
      - Meaning

    * - ``HIGH``
      - Issues that are possibly bugs

    * - ``MEDIUM``
      - Suggestions about defensive programming in order to prevent potential bugs

    * - ``LOW``
      - Issues related to code cleanup and performance (unused functions, redundant code, const-ness, etc)

.. option::
    -d, --project-dir

Specify the path to project directory. By default, ``--project-dir`` is equal
to the current working directory (``CWD``).

.. option::
    -c, --project-conf

.. versionadded:: 4.0

Process project with a custom :ref:`projectconf`.

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`_ format

.. option::
    -s, --silent

Suppress progress reporting

.. option::
    -v, --verbose

Show detailed information when processing environments.

This option can also be set globally using :ref:`setting_force_verbose` setting
or by environment variable :envvar:`PLATFORMIO_SETTING_FORCE_VERBOSE`.

Examples
--------

For the examples please follow to :ref:`code_analysis` page.
