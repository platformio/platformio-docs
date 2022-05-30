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

.. _unit_testing:

Unit Testing
============

Unit Testing is a software testing technique that reduces defects in the
newly developed features or reduces bugs when changing the existing functionality.

**PlatformIO Unit Testing** allows you to segregate each part of the firmware/program
and test that the individual parts are working correctly. Using PlatformIO you
can execute the same tests on the local host machine (native), on the multiple
local embedded devices/boards (connected to local host machine), or on both.
When testing both, PlatformIO builds firmware on the host machine, uploads it into
a target device, starts tests and collects the test results into test reports.
The final information will be shown on the host side with informative output
and statistics.

Using :ref:`pioremote` you can start unit tests on the **Remote Device** from
anywhere in the world or integrate with :ref:`ci` systems.

.. toctree::
    :maxdepth: 2

    introduction
    runner
    structure/index
    configuration
    frameworks/index
    simulators/index
    semihosting
    cli
