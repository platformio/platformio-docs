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

.. _projectconf_section_env_general:

General options
~~~~~~~~~~~~~~~

.. contents::
    :local:

.. _projectconf_env_platform:

``platform``
^^^^^^^^^^^^

:ref:`platforms` name.

PlatformIO allows to use specific version of platform using
`Semantic Versioning <http://semver.org>`_ (X.Y.Z=MAJOR.MINOR.PATCH) or VCS
(Git, Mercurial and Subversion).

Version specifications can take any of the following forms:

* ``1.2.3``: an exact version number. Use only this exact version
* ``^1.2.3``: any compatible version (exact version for ``1.x.x`` versions)
* ``~1.2.3``: any version with the same major and minor versions, and an
  equal or greater patch version
* ``>1.2.3``: any version greater than ``1.2.3``. ``>=``, ``<``, and ``<=``
  are also possible
* ``>0.1.0,!=0.2.0,<0.3.0``: any version greater than ``0.1.0``, not equal to
  ``0.2.0`` and less than ``0.3.0``

Other forms are the same as for the  :ref:`cmd_platform_install` command.

Examples:

.. code-block:: ini

    [env:the_latest_version]
    platform = atmelavr

    [env:exact_version]
    platform = atmelavr@1.2.3

    [env:specific_major_version]
    platform = atmelavr@^1.2.3

    [env:specific_major_and_minor_version]
    platform = atmelavr@~1.2.3

    [env:development_verion_by_git]
    platform = https://github.com/platformio/platform-ststm32.git

    [env:custom_git_branch]
    platform = https://github.com/platformio/platform-espressif8266.git#feature/stage

    [env:specific_git_commit]
    platform = https://github.com/platformio/platform-espressif8266.git#921855a9c530082efddb5d48b44c3f4be0e2dfa2

.. _projectconf_env_framework:

``framework``
^^^^^^^^^^^^^

:ref:`frameworks` name.

The multiple frameworks are allowed, *split them with comma+space ", "*.

.. _projectconf_env_board:

``board``
^^^^^^^^^

*PlatformIO* has pre-configured settings for the most popular boards:

- build configuration
- upload configuration
- debugging configuration
- connectivity information, etc.

You can find a valid  ``board`` ID in :ref:`boards` catalog,
`Boards Explorer <https://platformio.org/boards>`_ or
:ref:`cmd_boards` command.

.. _projectconf_targets:

``targets``
^^^^^^^^^^^

A list with targets which will be processed by :ref:`cmd_run` command by
default. You can enter more than one target, please split them with
comma+space **", "**.

The list with available targets is located in :option:`platformio run --target`.

**Examples**

1. Build a project using :ref:`Release Configuration <build_configurations>`,
   upload firmware, and start :ref:`Serial Monitor <cmd_device_monitor>`
   automatically:

    .. code-block:: ini

       [env:upload_and_monitor]
       targets = upload, monitor

2. Build a project using :ref:`Debug Configuration <build_configurations>`.


**Tip!** You can use these targets like an option to
:option:`platformio run --target` command. For example:

.. code-block:: bash

    # clean project
    platformio run -t clean

    # dump current build environment
    platformio run --target envdump

When no targets are defined, *PlatformIO* will build only sources by default.