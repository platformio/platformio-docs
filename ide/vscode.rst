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

    - 400+ embedded boards
    - 20+ development platforms
    - 10+ frameworks

* :ref:`debugging`
* :ref:`pio_remote`
* :ref:`unit_testing`
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
    are going to use :ref:`ide_vscode`. :ref:`core` is built into
    PlatformIO IDE and you will be able to use it within PlatformIO IDE Terminal.

- `Download <https://code.visualstudio.com>`_ and install official Microsoft
  Visual Studio Code, PlatformIO IDE is built on top of it
- Install `PlatformIO IDE for VSCode extension <https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide>`_.
  Launch VS Code Quick Open (Ctr+Shift+P or Cmd+Shift+P), paste the following
  command ``ext install platformio-ide``, and press enter
- Create empty directory and open it as a new project
- Please be patient and let the installation complete (only the first time, see progress in status bar).

Quick Start
-----------

This tutorial introduces you to the basics of PlatformIO IDE workflow and shows
you a creation process of a simple "Blink" example. After finishing you will
have a general understanding of how to work with projects in the IDE.

Launch
~~~~~~

After installation, you launch PlatformIO IDE by opening VSCode. Once VSCode is
opened, PlatformIO IDE auto installer will continue to install dependent packages
and :ref:`core`. Please be patient and let the installation complete. In the
final result PlatformIO IDE will ask you to reload VSCode window to apply
installed components. Please click on ``Reload Now``. After it PlatformIO IDE is
ready for using. Happy coding!

Setting Up the Project
~~~~~~~~~~~~~~~~~~~~~~

1. Create empty directory (or use existing) and open it as a new project

.. image:: ../_static/ide/vscode/platformio-ide-vscode-open-folder.png

2. Initialize PlatformIO Project using one of these methods:


    * Using :ref:`ide_vscode_toolbar` |pio_vscode_toolbar_new_project|
    * Launch "VS Code Menu: View > Command Palette..." or use hotkey ``Ctrl+Shift+P``
      (``Cmd+Shift+P`` for macOS), search for ``PlatformIO: Initialize or update project``, and press enter

.. |PIO_VSCODE_TOOLBAR_NEW_PROJECT| image:: ../_static/ide/vscode/platformio-ide-vscode-toolbar-new-project.png

3. Select a board. You can change it any time in :ref:`projectconf` or add
   new using the same ``PlatformIO: Initialize or update project``.

.. image:: ../_static/ide/vscode/platformio-ide-vscode-toolbar-select-board.png

4. Create New File named ``main.cpp`` in ``src`` folder

.. image:: ../_static/ide/vscode/platformio-ide-vscode-new-src-file.png

5. Copy the next source code to the just created file ``main.cpp``

    .. warning::

        The code below works only in pair with Arduino-based boards. Please
        follow to `PlatformIO Project Examples <https://github.com/platformio/platformio-examples>`_ repository for other pre-configured projects.

    .. code-block:: cpp

        /**
         * Blink
         *
         * Turns on an LED on for one second,
         * then off for one second, repeatedly.
         */
        #include "Arduino.h"

        // Set LED_BUILTIN if it is not defined by Arduino framework
        // #define LED_BUILTIN 13

        void setup()
        {
          // initialize LED digital pin as an output.
          pinMode(LED_BUILTIN, OUTPUT);
        }

        void loop()
        {
          // turn the LED on (HIGH is the voltage level)
          digitalWrite(LED_BUILTIN, HIGH);

          // wait for a second
          delay(1000);

          // turn the LED off by making the voltage LOW
          digitalWrite(LED_BUILTIN, LOW);

           // wait for a second
          delay(1000);
        }

6. Build your project with ``ctrl-shift-b`` (``cmd-shift-b``, for macOS) hotkey

.. image:: ../_static/ide/vscode/platformio-ide-vscode-build-project.png

7. Learn more about :ref:`ide_vscode_toolbar` and other commands (Upload, Clean,
   Serial Monitor, Library Manager, etc)

**Happy coding with PlatformIO!**


User Guide
----------

.. _ide_vscode_toolbar:

PlatformIO Toolbar
~~~~~~~~~~~~~~~~~~

PlatformIO IDE Toolbar is located in VSCode Status Bar (left corner)
and contains quick access buttons for the popular commands.
Each button contains hint (delay mouse on it).

.. image:: ../_static/ide/vscode/platformio-ide-vscode-toolbar.png

* PlatformIO: Build
* PlatformIO: Upload
* PlatformIO: Clean
* PlatformIO: Run Tasks
* Initialize new PlatformIO Project or update existing...
* Library Manager
* Serial Monitor
* Terminal

Building / Uploading / Tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``cmd-shift-b`` / ``ctrl-shift-b`` builds project without auto-uploading
* ``cmd-shift-d`` / ``ctrl-shift-d`` debug project
* ``cmd-shift-p`` / ``ctrl-shift-p`` type ``run`` and select "Tasks: Run Task"
