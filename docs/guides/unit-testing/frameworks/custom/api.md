---
description: "line (str) -- testing output line."
---

<a id="unit-testing-frameworks-custom-api"></a>

# Test Runner API {#test-runner-api}

## TestStatus {#teststatus}

### `class TestStatus` {#TestStatus}

<dl>

<dt>

Source Code

</dt>

<dd>

[TestStatus](https://github.com/platformio/platformio-core/blob/develop/platformio/test/result.py)

</dd>

</dl>

#### `PASSED` {#TestStatus.PASSED}

Attribute to mark test or test suite as passed.

#### `FAILED` {#TestStatus.FAILED}

Attribute to mark test or test suite as failed.

#### `SKIPPED` {#TestStatus.SKIPPED}

Attribute to mark test or test suite as skipped.

#### `ERRORED` {#TestStatus.ERRORED}

Attribute to mark test or test suite as errored. It indicates that an unexpected error has happened while testing the test suite.

## TestCase {#testcase}

### `class TestCase` {#TestCase}

<dl>

<dt>

Source Code

</dt>

<dd>

[TestCase](https://github.com/platformio/platformio-core/blob/develop/platformio/test/result.py)

</dd>

</dl>

#### `name` {#TestCase.name}

Name of a test case.

<dl>

<dt>

Example

</dt>

<dd>

`test_configuration`, `embedded/test_mqtt_connection`, etc.

</dd>

</dl>

#### `status` {#TestCase.status}

Instance of `TestStatus` class.

<dl>

<dt>

Example

</dt>

<dd>

`TestStatus.PASSED`

</dd>

</dl>

#### `message` {#TestCase.message}

Message that explains the reason why a test failed. Available only when `TestCase.status == TestStatus.FAILED`.

#### `stdout` {#TestCase.stdout}

Extra output when running a test case.

#### `duration` {#TestCase.duration}

Test case duration in seconds.

#### `exception` {#TestCase.exception}

Unexpected happened when running a test case. Should be an instance of the Python `Exception` class.

#### `source` {#TestCase.source}

Instance of `TestCaseSource` (see below) that contains details of the source file and a test case line.

## TestCaseSource {#testcasesource}

### `class TestCaseSource` {#TestCaseSource}

<dl>

<dt>

Source Code

</dt>

<dd>

[TestCaseSource](https://github.com/platformio/platformio-core/blob/develop/platformio/test/result.py)

</dd>

</dl>

#### `file` {#TestCaseSource.file}

Path of the source file where a test case is implemented. The relative path to a project folder is allowed.

#### `line` {#TestCaseSource.line}

Number of the line for a test case.

<a id="unit-testing-frameworks-custom-api-test-runner"></a>

## CustomTestRunner {#customtestrunner}

**CustomTestRunner** class must inherit `TestRunnerBase` or the already implemented runners for supported [Testing Frameworks](../index.md). See the source code of [already implemented runners](https://github.com/platformio/platformio-core/tree/develop/platformio/test/runners).

### `class CustomTestRunner` {#CustomTestRunner}

<dl>

<dt>

Source Code

</dt>

<dd>

[TestRunnerBase](https://github.com/platformio/platformio-core/blob/develop/platformio/test/runners/base.py),

</dd>

</dl>

#### `setup(self)` {#CustomTestRunner.setup}

Method called to prepare the test runner. This is called immediately before calling `self.stage_building()`. The default implementation does nothing.

#### `teardown(self)` {#CustomTestRunner.teardown}

Method called immediately after the `self.stage_testing()` method has been called and the result recorded. This is called even if the test method raised an exception, so the implementation in subclasses may need to be particularly careful about checking the internal state. The default implementation does nothing.

#### `stage_building(self)` {#CustomTestRunner.stage_building}

Method called to build source code of a particular test.

#### `stage_uploading(self)` {#CustomTestRunner.stage_uploading}

Method called to upload a testing firmware to the target embedded device. This method is ignored on the [Native](/hardware/platforms/native) development platform.

#### `stage_testing(self)` {#CustomTestRunner.stage_testing}

Method called to run test cases and record test results via calling `self.test_suite.add_case(TestCase(...))`.

You can implement your own testing method depending on the target where tests are running. For example, connecting to the "BoardFarm/Remote CI Runner" via HTTT/TCP, gathering results, parsing them, and recoding via `self.test_suite.add_case(TestCase(...))`.

#### `configure_build_env(self)` {#CustomTestRunner.configure_build_env}

Method called to configure a SCons build environment in the testing mode. It is uesfult to provide extra runtime configuration for a testing framework (macros, includes, dynamic configs).

<dl>

<dt>

Example

</dt>

<dd>

See [Unity Test Runner](https://github.com/platformio/platformio-core/blob/develop/platformio/test/runners/unity.py).

</dd>

</dl>

#### `on_testing_data_output(self, data)` {#CustomTestRunner.on_testing_data_output}

Method called on receiving data when running tests at the `stage_testing`. `data` can be the complete test result output, line, or part of a line. When data are chunked, `on_testing_data_output` will be called multiple times until testing is completed.

<dl>

<dt>

Parameters

</dt>

<dd>

`data` (`str`) -- testing output data

</dd>

</dl>

#### `on_testing_line_output(self, line)` {#CustomTestRunner.on_testing_line_output}

Method called on each line split from data received by `on_testing_data_output` method.

<dl>

<dt>

Parameters

</dt>

<dd>

`line` (`str`) -- testing output line

</dd>

</dl>
