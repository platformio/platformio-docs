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

.. _cmd_pkg_install:

pio pkg install
===============

.. contents::

Usage
-----

.. code-block:: bash

    pio pkg install [OPTIONS]

Description
-----------

Install the project dependencies or custom packages from the |PIOREGISTRY| or
external sources.

If no custom packages (``--library``, ``--platform``, or ``--tool``) are
specified, the command will install the following project
dependencies based on :ref:`projectconf`:

* Library dependencies declared using the :ref:`projectconf_lib_deps` option
* Development platform declared using the :ref:`projectconf_env_platform` option
  and its dependencies (toolchain, framework, SDKs, debugging server, etc)
* Custom tools declared using the :ref:`projectconf_env_platform_packages` option.

Options
-------

.. program:: pio pkg install

.. option::
    -d, --project-dir

Specify the path to project directory. By default, ``--project-dir`` is equal
to current working directory (``CWD``).

.. option::
    -e, --environment

Install project dependencies only for the specified environments.
Multiple environments are allowed.

.. option::
    -p, --platform

Install specified development platform using :ref:`cmd_pkg_install_specifications`.
Multiple items are allowed.

**Examples**

.. code:: shell

    pio pkg install -p "aceinna/aceinna_imu@^1.3.8" -p "platformio/atmelavr"
    pio pkg install --platform "https://github.com/platformio/platform-sifive.git"

.. option::
    -t, --tool

Install specified tool using :ref:`cmd_pkg_install_specifications`.
Multiple items are allowed.

**Examples**

.. code:: shell

    pio pkg install -t "platformio/tool-openocd"
    pio pkg install --tool https://github.com/platformio/platform-sifive.git

.. option::
    -l, --library

Install specified library using :ref:`cmd_pkg_install_specifications`.
Multiple items are allowed.

**Examples**

.. code:: shell

    pio pkg install -l "bblanchon/ArduinoJson@^6.19.2" -l "milesburton/DallasTemperature@^3.9.1"
    pio pkg install --library https://github.com/Makuna/NeoPixelBus.git

.. option::
    --no-save

Prevent saving specified packages to :ref:`projectconf`.

.. option::
    --skip-dependencies

Install a package but skip its dependencies declared in the manifest
:ref:`manifest_library_json_dependencies` field.

.. option::
    -g, --global

.. warning::

    We **DO NOT recommend installing** libraries in the global storage.
    Please use the :ref:`projectconf_lib_deps` option and declare library
    dependencies per project.

Install packages to the global storage:

* :ref:`projectconf_pio_platforms_dir` - development platforms
* :ref:`projectconf_pio_packages_dir` - tools
* :ref:`projectconf_pio_globallib_dir` - libraries.

A package installed to the global storage will be available for any PlatformIO
project.

.. option::
    --storage-dir

Specify a custom Package Manager storage for global packages.

.. option::
    -f, --force

Reinstall a package if exists. The existing package will be removed and the latest
compatible version will be installed.

.. option::
    -s, --silent

Suppress progress reporting.

.. _cmd_pkg_install_types:

Package Types
-------------

PlatformIO supports the next package types:

:``library``:
    The Assembly/C/C++ files that can extend project functionality

:``platform``:
    See :ref:`platforms` for details

:``tool``:
    A specialized program, toolchain, or source of auxiliary files (framework, SDK)
    that are used to build a project, debug it or upload firmware to the target device.

Browse over 10,000 packages in the |PIOREGISTRY|.

.. _cmd_pkg_install_specifications:

Package Specifications
----------------------

PlatformIO supports different package sources which you can specify for
:ref:`cmd_pkg_install` command or configure project dependencies using
:ref:`projectconf` options:

* :ref:`projectconf_env_platform` - development platform
* :ref:`projectconf_env_platform_packages` - custom tools/packages
* :ref:`projectconf_lib_deps` - libraries.

A ``package`` is:

a) A folder containing manifest file (:ref:`library_json`, ``platform.json`` or ``package.json``)
b) TAR or ZIP archive containing (a)
c) A URL that resolves to (b)
d) An ``<owner>/<name>@<version requirements>`` that is published on the |PIOREGISTRY|
e) A <git/hg/svn remote url> that resolves to (a).

.. contents:: Specifications
    :local:

Registry: Latest Version
~~~~~~~~~~~~~~~~~~~~~~~~

**Specification:** ``<owner>/<name>``

Install the latest package version from the |PIOREGISTRY|.

