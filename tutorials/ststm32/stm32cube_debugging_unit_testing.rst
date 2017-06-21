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

.. _stm32cube_debugging_unit_testing:

Developing STM32Cube HAL based project with debugging and unit testing in PlatformIO IDE
----------------------------------------------------------------------------------------

The goal of this tutorial is to demonstrate how simple it is to use :ref:`ide_atom` to develop, run and debug a basic blink project with :ref:`framework_stm32cube` framework for ``STM32 Nucleo-F401RE`` board.

* **Level:** Intermediate 
* **Platforms:** Windows, Mac OS X, Linux
 
**Requirements:**
    - Downloaded and installed :ref:`ide_atom`
    - `Nucleo-F401RE <http://www.st.com/en/evaluation-tools/nucleo-f401re.html>`_ development board


.. contents::

Setting Up the Project
~~~~~~~~~~~~~~~~~~~~~~

There are two ways how to create a new project in PlatformIO IDE: using "New Project" button menu on Home Page or 
using ``Menu: PlatformIO > Initialize or Update PlatformIO Project``:

.. image:: ../_static/tutorials/ststm32/stm32cube-debugging-unit-testing-1.png

On the next step we choose the desired board (in our case it’s ``ST Nucleo-F401RE``) and also select a directory for our project:

.. image:: ../_static/tutorials/ststm32/stm32cube-debugging-unit-testing-2.png

After processing the selected options (PlatformIO IDE will download and install all required packages, thus the first installation may take some amount of time), we should now have the new project created with the following folder structure:

.. image:: ../_static/tutorials/ststm32/stm32cube-debugging-unit-testing-3.png

The default framework used with ``ST Nucleo-F401RE`` board is :ref:`framework_mbed`, but since we decided to use :ref:`framework_stm32cube` we need to change the framework parameter in :ref:`projectconf` to the next one:

.. code-block:: ini

    [env:nucleo_f401re]
    platform = ststm32
    board = nucleo_f401re
    framework = stm32cube

After these steps, we have a fully configured project that is ready for developing code with :ref:`framework_stm32cube` framework.

Adding Code to the Generated Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's add some actual code to the project. Firstly, we create two main files ``main.c`` and ``main.h`` in the :ref:`projectconf_pio_src_dir` folder. Right click on the ``src`` in the project window:

.. image:: ../_static/tutorials/ststm32/stm32cube-debugging-unit-testing-4.png

Add next content to ``main.h``:

.. code-block:: cpp
 
    #ifndef MAIN_H
    #define MAIN_H
     
    #include "stm32f4xx_hal.h"
     
    #define LED_PIN                                GPIO_PIN_5
    #define LED_GPIO_PORT                          GPIOA
    #define LED_GPIO_CLK_ENABLE()                  __HAL_RCC_GPIOA_CLK_ENABLE()
     
    #endif // MAIN_H


Add this code to ``main.c``:

.. code-block:: cpp
 
    #include "main.h"
     
    void LED_Init();
     
    int main(void) {
      HAL_Init();
      LED_Init();
     
      while (1)
      {
        HAL_GPIO_TogglePin(LED_GPIO_PORT, LED_PIN);
        HAL_Delay(1000);
      }
    }
     
    void LED_Init() {
      LED_GPIO_CLK_ENABLE();
      GPIO_InitTypeDef GPIO_InitStruct;
      GPIO_InitStruct.Pin = LED_PIN;
      GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
      GPIO_InitStruct.Pull = GPIO_PULLUP;
      GPIO_InitStruct.Speed = GPIO_SPEED_HIGH;
      HAL_GPIO_Init(LED_GPIO_PORT, &GPIO_InitStruct);
    }
     
    void SysTick_Handler(void) {
      HAL_IncTick();
    }


After this step, we created a basic blink project that is ready for compiling and uploading.

Compiling and Uploading the Firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we can build the project. To compile firmware we can use three options: 
Using Build button on :ref:`atom_ide_platformio_toolbar`, using ``Menu: PlatformIO > Build`` option from top menu, using targets list in bottom left corner or via hotkeys ``cmd-alt-b / ctrl-alt-b / f9``:

.. image:: ../_static/tutorials/ststm32/stm32cube-debugging-unit-testing-5.png

If everything went well, we should see successful result in the terminal window:

.. image:: ../_static/tutorials/ststm32/stm32cube-debugging-unit-testing-6.png

Now we can upload firmware to the board:
Using Build button on :ref:`atom_ide_platformio_toolbar`, using ``Menu: PlatformIO > Upload`` from top menu, using targets list in bottom left corner or via hotkeys ``cmd-alt-u / ctrl-alt-u``

.. image:: ../_static/tutorials/ststm32/stm32cube-debugging-unit-testing-7.png

After successful uploading, the green LED2 should start blinking.

Debugging the Firmware
~~~~~~~~~~~~~~~~~~~~~~

