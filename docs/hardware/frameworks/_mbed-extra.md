## Configuration {#configuration}

### Configuration system {#configuration-system}

:::warning

In Mbed OS 6 the list of supported boards was heavily reduced, only officially supported and well maintained targets left. More information in [the official explanation](https://os.mbed.com/blog/entry/Increase-the-quality-of-platform-support/).

:::

PlatformIO allows you to customize Mbed OS compile time configuration parameters using `mbed_app.json` manifest. It should be placed into the root of your project and located on the same level as ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md).

Configuration is defined using [JSON](https://en.wikipedia.org/wiki/JSON). Some examples of configuration parameters:

- The sampling period for a data acquisition application.
- The default stack size for a newly created OS thread.
- The receive buffer size of a serial communication library.
- The flash and RAM memory size of a target board.

See more details in the official [ARM Mbed OS Configuration System](https://os.mbed.com/docs/mbed-os/v6.16/program-setup/advanced-configuration.html).

A few PlatformIO-ready projects based on ARM Mbed OS which use `mbed_app.json`:

- [Freescale Kinetis: mbed-rtos-kvstore](https://github.com/platformio/platform-freescalekinetis/tree/develop/examples/mbed-rtos-kvstore)
- [ST STM32: mbed-rtos-mesh-minimal](https://github.com/platformio/platform-ststm32/tree/develop/examples/mbed-rtos-mesh-minimal)

:::warning

On Windows the maximum length for a path (file name and directory route, also known as `MAX_PATH`) — has been defined by 260 characters which can lead to compilation error for some targets. It's possible to shorten these paths is to install packages in root of any logical disk by specifying [core_dir](../../reference/platformio-ini/platformio/core-dir.md).

:::

#### Using Bare Metal profile {#using-bare-metal-profile}

The bare metal profile implements a subset of Mbed OS's RTOS APIs that are useful in non-threaded applications, such as semaphores (calling the release API from interrupts) and tickers (to set up a recurring interrupt). It does not include an RTX, and is therefore suitable for applications that do not require complex thread management. Instead of the RTOS's scheduler, all activities are polled or interrupt-driven.

Useful links:

- [Detailed description of bare metal profile](https://os.mbed.com/docs/mbed-os/v6.2/bare-metal/index.html)
- [Porting a target from Mbed OS 2 to Mbed OS 6 bare metal](https://os.mbed.com/docs/mbed-os/v6.2/bare-metal/porting-a-target-from-mbed-os-2-to-mbed-os-6-bare-metal.html)

##### Build profiles {#build-profiles}

By default, PlatformIO builds your project using `develop profile` which provides optimized firmware size with full error information and allows MCU to go to sleep mode. In the case when default build profile is not suitable for your project there two other profiles `release` and `debug` that can be enabled using special macro definitions. You can change build profile [build_flags](../../reference/platformio-ini/env/build-flags.md) of ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md):

| Name | Description |
|---|---|
| `MBED_BUILD_PROFILE_RELEASE` | Release profile (smallest firmware, minimal error info) |
| `MBED_BUILD_PROFILE_DEBUG` | Debug profile (largest firmware, disabled sleep mode) |

More information about differences between build profiles can be found on the official page [ARM Mbed OS Build Profiles](https://os.mbed.com/docs/mbed-os/v6.16/program-setup/build-profiles-and-rules.html).

#### Ignoring particular components {#ignoring-particular-components}

In case you don't need all parts of the framework or you want to reduce the compilation time, you can explicitly exclude folders with redundant sources. For example, to remove `cellular`, `kvstore` and `nanostack` features from the build process, navigate to the root of your project and create a new file `.mbedignore` with the following contents:

```ini
mbed-os/connectivity/cellular/*
mbed-os/connectivity/nanostack/*
mbed-os/storage/kvstore/*
```

#### Custom Targets {#custom-targets}

In case when your board is not officially supported by [Mbed](/hardware/frameworks/mbed) you can manually add custom board definitions to your project. First of all, you need to create a special file `custom_targets.json` in the root folder of your project where you describe your board, for example here is the configuration for `NUCLEO-F401RE` board:

```json
{
  "NUCLEO_F401RE": {
    "inherits": [
        "MCU_STM32"
    ],
    "supported_form_factors": [
        "ARDUINO",
        "MORPHO"
    ],
    "core": "Cortex-M4F",
    "extra_labels_add": [
        "STM32F4",
        "STM32F401xE"
    ],
    "macros_add": [
        "STM32F401xE"
    ],
    "config": {
        "clock_source": {
            "help": "Mask value : USE_PLL_HSE_EXTC | USE_PLL_HSE_XTAL (need HW patch) | USE_PLL_HSI",
            "value": "USE_PLL_HSE_EXTC|USE_PLL_HSI",
            "macro_name": "CLOCK_SOURCE"
        }
    },
    "detect_code": [
        "0720"
    ],
    "device_has_add": [
        "SERIAL_ASYNCH",
        "FLASH",
        "MPU"
    ],
    "device_name": "STM32F401RE"
  }
}
```

Secondly, you need to add code specific to your target to the `src` folder of your project. Usually, it's a good idea to isolate this code in a separate folder and add the path to this folder to [build_flags](../../reference/platformio-ini/env/build-flags.md) of ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md):

```ini
[env:my_custom_board]
platform = nxplpc
framework = mbed
board = my_custom_board
build_flags = -I$PROJECT_SRC_DIR/MY_CUSTOM_BOARD_TARGET
```

Next, you need to inform PlatformIO that there is a new custom board. To do this, you can create `boards` directory in the root folder of your project and add a board manifest file with your board name, e.g. `my_custom_board.json` as described here [Custom Embedded Boards](../../guides/custom-platforms-and-boards/creating-board.md)

After these steps, your project structure should look like this:

```bash
project_dir
├── include
├── boards
│    └── my_custom_board.json
├── src
│    ├── main.cpp
│    └── MY_CUSTOM_BOARD_TARGET
│         ├── pinNames.h
│         └── pinNames.c
├── custom_targets.json
└── platformio.ini
```

<dl>

<dt>

More information about adding custom targets can be found on the official page

</dt>

<dd>

[Adding and configuring targets](https://os.mbed.com/docs/mbed-os/v6.2/porting/porting-custom-boards.html).

</dd>

</dl>

See full examples with a custom board:

- [https://github.com/platformio/platform-ststm32/tree/develop/examples/mbed-rtos-custom-target](https://github.com/platformio/platform-ststm32/tree/develop/examples/mbed-rtos-custom-target)
