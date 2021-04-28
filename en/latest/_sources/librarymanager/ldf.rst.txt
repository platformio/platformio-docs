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

.. _ldf:

Library Dependency Finder (LDF)
===============================

Library Dependency Finder is a core part of PlatformIO Build System that
operates with the C/C++ source files and looks for ``#include ...``
directives to know what header directories to include for the compiler.

In spite of the fact that Library Dependency Finder is written in pure Python,
it evaluates :ref:`ldf_c_cond_syntax` (``#ifdef``, ``if``, ``defined``,
``else``, and ``elif``) without calling ``gcc -E``. This approach allows
to significantly reduce the total compilation time. See :ref:`ldf_mode` for more
details.

.. contents::

Configuration
-------------

Library Dependency Finder can be configured from :ref:`projectconf`:

.. toctree::
  :maxdepth: 2

  ../projectconf/section_env_library

.. _ldf_storage:

Storage
-------

There are different storages where Library Dependency Finder looks for
libraries. These storages (folders) have priority and LDF operates in the next
order:

1. :ref:`projectconf_lib_extra_dirs` - extra storages per build environment
2. :ref:`projectconf_pio_lib_dir` - own/private library storage per project
3. :ref:`projectconf_pio_libdeps_dir` - project dependency storage used by
   :ref:`librarymanager`
4. ":ref:`projectconf_pio_core_dir`/lib" - global storage per all projects.
5. Library storages built into frameworks, SDKs.

.. _ldf_mode:

Dependency Finder Mode
----------------------

Library Dependency Finder starts work from analyzing source files of the
project (:ref:`projectconf_pio_src_dir`) and can work in the next modes:

:``off``:
    "Manual mode", does not process source files of a project and dependencies.
    Builds only the libraries that are specified in manifests
    (:ref:`library_json`, ``module.json``) or using :ref:`projectconf_lib_deps`
    option.

:``chain``:
    [**DEFAULT**] Parses ALL C/C++ source files of the project and follows
    only by nested includes (``#include ...``, chain...) from the libraries.
    It also parses C, CC, CPP files from libraries which have the same name as
    included header file. **Does not evaluate** :ref:`ldf_c_cond_syntax`.

:``deep``:
    Parses ALL C/C++ source files of the project and parses ALL C/C++ source
    files of the each found dependency (recursively).
    **Does not evaluate** :ref:`ldf_c_cond_syntax`.

:``chain+``:
    The same behavior as for the ``chain`` but **evaluates** :ref:`ldf_c_cond_syntax`.

:``deep+``:
    The same behavior as for the ``deep`` but **evaluates** :ref:`ldf_c_cond_syntax`.

The mode can be changed using :ref:`projectconf_lib_ldf_mode` option in
:ref:`projectconf`. Default value is set to ``chain``.

.. note::
  Usually, when the LDF appears to fail to identify a dependency of a library,
  it is because the dependency is only referenced from a library source file,
  and not a library header file (see example below). In this case, it is
  necessary to either explicitly reference the dependency from the project
  source or :ref:`projectconf` (:ref:`projectconf_lib_deps` option), or change
  the LDF mode to "deep" (not generally recommended).

A difference between ``chain/chain+`` and ``deep/deep+`` modes. For example,
there are 2 libraries:

* Library ``Foo`` with files:

  - ``Foo/foo.h``
  - ``Foo/foo.cpp``
  - ``Foo/extra.cpp``

* Library ``Bar`` with files:

  - ``Bar/bar.h``
  - ``Bar/bar.cpp``

:Case 1:

    * ``lib_ldf_mode = chain``
    * ``Foo/foo.h`` depends on the ``Bar`` library (contains ``#include <bar.h>``)
    * ``#include <foo.h>`` is located in one of the project source files

    Here the nested includes (``project file > foo.h > bar.h``) and LDF
    will find both libraries ``Foo`` and ``Bar``.

:Case 2:

    * ``lib_ldf_mode = chain``
    * ``Foo/extra.cpp`` depends on the ``Bar`` library (contains ``#include <bar.h>``)
    * ``#include <foo.h>`` is located in one of the project source files

    In this case, LDF will not find the ``Bar`` library because it doesn't know
    about the CPP file (``Foo/extra.cpp``).

:Case 3:

    * ``lib_ldf_mode = deep``
    * ``Foo/extra.cpp`` depends on ``Bar`` library (contains ``#include <bar.h>``)
    * ``#include <foo.h>`` is located in one of the project source files

    Firstly, LDF finds the ``Foo`` library, then it parses all sources
    from the ``Foo`` library and finds ``Foo/extra.cpp`` that depends
    on ``#include <bar.h>``.  Secondly, it will parse all sources from
    the ``Bar`` library. This operation continues until all
    dependencies will not be parsed.

.. _ldf_compat_mode:

Compatibility Mode
------------------

Compatibility mode allows one to control strictness of Library Dependency Finder.
If library contains one of manifest file (:ref:`library_json`,
``library.properties``, ``module.json``), then LDF check compatibility of this
library with real build environment. Available compatibility modes:

:``off``:
    Does not check for compatibility (is not recommended)

:``soft``:
    [**DEFAULT**] Checks for the compatibility with :ref:`projectconf_env_framework` from
    build environment

:``strict``:
    Checks for the compatibility with :ref:`projectconf_env_framework`
    and :ref:`projectconf_env_platform` from build environment.

This mode can be changed using :ref:`projectconf_lib_compat_mode` option in
:ref:`projectconf`. Default value is set to ``soft``.

.. _ldf_c_cond_syntax:

C/C++ Preprocessor conditional syntax
-------------------------------------

In spite of the fact that Library Dependency Finder is written in pure Python,
it evaluates `C/C++ Preprocessor conditional syntax <https://gcc.gnu.org/onlinedocs/cpp/Conditional-Syntax.html#Conditional-Syntax>`_
(``#ifdef``, ``if``, ``defined``, ``else``, and ``elif``) without calling
``gcc -E``. For example,

``platformio.ini``

.. code-block:: ini

    [env:myenv]
    lib_ldf_mode = chain+
    build_flags = -D MY_PROJECT_VERSION=13

``mylib.h``

.. code-block:: c

    #ifdef MY_PROJECT_VERSION
    // include common file for the project
    #include "my_common.h"
    #endif

    #if MY_PROJECT_VERSION < 10
    // this include will be ignored because does not satisfy condition above
    #include "my_old.h"
    #endif
