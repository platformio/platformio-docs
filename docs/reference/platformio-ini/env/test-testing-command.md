---
description: "A custom testing command that runs test cases and returns results to the standard output (platformio.ini option test_testing_command)."
---

<a id="projectconf-test-testing-command"></a>

# `test_testing_command` {#test-testing-command}

- **Type:** String
- **Multiple values:** Yes

A custom testing command that executes test cases and returns results to the standard output.

Typically, a default value for the [Native](/hardware/platforms/native) is equal to:

```ini
[env:myenv]
platform = native
test_testing_command =
  ${platformio.build_dir}/${this.__env__}/program
```

You can override the default command and pass extra program arguments:

```ini
[env:myenv]
platform = native
test_testing_command =
  ${platformio.build_dir}/${this.__env__}/program
  arg1
  --option2
  option2_value
```

Note that you can pass extra arguments to the program using CLI and [`pio test --program-arg`](../../cli/pio-test.md#cmdoption-pio-test-a) option.

See [Simulators](../../../guides/unit-testing/simulators/index.md) examples.
