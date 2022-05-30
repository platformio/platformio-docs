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

``extraScript``
~~~~~~~~~~~~~~~

*Optional* | Type: ``String``

Launch extra script before build process.
More details :ref:`projectconf_extra_scripts`.

**Example** (HAL-based library)

This example demonstrates how to build HAL-dependent source files and
exclude other source files from a build process.

Project structure

.. code::

    ├── lib
    │   ├── README
    │   └── SomeLib
    │       ├── extra_script.py
    │       ├── hal
    │       │   ├── bar
    │       │   │   ├── hal.c
    │       │   │   └── hal.h
    │       │   ├── foo
    │       │       ├── hal.c
    │       │       └── hal.h
    │       ├── library.json
    │       ├── SomeLib.c
    │       └── SomeLib.h
    ├── platformio.ini
    └── src
        └── test.c

``platformio.ini``

.. code-block:: ini

    [env:foo]
    platform = native
    build_flags = -DHAL=foo

    [env:bar]
    platform = native
    build_flags = -DHAL=bar

``library.json``

.. code-block:: ini

    {
        "name": "SomeLib",
        "version": "0.0.0",
        "build": {
            "extraScript": "extra_script.py"
        }
    }

``extra_script.py``

.. code-block:: py

    Import('env')
    from os.path import join, realpath

    # private flags (only for the current "SomeLib" source files)
    for item in env.get("CPPDEFINES", []):
        if isinstance(item, tuple) and item[0] == "HAL":
            env.Append(CPPPATH=[realpath(join("hal", item[1]))])
            env.Replace(SRC_FILTER=["+<*>", "-<hal*>", "+<hal/%s>" % item[1]])
            break

    # pass flags to the global env (project files, frameworks)
    global_env = DefaultEnvironment()
    global_env.Append(CPPDEFINES=[("TEST_GLOBAL", 1)])

    # pass flags to the project dependencies (libraries)
    for lb in env.GetLibBuilders():
        lb.env.Append(CPPDEFINES=[("TEST_LIBDEPS", 1)])