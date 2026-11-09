# Semihosting

Semihosting is a mechanism that enables code running on the target device to communicate and use the Input/Output of the host computer.

## Introduction {#introduction}

- [Introduction to ARM Semihosting](https://interrupt.memfault.com/blog/arm-semihosting)
- [Official ARM documentation](https://www.keil.com/support/man/docs/armcc/armcc_pge1358787046598.htm)
- [Segger: Semihosting](https://wiki.segger.com/Semihosting)

## Configuration {#configuration}

Firstly, to enable semihosting, you need to remove stubs (`-lnosys` and `-specs=nosys.specs` flags) from a development platform, and use the semihosted version of the syscalls (adding `--specs=rdimon.specs` and `-lrdimon` to the compiler).

Secondly, you need to override the [test_testing_command](../../reference/platformio-ini/env/test-testing-command.md) and configure a tool that will redirect test results to the I/O.

## Example {#example}

In this example, we run a simple `test_dummy` test on the [ST Nucleo L152RE](/hardware/boards/ststm32/nucleo-l152re) board from the [ST STM32](/hardware/platforms/ststm32) development platform.

The configuration is done in `enable_semihosting.py` extra script using [Advanced Scripting](../scripting/index.md). The example uses [Unity](./frameworks/unity.md) testing framework and the [Custom unity_config.h](./frameworks/unity.md#unit-testing-frameworks-unity-custom-config).

See the [source code and complete PlatformIO project](https://github.com/platformio/platformio-examples/tree/develop/unit-testing/semihosting).

## Testing {#testing}

We use the [pio test](../../reference/cli/pio-test.md) command to run the tests.

```bash
pio test
```

```text
Verbose mode can be enabled via `-v, --verbose` option
Collected 1 tests

Processing test_dummy in nucleo_l1521re environment
---------------------------------------------------
Building...
Uploading...
Testing...
Info : clock speed 300 kHz
Info : STLINK V2J29M18 (API v2) VID:PID 0483:374B
Info : Target voltage: 3.272727
Info : stm32l1.cpu: Cortex-M3 r2p0 processor detected
Info : stm32l1.cpu: target has 6 breakpoints, 4 watchpoints
Info : starting gdb server for stm32l1.cpu on 3333
Info : Listening on port 3333 for gdb connections
semihosting is enabled
Info : Unable to match requested speed 300 kHz, using 240 kHz
Info : Unable to match requested speed 300 kHz, using 240 kHz
Info : Listening on port 6666 for tcl connections
Info : Listening on port 4444 for telnet connections
test/test_dummy/test_main.c:19: test_dummy    [PASSED]
-------------------- nucleo_l1521re:test_dummy [PASSED] Took 5.43 seconds --------------------

===================================== SUMMARY =====================================
Environment     Test        Status    Duration
--------------  ----------  --------  ------------
nucleo_l1521re  test_dummy  PASSED    00:00:05.433
==================== 1 test cases: 1 succeeded in 00:00:05.433 ====================
```
