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

.. _tutorial_arduino_debugging_unit_testing:

Get started with Arduino and Nordic nRF52-DK: debugging and unit testing
============================================================================

The goal of this tutorial is to demonstrate how simple it is to use :ref:`ide_vscode` to develop, run and debug a simple project with :ref:`framework_arduino` framework for ``Nordic nRF52-DK`` board.

* **Level:** Beginner
* **Platforms:** Windows, Mac OS X, Linux

**Requirements:**
    - Downloaded and installed :ref:`ide_vscode`
    - `Nordic nRF52-DK <https://www.nordicsemi.com/eng/Products/Bluetooth-low-energy/nRF52-DK>`_ development board


.. contents:: Contents
    :local:

Setting Up the Project
----------------------

At first step, we need to create a new project using PlatformIO Home Page (to open this page just press Home icon on the toolbar):

.. image:: ../../_static/tutorials/nordicnrf52/arduino-debugging-unit-testing-1.png

On the next step we need to select ``Nordic nRF52-DK`` as a development board, :ref:`framework_arduino` as a framework and a path to the project location (or use the default one):

.. image:: ../../_static/tutorials/nordicnrf52/arduino-debugging-unit-testing-2.png

Processing the selected project may take some amount of time (PlatformIO will download and install all required packages)
and after these steps, we have a fully configured project that is ready for developing code with :ref:`framework_arduino` framework.

Adding Code to the Generated Project
------------------------------------

Let's add some actual code to the project. Firstly, we open a default main file named ``main.cpp`` in the :ref:`projectconf_pio_src_dir` folder and replace its content with next one:

.. code-block:: cpp

    #include <Arduino.h>

    void setup()
    {
        pinMode(LED_BUILTIN, OUTPUT);
    }

    void loop()
    {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(100);
        digitalWrite(LED_BUILTIN, LOW);
        delay(100);
    }

.. image:: ../../_static/tutorials/nordicnrf52/arduino-debugging-unit-testing-3.png

After this step, we created a basic blink project ready for compiling and uploading.

Compiling and Uploading the Firmware
------------------------------------

Now we can build the project. To compile firmware we can use three options:
Using Build button on :ref:`ide_vscode_toolbar`, using Command Palette ``View: Command Palette > PlatformIO: Build``, using Task Menu ``Tasks: Run Task... > PlatformIO: Build`` or via hotkeys ``cmd-alt-b / ctrl-alt-b``:

.. image:: ../../_static/tutorials/nordicnrf52/arduino-debugging-unit-testing-4.png

If everything went well, we should see a successful result message in the terminal window:

.. image:: ../../_static/tutorials/nordicnrf52/arduino-debugging-unit-testing-5.png

Now we can upload firmware to the board:
Using Upload button on :ref:`ide_vscode_toolbar`, using Command Palette ``View: Command Palette > PlatformIO: Upload``, using Task Menu ``Tasks: Run Task... > PlatformIO: Upload`` or via hotkeys ``cmd-alt-u / ctrl-alt-u``:

.. image:: ../../_static/tutorials/nordicnrf52/arduino-debugging-unit-testing-6.png

After successful uploading, the green LED1 should start blinking.

Debugging the Firmware
----------------------

:ref:`piodebug` offers the easiest way to debug your board. Just navigate to the top menu and select ``Debug: Start debugging`` or use hotkey button ``F5``:

.. image:: ../../_static/tutorials/nordicnrf52/arduino-debugging-unit-testing-7.png

We need to wait some time while PlatformIO is initializing debug session and when the first line after the main function is highlighted we are ready to debug:

.. image:: ../../_static/tutorials/nordicnrf52/arduino-debugging-unit-testing-8.png

We can walk through the code using control buttons, set breakpoints, add variables to ``Watch window``:

.. image:: ../../_static/tutorials/nordicnrf52/arduino-debugging-unit-testing-9.png

Writing Unit Tests
------------------

Test cases can be added to a single file that may include multiple tests. First of all, in this file, we need to add three default functions: ``setUp``, ``tearDown``, ``setup`` and ``loop``. ``setUp`` and ``tearDown`` are used to initialize and finalize test conditions. Implementations of these functions are not required for running tests but if you need to initialize some variables before you run a test, you use the ``setUp`` function and if you need to clean up variables you use ``tearDown`` function. In our example we will use these functions to accordingly initialize and deinitialize LED.  ``setup`` and ``loop`` functions act as a simple Arduino program where we describe our test plan.

Let’s implement some basic tests for blinking routine:

