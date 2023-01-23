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

.. _projectconf_pio_data_dir:

``data_dir``
------------

Type: ``DirPath`` | Multiple: ``No`` | Default: "<Project>/``data``"

Data directory to store contents and :ref:`platform_espressif_uploadfs`.
The default value is ``data`` that means that folder is located in the root of
the project.

This option can also be configured by the global environment variable
:envvar:`PLATFORMIO_DATA_DIR`.