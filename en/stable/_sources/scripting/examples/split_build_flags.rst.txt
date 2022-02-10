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

Split C/C++ build flags
~~~~~~~~~~~~~~~~~~~~~~~

``platformio.ini``:

.. code-block:: ini

    [env:my_env]
    platform = ...
    extra_scripts = extra_script.py

``extra_script.py`` (place it near ``platformio.ini``):

.. code-block:: python

    Import("env")

    # General options that are passed to the C and C++ compilers
    env.Append(CCFLAGS=["flag1", "flag2"])

    # General options that are passed to the C compiler (C only; not C++).
    env.Append(CFLAGS=["flag1", "flag2"])

    # General options that are passed to the C++ compiler
    env.Append(CXXFLAGS=["flag1", "flag2"])