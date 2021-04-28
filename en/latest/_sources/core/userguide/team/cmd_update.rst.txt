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

.. _cmd_team_update:

pio team update
===============

.. versionadded:: 5.0

.. contents::

Usage
-----

.. code-block:: bash

    pio team update [OPTIONS] ORGNAME:TEAMNAME

Description
-----------

Rename a team or update the existing details.

Options
~~~~~~~

.. program:: pio team update

.. option::
    --name

A new team name. Team name must only contain alphanumeric characters, single hyphens,
underscores, spaces. It can not begin or end with a hyphen or a underscore and must
not be longer than 20 characters.

.. option::
    --description

A team description.

Examples
--------

.. code-block:: bash

    > pio team update platformio:dev --description "Developers team"
    The team "dev" has been successfully updated.

See Also
--------

* :ref:`cmd_team_list`
* :ref:`cmd_team_remove`
