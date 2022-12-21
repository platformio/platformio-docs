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

.. _projectconf_check_severity:

``check_severity``
------------------

Type: ``String`` | Multiple: ``Yes`` | Default: ``low, medium, high``

This option allows specifying the :ref:`check_severity` types which will
be reported by the :ref:`check_tools`.

Another option for filtering source files is :option:`pio check --severity` command.

**Example**

.. code-block:: ini

    [env:detect_only_medium_or_high_defects]
    platform = ...
    board = ...
    check_severity = medium, high
