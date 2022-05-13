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

.. _check_severity:

Defect severity
---------------

Defect severity is a classification of software defect (bug,
vulnerability, etc) that indicates the degree of negative impact on the quality
of software.

**Static Code Analysis** uses the next classification of possible defects:

.. list-table::
    :header-rows:  1

    * - Severity
      - Meaning

    * - ``high``
      - Issues that are possibly bugs

    * - ``medium``
      - Suggestions about defensive programming in order to prevent potential bugs

    * - ``low``
      - Issues related to code cleanup and performance (unused functions, redundant code, const-ness, etc)
