<a id="tutorial-espressif32-espidf-debugging-unit-testing-analysis"></a>

# Get started with ESP-IDF and ESP32-DevKitC: debugging, unit testing, project analysis {#get-started-with-esp-idf-and-esp32-devkitc-debugging-unit-testing-project-analysis}

The goal of this tutorial is to demonstrate how simple it is to use [PlatformIO IDE for VSCode](../../../guides/ide/vscode.md) to develop, run and debug a simple Wi-Fi project with the [Espressif IoT Development Framework](/hardware/frameworks/espidf) framework for the `ESP32-DevKitC` board.

- **Level:** Intermediate
- **Platforms:** Windows, Mac OS X, Linux

**Requirements:**

- Downloaded and installed [PlatformIO IDE for VSCode](../../../guides/ide/vscode.md)
- [Espressif ESP32 Dev Module](/hardware/boards/espressif32/esp32dev)
- An external debug adapter (e.g. [Olimex ARM-USB-OCD](../../../hardware/debug-probes/olimex-arm-usb-ocd.md))

## Setting Up the Project {#setting-up-the-project}

1. Click on "PlatformIO Home" button on the bottom PlatformIO Toolbar:

   ![](./img/espidf-debugging-unit-testing-analysis-1.png)

2. Click on "New Project", select `Espressif ESP32 Dev Module` as the development board, [Espressif IoT Development Framework](/hardware/frameworks/espidf) as the framework and a path to the project location (or use the default one):

   ![](./img/espidf-debugging-unit-testing-analysis-2.png)

## Adding Code to the Generated Project {#adding-code-to-the-generated-project}

1. Create a new file `main.c` in [src_dir](../../../reference/platformio-ini/platformio/src-dir.md) folder and add the following code:

   ```c
   /*  WiFi softAP Example

      This example code is in the Public Domain (or CC0 licensed, at your option.)

      Unless required by applicable law or agreed to in writing, this
      software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
      CONDITIONS OF ANY KIND, either express or implied.
   */
   #include <string.h>
   #include "freertos/FreeRTOS.h"
   #include "freertos/task.h"
   #include "esp_mac.h"
   #include "esp_wifi.h"
   #include "esp_event.h"
   #include "esp_log.h"
   #include "nvs_flash.h"

   #include "lwip/err.h"
   #include "lwip/sys.h"

   /* The examples use WiFi configuration that you can set via project configuration menu.

      If you'd rather not, just change the below entries to strings with
      the config you want - ie #define EXAMPLE_WIFI_SSID "mywifissid"
   */
   #define EXAMPLE_ESP_WIFI_SSID      "mywifissid"
   #define EXAMPLE_ESP_WIFI_PASS      "mywifipass"
   #define EXAMPLE_ESP_WIFI_CHANNEL   1
   #define EXAMPLE_MAX_STA_CONN       4

   static const char *TAG = "wifi softAP";

   static void wifi_event_handler(void* arg, esp_event_base_t event_base,
                                       int32_t event_id, void* event_data)
   {
       if (event_id == WIFI_EVENT_AP_STACONNECTED) {
           wifi_event_ap_staconnected_t* event = (wifi_event_ap_staconnected_t*) event_data;
           ESP_LOGI(TAG, "station "MACSTR" join, AID=%d",
                    MAC2STR(event->mac), event->aid);
       } else if (event_id == WIFI_EVENT_AP_STADISCONNECTED) {
           wifi_event_ap_stadisconnected_t* event = (wifi_event_ap_stadisconnected_t*) event_data;
           ESP_LOGI(TAG, "station "MACSTR" leave, AID=%d",
                    MAC2STR(event->mac), event->aid);
       }
   }

   void wifi_init_softap(void)
   {
       ESP_ERROR_CHECK(esp_netif_init());
       ESP_ERROR_CHECK(esp_event_loop_create_default());
       esp_netif_create_default_wifi_ap();

       wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
       ESP_ERROR_CHECK(esp_wifi_init(&cfg));

       ESP_ERROR_CHECK(esp_event_handler_instance_register(WIFI_EVENT,
                                                           ESP_EVENT_ANY_ID,
                                                           &wifi_event_handler,
                                                           NULL,
                                                           NULL));

       wifi_config_t wifi_config = {
           .ap = {
               .ssid = EXAMPLE_ESP_WIFI_SSID,
               .ssid_len = strlen(EXAMPLE_ESP_WIFI_SSID),
               .channel = EXAMPLE_ESP_WIFI_CHANNEL,
               .password = EXAMPLE_ESP_WIFI_PASS,
               .max_connection = EXAMPLE_MAX_STA_CONN,
               .authmode = WIFI_AUTH_WPA_WPA2_PSK,
               .pmf_cfg = {
                       .required = false,
               },
           },
       };
       if (strlen(EXAMPLE_ESP_WIFI_PASS) == 0) {
           wifi_config.ap.authmode = WIFI_AUTH_OPEN;
       }

       ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_AP));
       ESP_ERROR_CHECK(esp_wifi_set_config(WIFI_IF_AP, &wifi_config));
       ESP_ERROR_CHECK(esp_wifi_start());

       ESP_LOGI(TAG, "wifi_init_softap finished. SSID:%s password:%s channel:%d",
                EXAMPLE_ESP_WIFI_SSID, EXAMPLE_ESP_WIFI_PASS, EXAMPLE_ESP_WIFI_CHANNEL);
   }

   void app_main(void)
   {
       //Initialize NVS
       esp_err_t ret = nvs_flash_init();
       if (ret == ESP_ERR_NVS_NO_FREE_PAGES || ret == ESP_ERR_NVS_NEW_VERSION_FOUND) {
         ESP_ERROR_CHECK(nvs_flash_erase());
         ret = nvs_flash_init();
       }
       ESP_ERROR_CHECK(ret);

       ESP_LOGI(TAG, "ESP_WIFI_MODE_AP");
       wifi_init_softap();
   }
   ```

   :::warning

   Make sure this new file `main.c` is registered as source file using `idf_component_register` function in `src/CMakeLists.txt` file:

   ```cmake
   idf_component_register(SRCS "main.c")
   ```

   :::

