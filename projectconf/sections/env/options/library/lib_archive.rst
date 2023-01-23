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

.. _projectconf_lib_archive:

``lib_archive``
---------------

Type: ``Bool (yes or no)`` | Multiple: ``No`` | Default: ``yes``

Create an archive (``*.a``, static library) from the object files and link it
into a firmware (program). This is default behavior of PlatformIO Build System
(``lib_archive = yes``).

Setting ``lib_archive = no`` will instruct PlatformIO Build System to link object
files directly (in-line). This could be useful if you need to override ``weak``
symbols defined in framework or other libraries.

You can disable library archiving per a custom library using
:ref:`manifest_library_json_build_libArchive` field in :ref:`library_json` manifest.

Example:

.. code-block:: ini

    [env:myenv]
    lib_archive = no