..  Copyright 2014-present PlatformIO <contact@platformio.org>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _tutorial_nordicnrf52_zephyr_debugging_unit_testing_analysis:

Zephyr and Nordic nRF52-DK: debugging, unit testing, project analysis
=====================================================================

The goal of this tutorial is to demonstrate how simple it is to use :ref:`ide_vscode`
to develop, run and debug a simple Bluetooth project using :ref:`framework_zephyr`
framework for the ``Nordic nRF52-DK`` board.

* **Level:** Intermediate
* **Platforms:** Windows, Mac OS X, Linux

**Requirements:**
  - Downloaded and installed :ref:`ide_vscode`
  - Install drivers for :ref:`debugging_tool_jlink` debug tool
  - :ref:`board_nordicnrf52_nrf52_dk` development board

.. contents:: Contents
    :local:

Setting Up the Project
----------------------

#. Click on "PlatformIO Home" button on the bottom PlatformIO Toolbar:

    .. image:: ../../_static/images/tutorials/nordicnrf52/zephyr-debugging-unit-testing-inspect-1.png

#. Click on "New Project", select ``Nordic nRF52-DK`` as the development board,
   :ref:`framework_zephyr` as the framework and a path to the project location
   (or use the default one):

    .. image:: ../../_static/images/tutorials/nordicnrf52/zephyr-debugging-unit-testing-inspect-2.png

Adding Code to the Generated Project
------------------------------------

#. Create a new file ``main.c`` in :ref:`projectconf_pio_src_dir` folder and add the
   following code:

    .. code-block:: c

      //
      // Copyright (c) 2015-2016 Intel Corporation
      //
      // SPDX-License-Identifier: Apache-2.0
      //

      #include <zephyr/types.h>
      #include <stddef.h>
      #include <sys/printk.h>
      #include <sys/util.h>

      #include <bluetooth/bluetooth.h>
      #include <bluetooth/hci.h>

      #define DEVICE_NAME CONFIG_BT_DEVICE_NAME
      #define DEVICE_NAME_LEN (sizeof(DEVICE_NAME) - 1)


      // Set Advertisement data. Based on the Eddystone specification:
      // https://github.com/google/eddystone/blob/master/protocol-specification.md
      // https://github.com/google/eddystone/tree/master/eddystone-url

      static const struct bt_data ad[] = {
          BT_DATA_BYTES(BT_DATA_FLAGS, BT_LE_AD_NO_BREDR),
          BT_DATA_BYTES(BT_DATA_UUID16_ALL, 0xaa, 0xfe),
          BT_DATA_BYTES(BT_DATA_SVC_DATA16,
                    0xaa, 0xfe,
                    0x10, // Eddystone-URL frame type
                    0x00, // Calibrated Tx power at 0m
                    0x00, // URL Scheme Prefix http://www.
                    'z', 'e', 'p', 'h', 'y', 'r',
                    'p', 'r', 'o', 'j', 'e', 'c', 't',
                    0x08) // .org
      };

      // Set Scan Response data
      static const struct bt_data sd[] = {
          BT_DATA(BT_DATA_NAME_COMPLETE, DEVICE_NAME, DEVICE_NAME_LEN),
      };

      static void bt_ready(int err)
      {
          if (err) {
              printk("Bluetooth init failed (err %d)\n", err);
              return;
          }

          printk("Bluetooth initialized\n");

          // Start advertising
          err = bt_le_adv_start(BT_LE_ADV_NCONN, ad, ARRAY_SIZE(ad),
                        sd, ARRAY_SIZE(sd));
          if (err) {
              printk("Advertising failed to start (err %d)\n", err);
              return;
          }

          printk("Beacon started\n");
        }

      void main(void)
      {
          int err;

          printk("Starting Beacon Demo\n");

          // Initialize the Bluetooth Subsystem
          err = bt_enable(bt_ready);
          if (err) {
              printk("Bluetooth init failed (err %d)\n", err);
          }
      }

#. By default Bluetooth feature is disabled, we can enable it by creating a new file
   ``prj.conf`` in ``zephyr`` folder and adding the following lines:

    .. code-block:: none

      CONFIG_BT=y
      CONFIG_BT_DEBUG_LOG=y
      CONFIG_BT_DEVICE_NAME="Test beacon"

Compiling and Uploading the Firmware
------------------------------------

#. To compile the project use one of the following options:

    - Build option from the ``Project Tasks`` menu
    - Build button in :ref:`ide_vscode_toolbar`
    - Task Menu ``Tasks: Run Task... > PlatformIO: Build`` or in :ref:`ide_vscode_toolbar`
    - Command Palette ``View: Command Palette > PlatformIO: Build``
    - Hotkeys ``cmd-alt-b / ctrl-alt-b``:

    .. image:: ../../_static/images/tutorials/nordicnrf52/zephyr-debugging-unit-testing-inspect-3.png

#. If everything went well, we should see a successful result message in the terminal
   window:

    .. image:: ../../_static/images/tutorials/nordicnrf52/zephyr-debugging-unit-testing-inspect-4.png

#. To upload the firmware to the board we can use the following options:

    - Upload option from the ``Project Tasks`` menu
    - Upload button in :ref:`ide_vscode_toolbar`
    - Command Palette ``View: Command Palette > PlatformIO: Upload``
    - Task Menu ``Tasks: Run Task... > PlatformIO: Upload``
    - Hotkeys ``cmd-alt-u / ctrl-alt-u``:

    .. image:: ../../_static/images/tutorials/nordicnrf52/zephyr-debugging-unit-testing-inspect-5.png

