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
------------

.. seealso::
    Please make sure to read :ref:`unit_testing` guide first.

.. contents::
    :local:

.. _projectconf_test_framework:

``test_framework``
^^^^^^^^^^^^^^^^^^

.. versionadded:: 6.0

Type: ``String`` | Multiple: ``No`` | Default: ``unity``

A Unit Testing framework name. Please follow to the :ref:`unit_testing_frameworks`
for the available frameworks.

.. _projectconf_test_filter:

``test_filter``
^^^^^^^^^^^^^^^

Type: ``String (Pattern)`` | Multiple: ``Yes``

Process only the :ref:`unit_testing` tests where the name matches specified
patterns.

Also, you can override this option using :option:`pio test --filter` command.

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
  test_filter =
    footest
    bartest_*
    test[13]

.. _projectconf_test_ignore:

``test_ignore``
^^^^^^^^^^^^^^^

Type: ``String (Pattern)`` | Multiple: ``Yes``

Ignore :ref:`unit_testing` tests where the name matches specified patterns.

Also, you can override this option using :option:`pio test --ignore` command.

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
  test_ignore =
    footest
    bartest_*
    test[13]

.. _projectconf_test_port:

``test_port``
^^^^^^^^^^^^^

Type: ``String (Pattern)`` | Multiple: ``No``

This option specifies communication interface between PlatformIO
:ref:`unit_testing` Test Runner and the target device. The possible
values are the same as documented for :ref:`projectconf_monitor_port`
option.

If ``test_port`` isn't specified, the PlatformIO :ref:`unit_testing`
runner will try to detect it automatically.

To print all available serial ports use the :ref:`cmd_device_list` command.

.. _projectconf_test_speed:

``test_speed``
^^^^^^^^^^^^^^

Type: ``Number`` | Multiple: ``No`` | Default: ``115200``

A connection speed (`baud rate <http://en.wikipedia.org/wiki/Baud>`_)
to communicate with a target device.

.. _projectconf_test_build_src:

``test_build_src``
^^^^^^^^^^^^^^^^^^

Type: ``Bool (yes or no)`` | Multiple: ``No`` | Default: ``no``

Setting ``test_build_src`` to ``yes`` will force :ref:`unit_testing` engine
to build the main source code from :ref:`projectconf_pio_src_dir` in pair
with a test code. See :ref:`unit_testing_shared_code` for details.

**Example**

.. code-block:: ini

  [env:myenv]
  platform = ...
  test_build_src = yes

.. _projectconf_test_testing_command:

``test_testing_command``
^^^^^^^^^^^^^^^^^^^^^^^^

Type: ``String`` | Multiline Arguments: ``Yes``

A custom testing command that executes test cases and returns results
to the standard output.

Typically, a default value for the :ref:`platform_native` is equal
to:

.. code:: ini

  [env:myenv]
  platform = native
  test_testing_command =
    ${platformio.build_dir}/${this.__env__}/program

You can override the default command and pass extra program arguments:

.. code:: ini

  [env:myenv]
  platform = native
  test_testing_command =
    ${platformio.build_dir}/${this.__env__}/program
    arg1
    --option2
    option2_value

Please note that you can pass extra arguments to the program
using CLI and :option:`pio test --program-arg` option.

See :ref:`unit_testing_simulators` examples.
