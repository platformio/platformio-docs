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

.. _cmd_org_remove:

pio org remove
==============

.. versionadded:: 5.0

.. contents::

Usage
-----

.. code-block:: bash

    pio org remove ORGNAME USERNAME

Description
-----------

Remove a user from an organization.

If you need to destroy an existing organization, please use :ref:`cmd_org_destroy` command.

Examples
--------

Remove Bob from "platformio" organization:

.. code-block:: bash

    > pio org remove platformio bob
    The `bob` owner has been successfully removed from the `platformio` organization.

See Also
--------

* :ref:`cmd_org_add`
* :ref:`cmd_org_list`
