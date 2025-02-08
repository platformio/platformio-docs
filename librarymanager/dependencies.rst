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

.. |PIOREGISTRY| replace:: `PlatformIO Registry <https://registry.platformio.org>`__

.. _librarymanager_dependencies:

Dependency Management
=====================

Modern software projects rarely work in isolation. In most cases, a project
relies on reusable functionality in the form of libraries or is broken up into
individual components to compose a modularized system. Dependency management
is a technique for declaring, resolving, and using dependencies required by the
project in an automated fashion.

PlatformIO is the missing solution in the embedded system industry which has
built-in support for dependency management and lives up to the task of
fulfilling typical scenarios encountered in modern software projects.

.. contents:: Contents
    :local:

Library Registry
----------------

|PIOREGISTRY| contains a rich set of popular libraries with examples and
instructions on how to add them to your project. Libraries in PlatformIO
are isolated between projects and project environments. This helps you
to avoid conflicts or break existing projects when you update libraries
to the newest versions.

If you prefer using :ref:`piocore` instead of web browsing, the
:ref:`cmd_pkg_search` command allows you to search for libraries matching
the search query.

Library sources
---------------

PlatformIO supports different library sources which you can use for
declaring dependencies. The most popular are:

- Versioned libraries from |PIOREGISTRY|
- VCS repositories (Git, Hg, SVN)
- Remote or local library as a TAR or ZIP archive
- Local library as a source folder.

Dependency specifications
-------------------------

Please check :ref:`cmd_pkg_install_specifications` for the available
options.

Declaring dependencies
----------------------

:ref:`projectconf` and the :ref:`projectconf_lib_deps` is the only place
for declaring project dependencies. There are 2 sections where dependencies
can be declared:

1. :ref:`projectconf_section_env` - declare common dependencies for all
   environments
2. :ref:`projectconf_section_env_named` - declare specific dependencies for
   the working environment.

Please take a look at the example below. The ``dep_1`` and ``dep_2`` dependencies
are common to the ``release`` and ``debug`` working environments, whereas
the ``dep_3`` is a specific only for the ``debug`` working environment.
The ``[env:debug]`` section overrides common ``lib_deps`` option, and the
``${env.lib_deps}`` (:ref:`projectconf_interpolation` technique) is used to merge
the common and custom dependencies.

.. code-block:: ini

  ; Common dependencies declared in the common "[env]" section
  [env]
  platform = ...
  board = ...
  framework = ...
  lib_deps =
    dep_1
    dep_2

  [env:release]
  build_flags = -D RELEASE=1

  ; Specific dependencies that extend the common dependencies
  [env:debug]
  lib_deps =
    ${env.lib_deps}
    dep_3

.. note::

  If some libraries are not visible in :ref:`pioide` and Code Completion or
  Code Linting does not work properly, please perform

  * **VSCode**: "Menu: View > Command Palette... > PlatformIO: Rebuild C/C++
    Project Index"

Declaring practices
-------------------

Good practice
~~~~~~~~~~~~~

.. code:: ini

  [env:myenv]
  lib_deps =
    ; Depend on the latest 6.x stable version of ArduinoJson.
    ; The minimum required version is 6.19.4.
    ; New functionality (backward-compatible) and bug-fixed are allowed
    bblanchon/ArduinoJson @ ^6.19.4

    ; Depend on the exact 1.1.1 version
    ; No new functionality (backward-compatible) or bug fixes.
    ; Recommended for safety-critical projects
    me-no-dev/AsyncTCP @ 1.1.1

    ; Depend on the particular tag (v2.13) of a Git repository
    https://github.com/username/HelloWorld.git#v2.13

Bad practice
~~~~~~~~~~~~

.. warning::
  **NOT RECOMMENDED**

.. code:: ini

  [env:myenv]
  lib_deps =
    ; Omit library package owner (<owner>/<name>) and depend on the library by name.
    ; Lead to the conflicts when there are multiple libraries with the same name
    OneWire

    ; Depend on ANY/Latest version of the development platform
    ; allowing breaking changes
    me-no-dev/AsyncTCP

    ; Depend on the development branch of the Git repository,
    ; allow breaking changes, and untested commits
    https://github.com/username/HelloWorld.git


Installing dependencies
-----------------------

PlatformIO automatically resolves and installs project dependencies when you
build, debug, or test a project. If you want to install project dependencies
manually, please use :ref:`piocore` and the :ref:`cmd_pkg_install` command.

Updating dependencies
---------------------

PlatformIO does not update project dependencies automatically. You need to use
:ref:`piocore` and the :ref:`cmd_pkg_update` command to update all project
dependencies or for the specified environment. It is also possible to update
the specified dependency.

We recommend using the :ref:`cmd_pkg_outdated` command, checking available updates,
and avoiding versions that introduce breaking changes.
