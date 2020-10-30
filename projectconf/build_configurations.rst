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

.. _build_configurations:

Build Configurations
====================

There are 2 types (:ref:`projectconf_build_type`) of build configuration in
PlatformIO:

:``release``:
  **Default configuration**. A "release" configuration of your firmware/program
  does not contain symbolic debug information and is optimized for the firmware
  size or speed (depending on :ref:`platforms`)

:``debug``:
  A "debug" configuration of your firmware/program is compiled with full
  symbolic debug information and no optimization. Optimization complicates
  debugging, because the relationship between source code and generated
  instructions is more complex.

.. note::
  If you need to control build flags that are specific for debug configuration please
  refer to :ref:`projectconf_debug_build_flags`.

If you need to build a project in ``debug`` configuration, please use one of
these options:

* Add :ref:`projectconf_build_type` with ``debug`` value to :ref:`projectconf`
* Use target ``debug`` for the :option:`pio run --target` command.

.. note::
  :ref:`piodebug` automatically switches to ``debug`` configuration when you do
  project debugging from :ref:`pioide` or use the :ref:`cmd_debug` command.

  To avoid having :ref:`piodebug` rebuild the project, please create a
  separate build environment that defines ``build_type = debug``. See
  the example below where the ``mydebug`` build environment will be used
  automatically by :ref:`piodebug`:

  .. code-block:: ini

     [env]
     platform = ...
     board = ...
     framework = ...
     ... other common configuration

     [env:myrelease]
     some_extra_options = ...

     [env:mydebug]
     build_type = debug
     some_extra_options = ...

Please note that you can set a default build environment per a project using the
:ref:`projectconf_pio_default_envs` option in :ref:`projectconf_section_platformio`.
