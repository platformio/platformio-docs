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

.. _cmd_system_prune:

pio system prune
================

.. versionadded:: 5.0

.. contents::

Usage
-----

.. code-block:: bash

    pio system prune

Description
-----------

Remove unused data:

- cached API requests
- cached package downloads
- temporary data
- unnecessary core packages
- unnecessary development platform packages.

.. note::
    If you have a custom package in :ref:`projectconf_pio_packages_dir` folder
    and would like to skip it from "prune process", please add empty ``.piokeep`` file
    to the root of a package folder.

Options
-------

.. program:: pio system prune

.. option::
    --force, -f

Do not prompt for confirmation.

.. option::
    --dry-run

Do not prune, only show data that will be removed.

.. option::
    --cache

Prune only cached data.

.. option::
    --core-packages

Prune only unnecessary core packages.

.. option::
    --platform-packages

Prune only unnecessary development platform packages.

Examples
--------

.. code::

    > pio system prune

    Prune cached data:
     - cached API requests
     - cached package downloads
     - temporary data
    Do you want to continue? [y/N]: y
    Space on disk: 2.34MB

    Prune unnecessary core packages:
    Calculating...
    Do you want to continue? [y/N]: y
    Space on disk: 0B

    Prune unnecessary development platform packages:
    Calculating...
    Package                                 Version       Size
    --------------------------------------  ------------  --------
    platformio/framework-stm32cube          2.0.200813    458.88MB
    platformio/framework-arduinosam         4.4.191002    290.35MB
    platformio/framework-arduino-samd       1.8.9         17.59MB
    platformio/framework-arduinonordicnrf5  1.600.190830  4.70MB
    Do you want to continue? [y/N]: y
    Tool Manager: Removing framework-arduino-samd @ 1.8.9
    Tool Manager: framework-arduino-samd @ 1.8.9 has been removed!
    Tool Manager: Removing framework-arduinonordicnrf5 @ 1.600.190830
    Tool Manager: framework-arduinonordicnrf5 @ 1.600.190830 has been removed!
    Tool Manager: Removing framework-arduinosam @ 4.4.191002
    Tool Manager: framework-arduinosam @ 4.4.191002 has been removed!
    Tool Manager: Removing framework-stm32cube @ 2.0.200813
    Tool Manager: framework-stm32cube @ 2.0.200813 has been removed!
    Space on disk: 771.52MB

    Total reclaimed space: 773.86MB
