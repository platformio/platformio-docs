..  Copyright (c) 2019-present PlatformIO <contact@platformio.org>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _projectconf_check_skip_packages:

``check_skip_packages``
-----------------------

Type: ``Bool (yes or no)`` | Multiple: ``No`` | Default: ``no``

Exclude underlying third-party packages from the checking process. By default, PlatformIO
passes frameworks and toolchains include paths required by internal analysis tools to
properly analyze project sources. Some of the supported analysis tools use their own
preprocessor which may fail to parse perfectly valid code and thus provide empty or
partial check reports. This option is useful when developers have no control over this
third-party code and want to perform analysis at least on project sources.

Another option for excluding third-party packages is :option:`pio check --skip-packages`
command.

**Example**

.. code-block:: ini

    [env:extra_check_flags]
    platform = ...
    board = ...
    check_tool = cppcheck, clangtidy
    check_skip_packages = yes