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

.. _cmd_pkg_outdated:

pio pkg outdated
================

.. contents::

Usage
-----

.. code-block:: bash

    pio pkg outdated [OPTIONS]

Description
-----------

Check for outdated project packages and list version information for all dependencies.
This information includes the currently installed version, the desired version based on
`Semantic Versioning <https://semver.org/>`__, and the latest available version.

Options
-------

.. program:: pio pkg outdated

.. option::
    -d, --project-dir

Specify the path to project directory. By default, ``--project-dir`` is equal
to current working directory (``CWD``).

.. option::
    -e, --environment

Check for outdated packages only for the specified environments. Multiple environments are allowed.

Examples
--------

Check outdated packages for `ESPHome <https://github.com/esphome/esphome>`__ project

.. code::

    > pio pkg outdated -e esp8266-arduino
    Checking  [####################################]  100%

    Semantic Versioning color legend:
    <Major Update>  backward-incompatible updates
    <Minor Update>  backward-compatible features
    <Patch Update>  backward-compatible bug fixes

    Package      Current    Wanted    Latest    Type     Environments
    -----------  ---------  --------  --------  -------  ---------------
    ArduinoJson  6.18.5     6.18.5    6.19.1    Library  esp8266-arduino
    FastLED      3.3.2      3.3.2     3.5.0     Library  esp8266-arduino
    TinyGPSPlus  1.0.2      1.0.2     1.0.3     Library  esp8266-arduino
