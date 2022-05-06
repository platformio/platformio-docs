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

.. _unit_testing_frameworks_doctest:

doctest
-------

:Registry:
  `https://registry.platformio.org/libraries/doctest/doctest <https://registry.platformio.org/libraries/doctest/doctest>`_
:Configuration:
  :ref:`projectconf_test_framework` = ``doctest``

**doctest** is a new C++ testing framework but is by far the fastest both in
compile times and runtime compared to other feature-rich alternatives.

.. warning::
  The **doctest** testing framework **DOES NOT WORK** on the embedded
  devices with constrained resources. The only "Native"
  :ref:`unit_testing_runner_test_types` are supported.

  Please check the :ref:`unit_testing_frameworks_unity` testing framework
  that supports "Embedded" tests.

.. contents:: Contents
  :local:

Getting Started
~~~~~~~~~~~~~~~

To get started with **doctest** all you need is to set
the :ref:`projectconf_test_framework` option in your :ref:`projectconf`
to the ``doctest`` and implement your own ``main()`` function that
forces doctest to report successful test cases.

When you're done, your configuration will look something like this:

``platformio.ini``

.. code:: ini

  [env:native]
  platform = native
  test_framework = doctest


``test/test_dummy/test_main.cpp``

.. code:: cpp

  #define DOCTEST_CONFIG_IMPLEMENT  // REQUIRED: Enables custom main()
  #include <doctest.h>

  // TEST_CASE ...
  // TEST_SUITE ...

  int main(int argc, char **argv)
  {
    doctest::Context context;

    // BEGIN:: PLATFORMIO REQUIRED OPTIONS
    context.setOption("success", true);     // Reports successful tests
    context.setOption("no-exitcode", true); // Do not return non-zero code on failed test case
    // END:: PLATFORMIO REQUIRED OPTIONS

    // YOUR CUSTOM DOCTEST OPTIONS

    context.applyCommandLine(argc, argv);
    return context.run();
  }

Now, you can run tests using the :ref:`cmd_test` command. If you need a
full output from **doctest**, please use :option:`pio test --verbose`
option.

**Useful links**

* `doctest - Tutorial <https://github.com/doctest/doctest/blob/master/doc/markdown/tutorial.md>`_
* `doctest - Assertion macros <https://github.com/doctest/doctest/blob/master/doc/markdown/assertions.md>`_
* `doctest - Logging macros <https://github.com/doctest/doctest/blob/master/doc/markdown/logging.md>`_
* `doctest - Test cases, subcases and test fixtures <https://github.com/doctest/doctest/blob/master/doc/markdown/testcases.md>`_

Configuration
~~~~~~~~~~~~~

The **doctest** can be configured in two ways: using identifiers
(macros) or ``doctest::Context``.

Using identifiers
^^^^^^^^^^^^^^^^^

The **doctest** is designed to "just work" as much as possible. It also allows
configuring how it is built with a set of identifiers.

See `doctest Configuration Guide <https://github.com/doctest/doctest/blob/master/doc/markdown/configuration.md>`_
for the available identifiers.

**Example**

.. code:: ini

  [env:extra_doctest_identifiers]
  platform = native
  test_framework = doctest
  build_flags =
      -D DOCTEST_CONFIG_SUPER_FAST_ASSERTS
      -D DOCTEST_CONFIG_NO_COMPARISON_WARNING_SUPPRESSION

Using ``doctest::Context``
^^^^^^^^^^^^^^^^^^^^^^^^^^

If you need more control and want to set options with code to the
execution context, then the custom implementation of ``main()``
function will give you access to the ``doctest::Context``.

See `The "main()" entry point <https://github.com/doctest/doctest/blob/master/doc/markdown/main.md>`__
docs for details.

**Example**

.. code:: cpp

  int main(int argc, char **argv)
  {
    doctest::Context context;

    // BEGIN:: PLATFORMIO REQUIRED OPTIONS
    context.setOption("success", true);     // Reports successful tests
    context.setOption("no-exitcode", true); // Do not return non-zero code on failed test case
    // END:: PLATFORMIO REQUIRED OPTIONS

    // YOUR CUSTOM DOCTEST OPTIONS
    context.setOption("abort-after", 5);    // stop test execution after 5 failed assertions
    context.setOption("order-by", "name");  // sort the test cases by their name

    context.applyCommandLine(argc, argv);
    return context.run();
  }

Test Runner
~~~~~~~~~~~

If you would like to change the default PlatformIO's Test Runner
for the **doctest**, please implement your :ref:`unit_testing_frameworks_custom`
runner extending `DoctestTestRunner <https://github.com/platformio/platformio-core/blob/develop/platformio/test/runners/doctest.py>`_
class. See :ref:`unit_testing_frameworks_custom` for the examples.
