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

.. _cmd_pkg_exec:

pio pkg exec
============

.. contents::

Usage
-----

.. code-block:: bash

    pio pkg exec [OPTIONS] [ARGS]
    pio pkg exec -- <CMD> [ARGS]
    pio pkg exec --package <SPECIFICATION> -- <CMD> [ARGS]
    pio pkg exec --call '<cmd> [args]'

Description
-----------

Run command from a PlatformIO package.

.. note::
    A double-hyphen ``--`` flag is required before a command when passing its options.

Options
-------

.. program:: pio pkg exec

.. option::
    -p, --package

Run a command from the specified package using :ref:`cmd_pkg_install_specifications`.
If a package has not been installed yet,
PlatformIO will install it from the `PlatformIO Registry <https://registry.platformio.org>`__.

If a package is not provided, run an arbitrary command from the first matched installed package.

.. option::
    -c, --call

Run a command and its arguments specified as a string.

Examples
--------

1. Run an arbitrary command from the first matched installed package

.. code::

    > pio pkg exec -- openocd --help

    OpenOCD x86_64 Open On-Chip Debugger 0.11.0+dev (2021-10-17-00:18)
    Licensed under GNU GPL v2
    For bug reports, read
        http://openocd.org/doc/doxygen/bugs.html
    Open On-Chip Debugger
    Licensed under GNU GPL v2
    --help       | -h   display this help
    --version    | -v   display OpenOCD version
    --file       | -f   use configuration file <name>
    --search     | -s   dir to search for config files and scripts
    --debug      | -d   set debug level to 3
                 | -d<n>    set debug level to <level>
    --log_output | -l   redirect log output to file <name>
    --command    | -c   run <command>

2. Install JLink package and run GDB server

.. code::

    > pio pkg exec -p tool-jlink -- JLinkGDBServer -singlerun -if JTAG -select USB -jtagconf -1,-1 -device EFR32BG22CxxxF512 -port 2331