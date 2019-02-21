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

Tutorials
---------

* :ref:`tutorial_espressif32_arduino_debugging_unit_testing`
* :ref:`tutorial_nordicnrf52_arduino_debugging_unit_testing`

Configuration
-------------

Switching between cores
~~~~~~~~~~~~~~~~~~~~~~~

If board supports multiple Arduino cores, you can switch between them using
``board_build.core`` option in :ref:`projectconf`.

For example, some boards of :ref:`platform_ststm32` development platform
support official ``stm32`` core and ``maple`` core by
`Roger Clark <https://github.com/rogerclarkmelbourne/Arduino_STM32>`_.

Example:

.. code-block:: ini

	[env:disco_f100rb_stm32]
	platform = ststm32
	framework = arduino
	board = disco_f100rb

	; Is set by default
	board_build.core = stm32

	[env:disco_f100rb_maple]
	platform = ststm32
	framework = arduino
	board = disco_f100rb

	; force to Maple core
	board_build.core = maple
