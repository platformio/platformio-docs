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

.. _cmd_access:

pio access
==========

.. versionadded:: 5.0

Set access level on published resources (packages) in the registry.

You must have privileges to set the access of a resource:

* You are an owner of published resources
* You are a member of the team that owns a resource
* You have been given "maintainer" privileges for a package, either as a member of a team or directly as an owner.

Management of teams and team memberships is done with the :ref:`cmd_team` command.

To print all available commands and options use:

.. code-block:: bash

    pio access --help
    pio access COMMAND --help

.. toctree::
    :maxdepth: 2

    cmd_grant
    cmd_list
    cmd_private
    cmd_public
    cmd_revoke
