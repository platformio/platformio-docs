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

.. _unit_testing_frameworks_custom_runner:

Custom Test Runner
------------------

Setting the :ref:`projectconf_test_framework` option to the ``custom``
will instruct PlatformIO to look for a ``test_custom_runner.py``
file located in the current (running) test folder. If the file is
not found, PlatformIO will check the parent folders
in a tree until reaches the :ref:`projectconf_pio_test_dir`.

If you plan to use a custom test framework for ALL tests, please
put the ``test_custom_runner.py`` file at the root of
:ref:`projectconf_pio_test_dir`. Otherwise, use
:ref:`unit_testing_test_hierarchy` and put it to the test folder
or to the group of tests that depend on it.

The ``test_custom_runner.py`` is a Python-based script. It must
contain the :ref:`unit_testing_frameworks_custom_api_test_runner`
class. See a base example of ``test_custom_runner.py``:

.. code:: python

    from platformio.public import TestRunnerBase

    class CustomTestRunner(TestRunnerBase):
        pass

In case you want to override the functionality of the existing
testing framework, you have to inherit its class. For example,
let's override a "testing" stage for the :ref:`unit_testing_frameworks_unity`:

.. code:: python

    from platformio.public import TestCase, TestCaseSource, TestStatus, UnityTestRunner


    class CustomTestRunner(UnityTestRunner):
        def stage_testing(self):
            # 1. Gather test results from Serial, HTTP, Socket, or other sources
            # 2. Report test results (add cases)

            # Example: Report succeed result with duration (optional)
            self.test_suite.add_case(
                TestCase(name="test_connectivity", status=TestStatus.PASSED, duration=1.34)
            )

            # Example: Report failed result with source file
            self.test_suite.add_case(
                TestCase(
                    name="test_calculator_division",
                    status=TestStatus.FAILED,
                    message="Expected 32 Was 33",
                    stdout="test/test_desktop/test_calculator.cpp:43:test_calculator_division:FAIL: Expected 32 Was 33",
                    duration=0.44,
                    source=TestCaseSource(
                        filename="test/test_desktop/test_calculator.cpp", line=43
                    ),
                )
            )

See more custom test runner :ref:`unit_testing_frameworks_custom_examples`.
