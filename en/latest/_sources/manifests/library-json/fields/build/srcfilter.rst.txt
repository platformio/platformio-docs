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

.. _library_json_buid_src_filter:

``srcFilter``
~~~~~~~~~~~~~

*Optional* | Type: ``String`` or ``Array``

Specify which source files should be included/excluded from build process.
The path in filter should be relative to the ``srcDir`` option of a library.

See syntax for :ref:`projectconf_build_src_filter`.

Please note that you can generate source filter "on-the-fly" using
``extraScript`` (see below)
