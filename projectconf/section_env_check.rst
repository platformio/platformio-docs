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

.. _projectconf_section_env_check:

Check options
-------------

.. seealso::
    Please make sure to read :ref:`piocheck` guide first.

.. contents::
    :local:

.. _projectconf_check_tool:

``check_tool``
^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``Yes`` | Default: ``cppcheck``

A name of the check tool used for analysis. This option is useful when you
want to check source code with two or more tools.

See available tools in :ref:`check_tools`.

**Example**

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    check_tool = cppcheck, clangtidy


.. _projectconf_check_patterns:

``check_patterns``
^^^^^^^^^^^^^^^^^^

Type: ``String (Pattern)`` | Multiple: ``Yes``

This option allows specifying which source files or folders should be
included/excluded from the check process. `GLOB Patterns <http://en.wikipedia.org/wiki/Glob_(programming)>`_ are allowed.
:ref:`projectconf_pio_src_dir` and :ref:`projectconf_pio_include_dir` folders are checked
by default.

Another option for filtering source files is :option:`pio check --pattern` command.

**Example**

.. code-block:: ini

    [env:custom_check_patterns]
    platform = ...
    board = ...
    check_tool = clangtidy
    check_patterns =
      app/sources
      tests/hardware/*.c


.. _projectconf_check_flags:

``check_flags``
^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``Yes``

Additional flags to be passed to the tool command line. This option is useful
when you want to adjust the check process to fit your project requirements.
By default, the flags are passed to all tools specified in :ref:`projectconf_check_tool`
section. To set individual flags, define tool name at the beginning of the line.

Another option for adding flags is :option:`pio check --flags` command.

**Example**

.. code-block:: ini

    [env:extra_check_flags]
    platform = ...
    board = ...
    check_tool = cppcheck, clangtidy
    check_flags =
      --common-flag
      cppcheck: --enable=performance --inline-suppr
      clangtidy: -fix-errors -format-style=mozilla


.. _projectconf_check_severity:

``check_severity``
^^^^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``Yes`` | Default: ``low, medium, high``

This option allows specifying the :ref:`check_severity` types which will
be reported by the :ref:`check_tools`.

Another option for filtering source files is :option:`pio check --severity` command.

**Example**

.. code-block:: ini

    [env:detect_only_medium_or_high_defects]
    platform = ...
    board = ...
    check_severity = medium, high
