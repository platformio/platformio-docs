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

Configuration
-------------

.. contents::
  :local:

Drivers
~~~~~~~

See "Drivers" section for :ref:`debugging_tool_ftdi` debug probe.

AutoTiler
~~~~~~~~~

You need GAP8 AutoTiler library, please request it via
`support@greenwaves-technologies.com <mailto:support@greenwaves-technologies.com>`_

Put a library somewhere on a disk and add this folder to library path using
:ref:`projectconf_build_flags` in :ref:`projectconf`. For example,

  .. code-block:: ini

    [env:gapuino]
    platform = riscv_gap
    board = gapuino
    framework = ...
    build_flags = -L/path/to/libtile/folder


Running modes
~~~~~~~~~~~~~

GAPuino supports 2 main modes:

1. Running from RAM, ``boot_mode=jtag``
2. Running from HyperFlash, ``boot_mode=jtag_hyper``

A running process can be controlled through the internal upload commands:

* ``load``, @TODO
* ``reqloop``, @TODO
* ``ioloop``, @TODO
* ``start``, @TODO
* ``wait``, @TODO

You can configure "boot mode" and list of upload commands using :ref:`projectconf`.
Default values are:

* ``board_upload.boot_mode = jtag``
* ``board_upload.commands = load reqloop ioloop start wait``

Run from RAM
^^^^^^^^^^^^

This is a default behavior when you run "Upload" task in :ref:`pioide` or use
:ref:`piocore` and :option:`pio run --target` command with ``upload`` target.

Run from RAM (without any bridge interaction)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Configure build environment using :ref:`projectconf` as described below

  .. code-block:: ini

    [env:gapuino]
    platform = riscv_gap
    board = gapuino
    framework = ...
    board_upload.commands = load start

* Run "Upload" task in :ref:`pioide` or use :ref:`piocore` and
  :option:`pio run --target` command with ``upload`` target.

Flash and run from RAM
^^^^^^^^^^^^^^^^^^^^^^

The same as :ref:`platform_riscv_gap_uploadfs`.

Flash and run from Flash
^^^^^^^^^^^^^^^^^^^^^^^^

* Configure build environment using :ref:`projectconf` as described below

  .. code-block:: ini

    [env:gapuino]
    platform = riscv_gap
    board = gapuino
    framework = ...
    board_upload.boot_mode = jtag_hyper
    board_upload.commands = reqloop ioloop start wait

* Perform :ref:`platform_riscv_gap_uploadfs`.

Run from Flash
^^^^^^^^^^^^^^

.. note::
  You have to perform :ref:`platform_riscv_gap_uploadfs` before.

* Configure build environment using :ref:`projectconf` as described below

  .. code-block:: ini

    [env:gapuino]
    platform = riscv_gap
    board = gapuino
    framework = ...
    board_upload.boot_mode = jtag_hyper
    board_upload.commands = reqloop ioloop start wait

* Run "Upload" task in :ref:`pioide` or use :ref:`piocore` and
  :option:`pio run --target` command with ``upload`` target.

Run from Flash (without any bridge interaction)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
  You have to perform :ref:`platform_riscv_gap_uploadfs` before.

* Configure build environment using :ref:`projectconf` as described below

  .. code-block:: ini

    [env:gapuino]
    platform = riscv_gap
    board = gapuino
    framework = ...
    board_upload.boot_mode = jtag_hyper
    board_upload.commands = start

* Run "Upload" task in :ref:`pioide` or use :ref:`piocore` and
  :option:`pio run --target` command with ``upload`` target.

.. _platform_riscv_gap_uploadfs:

Uploading files to HyperFlash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create new project using :ref:`pioide` or initialize project using
   :ref:`piocore` and :ref:`cmd_project_init` (if you have not initialized it yet)
2. Create ``data`` folder (it should be on the same level as ``src`` folder)
   and put files here. Also, you can specify own location for
   :ref:`projectconf_pio_data_dir`
3. Run "Upload File System image" task in :ref:`pioide` or use :ref:`piocore`
   and :option:`pio run --target` command with ``uploadfs`` target.

Examples:

* `PULP OS File System <https://github.com/pioplus/platform-riscv_gap/tree/develop/examples/gapuino-pulp-os-filesystem>`_
