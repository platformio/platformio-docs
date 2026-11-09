---
sidebar_label: "STM32Cube on Nucleo-F401RE"
description: Build, upload, debug and unit test an STM32Cube HAL blink project on the ST Nucleo-F401RE with PlatformIO IDE for VS Code.
---

<a id="tutorial-stm32cube-debugging-unit-testing"></a>

# STM32Cube HAL on Nucleo-F401RE: debugging and unit testing {#stm32cube-hal-and-nucleo-f401re-debugging-and-unit-testing}

In this tutorial you use [PlatformIO IDE for VS Code](../../../guides/ide/vscode.md)
to write a blink program with the [STM32Cube](/hardware/frameworks/stm32cube)
HAL for the ST Nucleo-F401RE board, debug it with the on-board ST-LINK probe,
and run unit tests on the board.

- **Level:** intermediate
- **Host:** Windows, macOS or Linux

## What you need {#what-you-need}

- [PlatformIO IDE for VS Code](../../../guides/ide/vscode.md), installed.
- An [ST Nucleo-F401RE](/hardware/boards/ststm32/nucleo-f401re) board. Its
  on-board ST-LINK is used for uploading, debugging and the serial port, so
  you need no other hardware.
- The [ST-LINK drivers](../../../hardware/debug-probes/stlink.md), if your
  operating system needs them.

## Create the project {#setting-up-the-project}

1. Open [PlatformIO Home](../../platformio-home.md) with the **Home** button on
   the PlatformIO toolbar, and select **New Project**:

   ![PlatformIO Home with the New Project button](./img/stm32cube-debugging-unit-testing-1.png)

2. Select **ST Nucleo-F401RE** as the board and **STM32Cube** as the
   framework. Keep or change the location, and select **Finish**:

   ![Project wizard with the Nucleo-F401RE board and STM32Cube framework](./img/stm32cube-debugging-unit-testing-2.png)

PlatformIO creates the project and installs the toolchain and framework. The
first time, this can take a few minutes.

## Add the code {#adding-code-to-the-generated-project}

In the [`src_dir`](../../../reference/platformio-ini/platformio/src-dir.md)
folder, create two files, `main.h` and `main.c`. To create a file, right-click
`src` in the **Explorer** and select **New File**:

![Creating a file in the src folder](./img/stm32cube-debugging-unit-testing-3.png)

`src/main.h` defines the LED pin. On the Nucleo-F401RE, the green user LED
(LD2) is on `PA5`:

```cpp
#ifndef MAIN_H
#define MAIN_H

#include "stm32f4xx_hal.h"

#define LED_PIN                                GPIO_PIN_5
#define LED_GPIO_PORT                          GPIOA
#define LED_GPIO_CLK_ENABLE()                  __HAL_RCC_GPIOA_CLK_ENABLE()

#endif // MAIN_H
```

`src/main.c` initializes the HAL and the LED pin, then toggles the LED every
second:

```cpp
#include "main.h"

void LED_Init();

int main(void)
{
  HAL_Init();
  LED_Init();

  while (1)
  {
    HAL_GPIO_TogglePin(LED_GPIO_PORT, LED_PIN);
    HAL_Delay(1000);
  }
}

void LED_Init()
{
  LED_GPIO_CLK_ENABLE();
  GPIO_InitTypeDef GPIO_InitStruct;
  GPIO_InitStruct.Pin = LED_PIN;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_PULLUP;
  GPIO_InitStruct.Speed = GPIO_SPEED_HIGH;
  HAL_GPIO_Init(LED_GPIO_PORT, &GPIO_InitStruct);
}

void SysTick_Handler(void)
{
  HAL_IncTick();
}
```

## Build and upload {#compiling-and-uploading-the-firmware}

