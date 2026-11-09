---
sidebar_label: "Zephyr on nRF52-DK"
description: Build, upload, debug, unit test and inspect a Zephyr Bluetooth beacon on the Nordic nRF52-DK with PlatformIO IDE for VS Code.
---

# Zephyr on Nordic nRF52-DK: debugging, unit testing and project analysis

In this tutorial you use [PlatformIO IDE for VS Code](../../../guides/ide/vscode.md)
to build a Bluetooth LE beacon with the [Zephyr](/hardware/frameworks/zephyr)
framework on the Nordic nRF52-DK board. You then debug it, unit test a small
library on the board, and inspect the firmware's memory use and code quality.

- **Level:** intermediate
- **Host:** Windows, macOS or Linux

## What you need {#what-you-need}

- [PlatformIO IDE for VS Code](../../../guides/ide/vscode.md), installed.
- A [Nordic nRF52-DK](/hardware/boards/nordicnrf52/nrf52-dk) board.
- The [J-Link drivers](../../../hardware/debug-probes/jlink.md) for the board's
  on-board J-Link probe.

## Create the project {#setting-up-the-project}

1. Select the **Home** button on the PlatformIO toolbar to open
   [PlatformIO Home](../../platformio-home.md):

   ![PlatformIO toolbar with the Home button](./img/zephyr-debugging-unit-testing-inspect-1.png)

2. Select **New Project**. Choose **Nordic nRF52-DK** as the board and
   **Zephyr** as the framework, keep or change the location, and select
   **Finish**:

   ![Project wizard with the nRF52-DK board and Zephyr framework](./img/zephyr-debugging-unit-testing-inspect-2.png)

## Add the code {#adding-code-to-the-generated-project}

