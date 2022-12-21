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

.. _projectconf_lib_compat_mode:

``lib_compat_mode``
-------------------

.. seealso::
    Please make sure to read :ref:`ldf` guide first.

Type: ``String`` | Multiple: ``No`` | Default: ``soft``

Library compatibility mode allows one to control strictness of Library Dependency
Finder. See :ref:`ldf_compat_mode` for details and available options..

By default, this value is set to ``lib_compat_mode = soft`` and means that LDF
will check only for framework compatibility.

Example:

.. code-block:: ini

    [env:myenv]
    ; Checks for the compatibility with frameworks and dev/platforms
    lib_compat_mode = strict
