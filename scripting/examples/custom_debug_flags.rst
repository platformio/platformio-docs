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

Custom debug flags
~~~~~~~~~~~~~~~~~~

PlatformIO removes all debug/optimization flags before a debug session or when
:ref:`build_configurations` is set to ``debug`` and overrides them with
``-0g -g2 -ggdb2`` for ``ASFLAGS``, ``CCFLAGS``, and ``LINKFLAGS`` build
scopes.

An extra script allows us to override PlatformIO's default behavior and declare
custom flags. See example below where we override ``-Og`` with ``-O0``:

``platformio.ini``:

.. code-block:: ini

    [env:teensy31]
    platform = teensy
    board = teensy31
    framework = arduino
    extra_scripts = custom_debug_flags.py

``custom_debug_flags.py``:

.. code-block:: python

    Import("env")

    if env.GetBuildType() == "debug":
       for scope in ("ASFLAGS", "CCFLAGS", "LINKFLAGS"):
          for i, flag in enumerate(env[scope]):
             if flag == "-Og":
                env[scope][i] = "-O0"