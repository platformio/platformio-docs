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

.. _projectconf_pio_cache_dir:

``cache_dir``
-------------

Type: ``DirPath`` | Multiple: ``No`` | Default: ":ref:`projectconf_pio_core_dir`/cache"

:ref:`piocore` uses this folder to store caching information (requests to
PlatformIO Registry, downloaded packages and other service information).

To reset a cache, please run :ref:`cmd_update` command.

This option can also be configured by the global environment variable
:envvar:`PLATFORMIO_CACHE_DIR`.