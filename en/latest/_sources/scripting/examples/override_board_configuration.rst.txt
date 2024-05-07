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

Override board configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PlatformIO allows one to override some basic options (integer or string values)
using :ref:`projectconf_board_more_options` in :ref:`projectconf`.
Sometimes you need to do complex changes to default board manifest and
extra PRE scripting work well here. See example below how to override default
hardware VID/PIDs.

.. warning::
    Due to a technical limitation these board changes will not work for
    :ref:`cmd_device_monitor` command.

``platformio.ini``:

.. code-block:: ini

    [env:uno]
    platform = atmelavr
    board = uno
    framework = arduino
    extra_scripts = pre:custon_hwids.py

``custon_hwids.py``:

.. code-block:: python

    Import("env")

    board_config = env.BoardConfig()
    # should be array of VID:PID pairs
    board_config.update("build.hwids", [
      ["0x2341", "0x0243"],  # 1st pair
      ["0x2A03", "0x0043"],  # 2nd pair, etc.
    ])