2. To compile the project use one of the following options:

   - Build option from the `Project Tasks` menu
   - Build button in [PlatformIO Toolbar](../../../guides/ide/vscode.md#ide-vscode-toolbar)
   - Task Menu `Tasks: Run Task... > PlatformIO: Build` or in [PlatformIO Toolbar](../../../guides/ide/vscode.md#ide-vscode-toolbar)
   - Command Palette `View: Command Palette > PlatformIO: Build`
   - Hotkeys `cmd-alt-b / ctrl-alt-b`:

   ![](./img/espidf-debugging-unit-testing-analysis-3.png)

3. If everything went well, we should see a successful result message in the terminal window:

   ![](./img/espidf-debugging-unit-testing-analysis-4.png)

4. To upload the firmware to the board we can use the following options:

   - Upload option from the `Project Tasks` menu
   - Upload button in [PlatformIO Toolbar](../../../guides/ide/vscode.md#ide-vscode-toolbar)
   - Command Palette `View: Command Palette > PlatformIO: Upload`
   - Task Menu `Tasks: Run Task... > PlatformIO: Upload`
   - Hotkeys `cmd-alt-u / ctrl-alt-u`:

   ![](./img/espidf-debugging-unit-testing-analysis-5.png)

5. Connect the board to your computer and update the default monitor speed to `115200` in `platformio.ini` file:

   ```ini
   [env:esp32dev]
   platform = espressif32
   board = esp32dev
   framework = espidf
   monitor_speed = 115200
   ```

6. Open Serial Monitor to observe the output from the board:

   ![](./img/espidf-debugging-unit-testing-analysis-6.png)

7. If everything went well, the board should be visible as a WiFi access point:

   ![](./img/espidf-debugging-unit-testing-analysis-7.png)

## Debugging the Firmware {#debugging-the-firmware}

### Setting Up the Hardware {#setting-up-the-hardware}

In order to use [Debugging](../../../guides/debugging/index.md), we need to connect an external JTAG probe and the board using the following pins:

| ESP32 pin | JTAG probe pin |
|---|---|
| `3.3V` | `Pin 1(VTref)` |
| `GPIO 9 (EN)` | `Pin 3 (nTRST)` |
| `GND` | `Pin 4 (GND)` |
| `GPIO 12 (TDI)` | `Pin 5 (TDI)` |
| `GPIO 14 (TMS)` | `Pin 7 (TMS)` |
| `GPIO 13 (TCK)` | `Pin 9 (TCK)` |
| `GPIO 15 (TDO)` | `Pin 13 (TDO)` |

1. Specify [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md). In this tutorial, [Olimex ARM-USB-OCD-H](../../../hardware/debug-probes/olimex-arm-usb-ocd-h.md) debug probe is used:

   ```ini
   [env:esp32dev]
   platform = espressif32
   board = esp32dev
   framework = espidf
   monitor_speed = 115200
   debug_tool = olimex-arm-usb-ocd-h
   ```

2. To start the debug session we can use the following methods:

   - `Debug: Start debugging` in the top menu
   - `Start Debugging` option in the Quick Access menu
   - Hotkey button `F5`:

   ![](./img/espidf-debugging-unit-testing-analysis-8.png)

3. Walk through the code using control buttons, set breakpoints, and add variables to the `Watch window`:

   ![](./img/espidf-debugging-unit-testing-analysis-9.png)

## Writing Unit Tests {#writing-unit-tests}

:::note

Functions `setUp` and `tearDown` are used to initialize and finalize test conditions. Implementations of these functions are not required for running tests but if you need to initialize some variables before you run a test, you use the `setUp` function and if you need to clean up variables you use `tearDown` function.

:::

For the sake of simplicity, let's create a small library called `calculator`, implement several basic functions `addition`, `subtraction`, `multiplication`, `division` and test them using PlatformIO [Unit Testing](../../../guides/unit-testing/index.md) solution.

1. Create a new folder `calculator` in the [lib_dir](../../../reference/platformio-ini/platformio/lib-dir.md) folder and add two new files `calculator.h` and `calculator.c` with the following contents:

   `calculator.h`:

   ```c
   #ifndef _CALCULATOR_H_
   #define _CALCULATOR_H_

   #ifdef __cplusplus
   extern "C"
   {
   #endif

     int addition(int a, int b);
     int subtraction(int a, int b);
     int multiplication(int a, int b);
     int division(int a, int b);

   #ifdef __cplusplus
   }
   #endif

   #endif // _CALCULATOR_H_
   ```

   `calculator.c`:

   ```c
   #include "calculator.h"

   int addition(int a, int b)
   {
     return a + b;
   }

   int subtraction(int a, int b)
   {
     return a - b;
   }

   int multiplication(int a, int b)
   {
     return a * b;
   }

   int division(int a, int b)
   {
     return a / b;
   }
   ```

2. Create a new file `test_calc.c` to the folder [test_dir](../../../reference/platformio-ini/platformio/test-dir.md) and add basic tests for the `calculator` library:

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
     TEST_ASSERT_EQUAL(32, addition(25, 7));
   }

   void test_function_calculator_subtraction(void)
   {
     TEST_ASSERT_EQUAL(20, subtraction(23, 3));
   }

   void test_function_calculator_multiplication(void)
   {
     TEST_ASSERT_EQUAL(50, multiplication(25, 2));
   }

   void test_function_calculator_division(void)
   {
     TEST_ASSERT_EQUAL(32, division(100, 3));
   }

   void app_main()
   {
     UNITY_BEGIN();

     RUN_TEST(test_function_calculator_addition);
     RUN_TEST(test_function_calculator_subtraction);
     RUN_TEST(test_function_calculator_multiplication);
     RUN_TEST(test_function_calculator_division);

     UNITY_END();
   }
   ```

3. Let's run tests on the board and check the results. There should be a problem with `test_function_calculator_division` test:

   ![](./img/espidf-debugging-unit-testing-analysis-10.png)

4. Let's fix the incorrect expected value and run tests again. After processing the results should be correct:

   ![](./img/espidf-debugging-unit-testing-analysis-11.png)

## Project Inspection {#project-inspection}

For illustrative purposes, let's imagine we need to find a function with the biggest memory footprint. Also, let's introduce a bug to our project so [Static Code Analysis](../../../guides/static-code-analysis/index.md) can report it.

1. Open `PlatformIO Home` and navigate to `Inspect` section, select the current project and press `Inspect` button:

   ![](./img/espidf-debugging-unit-testing-analysis-12.png)

2. Project statistics:

   ![](./img/espidf-debugging-unit-testing-analysis-13.png)

3. The biggest function:

   ![](./img/espidf-debugging-unit-testing-analysis-14.png)

4. Possible bugs:

   ![](./img/espidf-debugging-unit-testing-analysis-15.png)

## Conclusion {#conclusion}

Now we have a project template for the `ESP32-DevKitC` board that we can use as boilerplate for later projects.
