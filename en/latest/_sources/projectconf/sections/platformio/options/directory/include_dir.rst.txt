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

.. _projectconf_pio_include_dir:

``include_dir``
---------------

Type: ``DirPath`` | Multiple: ``No`` | Default: "<Project>/``include``"

The path to project's default header files. PlatformIO uses it for the
:ref:`cmd_run` command. The default value is ``include`` meaning an
``include`` directory located under the root directory of the project. This
path will be added to ``CPPPATH`` of the build environment.

If you need to add extra include directories to ``CPPPATH`` scope, please use
:ref:`projectconf_build_flags` with ``-I /path/to/extra/dir`` option.

This option can also be configured by the global environment variable
:envvar:`PLATFORMIO_INCLUDE_DIR`.
