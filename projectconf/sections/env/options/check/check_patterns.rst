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

.. _projectconf_check_patterns:

``check_patterns``
------------------

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
