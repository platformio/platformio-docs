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

.. _cmd_pkg_show:

pio pkg show
============

.. contents::

Usage
-----

.. code-block:: bash

    pio pkg show [OPTIONS] [<owner>/]<pkg>[@<version>]

Description
-----------

Show package information from the `PlatformIO Registry <https://registry.platformio.org>`__.

Options
-------

.. program:: pio pkg show

.. option::
    -t, --type

Set the type of a package if there is a conflict name.
See supported :ref:`cmd_pkg_install_types`.

Examples
--------

Show information about `ArduinoJson <https://registry.platformio.org/libraries/bblanchon/ArduinoJson>`__ package

.. code::

    > pio pkg show bblanchon/ArduinoJson

    bblanchon/ArduinoJson
    Library • 6.19.3 • Public • Published Tue Mar  8 16:24:14 2022

    https://registry.platformio.org/libraries/bblanchon/ArduinoJson

    A simple and efficient JSON library for embedded C++. ...

    ---------------------  ----------------------------------------------------------------
    Homepage               https://arduinojson.org/?utm_source=meta&utm_medium=library.json
    Repository             https://github.com/bblanchon/ArduinoJson.git
    License                MIT
    Popularity             2
    Stars                  5599
    Examples               10
    Installed Size         385.83KB
    Used By                134
    Compatible Platforms   *
    Compatible Frameworks  *
    Keywords               json, rest, http, web
    ---------------------  ----------------------------------------------------------------

    Version    Size      Published
    ---------  --------  -------------------
    6.19.3     85.04KB   2022-03-08 16:24:14
    6.19.2     84.82KB   2022-02-14 08:06:06
    ...

See Also
--------

* :ref:`cmd_pkg_search`
* :ref:`cmd_pkg_list`
* :ref:`cmd_pkg_install`
