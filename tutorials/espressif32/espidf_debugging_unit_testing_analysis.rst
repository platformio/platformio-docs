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

.. _tutorial_espressif32_espidf_debugging_unit_testing_analysis:

Get started with ESP-IDF and ESP32-DevKitC: debugging, unit testing, project analysis
=====================================================================================

The goal of this tutorial is to demonstrate how simple it is to use :ref:`ide_vscode`
to develop, run and debug a simple Wi-Fi project with the :ref:`framework_espidf`
framework for the ``ESP32-DevKitC`` board.

* **Level:** Intermediate
* **Platforms:** Windows, Mac OS X, Linux

**Requirements:**
    - Downloaded and installed :ref:`ide_vscode`
    - :ref:`board_espressif32_esp32dev`
    - An external debug adapter (e.g. :ref:`debugging_tool_olimex-arm-usb-ocd`)

.. contents:: Contents
    :local:

Setting Up the Project
----------------------

#. Click on "PlatformIO Home" button on the bottom PlatformIO Toolbar:

    .. image:: ../../_static/images/tutorials/espressif32/espidf-debugging-unit-testing-analysis-1.png

#. Click on "New Project", select ``Espressif ESP32 Dev Module`` as the development board,
   :ref:`framework_espidf` as the framework and a path to the project location
   (or use the default one):

    .. image:: ../../_static/images/tutorials/espressif32/espidf-debugging-unit-testing-analysis-2.png

Adding Code to the Generated Project
------------------------------------

#. Create a new file ``main.c`` in :ref:`projectconf_pio_src_dir` folder and add the
   following code:

    .. code-block:: c

      /* WiFi softAP Example

         This example code is in the Public Domain (or CC0 licensed, at your option.)

         Unless required by applicable law or agreed to in writing, this
         software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
         CONDITIONS OF ANY KIND, either express or implied.
      */
      #include <string.h>
      #include "freertos/FreeRTOS.h"
      #include "freertos/task.h"
      #include "esp_system.h"
      #include "esp_wifi.h"
      #include "esp_event.h"
      #include "esp_log.h"
      #include "nvs_flash.h"

      #include "lwip/err.h"
      #include "lwip/sys.h"

      #define EXAMPLE_ESP_WIFI_SSID      "mywifissid"
      #define EXAMPLE_ESP_WIFI_PASS      "mywifipass"
      #define EXAMPLE_MAX_STA_CONN       (3)

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

      void wifi_init_softap()
      {
          tcpip_adapter_init();
          ESP_ERROR_CHECK(esp_event_loop_create_default());

          wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
          ESP_ERROR_CHECK(esp_wifi_init(&cfg));

          ESP_ERROR_CHECK(esp_event_handler_register(WIFI_EVENT, ESP_EVENT_ANY_ID, &wifi_event_handler, NULL));

          wifi_config_t wifi_config = {
              .ap = {
                  .ssid = EXAMPLE_ESP_WIFI_SSID,
                  .ssid_len = strlen(EXAMPLE_ESP_WIFI_SSID),
                  .password = EXAMPLE_ESP_WIFI_PASS,
                  .max_connection = EXAMPLE_MAX_STA_CONN,
                  .authmode = WIFI_AUTH_WPA_WPA2_PSK
              },
          };
          if (strlen(EXAMPLE_ESP_WIFI_PASS) == 0) {
              wifi_config.ap.authmode = WIFI_AUTH_OPEN;
          }

          ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_AP));
          ESP_ERROR_CHECK(esp_wifi_set_config(ESP_IF_WIFI_AP, &wifi_config));
          ESP_ERROR_CHECK(esp_wifi_start());

          ESP_LOGI(TAG, "wifi_init_softap finished. SSID:%s password:%s",
                   EXAMPLE_ESP_WIFI_SSID, EXAMPLE_ESP_WIFI_PASS);
      }

      void app_main()
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

    .. warning::
        Make sure this new file ``main.c`` is registered as source file using
        ``idf_component_register`` function in ``src/CMakeLists.txt`` file:

        .. code-block:: cmake

          idf_component_register(SRCS "main.c")

#. To compile the project use one of the following options:

    - Build option from the ``Project Tasks`` menu
    - Build button in :ref:`ide_vscode_toolbar`
    - Task Menu ``Tasks: Run Task... > PlatformIO: Build`` or in :ref:`ide_vscode_toolbar`
    - Command Palette ``View: Command Palette > PlatformIO: Build``
    - Hotkeys ``cmd-alt-b / ctrl-alt-b``:


    .. image:: ../../_static/images/tutorials/espressif32/espidf-debugging-unit-testing-analysis-3.png

#. If everything went well, we should see a successful result message in the terminal
   window:

    .. image:: ../../_static/images/tutorials/espressif32/espidf-debugging-unit-testing-analysis-4.png

#. To upload the firmware to the board we can use the following options:

    - Upload option from the ``Project Tasks`` menu
    - Upload button in :ref:`ide_vscode_toolbar`
    - Command Palette ``View: Command Palette > PlatformIO: Upload``
    - Task Menu ``Tasks: Run Task... > PlatformIO: Upload``
    - Hotkeys ``cmd-alt-u / ctrl-alt-u``:

    .. image:: ../../_static/images/tutorials/espressif32/espidf-debugging-unit-testing-analysis-5.png

