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

.. _manifest_library_json_schema:

``$schema``
-----------

*Optional* | Type: ``String``

A `JSON Schema <https://json-schema.org/>`__ to annotate and validate the ``library.json`` manifest.
The :ref:`ide_vscode` has built-in support for JSON Schema validation.

You can also validate the ``library.json`` manifest file using the :ref:`cmd_pkg_pack` command.

The ``library.json`` Schema URL:

.. code:: shell

  https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/schema/library.json


**Example**

.. code:: javascript

  {
    "$schema": "https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/schema/library.json",
    "name": "Foo",
    "version": "1.0.0"
  }