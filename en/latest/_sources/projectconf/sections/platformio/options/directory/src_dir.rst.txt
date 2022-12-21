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

.. _projectconf_pio_src_dir:

``src_dir``
-----------

Type: ``DirPath`` | Multiple: ``No`` | Default: "<Project>/``src``"

The path to the project's directory with source code. PlatformIO uses
it for the :ref:`cmd_run` command. The default value is ``src``
meaning a ``src`` directory located in the root directory of the project.

This option can also be configured by the global environment variable
:envvar:`PLATFORMIO_SRC_DIR`.

.. note::
    This option is useful for people who migrate from Arduino IDE where
    the source directory should have the same name as the main source file.
    See `example <https://github.com/platformio/platform-atmelavr/tree/develop/examples/arduino-own-src_dir>`__ project with own source directory.
