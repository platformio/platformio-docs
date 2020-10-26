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

.. _cmd_account_update:

pio account update
==================

.. contents::

Usage
-----

.. code-block:: bash

    pio account update [OPTIONS]

Description
-----------

Update :ref:`pioaccount` profile.

Options
~~~~~~~

You can omit these options and enter them later in update Wizard.

.. program:: pio account register

.. option::
    --username, -u

A username that must contain at least 4 characters including single hyphens, and cannot
begin or end with a hyphen.

.. option::
    --email, -e

An email. Please enter existing email, you will receive a confirmation letter.

.. option::
    --firstname

A first name.

.. option::
    --lastname

A last name.

.. option::
    --current-password

A current password to confirm this operation.
