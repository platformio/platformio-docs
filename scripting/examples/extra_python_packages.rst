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

Extra Python packages
~~~~~~~~~~~~~~~~~~~~~

If your project or library depends on the extra Python packages, you can use extra script to
install them into the same virtual environment where :ref:`piocore` is installed.

``platformio.ini``:

.. code-block:: ini

    [env:my_env]
    platform = ...
    extra_scripts = extra_script.py

``extra_script.py`` (place it near ``platformio.ini``):

.. code-block:: python

    Import("env")

    # List installed packages
    env.Execute("$PYTHONEXE -m pip list")

    # Install custom packages from the PyPi registry
    env.Execute("$PYTHONEXE -m pip install pkg1 pkg2")

    # Install missed package
    try:
    	import some_package
    except ImportError:
    	env.Execute("$PYTHONEXE -m pip install some_package")