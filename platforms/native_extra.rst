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

Installation
------------

PlatformIO does not install automatically any toolchains
for the **native** development platform. It depends
on the system ``GCC`` toolchain that must be added to the ``PATH``
system environment variable.

Please open the system terminal and type ``gcc --version``. If the
``gcc`` command is not found, you have to install the GCC toolchain
manually depending on your operating system:

* **Windows** - follow the `MSYS2 <https://www.msys2.org/>`_
  installation guide and add the following paths to the ``PATH``
  system environment variable:

  .. code::

    C:\msys64\mingw64\bin
    C:\msys64\ucrt64\bin
    C:\msys64\usr\bin

* **Linux** - open the system terminal and run the following commands:

  .. code:: shell

    sudo apt update
    sudo apt install build-essential

* **macOS** - open the system terminal and install Xcode Command Line Tools

  .. code:: shell

    xcode-select --install

Running of Program
------------------

To execute a native program, you need to use ``exec`` target for the
:option:`pio run --target` command. Extra program arguments can be
passed using the :option:`pio run --program-arg` option.

**Example**

.. code:: shell

    > pio run -t exec

    # extra args
    > pio run -t exec --program-arg "arg1" --program-arg="--option1=value1"

    # or short format
    > pio run -t exec -a "arg1" -a "--option1=value1"
