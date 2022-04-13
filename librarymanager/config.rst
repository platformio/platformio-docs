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

.. _library_json:

library.json
============

``library.json`` is a manifest file of a library package. It allows developers
to keep a project in its own structure and define:

* compatible frameworks and platforms
* external dependencies
* advanced build settings.

Information in ``library.json`` should be represented in `JSON-style <http://en.wikipedia.org/wiki/JSON>`_
via `associative array <http://en.wikipedia.org/wiki/Associative_array>`_
(name/value pairs). The order doesn't matter. The allowable fields
(names from pairs) are described below.

You can validate ``library.json`` manifest file using the :ref:`cmd_pkg_pack` command.

.. contents:: Fields
    :local:

.. _libjson_name:

``name``
--------

**Required** | Type: ``String`` | Max. Length: 50

A name of a library.

* Must be unique in the |PIOREGISTRY|
* Should be slug style for simplicity, consistency, and compatibility.
  Example: *HelloWorld*
* Can contain a-z, digits, and dashes (but not start/end with them)
* Consecutive dashes and [:;/,@<>] chars are not allowed.

.. _libjson_version:

``version``
-----------

*Required* | Type: ``String`` | Max. Length: 20

A version of a current library source code. Can contain a-z, digits, dots or
dash and should be `Semantic Versioning <http://semver.org>`__ compatible.

**Example**

.. code-block:: javascript

    "name": "Bar",
    "version": "1.0.0",
    "repository":
    {
        "type": "git",
        "url": "https://github.com/foo/bar.git"
    }

.. _libjson_description:

``description``
---------------

**Required** | Type: ``String`` | Max. Length: 255

The field helps users to identify and search for your library with a brief
description. Describe the hardware devices (sensors, boards and etc.) which
are suitable with it.

.. _libjson_keywords:

``keywords``
------------

**Required** | Type: ``String`` or ``Array`` | Max. Length: 255

Used for search by keyword. Helps to make your library easier to discover
without people needing to know its name.

The keyword should be lowercased, can contain a-z, digits and dash (but not
start/end with them). A list from the keywords can be specified with
separator ``,`` or declared as Array.

``homepage``
------------

*Optional* | Type: ``String`` | Max. Length: 255

Home page of a library (if is different from :ref:`libjson_repository` url).

.. _libjson_repository:

``repository``
--------------

*Optional* | Type: ``Object``

The repository in which the source code can be found. The field consists of the
next items:

* ``type`` the only "git", "hg" or "svn" are supported
* ``url``
* ``branch`` if is not specified, default branch will be used. This field will
  be ignored if tag/release exists with the value of :ref:`libjson_version`.

**Example**

.. code-block:: javascript

    "repository":
    {
        "type": "git",
        "url": "https://github.com/foo/bar.git"
    }

.. _libjson_authors:

``authors``
-----------

*Optional* | Type: ``Object`` or ``Array``

An author contact information

* ``name`` Full name (**Required**)
* ``email``
* ``url`` An author's contact page
* ``maintainer`` Specify "maintainer" status

**Examples**

.. code-block:: javascript

    "authors":
    {
        "name": "John Smith",
        "email": "me@john-smith.com",
        "url": "https://www.john-smith/contact"
    }

    ...

    "authors":
    [
        {
            "name": "John Smith",
            "email": "me@john-smith.com",
            "url": "https://www.john-smith/contact"
        },
        {
            "name": "Andrew Smith",
            "email": "me@andrew-smith.com",
            "url": "https://www.andrew-smith/contact",
            "maintainer": true
        }
    ]


.. note::
    If :ref:`libjson_authors` field is not defined, PlatformIO will try to fetch data
    from VCS provider (Github, Gitlab, etc) if :ref:`libjson_repository` is declared.

``license``
-----------

*Optional* | Type: ``SPDX Expression``

A SPDX license ID or `SPDX Expression <https://spdx.github.io/spdx-spec/SPDX-license-expressions/>`_.
You can check `the full list of SPDX license IDs <https://spdx.org/licenses/>`_ (see "Identifier" column).

