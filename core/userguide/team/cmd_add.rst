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

.. _cmd_team_add:

pio team add
============

.. versionadded:: 5.0

.. contents::

Usage
-----

.. code-block:: bash

    pio team add ORGNAME:TEAMNAME USERNAME

Description
-----------

Add a new member to a team.

If you need to create a new team, please use :ref:`cmd_team_create` command.

Examples
--------

Add Bob to the "developers" team of "platformio" organization

.. code-block:: bash

    > pio team add platformio:developers bob
    The new member "bob" has been successfully added to the "developers" team.

See Also
--------

* :ref:`cmd_team_create`
* :ref:`cmd_team_list`
* :ref:`cmd_team_remove`
