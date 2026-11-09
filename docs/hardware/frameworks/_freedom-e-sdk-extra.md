## Configuration {#configuration}

### Using with FreeRTOS {#using-with-freertos}

In order to add FreeRTOS to your project, it must be explicitly specified as an additional framework in the `framework` field of ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md), for example:

```ini
[env:freertos]
platform = sifive
framework = freedom-e-sdk, freertos
board = ...
```

:::note

FreeRTOS RISC-V port for the [SiFive](/hardware/platforms/sifive) development platform is distributed as part of `Freedom E SDK` and cannot be used as a standalone framework

:::

Most of the application specific configuration is done in a special file called `FreeRTOSConfig.h` which must be present in each FreeRTOS-based project. Additional settings for build configuration are set in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) using the following syntax `board_build.freertos.*` where `*` is an option from the following list:

#### FreeRTOS settings {#freertos-settings}

<dl>

<dt>

heap_model

</dt>

<dd>



</dd>

</dl>

Available values: `heap_1, heap_2, heap_3, heap_4, heap_5` | Default: `heap_4`

FreeRTOS offers several heap management schemes that range in complexity and features:

- `heap_1` – the very simplest, does not permit memory to be freed.
- `heap_2` – permits memory to be freed, but does not coalescence adjacent free blocks.
- `heap_3` – simply wraps the standard `malloc()` and `free()` for thread safety.
- `heap_4` – coalescences adjacent free blocks to avoid fragmentation. Includes absolute address placement option.
- `heap_5` – as per `heap_4`, with the ability to span the heap across multiple non-adjacent memory areas.

More information about FreeRTOS Memory Management can be found in [the official documentation](https://www.freertos.org/a00111.html).

<dl>

<dt>

interrupt_handler

</dt>

<dd>



</dd>

</dl>

Default: `FreedomMetal_InterruptHandler`

The name of a function to be called to handle interrupts

<dl>

<dt>

exception_handler

</dt>

<dd>



</dd>

</dl>

Default: `FreedomMetal_ExceptionHandler`

The name of a function to be called to handle exceptions

<dl>

<dt>

mtime_ctrl_addr

</dt>

<dd>



</dd>

</dl>

Default: `0x2000000`

The address of Machine Timer Register `mtime`

<dl>

<dt>

mpu_wrappers

</dt>

<dd>



</dd>

</dl>

Available values: `enable | disable` | Default: `disable`

Use Memory Protection Unit wrappers

#### Segger SystemView settings {#segger-systemview-settings}

SystemView is a real-time recording and visualization tool for embedded systems that reveals the true runtime behavior of an application.

<dl>

<dt>

systemview

</dt>

<dd>



</dd>

</dl>

Available values: `enable | disable` | Default: `disable`

Compile and link Segger SystemView library

<dl>

<dt>

sysview_record_enter_isr

</dt>

<dd>



</dd>

</dl>

Default: `SEGGER_SYSVIEW_RecordEnterISR`

The name of a function to be called to record interrupt execution.

<dl>

<dt>

sysview_record_enter_isr

</dt>

<dd>



</dd>

</dl>

Default: `SEGGER_SYSVIEW_RecordExitISR`

The name of a function to be called to record finish of interrupt execution.

<dl>

<dt>

sysview_record_exit_isr_to_scheduler

</dt>

<dd>



</dd>

</dl>

Default: `SEGGER_SYSVIEW_RecordExitISRToScheduler`

The name of a function to be called to record finish of interrupt when it's caused by a context switch.

An example of ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) with modified heap settings and enabled SystemView feature:

```ini
[env:sifive-hifive1-revb]
platform = sifive
framework = freedom-e-sdk, freertos
board = hifive1-revb
monitor_speed = 115200
; Configure stack size
board_build.freedom-e-sdk.heap_size = 0x400
; Configure heap model and enable SystemView
board_build.freertos.heap_model = heap_1
board_build.freertos.systemview = enable
```

More information about FreeRTOS package for [SiFive](/hardware/platforms/sifive) development platform can be found in [the official repository](https://github.com/sifive/FreeRTOS-metal).