.. tip::
    We highly recommend pinning a package to a :ref:`cmd_pkg_install_specific_version`
    and to prefix the version with the ``^`` (caret) symbol.
    This will instruct PlatformIO to install the latest compatible version
    avoiding breaking changes in the future.
    See :ref:`cmd_pkg_install_requirements` for details.

**Examples**

1.  Install `ArduinoJson <https://registry.platformio.org/libraries/bblanchon/ArduinoJson>`__
    and `Embedded Template <https://registry.platformio.org/libraries/etlcpp/Embedded%20Template%20Library>`_
    libraries, and add them to the project dependencies (:ref:`projectconf_lib_deps`):

    .. code:: shell

        pio pkg install --library "bblanchon/ArduinoJson" --library "etlcpp/Embedded Template Library"

2.  Declare `ArduinoJson <https://registry.platformio.org/libraries/bblanchon/ArduinoJson>`__
    and `Embedded Template <https://registry.platformio.org/libraries/etlcpp/Embedded%20Template%20Library>`_
    libraries as the project dependencies using :ref:`projectconf_lib_deps`
    configuration option:

    .. code:: ini

        [env:myenv]
        lib_deps =
            bblanchon/ArduinoJson
            etlcpp/Embedded Template Library

3.  Install `SEGGER J-Link Software <https://registry.platformio.org/tools/platformio/tool-jlink>`__
    for debug probes:

    .. code:: shell

        pio pkg install --tool "platformio/tool-jlink"

.. _cmd_pkg_install_specific_version:

Registry: Specific Version
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Specification:** ``<owner>/<name>@<version>``

Install the specified version of a package from the |PIOREGISTRY|.
This will fail if the version has not been published to the registry.

**Example**

.. code:: shell

    bblanchon/ArduinoJson@6.9.12

Registry: Version Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Specification:** ``<owner>/<name>@<version requirements>``

Install the latest version of a package from the |PIOREGISTRY| matching the
specified version requirements. See :ref:`cmd_pkg_install_requirements` for details.

**Example**

.. code:: shell

    bblanchon/ArduinoJson@>=6,!=6.13.0

Repository (git, hg, svn)
~~~~~~~~~~~~~~~~~~~~~~~~~

