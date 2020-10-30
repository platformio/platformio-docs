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

.. _cmd_debug:

pio debug
=========

Helper command for :ref:`piodebug`.

.. contents::

Usage
-----

.. code-block:: bash

    pio debug [OPTIONS]

    # A binary shortcut for "pio debug --interface=gdb" command
    piodebuggdb [GDB OPTIONS]


Description
-----------

Prepare PlatformIO project for debugging or launch debug server.


Options
-------

.. program:: pio debug

.. option::
    -e, --environment

Debug specified environments.

You can also specify which environments should be used for debugging by default
using :ref:`projectconf_pio_default_envs` option from :ref:`projectconf`.

.. option::
    -d, --project-dir

Specify the path to a project directory. By default, ``--project-dir`` is equal
to a current working directory (``CWD``).

.. option::
    -c, --project-conf

Process project with a custom :ref:`projectconf`.

.. option::
    --interface

PlatformIO Debugging Interface. Valid values:

* ``gdb`` - GDB: The GNU Project Debugger

.. option::
    -v, --verbose

Shows detailed information when processing environments.

This option can also be set globally using :ref:`setting_force_verbose` setting
or by environment variable :envvar:`PLATFORMIO_SETTING_FORCE_VERBOSE`.

Examples
--------

1. Prepare a project for debugging

.. code::

    > pio debug

    [Sun Apr 30 01:34:01 2017] Processing mzeropro (platform: atmelsam; debug_extra_cmds: b main.cpp:26; board: mzeropro; framework: arduino)
    -----------------------------------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    Collected 26 compatible libraries
    Looking for dependencies...
    Project does not have dependencies
    Compiling .pio/build/mzeropro/src/main.o
    Compiling .pio/build/mzeropro/FrameworkArduinoVariant/variant.o
    Compiling .pio/build/mzeropro/FrameworkArduino/IPAddress.o
    Compiling .pio/build/mzeropro/FrameworkArduino/Print.o
    Archiving .pio/build/mzeropro/libFrameworkArduinoVariant.a
    Indexing .pio/build/mzeropro/libFrameworkArduinoVariant.a
    ...
    Compiling .pio/build/mzeropro/FrameworkArduino/wiring_analog.o
    Compiling .pio/build/mzeropro/FrameworkArduino/wiring_digital.o
    Compiling .pio/build/mzeropro/FrameworkArduino/wiring_private.o
    Compiling .pio/build/mzeropro/FrameworkArduino/wiring_shift.o
    Archiving .pio/build/mzeropro/libFrameworkArduino.a
    Indexing .pio/build/mzeropro/libFrameworkArduino.a
    Linking .pio/build/mzeropro/firmware.elf
    Calculating size .pio/build/mzeropro/firmware.elf
    Building .pio/build/mzeropro/firmware.bin
    text       data     bss     dec     hex filename
    11512       256    1788   13556    34f4 .pio/build/mzeropro/firmware.elf
    =========================== [SUCCESS] Took 7.82 seconds ===========================

2. Launch GDB instance and load initial configuration per a project

.. code::

    > pio debug --interface=gdb -x .pioinit

    ...
    Loading section .text, size 0x2c98 lma 0x4000
    Loading section .ramfunc, size 0x60 lma 0x6c98
    Loading section .data, size 0x100 lma 0x6cf8
    Start address 0x47b0, load size 11768
    Transfer rate: 4 KB/sec, 3922 bytes/write.
    target halted due to debug-request, current mode: Thread
    xPSR: 0x81000000 pc: 0x000028f4 msp: 0x20002c00
    target halted due to debug-request, current mode: Thread
    xPSR: 0x81000000 pc: 0x000028f4 msp: 0x20002c00
    Breakpoint 2 at 0x413a: file src/main.cpp, line 26.
