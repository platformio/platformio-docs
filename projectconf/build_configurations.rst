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

.. versionadded:: 3.6.1

There are 2 types of build configurations in PlatformIO:

:Release:
	**Default configuration**. The release configuration of your firmware/program
	does not contain symbolic debug information and is fully optimized.

:Debug:
	The debug configuration of your firmware/program is compiled with full
	symbolic debug information and no optimization. Optimization complicates
	debugging, because the relationship between source code and generated
	instructions is more complex.

As we mentioned before, PlatformIO builds project in ``Release`` configuration
by default. You can build project in ``Debug`` configuration using one of
these options:

* Using target ``debug`` for :option:`platformio run --target` command
* Using :ref:`projectconf_targets` option in :ref:`projectconf` per build
  environment.

:ref:`piodebug` automatically switches to "Debug" configuration when you do
project debugging from :ref:`pioide` or use :ref:`cmd_debug` command.

.. note::
  If you use the same build environment for "Release" and for :ref:`piodebug`,
  PlatformIO will rebuild your project each time when you switch between
  build configurations. To avoid this issue, please declare 2 separate
  project build environments in :ref:`projectconf` as described below in example.

  Otherwise, please add ``targets = debug`` to your build environment and
  PlatformIO will build project using "Debug" configuration even when you
  do not use :ref:`piodebug`.

--------------

**Example** of classic "release" and "debug" scheme using :ref:`projectconf`

.. code-block:: ini

   [env:debug]
   platform = ...
   board = ...
   framework = ...
   targets = debug

   [env:release]
   platform = ...
   board = ...
   framework = ...

* :ref:`cmd_run` command builds ALL environments and places artifacts to
  :ref:`projectconf_pio_build_dir`
* ``platformio run --environment debug`` builds only ``debug`` environment
* ``platformio run --environment release`` builds only ``release`` environment.
* ``platformio run --environment release --target upload`` builds project using
  "Release" configuration and upload firmware/artifacts to end device.

Please note that you can set a default build environment per a project using
:ref:`projectconf_pio_env_default` option in :ref:`projectconf_section_platformio`.
