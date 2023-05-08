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

.. _unit_testing_frameworks_unity:

Unity
-----

:Registry:
  `https://registry.platformio.org/libraries/throwtheswitch/Unity <https://registry.platformio.org/libraries/throwtheswitch/Unity>`_
:Configuration:
  :ref:`projectconf_test_framework` = ``unity``
:Native Tests:
  Yes
:Embedded Tests:
  Yes
:Mocking Support:
  No

**Unity** is a unit test framework. The goal has been to keep it small and
functional. Unity was designed to be cross-platform. It works hard to stick
with C standards while still providing support for the many embedded C
compilers that bend the rules. Unity has been used with many compilers,
including GCC, IAR, Clang, Green Hills, Microchip, and MS Visual Studio.
It's not much work to get it to work with a new target.

.. contents:: Contents
  :local:

Getting Started
~~~~~~~~~~~~~~~

Test files are C/C++ files. Most often you will create a single test file for each C/C++
component that you want to test. The test file should include ``unity.h`` and the header
for your C/C++ component to be tested.

Next, a test file will include a ``setUp()`` and ``tearDown()`` function.
The **setUp** function can contain anything you would like to run before each test.
The **tearDown** function can contain anything you would like to run after each test.
Both functions accept no arguments and return nothing.
You may leave either or both of these blank if you have no need for them.

The majority of the file will be a series of test functions.
Test functions follow the convention of starting with the word ``test_`` or ``spec_``.
You don't HAVE to name them this way, but it makes it clear what functions are tests
for other developers. Test functions take no arguments and return nothing.
All test accounting is handled internally in Unity.

Finally, at the bottom of your test file, you will write a ``main()`` function
(``setup() / loop()`` for :ref:`framework_arduino`, ``app_main()`` for
:ref:`framework_espidf`). This function will call ``UNITY_BEGIN()``, then ``RUN_TEST``
for each test, and finally ``UNITY_END()``.
This is what will actually trigger each of those test functions to run, so it is
important that each function gets its own ``RUN_TEST`` call.
Please remember to add each test to the main function.

When you're done, your test file will look something like this:

.. code:: c

  #include "unity.h"
  #include "file_to_test.h"

  void setUp(void) {
    // set stuff up here
  }

  void tearDown(void) {
    // clean stuff up here
  }

  void test_function_should_doBlahAndBlah(void) {
    // test stuff
  }

  void test_function_should_doAlsoDoBlah(void) {
    // more test stuff
  }

  int runUnityTests(void) {
    UNITY_BEGIN();
    RUN_TEST(test_function_should_doBlahAndBlah);
    RUN_TEST(test_function_should_doAlsoDoBlah);
    return UNITY_END();
  }

  // WARNING!!! PLEASE REMOVE UNNECESSARY MAIN IMPLEMENTATIONS //

  /**
    * For native dev-platform or for some embedded frameworks
    */
  int main(void) {
    return runUnityTests();
  }

  /**
    * For Arduino framework
    */
  void setup() {
    // Wait ~2 seconds before the Unity test runner
    // establishes connection with a board Serial interface
    delay(2000);

    runUnityTests();
  }
  void loop() {}

  /**
    * For ESP-IDF framework
    */
  void app_main() {
    runUnityTests();
  }

**Useful links**

* `Unity - Getting Started <https://github.com/ThrowTheSwitch/Unity/blob/master/docs/UnityGettingStartedGuide.md>`_
* `Unity - Assertions Reference <https://github.com/ThrowTheSwitch/Unity/blob/master/docs/UnityAssertionsReference.md>`_
* `Unity - Assertions CheatSheet <https://github.com/ThrowTheSwitch/Unity/blob/master/docs/UnityAssertionsCheatSheetSuitableforPrintingandPossiblyFraming.pdf>`_

Configuration
~~~~~~~~~~~~~

All of Unity's configuration options are ``#defines``. Most of these are simple
definitions. A couple is macros with arguments. Because these options are specified
via C defines, you can pass most of these options to the :ref:`projectconf_build_flags`.

See `Unity Configuration Guide <https://github.com/ThrowTheSwitch/Unity/blob/master/docs/UnityConfigurationGuide.md>`_
for the available options.

**Example**

.. code:: ini

  [env:extra_unity_options]
  platform = native
  build_flags =
      -D UNITY_INT_WIDTH=16
      -D UNITY_FLOAT_TYPE=float16_t

.. _unit_testing_frameworks_unity_custom_config:

Custom ``unity_config.h``
^^^^^^^^^^^^^^^^^^^^^^^^^

PlatformIO's Unity test runner comes with an already defined ``UNITY_INCLUDE_CONFIG_H``
macro. It looks for a custom ``unity_config.h`` in a current test folder. In case
the ``unity_config.h`` is missed, PlatformIO will walk through the test hierarchy
until to the root (:ref:`projectconf_pio_test_dir`).

Let's take a look at the Pizza Project from the :ref:`unit_testing_test_hierarchy`
example. If you run an "embedded/components/sauce/test_tomatos" test, PlatformIO will
check folders for the ``unity_config.h`` in the following order:

#. "embedded/components/sauce/test_tomatos"
#. "embedded/components/sauce"
#. "embedded/components"
#. "embedded"
#. :ref:`projectconf_pio_test_dir` (finish).

If the ``unity_config.h`` is not found, PlatformIO will generate a default
``unity_config.h`` that routes test result output to a framework specified in the
:ref:`projectconf_env_framework`. On the :ref:`platform_native` development platform,
it will be the standard input/output, whereas, on the embedded development platforms,
the first available Serial interface will be used (see `UNITY_FRAMEWORK_CONFIG <https://github.com/platformio/platformio-core/blob/develop/platformio/test/runners/unity.py>`_
for the default framework configurations).

**Useful links**

* `"unity_config.h" template <https://github.com/ThrowTheSwitch/Unity/blob/master/examples/unity_config.h>`_
* :ref:`tutorial_stm32cube_debugging_unit_testing`
* `STM32Cube Unit Testing <https://github.com/platformio/platformio-examples/tree/develop/unit-testing/stm32cube>`_
  example with the custom ``unity_config.h``.

Custom Unity Library
^^^^^^^^^^^^^^^^^^^^

See :ref:`unit_testing_frameworks_custom_examples_unity_library` example.

Test Runner
~~~~~~~~~~~

Thanks to the minimum system requirements of the Unity testing framework, you can
use Unity for all :ref:`unit_testing_runner_test_types`, including for constrained
embedded devices.

If you would like to change the default PlatformIO's Test Runner
for the Unity, please implement your :ref:`unit_testing_frameworks_custom`
runner extending `UnityTestRunner <https://github.com/platformio/platformio-core/blob/develop/platformio/test/runners/unity.py>`_
class. See :ref:`unit_testing_frameworks_custom` for the examples.
