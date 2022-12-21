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

Configuration
-------------

**Static Code Analysis** can be configured from :ref:`projectconf`
using the next options:

.. toctree::
    :maxdepth: 2

    ../../projectconf/sections/env/options/check/index

You can also override some options using :ref:`cmd_check` command.

Custom tool version can be configured using :ref:`projectconf_env_platform_packages` option.
Check `PlatformIO Registry <https://registry.platformio.org/>`_ for the available versions.

**Example**

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    check_tool = cppcheck
    platform_packages = tool-cppcheck@1.260.0

