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

.. _projectconf_pio_core_dir:

``core_dir``
------------

Type: ``DirPath`` | Multiple: ``No``

The core_dir variable points out the directory used for all
development platform packages (toolchains, frameworks, SDKs, upload
and debug tools), global libraries for :ref:`ldf`, and other
PlatformIO Core service data. The size of this folder will depend on
the number of installed development platforms.

The default value is the user's home directory:

* Unix ``~/.platformio``
* Windows ``%HOMEPATH%\.platformio``

This option can also be configured by the global environment variable
:envvar:`PLATFORMIO_CORE_DIR`.

Example:

.. code-block:: ini

    [platformio]
    core_dir = /path/to/custom/pio-core/storage
