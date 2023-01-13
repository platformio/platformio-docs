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

.. _library_json:

library.json
============

``library.json`` is a manifest file of a library package. It allows developers
to keep a project in its own structure and define:

* compatible frameworks and platforms
* external dependencies
* advanced build settings.

Information in ``library.json`` should be represented in `JSON-style <http://en.wikipedia.org/wiki/JSON>`_
via `associative array <http://en.wikipedia.org/wiki/Associative_array>`_
(name/value pairs). The order doesn't matter. The allowable fields
(names from pairs) are described below.

You can validate ``library.json`` manifest file using the :ref:`cmd_pkg_pack` command
or :ref:`manifest_library_json_schema`.

.. toctree::
    :maxdepth: 2

    fields/schema
    fields/name
    fields/version
    fields/description
    fields/keywords
    fields/homepage
    fields/repository
    fields/authors
    fields/license
    fields/frameworks
    fields/platforms
    fields/headers
    fields/examples
    fields/dependencies
    fields/export/index
    fields/scripts
    fields/build/index
