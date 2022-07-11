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

.. _faq_convert_ino_to_cpp:

Convert Arduino file to C++ manually
------------------------------------

Some :ref:`ide` don't support Arduino files (``*.ino`` and ``.pde``) because
they are not valid C/C++ based source files:

1. Missing includes such as ``#include <Arduino.h>``
2. Function declarations are omitted.

In this case, code completion and code linting do not work properly or
are disabled. To avoid this issue you can manually convert your INO files to CPP.

For example, we have the next ``Demo.ino`` file:

.. code-block:: cpp

    void setup () {
        someFunction(13);
    }

    void loop() {
        delay(1000);
    }

    void someFunction(int num) {
    }

Let's convert it to  ``Demo.cpp``:

1. Add ``#include <Arduino.h>`` at the top of the source file
2. Declare each custom function (excluding built-in, such as ``setup`` and ``loop``)
   before it will be called.

The final ``Demo.cpp``:

.. code-block:: cpp

    #include <Arduino.h>

    void someFunction(int num);

    void setup () {
        someFunction(13);
    }

    void loop() {
        delay(1000);
    }

    void someFunction(int num) {
    }

Finish.
