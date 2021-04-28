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

.. _projectconf_section_env_advanced:

Advanced options
----------------

.. _projectconf_env_extends:

``extends``
^^^^^^^^^^^

Type: ``String`` | Multiple: ``Yes``

This option allows one to inherit configuration from other sections or build environments
in :ref:`projectconf`. Multiple items are allowed, split them with ``,`` or
with a new line.

If you need to extend only a few options from some section, please take a look at
:ref:`projectconf_dynamic_vars`.

Example:

.. code-block:: ini

    [strict_ldf]
    lib_ldf_mode = chain+
    lib_compat_mode = strict

    [espressi32_base]
    platform = espressif32
    framework = arduino

    [env:release]
    extends = espressi32_base, strict_ldf
    board = esp32dev
    build_flags = -D RELEASE

    [env:debug]
    extends = env:release
    build_type = debug
    build_flags = -D DEBUG


.. _projectconf_extra_scripts:

``extra_scripts``
^^^^^^^^^^^^^^^^^

Type: ``FilePath`` | Multiple: ``Yes``

A list of PRE and POST extra scripts.

See details and examples in :ref:`projectconf_advanced_scripting` section.

If you plan to share these scripts with :ref:`pioremote` machine, please
put them to :ref:`projectconf_pio_shared_dir`.
