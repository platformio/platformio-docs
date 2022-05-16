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

.. _scripting_custom_targets:

Custom Targets
--------------

PlatformIO allows you to declare unlimited number of the custom targets. There are a
lot of use cases for them:

- Pre/Post processing based on a dependent sources (other target, source file, etc.)
- Command launcher with own arguments
- Launch command with custom options declared in :ref:`projectconf`
- Python callback as a target (use the power of Python interpreter and PlatformIO Build API).

A custom target can be processed using :option:`pio run --target` option and
you can list them via :option:`pio run --list-targets` command.

Build System API
~~~~~~~~~~~~~~~~

.. code-block:: python

    Import("env")

    env.AddCustomTarget(
        name,
        dependencies,
        actions,
        title=None,
        description=None,
        always_build=True
    )


``AddCustomTarget`` arguments:

:name:
    A name of target. ASCII chars (a-z, 0-9, _, -) are recommended. Good names are
    "gen_headers", "program_bitstream", etc.

:dependencies:
    A list of dependencies that should be built BEFORE target will be launched. It is
    possible pass multiple dependencies as a Python list ``["dep1", dep_target_2]``.
    If a target does not have dependencies, ``None`` should be passed.

:actions:
    A list of actions to call on a target. It is possible to pass multiple actions as
    a Python list ``["python --version", my_calback]``.

:title:
    A title of a target. It will be printed when using :ref:`piocore` or :ref:`pioide`.
    We recommend to keep a title very short, 1-2 words.

:description:
    The same as a ``title`` argument but allows you to provide detailed explanation
    what target does.

:always_build:
    If there are declared ``dependencies`` and they are already built, this target
    will not be called if ``always_build=False``. A default value is
    ``always_build=True`` and means always building/calling target.


Examples
~~~~~~~~

Command shortcut
^^^^^^^^^^^^^^^^

Create a custom ``node`` target (alias) which will print a NodeJS version

``platformio.ini``:

.. code-block:: ini

    [env:myenv]
    platform = ...
    ...
    extra_scripts = extra_script.py

``extra_script.py``:

.. code-block:: python

    Import("env")

    # Single action/command per 1 target
    env.AddCustomTarget("sysenv", None, 'python -c "import os; print(os.environ)"')

    # Multiple actions
    env.AddCustomTarget(
        name="pioenv",
        dependencies=None,
        actions=[
            "pio --version",
            "python --version"
        ],
        title="Core Env",
        description="Show PlatformIO Core and Python versions"
    )


Now, run ``pio run --target sysenv`` or ``pio run -t pioenv`` (short version).

Dependent target
^^^^^^^^^^^^^^^^

Sometimes you need to run a command which depends on another target (file,
firmware, etc). Let's create an ``ota`` target and declare command which will
depend on a project firmware. If a build process successes, declared command
will be run.

``platformio.ini``:

.. code-block:: ini

    [env:myenv]
    platform = ...
    ...
    extra_scripts = extra_script.py


``extra_script.py``:

.. code-block:: python

    Import("env")

    env.AddCustomTarget(
        "ota",
        "$BUILD_DIR/${PROGNAME}.elf",
        "ota_script --firmware-path $SOURCE"
    )


Now, run ``pio run -t ota``.

Target with options
^^^^^^^^^^^^^^^^^^^

Let's create a simple ``ping`` target and process it with
``pio run --target ping`` command:

``platformio.ini``:

.. code-block:: ini

    [env:env_custom_target]
    platform = ...
    ...
    extra_scripts = extra_script.py
    custom_ping_host = google.com

``extra_script.py``:

.. code-block:: python

    Import("env")

    host = env.GetProjectOption("custom_ping_host")

    def mytarget_callback(*args, **kwargs):
        print("Hello PlatformIO!")
        env.Execute("ping " + host)


    env.AddCustomTarget("ping", None, mytarget_callback)
