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

.. _projectconf_test_testing_command:

``test_testing_command``
------------------------

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