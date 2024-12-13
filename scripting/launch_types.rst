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

.. _scripting_launch_types:

Launch Types
------------

There are two execution types for extra scripts:

*  **PRE** - executes before the main script of :ref:`platforms`.

   Useful to pre-generate extra source files or make dynamic
   changes/patches to the existing, pass flags to the global
   building environment, add :ref:`scripting_middlewares`, etc.

   .. note::
      Please note that the ``projenv``
      (see :ref:`scripting_envs`) is not available at this stage.

*  **POST** - executes after the **PRE** and the main script of
   :ref:`platforms`.

   The building environment is fully constructed at this stage with
   all build flags, development platform targets, dependent libraries,
   and ``projenv``. Useful to assign :ref:`scripting_actions`,
   modify default build flags set by the development platform,
   or extend the building workflow.

The extra scripts can be configured using the :ref:`projectconf_extra_scripts`
option in :ref:`projectconf` or using the :ref:`library_json_buid_extra_script`
in :ref:`library_json` manifest.

The launch type can be specified as a prefix
(``pre:`` or ``post:``) to the script path.
If there is no prefix specified, the ``post:`` will be used automatically.

**Example**

.. code-block:: ini

  [env:my_env_1]
  platform = ...
  ; Defaults to POST script since no prefix is used
  extra_scripts = post_extra_script.py

  [env:my_env_2]
  platform = ...
  extra_scripts =
    pre:pre_extra_script.py
    post:post_extra_script1.py
    post_extra_script2.py

.. note::
   PlatformIO includes a service stage during runtime where it re-executes extra
   scripts to gather integration information intended for IDE plugins. If you want
   your scripts to run exclusively for the "build" target, include the following
   hook at the beginning of your script:

.. code-block:: python

   Import("env")

   if env.IsIntegrationDump():
      # stop the current script execution
      Return()

   # code below runs for the "build" and other targets
   env.Append(CPPDEFINES=["MACRO_NAME"])
