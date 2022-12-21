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

.. _projectconf_check_flags:

``check_flags``
---------------

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
