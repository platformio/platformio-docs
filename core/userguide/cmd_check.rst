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

pio check
=========

Helper command for :ref:`piocheck`.

.. contents::

Usage
-----

.. code-block:: bash

    pio check [OPTIONS]

Description
-----------

Perform static analysis check on PlatformIO based project. By default :ref:`check_tool_cppcheck` analysis tool is used.

More details about PlatformIO :ref:`piocheck`.

Options
-------

.. program:: pio check

.. option::
    -e, --environment

Process specified environments.

.. option::
    --pattern

You can specify which source files or folders should be included/excluded from check
process. By default only :ref:`projectconf_pio_src_dir` and :ref:`projectconf_pio_include_dir`
are checked. Multiple ``--pattern`` options and `GLOB Patterns <http://en.wikipedia.org/wiki/Glob_(programming)>`_ are allowed.


Example: ``pio check --pattern="tests" --pattern="src/*.cpp"``

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

Multiple ``--flags`` options are allowed.

Example: ``pio check --flags "-DDEBUG cppcheck: --std=c++11 --platform=avr8"``

.. option::
    --severity

Specify the :ref:`check_severity` types which will be reported by the :ref:`check_tools`.
Possible values described in :ref:`check_severity` section. Multiple ``--severity``
options are allowed.

Example: ``pio check --severity=high``

.. option::
    -d, --project-dir

Specify the path to project directory. By default, ``--project-dir`` is equal
to the current working directory (``CWD``).

.. option::
    -c, --project-conf

Process project with a custom :ref:`projectconf`.

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`_ format.

.. option::
    --fail-on-defect

Fail (exit with non-zero code) if there is a defect found with specified
severity. By default exit code is the same as the exit code returned by
a tool selected for performing check. Possible values described in
:ref:`check_severity` section. Multiple ``--fail-on-defect`` options are allowed.

Example: ``pio check --fail-on-defect=low --fail-on-defect=medium``

.. option::
    -s, --silent

Suppress progress reporting and show only defects with ``high`` severity.
See :ref:`check_severity`.

.. option::
    -v, --verbose

Show detailed information when processing environments.

This option can also be set globally using :ref:`setting_force_verbose` setting
or by environment variable :envvar:`PLATFORMIO_SETTING_FORCE_VERBOSE`.

Examples
--------

For the examples please follow to :ref:`piocheck` page.
