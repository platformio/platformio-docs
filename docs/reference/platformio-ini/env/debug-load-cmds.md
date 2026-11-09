<a id="projectconf-debug-load-cmds"></a>

# `debug_load_cmds` {#debug-load-cmds}

Type: `String` | Multiple: `Yes` | Default: `load`

Specify a command which will be used to load program/firmware to a target device. Possible options:

- `load` - **default** option
- `load [address]` - load program at specified address, where "\[address\]" should be a valid number
- `preload` - some embedded devices have locked Flash Memory (a few Freescale Kinetis and NXP LPC boards). In this case, firmware loading using debugging client is disabled. `preload` command instructs [PlatformIO Core (CLI)](../../../get-started/platformio-core.md) to load program/firmware using development platform "upload" method (via bootloader, media disk, etc)
- (empty value, `debug_load_cmds =`), disables program loading at all.
- `custom commands` - pass any debugging client command (GDB, etc.)

Sometimes you need to run extra monitor commands (on debug server side) before program/firmware loading, such as flash unlocking or erasing. In this case we can combine service commands with loading and run them before. See example:

```ini
[env:debug]
platform = ...
board = ...
debug_load_cmds =
  monitor flash erase_sector 0 0 11
  load
```
