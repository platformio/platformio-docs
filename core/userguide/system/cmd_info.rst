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

.. _cmd_system_info:

platformio system info
======================

.. versionadded:: 4.4

.. contents::

Usage
-----


.. code-block:: bash

    platformio system info
    pio system info

Description
-----------

Display PlatformIO system-wide information

Options
-------

.. program:: platformio system info

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`_ format

Examples
--------

.. code::

    > platformio system info

    PlatformIO Core            4.4.0
    Python                     3.7.7-final.0
    System Type                darwin_x86_64
    Platform                   Darwin-19.5.0
    PlatformIO Core Directory  /Users/freedom/.platformio
    Global Libraries           1
    Development Platforms      36
    Package Tools              77
