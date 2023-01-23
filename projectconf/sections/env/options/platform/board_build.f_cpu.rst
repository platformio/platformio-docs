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

.. _projectconf_board_build.f_cpu:

``board_build.f_cpu``
^^^^^^^^^^^^^^^^^^^^^

Type: ``Number`` | Multiple: ``No``

The option ``board_build.f_cpu`` is used to define MCU frequency (Hertz, Clock). A
format of this option is ``C-like long integer`` value with ``L`` suffix. The
1 Hertz is equal to ``1L``, then 16 MHz (Mega Hertz) is equal to ``16000000L``.

The full list of ``board_build.f_cpu`` for the popular embedded platforms you can
find in *Boards* section of :ref:`platforms`. See "Frequency" column.

.. note::
    This option doesn't make any changes to real clock settings on hardware. You should
    specify a ``board_build.f_cpu`` value  if you have changed a target's clock frequency
    so that the underlying software will be configured accordingly to match the change.
