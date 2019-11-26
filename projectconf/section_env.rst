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

.. _projectconf_section_env:

Section ``[env]``
=================

.. contents::
    :local:

Allows declaring configuration environments for building, programming, debugging,
unit testing, device monitoring, library dependencies, etc.

Common ``[env]``
----------------

.. versionadded:: 4.0

Allows declaring a configuration environment with common options that will be shared
between all ``[env:NAME]`` environments in :ref:`projectconf`. It is very useful if
the configuration file has a lot of custom environments ``[env:NAME]`` and they have
common data.

For example:

.. code-block:: ini

    [env]
    platform = ststm32
    framework = stm32cube
    board = nucleo_l152re
    lib_deps = Dep1, Dep2

    [env:release]
    build_flags = -D RELEASE
    lib_deps =
        ${env.lib_deps}
        Dep3

    [env:debug]
    build_type = debug
    build_flags = -D DEBUG
    lib_deps = DepCustom

In this example we have 2 configuration environments ``release`` and ``debug``. This
is the same if you duplicate all options:

.. code-block:: ini

    [env:release]
    platform = ststm32
    framework = stm32cube
    board = nucleo_l152re
    build_flags = -D RELEASE
    lib_deps = Dep1, Dep2, Dep3

    [env:debug]
    platform = ststm32
    framework = stm32cube
    board = nucleo_l152re
    build_type = debug
    build_flags = -D DEBUG
    lib_deps = DepCustom


Environment ``[env:NAME]``
--------------------------

A section with ``env:`` prefix is used to define **a working environment** for
:ref:`cmd_run`, :ref:`cmd_test`, :ref:`cmd_check`, :ref:`cmd_debug`, and other commands.
Project should contain as minimum one working environment.

Each environment must have a unique ``NAME``. The valid chars for ``NAME`` are
letters ``a-z``, numbers ``0-9``,  special char ``_`` (underscore).
For example, ``[env:hello_world]``.
Multiple ``[env:NAME]`` environments with different ``NAME`` are allowed.

If you have more than one working environment and you need to process only a few
of them, please check ``-e, --environment`` option for commands mentioned above
or :ref:`projectconf_pio_default_envs` option.

Options
-------

.. toctree::
    :maxdepth: 2

    section_env_platform
    section_env_build
    section_env_library
    section_env_upload
    section_env_monitor
    section_env_check
    section_env_test
    section_env_debug
    section_env_advanced
