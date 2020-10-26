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

.. _cmd_lib_install:

pio lib install
===============

.. contents::

Usage
-----

.. code-block:: bash

    pio lib [STORAGE_OPTIONS] install [OPTIONS] [LIBRARY...]

    # RECOMMENDED
    # install all project dependencies declared via "lib_deps"
    # (run it from a project root where is located "platformio.ini")
    pio lib install [OPTIONS]

    # install project dependent library
    # (run it from a project root where is located "platformio.ini")
    pio lib install [OPTIONS] [LIBRARY...]

    # install dependencies for the specific project environment
    # (run it from a project root where is located "platformio.ini")
    pio lib -e myenv install [OPTIONS] [LIBRARY...]
    pio lib -d /path/to/platformio/project -e myenv install [OPTIONS] [LIBRARY...]

    # install to global storage (NOT RECOMMENDED)
    pio lib --global install [OPTIONS] [LIBRARY...]
    pio lib -g install [OPTIONS] [LIBRARY...]

    # install to custom storage
    pio lib --storage-dir /path/to/dir install [OPTIONS] [LIBRARY...]
    pio lib -d /path/to/dir1 -d /path/to/dir2 install [OPTIONS] [LIBRARY...]

    # [LIBRARY...] forms
    pio lib [STORAGE_OPTIONS] install (with no args, install project dependencies from "lib_deps")
    pio lib [STORAGE_OPTIONS] install <ownername/name>
    pio lib [STORAGE_OPTIONS] install <ownername/name>@<version>
    pio lib [STORAGE_OPTIONS] install <ownername/name>@<version range>
    pio lib [STORAGE_OPTIONS] install <zip or tarball url>
    pio lib [STORAGE_OPTIONS] install file://<zip or tarball file>
    pio lib [STORAGE_OPTIONS] install file://<folder>
    pio lib [STORAGE_OPTIONS] install <repository>
    pio lib [STORAGE_OPTIONS] install <name>=<repository> (name it should have locally)
    pio lib [STORAGE_OPTIONS] install <repository#tag> ("tag" can be commit, branch or tag)

.. warning::

  If some libraries are not visible in :ref:`pioide` and Code Completion or
  Code Linting does not work properly, please perform

  * **VSCode**: "Menu: View > Command Palette... > PlatformIO: Rebuild C/C++
    Project Index"

Description
-----------

Install a library, and any libraries that it depends on using:

1. `PlatformIO Library Registry <https://platformio.org/lib>`_
2. Custom folder, repository or archive.

The ``version`` supports `Semantic Versioning <https://devhints.io/semver>`_ (
``<major>.<minor>.<patch>``) and can take any of the following forms:

* ``^1.2.3`` - any compatible version (new functionality in a backwards compatible manner and patches are allowed, 1.x.x). **RECOMMENDED**
* ``~1.2.3`` - any version with the same major and minor versions, and an
  equal or greater patch version
* ``>1.2.3`` - any version greater than ``1.2.3``. ``>=``, ``<``, and ``<=``
  are also possible
* ``>0.1.0,!=0.2.0,<0.3.0`` - any version greater than ``0.1.0``, not equal to
  ``0.2.0`` and less than ``0.3.0``
* ``1.2.3`` - an exact version number. Use only this exact version.

PlatformIO supports installing from local directory or archive.
YOu need to use ``file://`` prefix before local path.

* ``file:///local/path/to/the/platform/dir``
* ``file:///local/path/to/the/platform.zip``
* ``file:///local/path/to/the/platform.tar.gz``

Storage Options
---------------

See base options for :ref:`cmd_lib`.

Options
-------

.. program:: pio lib install

.. option::
    --save / --no-save

Save installed libraries into the :ref:`projectconf` dependency list
(:ref:`projectconf_lib_deps`). Default value is to save.

You can save libraries for the specific project environment using
``-e, --environment`` option from :ref:`pio lib <cmd_lib>` command. For example,
``pio lib -e myenv install [LIBRARY...]``.

.. option::
    -s, --silent

Suppress progress reporting.

.. option::
    -f, --force

Reinstall library if it is already installed.

Version control
---------------

PlatformIO supports installing from Git, Mercurial and Subversion, and detects
the type of VCS using url prefixes: "git+", "hg+", or "svn+".

.. note::
    PlatformIO requires a working VCS command on your path: ``git``, ``hg``
    or ``svn``.

Git
^^^

The supported schemes are: ``git``, ``git+https`` and ``git+ssh``. Here are
the supported forms:

