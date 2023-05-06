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

.. _unit_testing_frameworks_googletest:

GoogleTest
----------

:Registry:
  `https://registry.platformio.org/libraries/google/googletest <https://registry.platformio.org/libraries/google/googletest>`_
:Configuration:
  :ref:`projectconf_test_framework` = ``googletest``
:Native Tests:
  Yes
:Embedded Tests:
  Yes* (only for :ref:`platform_espressif8266` and :ref:`platform_espressif32`)
:Mocking Support:
  Yes

**GoogleTest** is a testing framework developed by the Testing Technology
team with Google's specific requirements and constraints in mind. Whether
you work on Linux, Windows, or a Mac, if you write C++ code,
GoogleTest can help you.

.. contents:: Contents
  :local:

Getting Started
~~~~~~~~~~~~~~~

To get started with the GoogleTest all you need is to set
the :ref:`projectconf_test_framework` option in your :ref:`projectconf`
to the ``googletest`` and implement your own ``main()`` function:

``platformio.ini``

.. code:: ini

  [env]
  test_framework = googletest

  [env:native]
  platform = native

  [env:esp32dev]
  platform = espressif32
  framework = arduino
  test_framework = googletest


``test/test_dummy/test_dummy.cpp``

.. code:: cpp

  #include <gtest/gtest.h>
  // uncomment line below if you plan to use GMock
  // #include <gmock/gmock.h>

  // TEST(...)
  // TEST_F(...)

  #if defined(ARDUINO)
  #include <Arduino.h>

  void setup()
  {
      // should be the same value as for the `test_speed` option in "platformio.ini"
      // default value is test_speed=115200
      Serial.begin(115200);

      ::testing::InitGoogleTest();
      // if you plan to use GMock, replace the line above with
      // ::testing::InitGoogleMock();
  }

  void loop()
  {
    // Run tests
    if (RUN_ALL_TESTS())
    ;

    // sleep for 1 sec
    delay(1000);
  }

  #else
  int main(int argc, char **argv)
  {
      ::testing::InitGoogleTest(&argc, argv);
      // if you plan to use GMock, replace the line above with
      // ::testing::InitGoogleMock(&argc, argv);

      if (RUN_ALL_TESTS())
      ;

      // Always return zero-code and allow PlatformIO to parse results
      return 0;
  }
  #endif

Now, you can run tests using the :ref:`cmd_test` command. If you need a
full output from the GoogleTest, please use :option:`pio test --verbose`
option.

**Example**

Please check the complete `GoogleTest example <https://github.com/platformio/platformio-examples/tree/develop/unit-testing/googletest>`_
using GTest, GMock, and PlatformIO.

**Useful links**

* `GoogleTest Primer <https://google.github.io/googletest/primer.html>`_ - Teaches you how to write simple tests using GoogleTest. Read this first if you are new to GoogleTest
* `GoogleTest Advanced <https://google.github.io/googletest/advanced.html>`_ - Read this when you've finished the Primer and want to utilize GoogleTest to its full potential
* `GoogleTest Samples <https://google.github.io/googletest/samples.html>`_ - Describes some GoogleTest samples
* `GoogleTest FAQ <https://google.github.io/googletest/faq.html>`_ - Have a question? Want some tips? Check here first
* `Mocking for Dummies <https://google.github.io/googletest/gmock_for_dummies.html>`_ - Teaches you how to create mock objects and use them in tests
* `Mocking Cookbook <https://google.github.io/googletest/gmock_cook_book.html>`_ - Includes tips and approaches to common mocking use cases
* `Mocking Cheat Sheet <https://google.github.io/googletest/gmock_cheat_sheet.html>`_ - A handy reference for matchers, actions, invariants, and more
* `Mocking FAQ <https://google.github.io/googletest/gmock_faq.html>`_ - Contains answers to some mocking-specific questions.

Configuration
~~~~~~~~~~~~~

The GoogleTest can be configured using system environment variables.
See supported `GoogleTest environment variables <https://google.github.io/googletest/advanced.html#running-test-programs-advanced-options>`_.

GoogleTest CLI
~~~~~~~~~~~~~~

The GoogleTest works quite nicely without any command-line options at all -
but for more control a few of them are available.
See `GoogleTest CLI guide <https://google.github.io/googletest/advanced.html#running-test-programs-advanced-options>`_.

There are two options for how to pass extra arguments to the testing program:

1. Using PlatformIO Core CLI and :option:`pio test --program-arg` option
2. Overriding :ref:`projectconf_test_testing_command` with a custom command.

**Example**

Let's run everything in a test suite ``FooTest`` except ``FooTest.Bar``.

Stop executing test cases after the first error and include  successful
assertions in the output. We will use the ``--gtest_filter``
GoogleTest's CLI option.

1.  Using CLI and :option:`pio test --program-arg` option:

    .. code:: shell

      > pio test --program-arg "--gtest_filter=FooTest.*-FooTest.Bar"
      # or short format
      > pio test -a "--gtest_filter=FooTest.*-FooTest.Bar"

2.  Overriding :ref:`projectconf_test_testing_command` with custom command.

    .. code:: ini

      [env:myenv]
      platform = native
      test_testing_command =
        ${platformio.build_dir}/${this.__env__}/program
        --gtest_filter=FooTest.*-FooTest.Bar

Test Runner
~~~~~~~~~~~

If you would like to change the default PlatformIO's Test Runner
for the GoogleTest, please implement your :ref:`unit_testing_frameworks_custom`
runner extending `GooglestTestRunner <https://github.com/platformio/platformio-core/blob/develop/platformio/test/runners/googletest.py>`_
class. See :ref:`unit_testing_frameworks_custom` for examples.
