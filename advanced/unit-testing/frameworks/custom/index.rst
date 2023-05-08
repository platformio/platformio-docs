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

.. _unit_testing_frameworks_custom:

Custom Testing Framework
------------------------

:Configuration:
    :ref:`projectconf_test_framework` = ``custom``

.. seealso::
    We welcome you to provide a PR to the
    https://github.com/platformio/platformio-core/pulls with support
    for the missing testing framework or file a new request at
    https://github.com/platformio/platformio-core/issues

If you found a testing framework that is not supported by PlatformIO
or the existing runner has limitations, this guide will help you to
implement a custom Unit Test Runner and get full control of the
testing process.

.. toctree::
    :maxdepth: 2

    runner
    api
    examples/index

