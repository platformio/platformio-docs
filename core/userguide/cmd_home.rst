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

.. _cmd_home:

pio home
========

Helper command for :ref:`piohome`.

.. contents::

Usage
-----

.. code-block:: bash

    pio home

Description
-----------

Launch :ref:`piohome` Web-server.

Options
-------

.. program:: pio home

.. option::
    --port

Web-server HTTP port, default is ``8008``.

.. option::
    --host

Web-server HTTP host, default is ``127.0.0.1``.
You can open PlatformIO Home for inbound connections using host ``0.0.0.0``.

.. option::
    --no-open

Do not automatically open PlatformIO Home in a system Web-browser.

.. option::
    --shutdown-timeout

Automatically shutdown server on timeout (in seconds) when no clients are connected.
Default is ``0`` which means never auto shutdown.

Examples
--------

.. code::

    > pio home

      ___I_
     /\-_--\   PlatformIO Home
    /  \_-__\
    |[]| [] |  http://127.0.0.1:8008
    |__|____|_______________________

    Open PlatformIO Home in your browser by this URL => http://127.0.0.1:8008
    PlatformIO Home has been started. Press Ctrl+C to shutdown.
