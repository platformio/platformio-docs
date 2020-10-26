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
- temporary data.

Options
-------

.. program:: pio system prune

.. option::
    --force, -f

Do not prompt for confirmation.

Examples
--------

.. code::

    > pio system prune

    WARNING! This will remove:
     - cached API requests
     - cached package downloads
     - temporary data
    Do you want to continue? [y/N]: y
    Total reclaimed space: 36.48KB
