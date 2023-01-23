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

.. _projectconf_board_build.ldscript:

``board_build.ldscript``
^^^^^^^^^^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``No``

Path to the linker script to be used instead of the one defined by a framework. This
is useful for specifying a modified linker script, for example, when an application
requires a special memory section for a bootloader.