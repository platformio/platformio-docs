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

.. _cmd_access_grant:

pio access grant
================

.. versionadded:: 5.0

.. contents::

Usage
-----

.. code-block:: bash

    pio access grant [OPTIONS] LEVEL <ORGNAME:TEAMNAME>|<USERNAME> URN

Description
-----------

Add the ability of users and teams to have "LEVEL" access to a resource.

The next levels are supported:

:``admin``:
    Administrative privileges. Can perform all available operations on the particular resource.

:``maintainer``:
    Read-write access. Can update a resource, publish a new version, unpublish existing version.

    Cannot manage resource permissions and grant access to other members.

:``guest``:
    Read-only access. It's automatically granted for the public resources.

You can grant access to the team members using the next format ``orgname:teamname``.
See the examples below.

Options
~~~~~~~

.. program:: pio access grant

.. option::
    --urn-type

Resource type in `URN <https://en.wikipedia.org/wiki/Uniform_Resource_Name>`_ form.
Default is set to ``prn:reg:pkg`` which means to grant an access to the package in
the PlatormIO Registry.

Examples
--------

1. Grant "maintainer" access to a resource for the "bob" user:

.. code-block:: bash

    > pio access grant maintainer bob prn:reg:pkg:8036:platform
    Access for resource "prn:reg:pkg:8036:platform" has been granted for "bob"

2. Add the ability of PlatformIO's "developer" team to have "admin" access to a resource.

.. code-block:: bash

    > pio access grant admin platformio:developers prn:reg:pkg:8036:platform
    Access for resource "prn:reg:pkg:8036:platform" has been granted for "platformio:developers"

See Also
--------

* :ref:`cmd_access_revoke`
