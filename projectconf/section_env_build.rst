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

.. _projectconf_section_env_build:

Build options
~~~~~~~~~~~~~

.. contents::
    :local:

.. _projectconf_build_flags:

``build_flags``
^^^^^^^^^^^^^^^

These flags/options control preprocessing, compilation, assembly and linking
processes:

.. list-table::
    :header-rows:  1

    * - Format
      - Scope
      - Description
    * - ``-D name``
      - CPPDEFINES
      - Predefine *name* as a macro, with definition 1.
    * - ``-D name=definition``
      - CPPDEFINES
      - The contents of *definition* are tokenized and processed as if they
        appeared during translation phase three in a ``#define`` directive.
    * - ``-U name``
      - CPPDEFINES
      - Cancel any previous definition of *name*, either built in or provided
        with a ``-D`` option.
    * - ``-Wp,option``
      - CPPFLAGS
      - Bypass the compiler driver and pass *option* directly  through to the
        preprocessor
    * - ``-Wall``
      - CCFLAGS
      - Turns on all optional warnings which are desirable for normal code.
    * - ``-Werror``
      - CCFLAGS
      - Make all warnings into hard errors. Source code which triggers warnings will be rejected.
    * - ``-w``
      - CCFLAGS
      - Suppress all warnings, including those which GNU CPP issues by default.
    * - ``-include file``
      - CCFLAGS
      - Process *file* as if ``#include "file"`` appeared as the first line of
        the primary source file.
    * - ``-Idir``
      - CPPPATH
      - Add the directory *dir* to the list of directories to be searched
        for header files.
    * - ``-Wa,option``
      - ASFLAGS, CCFLAGS
      - Pass *option* as an option to the assembler. If *option* contains
        commas, it is split into multiple options at the commas.
    * - ``-Wl,option``
      - LINKFLAGS
      - Pass *option* as an option to the linker. If *option* contains
        commas, it is split into multiple options at the commas.
    * - ``-llibrary``
      - LIBS
      - Search the *library* named library when linking
    * - ``-Ldir``
      - LIBPATH
      - Add directory *dir* to the list of directories to be searched for
        ``-l``.

This option can be set by global environment variable
:envvar:`PLATFORMIO_BUILD_FLAGS`.

For more detailed information about available flags/options go to:

* `Options to Request or Suppress Warnings
  <https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html>`_
* `Options for Debugging Your Program
  <https://gcc.gnu.org/onlinedocs/gcc/Debugging-Options.html>`_
* `Options That Control Optimization
  <https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html>`_
* `Options Controlling the Preprocessor
  <https://gcc.gnu.org/onlinedocs/gcc/Preprocessor-Options.html>`_
* `Passing Options to the Assembler
  <https://gcc.gnu.org/onlinedocs/gcc/Assembler-Options.html>`_
* `Options for Linking <https://gcc.gnu.org/onlinedocs/gcc/Link-Options.html>`_
* `Options for Directory Search
  <https://gcc.gnu.org/onlinedocs/gcc/Directory-Options.html>`_

Examples:

.. code-block:: ini

    [env:specific_defines]
    build_flags =
      -DFOO -DBAR=1
      -D BUILD_ENV_NAME=$PIOENV
      -D CURRENT_TIME=$UNIX_TIME
      -DFLOAT_VALUE=1.23457e+07

    [env:string_defines]
    build_flags =
      -DHELLO="World!"
      '-DWIFI_PASS="My password"'
      ; Password with special chars: My pass'word
      -DWIFI_PASS=\"My\ pass\'word\"

    [env:specific_inclibs]
    build_flags =
      -I/opt/include
      -L/opt/lib
      -lfoo

    [env:specific_ld_script]
    build_flags = -Wl,-T/path/to/ld_script.ld

    [env:ignore_incremental_builds]
    ; We dynamically change the value of "LAST_BUILD_TIME" macro,
    ; PlatformIO will not cache objects
    build_flags = -DLAST_BUILD_TIME=$UNIX_TIME

