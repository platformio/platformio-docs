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

.. _cmd_org_add:

pio org add
===========

.. versionadded:: 5.0

.. contents::

Usage
-----

.. code-block:: bash

    pio org add ORGNAME USERNAME

Description
-----------

Add a user as an owner to an organization.

If you need to create a new organization, please use :ref:`cmd_org_create` command.

Examples
--------

Add Bob as an owner of "platformio" organization:

.. code-block:: bash

    > pio org add platformio bob
    The new owner "bob" has been successfully added to the "platformio" organization.

See Also
--------

* :ref:`cmd_org_create`
* :ref:`cmd_org_list`
* :ref:`cmd_org_remove`
