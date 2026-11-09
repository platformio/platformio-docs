<a id="unit-testing-simulators-qemu"></a>

# QEMU {#qemu}

[![](./img/qemu.png)](https://www.qemu.org/?utm_source=platformio&utm_medium=docs)

QEMU is a free and open-source emulator that performs hardware virtualization. Official reference can be found [here](https://www.qemu.org/?utm_source=platformio&utm_medium=docs).

## Configuration {#configuration}

Integration of the QEMU requires adding the platform compatible package to the [platform_packages](../../../reference/platformio-ini/env/platform-packages.md) option in your [`platformio.ini`](../../../reference/platformio-ini/index.md), and overriding the [test_testing_command](../../../reference/platformio-ini/env/test-testing-command.md).

See the example of `platformio.ini` for the [HiFive1](/hardware/boards/sifive/hifive1) board from [SiFive](/hardware/platforms/sifive):

```ini
[env:hifive1]
platform = sifive
framework = freedom-e-sdk
board = hifive1

platform_packages =
    platformio/tool-qemu-riscv
test_testing_command =
    ${platformio.packages_dir}/tool-qemu-riscv/bin/qemu-system-riscv32
    -nographic
    -machine
    sifive_e
    -kernel
    ${platformio.build_dir}/${this.__env__}/firmware.elf
```

## Testing {#testing}

QEMU does not require a firmware uploading stage. Use the [`pio test --without-uploading`](../../../reference/cli/pio-test.md#cmdoption-pio-test-without-uploading) command option.

```bash
pio test --without-uploading
```

```text
Verbose mode can be enabled via `-v, --verbose` option
Collected 1 tests

Processing test_dummy in hifive1 environment
--------------------------------------------
Building...
Testing...
test/test_dummy/main.c:18: dummy_test [PASSED]
---------------------- hifive1:test_dummy [PASSED] Took 2.05 seconds ----------------------

======================================= SUMMARY =======================================
Environment    Test        Status    Duration
-------------  ----------  --------  ------------
hifive1        test_dummy  PASSED    00:00:02.055
====================== 1 test cases: 1 succeeded in 00:00:02.055 ======================
```