:ref:`piodebug` offers the easiest way to debug your board. Just click Debug button on :ref:`atom_ide_platformio_toolbar` or use ``Menu: PlatformIO > Debug > Start new debug session``: 

.. image:: ../_static/tutorials/ststm32/stm32cube-debugging-unit-testing-8.png

We need to wait some time while PlatformIO is initializing debug session and when the first line after the main function is highlighted we are ready to debug:

.. image:: ../_static/tutorials/ststm32/stm32cube-debugging-unit-testing-9.png

We can walk through the code using control buttons, set breakpoints, add variables to ``Watch window``:

.. image:: ../_static/tutorials/ststm32/stm32cube-debugging-unit-testing-10.png

Writing Unit Tests
~~~~~~~~~~~~~~~~~~

Now let’s write some tests using :ref:`unit_testing` feature that can help us test code directly on the target board. :ref:`unit_testing` engine by default supports only three frameworks: :ref:`framework_arduino`, :ref:`framework_energia` and :ref:`framework_mbed`. Since we decided to use :ref:`framework_stm32cube` we need to implement a custom :ref:`projectconf_test_transport` to print testing results and specify that condition in :ref:`projectconf`:

.. code-block:: ini

  [env:nucleo_f401re]
  platform = ststm32
  board = nucleo_f401re
  framework = stm32cube
  test_transport = custom

.. image:: ../_static/tutorials/ststm32/stm32cube-debugging-unit-testing-11.png

We will use ``USART2`` on ``ST Nucleo-F401RE`` board because it's directly connected to the STLink debug interface and in OS it can be visible as a Virtual Com Port, so we don't need any additional USB-UART converter. To implement the custom :ref:`projectconf_test_transport` we need to create two files ``unittest_transport.h`` and ``unittest_transport.c`` and put them in the :ref:`projectconf_pio_test_dir` in the root folder of our project. In these files we need to implement next four functions:

.. code-block:: cpp
 
    void unittest_uart_begin();
    void unittest_uart_putchar(char c);
    void unittest_uart_flush();
    void unittest_uart_end();

Implementation of unittest_transport.h:

.. code-block:: cpp

    #ifndef UNITEST_TRANSPORT_H
    #define UNITEST_TRANSPORT_H
     
    #ifdef __cplusplus
    extern "C" {
    #endif
     
    void unittest_uart_begin();
    void unittest_uart_putchar(char c);
    void unittest_uart_flush();
    void unittest_uart_end();
     
    #ifdef __cplusplus
    }
    #endif
     
    #endif // UNITEST_TRANSPORT_H
 
Implementation of unittest_transport.c:

.. code-block:: cpp

    #include "unittest_transport.h"
    #include "stm32f4xx_hal.h"
     
    #define USARTx                           USART2
    #define USARTx_CLK_ENABLE()              __HAL_RCC_USART2_CLK_ENABLE()
    #define USARTx_CLK_DISABLE()             __HAL_RCC_USART2_CLK_DISABLE()
    #define USARTx_RX_GPIO_CLK_ENABLE()      __HAL_RCC_GPIOA_CLK_ENABLE()
    #define USARTx_TX_GPIO_CLK_ENABLE()      __HAL_RCC_GPIOA_CLK_ENABLE()
    #define USARTx_RX_GPIO_CLK_DISABLE()     __HAL_RCC_GPIOA_CLK_DISABLE()
    #define USARTx_TX_GPIO_CLK_DISABLE()     __HAL_RCC_GPIOA_CLK_DISABLE()
     
    #define USARTx_FORCE_RESET()             __HAL_RCC_USART2_FORCE_RESET()
    #define USARTx_RELEASE_RESET()           __HAL_RCC_USART2_RELEASE_RESET()
     
    #define USARTx_TX_PIN                    GPIO_PIN_2
    #define USARTx_TX_GPIO_PORT              GPIOA
    #define USARTx_TX_AF                     GPIO_AF7_USART2
    #define USARTx_RX_PIN                    GPIO_PIN_3
    #define USARTx_RX_GPIO_PORT              GPIOA
    #define USARTx_RX_AF                     GPIO_AF7_USART2
     
    static UART_HandleTypeDef UartHandle;
     
    void unittest_uart_begin()
    {
       GPIO_InitTypeDef  GPIO_InitStruct;
     
      USARTx_TX_GPIO_CLK_ENABLE();
      USARTx_RX_GPIO_CLK_ENABLE();
     
      USARTx_CLK_ENABLE();
     
      GPIO_InitStruct.Pin       = USARTx_TX_PIN;
      GPIO_InitStruct.Mode      = GPIO_MODE_AF_PP;
      GPIO_InitStruct.Pull      = GPIO_PULLUP;
      GPIO_InitStruct.Speed     = GPIO_SPEED_FAST;
      GPIO_InitStruct.Alternate = USARTx_TX_AF;
     
      HAL_GPIO_Init(USARTx_TX_GPIO_PORT, &GPIO_InitStruct);
     
      GPIO_InitStruct.Pin = USARTx_RX_PIN;
      GPIO_InitStruct.Alternate = USARTx_RX_AF;
     
      HAL_GPIO_Init(USARTx_RX_GPIO_PORT, &GPIO_InitStruct);
      UartHandle.Instance          = USARTx;
     
      UartHandle.Init.BaudRate     = 9600;
      UartHandle.Init.WordLength   = UART_WORDLENGTH_8B;
      UartHandle.Init.StopBits     = UART_STOPBITS_1;
      UartHandle.Init.Parity       = UART_PARITY_NONE;
      UartHandle.Init.HwFlowCtl    = UART_HWCONTROL_NONE;
      UartHandle.Init.Mode         = UART_MODE_TX_RX;
      UartHandle.Init.OverSampling = UART_OVERSAMPLING_16;
     
      if(HAL_UART_Init(&UartHandle) != HAL_OK) {
        while(1){}
      }
     
    }
     
    void unittest_uart_putchar(char c)
    {
        HAL_UART_Transmit(&UartHandle, (uint8_t*)(&c), 1, 1000);
    }
     
    void unittest_uart_flush(){}
     
    void unittest_uart_end() {
      USARTx_CLK_DISABLE();
      USARTx_RX_GPIO_CLK_DISABLE();
      USARTx_TX_GPIO_CLK_DISABLE();
    }