Built-in Variables
''''''''''''''''''

You can inject into build flags built-in variables, such as:

* ``$PYTHONEXE``, full path to current Python interpreter
* ``$UNIX_TIME``, current time in Unix format
* ``$PIOENV``, name of build environment from :ref:`projectconf`
* ``$PIOPLATFORM``, name of development platform
* ``$PIOFRAMEWORK``, name of framework
* ``$PIOHOME_DIR``, PlatformIO Home directory
* ``$PROJECT_DIR``, project directory
* ``$PROJECTBUILD_DIR``, project build directory per all environments
* ``$BUILD_DIR``, build directory per current environment
* `Need more PlatformIO variables? <https://github.com/platformio/platformio-core/blob/develop/platformio/builder/main.py#L30:L113>`_

Please use target ``envdump`` for :option:`platformio run --target` command to
see ALL variables from a build environment.

.. _projectconf_dynamic_build_flags:

Dynamic build flags
'''''''''''''''''''

PlatformIO allows one to run external command/script which outputs build flags
into STDOUT. PlatformIO will automatically parse this output and append flags
to a build environment.

**You can use any shell or programming language.**

This external command will be called on each :ref:`cmd_run` command before
building/uploading process.

Use Cases:

 * Macro with the latest VCS revision/tag "on-the-fly"
 * Generate dynamic headers (``*.h``)
 * Process media content before generating SPIFFS image
 * Make some changes to source code or related libraries

.. note::
  If you need more advanced control and would like to apply changes to
  PlatformIO Build System environment, please refer to :ref:`projectconf_advanced_scripting`.

Example:

.. code-block:: ini

    [env:generate_flags_with_external_command]
    build_flags = !cmd_or_path_to_script

    ; Unix only, get output from internal command
    build_flags = !echo "-DSOME_MACRO="$(some_cmd arg1 --option1)


**Use Case: Create "PIO_SRC_REV" macro with the latest Git revision**

You will need to create a separate file named ``git_rev_macro.py`` and place it
near ``platformio.ini``.

``platformio.ini``:

.. code-block:: ini

    [env:git_revision_macro]
    build_flags = !python git_rev_macro.py

``git_rev_macro.py``:

.. code-block:: py

    import subprocess

    revision = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip()
    print "-DPIO_SRC_REV=%s" % revision


.. _projectconf_src_build_flags:

``src_build_flags``
^^^^^^^^^^^^^^^^^^^

An option ``src_build_flags`` has the same behavior like ``build_flags``
but will be applied only for the project source code from
:ref:`projectconf_pio_src_dir` directory.

This option can be set by global environment variable
:envvar:`PLATFORMIO_SRC_BUILD_FLAGS`.

.. _projectconf_build_unflags:

``build_unflags``
^^^^^^^^^^^^^^^^^

Remove base/initial flags which were set by development platform.

.. code-block:: ini

   [env:unflags]
   build_unflags = -Os -std=gnu++11
   build_flags = -O2

.. _projectconf_src_filter:

``src_filter``
^^^^^^^^^^^^^^

This option allows one to specify which source files should be included/excluded
from build process. Filter supports 2 templates:

* ``+<PATH>`` include template
* ``-<PATH>`` exclude template

``PATH`` MUST BE related from :ref:`projectconf_pio_src_dir`. All patterns will
be applied in theirs order.
`GLOB Patterns <http://en.wikipedia.org/wiki/Glob_(programming)>`_ are allowed.

By default, ``src_filter`` is predefined to
``+<*> -<.git/> -<svn/> -<example/> -<examples/> -<test/> -<tests/>``,
that means "includes ALL files, then
exclude ``.git`` and ``svn`` repository folders, ``example`` ... folder.

This option can be set by global environment variable
:envvar:`PLATFORMIO_SRC_FILTER`.
