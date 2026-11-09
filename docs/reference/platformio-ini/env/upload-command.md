---
description: "A custom upload command which overwrites a default from development platform (platformio.ini option upload_command)."
---

# `upload_command`

- **Type:** String
- **Multiple values:** No

Override default [Development Platforms](../../../hardware/platforms/index.md) upload command with a custom command. You can pass a full upload command with arguments and options or mix with [upload_flags](./upload-flags.md).

In order to use `upload_command`, `upload_protocol = custom` must be specified.

Default upload commands are declared in `builder/main.py` script file of [Development Platforms](../../../hardware/platforms/index.md). See a list with open source [Development Platforms](../../../hardware/platforms/index.md) => [https://github.com/topics/platformio-platform](https://github.com/topics/platformio-platform)

:::note

Note that you can use build variables in `upload_command`, such as PlatformIO project folders and other runtime configuration. A list with build variables are available by running `pio run --target envdump` command.

:::

## Examples

1. Override default upload command but handle pre-uploading actions (looking for serial port, extra image preparation, etc.). Normally, the pre-configured upload options will be stored in `$UPLOADERFLAGS` build variable. A classic default upload command for [Development Platforms](../../../hardware/platforms/index.md) may look as `some-flash-bin-tool $UPLOADERFLAGS $SOURCE`, where `$SOURCE` will be replaced by a real program/firmware binary.

   `${platformio.packages_dir}` template points to [packages_dir](../platformio/packages-dir.md).

   ```ini
   [env:program_via_AVR_ISP]
   platform = atmelavr
   framework = arduino
   board = uno
   upload_protocol = custom
   upload_flags =
       -C
       ${platformio.packages_dir}/tool-avrdude/avrdude.conf
       -p
       atmega328p
       -P
       $UPLOAD_PORT
       -b
       115200
       -c
       stk500v1
   upload_command = avrdude $UPLOAD_FLAGS -U flash:w:$SOURCE:i
   ```

2. Override default upload command and skip pre-uploading actions.

   ```ini
   [env:program_via_usbasp]
   platform = atmelavr
   framework = arduino
   board = uno
   upload_protocol = custom
   upload_flags =
       -C
       ${platformio.packages_dir}/tool-avrdude/avrdude.conf
       -p
       atmega328p
       -Pusb
       -c
       stk500v1
   upload_command = avrdude $UPLOAD_FLAGS -U flash:w:$SOURCE:i

   ; Use ST-util for flashing
   ; https://github.com/texane/stlink

   [env:custom_st_flash]
   platform = ststm32
   framework = stm32cube
   board = bluepill_f103c6
   upload_protocol = custom
   upload_command = ${platformio.packages_dir}/tool-stlink/st-flash write $SOURCE 0x8000000
   ```
