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

.. _projectconf_pio_build_cache_dir:

``build_cache_dir``
-------------------

Type: ``DirPath`` | Multiple: ``No`` | Default: None (Disabled)

:ref:`piocore` uses this folder to store derived files from a build system
(objects, firmwares, ELFs). These files are shared between all build
environments. To speed up a build process, you can use the same cache folder
between different projects if they depend on the same development platform and
framework.

This option can also be configured by the global environment variable
:envvar:`PLATFORMIO_BUILD_CACHE_DIR`.

The example of :ref:`projectconf` below instructs PlatformIO Build System to
check :ref:`projectconf_pio_build_cache_dir` for already compiled objects for
:ref:`framework_stm32cube` and project source files. The cached object will
not be used if the original source file was modified or build environment has
a different configuration (new build flags, etc):

.. code-block:: ini

    [platformio]
    ; Set a path to a cache folder
    build_cache_dir =

    ; Examples:
    ; (Unix) build_cache_dir = /path/to/cache/folder
    ; (Windows) build_cache_dir = C:/path/to/cache/folder

    [env:bluepill_f103c6]
    platform = ststm32
    framework = stm32cube
    board = bluepill_f103c6

    [env:nucleo_f411re]
    platform = ststm32
    framework = stm32cube
    board = nucleo_f411re