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

.. _manifest_library_json_export:

``export``
----------

*Optional* | Type: ``Object``

This option is useful if you need to exclude extra data (test code, docs, images, PDFs, etc).
It allows one to reduce the size of the final archive.

To check which files will be included in the final packages, please use
:ref:`cmd_pkg_pack` command.

Possible options:

.. toctree::
    :maxdepth: 2

    include
    exclude
