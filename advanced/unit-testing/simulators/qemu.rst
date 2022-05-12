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

.. _unit_testing_simulators_qemu:

QEMU
----

.. image:: ../../../_static/images/debug_probes/qemu.png
  :target: https://www.qemu.org/?utm_source=platformio&utm_medium=docs

QEMU is a free and open-source emulator that performs hardware virtualization.
Official reference can be found `here  <https://www.qemu.org/?utm_source=platformio&utm_medium=docs>`__.

Configuration
~~~~~~~~~~~~~

Integration of the QEMU requires adding the platform compatible
package to the :ref:`projectconf_env_platform_packages` option in your
:ref:`projectconf`, and overriding the :ref:`projectconf_test_testing_command`.

See the example of ``platformio.ini`` for the :ref:`board_sifive_hifive1`
board from :ref:`platform_sifive`:

.. code-block:: ini

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

Testing
~~~~~~~

QEMU does not require a firmware uploading stage. Please use
the :option:`pio test --without-uploading` command option.

.. code::

  > pio test --without-uploading

  Verbose mode can be enabled via `-v, --verbose` option
  Collected 1 tests

  Processing test_dummy in hifive1 environment
  --------------------------------------------
  Building...
  Testing...
  test/test_dummy/main.c:18: dummy_test	[PASSED]
  ---------------------- hifive1:test_dummy [PASSED] Took 2.05 seconds ----------------------

  ======================================= SUMMARY =======================================
  Environment    Test        Status    Duration
  -------------  ----------  --------  ------------
  hifive1        test_dummy  PASSED    00:00:02.055
  ====================== 1 test cases: 1 succeeded in 00:00:02.055 ======================