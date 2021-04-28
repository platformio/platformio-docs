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

.. _core_migration:

Migrating from 4.x to 5.0
=========================

Guidance on how to upgrade from :ref:`piocore` v4.x to v5.x with emphasis on
major changes, what is new, and what has been removed.

**PlatformIO Core 5.0 is fully backward compatible with PlatformIO 4.0 projects.**

Please read :ref:`PlatformIO 5.0 Release Notes <release_notes_5>` before.

.. contents:: Contents
  :local:

Migration Steps
---------------

1. Ensure that you do not use a short version of the Github declaration in :ref:`projectconf_lib_deps`.
   Please use ``https://github.com/username/repo.git`` instead of ``username/repo``.
2. We recommend updating your project dependency declarations in :ref:`projectconf_lib_deps`
   using a new owner-based syntax. See  the :ref:`core_migration_libmanager` section for details.

What is new
-----------

In this section, we are going to highlight the most important changes and
features introduced in :ref:`piocore` 5.0. Please visit
:ref:`PlatformIO 5.0 Release Notes <release_notes_5>` for more detailed information.

PlatformIO Trusted Registry
~~~~~~~~~~~~~~~~~~~~~~~~~~~

PlatformIO Core 5.0 has been switched to the official **PlatformIO Trusted Registry**:

- Enterprise-grade package storage with high availability (multi replicas)
- Secure, fast, and reliable global content delivery network (CDN)
- Universal support for all packages:

  * Libraries
  * Development platforms
  * Toolchains

- Built-in fine-grained access control (role-based, :ref:`teams <cmd_team>`, :ref:`organizations <cmd_org>`).

The new Web front-end and upgraded :ref:`piohome` are coming soon.

Collaborative Platform
~~~~~~~~~~~~~~~~~~~~~~

PlatformIO Core 5.0 is fully unlocked for developers and teams. They can now share their
packages (libraries, :ref:`platforms`, toolchains) with team members or collaborate
on open source projects. There are new CLI commands that help you to manage
organizations, teams, team memberships, and resource access:

* :ref:`cmd_package` – manage packages in the registry
* :ref:`cmd_org` - manage organizations
* :ref:`cmd_team` - manage teams and team memberships
* :ref:`cmd_access` – manage package access for users, teams, and maintainers.

Package Management
~~~~~~~~~~~~~~~~~~

The package management infrastructure has been rewritten from scratch.
It is based now on the new **PlatformIO Trusted Registry**
that supports a strict dependency declaration using the package owner. This improvement
resolves the issues when package maintainers publish packages under the same name.

PlatformIO Core 5.0 does not handle packages from unofficial repositories declared via
``packageRepositories`` in ``platform.json``. There were a lot of security issues and
reports when PlatformIO Core 4.0 hangs when you manage external dependencies.

PlatformIO Core 5.0 uses THE ONLY official **PlatformIO Trusted Registry** that
supports not only the libraries but also :ref:`platforms` and toolchains.

Package maintainers can publish their libraries, development platforms, and toolchains
to the registry using :ref:`cmd_package` CLI.

.. _core_migration_libmanager:

Library Manager
~~~~~~~~~~~~~~~

The biggest improvement for :ref:`librarymanager` is the owner-based dependency declaration.
You can finally forget about conflicts with library names in the registry. Use the new
syntax ``ownername/pkgname`` to declare an owner-based dependency in :ref:`projectconf`
via :ref:`projectconf_lib_deps`:

.. code-block:: ini

  [env:myenv]
  platform = ...
  framework = ...
  board = ...
  lib_deps =
    bblanchon/ArduinoJson @ ^6.16.1
    knolleary/PubSubClient @ ^2.8

You can find an owner name of a library in the registry using
:ref:`piohome` > Libraries > Some Library > Installation tab.

Build System
~~~~~~~~~~~~

