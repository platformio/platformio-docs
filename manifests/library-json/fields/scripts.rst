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

``scripts``
-----------

*Optional* | Type: ``Object``

Execute custom scripts during the special :ref:`cmd_pkg` life cycle events:

.. list-table::
    :header-rows:  1

    * - Event
      - Description
    * - ``postinstall``
      - runs a script AFTER the package has been installed
    * - ``preuninstall``
      - runs a script BEFORE the package is removed.

**Examples**

1.  Run a custom Python script located in the package "scripts" folder AFTER the package is installed.
    Please note that you don't need to specify a Python interpreter for Python scripts.

    .. code-block:: javascript

        "scripts": {
            "postinstall": "scripts/after_install.py"
        }

2.  Run a custom Bash script BEFORE the package is uninstalled.
    The script is declared as a list of command arguments
    and is located at the root of a package:

    .. code-block:: javascript

        "scripts": {
            "preuninstall": ["maintenance.sh", "--action", "uninstall"]
        }