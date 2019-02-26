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

.. _ide_cloud9:

Cloud9
======

`Cloud9 <https://c9.io/>`_ combines a powerful online code editor with a full
Ubuntu workspace in the cloud.
Workspaces are powered by Docker Ubuntu containers that give you full freedom
over your environment, including sudo rights. Do a git push, compile SASS, see
server output, and Run apps easily with the built-in Terminal and Runners.

.. contents::

.. note::

    1. Please make sure to read :ref:`pioremote` guide first.
    2. You need :ref:`pioaccount` if you don't have it. Registration is FREE.
    3. You should have a running :ref:`cmd_remote_agent` on a remote machine
       where hardware devices are connected physically or accessible for the
       remote operations. See **PIO Remote** :ref:`pio_remote_quickstart` for details.

Demo
----

.. image:: ../_static/images/ide/cloud9/ide-cloud9-demo.jpg
    :target: https://www.youtube.com/watch?v=NX56_0Ea_K8

Integration
-----------

1.  `Sign in to Cloud9 <https://c9.io/dashboard.html>`_. A registration is FREE
    and gives you for FREE 1 private workspace (where you can host multiple
    PlatformIO Projects) and unlimited public workspaces.

2.  Create a new workspace using **Blank** template

.. image:: ../_static/images/ide/cloud9/ide-cloud9-new-workspace.png

3. Install :ref:`piocore` using Cloud IDE Terminal. Paste a next command

.. code-block:: bash

    sudo python -c "$(curl -fsSL https://raw.githubusercontent.com/platformio/platformio/develop/scripts/get-platformio.py)"

.. image:: ../_static/images/ide/cloud9/ide-cloud9-install-pio-cli.png

4.  Log in to :ref:`pioaccount` using :ref:`cmd_account_login` command.


Quick Start
-----------

Let's create our first PlatformIO-based Cloud9 Project

1.  Initialize new PlatformIO-based Project. Run a next command in Cloud IDE
    Terminal:

    .. code-block:: bash

        platformio init --board <ID>

        # initialize project for Arduino Uno
        platformio init --board uno

    To get board ``ID`` please use :ref:`cmd_boards` command or
    `Embedded Boards Explorer <https://platformio.org/boards>`_.

2.  Create new source file named ``main.cpp`` in ``src`` folder using
    Project Tree (left side). Please make right click on ``src`` folder,
    then "New File" and insert a next content:

    .. code-block:: c

        #include <Arduino.h>

        int i = 0;

        void setup() {
            Serial.begin(9600);
            Serial.println("Hello Cloud9!");
        }

        void loop() {
            /*  serial echo */
            while (Serial.available()) {
                Serial.write(Serial.read());
            }

            i++;
            Serial.println(i);
            delay(100);
        }

.. image:: ../_static/images/ide/cloud9/ide-cloud9-init-project.png

3.  If you prefer to work with :ref:`piocore` CLI, then you can process project
    using Cloud IDE Terminal and the next commands:

    * :ref:`cmd_run` - build project locally (using Cloud IDE's virtual machine)
    * :ref:`pio run -t clean <cmd_run>` - clean project
    * :ref:`pio remote run -t upload <cmd_remote_run>` - upload firmware (program) to a remote device
    * :ref:`cmd_remote_device_list` - list available remote devices
    * :ref:`cmd_remote_device_monitor` - Remote Serial Port Monitor

    If you are interested in better integration with Cloud9 and GUI, please
    read guide below where we will explain how to create custom Build System
    for PlatformIO and own Runners.

PlatformIO Build System
-----------------------

Cloud9 allows one to create own build system and use hotkey or command
(Menu: Run > Build) to build a project.

Let's create PlatformIO Build System that will be used for C/C++/H/INO/PDE
files by default. Please click on ``Menu: Run > Build System > New Build System``
and replace all content with the next:

.. code-block:: js

    {
        "cmd" : ["pio", "run", "-d", "$file"],
        "info" : "Building $project_path/$file_name",
        "selector": "^.*\\.(cpp|c|h|hpp|S|ini|ino|pde)$"
    }

Save new Build System and give a name ``PIOBuilder``. Now, you can select it
as default Build System using ``Menu: Run > Build System > PIOBuilder``.

Remote Device Manager
---------------------

Remote Device Manager works in pair with :ref:`pioremote`.
You can list remote devices that are connected to host machine where
:ref:`cmd_remote_agent` is started or are visible for it.

Let's create New Run Configuration (shortcut) that will be used for Remote Device Manager.
Please click on ``Menu: Run > Run Configurations > Manage...``, then
"Add New Config" and specify the next values:

* **First Blank Input**: a name of runner. Please set it to "PIO: Remote Devices"
* **Command**: set to ``pio remote device list``
* **Runner**: set to "Shell command"

.. image:: ../_static/images/ide/cloud9/ide-cloud9-runner-ota-devices.png

.. _ide_cloud9_ota_updates:

Remote Firmware Uploading
-------------------------

Remote Firmware Uploading works in pair with :ref:`pioremote`.
You can deploy firmware (program) to any devices which are visible for :ref:`cmd_remote_agent`.

Let's create New Run Configuration (shortcut) that will be used for Remote Firmware Uploading.
Please click on ``Menu: Run > Run Configurations > Manage...``, then
"Add New Config" and specify the next values:

* **First Blank Input**: a name of runner. Please set it to "PIO: Remote Upload"
* **Command**: set to ``pio remote run -t upload``
* **Runner**: set to "Shell command"

.. image:: ../_static/images/ide/cloud9/ide-cloud9-runner-ota-uploading.png

Remote Serial Port Monitor
--------------------------

Remote Serial Port Monitor works in pair with :ref:`pioremote`.
You can read or send data to any device that is connected to host machine
where :ref:`cmd_remote_agent` is started.
To list active agents please use this command :ref:`cmd_remote_agent_list`.

Let's create New Run Configuration (shortcut) that will be used for Remote Serial Port Monitor.
Please click on ``Menu: Run > Run Configurations > Manage...``, then
"Add New Config" and specify the next values:

* **First Blank Input**: a name of runner. Please set it to "PIO: Remote Serial Monitor"
* **Command**: set to ``pio remote device monitor``
* **Runner**: set to "Shell command"

.. image:: ../_static/images/ide/cloud9/ide-cloud9-runner-ota-serial-monitor.png

Multi-Project workspace
-----------------------

You can have multiple PlatformIO-based Projects in the same workspace. We
recommend a next folders structure:

.. code::

    ├── project-A
    │   ├── lib
    │   │   └── README
    │   ├── platformio.ini
    │   └── src
    │       └── main.ino
    └── project-B
        ├── lib
        │   └── README
        ├── platformio.ini
        └── src
            ├── main.cpp
            └── main.h

In this case, you need to create 2 "New Run Configuration" for
:ref:`ide_cloud9_ota_updates` with using the next **commands**:

* ``pio remote run --project-dir project-A -t upload`` for Project-A
* ``pio remote run -d project-B -t upload`` for Project-B

See documentation for :option:`platformio remote run --project-dir` option.