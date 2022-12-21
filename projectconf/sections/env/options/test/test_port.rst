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

.. _projectconf_test_port:

``test_port``
-------------

Type: ``String (Pattern)`` | Multiple: ``No``

This option specifies communication interface between PlatformIO
:ref:`unit_testing` Test Runner and the target device. The possible
values are the same as documented for :ref:`projectconf_monitor_port`
option.

If ``test_port`` isn't specified, the PlatformIO :ref:`unit_testing`
runner will try to detect it automatically.

To print all available serial ports use the :ref:`cmd_device_list` command.
