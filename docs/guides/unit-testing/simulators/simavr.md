# SimAVR

[SimAVR](https://github.com/buserror/simavr/) is a lean, mean and hackable AVR simulator.

:::warning

SimAVR does not work on Windows for the Unit Testing due to [issue #489](https://github.com/buserror/simavr/issues/489).

:::

## Configuration {#configuration}

Integration of the SimAVR simulator requires adding the [platformio/tool-simavr](https://registry.platformio.org/tools/platformio/tool-simavr) package to the [platform_packages](../../../reference/platformio-ini/env/platform-packages.md) option in your [`platformio.ini`](../../../reference/platformio-ini/index.md), setting [test_speed](../../../reference/platformio-ini/env/test-speed.md) to the `9600`, and overriding  [test_testing_command](../../../reference/platformio-ini/env/test-testing-command.md).

See the example of `platformio.ini` for the [Arduino Uno](/hardware/boards/atmelavr/uno) board from [Atmel AVR](/hardware/platforms/atmelavr):

```ini
[env:uno]
platform = atmelavr
framework = arduino
board = uno

platform_packages =
    platformio/tool-simavr
test_speed = 9600
test_testing_command =
    ${platformio.packages_dir}/tool-simavr/bin/simavr
    -m
    atmega328p
    -f
    16000000L
    ${platformio.build_dir}/${this.__env__}/firmware.elf
```

## Testing {#testing}

SimAVR does not require a firmware uploading stage. Use the [`pio test --without-uploading`](../../../reference/cli/pio-test.md#cmdoption-pio-test-without-uploading) command option.

```bash
pio test --without-uploading
```

```text
Verbose mode can be enabled via `-v, --verbose` option
Collected 1 tests

Processing test_dummy in uno environment
----------------------------------------
Building...
Testing...
test/test_dummy/test_main.cpp:19: dummy_test  [PASSED]
--------------------------- uno:test_dummy [PASSED] Took 0.94 seconds -------------------------

=============================== SUMMARY ===============================
Environment    Test        Status    Duration
-------------  ----------  --------  ------------
uno            test_dummy  PASSED    00:00:00.942
======================= 1 test cases: 1 succeeded in 00 ==================================
```
