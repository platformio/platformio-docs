---
description: "An initial breakpoint that makes program stop whenever a certain point in the program is reached (platformio.ini option debug_init_break)."
---

<a id="projectconf-debug-init-break"></a>

# `debug_init_break` {#debug-init-break}

- **Type:** String
- **Multiple values:** No
- **Default:** `tbreak main`

An initial breakpoint that makes your program stop whenever a certain point in the program is reached. **Default** value is set to `tbreak main` and means creating a temporary breakpoint at `int main(...)` function and automatically delete it after the first time a program stops there.

- [GDB Setting Breakpoints](https://sourceware.org/gdb/onlinedocs/gdb/Set-Breaks.html#Set-Breaks)
- [GDB Breakpoint Locations](https://sourceware.org/gdb/onlinedocs/gdb/Specify-Location.html#Specify-Location)

:::note

Note that each debugging tool (adapter, probe) has limited number of hardware breakpoints.

If you need more **Project Initial Breakpoints**, please place them in [debug_extra_cmds](./debug-extra-cmds.md).

:::

## Examples

```ini
[env:debug]
platform = ...
board = ...

; Examples 1: disable initial breakpoint
debug_init_break =

; Examples 2: temporary stop at ``void loop()`` function
debug_init_break = tbreak loop

; Examples 3: stop in main.cpp at line 13
debug_init_break = break main.cpp:13

; Examples 4: temporary stop at ``void Reset_Handler(void)``
debug_init_break = tbreak Reset_Handler
```
