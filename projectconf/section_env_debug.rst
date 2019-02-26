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

.. _projectconf_section_env_debug:

Debugging options
~~~~~~~~~~~~~~~~~

.. versionadded:: 3.4
.. seealso::
    Please make sure to read :ref:`piodebug` guide first.

.. contents::
    :local:

.. _projectconf_debug_tool:

``debug_tool``
^^^^^^^^^^^^^^

A name of debugging tool. This option is useful when board supports more than
one debugging tool (adapter, probe) or you want to create :ref:`debugging_tool_custom`
debugging configuration.

See available tools in :ref:`debugging_tools`.

**Example**

.. code-block:: ini

    [env:debug]
    platform = ...
    board = ...
    debug_tool = custom

.. _projectconf_debug_init_break:

``debug_init_break``
^^^^^^^^^^^^^^^^^^^^

An initial breakpoint that makes your program stop whenever a certain point in
the program is reached. **Default** value is set to ``tbreak main`` and means
creating a temporary breakpoint at ``int main(...)`` function and
automatically delete it after the first time a program stops there.

* `GDB Setting Breakpoints <https://sourceware.org/gdb/onlinedocs/gdb/Set-Breaks.html#Set-Breaks>`_
* `GDB Breakpoint Locations <https://sourceware.org/gdb/onlinedocs/gdb/Specify-Location.html#Specify-Location>`_

.. note::
  Please note that each debugging tool (adapter, probe) has limited number of
  hardware breakpoints.

  If you need more **Project Initial Breakpoints**, please place them in :ref:`projectconf_debug_extra_cmds`.

**Examples**

.. code-block:: ini

    [env:debug]
    platform = ...
    board = ...

    ; Examples 1: disable initial breakpoint
    debug_init_break =

    ; Examples 2: temporary stop at ``void loop()`` function
    debug_init_break = tbreak loop

    ; Examples 3: stop in main.cpp at line 13
    debug_init_break = break main.cpp:13

    ; Examples 4: temporary stop at ``void Reset_Handler(void)``
    debug_init_break = tbreak Reset_Handler

.. _projectconf_debug_init_cmds:

``debug_init_cmds``
^^^^^^^^^^^^^^^^^^^

Initial commands that will be passed to back-end debugger.

PlatformIO dynamically configures back-end debugger depending on a debug environment.
**Highly recommended to DO NOT override this option.**

For example, the custom initial commands for GDB:

.. code-block:: ini

    [env:debug]
    platform = ...
    board = ...
    debug_init_cmds =
      target extended-remote $DEBUG_PORT
      $INIT_BREAK
      monitor reset halt
      $LOAD_CMD
      monitor init
      monitor reset halt

.. _projectconf_debug_extra_cmds:

``debug_extra_cmds``
^^^^^^^^^^^^^^^^^^^^

Extra commands that will be passed to back-end debugger after initialization.
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

.. _projectconf_debug_load_cmd:

``debug_load_cmd``
^^^^^^^^^^^^^^^^^^

Specify a command which will be used to load program/firmware to a target
device. Possible options:

* ``load`` - **default** option
* ``some command`` - pass any debugging client command (GDB, etc.)
* ``load address`` - load program at specified address, where "address"
  should be a valid number
* ``preload`` - some embedded devices have locked Flash Memory (a few
  Freescale Kinetis and NXP LPC boards). In this case, firmware loading using
  debugging client is disabled. ``preload`` command instructs
  :ref:`piocore` to load program/firmware using development platform "upload"
  method (via bootloader, media disk, etc)
* (empty value, ``debug_load_cmd =``), disables program loading at all.


.. _projectconf_debug_load_mode:

``debug_load_mode``
^^^^^^^^^^^^^^^^^^^

Allows one to control when PlatformIO should load debugging firmware to the end
target. Possible options:

* ``always`` - load for the each debugging session, **default**
* ``modified`` - load only when firmware was modified
* ``manual`` - do not load firmware automatically. You are responsible to
  pre-flash target with debugging firmware in this case.

.. _projectconf_debug_server:

``debug_server``
^^^^^^^^^^^^^^^^

Allows one to setup a custom debugging server. By default, boards are pre-configured
with a debugging server that is compatible with "on-board" debugging tool
(adapter, probe). Also, this option is useful for a
:ref:`debugging_tool_custom` debugging tool.

**Option format (multi-line)**:

* First line is an executable path of debugging server
* 2-nd and the next lines are arguments for executable file

**Example:**

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

.. _projectconf_debug_port:

``debug_port``
^^^^^^^^^^^^^^

A debugging port of a remote target. Could be a serial device or network address.
PlatformIO detects it automatically if is not specified.

For example:

* ``/dev/ttyUSB0`` - Unix-based OS
* ``COM3`` - Windows OS
* ``localhost:3333``

.. _projectconf_debug_svd_path:

``debug_svd_path``
^^^^^^^^^^^^^^^^^^

A custom path to `SVD file <https://www.keil.com/pack/doc/CMSIS/SVD/html/svd_Format_pg.html>`_
which contains information about device peripherals.