**Examples**

A single license

.. code-block:: javascript

    "license": "Apache-2.0"

Multiple license using SPDX Expression

.. code-block:: javascript

    "license": "MIT AND (LGPL-2.1-or-later OR BSD-3-Clause)"

.. _libjson_frameworks:

``frameworks``
--------------

*Optional* | Type: ``String`` or ``Array``

A list with compatible frameworks. The available framework names are defined in
the :ref:`frameworks` section.

**Example**

.. code-block:: javascript

    "frameworks": ["espidf", "freertos"]

If the library is compatible with the all frameworks, then do not declare this field or
you use ``*`` symbol:

.. code-block:: javascript

    "frameworks": "*"

.. _libjson_platforms:

``platforms``
-------------

*Optional* | Type: ``String`` or ``Array``

A list with compatible development platforms. The available platform name are defined
in :ref:`platforms` section.

**Example**

.. code-block:: javascript

    "platforms": ["atmelavr", "espressif8266"]

If the library is compatible with the all platforms, then do not declare this field or
use ``*`` symbol:

.. code-block:: javascript

    "platforms": "*"

.. note::
    PlatformIO does not check platforms for compatibility in default mode.
    See :ref:`ldf_compat_mode` for details. If you need a strict checking for compatible
    platforms for a library, please set :ref:`libjons_compatmode` to ``strict``.

``headers``
-----------

*Optional* | Type: ``String`` or ``Array``

A list of header files that can be included in a project source files using
``#include <...>`` directive.

**Examples**

.. code-block:: javascript

    "headers": "MyLibrary.h"


.. code-block:: javascript

    "headers": ["FooCore.h", "FooFeature.h"]

.. _libjson_examples:

``examples``
------------

*Optional* | Type: ``Array`` | `Glob Pattern <http://en.wikipedia.org/wiki/Glob_(programming)>`_

A list of example patterns. This field is predefined with default value:

.. code-block:: javascript

    "examples": [
        {
            "name": "Hello",
            "base": "examples/world",
            "files": [
                "platformio.ini",
                "include/world.h",
                "src/world.c",
                "README",
                "extra.py"
            ]
        },
        {
            "name": "Blink",
            "base": "examples/blink",
            "files": ["blink.cpp", "blink.h"]
        }
    ]

.. _libjson_dependencies:

``dependencies``
----------------

*Optional* | Type: ``Array`` or ``Object``

A list of dependent libraries that will be automatically installed.

Allowed requirements for dependent library:

* ``owner`` | Type: ``String`` – an owner name (username) from the |PIOREGISTRY|
* ``name`` | Type: ``String`` – library name
* ``version`` | Type: ``String`` – :ref:`cmd_pkg_install_requirements` or :ref:`cmd_pkg_install_specifications`
* ``frameworks`` | Type: ``String`` or ``Array`` – project compatible :ref:`frameworks`
* ``platforms`` | Type: ``String`` or ``Array`` – project compatible :ref:`platforms`

**Example**

.. code-block:: javascript

    "dependencies":
    {
        "bblanchon/ArduinoJson": "^6.16.1",
        "me-no-dev/AsyncTCP": "*",
        "external-repo": "https://github.com/user/package.git#1.2.3",
        "external-zip": "https://github.com/me-no-dev/AsyncTCP/archive/master.zip"
    }

More advanced usage:

.. code-block:: javascript

    "dependencies":
    [
        {
            "owner": "bblanchon",
            "name": "ArduinoJson",
            "version": "^6.16.1"
        },
        {
            "owner": "me-no-dev",
            "name": "AsyncTCP",
            "version": "*",
            "platforms": ["espressif32"]
        },
        {
            "name": "external-repo",
            "version": "https://github.com/user/package.git#1.2.3"
        },
        {
            "name": "external-zip",
            "version": "https://github.com/me-no-dev/AsyncTCP/archive/master.zip"
        }
    ]

.. _libjson_export:

``export``
----------

*Optional* | Type: ``Object``

