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

.. _debugging_tool_blackmagic:

Black Magic Probe
=================

:Configuration:
  :ref:`projectconf_debug_tool` = ``blackmagic``

.. image:: ../../_static/debug_probes/blackmagic.jpg
  :target: https://github.com/blacksphere/blackmagic/wiki?utm_source=platformio&utm_medium=docs

The Black Magic Probe is a modern, in-application debugging tool for embedded
microprocessors. It is able to control and examine the state of the target
microprocessor using a JTAG or Serial Wire Debugging (SWD) port and on-chip
debug logic provided by the microprocessor. The probe connects to a host
computer using a standard USB interface.
`Vendor information... <https://github.com/blacksphere/blackmagic/wiki?utm_source=platformio&utm_medium=docs>`__

Also, see :ref:`debugging_tool_custom` debugging configuration with
Black Magic Probe.

Drivers
-------

Not required.

.. begin_compatible_platforms

Compatible Platforms
--------------------

* :ref:`platform_atmelsam`
* :ref:`platform_freescalekinetis`
* :ref:`platform_nordicnrf51`
* :ref:`platform_nordicnrf52`
* :ref:`platform_nxplpc`
* :ref:`platform_siliconlabsefm32`
* :ref:`platform_ststm32`

.. end_compatible_platforms