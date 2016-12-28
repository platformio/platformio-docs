..  Copyright 2014-present PlatformIO <contact@platformio.org>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _cmd_lib_show:

platformio lib show
===================

.. contents::

Usage
-----

.. code-block:: bash

    platformio lib show [LIBRARY]
    pio lib show [LIBRARY]


Description
-----------

Show detailed info about a library using
`PlatformIO Library Registry <http://platformio.org/lib>`_.

The possible values for ``[LIBRARY]``:

* Library ID from Registry (preferred)
* Library Name

Examples
--------

.. code::

    > platformio lib show OneWire

    OneWire
    =======
    Control 1-Wire protocol (DS18S20, DS18B20, DS2408 and etc)

    Version: 2.3.2, released 3 months ago
    Registry ID: 1
    Manifest: https://raw.githubusercontent.com/PaulStoffregen/OneWire/master/library.json
    Homepage: https://www.pjrc.com/teensy/td_libs_OneWire.html
    Repository: https://github.com/PaulStoffregen/OneWire

    Authors
    -------
    Paul Stoffregen <paul@pjrc.com> http://www.pjrc.com (maintainer)
    Tom Pollard <pollard@alum.mit.edu>
    Derek Yerger
    Jim Studt
    Jason Dangel <dangel.jason@gmail.com>
    Robin James
    Ken Butcher
    Guillermo Lovato
    Scott Roberts
    Bertrik Sikken
    Mark Tillotson
    Glenn Trewitt
    Josh Larios

    Keywords
    --------
    onewire
    temperature
    bus
    1-wire
    ibutton
    sensor

    Compatible Frameworks
    ---------------------
    arduino

    Headers
    -------
    OneWire.h

    Examples
    --------
    http://dl.platformio.org/libraries/examples/0/1/DS18x20_Temperature.pde
    http://dl.platformio.org/libraries/examples/0/1/DS2408_Switch.pde
    http://dl.platformio.org/libraries/examples/0/1/DS250x_PROM.pde

    Versions
    --------
    2.3.2, released 3 months ago

    Unique Downloads
    ----------------
    Today: 5
    Week: 87
    Month: 341
