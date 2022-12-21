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

.. _projectconf_debug_server:

``debug_server``
----------------

Type: ``String`` | Multiline Arguments: ``Yes``

Allows one to setup a custom debugging server. By default, boards are pre-configured
with a debugging server that is compatible with "on-board" debugging tool
(adapter, probe). Also, this option is useful for a
:ref:`debugging_tool_custom` debugging tool.

**Option format (multi-line)**:

* First line is an executable path of debugging server
* 2-nd and the next lines are arguments for executable file

**Examples:**

.. code-block:: ini

    [env:debug]
    platform = ...
    board = ...
    debug_server =
      /path/to/debugging/server
      arg1
      arg2
      ...
      argN

    [env:debug_openocd]
    platform = ...
    board = ...
    debug_tool = custom
    debug_server =
        ${platformio.packages_dir}/tool-openocd/openocd
        -f
        ${platformio.packages_dir}/tool-openocd/scripts/board/stm32f103zet6_warship.cfg

