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

``srcDir``
~~~~~~~~~~

*Optional* | Type: ``String``

The base path where PlatformIO should look for library source code.
The default value is ``src`` and indicates that folder is located in
the root of the library.

Setting ``srcDir`` to ``.`` will instruct PlatformIO
to recursively build all source files located in the root of
the library and its subfolders.

If you need to exclude some files from the build process,
refer to the :ref:`library_json_buid_src_filter`.

**Example**

Build ALL files starting from the root of a library and exclude
``examples`` and ``test`` subfolders:

.. code:: javascript

  {
    "name": "SomeLib",
    "version": "0.0.0",
    "build": {
      "srcDir": ".",
      "srcFilter": "+<*> -<examples> -<test>"
    }
  }