* https://github.com/user/library.git
* git+git://git.server.org/my-library
* git+https://git.server.org/my-library
* git+ssh://git.server.org/my-library
* git+ssh://user@git.server.org/my-library
* [user@]host.xz:path/to/repo.git

Passing branch names, a commit hash or a tag name is possible like so:

* https://github.com/user/library.git#master
* git+git://git.server.org/my-library#master
* git+https://git.server.org/my-library#v1.0
* git+ssh://git.server.org/my-library#7846d8ad52f983f2f2887bdc0f073fe9755a806d

Mercurial
^^^^^^^^^

The supported schemes are: ``hg+http``, ``hg+https`` and ``hg+ssh``. Here are
the supported forms:

* https://developer.mbed.org/users/user/code/library/ (install ARM mbed library)
* hg+hg://hg.server.org/my-library
* hg+https://hg.server.org/my-library
* hg+ssh://hg.server.org/my-library

Passing branch names, a commit hash or a tag name is possible like so:

* hg+hg://hg.server.org/my-library#master
* hg+https://hg.server.org/my-library#v1.0
* hg+ssh://hg.server.org/my-library#4cfe2fa00668

Subversion
^^^^^^^^^^

The supported schemes are: ``svn``, ``svn+svn``, ``svn+http``, ``svn+https``
and ``svn+ssh``. Here are the supported forms:

* svn+svn://svn.server.org/my-library
* svn+https://svn.server.org/my-library
* svn+ssh://svn.server.org/my-library

You can also give specific revisions to an SVN URL, like so:

* svn+svn://svn.server.org/my-library#13


Examples
--------

1. Install the latest version of library to a global storage using ID or NAME

.. code::

    > pio lib -g install 4

    Library Storage: /storage/dir/...
    LibraryManager: Installing id=4
    Downloading  [####################################]  100%
    Unpacking  [####################################]  100%
    IRremote @ 2.2.1 has been successfully installed!

    # repeat command with name
    > pio lib -g install IRRemote

    Library Storage: /storage/dir/...
    Looking for IRRemote library in registry
    Found: https://platformio.org/lib/show/4/IRremote
    LibraryManager: Installing id=4
    IRremote @ 2.2.1 is already installed


2. Install specified version of a library to a global storage

.. code::

    > pio lib -g install ArduinoJson@5.6.7

    Library Storage: /storage/dir/...
    Looking for ArduinoJson library in registry
    Found: https://platformio.org/lib/show/64/ArduinoJson
    LibraryManager: Installing id=64 @ 5.6.7
    Downloading  [####################################]  100%
    Unpacking  [####################################]  100%
    ArduinoJson @ 5.6.7 has been successfully installed!


3. Install library with dependencies to custom storage

.. code::

    > pio lib --storage-dir /my/storage/dir install DallasTemperature

    Library Storage: /my/storage/dir
    Looking for DallasTemperature library in registry
    Found: https://platformio.org/lib/show/54/DallasTemperature
    LibraryManager: Installing id=54
    Downloading  [####################################]  100%
    Unpacking  [####################################]  100%
    DallasTemperature @ 3.7.7 has been successfully installed!
    Installing dependencies
    Looking for OneWire library in registry
    Found: https://platformio.org/lib/show/1/OneWire
    LibraryManager: Installing id=1
    Downloading  [####################################]  100%
    Unpacking  [####################################]  100%
    OneWire @ 8fd2ebfec7 has been successfully installed!

4. Install ARM mbed library to the global storage

.. code::

    > pio lib -g install https://developer.mbed.org/users/simon/code/TextLCD/

    Library Storage: /storage/dir/...
    LibraryManager: Installing TextLCD
    Mercurial Distributed SCM (version 3.8.4)
    (see https://mercurial-scm.org for more information)

    Copyright (C) 2005-2016 Matt Mackall and others
    This is free software; see the source for copying conditions. There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    requesting all changes
    adding changesets
    adding manifests
    adding file changes
    added 9 changesets with 18 changes to 6 files
    updating to branch default
    2 files updated, 0 files merged, 0 files removed, 0 files unresolved
    TextLCD @ 308d188a2d3a has been successfully installed!

5. Install from archive using URL

.. code::

    > pio lib -g install  https://github.com/adafruit/DHT-sensor-library/archive/master.zip

    Library Storage: /storage/dir/...
    LibraryManager: Installing master
    Downloading  [####################################]  100%
    Unpacking  [####################################]  100%
    DHT sensor library @ 1.2.3 has been successfully installed!
