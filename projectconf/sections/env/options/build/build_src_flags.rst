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

.. _projectconf_build_src_flags:

``build_src_flags``
-------------------

Type: ``String`` | Multiple: ``Yes``

An option ``build_src_flags`` has the same behavior as ``build_flags``
but will be applied only for the project source files in the
:ref:`projectconf_pio_src_dir` directory.

This option can also be set by the global environment variable
:envvar:`PLATFORMIO_BUILD_SRC_FLAGS`.