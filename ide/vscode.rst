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

.. _ide_vscode:

PlatformIO IDE for VScode
=========================

PlatformIO IDE is the next-generation integrated development environment for IoT:

* Cross-platform build system without external dependencies to the OS software:

    - 350+ embedded boards
    - 20+ development platforms
    - 10+ frameworks

* :ref:`debugging`
* C/C++ Intelligent Code Completion
* C/C++ Smart Code Linter for rapid professional development
* Library Manager for the hundreds popular libraries
* Multi-projects workflow with multiple panes
* Themes support with dark and light colors
* Serial Port Monitor
* Built-in Terminal with :ref:`core` and CLI tool (``pio``, ``platformio``)

`Visual Studio Code <https://code.visualstudio.com>`_ is a lightweight but
powerful source code editor which runs on your desktop and is available for
Windows, macOS and Linux. It comes with built-in support for JavaScript,
TypeScript and Node.js and has a rich ecosystem of extensions for other
languages (such as C++, C#, Python, PHP, Go) and runtimes (such as .NET and Unity)

.. image:: ../_static/ide/vscode/platformio-ide-vscode.png
    :target: https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide

.. contents::

Installation
------------

.. note::

    Please note that you do not need to install :ref:`core` if you
    are going to use :ref:`ide_atom`. :ref:`core` is built into
    PlatformIO IDE and you will be able to use it within PlatformIO IDE Terminal.

- `Download <https://code.visualstudio.com>`_ and install official Microsoft
  Visual Studio Code, PlatformIO IDE is built on top of it
- Launch VS Code Quick Open (Ctr+P or Cmd+P), paste the following command ``ext install platformio-ide``, and press enter.
- Please be patient and let the installation complete.

Building / Uploading / Tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``cmd-shift-b`` / ``ctrl-shift-b`` builds project without auto-uploading.
* ``cmd-shift-p`` / ``ctrl-shift-p`` type ``run`` and select "Tasks: Run Task"
