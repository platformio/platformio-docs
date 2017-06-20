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

.. _projectconf_section_env_test:

Test options
~~~~~~~~~~~~

.. contents::
    :local:

.. _projectconf_test_ignore:

``test_ignore``
^^^^^^^^^^^^^^^

.. versionadded:: 3.0
.. seealso::
    Please make sure to read :ref:`unit_testing` guide first.

Ignore :ref:`unit_testing` tests where the name matches specified patterns.
Multiple names are allowed. *Please separate them using comma+space ", "*.
Also, you can ignore some tests using :option:`platformio test --ignore` command.

.. list-table::
    :header-rows:  1

    * - Pattern
      - Meaning

    * - ``*``
      - matches everything

    * - ``?``
      - matches any single character

    * - ``[seq]``
      - matches any character in seq

    * - ``[!seq]``
      - matches any character not in seq

**Example**

.. code-block:: ini

  [env:myenv]
  test_ignore = footest, bartest_*, test[13]

.. _projectconf_test_port:

``test_port``
^^^^^^^^^^^^^

This option is used as communication interface (Serial/UART) between PlatformIO
:ref:`unit_testing` Engine and target device. For example,

* ``/dev/ttyUSB0`` - Unix-based OS
* ``COM3`` - Windows OS

If ``test_port`` isn't specified, then *PlatformIO* will try to detect it
automatically.

To print all available serial ports use :ref:`cmd_device_list` command.
