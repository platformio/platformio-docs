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

.. _unit_testing_simulators:

Simulators
----------

Simulation tools and frameworks allow you to simulate hardware systems
and run unit tests in virtual environments. Simulators can significantly
accelerate your project development, especially when used in pair
with :ref:`ci`.

Integration of any simulator tool to the PlatformIO :ref:`unit_testing`
is very simple and does not require any extra software or code writing.
Please use :ref:`projectconf_test_testing_command` project configuration
option and specify a custom command to the simulation program that will
be responsible for the test running. This program must output test
results to the standard output or error stream.

.. note::
  Please note that simulator tools do not require a firmware uploading
  stage. Please use the :option:`pio test --without-uploading` command
  option.

See a few integration examples for the popular simulation tools and
frameworks:

.. toctree::
  :maxdepth: 1

  qemu
  renode
  simavr
