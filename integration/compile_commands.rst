
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

You can generate a project ``compile_commands.json`` using the
:option:`pio run --target` command and ``compiledb`` target.
A default location for ``compile_commands.json`` is a project directory.

The following build variables can be used for customization using :ref:`scripting`:

.. list-table::
    :header-rows:  1
    :widths: 25 75

    * - Variable
      - Description
    * - ``COMPILATIONDB_PATH``
      - A path where the ``compile_commands.json`` file should be saved.
        A default location is the root of a project
    * - ``COMPILATIONDB_INCLUDE_TOOLCHAIN``
      - A boolean flag to control if toolchain paths should be included in the compilation unit.
        A default value is ``False``, only project-dependent includes are exported.

**Example**

Generate ``compile_commands.json`` with toolchain includes for each project environment
and save database to the ":ref:`projectconf_pio_build_dir`/envname" folder:

``platformio.ini``:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    extra_scripts = pre:extra_script.py

``extra_script.py``:

.. code-block:: python

    import os
    Import("env")

    # include toolchain paths
    env.Replace(COMPILATIONDB_INCLUDE_TOOLCHAIN=True)

    # override compilation DB path
    env.Replace(COMPILATIONDB_PATH=os.path.join("$BUILD_DIR", "compile_commands.json"))

Generate ``compile_commands.json``

.. code::

  > pio run -t compiledb
