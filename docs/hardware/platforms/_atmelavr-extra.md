## Configuration {#configuration}

<a id="atmelavr-upload-via-programmer"></a>

### Upload using programmer {#upload-using-programmer}

In the case of external programmers, it's easy to brick a board simply by specifying incorrect upload flags. It's highly recommended to use the [upload_command](../../reference/platformio-ini/env/upload-command.md) option that gives the full control over flags used for uploading.

:::note

The list of supported programmers available in avrdude is accessible via the `avrdude -c ?` command

:::

Configuration for the programmers:

- AVRISP

  ```ini
  [env:program_via_AVRISP]
  platform = atmelavr
  framework = arduino
  upload_protocol = custom
  upload_port = SERIAL_PORT_HERE
  upload_speed = 19200
  upload_flags =
      -C
      ; use "tool-avrdude-megaavr" for the atmelmegaavr platform
      ${platformio.packages_dir}/tool-avrdude/avrdude.conf
      -p
      $BOARD_MCU
      -P
      $UPLOAD_PORT
      -b
      $UPLOAD_SPEED
      -c
      stk500v1
  upload_command = avrdude $UPLOAD_FLAGS -U flash:w:$SOURCE:i
  ```

- AVRISP mkII

  ```ini
  [env:program_via_AVRISP_mkII]
  platform = atmelavr
  framework = arduino
  upload_protocol = custom
  upload_port = usb
  upload_flags =
      -C
      ; use "tool-avrdude-megaavr" for the atmelmegaavr platform
      ${platformio.packages_dir}/tool-avrdude/avrdude.conf
      -p
      $BOARD_MCU
      -P
      $UPLOAD_PORT
      -c
      stk500v2
  upload_command = avrdude $UPLOAD_FLAGS -U flash:w:$SOURCE:i
  ```

- USBtinyISP

  ```ini
  [env:myenv]
  platform = atmelavr
  framework = arduino
  upload_protocol = usbtiny

  [env:program_via_USBtinyISP]
  platform = atmelavr
  framework = arduino
  upload_protocol = custom
  upload_flags =
      -C
      ; use "tool-avrdude-megaavr" for the atmelmegaavr platform
      ${platformio.packages_dir}/tool-avrdude/avrdude.conf
      -p
      $BOARD_MCU
      -c
      usbtiny
  upload_command = avrdude $UPLOAD_FLAGS -U flash:w:$SOURCE:i
  ```

- DiamexISP

  ```ini
  [env:program_via_DiamexISP]
  platform = atmelavr
  framework = arduino
  upload_protocol = avrispv2
  upload_port = SERIAL_PORT_HERE
  upload_speed = 19200
  upload_flags =
      -C
      ; use "tool-avrdude-megaavr" for the atmelmegaavr platform
      ${platformio.packages_dir}/tool-avrdude/avrdude.conf
      -p
      $BOARD_MCU
      -P
      $UPLOAD_PORT
      -b
      $UPLOAD_SPEED
      -c
      stk500v2
  upload_command = avrdude $UPLOAD_FLAGS -U flash:w:$SOURCE:i
  ```

- Arduino as ISP

  ```ini
  [env:program_via_ArduinoISP]
  platform = atmelavr
  framework = arduino
  upload_protocol = custom
  upload_port = SERIAL_PORT_HERE
  upload_speed = 19200
  upload_flags =
      -C
      ; use "tool-avrdude-megaavr" for the atmelmegaavr platform
      ${platformio.packages_dir}/tool-avrdude/avrdude.conf
      -p
      $BOARD_MCU
      -P
      $UPLOAD_PORT
      -b
      $UPLOAD_SPEED
      -c
      stk500v1
  upload_command = avrdude $UPLOAD_FLAGS -U flash:w:$SOURCE:i
  ```

- USBasp

  ```ini
  [env:program_via_USBasp]
  platform = atmelavr
  framework = arduino
  upload_protocol = custom
  upload_port = usb
  upload_flags =
      -C
      ; use "tool-avrdude-megaavr" for the atmelmegaavr platform
      ${platformio.packages_dir}/tool-avrdude/avrdude.conf
      -p
      $BOARD_MCU
      -P
      $UPLOAD_PORT
      -c
      usbasp
  upload_command = avrdude $UPLOAD_FLAGS -U flash:w:$SOURCE:i
  ```

