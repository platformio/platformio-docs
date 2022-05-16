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

.. _cmd_project_metadata:

pio project metadata
====================

.. contents::

Usage
-----

.. code-block:: bash

    pio project metadata [OPTIONS]


Description
-----------

Dump a build metadata intended for IDE extensions/plugins:

- Toolchain type and location
- Compiler flags
- Defines/Macros
- CPP Preprocessor includes/paths
- Program path
- SVD path if available for :ref:`platforms`
- Targets by :ref:`platforms` (see :option:`pio run --list-targets` for details)
- Extra information.

Options
~~~~~~~

.. program:: pio project metadata

.. option::
    -d, --project-dir

Specify the path to project directory. By default, ``--project-dir`` is equal
to current working directory (``CWD``).

.. option::
    -e, --environment

Dump specified environments. Multiple environments are allowed.

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`__ format.

.. option::
    --json-output-path

Dump metadata in `JSON <https://en.wikipedia.org/wiki/JSON>`__ format
and save it to the specified path. If the only folder path is provided,
the file name will be generated automatically.
Please note that the parent folder must exist before.
