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

.. _projectconf_env_platform:

``platform``
^^^^^^^^^^^^

Type: ``Package Specification`` | Multiple: ``No``

Specify a development platform that provides integration of vendor-specific
boards (development kits, MCUs), high-level frameworks, and SDKs.
See :ref:`cmd_pkg_install_specifications` for details.

`PlatformIO Registry <https://registry.platformio.org>`__ allows you to explore
supported development platforms, boards, frameworks, and toolchains.

For the advanced platform configuration, please check the :ref:`platforms` documentation.

Example of using a `Espressif 32 development platform <https://registry.platformio.org/platforms/platformio/espressif32>`_:

.. code-block:: ini

    [env:recommended_specification]
    ; allow backwards-compatible new functionality and bug-fixes
    platform = platformio/espressif32@^6.1.0

    [env:allow_only_bug_fixes]
    platform = platformio/espressif32@~6.1.0

    [env:exact_version]
    platform = platformio/espressif32@6.1.0

    [env:latest_version]
    ; not recommended as it does not ensure that
    ; - builds are repeatable
    ; - all developers who checkout the project will build against the same platform version
    platform = platformio/espressif32

    [env:development_verion_by_git]
    platform = https://github.com/platformio/platform-espressif32.git

    [env:custom_git_branch]
    platform = https://github.com/platformio/platform-espressif32.git#master

    [env:specific_git_commit]
    platform = https://github.com/platformio/platform-espressif32.git#f8340a2081a31c2ac8ed2b16907f2a21dc8897d4


.. note::
    We highly recommend pinning the platform to a version.
    See :ref:`cmd_pkg_install_requirements` for details.
