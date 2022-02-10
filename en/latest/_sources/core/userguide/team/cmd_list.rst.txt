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

.. _cmd_team_list:

pio team list
=============

.. versionadded:: 5.0

.. contents::

Usage
-----

.. code-block:: bash

    pio team list [OPTIONS] [ORGNAME]

Description
-----------

List teams and their members.

Options
~~~~~~~

.. program:: pio team list

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`_ format.

Examples
--------

.. code-block:: bash

    > pio team list

    platformio:dev
    ------------------------
    Description:  Developers team
    Members:      alice, bob
