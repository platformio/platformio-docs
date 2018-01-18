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

.. |PIOUTE| replace:: **PIO Unit Testing Engine**
.. |PIOUTF| replace:: *PIO Unit Testing Framework*

.. _unit_testing:

PIO Unit Testing
================

.. versionadded:: 3.0 (`PlatformIO Plus <https://pioplus.com>`_)

`Unit Testing (wiki) <https://en.wikipedia.org/wiki/Unit_testing>`_
is a software testing method by which individual units of source code, sets
of one or more MCU program modules together with associated control data,
usage procedures, and operating procedures, are tested to determine whether
they are fit for use. Unit testing finds problems early in the development cycle.

.. contents:: Contents
    :local:

Demo
----

Demo of `Local & Embedded: Calculator <https://github.com/platformio/platformio-examples/tree/develop/unit-testing/calculator>`_.

.. image:: ../_static/pioplus-unit-testing-demo.png
    :target: https://youtu.be/bo3VVRZVKhA

Tutorials and Examples
----------------------

Tutorials
~~~~~~~~~

* :ref:`tutorial_unit_testing_blink`
* :ref:`tutorial_stm32cube_debugging_unit_testing`
* `ThingForward: Start Embedded Testing with PlatformIO <http://www.thingforward.io/techblog/2017-07-25-starting-embedded-testing-with-platformio.html>`_
* `ThingForward: Embedded Testing with PlatformIO - Part 2 <http://www.thingforward.io/techblog/2017-08-08-embedded-testing-with-platformio-part-2.html>`_
* `ThingForward: Embedded Testing with PlatformIO – Part 3: Remoting <http://www.thingforward.io/techblog/2017-09-06-embedded-testing-with-platformio-part-3-remoting.html>`_
* `ThingForward: Embedded Testing with PlatformIO – Part 4: Continuous Integration <http://www.thingforward.io/techblog/2017-09-18-embedded-testing-with-platformio-part-4-continuous-integration.html>`_


Project Examples
~~~~~~~~~~~~~~~~

* `Embedded: Wiring Blink <https://github.com/platformio/platformio-examples/tree/develop/unit-testing/wiring-blink>`_
* `Local & Embedded: Calculator <https://github.com/platformio/platformio-examples/tree/develop/unit-testing/calculator>`_
* `Labmet Weather Station <https://github.com/lab804/labmet-weatherstation>`_
* `PlatformIO Remote Unit Testing Example <https://github.com/platformio/platformio-remote-unit-testing-example>`__

For the other examples and source code please follow to
`PlatformIO Unit Testing Examples <https://github.com/platformio/platformio-examples/tree/develop/unit-testing>`_ repository.


Configuration
-------------

|PIOUTE| can be configured from :ref:`projectconf`

* :ref:`projectconf_test_filter`
* :ref:`projectconf_test_ignore`
* :ref:`projectconf_test_port`
* :ref:`projectconf_test_speed`
* :ref:`projectconf_test_transport`

Test Types
----------

Desktop
~~~~~~~

PlatformIO wraps a test and a main program (from :ref:`projectconf_pio_src_dir`)
with |PIOUTF| and builds the final program using :ref:`platform_native`
development platform. Finally, PlatformIO runs tests on the host machine
(desktop or :ref:`ci` VM instance).

.. note::
    PlatformIO does not install any toolchains automatically for
    :ref:`platform_native` and requires ``GCC`` toolchain to be installed
    on your host machine.
    Please open Terminal and check that the ``gcc`` command is installed.

Embedded
~~~~~~~~

PlatformIO wraps a test and main firmware (from :ref:`projectconf_pio_src_dir`)
with |PIOUTF| and builds special firmware for a target device and deploy it.
Then, PlatformIO connects to the embedded device (board) using configured
Serial :ref:`projectconf_test_port` and communicate via
:ref:`projectconf_test_transport`. Finally, it runs tests on embedded side,
collects results, analyzes them and provides a summary on host machine side
(desktop).

.. note::

    Please note that the |PIOUTF| uses the first available ``Serial/UART``
    implementation (depending on a :ref:`projectconf_env_framework`) as a
    communication interface between the |PIOUTE| and target device. If you use
    ``Serial`` in your project, please wrap/hide Serial-based blocks with
    ``#ifndef UNIT_TEST`` macro.

    Also, you can create custom :ref:`projectconf_test_transport` and implement
    base interface.

