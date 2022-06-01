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

``include``
~~~~~~~~~~~

*Optional* | Type: ``Array`` | `Glob Pattern <http://en.wikipedia.org/wiki/Glob_(programming)>`_

Export only files that matched declared patterns.

**Pattern Meaning**

.. list-table::
    :header-rows:  1

    * - Pattern
      - Meaning
    * - ``*``
      - matches everything
    * - ``?``
      - matches any single character
    * - ``[seq]``
      - matches any character in seq
    * - ``[!seq]``
      - matches any character not in seq

**Example**

.. code-block:: javascript

    "export": {
        "include":
        [
            "dir/*.[ch]pp",
            "dir/examples/*",
            "*/*/*.h"
        ]
    }

