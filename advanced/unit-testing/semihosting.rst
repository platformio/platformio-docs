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

.. _unit_testing_semihosting:

Semihosting
-----------

Semihosting is a mechanism that enables code running on the target device
to communicate and use the Input/Output of the host computer.

.. contents::
  :local:

Introduction
~~~~~~~~~~~~

- `Introduction to ARM Semihosting <https://interrupt.memfault.com/blog/arm-semihosting>`_
- `Official ARM documentation <https://www.keil.com/support/man/docs/armcc/armcc_pge1358787046598.htm>`_
- `Segger: Semihosting <https://wiki.segger.com/Semihosting>`_

Configuration
~~~~~~~~~~~~~

Firstly, to enable semihosting, you need to remove stubs (``-lnosys`` and
``-specs=nosys.specs`` flags) from a development platform,
and use the semihosted version of the syscalls (adding
``--specs=rdimon.specs`` and ``-lrdimon`` to the compiler).

Secondly, you need to override the :ref:`projectconf_test_testing_command`
and configure a tool that will redirect test results to the I/O.

Example
~~~~~~~

In this example, we run a simple ``test_dummy`` test on the
:ref:`board_ststm32_nucleo_l152re` board from the
:ref:`platform_ststm32` development platform.

The configuration is done in ``enable_semihosting.py`` extra script using
:ref:`scripting`. The example uses :ref:`unit_testing_frameworks_unity`
testing framework and the :ref:`unit_testing_frameworks_unity_custom_config`.

See the `source code and complete PlatformIO project <https://github.com/platformio/platformio-examples/tree/develop/unit-testing/semihosting>`_.

Testing
~~~~~~~

We use the :ref:`cmd_test` command to run the tests.

.. code::

  > pio test

  Verbose mode can be enabled via `-v, --verbose` option
  Collected 1 tests

  Processing test_dummy in nucleo_l1521re environment
  ---------------------------------------------------
  Building...
  Uploading...
  Testing...
  Info : clock speed 300 kHz
  Info : STLINK V2J29M18 (API v2) VID:PID 0483:374B
  Info : Target voltage: 3.272727
  Info : stm32l1.cpu: Cortex-M3 r2p0 processor detected
  Info : stm32l1.cpu: target has 6 breakpoints, 4 watchpoints
  Info : starting gdb server for stm32l1.cpu on 3333
  Info : Listening on port 3333 for gdb connections
  semihosting is enabled
  Info : Unable to match requested speed 300 kHz, using 240 kHz
  Info : Unable to match requested speed 300 kHz, using 240 kHz
  Info : Listening on port 6666 for tcl connections
  Info : Listening on port 4444 for telnet connections
  test/test_dummy/test_main.c:19: test_dummy	[PASSED]
  -------------------- nucleo_l1521re:test_dummy [PASSED] Took 5.43 seconds --------------------

  ===================================== SUMMARY =====================================
  Environment     Test        Status    Duration
  --------------  ----------  --------  ------------
  nucleo_l1521re  test_dummy  PASSED    00:00:05.433
  ==================== 1 test cases: 1 succeeded in 00:00:05.433 ====================
