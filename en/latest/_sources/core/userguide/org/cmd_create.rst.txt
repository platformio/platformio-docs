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

.. _cmd_org_create:

pio org create
==============

.. versionadded:: 5.0

.. contents::

Usage
-----

.. code-block:: bash

    pio org create [OPTIONS] ORGNAME

Description
-----------

Create a new organization.

Options
~~~~~~~

.. program:: pio org create

.. option::
    --email

An organization e-mail.

.. option::
    --displayname

An organization display name (company name).

Examples
--------

.. code-block:: bash

    > pio org create platformio --email contact@platformio.org --displayname PlatformIO
    The organization "platformio" has been successfully created.

See Also
--------

* :ref:`cmd_org_list`
* :ref:`cmd_org_remove`