- Parallel Programmer

  ```ini
  [env:program_via_PP]
  platform = atmelavr
  framework = arduino
  upload_protocol = custom
  upload_flags =
      -C
      ; use "tool-avrdude-megaavr" for the atmelmegaavr platform
      ${platformio.packages_dir}/tool-avrdude/avrdude.conf
      -p
      $BOARD_MCU
      -c
      dapa
      -F
  upload_command = avrdude $UPLOAD_FLAGS -U flash:w:$SOURCE:i
  ```

- Bus Pirate as ISP

  ```ini
  [env:program_via_BP]
  platform = atmelavr
  framework = arduino
  upload_protocol = custom
  upload_port = SERIAL_PORT_HERE
  upload_speed = 115200
  upload_flags =
      -C
      ; use "tool-avrdude-megaavr" for the atmelmegaavr platform
      ${platformio.packages_dir}/tool-avrdude/avrdude.conf
      -p
      $BOARD_MCU
      -P
      $UPLOAD_PORT
      -b
      $UPLOAD_SPEED
      -c
      buspirate
  upload_command = avrdude $UPLOAD_FLAGS -U flash:w:$SOURCE:i
  ```

### Upload EEPROM data {#upload-eeprom-data}

To upload EEPROM data (from EEMEM directive) you need to use `uploadeep` target instead `upload` for [`pio run --target`](../../reference/cli/pio-run.md#cmdoption-pio-run-t) command. For example, `pio run -t uploadeep`.

### Erase chip before programming {#erase-chip-before-programming}

In some cases erasing chip memory is a mandatory procedure before uploading bootloader or setting fuses. AVRDUDE provides a special flag `-e` that causes a chip erase to be executed. This will reset the contents of the flash ROM and EEPROM to the value `0xff`, and clear all lock bits. The easiest way to use it is to add this flag via the [upload_flags](../../reference/platformio-ini/env/upload-flags.md) option:

```ini
[env:uno]
platform = atmelavr
framework = arduino
board = uno
upload_flags =
  -e
```

### Fuses programming {#fuses-programming}

PlatformIO has a built-in target called `fuses` for setting fuse bits. The default fuse bits are predefined in the board manifest file in the `fuses` section. For example, [fuses section for Arduino Uno board](https://github.com/platformio/platform-atmelavr/blob/develop/boards/uno.json). To set fuse bits you need to use target `fuses` with [`pio run --target`](../../reference/cli/pio-run.md#cmdoption-pio-run-t) command.

#### Custom fuses {#custom-fuses}

Custom fuse values and upload flags (based on upload protocol) should be specified in [`platformio.ini`](../../reference/platformio-ini/index.md). The `lfuse` and `hfuse` bits are mandatory, `efuse` is optional and not supported by all targets. An example of setting custom fuses for `uno` board:

```ini
[env:custom_fuses]
platform = atmelavr
framework = arduino
board = uno
upload_protocol = stk500v1
upload_speed = 19200
board_fuses.lfuse = 0xAA
board_fuses.hfuse = 0xBB
board_fuses.efuse = 0xCC
upload_flags =
    -PCOM15
    -b$UPLOAD_SPEED
    -e
```

#### MiniCore, MegaCore, MightyCore, MajorCore and MicroCore {#minicore-megacore-mightycore-majorcore-and-microcore}

`MiniCore`, `MegaCore`, `MightyCore`, `MajorCore` and `MicroCore` support dynamic fuses generation. Generated values are based on the following parameters:

| Parameter | Description | Default value |
|---|---|---|
| `board_build.f_cpu` | Specifies the clock frequencies in Hz. Used to determine what oscillator option to choose. A capital L has to be added to the end of the frequency number. | `16000000L` |
| `board_hardware.oscillator` | Specifies which oscillator is used `internal` or `external`. Internal oscillator only works with `f_cpu` values `8000000L` and `1000000L` | `external` |
| `board_hardware.uart` | Specifies the hardware UART port used for serial upload. can be `uart0`, `uart1`, `uart2` or `uart3` depending on the target. Use `no_bootloader` if you're not using a bootloader for serial upload. | `uart0` |
| `board_hardware.bod` | Specifies the hardware brown-out detection. Use `disabled` to disable brown-out detection. | `2.7v` |
| `board_hardware.eesave` | Specifies if the EEPROM memory should be retained when uploading using a programmer. Use `no` to disable | `yes` |
| `board_hardware.ckout` | Enables system clock output on targets that have this feature. The system clock will be output on a dedicated output pin. See the target datasheet for more information. Use `Yes` to enable | `no` |
| `board_hardware.jtagen` | Enables the JTAG programming and debugging interface for targets that supports JTAG. Use `Yes` to enable | `no` |
| `board_hardware.cfd` | Enables clock failure detection. Note that this feature is only available on ATmega324PB and ATmega328PB. Use `Yes` to enable CFD | `no` |

Valid BOD values:

| ATmega8, ATmega8515, ATmega8535/16/32, ATmega64/128 | AT90CAN32/64/128 | Other targets |
|---|---|---|
| 4.0v | 4.1v | 4.3v |
| 2.7v | 4.0v | 2.7v |
| disabled | 3.9v | 1.8v |
|  | 3.8v | disabled |
|  | 2.7v |  |
|  | 2.6v |  |
|  | 2.5v |  |
|  | disabled |  |

Hardware configuration example:

```ini
[env:custom_fuses]
platform = atmelavr
framework = arduino
board = ATmega32

board_build.f_cpu = 1000000L
board_hardware.uart = uart0
board_hardware.oscillator = internal
board_hardware.bod = 2.7v
board_hardware.eesave = no

upload_protocol = usbasp
upload_flags =
  -Pusb
```

<a id="atmelavr-overriding-fuses-command"></a>

#### Overriding default fuses command {#overriding-default-fuses-command}

PlatformIO splits the command for programming fuses in the following overridable parts:

| Variable | Description | Examples |
|---|---|---|
| `FUSESUPLOADER` | The tool used for setting fuses | By default `avrdude` is used |
| `FUSESUPLOADERFLAGS` | General command-line options that control uploader's behavior | `-D`, `-V`, `-P COM1`, `-C atmelice_isp`, `-b 115200` |
| `FUSESFLAGS` | A list of flags specific to fuses settings | `-Ulock:w:0x2F:m`, `-Uefuse:w:0xCB:m`, `-Ulfuse:w:0xFF:m` |
| `SETFUSESCMD` | Variable that holds the final command compiled from variables above | `$FUSESUPLOADER $FUSESUPLOADERFLAGS $UPLOAD_FLAGS $FUSESFLAGS` |

If for any reason default parameters are not suitable for your project, you can override the entire upload command or any particular part of that command using [an extra script](../../reference/scripting-api/actions.md), for example, you can override only fuses values:

```python
Import("env")

env.Replace(
    FUSESFLAGS=[
        "-Uhfuse:w:0xAA:m",
        "-Uefuse:w:0xBB:m",
        "-Ulfuse:w:0xCC:m",
        "-Ulock:w:0xDD:m"
    ]
)
```

Or override a specific uploader flag:

```python
Import("env")

env.Append(
    FUSESUPLOADERFLAGS=[
        "-V",
        "-D"
    ]
)
```

It's also possible to completely override the entire upload command:

```python
Import("env")

env.Replace(
    FUSESUPLOADERFLAGS=[
        # use "tool-avrdude-megaavr" for the atmelmegaavr platform
        "-C", "$PROJECT_PACKAGES_DIR/tool-avrdude/avrdude.conf",
        "-p", "$BOARD_MCU",
        "-c", "atmelice_isp",
        "-e", "-v"
    ],
    SETFUSESCMD="avrdude $FUSESUPLOADERFLAGS -Ulock:w:0x0F:m",
)
```

### Bootloader programming {#bootloader-programming}

PlatformIO has a built-in target called `bootloader` for flashing bootloaders. The default bootloader image and corresponding fuse bits are predefined in the board manifest file in the `bootloader` section, for example, [Arduino Uno](https://github.com/platformio/platform-atmelavr/blob/develop/boards/uno.json). To upload a bootloader image you need to use target `bootloader` with [`pio run --target`](../../reference/cli/pio-run.md#cmdoption-pio-run-t) command.

#### Custom bootloader {#custom-bootloader}

Custom bootloader and accompanying fuses should be specified in [`platformio.ini`](../../reference/platformio-ini/index.md). If `lock_bits` and `unlock_bits` are not set then the default values `0x0F` and `0x3F` are used accordingly. An example of setting custom bootloader for `uno` board:

```ini
[env:uno]
platform = atmelavr
framework = arduino
board = uno

board_bootloader.file = /path/to/custom/bootloader.hex
board_bootloader.lfuse = 0xFF
board_bootloader.hfuse = 0xDE
board_bootloader.efuse = 0xFD
board_bootloader.lock_bits = 0x0F
board_bootloader.unlock_bits = 0x3F
```

`MiniCore`, `MegaCore`, `MightyCore` and `MajorCore` have a wide variety of precompiled bootloaders. Bootloader binaries are dynamically selected according to the hardware parameters `f_cpu`, `oscillator`, `uart` and `upload_speed`. For a complete table with all available baud rates, see the [Optiboot flash repo](https://github.com/MCUdude/optiboot_flash). Here is a table with recommended baud rates for different clock frequencies:

| Frequency | Oscillator type | Recommended upload speed |
|---|---|---|
| `20000000L` | external | `115200` |
| `18432000L` | external | `115200` |
| `16000000L` | external | `115200` |
| `14745600L` | external | `115200` |
| `12000000L` | external | `57600` |
| `11059200L` | external | `115200` |
| `8000000L` | external/internal | `57600/38400` |
| `7372800L` | external | `115200` |
| `4000000L` | external | `9600` |
| `3686400L` | external | `115200` |
| `2000000L` | external | `9600` |
| `1843200L` | external | `115200` |
| `1000000L` | external/internal | `9600` |

<a id="atmelavr-overriding-bootloader-command"></a>

#### Overriding default bootloader command {#overriding-default-bootloader-command}

PlatformIO splits the command for programming bootloader in the following overridable parts:

| Variable | Description | Examples |
|---|---|---|
| `BOOTUPLOADER` | The tool used for programming bootloader image | By default `avrdude` is used |
| `BOOTUPLOADERFLAGS` | General command-line options that control uploader's behavior | `-D`, `-V`, `-P COM1`, `-C atmelice_isp`, `-b 115200` |
| `BOOTFLAGS` | A list of flags specific to bootloader settings | `-Uflash:w:/path/to/bootlader_image:i`, `-Ulock:w:0x2F:m` |
| `UPLOADBOOTCMD` | Variable that holds the final command compiled from variables above | `$BOOTUPLOADER $BOOTUPLOADERFLAGS $UPLOAD_FLAGS $BOOTFLAGS` |

If for any reason default parameters are not suitable for your project, you can override the entire upload command or any particular part of that command using [an extra script](../../reference/scripting-api/actions.md), for example, you can override only fuses values:

```python
Import("env")

bootloader_path = "/path/to/custom/bootloader.hex"

env.Replace(
    BOOTFLAGS=[
        "-Uflash:w:%s:i" % bootloader_path,
        "-Ulock:w:0xFF:m"
    ]
)
```

Or override a specific uploader flag:

```python
Import("env")

env.Append(
    BOOTUPLOADERFLAGS=[
        "-e", "-p", "/dev/cu.usbserial-1414302"
    ]
)
```

It's also possible to completely override the entire upload command:

```python
Import("env")

env.Replace(
    BOOTUPLOADERFLAGS=[
        # use "tool-avrdude-megaavr" for the atmelmegaavr platform
        "-C", "$PROJECT_PACKAGES_DIR/tool-avrdude/avrdude.conf",
        "-p", "$BOARD_MCU",
        "-c", "atmelice_isp"
    ],
    UPLOADBOOTCMD="avrdude $BOOTUPLOADERFLAGS -Ulock:w:0x0F:m",
)
```
