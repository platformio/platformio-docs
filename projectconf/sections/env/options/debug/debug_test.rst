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

.. _projectconf_debug_test:

``debug_test``
--------------

Type: ``String`` | Multiple: ``No``

A name of a unit test to be debugged. See :ref:`unit_testing` for further details.

If a source file of a test is located in the root of :ref:`projectconf_pio_test_dir`,
the ``debug_test`` option should be set to ``*``.

Examples:

.. code-block:: ini

    [env:debug_a_test]
    ...

    debug_test = test_calculator