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

.. _projectconf_debug_load_mode:

``debug_load_mode``
-------------------

Type: ``String`` | Multiple: ``No`` | Default: ``always``

Allows one to control when PlatformIO should load debugging firmware to the end
target. Possible options:

* ``always`` - load for the each debugging session, **default**
* ``modified`` - load only when firmware was modified
* ``manual`` - do not load firmware automatically. You are responsible to
  pre-flash target with debugging firmware in this case.
