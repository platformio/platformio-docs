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

.. _projectconf_extra_scripts:

``extra_scripts``
-----------------

Type: ``FilePath`` | Multiple: ``Yes``

A list of PRE and POST extra scripts. Paths are relative to the project
folder. See details and examples in the :ref:`scripting` and
:ref:`scripting_launch_types` sections.

If you plan to share these scripts with :ref:`pioremote` machine, please
put them to :ref:`projectconf_pio_shared_dir`.

This option can also be set by the global environment
variable :envvar:`PLATFORMIO_EXTRA_SCRIPTS`.
