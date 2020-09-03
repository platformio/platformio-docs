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

.. _debugging_tool_custom:

Custom
======

:Configuration:
  :ref:`projectconf_debug_tool` = ``custom``


**PLatformIO Debugging Solution** can be configured using :ref:`projectconf`:

.. toctree::
  :maxdepth: 2

  ../../projectconf/section_env_debug

Examples
--------

.. contents::
    :local:

J-Link and ST Nucleo
~~~~~~~~~~~~~~~~~~~~

Segger J-Link probe and ST Nucleo F446RE board in pair with J-Link GDB Server:

* Install `J-Link GDB Server <https://www.segger.com/products/debug-probes/j-link/tools/j-link-gdb-server/about-j-link-gdb-server/?utm_source=platformio&utm_medium=docs>`_
* `Convert ST-LINK On-Board Into a J-Link <https://www.segger.com/products/debug-probes/j-link/models/other-j-links/st-link-on-board/?utm_source=platformio&utm_medium=docs>`_

.. note::

  You can use configuration below in pair with other boards, not only with ST
  Nucleo F446RE. In this case, please replace ``STM32F446RE`` with
  your own device name in ``debug_server`` option.

  See full list with `J-Link Supported Devices <https://www.segger.com/downloads/supported_devices_jlink.php?utm_source=platformio&utm_medium=docs>`__.


.. code-block:: ini

    [env:debug_jlink]
    platform = ststm32
    framework = mbed
    board = nucleo_f446re

    debug_tool = custom
    debug_port = :2331

    debug_server =
      /full/path/to/JLinkGDBServerCL
      -singlerun
      -if
      SWD
      -select
      USB
      -port
      2331
      -device
      STM32F446RE

    debug_init_cmds =
      define pio_reset_halt_target
          monitor reset
          monitor halt
      end
      define pio_reset_run_target
          monitor clrbp
          monitor reset
          monitor go
      end
      target extended-remote $DEBUG_PORT
      monitor clrbp
      monitor speed auto
      pio_reset_halt_target
      $LOAD_CMDS
      $INIT_BREAK

J-Link as debugger and uploader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Segger J-Link probe as debugger and uploader for a custom board.
If you plan to use with other board, please change device ``MK20DX256xxx7``
to a valid identifier. See supported J-Link devices at :ref:`debugging_tool_jlink`.

* Install `J-Link GDB Server <https://www.segger.com/products/debug-probes/j-link/tools/j-link-gdb-server/about-j-link-gdb-server/?utm_source=platformio&utm_medium=docs>`_


.. code-block:: ini

    [env:jlink_debug_and_upload]
    platform = teensy
    framework = arduino
    board = teensy31
    extra_scripts = extra_script.py
    upload_protocol = custom
    debug_tool = jlink
    debug_server =
      /full/path/to/JLinkGDBServerCL
      -singlerun
      -if
      SWD
      -select
      USB
      -port
      2331
      -device
      MK20DX256xxx7

**extra_script.py**

Place this file on the same level as :ref:`projectconf`.

.. code-block:: py

    from os import makedirs
    from os.path import isdir, join
    Import('env')

    def _jlink_cmd_script(env, source):
        build_dir = env.subst("$BUILD_DIR")
        if not isdir(build_dir):
            makedirs(build_dir)
        script_path = join(build_dir, "upload.jlink")
        commands = ["h", "loadbin %s,0x0" % source, "r", "q"]
        with open(script_path, "w") as fp:
            fp.write("\n".join(commands))
        return script_path

    env.Replace(
        __jlink_cmd_script=_jlink_cmd_script,
        UPLOADER="/full/path/to/JLink",
        UPLOADERFLAGS=[
            "-device", "MK20DX256xxx7",
            "-speed", "4000",
            "-if", "swd",
            "-autoconnect", "1"
        ],
        UPLOADCMD='"$UPLOADER" $UPLOADERFLAGS -CommanderScript ${__jlink_cmd_script(__env__, SOURCE)}'
    )


ST-Util and ST-Link
~~~~~~~~~~~~~~~~~~~

On-board ST-Link V2/V2-1 in pair with `ST-Util GDB Server <https://github.com/texane/stlink>`_:

.. code-block:: ini

    [env:debug]
    platform = ststm32
    framework = mbed
    board = ...
    debug_tool = custom
    debug_port = :4242
    debug_server = $PLATFORMIO_CORE_DIR/packages/tool-stlink/bin/st-util

OpenOCD and ST-Link
~~~~~~~~~~~~~~~~~~~

On-board ST-Link V2/V2-1 in pair with `OpenOCD GDB Server <http://openocd.org>`_:

.. code-block:: ini

    [env:debug]
    platform = ststm32
    framework = mbed
    board = ...
    debug_tool = custom
    debug_server =
      $PLATFORMIO_CORE_DIR/packages/tool-openocd/bin/openocd
      -f
      $PLATFORMIO_CORE_DIR/packages/tool-openocd/scripts/board/st_nucleo_f4.cfg

pyOCD and CMSIS-DAP
~~~~~~~~~~~~~~~~~~~

Using pyOCD for CMSIS-DAP based boards

Firstly, please install `pyOCD <https://github.com/mbedmicro/pyOCD>`__ and
check that ``pyocd-gdbserver --version`` command works.

.. code-block:: ini

    [env:debug]
    platform = ...
    board = ...
    framework = mbed
    debug_tool = custom
    debug_server = pyocd-gdbserver