Test Runner
-----------

Test Runner allows you to process specific environments or ignore tests using
"Glob patterns". You can also ignore tests for specific environments using a
:ref:`projectconf_test_ignore` option from :ref:`projectconf`.

Local
~~~~~
Allows you to run tests on a host machine or on target devices (boards) that are
directly connected to the host machine. In this case, need to use the
:ref:`cmd_test` command.

Remote
~~~~~~

Allows you to run tests on a remote machine or remote target devices (boards)
without having to depend on OS software, extra software, SSH, VPN or opening
network ports. Remote Unit Testing works in pair with :ref:`pioremote`. In this
case, you need to use the special command :ref:`cmd_remote_test`.

PlatformIO supports multiple :ref:`ci` systems where you can run unit tests
on each integration stage. See real
`PlatformIO Remote Unit Testing Example <https://github.com/platformio/platformio-remote-unit-testing-example>`__.

.. _unit_testing_design:

Design
------

The |PIOUTE| design is based on a few isolated components:

1. **Main Program**. Contains the independent modules, procedures, functions or
   methods that will be the target candidates (TC) for testing.
2. **Unit Test**. A small independent program that is intended to re-use TC from
   the main program and apply tests to them.
3. **Test Processor**. The set of approaches and tools that will be used
   to apply tests for the environments from :ref:`projectconf`.

Workflow
--------

1. Create PlatformIO project using the :ref:`cmd_init` command. For Desktop Unit
   Testing (on the host machine), you need to use :ref:`platform_native`.

   .. code-block:: ini

        ; PlatformIO Project Configuration File
        ;
        ;   Build options: build flags, source filter, extra scripting
        ;   Upload options: custom port, speed and extra flags
        ;   Library options: dependencies, extra library storages
        ;
        ; Please visit documentation for the other options and examples
        ; http://docs.platformio.org/page/projectconf.html

        ;
        ; Embedded platforms
        ;

        [env:uno]
        platform = atmelavr
        framework = arduino
        board = uno

        [env:nodemcu]
        platform = espressif8266
        framework = arduino
        board = nodemcuv2

        ;
        ; Desktop platforms (Win, Mac, Linux, Raspberry Pi, etc)
        ; See http://platformio.org/platforms/native
        ;

        [env:native]
        platform = native

2. Place source code for the main program in the ``src`` directory.
3. Wrap ``main()`` or ``setup()/loop()`` methods in the main program with a
   ``UNIT_TEST`` guard:

   .. code-block:: c

        /**
        * Arduino Wiring-based Framework
        */
        #ifndef UNIT_TEST
        #include <Arduino.h>
        void setup () {
          // some code...
        }

        void loop () {
          // some code...
        }
        #endif


   .. code-block:: c

        /**
        * Generic C/C++
        */
        #ifndef UNIT_TEST
        int main(int argc, char **argv) {
          // setup code...

          while (1) {
              // loop code...
          }
          return 0
        }
        #endif

4. Create a ``test`` directory in the root of your project. See :ref:`projectconf_pio_test_dir`.
5. Write the test using :ref:`unit_testing_api`. Each test is a small independent
   program with its own ``main()`` or ``setup()/loop()`` methods. Tests should
   start with ``UNITY_BEGIN()`` and finish with ``UNITY_END()``.

   .. warning::
     If your board does not support software reset via ``Serial.DTR/RTS``,
     you should add >2 seconds delay before ``UNITY_BEGIN()`.
     That time is needed to establish a ``Serial`` communication between the host
     machine and target device.

     .. code-block:: c

         delay(2000); // for Arduino framework
         wait(2);     // for ARM mbed framework
         UNITY_BEGIN();


6. Place the test in the ``test`` directory. If you have more than one test,
   split them into sub-folders. For example, ``test/test_1/*.[c,cpp,h]``,
   ``test_N/*.[c,cpp,h]``, etc. If there is no such directory in the ``test``folder,
   then |PIOUTE| will treat the source code of ``test`` folder as SINGLE test.
7. Run tests using the :ref:`cmd_test` command.

.. _unit_testing_api:

API
---

Summary of the `Unity Test API <https://github.com/ThrowTheSwitch/Unity#unity-test-api>`_:

* `Running Tests <https://github.com/ThrowTheSwitch/Unity#running-tests>`_

  - ``RUN_TEST(func, linenum)``

