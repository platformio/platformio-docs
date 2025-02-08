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

.. _scripting_envs:

Construction Environments
-------------------------

The PlatformIO Build System uses the following construction environments
to process a project:

*  ``DefaultEnvironment()`` - the global construction environment.

   It is used for the :ref:`platforms` and :ref:`frameworks` build scripts,
   :ref:`scripting_actions`, upload tools, :ref:`ldf`,
   and for other internal operations.

*  ``Import("projenv")`` - the isolated construction environment
   used for processing the project source code in :ref:`projectconf_pio_src_dir`.

   Please note that any :ref:`projectconf_build_src_flags` specified in
   :ref:`projectconf` will be passed to the ``projenv`` and not to the ``DefaultEnvironment()``.

   .. note::
      1. The ``projenv`` is available only for the POST-type scripts (see :ref:`scripting_launch_types`)
         and :ref:`library_json_buid_extra_script` (see :ref:`library_json`).
      2. Flags passed to the global construction environment using PRE-type scripts will affect the ``projenv`` too.

*  ``Import("env")`` - the current working construction environment.

   Imported ``env`` refers to the ``DefaultEnvironment()`` for scripts
   configured using the :ref:`projectconf_extra_scripts` option
   in :ref:`projectconf`.

   If you use :ref:`library_json` and :ref:`library_json_buid_extra_script`,
   the ``Import("env")`` refers to the library's isolated
   environment from which a script was called (not to the global environment).
   Please use ``env = DefaultEnvironment()`` instead to access the global
   environment.

--------

**Examples**

``my_pre_extra_script.py``:

.. code-block:: python

    # Import the current working construction
    # environment to the `env` variable.
    # alias of `env = DefaultEnvironment()`
    Import("env")

    # Dump construction environment (for debug purpose)
    print(env.Dump())

    # append extra flags to global build environment
    # which later will be used to build:
    # - project source code
    # - frameworks
    # - dependent libraries
    env.Append(CPPDEFINES=[
      "MACRO_1_NAME",
      ("MACRO_2_NAME", "MACRO_2_VALUE")
    ])


``my_post_extra_script.py``:

.. code-block:: python

    Import("env", "projenv")

    # Dump global construction environment (for debug purpose)
    print(env.Dump())

    # Dump project construction environment (for debug purpose)
    print(projenv.Dump())

    # append extra flags to global build environment
    # which later will be used to build:
    # - frameworks
    # - dependent libraries
    env.Append(CPPDEFINES=[
      "MACRO_1_NAME",
      ("MACRO_2_NAME", "MACRO_2_VALUE")
    ])

    # append extra flags to only project build environment
    projenv.Append(CPPDEFINES=[
      "PROJECT_EXTRA_MACRO_1_NAME",
      ("ROJECT_EXTRA_MACRO_2_NAME", "ROJECT_EXTRA_MACRO_2_VALUE")
    ])
