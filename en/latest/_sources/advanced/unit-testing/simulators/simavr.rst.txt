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

.. _unit_testing_simulators_simavr:

SimAVR
------

`SimAVR <https://github.com/buserror/simavr/>`_ is a lean, mean and hackable
AVR simulator.

.. warning::
  SimAVR does not work on Windows for the Unit Testing due to
  `issue #489 <https://github.com/buserror/simavr/issues/489>`_.

Configuration
~~~~~~~~~~~~~

Integration of the SimAVR simulator requires adding the
`platformio/tool-simavr <https://registry.platformio.org/tools/platformio/tool-simavr>`_
package to the :ref:`projectconf_env_platform_packages` option in your
:ref:`projectconf`, setting :ref:`projectconf_test_speed` to the ``9600``,
and overriding  :ref:`projectconf_test_testing_command`.

See the example of ``platformio.ini`` for the :ref:`board_atmelavr_uno`
board from :ref:`platform_atmelavr`:

.. code-block:: ini

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

Testing
~~~~~~~

SimAVR does not require a firmware uploading stage. Please use
the :option:`pio test --without-uploading` command option.


.. code::

  > pio test --without-uploading

  Verbose mode can be enabled via `-v, --verbose` option
  Collected 1 tests

  Processing test_dummy in uno environment
  ----------------------------------------
  Building...
  Testing...
  test/test_dummy/test_main.cpp:19: dummy_test	[PASSED]
  --------------------------- uno:test_dummy [PASSED] Took 0.94 seconds -------------------------

  =============================== SUMMARY ===============================
  Environment    Test        Status    Duration
  -------------  ----------  --------  ------------
  uno            test_dummy  PASSED    00:00:00.942
  ======================= 1 test cases: 1 succeeded in 00 ==================================
