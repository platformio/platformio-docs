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

.. _projectconf_debug_load_cmds:

``debug_load_cmds``
-------------------

Type: ``String`` | Multiple: ``Yes`` | Default: ``load``

Specify a command which will be used to load program/firmware to a target
device. Possible options:

* ``load`` - **default** option
* ``load [address]`` - load program at specified address, where "[address]"
  should be a valid number
* ``preload`` - some embedded devices have locked Flash Memory (a few
  Freescale Kinetis and NXP LPC boards). In this case, firmware loading using
  debugging client is disabled. ``preload`` command instructs
  :ref:`piocore` to load program/firmware using development platform "upload"
  method (via bootloader, media disk, etc)
* (empty value, ``debug_load_cmds =``), disables program loading at all.
* ``custom commands`` - pass any debugging client command (GDB, etc.)

Sometimes you need to run extra monitor commands (on debug server side) before
program/firmware loading, such as flash unlocking or erasing. In this case we
can combine service commands with loading and run them before. See example:

.. code-block:: ini

    [env:debug]
    platform = ...
    board = ...
    debug_load_cmds =
      monitor flash erase_sector 0 0 11
      load
