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

.. _unit_testing_frameworks:

Testing Frameworks
------------------

PlatformIO supports the most popular testing frameworks and allows you to
easily switch between them using the :ref:`projectconf_test_framework`
option in :ref:`projectconf`.

You can mix different frameworks in the same project. For example, use a
more advanced C++ testing framework with Mocks for the :ref:`platform_native`
development platform to run desktop tests on a host machine and a lightweight
framework, such as :ref:`unit_testing_frameworks_unity`, for running tests on the
target embedded device with constrained resources.

**Compatibility**

.. list-table::
  :header-rows:  1

  * - Framework
    - :ref:`unit_testing_runner_test_types`
    - :ref:`platforms`
    - Mocking

  * - :ref:`unit_testing_frameworks_doctest`
    - Native
    - :ref:`platform_native`
    - No

  * - :ref:`unit_testing_frameworks_googletest`
    - Any
    - :ref:`platform_native`, :ref:`platform_espressif8266`,
      :ref:`platform_espressif32`
    - Yes

  * - :ref:`unit_testing_frameworks_unity`
    - Any
    - Any
    - No

.. tip::

  We highly recommend using the :ref:`unit_testing_frameworks_unity` testing
  framework if you plan to run tests on the target devices with constrained
  resources. The :ref:`unit_testing_frameworks_unity` has minimal requirements
  and works even on the 8-bit AVR MCUs.

See supported testing frameworks:

.. toctree::
  :maxdepth: 1

  doctest
  googletest
  unity
  Custom <custom/index>
