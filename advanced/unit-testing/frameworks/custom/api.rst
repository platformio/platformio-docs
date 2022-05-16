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

.. _unit_testing_frameworks_custom_api:

Test Runner API
---------------

.. contents::
  :local:

TestStatus
~~~~~~~~~~

.. py:class:: TestStatus

    :Source Code: `TestStatus <https://github.com/platformio/platformio-core/blob/develop/platformio/test/result.py>`_

    ..  py:attribute:: TestStatus.PASSED

        Attribute to mark test or test suite as passed.

    ..  py:attribute:: TestStatus.FAILED

        Attribute to mark test or test suite as failed.

    ..  py:attribute:: TestStatus.SKIPPED

        Attribute to mark test or test suite as skipped.

    ..  py:attribute:: TestStatus.ERRORED

        Attribute to mark test or test suite as errored.
        It indicates that an unexpected error has happened
        while testing the test suite.

TestCase
~~~~~~~~

.. py:class:: TestCase

    :Source Code: `TestCase <https://github.com/platformio/platformio-core/blob/develop/platformio/test/result.py>`_

    ..  py:attribute:: name

        Name of a test case.

        :Example: ``test_configuration``, ``embedded/test_mqtt_connection``, etc.

    ..  py:attribute:: status

        Instance of ``TestStatus`` class.

        :Example: ``TestStatus.PASSED``

    ..  py:attribute:: message

        Message that explains the reason why a test failed.
        Available only when ``TestCase.status == TestStatus.FAILED``.

    ..  py:attribute:: stdout

        Extra output when running a test case.

    ..  py:attribute:: duration

        Test case duration in seconds.

    ..  py:attribute:: exception

        Unexpected happened when running a test case.
        Should be an instance of the Python ``Exception`` class.

    ..  py:attribute:: source

        Instance of ``TestCaseSource`` (see below) that contains
        details of the source file and a test case line.

TestCaseSource
~~~~~~~~~~~~~~

.. py:class:: TestCaseSource

    :Source Code: `TestCaseSource <https://github.com/platformio/platformio-core/blob/develop/platformio/test/result.py>`_

    ..  py:attribute:: file

        Path of the source file where a test case is implemented.
        The relative path to a project folder is allowed.

    ..  py:attribute:: line

        Number of the line for a test case.

.. _unit_testing_frameworks_custom_api_test_runner:

CustomTestRunner
~~~~~~~~~~~~~~~~

**CustomTestRunner** class must inherit ``TestRunnerBase`` or
the already implemented runners for supported :ref:`unit_testing_frameworks`.
See the source code of
`already implemented runners <https://github.com/platformio/platformio-core/tree/develop/platformio/test/runners>`__.

.. py:class:: CustomTestRunner

        :Source Code:
            `TestRunnerBase <https://github.com/platformio/platformio-core/blob/develop/platformio/test/runners/base.py>`_,

    ..  py:method:: setup(self)

        Method called to prepare the test runner. This is called
        immediately before calling ``self.stage_building()``.
        The default implementation does nothing.

    ..  py:method:: teardown(self)

        Method called immediately after the ``self.stage_testing()``
        method has been called and the result recorded. This is called
        even if the test method raised an exception, so the implementation
        in subclasses may need to be particularly careful about checking
        the internal state. The default implementation does nothing.

    ..  py:method:: stage_building(self)

        Method called to build source code of a particular test.

    ..  py:method:: stage_uploading(self)

        Method called to upload a testing firmware to the target embedded
        device. This method is ignored on the :ref:`platform_native`
        development platform.

    ..  py:method:: stage_testing(self)

        Method called to run test cases and record test results via
        calling ``self.test_suite.add_case(TestCase(...))``.

        You can implement your own testing method depending on the
        target where tests are running. For example, connecting to the
        "BoardFarm/Remote CI Runner" via HTTT/TCP, gathering results,
        parsing them, and recoding via ``self.test_suite.add_case(TestCase(...))``.

    ..  py:method:: configure_build_env(self)

        Method called to configure a SCons build environment in the testing
        mode. It is uesfult to provide extra runtime configuration for a
        testing framework (macros, includes, dynamic configs).

        :Example: See `Unity Test Runner <https://github.com/platformio/platformio-core/blob/develop/platformio/test/runners/unity.py>`__.

    ..  py:method:: on_testing_data_output(self, data)

        Method called on receiving data when running tests
        at the ``stage_testing``. ``data`` can be the
        complete test result output, line, or part of a line.
        When data are chunked, ``on_testing_data_output`` will be called
        multiple times until testing is completed.

        :param str data: testing output data

    ..  py:method:: on_testing_line_output(self, line)

        Method called on each line split from data received
        by ``on_testing_data_output`` method.

        :param str line: testing output line

