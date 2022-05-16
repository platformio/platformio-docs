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

.. _unit_testing_simulators_renode:

Renode
------

.. image:: ../../../_static/images/debug_probes/renode.png
  :target: https://renode.io/?utm_source=platformio&utm_medium=docs

Renode is a development framework which accelerates IoT and embedded systems
development by letting you simulate physical hardware systems - including both the CPU,
peripherals, sensors, environment and wired or wireless medium between nodes.
For more information, see `Renode's official website <https://renode.io/?utm_source=platformio&utm_medium=docs>`__.

Configuration
~~~~~~~~~~~~~

Integration of the Renode requires adding the
`platformio/tool-renode <https://registry.platformio.org/tools/platformio/tool-renode>`_
package to the :ref:`projectconf_env_platform_packages` option in your
:ref:`projectconf`, and overriding the :ref:`projectconf_test_testing_command`.

See the example of ``platformio.ini`` for the :ref:`board_sifive_hifive1-revb`
board from :ref:`platform_sifive`:

.. code-block:: ini

  [env:hifive1-revb]
  platform = sifive
  framework = zephyr
  board = hifive1-revb

  platform_packages =
      platformio/tool-renode
  test_testing_command =
      ${platformio.packages_dir}/tool-renode/renode
      --disable-xwt
      -e include @scripts/single-node/sifive_fe310.resc
      -e showAnalyzer uart1
      -e sysbus LoadELF @${platformio.build_dir}/${this.__env__}/firmware.elf
      -e start

Testing
~~~~~~~

Renode does not require a firmware uploading stage. Please use
the :option:`pio test --without-uploading` command option.

.. code::

  > pio test --without-uploading

  Verbose mode can be enabled via `-v, --verbose` option
  Collected 1 tests

  Processing test_dummy in hifive1-revb environment
  -------------------------------------------------
  Building...
  Testing...
  14:56:26.9860 [INFO] Loaded monitor commands from: ~/.platformio/packages/tool-renode/scripts/monitor.py
  14:56:27.0093 [INFO] Monitor available in telnet mode on port 1234
  14:56:27.0433 [INFO] Including script: ~/.platformio/packages/tool-renode/scripts/single-node/sifive_fe310.resc
  14:56:27.0572 [INFO] System bus created.
  14:56:27.8744 [INFO] sysbus: Loaded SVD: /tmp/renode-60394/61f3c8f5-c4df-4dc2-b892-2f96defd7e06.tmp. Name: FE310. Description: E31 CPU Coreplex, high-performance, 32-bit RV32IMAC core
  14:56:27.9010 [INFO] sysbus: Loading segment of 20520 bytes length at 0x20400000.
  14:56:27.9148 [INFO] sysbus: Loading segment of 324 bytes length at 0x20405028.
  14:56:27.9149 [INFO] sysbus: Loading segment of 7944 bytes length at 0x80000148.
  14:56:27.9380 [INFO] cpu: Setting PC value to 0x20401BC4.
  14:56:28.0913 [INFO] sysbus: Loading segment of 32 bytes length at 0x20010000.
  14:56:28.0914 [INFO] sysbus: Loading segment of 19132 bytes length at 0x20010020.
  14:56:28.0914 [INFO] sysbus: Loading segment of 32 bytes length at 0x20014ADC.
  14:56:28.0915 [INFO] sysbus: Loading segment of 4288 bytes length at 0x80000000.
  14:56:28.0954 [INFO] cpu: Setting PC value to 0x20010000.
  14:56:28.1041 [INFO] SiFive-FE310: Machine started.
  14:56:28.1662 [INFO] uart0: [+0.28s host +0s virt 0s virt from start] *** Booting Zephyr OS build zephyr-v20701  ***
  14:56:28.1695 [INFO] uart0: [+3.38ms host +0s virt 0s virt from start]   test/test_dummy/main.c:13: dummy_test	[PASSED]
  --------------------- hifive1-revb:test_dummy [PASSED] Took 9.98 seconds ---------------------

  ================================================== SUMMARY ==================================================
  Environment    Test        Status    Duration
  -------------  ----------  --------  ------------
  hifive1-revb   test_dummy  PASSED    00:00:09.976
  ================================= 1 test cases: 1 succeeded in 00:00:09.976 =================================