#. Connect the board to your computer and update the default monitor speed to
   ``115200`` in ``platformio.ini`` file:

    .. code-block:: ini

      [env:esp32dev]
      platform = espressif32
      board = esp32dev
      framework = espidf
      monitor_speed = 115200

#. Open Serial Monitor to observe the output from the board:

    .. image:: ../../_static/images/tutorials/espressif32/espidf-debugging-unit-testing-analysis-6.png

#. If everything went well, the board should be visible as a WiFi access point:

    .. image:: ../../_static/images/tutorials/espressif32/espidf-debugging-unit-testing-analysis-7.png

Debugging the Firmware
----------------------

Setting Up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

In order to use :ref:`piodebug`, we need to connect an external JTAG probe and the board
using the following pins:

.. list-table::
    :header-rows:  1

    * - ESP32 pin
      - JTAG probe pin

    * - ``3.3V``
      - ``Pin 1(VTref)``

    * - ``GPIO 9 (EN)``
      - ``Pin 3 (nTRST)``

    * - ``GND``
      - ``Pin 4 (GND)``

    * - ``GPIO 12 (TDI)``
      - ``Pin 5 (TDI)``

    * - ``GPIO 14 (TMS)``
      - ``Pin 7 (TMS)``

    * - ``GPIO 13 (TCK)``
      - ``Pin 9 (TCK)``

    * - ``GPIO 15 (TDO)``
      - ``Pin 13 (TDO)``

#. Specify :ref:`projectconf_debug_tool` in :ref:`projectconf`. In this tutorial,
   :ref:`debugging_tool_olimex-arm-usb-ocd-h` debug probe is used:

    .. code-block:: ini

        [env:esp32dev]
        platform = espressif32
        board = esp32dev
        framework = espidf
        monitor_speed = 115200
        debug_tool = olimex-arm-usb-ocd-h

#. To start the debug session we can use the following methods:

    * ``Debug: Start debugging`` in the top menu
    * ``Start Debugging`` option in the Quick Access menu
    * Hotkey button ``F5``:

    .. image:: ../../_static/images/tutorials/espressif32/espidf-debugging-unit-testing-analysis-8.png

#. Walk through the code using control buttons, set breakpoints, and add variables to the ``Watch window``:

    .. image:: ../../_static/images/tutorials/espressif32/espidf-debugging-unit-testing-analysis-9.png

Writing Unit Tests
------------------

.. note::
    Functions ``setUp`` and ``tearDown`` are used to initialize and finalize test
    conditions. Implementations of these functions are not required for running tests
    but if you need to initialize some variables before you run a test, you use the
    ``setUp`` function and if you need to clean up variables you use ``tearDown``
    function.

For the sake of simplicity, let's create a small library called ``calculator``,
implement several basic functions ``addition``, ``subtraction``, ``multiplication``,
``division`` and test them using :ref:`unit_testing` engine.

#. Create a new folder ``calculator`` in the :ref:`projectconf_pio_lib_dir` folder and
   add two new files ``calculator.h`` and ``calculator.c`` with the following contents:

    ``calculator.h``:

    .. code-block:: c

      #ifndef _CALCULATOR_H_
      #define _CALCULATOR_H_

      #ifdef __cplusplus
      extern "C" {
      #endif

      int addition (int a, int b);
      int subtraction (int a, int b);
      int multiplication (int a, int b);
      int division (int a, int b);

      #ifdef __cplusplus
      }
      #endif

      #endif // _CALCULATOR_H_


    ``calculator.c``:

    .. code-block:: c

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

#. Create a new file ``test_calc.c`` to the folder :ref:`projectconf_pio_test_dir`
   and add basic tests for the ``calculator`` library:

    .. code-block:: c

      #include <calculator.h>
      #include <unity.h>

      void test_function_calculator_addition(void) {
          TEST_ASSERT_EQUAL(32, addition(25, 7));
      }

      void test_function_calculator_subtraction(void) {
          TEST_ASSERT_EQUAL(20, subtraction(23, 3));
      }

      void test_function_calculator_multiplication(void) {
          TEST_ASSERT_EQUAL(50, multiplication(25, 2));
      }

      void test_function_calculator_division(void) {
          TEST_ASSERT_EQUAL(32, division(100, 3));
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

    .. image:: ../../_static/images/tutorials/espressif32/espidf-debugging-unit-testing-analysis-10.png

#. Let's fix the incorrect expected value and run tests again. After processing the
   results should be correct:

    .. image:: ../../_static/images/tutorials/espressif32/espidf-debugging-unit-testing-analysis-11.png

Project Inspection
------------------

For illustrative purposes, let's imagine we need to find a function with the biggest
memory footprint. Also, let's introduce a bug to our project so :ref:`piocheck` can
report it.

#. Open ``PlatformIO Home`` and navigate to ``Inspect`` section, select the current
   project and press ``Inspect`` button:

    .. image:: ../../_static/images/tutorials/espressif32/espidf-debugging-unit-testing-analysis-12.png

#. Project statistics:

    .. image:: ../../_static/images/tutorials/espressif32/espidf-debugging-unit-testing-analysis-13.png

#. The biggest function:

    .. image:: ../../_static/images/tutorials/espressif32/espidf-debugging-unit-testing-analysis-14.png

#. Possible bugs:

    .. image:: ../../_static/images/tutorials/espressif32/espidf-debugging-unit-testing-analysis-15.png

Conclusion
----------

Now we have a project template for the ``ESP32-DevKitC`` board that we can use as
boilerplate for later projects.
