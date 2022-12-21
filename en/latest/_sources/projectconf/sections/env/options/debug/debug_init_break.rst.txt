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

.. _projectconf_debug_init_break:

``debug_init_break``
--------------------

Type: ``String`` | Multiple: ``No`` | Default: ``tbreak main``

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