1. Build the project with **Build** in the **Project Tasks** panel, the
   **Build** button on the [PlatformIO toolbar](../../../guides/ide/vscode.md#platformio-toolbar),
   **Command Palette** > **PlatformIO: Build**, or
   <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>B</kbd>
   (<kbd>Cmd</kbd>+<kbd>Alt</kbd>+<kbd>B</kbd> on macOS):

   ![Ways to start a build](./img/stm32cube-debugging-unit-testing-4.png)

   The terminal shows `SUCCESS` when the build finishes:

   ![Successful build output](./img/stm32cube-debugging-unit-testing-5.png)

2. Connect the board and upload with **Upload** in the same places, or
   <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>U</kbd>
   (<kbd>Cmd</kbd>+<kbd>Alt</kbd>+<kbd>U</kbd> on macOS):

   ![Ways to start an upload](./img/stm32cube-debugging-unit-testing-6.png)

The green LED LD2 starts blinking.

## Debug the firmware {#debugging-the-firmware}

The board's on-board ST-LINK is also its debug probe, so no configuration is
needed.

1. Start a debug session with **Run** > **Start Debugging**, or press
   <kbd>F5</kbd>:

   ![Starting a debug session](./img/stm32cube-debugging-unit-testing-7.png)

2. Wait until the session stops at the first line of `main()`:

   ![Debug session stopped at main](./img/stm32cube-debugging-unit-testing-8.png)

3. Step through the code, set breakpoints, inspect peripheral registers, and
   add variables to **Watch**:

   ![Debugging with peripheral registers and watched variables](./img/stm32cube-debugging-unit-testing-9.png)

For more about debugging, see [Debugging](../../../guides/debugging/index.md).

## Write unit tests {#writing-unit-tests}

You will test the LED code on the board with the
[Unity](../../../guides/unit-testing/frameworks/unity.md) framework.

### Send test output over the serial port {#custom-unity-configuration}

Unity needs to know how to print its results. The STM32Cube framework has no
default output for Unity, so you provide a
[custom `unity_config.h`](../../../guides/unit-testing/frameworks/unity.md#unit-testing-frameworks-unity-custom-config)
that sends the output over `USART2`. On the Nucleo-F401RE, `USART2` is
connected to the ST-LINK, which appears on your computer as a virtual COM
port, so you need no USB-to-serial adapter.

1. Create a `test` folder in the project root (the
   [`test_dir`](../../../reference/platformio-ini/platformio/test-dir.md)):

   ![The test folder in the project](./img/stm32cube-debugging-unit-testing-10.png)

2. Create `test/unity_config.h`:

   ```cpp
   #ifndef UNITY_CONFIG_H
   #define UNITY_CONFIG_H

   #ifndef NULL
   #ifndef __cplusplus
   #define NULL (void*)0
   #else
   #define NULL 0
   #endif
   #endif

   #ifdef __cplusplus
   extern "C"
   {
   #endif

   void unityOutputStart();
   void unityOutputChar(char);
   void unityOutputFlush();
   void unityOutputComplete();

   #define UNITY_OUTPUT_START()    unityOutputStart()
   #define UNITY_OUTPUT_CHAR(c)    unityOutputChar(c)
   #define UNITY_OUTPUT_FLUSH()    unityOutputFlush()
   #define UNITY_OUTPUT_COMPLETE() unityOutputComplete()

   #ifdef __cplusplus
   }
   #endif /* extern "C" */

   #endif /* UNITY_CONFIG_H */
   ```

3. Create `test/unity_config.c`. It initializes `USART2` at 115200 baud and
   implements the output functions declared above:

   ```cpp
   #include "unity_config.h"
   #include "stm32f4xx_hal.h"

   #define USARTx USART2
   #define USARTx_CLK_ENABLE() __HAL_RCC_USART2_CLK_ENABLE()
   #define USARTx_CLK_DISABLE() __HAL_RCC_USART2_CLK_DISABLE()
   #define USARTx_RX_GPIO_CLK_ENABLE() __HAL_RCC_GPIOA_CLK_ENABLE()
   #define USARTx_TX_GPIO_CLK_ENABLE() __HAL_RCC_GPIOA_CLK_ENABLE()
   #define USARTx_RX_GPIO_CLK_DISABLE() __HAL_RCC_GPIOA_CLK_DISABLE()
   #define USARTx_TX_GPIO_CLK_DISABLE() __HAL_RCC_GPIOA_CLK_DISABLE()

   #define USARTx_FORCE_RESET() __HAL_RCC_USART2_FORCE_RESET()
   #define USARTx_RELEASE_RESET() __HAL_RCC_USART2_RELEASE_RESET()

   #define USARTx_TX_PIN GPIO_PIN_2
   #define USARTx_TX_GPIO_PORT GPIOA
   #define USARTx_TX_AF GPIO_AF7_USART2
   #define USARTx_RX_PIN GPIO_PIN_3
   #define USARTx_RX_GPIO_PORT GPIOA
   #define USARTx_RX_AF GPIO_AF7_USART2

   static UART_HandleTypeDef UartHandle;

   void unityOutputStart()
   {
     GPIO_InitTypeDef GPIO_InitStruct;

     USARTx_TX_GPIO_CLK_ENABLE();
     USARTx_RX_GPIO_CLK_ENABLE();

     USARTx_CLK_ENABLE();

     GPIO_InitStruct.Pin = USARTx_TX_PIN;
     GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
     GPIO_InitStruct.Pull = GPIO_PULLUP;
     GPIO_InitStruct.Speed = GPIO_SPEED_FAST;
     GPIO_InitStruct.Alternate = USARTx_TX_AF;

     HAL_GPIO_Init(USARTx_TX_GPIO_PORT, &GPIO_InitStruct);

     GPIO_InitStruct.Pin = USARTx_RX_PIN;
     GPIO_InitStruct.Alternate = USARTx_RX_AF;

     HAL_GPIO_Init(USARTx_RX_GPIO_PORT, &GPIO_InitStruct);
     UartHandle.Instance = USARTx;

     UartHandle.Init.BaudRate = 115200;
     UartHandle.Init.WordLength = UART_WORDLENGTH_8B;
     UartHandle.Init.StopBits = UART_STOPBITS_1;
     UartHandle.Init.Parity = UART_PARITY_NONE;
     UartHandle.Init.HwFlowCtl = UART_HWCONTROL_NONE;
     UartHandle.Init.Mode = UART_MODE_TX_RX;
     UartHandle.Init.OverSampling = UART_OVERSAMPLING_16;

     if (HAL_UART_Init(&UartHandle) != HAL_OK)
     {
       while (1)
       {
       }
     }
   }

   void unityOutputChar(char c)
   {
     HAL_UART_Transmit(&UartHandle, (uint8_t *)(&c), 1, 1000);
   }

   void unityOutputFlush() {}

   void unityOutputComplete()
   {
     USARTx_CLK_DISABLE();
     USARTx_RX_GPIO_CLK_DISABLE();
     USARTx_TX_GPIO_CLK_DISABLE();
   }
   ```

### Add the tests {#add-the-tests}

Unity calls `setUp()` before and `tearDown()` after each test; here they
initialize and deinitialize the LED pin. `main()` runs the tests.

| Test | Checks |
| --- | --- |
| `test_led_builtin_pin_number` | `LED_PIN` has the expected value |
| `test_led_state_high` | `HAL_GPIO_WritePin()` and `HAL_GPIO_ReadPin()` with `GPIO_PIN_SET` |
| `test_led_state_low` | `HAL_GPIO_WritePin()` and `HAL_GPIO_ReadPin()` with `GPIO_PIN_RESET` |

Create `test/test_main.c`:

:::note

The 2-second delay at the start of `main()` gives the test runner time to
open the serial port, because this board cannot be reset through the serial
port's DTR/RTS lines.

:::

```cpp
#include "../src/main.h"
#include <unity.h>

void setUp(void)
{
  LED_GPIO_CLK_ENABLE();
  GPIO_InitTypeDef GPIO_InitStruct;
  GPIO_InitStruct.Pin = LED_PIN;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_PULLUP;
  GPIO_InitStruct.Speed = GPIO_SPEED_HIGH;
  HAL_GPIO_Init(LED_GPIO_PORT, &GPIO_InitStruct);
}

void tearDown(void)
{
  HAL_GPIO_DeInit(LED_GPIO_PORT, LED_PIN);
}

void test_led_builtin_pin_number(void)
{
  TEST_ASSERT_EQUAL(GPIO_PIN_5, LED_PIN);
}

void test_led_state_high(void)
{
  HAL_GPIO_WritePin(LED_GPIO_PORT, LED_PIN, GPIO_PIN_SET);
  TEST_ASSERT_EQUAL(GPIO_PIN_SET, HAL_GPIO_ReadPin(LED_GPIO_PORT, LED_PIN));
}

void test_led_state_low(void)
{
  HAL_GPIO_WritePin(LED_GPIO_PORT, LED_PIN, GPIO_PIN_RESET);
  TEST_ASSERT_EQUAL(GPIO_PIN_RESET, HAL_GPIO_ReadPin(LED_GPIO_PORT, LED_PIN));
}

int main()
{
  HAL_Init();      // initialize the HAL library
  HAL_Delay(2000); // service delay

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

  while (1)
  {
  }
}

void SysTick_Handler(void)
{
  HAL_IncTick();
}
```

### Run the tests {#run-the-tests}

1. Run the tests on the board with the **Test** button on the PlatformIO
   toolbar or **Test** in the **Project Tasks** panel:

   ![Ways to run the tests](./img/stm32cube-debugging-unit-testing-11.png)

2. PlatformIO builds and uploads the tests and shows a report. All tests
   pass:

   ![Test report](./img/stm32cube-debugging-unit-testing-12.png)

## Next steps {#conclusion}

You now have a working STM32Cube project that you can use as a starting point
for more complex firmware. The complete project is in the
[PlatformIO examples](https://github.com/platformio/platformio-examples/tree/develop/unit-testing/stm32cube)
repository.

<a id="project-source-code"></a>

- [ST STM32 platform](/hardware/platforms/ststm32): upload methods and
  debugging options.
- [Unit testing](../../../guides/unit-testing/index.md): test on the host or
  in CI.
