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

.. _projectconf_pio_workspace_dir:

``workspace_dir``
-----------------

Type: ``DirPath`` | Multiple: ``No`` | Default: "<Project>/``.pio``"

The path to a project workspace directory where PlatformIO keeps by default
compiled objects, static libraries, firmwares, and external library
dependencies. It is used by these options:

- :ref:`projectconf_pio_build_dir`
- :ref:`projectconf_pio_libdeps_dir`.

The default value is ``.pio`` and means that folder is located in the root of
project.

This option can also be configured by the global environment variable
:envvar:`PLATFORMIO_WORKSPACE_DIR`.