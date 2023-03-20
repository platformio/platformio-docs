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

Each project may have multiple *configuration environments* defining
the available project tasks for building, programming, debugging, unit
testing, device monitoring, library dependencies, etc. The
configuration environments are declared using ``[env]`` sections in
:ref:`projectconf`.

The allowed options are listed under `Options`_.

Common ``[env]``
----------------

An optional configuration environment with common options that will be
shared between all ``[env:NAME]`` environments in the platformio.ini
file. It is very useful if the configuration file has a lot of
environments ``[env:NAME]`` and they share common settings.

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

In this example we have two configuration environments ``release``
and ``debug``. This is equivalent to duplicating all options as shown below:

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

.. _projectconf_section_env_named:

Working ``[env:NAME]``
----------------------

A working environment in PlatformIO is defined using the ``[env:NAME]`` syntax.
This environment is used by various PlatformIO commands such as :ref:`cmd_run`,
:ref:`cmd_test`, :ref:`cmd_check`, :ref:`cmd_debug`, and others.
Every project must define at least one working environment.

You can define multiple working environments in your project by using different
names for the ``[env:NAME]`` section. It's important to note that each
environment must have a unique name. The name should only include lowercase
letters ``a-z``, numbers ``0-9``, and special characters ``_`` (underscore) and
``-`` (hyphen). For example, ``[env:hello_world]`` is a valid name.

If you have defined multiple working environments and you only want to process
a subset of them, you can use the ``-e`` or ``--environment`` option with the
PlatformIO commands mentioned above. You can specify the name of the environment
you want to process using this option.

In addition to using the ``-e`` option, you can define a default set of working
environments for the PlatformIO commands to process by using the ``[platformio]``
:ref:`projectconf_pio_default_envs` option. This can be useful if you frequently
work with a specific set of environments and don't want to specify them
every time you run a command.

Options
-------

.. toctree::
    :maxdepth: 2

    options/platform/index
    options/build/index
    options/library/index
    options/upload/index
    options/monitor/index
    options/check/index
    options/test/index
    options/debug/index
    options/advanced/index
