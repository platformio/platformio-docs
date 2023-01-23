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

.. _projectconf_pio_shared_dir:

``shared_dir``
--------------

Type: ``DirPath`` | Multiple: ``No`` | Default: "<Project>/``shared``"

:ref:`pioremote` uses this folder to synchronize extra files between remote
machine. For example, you can share :ref:`projectconf_extra_scripts`.

Please note that these folders are automatically shared between remote machine
with :option:`pio remote run --force-remote` or
:option:`pio remote test --force-remote` commands:

- :ref:`projectconf_pio_lib_dir`
- :ref:`projectconf_pio_include_dir`
- :ref:`projectconf_pio_src_dir`
- :ref:`projectconf_pio_boards_dir`
- :ref:`projectconf_pio_data_dir`
- :ref:`projectconf_pio_test_dir`

The default value is ``shared``, meaning a directory named "shared"
located in the root of the project.

This option can also be configured by the global environment variable
:envvar:`PLATFORMIO_SHARED_DIR`.