SCons 4.0
'''''''''

PlatformIO Core 5.0 build engine has been upgraded to the latest `SCons 4.0 - a next-generation software construction tool <https://scons.org/>`__:

* :ref:`Configuration files are Python scripts <projectconf_advanced_scripting>` – use the power of a real programming language to solve build problems
* Built-in reliable and automatic dependency analysis
* Improved support for parallel builds
* Ability to :ref:`share built files in a cache <projectconf_pio_cache_dir>` to speed up multiple builds.

Custom Targets
''''''''''''''

PlatformIO Core 5.0 gives more freedom to developers and :ref:`platforms` maintainers.
They can now declare the :ref:`projectconf_advanced_scripting_custom_targets`:

* Pre/Post processing based on dependent sources (another target, source file, etc.)
* Command launcher with own arguments
* Launch command with custom options declared in :ref:`projectconf`
* Python callback as a target (use the power of Python interpreter and PlatformIO Build API)
* List available project targets (including dev-platform specific and custom targets) with a new :option:`pio run --list-targets` command

See **Build System** section in :ref:`release_notes_5` release notes
for more details.

What is changed or removed
--------------------------

Drop support for Python 2 and 3.5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python 2.7 is reached the `end of its life on 1 January 2020 <https://en.wikipedia.org/wiki/History_of_Python#Table_of_versions>`_,
and Python Software Foundation will not provide any security fixes for it. The same
situation with Python 3.5.

To avoid unrelated issues to the PlatformIO Core, we decided to drop support for
Python 2 and 3.5. **The minimum supported version for PlatformIO Core 5.0 is Python 3.6.**

If you use :ref:`pioide`, it already comes with the built-in compatible Python 3 interpreter.
You do not need to do any extra steps. If you see a warning message that your local
PlatformIO Core installation uses incompatible Python, please do the next steps:

1. Install the latest Python 3 following this guide :ref:`faq_install_python`
2. Open system terminal and type ``python3 --version`` or ``python.exe --version`` (for Windows).
   The output should contain a version of Python 3.6 or above (depending on which you installed it).
3. Remove PlatformIO Core installation "penv" folder that is located by this path
   ``USER_HOME_DIR/.platformio/penv``. If you use Windows and your user name contains non-ASCII
   chars the "penv" folder is located in ``C:/.platformio/penv``
4. Install PlatformIO Core using :ref:`installation_installer_script`
5. Run the :ref:`cmd_system_info` command and ensure that Python 3 is used.

Introducing Strict SSL/TLS
~~~~~~~~~~~~~~~~~~~~~~~~~~

The setting ``strict_ssl`` has been removed from :ref:`cmd_settings`. Now, PlatformIO Core 5.0
communicates over the encrypted SSL/TLS by default with the PlatformIO Registry and
other services such as :ref:`pioremote`.

At PlatformIO, we are always looking for ways to improve the security of our services.

packageRepositories
~~~~~~~~~~~~~~~~~~~

PlatformIO Core 5.0 does not support unofficial package repositories declared through
``packageRepositories`` in ``platform.json`` that was introduced in PlatformIO 3.0.

Please publish your development platforms and toolchains to the **PlatformIO Trusted
Registry** using :ref:`cmd_package` CLI.

Command Line Interface
~~~~~~~~~~~~~~~~~~~~~~

The following commands have been changed in v5.0.

.. list-table::
    :header-rows:  1

    * - Command
      - Description
    * - :ref:`cmd_access`
      - **New**. Manage package access for users, teams, and maintainers
    * - :ref:`cmd_package`
      - **New**. Manage packages in the registry (publish, unpublish)
    * - :ref:`cmd_project_data`
      - **New**. Dump build system data intended for IDE extensions/plugins
    * - :ref:`cmd_system_info`
      - **New**. Display system-wide information
    * - :ref:`cmd_system_prune`
      - **New**. Remove unused data
    * - :ref:`cmd_project_init`
      - Update project configuration for the specific environment using :option:`pio project init --environment` option
    * - :ref:`cmd_run`
      - List projects targets with :option:`pio run --list-targets` option
    * - :ref:`cmd_account_destroy`
      - New command to remove permanently :ref:`pioaccount` and related data
