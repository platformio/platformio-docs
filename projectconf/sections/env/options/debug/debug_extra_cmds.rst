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

.. _projectconf_debug_extra_cmds:

``debug_extra_cmds``
--------------------

Type: ``String`` | Multiple: ``Yes``

Extra commands that will be passed to back-end debugger after :ref:`projectconf_debug_init_cmds`.
For example, add custom breakpoint and load ``.gdbinit`` from a project directory
for GDB:

.. code-block:: ini

    [env:debug]
    platform = ...
    board = ...
    debug_extra_cmds =
      break main.cpp:13
      break foo.cpp:100
      source .gdbinit

.. note::

  **Initial Project Breakpoints**: Use ``break path/to/file:LINE_NUMBER`` to
  define initial breakpoints for debug environment. Multiple breakpoints are
  allowed.

  To save session breakpoints, please use ``save breakpoints [filename]``
  command in Debug Console. For example, ``save breakpoints .gdbinit``. Later,
  this file could be loaded via ``source [filename]`` command. See above.
