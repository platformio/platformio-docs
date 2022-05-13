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

.. _check_tools:

Check tools
-----------

You can switch between or specify multiple tools used for finding defects
using :ref:`projectconf_check_tool` option:

.. code-block:: ini

  [env:myenv]
  platform = ...
  board = ...
  check_tool = cppcheck, clangtidy


Detailed information about supported check tools and their configuration
process can be found on these pages:

.. toctree::
  :maxdepth: 1

  clang-tidy
  cppcheck
  pvs-studio

