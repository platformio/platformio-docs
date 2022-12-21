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

.. _projectconf_pio_boards_dir:

``boards_dir``
--------------

Type: ``DirPath`` | Multiple: ``No`` | Default: "<Project>/``boards``"

The location of project-specific board definitions. Each project may
choose a suitable directory name.  The default value is ``boards``,
meaning a "boards" directory located in the root of the project.

By default, PlatformIO looks for boards in this order:

1. Project :ref:`projectconf_pio_boards_dir` (as defined by this setting)
2. Global :ref:`projectconf_pio_core_dir`/boards
3. Development platform :ref:`projectconf_pio_core_dir`/platforms/\*/boards.

This option can also be configured by the global environment variable
:envvar:`PLATFORMIO_BOARDS_DIR`.