**Specification:** ``[<name>=][<scheme>://][<user>[:<password>]@]<hostname>[:<port>][:][/]<path>[#<commit-ish|branch|tag>]``

Install the package at the specified URL by attempting to clone it.
If the repository makes use of submodules, those submodules will be cloned as well.

The supported schemes are:

* ``http``
* ``https``
* ``git``
* ``git+http``
* ``git+https``
* ``git+ssh``
* ``hg+http``
* ``hg+https``
* ``hg+ssh``
* ``svn+http``
* ``svn+https``
* ``svn+ssh``

You can override a package folder name in the Package Manager storage using
the ``<name>=`` syntax. See the example below.

**Examples**

1.  Clone default branch of Github repository using HTTPS

    .. code:: shell

        https://github.com/platformio/platform-espressif32.git

2.  Clone default branch of Github repository using SSH

    .. code:: shell

        git@github.com:platformio/platform-espressif32.git

        # or

        git+username@github.com:platformio/platform-espressif32.git

3.  Clone Git repository using SSH and custom username

    .. code:: shell

        git+ssh://git.server.org/my-platform

        # or

        git+ssh://user@git.server.org/my-platform

4.  Clone "master" branch of Git repository

    .. code:: shell

        https://github.com/platformio/platform-espressif32.git#master

5.  Clone "v3.3.0" tag of Git repository

    .. code:: shell

        https://github.com/platformio/platform-espressif32.git#v3.3.0

6.  Clone specified commit of Git repository

    .. code:: shell

        https://github.com/platformio/platform-espressif32.git#084131f6634c818485781651d76818cd1f13a461

7.  Clone specified commit of Git repository and set custom package folder name to "ESP32"

    .. code:: shell

        ESP32=https://github.com/platformio/platform-espressif32.git#084131f6634c818485781651d76818cd1f13a461

8.  Clone Mercurial repository

    .. code:: shell

        hg+hg://hg.server.org/my-package
        hg+https://hg.server.org/my-package
        hg+ssh://hg.server.org/my-package

.. _cmd_pkg_install_local_folder:

Local Folder
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1
    :widths: 25 75

    * - Specification
      - Description
    * - ``[<name>=]file://<folder>``
      - Copy all files from the local folder to the Package Manager.
        Making changes in the source folder **WILL NOT** affect the installed package.
    * - ``[<name>=]symlink://<folder>``
      - Create a symbolic link pointing the local source folder to the Package Manager.
        Making changes in the source folder **WILL** affect the installed package.

Install a package and its :ref:`manifest_library_json_dependencies` from a local folder.
A path should start with ``file://`` or ``symlink://`` prefix and the package folder
must contain a manifest file (:ref:`library_json`, ``platform.json``, or ``package.json``)
with name and version properties.

You can override a package folder name in the Package Manager storage using
the ``<name>=`` syntax. See the example below.

**Examples**

.. code:: shell

    # Unix, hard copying
    file:///local/path/to/the/package/dir

    # Windows, symbolic link
    symlink://C:/local/path/to/the/package/dir

    # Custom package folder name "SomeLib" in the storage
    SomeLib=file:///local/path/to/the/package/dir

Local TAR or ZIP archive
~~~~~~~~~~~~~~~~~~~~~~~~

**Specification:** ``[<name>=]file://<tar or zip file>``

Install a package and its :ref:`manifest_library_json_dependencies` from a local TAR or ZIP archive.

Archive requirements:

* the filename must use ``.tar.gz``, ``.tar``, ``.tgz``, or ``.zip`` as the extension
* the package must contain a manifest file (:ref:`library_json`, ``platform.json``, or
  ``package.json``) with ``name`` and ``version`` properties.

You can override a package folder name in the Package Manager storage using
the ``<name>=`` syntax. See the example below.

**Examples**

.. code:: shell

    # tar.gz
    file:///local/path/to/the/archive.tar.gz

    # zip
    file:///local/path/to/the/archive.zip

    # Custom package folder name "SomeLib" in the storage
    SomeLib=file:///local/path/to/the/archive.tar.gz

Remote TAR or ZIP archive
~~~~~~~~~~~~~~~~~~~~~~~~~

**Specification:** ``[<name>=]<archive url>``

Fetch the archive URL, and then install a package and its :ref:`manifest_library_json_dependencies`.
The URL must start with ``http://`` or ``https://``.

You can override a package folder name in the Package Manager storage using
the ``<name>=`` syntax. See the example below.

**Examples**

.. code:: shell

    # TAR archive
    https://github.com/bblanchon/ArduinoJson/archive/refs/heads/6.x.tar.gz

    # ZIP archive
    https://github.com/bblanchon/ArduinoJson/archive/refs/heads/6.x.zip

    # Custom package folder name "JSON" in the storage
    JSON=https://github.com/bblanchon/ArduinoJson/archive/refs/heads/6.x.tar.gz

.. _cmd_pkg_install_requirements:

Version Requirements
--------------------

.. note::

    PlatformIO uses `python-semanticversion <https://github.com/rbarrois/python-semanticversion>`_
    library to handle SemVer versions and specifications.

The ``@<version requirements>`` specification supports `Semantic Versioning <https://semver.org/>`_ (
``<MAJOR>.<MINOR>.<PATCH>``):

* ``MAJOR`` - incompatible API changes
* ``MINOR`` - add functionality (backwards-compatible)
* ``PATCH`` - bug fixes (backwards-compatible).

The version requirements can take any of the following forms (see `Semver cheatsheet <https://devhints.io/semver>`_):

* ``^1.2.3`` - any compatible version (new functionality in a backwards compatible
  manner and patches are allowed, 1.x.x). **RECOMMENDED**
* ``~1.2.3`` - any version with the same major and minor versions, and an
  equal or greater patch version
* ``>1.2.3`` - any version greater than ``1.2.3``. ``>=``, ``<``, and ``<=``
  are also possible
* ``>0.1.0,!=0.2.0,<0.3.0`` - any version greater than ``0.1.0``, not equal to
  ``0.2.0`` and less than ``0.3.0``
* ``1.2.3`` - an exact version number. Use only this exact version.

To list available package versions and installation instructions, please visit the |PIOREGISTRY|.

**Example:**

Depend on the `platformio/espressif32 <https://registry.platformio.org/platforms/platformio/espressif32>`__
development platform with the next requirements:

* version is ``>=3.5.0``
* version is ``<4.0.0``
* version is not ``3.2.0``

.. code:: shell

    platformio/espressif32@>=3.5.0,<4,!=3.2.0

    # or short form
    platformio/espressif32@^3.5.0,!=3.2.0

See Also
--------

* :ref:`cmd_pkg_uninstall`
* :ref:`cmd_pkg_outdated`
* :ref:`library_json`
