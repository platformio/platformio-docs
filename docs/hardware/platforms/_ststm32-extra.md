## Tutorials {#tutorials}

- [STM32Cube HAL and Nucleo-F401RE: debugging and unit testing](../../get-started/tutorials/ststm32/stm32cube-debugging-unit-testing.md)

## Configuration {#configuration}

### Switching between Arduino cores {#switching-between-arduino-cores}

There are three different Arduino cores for STM32 microcontrollers: STM32Duino, Arduino STM32 (maple) and STM32L0. All of them have been developed independently, therefore, have different functionality and set of internal libraries. By default, official STM32Duino core is used (except cases when a board supports only one specific core). Some of the boards support all three cores. To change the core you can use a `board_build.core` option that needs be added to [build_flags](../../reference/platformio-ini/env/build-flags.md):

An example of [`platformio.ini`](../../reference/platformio-ini/index.md) with `maple` core

```ini
[env:hy_tinystm103tb]
platform = ststm32
framework = arduino
board = hy_tinystm103tb
board_build.core = maple
```

### STM32Duino configuration system {#stm32duino-configuration-system}

STM32Duino core has several options that can be configured using the next configuration flags in [build_flags](../../reference/platformio-ini/env/build-flags.md) section of [`platformio.ini`](../../reference/platformio-ini/index.md):

**C/C++ standard library configuration**

| Name | Description |
|---|---|
| `PIO_FRAMEWORK_ARDUINO_STANDARD_LIB` | Disable Newlib Nano library |
| `PIO_FRAMEWORK_ARDUINO_NANOLIB_FLOAT_PRINTF` | Newlib Nano + float printf support |
| `PIO_FRAMEWORK_ARDUINO_NANOLIB_FLOAT_SCANF` | Newlib Nano + float scanf support |

**USART Configuration**

| Name | Description |
|---|---|
| `PIO_FRAMEWORK_ARDUINO_SERIAL_WITHOUT_GENERIC` | Enabled (no generic Serial) |
| `PIO_FRAMEWORK_ARDUINO_SERIAL_DISABLED` | Disabled (no Serial support) |

**USB Configuration**

| Name | Description |
|---|---|
| `PIO_FRAMEWORK_ARDUINO_ENABLE_CDC` | CDC (generic Serial supersede U(S)ART) |
| `PIO_FRAMEWORK_ARDUINO_ENABLE_CDC_WITHOUT_SERIAL` | CDC (no generic Serial) |
| `PIO_FRAMEWORK_ARDUINO_ENABLE_HID` | HID (keyboard and mouse) |

**USB Speed Configuration**

| Name | Description |
|---|---|
| `PIO_FRAMEWORK_ARDUINO_USB_HIGHSPEED` | High Speed mode |
| `PIO_FRAMEWORK_ARDUINO_USB_HIGHSPEED_FULLMODE` | High Speed in Full Speed mode |

Example:

```ini
[env:nucleo_f401re]
platform = ststm32
framework = arduino
board = nucleo_f401re
build_flags =
  -D PIO_FRAMEWORK_ARDUINO_ENABLE_CDC
  -D PIO_FRAMEWORK_ARDUINO_NANOLIB_FLOAT_PRINTF
  -D PIO_FRAMEWORK_ARDUINO_USB_HIGHSPEED_FULLMODE
```

### Maple STM32 configuration system {#maple-stm32-configuration-system}

In this core the USB peripheral (STM32F4 boards only) can be configured using the next configuration flags in [build_flags](../../reference/platformio-ini/env/build-flags.md) section of [`platformio.ini`](../../reference/platformio-ini/index.md):

**USB Configuration for STM32F4 boards**

| Name | Description |
|---|---|
| `ENABLE_USB_SERIAL` | USB serial (CDC) |
| `ENABLE_USB_MASS_STORAGE` | USB Mass Storage (MSC) |

Example:

```ini
[env:disco_f407vg]
platform = ststm32
framework = arduino
board = disco_f407vg
board_build.core = maple
build_flags = -D ENABLE_USB_MASS_STORAGE
```

### Arduino STM32L0 configuration system {#arduino-stm32l0-configuration-system}

Arduino STM32L0 core has several options that can be configured using the next configuration flags in [build_flags](../../reference/platformio-ini/env/build-flags.md) section of [`platformio.ini`](../../reference/platformio-ini/index.md):

**USB Configuration**

| Name | Description |
|---|---|
| `PIO_FRAMEWORK_ARDUINO_ENABLE_MASS_STORAGE` | Serial + Mass Storage |
| `PIO_FRAMEWORK_ARDUINO_ENABLE_HID` | Serial + Keyboard + Mouse |
| `PIO_FRAMEWORK_ARDUINO_ENABLE_MASS_STORAGE_HID` | Serial + Mass Storage + Keyboard + Mouse |
| `PIO_FRAMEWORK_ARDUINO_NO_USB` | No USB |

**FS Configuration**

| Name | Description |
|---|---|
| `PIO_FRAMEWORK_ARDUINO_FS_SDCARD` | SDCARD (SPI) |
| `PIO_FRAMEWORK_ARDUINO_FS_SFLASH` | SFLASH (SPI) |

Example:

```ini
[env:cricket_l082cz]
platform = ststm32
framework = arduino
board = cricket_l082cz
build_flags =
  -D PIO_FRAMEWORK_ARDUINO_ENABLE_MASS_STORAGE
```
