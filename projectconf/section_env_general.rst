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
---------------

.. contents::
    :local:

.. _projectconf_env_platform:

``platform``
^^^^^^^^^^^^

Type: ``String`` | Multiple: ``No``

:ref:`platforms` name.

PlatformIO allows one to use specific version of platform using
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

.. _projectconf_env_platform_packages:

``platform_packages``
^^^^^^^^^^^^^^^^^^^^^

.. versionadded:: 4.0

Type: ``String`` | Multiple: ``Yes``

Configure custom packages per a build environment. You can also override
default packages by :ref:`platforms` using the same name. Packages will be
installed in :ref:`projectconf_pio_packages_dir`.

Examples:

.. code-block:: ini

    [env:override_default_toolchain]
    platform = atmelavr
    platform_packages =
        # use GCC AVR 5.0+
        toolchain-gccarmnoneeabi@>1.50000.0

    [env:override_framework]
    platform = espressif8266
    platform_packages =
        # use upstream Git version
        framework-arduinoespressif8266 @ https://github.com/esp8266/Arduino.git

    [env:external_package]
    platform = ststm32
    platform_packages =
        # latest openOCD from PlatformIO Package Registry
        tool-openocd

        # source code of ST-Link
        tool-stlink-source @ https://github.com/texane/stlink.git

.. _projectconf_env_framework:

``framework``
^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``Yes``

:ref:`frameworks` name.
