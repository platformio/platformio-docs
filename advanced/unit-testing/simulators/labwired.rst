..  Copyright (c) 2014-present PlatformIO <contact@platformio.org>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _unit_testing_simulators_labwired:

LabWired
--------

.. image:: ../../../_static/images/debug_probes/labwired.png
  :target: https://labwired.com/?utm_source=platformio&utm_medium=docs

LabWired is an open source (MIT) deterministic firmware simulator with
instruction-level CPU models (ARM Cortex-M, RISC-V, Xtensa) and peripheral
models validated against physical silicon. The same firmware binary that runs
on hardware runs in the simulator, and a run produces identical results every
time, which makes it suitable as a CI gate. For more information, see
`LabWired's official website <https://labwired.com/?utm_source=platformio&utm_medium=docs>`__.

Configuration
~~~~~~~~~~~~~

Integration of LabWired requires the ``labwired`` CLI on ``PATH``

.. code-block:: bash

  curl -fsSL https://labwired.com/install.sh | sh

and overriding the :ref:`projectconf_test_testing_command` in your
:ref:`projectconf`. PlatformIO builds the test firmware, LabWired boots the
ELF and mirrors the test UART to stdout, and PlatformIO parses the Unity
results as usual.

See the example of ``platformio.ini`` for the :ref:`board_nordicnrf52_nrf52840_dk`
board from :ref:`platform_nordicnrf52`:

.. code-block:: ini

  [platformio]
  ; required so the ${platformio.*} variables below resolve

  [env:nrf52840_dk]
  platform = nordicnrf52
  board = nrf52840_dk
  test_framework = unity

  test_testing_command =
      labwired
      test
      --no-key
      --script
      labwired.test.yaml
      --firmware
      ${platformio.build_dir}/${this.__env__}/firmware.elf

The ``labwired.test.yaml`` script selects the board model and the UART that
Unity output is read from. A complete, runnable project (including the test
script, a bare-metal nRF52840 setup, and a GitHub Actions workflow) is
available at
`labwired-core/examples/platformio/nrf52840-unity <https://github.com/w1ne/labwired-core/tree/main/examples/platformio/nrf52840-unity>`__.

Testing
~~~~~~~

LabWired does not require a firmware uploading stage. Please use
the :option:`pio test --without-uploading` command option.

.. code::

  > pio test --without-uploading -e nrf52840_dk

  Verbose mode can be enabled via `-v, --verbose` option
  Collected 1 tests

  Processing test_smoke in nrf52840_dk environment
  ------------------------------------------------
  Building...
  Testing...
  test/test_smoke/test_main.c:50: test_addition         [PASSED]
  test/test_smoke/test_main.c:51: test_uart_is_enabled  [PASSED]
  test/test_smoke/test_main.c:52: test_string_length    [PASSED]
  -------------- nrf52840_dk:test_smoke [PASSED] Took 2.12 seconds --------------

  ================================ SUMMARY ================================
  Environment    Test        Status    Duration
  -------------  ----------  --------  ------------
  nrf52840_dk    test_smoke  PASSED    00:00:02.122
  ============== 3 test cases: 3 succeeded in 00:00:02.122 ==============
