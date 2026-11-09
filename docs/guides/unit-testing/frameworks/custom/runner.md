<a id="unit-testing-frameworks-custom-runner"></a>

# Custom Test Runner {#custom-test-runner}

Setting the [test_framework](../../../../reference/platformio-ini/env/test-framework.md) option to the `custom` will instruct PlatformIO to look for a `test_custom_runner.py` file located in the current (running) test folder. If the file is not found, PlatformIO will check the parent folders in a tree until reaches the [test_dir](../../../../reference/platformio-ini/platformio/test-dir.md).

If you plan to use a custom test framework for ALL tests, please put the `test_custom_runner.py` file at the root of [test_dir](../../../../reference/platformio-ini/platformio/test-dir.md). Otherwise, use [Test Hierarchy](../../structure/hierarchy.md) and put it to the test folder or to the group of tests that depend on it.

The `test_custom_runner.py` is a Python-based script. It must contain the [CustomTestRunner](./api.md#unit-testing-frameworks-custom-api-test-runner) class. See a base example of `test_custom_runner.py`:

```python
from platformio.public import TestRunnerBase

class CustomTestRunner(TestRunnerBase):
    pass
```

In case you want to override the functionality of the existing testing framework, you have to inherit its class. For example, let's override a "testing" stage for the [Unity](../unity.md):

```python
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
```

See more custom test runner [Examples](./examples/index.md).
