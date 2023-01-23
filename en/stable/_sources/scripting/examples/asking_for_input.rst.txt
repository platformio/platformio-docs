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

Asking for input (prompts)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes you need to ask the user for the input (Wi-Fi password, station name, etc).
Python has a built-in `input() <https://docs.python.org/3/library/functions.html#input>`_
function for this case.

See the example below on how to read a user name and set it to the ``USER_NAME`` macro.

``platformio.ini``:

.. code-block:: ini

    [env:my_env]
    platform = ...
    extra_scripts = prompt-user-data.py

``prompt-user-data.py``:

.. code-block:: python

    Import("env")

    # Do not run a script when external applications, such as IDEs,
    # dump integration data. Otherwise, input() will block the process
    # waiting for the user input
    if env.IsIntegrationDump():
        # stop the current script execution
        Return()

    # Ask user name
    print("Enter your name:")
    user_name = input()
    env.Append(
        CPPDEFINES=[("USER_NAME",  env.StringifyMacro(user_name))],
    )
