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

Custom firmware/program name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes is useful to have a different firmware/program name in
:ref:`projectconf_pio_build_dir`.

``platformio.ini``:

.. code-block:: ini

    [env:env_custom_prog_name]
    platform = espressif8266
    board = nodemcuv2
    framework = arduino
    build_flags = -D VERSION=13
    extra_scripts = pre:extra_script.py

``extra_script.py``:

.. code-block:: python

    Import("env")

    build_flags = env.ParseFlags(env["BUILD_FLAGS"])
    cppdefines = build_flags.get("CPPDEFINES") or {}
    if cppdefines:
        cppdefines = dict(
            # Support "unvalued" defines, like `-DFOO`.
            (kv_or_k, None) if isinstance(kv_or_k, str) else kv_or_k
            for kv_or_k in cppdefines
        )
    # print(cppdefines)

    env.Replace(PROGNAME="firmware_%s" % cppdefines.get("VERSION"))
