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

.. _cmd_remote_agent:

PlatformIO Remote Agent
=======================

Start :ref:`cmd_remote_agent` on a host machine and work remotely with
your devices **WITHOUT** extra software, services, SSH, VPN, tunneling or
opening incoming network ports.

:ref:`pioremote` supports wired and wireless devices. Wired devices should be
connected physically to host machine where :ref:`cmd_remote_agent` is started,
where wireless devices should be visible for :ref:`cmd_remote_agent` to provide
network operations Over-The-Air (OTA).

.. contents::

.. _cmd_remote_agent_list:

pio remote agent list
---------------------

Usage
~~~~~

.. code::

    pio remote agent list


Description
~~~~~~~~~~~

List active :ref:`cmd_remote_agent` s started using own :ref:`pioaccount`
or shared with you by other PlatformIO developers.

Example
~~~~~~~

.. code::

    > pio remote agent list

    innomac.local
    -------------
    ID: 98853d930......788d77375e7
    Started: 2016-10-26 16:32:56

------------

.. _cmd_remote_agent_start:

pio remote agent start
----------------------

Usage
~~~~~

.. code-block:: bash

    pio remote agent start [OPTIONS]


Description
~~~~~~~~~~~

Start :ref:`cmd_remote_agent` and work remotely with your devices from
anywhere in the world. This command can be run as daemon or added to
autostart list of your OS.

Options
~~~~~~~

.. program:: pio remote agent start

.. option::
    -n, --name

Agent name/alias. By default, machine's ``hostname`` will be used.
You can use this name later for :ref:`cmd_remote_device` and :ref:`cmd_remote_run`
commands. Good names are home, office, lab or etc.

.. option::
    -s, --share

Share your agent/devices with other PlatformIO developers who have
:ref:`pioaccount`: friends, co-workers, team, etc.

The valid value for ``--share`` option is email address that was used for
:ref:`cmd_account_register` command.

.. option::
    -d, --working-dir

A working directory where :ref:`cmd_remote_agent` stores projects data for
incremental synchronization and embedded programs for PlatformIO Process Supervisor.
