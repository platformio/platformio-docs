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

.. _unit_testing_test_runner:

Test Runner
-----------

**PlatformIO Test Runner** is a powerful unit testing tool. It runs
your unit tests located in the :ref:`projectconf_pio_test_dir`, navigates
through tests, and facilitates the processing of test results. Test Runner
supports the most popular :ref:`unit_testing_frameworks`.

Test Runner allows you to run specific project environments or filter
tests using the "Glob patterns". Once tests are finished, Test Runner
provides a rich report with the status of all test suites and test cases
(passed, failed, ignored/skipped).

.. contents::
  :local:

Local Test Runner
~~~~~~~~~~~~~~~~~

**Local Test Runner** allows you to run a test on a local host machine
or on a local target device (board). In this case, you need to use
the :ref:`cmd_test` command.

.. _unit_testing_runner_remote:

Remote Test Runner
~~~~~~~~~~~~~~~~~~

**Remote Test Runner** allows you to run test on the remote machine or
on the remote target device (board) without having to depend on OS software,
extra software, SSH, VPN or opening network ports. Remote Unit Testing
works in pair with :ref:`pioremote`. In this case, you need to use the
special command :ref:`cmd_remote_test`.

PlatformIO supports multiple :ref:`ci` systems where you can run unit tests
at each integration stage.

.. _unit_testing_runner_test_types:

Test Types
~~~~~~~~~~

Before writing a test, you need to decide where it will be executed later:
on the host machine or on the target device connected to the host machine.
Tests that are written for the target device typically will not work on
your host machine due to the missing peripheral and other connectivity.

Using the :ref:`unit_testing_test_hierarchy` allows you to organize tests
by types and later skip an incompatible group of tests using
:ref:`projectconf_test_filter` or :ref:`projectconf_test_ignore` options
in :ref:`projectconf`.

Native
^^^^^^

Native tests are intended for the project components that are independent
of physical hardware. You can also use them in pair with Mocking frameworks.

PlatformIO provides you a :ref:`platform_native` development platform to
build and run tests on the local host machine or using :ref:`ci` VM instance.

.. warning::

  PlatformIO does not install automatically any toolchains
  for the :ref:`platform_native` development platform. It depends
  on the system ``GCC`` toolchain that must be added to the ``PATH``
  system environment variable.

  Please check the "Installation" guide for the :ref:`platform_native`
  development platform.

Embedded
^^^^^^^^

Embedded tests are intended for the target devices (boards, hardware). They allow
you to deeply test all project components that are part of your firmware.

How does PlatformIO Unit Testing Runner process embedded tests?

#. It builds a special firmware intended for your target using a compatible
   embedded development platform
#. Uploads a firmware to the end target (flashes device)
#. Connects to the target using a Serial interface and :ref:`projectconf_test_port`
#. Gathers Serial output from the target and parses test result on the
   host machine
#. Provides test results.

Please check :ref:`unit_testing_frameworks` documentation and learn
how to provide a custom configuration or to get full control of
PlatformIO Unit Testing Runner using :ref:`unit_testing_frameworks_custom`
implementation.

Hybrid
^^^^^^

The tests that work on a host machine and on the embedded target are hybrid tests.
You can run them using :ref:`platform_native` development platform or
embedded development :ref:`platforms`.