This option is useful if you need to exclude extra data (test code, docs, images, PDFs, etc).
It allows one to reduce the size of the final archive.

To check which files will be included in the final packages, please use
:ref:`cmd_pkg_pack` command.

Possible options:

.. contents::
    :local:

``include``
~~~~~~~~~~~

*Optional* | Type: ``Array`` | `Glob Pattern <http://en.wikipedia.org/wiki/Glob_(programming)>`_

Export only files that matched declared patterns.

**Pattern Meaning**

.. list-table::
    :header-rows:  1

    * - Pattern
      - Meaning
    * - ``*``
      - matches everything
    * - ``?``
      - matches any single character
    * - ``[seq]``
      - matches any character in seq
    * - ``[!seq]``
      - matches any character not in seq

**Example**

.. code-block:: javascript

    "export": {
        "include":
        [
            "dir/*.[ch]pp",
            "dir/examples/*",
            "*/*/*.h"
        ]
    }


``exclude``
~~~~~~~~~~~

*Optional* | Type: ``Array`` | `Glob Pattern <http://en.wikipedia.org/wiki/Glob_(programming)>`_

Exclude the directories and files which match with ``exclude`` patterns.

``scripts``
-----------

.. versionadded:: 6.0

*Optional* | Type: ``Object``

Execute custom scripts during the special :ref:`cmd_pkg` life cycle events:

.. list-table::
    :header-rows:  1

    * - Event
      - Description
    * - ``postinstall``
      - runs a script AFTER the package has been installed
    * - ``preuninstall``
      - runs a script BEFORE the package is removed.

**Examples**

1.  Run a custom Python script located in the package "scripts" folder AFTER the package is installed.
    Please note that you don't need to specify a Python interpreter for Python scripts.

    .. code-block:: javascript

        "scripts": {
            "postinstall": "scripts/after_install.py"
        }

2.  Run a custom Bash script BEFORE the package is uninstalled.
    The script is declared as a list of command arguments
    and is located at the root of a package:

    .. code-block:: javascript

        "scripts": {
            "preuninstall": ["maintainance.sh", "--action", "uninstall"]
        }

.. _libjson_build:

``build``
---------

*Optional* | Type: ``Object``

Specify advanced settings, options and flags for the build system. Possible
options:

.. contents::
    :local:

``flags``
~~~~~~~~~

*Optional* | Type: ``String`` or ``Array``

Extra flags to control preprocessing, compilation, assembly, and linking
processes. More details :ref:`projectconf_build_flags`.

.. note::
    Keep in mind when operating with the ``-I`` flag (directories to be
    searched for header files). The path should be relative to the
    root directory where the ``library.json`` manifest is located.

``unflags``
~~~~~~~~~~~

*Optional* | Type: ``String`` or ``Array``

Remove base/initial flags which were set by development platform. More
details :ref:`projectconf_build_unflags`.

``includeDir``
~~~~~~~~~~~~~~

*Optional* | Type: ``String``

Custom directory to be searched for header files.
A default value is ``include`` and means that folder is located at
the root of a library.

.. note::
    The :ref:`ldf` will pick a library automatically only when
    a project or other dependent libraries include any header file
    located in ``includeDir`` or ``srcDir``.

``srcDir``
~~~~~~~~~~

*Optional* | Type: ``String``

Custom location of library source code. A default value is ``src`` and
means that folder is located in the root of a library.

``srcFilter``
~~~~~~~~~~~~~

*Optional* | Type: ``String`` or ``Array``

Specify which source files should be included/excluded from build process.
The path in filter should be relative to the ``srcDir`` option of a library.

See syntax in :ref:`projectconf_src_filter`.

Please note that you can generate source filter "on-the-fly" using
``extraScript`` (see below)

``extraScript``
~~~~~~~~~~~~~~~

*Optional* | Type: ``String``

Launch extra script before build process.
More details :ref:`projectconf_extra_scripts`.

**Example** (HAL-based library)

This example demonstrates how to build HAL-dependent source files and
exclude other source files from a build process.

Project structure

