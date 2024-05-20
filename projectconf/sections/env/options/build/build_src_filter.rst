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

.. _projectconf_build_src_filter:

``build_src_filter``
--------------------

Type: ``String (Templates)`` | Multiple: ``Yes``

This option allows one to specify which source files should be
included or excluded from :ref:`projectconf_pio_src_dir` for a build process.
Filter supports two templates:

* ``+<PATH>`` include template
* ``-<PATH>`` exclude template

``PATH`` is relative to :ref:`projectconf_pio_src_dir`. All patterns will
be applied in their order of definition.
`GLOB Patterns <http://en.wikipedia.org/wiki/Glob_(programming)>`_ are allowed.

By default, ``build_src_filter`` is predefined to ``+<*> -<.git/> -<.svn/>``,
meaning "include ALL files, then exclude the ``.git`` and ``.svn`` repository folders.

This option can also be set by the global environment variable
:envvar:`PLATFORMIO_BUILD_SRC_FILTER`.

**Example**

Include all ``.c`` and ``.cpp`` files recursively (``**`` means ANY path)
to the build process but exclude assembly files ``.S`` and ``.asm``:

.. code:: ini

  [env:myenv]
  build_src_filter =
    +<**/*.c>
    +<**/*.cpp>
    -<**/*.S>
    -<**/*.asm>
