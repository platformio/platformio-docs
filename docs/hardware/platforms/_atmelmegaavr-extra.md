## Configuration {#configuration}

<a id="atmelmegaavr-upload-via-programmer"></a>

### Upload using programmer {#upload-using-programmer}

In the case of external programmers, it's easy to brick a board simply by specifying incorrect upload flags. It's highly recommended to use the [upload_command](../../reference/platformio-ini/env/upload-command.md) option that gives the full control over flags used for uploading. Read [Upload using Programmer](/hardware/platforms/atmelavr#atmelavr-upload-via-programmer) for more information.

#### Upload using pymcuprog serialUPDI {#upload-using-pymcuprog-serialupdi}

`pymcuprog` is a Python-based CLI tool for programming AVR devices with UPDI interface using either a Microchip debugger (Atmel-ICE, Power Debugger, PICkit4, Snap, PKOB nano / nEDBG / Curiosity Nano debugger) or via a standard serial port. It can be installed directly in the PlatformIO virtual environment using the following command:

```bash
python -m pip install pymcuprog
```

Once `pymcuprog` is installed it can be used as the uploader via a custom [upload_command](../../reference/platformio-ini/env/upload-command.md) option, for example:

```ini
[env:ATmega3209_pymcuprog_upload]
platform = atmelmegaavr
framework = arduino
board = ATmega3209
upload_speed = 115200
upload_flags =
    --tool
    uart
    --device
    atmega3209
    --uart
    $UPLOAD_PORT
    --clk
    $UPLOAD_SPEED
upload_command = pymcuprog write --erase $UPLOAD_FLAGS --filename $SOURCE
```

:::note

When using a Microchip debugger it must be specified in the --tool argument, and the --uart argument omitted.

:::

More information and a typical circuit diagram can be found in the official [pymcuprog repository](https://github.com/microchip-pic-avr-tools/pymcuprog#serial-port-updi-pyupdi).

`pymcuprog` is maintained by Microchip, and published on [GitHub](https://github.com/microchip-pic-avr-tools/pymcuprog) and [pypi.org](https://pypi.org/project/pymcuprog/).

#### Upload using pyupdi {#upload-using-pyupdi}

`pyupdi` is a Python-based tool for programming tinyAVR and megaAVR devices with UPDI interface via a standard serial port. It can be installed directly in the PlatformIO virtual environment using the following command:

```bash
python -m pip install https://github.com/mraardvark/pyupdi/archive/master.zip
```

Once `pyupdi` is installed it can be used as the uploader via a custom [upload_command](../../reference/platformio-ini/env/upload-command.md) option, for example:

```ini
[env:ATmega3209_pyupdi_upload]
platform = atmelmegaavr
framework = arduino
board = ATmega3209
upload_speed = 115200
upload_flags =
    -d
    mega3209
    -c
    $UPLOAD_PORT
    -b
    $UPLOAD_SPEED
upload_command = pyupdi $UPLOAD_FLAGS -f $SOURCE
```

:::warning

Device names used in in `pyupdi` differ from MCU names used in the `atmelmegaavr` platform. Run `pyupdi --help` to see the list of supported devices.

:::

More information and a typical circuit diagram can be found in the official [pyupdi repository](https://github.com/mraardvark/pyupdi) repository.

### Fuses programming {#fuses-programming}

PlatformIO has a built-in target called `fuses` for setting fuse bits. The default fuse bits are predefined in the board manifest file in the `fuses` section. For example, [fuses section for Arduino Nano Every board](https://github.com/platformio/platform-atmelmegaavr/blob/develop/boards/nano_every.json). To set fuse bits you need to use target `fuses` with [`pio run --target`](../../reference/cli/pio-run.md#cmdoption-pio-run-t) command.

#### Custom fuses {#custom-fuses}

Custom fuse values and upload flags (based on upload protocol) should be specified in [`platformio.ini`](../../reference/platformio-ini/index.md). An example of setting custom fuses for `ATmega3209` board:

```ini
[env:custom_fuses]
platform = atmelmegaavr
framework = arduino
board = ATmega3209
upload_protocol = xplainedmini_updi
board_fuses.bootend = 0xAA
board_fuses.syscfg0 = 0xBB
board_fuses.osccfg = 0xCC
```

#### Overriding default fuses command {#overriding-default-fuses-command}

For more detailed information read [Overriding default fuses command](/hardware/platforms/atmelavr#atmelavr-overriding-fuses-command).

### Bootloader programming {#bootloader-programming}

PlatformIO has a built-in target called `bootloader` for flashing bootloaders. The default bootloader image and corresponding fuse bits are predefined in the board manifest file in the `bootloader` section, for example, [Arduino Uno WiFi Rev2](https://github.com/platformio/platform-atmelmegaavr/blob/develop/boards/uno_wifi_rev2.json). To upload a bootloader image you need to use target `bootloader` with [`pio run --target`](../../reference/cli/pio-run.md#cmdoption-pio-run-t) command.

#### Custom bootloader {#custom-bootloader}

Custom bootloader and accompanying fuses should be specified in [`platformio.ini`](../../reference/platformio-ini/index.md). An example of setting custom bootloader for `ATmega4808` board:

```ini
[env:ATmega4808]
platform = atmelmegaavr
framework = arduino
board = ATmega4808

board_bootloader.file = /path/to/custom/bootloader.hex
board_bootloader.bootend = 0xFF
board_bootloader.syscfg0 = 0xDE
board_bootloader.osccfg = 0xFD
board_bootloader.lock_bits = 0x0F
```

#### Overriding default bootloader command {#overriding-default-bootloader-command}

For more detailed information read [Overriding default bootloader command](/hardware/platforms/atmelavr#atmelavr-overriding-bootloader-command).