.. code::

    ├── lib
    │   ├── README
    │   └── SomeLib
    │       ├── extra_script.py
    │       ├── hal
    │       │   ├── bar
    │       │   │   ├── hal.c
    │       │   │   └── hal.h
    │       │   ├── foo
    │       │       ├── hal.c
    │       │       └── hal.h
    │       ├── library.json
    │       ├── SomeLib.c
    │       └── SomeLib.h
    ├── platformio.ini
    └── src
        └── test.c

``platformio.ini``

.. code-block:: ini

    [env:foo]
    platform = native
    build_flags = -DHAL=foo

    [env:bar]
    platform = native
    build_flags = -DHAL=bar

``library.json``

.. code-block:: ini

    {
        "name": "SomeLib",
        "version": "0.0.0",
        "build": {
            "extraScript": "extra_script.py"
        }
    }

``extra_script.py``

.. code-block:: py

    Import('env')
    from os.path import join, realpath

    # private library flags
    for item in env.get("CPPDEFINES", []):
        if isinstance(item, tuple) and item[0] == "HAL":
            env.Append(CPPPATH=[realpath(join("hal", item[1]))])
            env.Replace(SRC_FILTER=["+<*>", "-<hal*>", "+<hal/%s>" % item[1]])
            break

    # pass flags to the project global scope (make them available for the project source files)
    global_env = DefaultEnvironment()
    global_env.Append(
        CPPDEFINES=[
            ("MQTT_MAX_PACKET_SIZE", 512),
            "ARDUINOJSON_ENABLE_STD_STRING",
            ("BUFFER_LENGTH", 32)
        ]
    )

.. _libjson_archive:

``libArchive``
~~~~~~~~~~~~~~

*Optional* | Type: ``Boolean``

Create an archive (``*.a``, static library) from the object files and link it
into a firmware (program). This is default behavior of PlatformIO Build System
(``"libArchive": true``).

Setting ``"libArchive": false`` will instruct PlatformIO Build System to link object
files directly (in-line). This could be useful if you need to override ``weak``
symbols defined in framework or other libraries.

You can disable library archiving globally using :ref:`projectconf_lib_archive`
option in :ref:`projectconf`.

``libLDFMode``
~~~~~~~~~~~~~~

*Optional* | Type: ``String``

Specify Library Dependency Finder Mode. See :ref:`ldf_mode` for details.

.. _libjons_compatmode:

``libCompatMode``
~~~~~~~~~~~~~~~~~

*Optional* | Type: ``String``

Specify Library Compatibility Mode. See :ref:`ldf_compat_mode` for details.

``builder``
~~~~~~~~~~~

*Optional* | Type: ``String``

Override default ``PlatformIOLibBuilder`` with another builder. Currently supported
builders:

* ``PlatformIOLibBuilder`` (default)
* ``ArduinoLibBuilder``
* ``MbedLibBuilder``

Examples
--------

1. Custom macros/defines

.. code-block:: javascript

    "build": {
        "flags": "-D MYLIB_REV=1.2.3 -DRELEASE"
    }

2. Extra includes for C preprocessor

.. code-block:: javascript

    "build": {
        "flags": [
            "-I inc",
            "-I inc/target_x13"
        ]
    }

3. Force to use ``C99`` standard instead of ``C11``

.. code-block:: javascript

    "build": {
        "unflags": "-std=gnu++11",
        "flags": "-std=c99"
    }

4. Build source files (``c, cpp, h``) at the top level of the library

.. code-block:: javascript

    "build": {
        "srcFilter": [
            "+<*.c>",
            "+<*.cpp>",
            "+<*.h>"
        ]
    }


5. Extend PlatformIO Build System with own extra script

.. code-block:: javascript

    "build": {
        "extraScript": "generate_headers.py"
    }

``generate_headers.py``

.. code-block:: python

    Import('env')
    # print(env.Dump())
    env.Append(
        CPPDEFINES=["HELLO=WORLD", "TAG=1.2.3", "DEBUG"],
        CPPPATH=["inc", "inc/devices"]
    )

    # some python code that generates header files "on-the-fly"
