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

``builder``
~~~~~~~~~~~

*Optional* | Type: ``String``

Override default ``PlatformIOLibBuilder`` with another builder. Currently supported
builders:

* ``PlatformIOLibBuilder`` (default)
* ``ArduinoLibBuilder``
* ``MbedLibBuilder``

Examples
--------

1. Custom macros/defines

.. code-block:: javascript

    "build": {
        "flags": "-D MYLIB_REV=1.2.3 -DRELEASE"
    }

2. Extra includes for C preprocessor

.. code-block:: javascript

    "build": {
        "flags": [
            "-I inc",
            "-I inc/target_x13"
        ]
    }

3. Force to use ``C99`` standard instead of ``C11``

.. code-block:: javascript

    "build": {
        "unflags": "-std=gnu++11",
        "flags": "-std=c99"
    }

4. Build source files (``c, cpp, h``) at the top level of the library

.. code-block:: javascript

    "build": {
        "srcFilter": [
            "+<*.c>",
            "+<*.cpp>",
            "+<*.h>"
        ]
    }


5. Extend PlatformIO Build System with own extra script

.. code-block:: javascript

    "build": {
        "extraScript": "generate_headers.py"
    }

``generate_headers.py``

.. code-block:: python

    Import('env')
    # print(env.Dump())
    env.Append(
        CPPDEFINES=["HELLO=WORLD", "TAG=1.2.3", "DEBUG"],
        CPPPATH=["inc", "inc/devices"]
    )

    # some python code that generates header files "on-the-fly"
