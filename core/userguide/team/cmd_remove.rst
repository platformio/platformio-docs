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

.. _cmd_team_remove:

pio team remove
===============

.. versionadded:: 5.0

.. contents::

Usage
-----

.. code-block:: bash

    pio team remove ORGNAME:TEAMNAME USERNAME

Description
-----------

Remove a member from a team.

If you need to destroy an existing team, please use :ref:`cmd_team_destroy` command.

Examples
--------

Remove Bob from the "dev" team of "platformio" organization:

.. code-block:: bash

    > pio team remove platformio:dev bob
    The "bob" member has been successfully removed from the "dev" team.

See Also
--------

* :ref:`cmd_team_add`
* :ref:`cmd_team_list`
