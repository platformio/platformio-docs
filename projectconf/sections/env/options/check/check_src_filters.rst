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

.. _projectconf_check_src_filters:

.. versionadded:: 6.1.7

``check_src_filters``
---------------------

Type: ``String (Templates)`` | Multiple: ``Yes``

This option allows one to specify which files should be
included or excluded from the check process. The filter supports two templates:

* ``+<PATH>`` include template
* ``-<PATH>`` exclude template

``PATH`` is relative to :ref:`projectconf_pio_src_dir`. All patterns will
be applied in their order of definition.
`GLOB Patterns <http://en.wikipedia.org/wiki/Glob_(programming)>`_ are allowed.

By default, ``check_src_filters`` is predefined to include ALL files from the :ref:`projectconf_pio_src_dir` and :ref:`projectconf_pio_include_dir` folders.

**Example**

.. code-block:: ini

   [env:check_src_filters]
   platform = ...
   board = ...
   check_src_filters =
     -<src/*>
     +<src/spi/spi.cpp>
     -<tests/>
     +<tests/test_embedded/*.c*>
