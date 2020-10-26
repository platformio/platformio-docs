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

.. _cmd_lib:

Library Manager CLI
===================

Usage
-----

.. code-block:: bash

    # To print all available commands and options use
    pio lib --help
    pio lib COMMAND --help

Options
-------

.. program:: pio lib

.. option::
    -d, --storage-dir

Manage custom library storage. It can be used later for the
:ref:`projectconf_lib_extra_dirs` option from :ref:`projectconf`.
Multiple options are allowed.

.. option::
    -g, --global

Manage global PlatformIO's library storage (
":ref:`projectconf_pio_core_dir`/lib") where :ref:`ldf` will look for
dependencies by default.

.. option::
    -e, --environment

Manage libraries for the specific project build environments declared in
:ref:`projectconf`. Works for ``--storage-dir`` which is valid PlatformIO
project.

Demo
----

.. image:: ../../../_static/images/platformio-demo-lib.gif

Commands
--------

.. toctree::
    :maxdepth: 2

    cmd_builtin
    cmd_install
    cmd_list
    cmd_register
    cmd_search
    cmd_show
    cmd_stats
    cmd_uninstall
    cmd_update
