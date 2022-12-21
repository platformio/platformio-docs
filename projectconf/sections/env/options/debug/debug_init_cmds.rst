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

.. _projectconf_debug_init_cmds:

``debug_init_cmds``
-------------------

Type: ``String`` | Multiple: ``Yes`` | Default: `See details... <https://github.com/platformio/platformio-core/tree/develop/platformio/debug/config>`__

Initial commands that will be passed to back-end debugger.

PlatformIO dynamically configures back-end debugger depending on a debug
environment. Here is `a list with default initial commands <https://github.com/platformio/platformio-core/blob/develop/platformio/commands/debug/initcfgs.py>`__
for the popular :ref:`debugging_tools`.

For example, the custom initial commands for GDB:

.. code-block:: ini

    [env:debug]
    platform = ...
    board = ...
    debug_init_cmds =
      target extended-remote $DEBUG_PORT
      $INIT_BREAK
      monitor reset halt
      $LOAD_CMDS
      monitor init
      monitor reset halt
