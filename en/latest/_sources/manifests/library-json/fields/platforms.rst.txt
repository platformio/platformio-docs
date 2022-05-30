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

``platforms``
-------------

*Optional* | Type: ``String`` or ``Array``

A list with compatible development platforms. The available platform name are defined
in :ref:`platforms` section.

**Example**

.. code-block:: javascript

    "platforms": ["atmelavr", "espressif8266"]

If the library is compatible with the all platforms, then do not declare this field or
use ``*`` symbol:

.. code-block:: javascript

    "platforms": "*"

.. note::
    PlatformIO does not check platforms for compatibility in default mode.
    See :ref:`ldf_compat_mode` for details. If you need a strict checking for compatible
    platforms for a library, please set :ref:`manifest_library_json_build_libCompatMode` to ``strict``.