1. Create `src/main.c` (in the [`src_dir`](../../../reference/platformio-ini/platformio/src-dir.md)
   folder) with the following code, based on the Zephyr beacon sample. It
   advertises an [Eddystone-URL](https://github.com/google/eddystone/tree/master/eddystone-url)
   beacon:

   ```c
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
     if (err)
     {
       printk("Bluetooth init failed (err %d)\n", err);
       return;
     }

     printk("Bluetooth initialized\n");

     // Start advertising
     err = bt_le_adv_start(BT_LE_ADV_NCONN, ad, ARRAY_SIZE(ad),
                           sd, ARRAY_SIZE(sd));
     if (err)
     {
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
     if (err)
     {
       printk("Bluetooth init failed (err %d)\n", err);
     }
   }
   ```

2. Bluetooth is disabled in Zephyr by default. Enable it in the Zephyr project
   configuration: create `zephyr/prj.conf` with these lines:

   ```text
   CONFIG_BT=y
   CONFIG_BT_DEBUG_LOG=y
   CONFIG_BT_DEVICE_NAME="Test beacon"
   ```

3. Zephyr prints its log at 115200 baud. Set the serial monitor to the same
   speed with [`monitor_speed`](../../../reference/platformio-ini/env/monitor-speed.md)
   in `platformio.ini`:

   ```ini
   [env:nrf52_dk]
   platform = nordicnrf52
   board = nrf52_dk
   framework = zephyr
   monitor_speed = 115200
   ```

## Build, upload and run {#compiling-and-uploading-the-firmware}

1. Build the project with **Build** in the **Project Tasks** panel, the
   **Build** button on the [PlatformIO toolbar](../../../guides/ide/vscode.md#platformio-toolbar),
   **Command Palette** > **PlatformIO: Build**, or
   <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>B</kbd>
   (<kbd>Cmd</kbd>+<kbd>Alt</kbd>+<kbd>B</kbd> on macOS):

   ![Ways to start a build](./img/zephyr-debugging-unit-testing-inspect-3.png)

   The terminal shows `SUCCESS` when the build finishes:

   ![Successful build output](./img/zephyr-debugging-unit-testing-inspect-4.png)

2. Connect the board and upload with **Upload** in the same places, or
   <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>U</kbd>
   (<kbd>Cmd</kbd>+<kbd>Alt</kbd>+<kbd>U</kbd> on macOS):

   ![Ways to start an upload](./img/zephyr-debugging-unit-testing-inspect-5.png)

3. Open the serial monitor to see the log:

   ![Serial monitor with the Zephyr log](./img/zephyr-debugging-unit-testing-inspect-6.png)

4. A Bluetooth scanner app on your phone now shows the board as a beacon:

   ![The beacon in a Bluetooth scanner app](./img/zephyr-debugging-unit-testing-inspect-7.png)

## Debug the firmware {#debugging-the-firmware}

The nRF52-DK has an on-board debug probe, so
[debugging](../../../guides/debugging/index.md) works without configuration.

1. Start a debug session with **Run** > **Start Debugging**, or press
   <kbd>F5</kbd>:

   ![Starting a debug session](./img/zephyr-debugging-unit-testing-inspect-8.png)

2. Step through the code, set breakpoints, and add variables to **Watch**:

   ![Debugging with breakpoints and watched variables](./img/zephyr-debugging-unit-testing-inspect-9.png)

## Write unit tests {#writing-unit-tests}

You will create a small `calculator` library with `add`, `sub`, `mul` and
`div` functions and [test](../../../guides/unit-testing/index.md) it on the
board with the [Unity](../../../guides/unit-testing/frameworks/unity.md)
framework.

:::note

Unity calls `setUp()` before and `tearDown()` after each test. Use them to
prepare and clean up test data; they can be empty.

:::

1. Unity does not work with Zephyr's default minimal C library. Switch to
   newlib by adding this line to `zephyr/prj.conf`:

   ```text
   CONFIG_NEWLIB_LIBC=y
   ```

2. In the `lib` folder, create a `calculator` folder with two files.

   `lib/calculator/calculator.h`:

   ```c
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
   ```

   `lib/calculator/calculator.c`:

   ```c
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
   ```

3. Create `test/test_calc.c` with tests for the library. One expected value
   is wrong on purpose, so that you can see a failing test:

   ```c
   #include <calculator.h>
   #include <unity.h>

   void setUp(void)
   {
     // set stuff up here
   }

   void tearDown(void)
   {
     // clean stuff up here
   }

   void test_function_calculator_addition(void)
   {
     TEST_ASSERT_EQUAL(32, add(25, 7));
   }

   void test_function_calculator_subtraction(void)
   {
     TEST_ASSERT_EQUAL(20, sub(23, 3));
   }

   void test_function_calculator_multiplication(void)
   {
     TEST_ASSERT_EQUAL(50, mul(25, 2));
   }

   void test_function_calculator_division(void)
   {
     TEST_ASSERT_EQUAL(32, div(100, 3));
   }

   void main()
   {
     UNITY_BEGIN();

     RUN_TEST(test_function_calculator_addition);
     RUN_TEST(test_function_calculator_subtraction);
     RUN_TEST(test_function_calculator_multiplication);
     RUN_TEST(test_function_calculator_division);

     UNITY_END();
   }
   ```

4. Run the tests on the board with the **Test** button on the PlatformIO
   toolbar or **Test** in the **Project Tasks** panel.
   `test_function_calculator_division` fails, because integer division of
   100 by 3 gives 33:

   ![Test report with a failing test](./img/zephyr-debugging-unit-testing-inspect-10.png)

5. Change the expected value to `33` and run the tests again. All tests pass:

   ![Test report with all tests passing](./img/zephyr-debugging-unit-testing-inspect-11.png)

## Inspect the project {#project-inspection}

PlatformIO Home can show where the firmware uses memory and run
[static code analysis](../../../guides/static-code-analysis/index.md).

1. In PlatformIO Home, open **Inspect**, select the project, and select
   **Inspect**:

   ![Inspect screen in PlatformIO Home](./img/zephyr-debugging-unit-testing-inspect-12.png)

2. The **Statistics** tab summarizes memory use and code quality:

   ![Project statistics](./img/zephyr-debugging-unit-testing-inspect-13.png)

3. Sort the symbols by size to find the function with the largest memory
   footprint:

   ![Largest functions](./img/zephyr-debugging-unit-testing-inspect-14.png)

4. The **Defects** tab lists possible bugs found by static analysis:

   ![Code defects](./img/zephyr-debugging-unit-testing-inspect-15.png)

## Next steps {#conclusion}

You now have a working Zephyr project for the
[Nordic nRF52-DK](/hardware/boards/nordicnrf52/nrf52-dk) that you can use as
a starting point. To go further:

- [Zephyr framework](/hardware/frameworks/zephyr): project configuration,
  modules and devicetree overlays.
- [Nordic nRF52 platform](/hardware/platforms/nordicnrf52).
- [Static code analysis](../../../guides/static-code-analysis/index.md).
