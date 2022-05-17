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

.. _unit_testing_frameworks_custom_examples_unity_library:

Custom Unity Library
--------------------

There are frameworks such as :ref:`framework_arduino` with Mbed core
and :ref:`framework_espidf` that contain a prebuilt library of
:ref:`unit_testing_frameworks_unity` testing framework. Using
PlatformIO's version of :ref:`unit_testing_frameworks_unity` will lead
to compilation issues ("multiple definitions").
See `issue #3980 <https://github.com/platformio/platformio-core/issues/3980>`_.

The example below allows you to use PlatformIO's :ref:`unit_testing_frameworks_unity`
Test Runner and your custom Unity library. It can be a part of
:ref:`frameworks` or as a project dependency declared in :ref:`projectconf_lib_deps`.

.. contents::
  :local:

Project Example
~~~~~~~~~~~~~~~

We have a project based on Arduino Mbed-core that ships with a custom
prebuilt "libunity.a". Let's leverage from the existing
:ref:`unit_testing_frameworks_unity` Test Runner and disable the default
`throwtheswitch/Unity <https://registry.platformio.org/libraries/throwtheswitch/Unity>`_
package.

Structure
^^^^^^^^^

.. code::

    /project
    ├── platformio.ini
    └── test
        ├── test_blink
        │   └── test_main.cpp
        └── test_custom_runner.py

    2 directories, 3 files

File contents
^^^^^^^^^^^^^

``platformio.ini``

.. code:: ini

    [env:nano33ble]
    platform = nordicnrf52
    board = nano33ble
    framework = arduino
    test_framework = custom

``test/test_custom_runner.py``

:ref:`unit_testing_frameworks_custom_runner` based on
`UnityTestRunner <https://github.com/platformio/platformio-core/blob/develop/platformio/test/runners/unity.py>`_.


.. code:: python

    from platformio.public import UnityTestRunner

    class CustomTestRunner(UnityTestRunner):

        # Ignore "throwtheswitch/Unity" package
        EXTRA_LIB_DEPS = None

        # Do not add default Unity to the build process
        def configure_build_env(self, env):
            pass

``test/test_blink/test_main.cpp``

.. code:: cpp

    #include <Arduino.h>
    #include <unity.h>

    void setUp(void) {
        // set stuff up here
    }

    void tearDown(void) {
        // clean stuff up here
    }

    void simple_test(void)
    {
        TEST_ASSERT_EQUAL(33, 33);
    }

    void setup()
    {
        delay(2000);

        UNITY_BEGIN();
        RUN_TEST(simple_test);
        UNITY_END();
    }

    void loop()
    {
        delay(1000);
    }




