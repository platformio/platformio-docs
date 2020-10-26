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

.. _cmd_lib_update:

pio lib update
==============

.. contents::

Usage
-----

.. code-block:: bash

    pio lib [STORAGE_OPTIONS] update [OPTIONS]

    # update all project libraries
    # (run it from a project root where is located "platformio.ini")
    pio lib update [OPTIONS]

    # update project dependent library
    pio lib [STORAGE_OPTIONS] update [OPTIONS] [LIBRARY...]

    # update library in global storage
    pio lib --global update [OPTIONS] [LIBRARY...]
    pio lib -g update [OPTIONS] [LIBRARY...]

    # update library in custom storage
    pio lib --storage-dir /path/to/dir update [OPTIONS] [LIBRARY...]
    pio lib -d /path/to/dir update [OPTIONS] [LIBRARY...]

    # [LIBRARY...] forms
    pio lib [STORAGE_OPTIONS] update <id>
    pio lib [STORAGE_OPTIONS] update <id>@<version>
    pio lib [STORAGE_OPTIONS] update <id>@<version range>
    pio lib [STORAGE_OPTIONS] update <name>
    pio lib [STORAGE_OPTIONS] update <name>@<version>
    pio lib [STORAGE_OPTIONS] update <name>@<version range>


Description
-----------

Check or update installed libraries.

The ``version`` supports `Semantic Versioning <https://devhints.io/semver>`_ (
``<major>.<minor>.<patch>``) and can take any of the following forms:

* ``1.2.3`` - an exact version number. Use only this exact version
* ``^1.2.3`` - any compatible version (exact version for ``1.x.x`` versions)
* ``~1.2.3`` - any version with the same major and minor versions, and an
  equal or greater patch version
* ``>1.2.3`` - any version greater than ``1.2.3``. ``>=``, ``<``, and ``<=``
  are also possible
* ``>0.1.0,!=0.2.0,<0.3.0`` - any version greater than ``0.1.0``, not equal to
  ``0.2.0`` and less than ``0.3.0``

Storage Options
---------------

See base options for :ref:`cmd_lib`.

Options
-------

.. program:: pio lib update

.. option::
    -c, --only-check

DEPRECATED. Please use ``--dry-run`` instead.


.. option::
    --dry-run

Do not update, only check for the new versions

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`_ format

Examples
--------

1. Update all installed libraries in global storage

.. code::

    > pio lib -g update

    Library Storage: /storage/dir/...
    Updating ESP8266_SSD1306 @ 3.2.3:   [Up-to-date]
    Updating EngduinoMagnetometer @ 3.1.0:  [Up-to-date]
    Updating IRremote @ 2.2.1:  [Up-to-date]
    Updating Json @ 5.4.0:  [Out-of-date]
    LibraryManager: Installing id=64 @ 5.6.4
    Downloading  [####################################]  100%
    Unpacking  [####################################]  100%
    Json @ 5.6.4 has been successfully installed!
    Updating PJON @ 1fb26fd:    [Checking]
    git version 2.7.4 (Apple Git-66)
    Already up-to-date.
    Updating TextLCD @ 308d188a2d3a:    [Checking]
    Mercurial Distributed SCM (version 3.8.4)
    (see https://mercurial-scm.org for more information)

    Copyright (C) 2005-2016 Matt Mackall and others
    This is free software; see the source for copying conditions. There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    pulling from https://developer.mbed.org/users/simon/code/TextLCD/
    searching for changes
    no changes found

2. Update specified libraries in global storage

.. code::

    > pio lib -g update Json 4

    Library Storage: /storage/dir/...
    Updating Json @ 5.6.4:  [Up-to-date]
    Updating IRremote @ 2.2.1:  [Up-to-date]
