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

.. _projectconf_pio_lib_dir:

``lib_dir``
-----------

Type: ``DirPath`` | Multiple: ``No`` | Default: "<Project>/``lib``"

You can put your own/private libraries here. The source code of each library
should be placed in separate directory, like
``lib/private_lib/[here are source files]``. This directory has the highest
priority for :ref:`ldf`.

The default value is ``lib``, meaning a ``lib`` directory located in
the root of the project.

This option can also be configured by the global environment variable
:envvar:`PLATFORMIO_LIB_DIR`.

For example, see how the ``Foo`` and ``Bar`` libraries are organized:

.. code::

    |--lib
    |  |--Bar
    |  |  |--docs
    |  |  |--examples
    |  |  |--src
    |  |     |- Bar.c
    |  |     |- Bar.h
    |  |--Foo
    |  |  |- Foo.c
    |  |  |- Foo.h
    |- platformio.ini
    |--src
       |- main.c


Then in ``src/main.c`` you should use:

.. code-block:: c

    #include <Foo.h>
    #include <Bar.h>

    // rest of H/C/CPP code

PlatformIO will find your libraries automatically, configure the
preprocessor's include paths and build them.