Now we need to add some test cases. Tests can be added to a single C file that may include multiple tests. First of all, in this file we need to add three default functions: ``setUp``, ``tearDown`` and ``main``. ``setUp`` and ``tearDown`` are used to initialize and finalize test conditions. Implementations of these functions are not required for running tests but if you need to initialize some variables before you run a test, you use the ``setUp`` function and if you need to clean up variables you use ``tearDown`` function. In our example we will use these functions to accordingly initialize and deinitialize LED.  ``main`` function acts as a simple program where we describe our test plan.

Let’s implement some basic tests for blinking routine:
 
.. code-block:: cpp

    #include <main.h>
    #include <unity.h>
     
    #ifdef UNIT_TEST
     
    void setUp(void) {
        HAL_Init();
      
        LED_GPIO_CLK_ENABLE();
      
        GPIO_InitTypeDef GPIO_InitStruct;
        GPIO_InitStruct.Pin = LED_PIN;
        GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
        GPIO_InitStruct.Pull = GPIO_PULLUP;
        GPIO_InitStruct.Speed = GPIO_SPEED_HIGH;
        HAL_GPIO_Init(LED_GPIO_PORT, &GPIO_InitStruct); 
    }
     
    void tearDown(void) {
        HAL_GPIO_DeInit(LED_GPIO_PORT, LED_PIN);
    }
     
    void test_led_builtin_pin_number(void) {
        TEST_ASSERT_EQUAL(LED_PIN, GPIO_PIN_5);
    }
     
    void test_led_state_high(void) {
        HAL_GPIO_WritePin(LED_GPIO_PORT, LED_PIN, GPIO_PIN_SET);
        TEST_ASSERT_EQUAL(HAL_GPIO_ReadPin(LED_GPIO_PORT, LED_PIN), GPIO_PIN_SET);
    }
     
    void test_led_state_low(void) {
        HAL_GPIO_WritePin(LED_GPIO_PORT, LED_PIN, GPIO_PIN_RESET);
        TEST_ASSERT_EQUAL(HAL_GPIO_ReadPin(LED_GPIO_PORT, LED_PIN), GPIO_PIN_RESET);
    }
     
    int main() {
        UNITY_BEGIN();
        RUN_TEST(test_led_builtin_pin_number);
        
        for (unsigned int i = 0; i < 5; i++)
        {
            RUN_TEST(test_led_state_high);
            HAL_Delay(500);
            RUN_TEST(test_led_state_low);
            HAL_Delay(500);
        }
        
        UNITY_END(); // stop unit testing
        
        while(1){}
    }
     
    #endif

Also, we need to wrap the main function in our application:

.. code-block:: cpp

    #ifndef UNIT_TEST
    int main(void)
    #else
    int app_main(void)
    #endif
    {
      HAL_Init();
      LED_Init();

      while (1)
      {
        HAL_GPIO_TogglePin(LED_GPIO_PORT, LED_PIN);
        HAL_Delay(1000);
      }
    }


Now we are ready to upload tests to the board. To do this we can use ``Menu: PlatformIO > Test (Unit Testing)`` from top menu or targets list in bottom left corner:

.. image:: ../_static/tutorials/ststm32/stm32cube-debugging-unit-testing-12.png

After processing we should see a detailed report about testing results:

.. image:: ../_static/tutorials/ststm32/stm32cube-debugging-unit-testing-13.png

Congratulations! As we can see from the report, all our tests went successfully!

Conclusion
~~~~~~~~~~

Now we have a decent template that we can improve for our next more complex projects.