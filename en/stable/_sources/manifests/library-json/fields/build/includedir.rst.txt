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

``includeDir``
~~~~~~~~~~~~~~

*Optional* | Type: ``String``

The base path to be searched for header files.
The default value is ``include`` and indicates that the folder
is located at the root of the library. Setting ``includeDir``
to ``.`` will change the base path to the root of the library.

If you need to export additional relative paths, refer to
:ref:`library_json_buid_flags`.

.. note::
    The :ref:`ldf` will pick a library automatically only when
    a project or other dependent libraries include any header file
    located in ``includeDir`` or ``srcDir``.

**Example**

Override the base include path to the library root directory and
provide the custom include paths:

.. code:: javascript

  {
    "name": "SomeLib",
    "version": "0.0.0",
    "build": {
      "includeDir": ".",
      "flags": [
        "-I include",
        "-I extra",
        "-I drivers"
      ]
    }
  }