* `Ignoring Tests <https://github.com/ThrowTheSwitch/Unity#ignoring-tests>`_

  - ``TEST_IGNORE()``
  - ``TEST_IGNORE_MESSAGE (message)``

* `Aborting Tests <https://github.com/ThrowTheSwitch/Unity#aborting-tests>`_

  - ``TEST_PROTECT()``
  - ``TEST_ABORT()``

* `Basic Validity Tests <https://github.com/ThrowTheSwitch/Unity#basic-validity-tests>`_

  - ``TEST_ASSERT_TRUE(condition)``
  - ``TEST_ASSERT_FALSE(condition)``
  - ``TEST_ASSERT(condition)``
  - ``TEST_ASSERT_UNLESS(condition)``
  - ``TEST_FAIL()``
  - ``TEST_FAIL_MESSAGE(message)``

* `Numerical Assertions: Integers <https://github.com/ThrowTheSwitch/Unity#numerical-assertions-integers>`_

  - ``TEST_ASSERT_EQUAL_INT(expected, actual)``
  - ``TEST_ASSERT_EQUAL_INT8(expected, actual)``
  - ``TEST_ASSERT_EQUAL_INT16(expected, actual)``
  - ``TEST_ASSERT_EQUAL_INT32(expected, actual)``
  - ``TEST_ASSERT_EQUAL_INT64(expected, actual)``

  - ``TEST_ASSERT_EQUAL_UINT(expected, actual)``
  - ``TEST_ASSERT_EQUAL_UINT8(expected, actual)``
  - ``TEST_ASSERT_EQUAL_UINT16(expected, actual)``
  - ``TEST_ASSERT_EQUAL_UINT32(expected, actual)``
  - ``TEST_ASSERT_EQUAL_UINT64(expected, actual)``

  - ``TEST_ASSERT_EQUAL_HEX(expected, actual)``
  - ``TEST_ASSERT_EQUAL_HEX8(expected, actual)``
  - ``TEST_ASSERT_EQUAL_HEX16(expected, actual)``
  - ``TEST_ASSERT_EQUAL_HEX32(expected, actual)``
  - ``TEST_ASSERT_EQUAL_HEX64(expected, actual)``
  - ``TEST_ASSERT_EQUAL_HEX8_ARRAY(expected, actual, elements)``

  - ``TEST_ASSERT_EQUAL(expected, actual)``
  - ``TEST_ASSERT_INT_WITHIN(delta, expected, actual)``

* `Numerical Assertions: Bitwise <https://github.com/ThrowTheSwitch/Unity#numerical-assertions-bitwise>`_

  - ``TEST_ASSERT_BITS(mask, expected, actual)``
  - ``TEST_ASSERT_BITS_HIGH(mask, actual)``
  - ``TEST_ASSERT_BITS_LOW(mask, actual)``
  - ``TEST_ASSERT_BIT_HIGH(mask, actual)``
  - ``TEST_ASSERT_BIT_LOW(mask, actual)``

* `Numerical Assertions: Floats <https://github.com/ThrowTheSwitch/Unity#numerical-assertions-floats>`_

  - ``TEST_ASSERT_FLOAT_WITHIN(delta, expected, actual)``
  - ``TEST_ASSERT_EQUAL_FLOAT(expected, actual)``
  - ``TEST_ASSERT_EQUAL_DOUBLE(expected, actual)``

* `String Assertions <https://github.com/ThrowTheSwitch/Unity#string-assertions>`_

  - ``TEST_ASSERT_EQUAL_STRING(expected, actual)``
  - ``TEST_ASSERT_EQUAL_STRING_LEN(expected, actual, len)``
  - ``TEST_ASSERT_EQUAL_STRING_MESSAGE(expected, actual, message)``
  - ``TEST_ASSERT_EQUAL_STRING_LEN_MESSAGE(expected, actual, len, message)``

* `Pointer Assertions <https://github.com/ThrowTheSwitch/Unity#pointer-assertions>`_

  - ``TEST_ASSERT_NULL(pointer)``
  - ``TEST_ASSERT_NOT_NULL(pointer)``

* `Memory Assertions <https://github.com/ThrowTheSwitch/Unity#pointer-assertions>`_

  - ``TEST_ASSERT_EQUAL_MEMORY(expected, actual, len)``


User Guide (CLI)
----------------

.. toctree::
    :maxdepth: 3

    platformio test <../userguide/cmd_test>
    platformio remote test <../userguide/remote/cmd_test>
