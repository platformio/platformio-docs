..  Copyright 2014-present PlatformIO <contact@platformio.org>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _cmd_account:

PIO Account
===========

Having **PIO Account** allows you to use extra professional features from
`PlatformIO Plus <https://pioplus.com/>`__:

* :ref:`pio_remote`
* :ref:`debugging`
* :ref:`unit_testing`
* :ref:`ide_cloud`

A registration is **FREE**. Please open :ref:`pioide` Terminal and type:

.. code::

    # Create PIO Account
    pio account register

    # Login with credentials (will be sent to your e-mail)
    pio account login

    # Change temporary password (from e-mail) to permanent
    pio account password

To print all available commands and options use:

.. code-block:: bash

    pio account --help
    platformio account --help
    platformio account COMMAND --help


.. toctree::
    :maxdepth: 2

    cmd_forgot
    cmd_login
    cmd_logout
    cmd_password
    cmd_register
    cmd_show
    cmd_token