.. code-block:: cpp

    #include <Arduino.h>
    #include <unity.h>

    #ifdef UNIT_TEST

    // void setUp(void) {
    // // set stuff up here
    // }

    // void tearDown(void) {
    // // clean stuff up here
    // }

    void test_led_builtin_pin_number(void)
    {
        TEST_ASSERT_EQUAL(LED_BUILTIN, 13);
    }

    void test_led_state_high(void)
    {
        digitalWrite(LED_BUILTIN, HIGH);
        TEST_ASSERT_EQUAL(digitalRead(LED_BUILTIN), LOW);
    }

    void test_led_state_low(void)
    {
        digitalWrite(LED_BUILTIN, LOW);
        TEST_ASSERT_EQUAL(digitalRead(LED_BUILTIN), LOW);
    }

    void setup()
    {
        UNITY_BEGIN();
        RUN_TEST(test_led_builtin_pin_number);
        pinMode(LED_BUILTIN, OUTPUT);

        for (uint8_t i = 0; i < 5; i++)
        {
            RUN_TEST(test_led_state_high);
            delay(200);
            RUN_TEST(test_led_state_low);
            delay(200);
        }

        UNITY_END(); // stop unit testing
    }

    void loop()
    {
    }

    #endif


Also, we need to wrap the main file using ``UNIT_TEST`` define:

.. code-block:: cpp

    #include <Arduino.h>

    #ifndef UNIT_TEST // <<

    void setup()
    {
        pinMode(LED_BUILTIN, OUTPUT);
    }

    void loop()
    {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(100);
        digitalWrite(LED_BUILTIN, LOW);
        delay(100);
    }

    #endif // <<


Now we are ready to upload tests to the board. To do this we can use ``Tasks: Run Task... > PlatformIO Test`` from top menu:

.. image:: ../../_static/tutorials/nordicnrf52/arduino-debugging-unit-testing-10.png

After processing we should see a detailed report about testing results:

.. image:: ../../_static/tutorials/nordicnrf52/arduino-debugging-unit-testing-11.png

As we can see from the report, all our tests were successful!

Adding Bluetooth LE features
----------------------------

To add the basic BLE functionality to our project we need to define the SoftDevice version
and install a library called `BLEPeripheral <https://platformio.org/lib/show/259/BLEPeripheral>`_.
Both these modifications can be specified in :ref:`projectconf`:


.. code-block:: ini

    [env:nrf52_dk]
    platform = nordicnrf52
    board = nrf52_dk
    framework = arduino
    ; SoftDevice version
    build_flags = -DNRF52_S132
    lib_deps =
      BLEPeripheral

Now let's create a basic application that can interact with other BLE devices (e.g phone)
For example, next code declares a BLE characteristic that controls the state of the LED1

.. code-block:: cpp

    #include <Arduino.h>
    #include <SPI.h>
    #include <BLEPeripheral.h>

    #ifndef UNIT_TEST

    BLEPeripheral ledPeripheral = BLEPeripheral();

    BLEService ledService = BLEService("19b10000e8f2537e4f6cd104768a1214");
    BLECharCharacteristic ledCharacteristic = BLECharCharacteristic("19b10001e8f2537e4f6cd104768a1214", BLERead | BLEWrite);

    void setup()
    {
      pinMode(LED_BUILTIN, OUTPUT);

      ledPeripheral.setAdvertisedServiceUuid(ledService.uuid());
      ledPeripheral.addAttribute(ledService);
      ledPeripheral.addAttribute(ledCharacteristic);
      ledPeripheral.setLocalName("Nordic NRF52 DK");
      ledPeripheral.begin();
    }

    void loop()
    {
      BLECentral central = ledPeripheral.central();

      if (central) {
        while (central.connected()) {
          if (ledCharacteristic.written()) {
            if (ledCharacteristic.value()) {
              digitalWrite(LED_BUILTIN, HIGH);
            }
            else{
              digitalWrite(LED_BUILTIN, LOW);
            }
          }
        }
      }
    }

    #endif

Now we can compile and upload this program to the board as described in previous sections.
To verify that our application works as expected, we can use any Android smartphone with BLE feature and
`Nordic nRF Connect tool <https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp&hl=en>`_.

At first, we need to scan all advertising BLE devices and connect to the device called ``Nordic NRF52 DK``.
After a successful connection to the board, we should see one "Unknown Service" with one "Unknown Characteristic" fields:

.. image:: ../../_static/tutorials/nordicnrf52/arduino-debugging-unit-testing-12.png

To switch the LED on or off we just need write ``0`` or ``1`` as ``UINT8`` to the BLE characteristic:

.. image:: ../../_static/tutorials/nordicnrf52/arduino-debugging-unit-testing-13.png

Conclusion
----------

Now we have a project template for Nordic ``nRF52-DK`` board that we can use as a boilerplate for the next projects.
