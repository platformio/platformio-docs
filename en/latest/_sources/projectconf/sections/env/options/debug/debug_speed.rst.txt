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

.. _projectconf_debug_speed:

``debug_speed``
---------------

Type: ``Number | String`` | Multiple: ``No``

The debug adapter speed. The value format depends on the type of :ref:`debugging_tools`.

.. note::
  Please note that this option takes effect only if :ref:`platforms` implement it.

Examples:

.. code-block:: ini

    [env:custom_debug_speed_examples]
    ...

    ; fixed speed in kHz
    debug_speed = 500

    ; automatic speed (only J-Link)
    debug_speed = auto

    ; adaptive clocking instead of fixed JTAG speed (only J-Link)
    debug_speed = adaptive
