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

.. _projectconf_section_env_board:

Board options
~~~~~~~~~~~~~

.. contents::
    :local:

``board_mcu``
^^^^^^^^^^^^^

``board_mcu`` is a microcontroller(MCU) type that is used by compiler to
recognize MCU architecture. The correct type of ``board_mcu`` depends on
platform library. For example, the list of ``board_mcu`` for "megaAVR Devices"
is described `here <http://www.nongnu.org/avr-libc/user-manual/>`_.

The full list of ``board_mcu`` for the popular embedded platforms you can find
in *Boards* section of :ref:`platforms`. See "Microcontroller" column.

.. _projectconf_board_f_cpu:

``board_f_cpu``
^^^^^^^^^^^^^^^

An option ``board_f_cpu`` is used to define MCU frequency (Hertz, Clock). A
format of this option is ``C-like long integer`` value with ``L`` suffix. The
1 Hertz is equal to ``1L``, then 16 MHz (Mega Hertz) is equal to ``16000000L``.

The full list of ``board_f_cpu`` for the popular embedded platforms you can
find in *Boards* section of :ref:`platforms`. See "Frequency" column. You can
overclock a board by specifying a ``board_f_cpu`` value other than the default.

.. _projectconf_board_f_flash:

``board_f_flash``
^^^^^^^^^^^^^^^^^

An option ``board_f_flash`` is used to define FLASH chip frequency (Hertz, Clock). A
format of this option is ``C-like long integer`` value with ``L`` suffix. The
1 Hertz is equal to ``1L``, then 40 MHz (Mega Hertz) is equal to ``40000000L``.

This option isn't available for the all development platforms. The only
:ref:`platform_espressif8266` supports it.

.. _projectconf_board_flash_mode:

``board_flash_mode``
^^^^^^^^^^^^^^^^^^^^

Flash chip interface mode. This option isn't available for the all development
platforms. The only :ref:`platform_espressif8266` supports it.