#. Connect the board to your computer and update the default monitor speed to
   ``115200`` in ``platformio.ini`` file:

    .. code-block:: ini

      [env:hifive1-revb]
      platform = sifive
      board = hifive1-revb
      framework = zephyr
      monitor_speed = 115200

#. Open Serial Monitor to observe the output from the board:

    .. image:: ../../_static/images/tutorials/nordicnrf52/zephyr-debugging-unit-testing-inspect-6.png

#. If everything went well, the board should be visible as a beacon:

    .. image:: ../../_static/images/tutorials/nordicnrf52/zephyr-debugging-unit-testing-inspect-7.png

Debugging the Firmware
----------------------

Since `Nordic nRF52-DK <https://docs.platformio.org/en/latest/boards/nordicnrf52/nrf52_dk.html>`__
includes an onboard debug probe we can use :ref:`piodebug` without any configuration.

#. To start a debug session we can use the following options:

    - ``Debug: Start debugging`` from the top menu
    - ``Start Debugging`` option from Quick Access menu
    - Hotkey button ``F5``:

    .. image:: ../../_static/images/tutorials/nordicnrf52/zephyr-debugging-unit-testing-inspect-8.png

#. We can walk through the code using control buttons, set breakpoints, add variables
   to ``Watch window``:

    .. image:: ../../_static/images/tutorials/nordicnrf52/zephyr-debugging-unit-testing-inspect-9.png

Writing Unit Tests
------------------

.. note::
    Functions ``setUp`` and ``tearDown`` are used to initialize and finalize test
    conditions. Implementations of these functions are not required for running tests
    but if you need to initialize some variables before you run a test, you use the
    ``setUp`` function and if you need to clean up variables you use ``tearDown``
    function.

For the sake of simplicity, let's create a small library called ``calculator``,
implement several basic functions ``add``, ``sub``, ``mul``, ``div`` and test them using
:ref:`unit_testing` engine.

#. PlatformIO uses a unit testing framework called ``Unity``. ``Unity`` is not
   compatible with C library implemented in the framework. Let's enable standard
   version of newlib C library in ``prj.conf`` file using the following config:

    .. code-block:: none

      CONFIG_NEWLIB_LIBC=y

#. Create a new folder ``calculator`` in the ``lib`` folder and add two new files
   ``calculator.h`` and ``calculator.c`` with the following contents:

    ``calculator.h``:

    .. code-block:: c

      #ifndef _CALCULATOR_H_
      #define _CALCULATOR_H_

      #ifdef __cplusplus
      extern "C" {
      #endif

      int add (int a, int b);
      int sub (int a, int b);
      int mul (int a, int b);
      int div (int a, int b);

      #ifdef __cplusplus
      }
      #endif

      #endif // _CALCULATOR_H_


    ``calculator.c``:

    .. code-block:: c

      #include "calculator.h"

      int add(int a, int b)
      {
          return a + b;
      }

      int sub(int a, int b)
      {
          return a - b;
      }

      int mul(int a, int b)
      {
          return a * b;
      }

#. Create a new file ```test_calc.c`` to the folder ``test`` and add basic tests for
   ``calculator`` library:

    .. code-block:: c

      #include <calculator.h>
      #include <unity.h>

      void test_function_calculator_addition(void) {
          TEST_ASSERT_EQUAL(32, add(25, 7));
      }

      void test_function_calculator_subtraction(void) {
          TEST_ASSERT_EQUAL(20, sub(23, 3));
      }

      void test_function_calculator_multiplication(void) {
          TEST_ASSERT_EQUAL(50, mul(25, 2));
      }

      void test_function_calculator_division(void) {
          TEST_ASSERT_EQUAL(32, div(100, 3));
      }

      void main() {
          UNITY_BEGIN();

          RUN_TEST(test_function_calculator_addition);
          RUN_TEST(test_function_calculator_subtraction);
          RUN_TEST(test_function_calculator_multiplication);
          RUN_TEST(test_function_calculator_division);

          UNITY_END();
      }

#. Let's run tests on the board and check the results. There should be a problem
   with ``test_function_calculator_division`` test:

    .. image:: ../../_static/images/tutorials/nordicnrf52/zephyr-debugging-unit-testing-inspect-10.png

#. Let's fix the incorrect expected value, run tests again. After processing the
   results should be correct:

    .. image:: ../../_static/images/tutorials/nordicnrf52/zephyr-debugging-unit-testing-inspect-11.png

Project Inspection
------------------

For illustrative purposes, let's imagine we need to find a function with the biggest
memory footprint. Also, let's introduce a bug to our project so :ref:`piocheck` can
report it.

#. Open ``PlatformIO Home`` and navigate to ``Inspect`` section, select the current
   project and press ``Inspect`` button:

    .. image:: ../../_static/images/tutorials/nordicnrf52/zephyr-debugging-unit-testing-inspect-12.png

#. Project statistics:

    .. image:: ../../_static/images/tutorials/nordicnrf52/zephyr-debugging-unit-testing-inspect-13.png

#. The biggest function:

    .. image:: ../../_static/images/tutorials/nordicnrf52/zephyr-debugging-unit-testing-inspect-14.png

#. Possible bugs:

    .. image:: ../../_static/images/tutorials/nordicnrf52/zephyr-debugging-unit-testing-inspect-15.png

Conclusion
----------

Now we have a project template for Nordic `Nordic nRF52-DK <https://docs.platformio.org/en/latest/boards/nordicnrf52/nrf52_dk.html>`__
board that we can use as a boilerplate for the next projects.
