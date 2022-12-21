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

.. _projectconf_pio_test_dir:

``test_dir``
------------

Type: ``DirPath`` | Multiple: ``No`` | Default: "<Project>/``test``"

The directory where :ref:`unit_testing` engine will look for the
tests.  The default value is ``test``, meaning a ``test`` directory
located in the root of the project.

This option can also be configured by the global environment variable
:envvar:`PLATFORMIO_TEST_DIR`.