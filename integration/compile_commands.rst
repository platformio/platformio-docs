
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

.. _compilation_db:

Compilation database ``compile_commands.json``
----------------------------------------------

A `compilation database <https://clang.llvm.org/docs/JSONCompilationDatabase.html>`_ is
a `JSON-formatted <https://www.json.org/>`_ file named ``compile_commands.json`` that
contains structured data about every compilation unit in your project.

:ref:`piocore` supports generating of compilation database using
:option:`pio run --target` command and ``compiledb`` target. For example,

.. code::

  > pio run -t compiledb


A default path for ``compile_commands.json`` is ":ref:`projectconf_pio_build_dir`/envname".
You can override this path with :ref:`projectconf_advanced_scripting` and
``COMPILATIONDB_PATH`` environment variable. For example, generate ``compile_commands.json``
in a root of project:


``platformio.ini``:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    extra_scripts = post:extra_script.py


``extra_script.py``:

.. code-block:: python

    import os
    Import("env")

    env.Replace(COMPILATIONDB_PATH=os.path.join("$PROJECT_DIR", "compile_commands.json"))
