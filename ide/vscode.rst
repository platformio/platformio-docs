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

.. _ide_vscode:

PlatformIO IDE for VScode
=========================

.. include:: pioide_features.rst

---------

`Visual Studio Code <https://code.visualstudio.com>`_ is a lightweight but
powerful source code editor which runs on your desktop and is available for
Windows, macOS and Linux. It comes with built-in support for JavaScript,
TypeScript and Node.js and has a rich ecosystem of extensions for other
languages (such as C++, C#, Python, PHP, Go) and runtimes (such as .NET and Unity)

.. image:: ../_static/ide/vscode/platformio-ide-vscode.png
    :target: ../_images/platformio-ide-vscode.png

.. contents:: Contents
    :local:

Installation
------------

.. note::

    Please note that you do not need to install :ref:`piocore` separately if
    you are going to use :ref:`ide_vscode`. :ref:`piocore` is built into
    PlatformIO IDE and you will be able to use it within PlatformIO IDE Terminal.

0. `Download <https://code.visualstudio.com>`_ and install official Microsoft Visual Studio Code. PlatformIO IDE is built on top of it
1. **Open** VSCode Package Manager
2. **Search** for official ``platformio-ide`` `extension <https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide>`_
3. **Install** PlatformIO IDE.

.. image:: ../_static/ide/vscode/platformio-ide-vscode-pkg-installer.png

Quick Start
-----------

This tutorial introduces you to the basics of PlatformIO IDE workflow and shows
you a creation process of a simple "Blink" example. After finishing you will
have a general understanding of how to work with projects in the IDE.

Setting Up the Project
~~~~~~~~~~~~~~~~~~~~~~

1. Click on "PlatformIO Home" button on the bottom :ref:`ide_vscode_toolbar`

.. image:: ../_static/ide/vscode/platformio-ide-vscode-welcome.png

2. Click on "New Project", select a board and create a new PlatformIO Project

.. image:: ../_static/ide/vscode/platformio-ide-vscode-new-project.png

3. Open ``main.cpp`` file form ``src`` folder and replace its contents with
   the next:

.. warning::

    The code below works only in pair with Arduino-based boards. Please
    follow to `PlatformIO Project Examples <https://github.com/platformio/platformio-examples>`_ repository for other pre-configured projects.


.. image:: ../_static/ide/vscode/platformio-ide-vscode-blink-project.png

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

4. Build your project with ``ctrl+alt+b`` hotkey (see all Key Bindings in
   "User Guide" section below) or using "Build" button on the :ref:`ide_vscode_toolbar`

.. image:: ../_static/ide/vscode/platformio-ide-vscode-build-project.png


Learn more about :ref:`ide_vscode_toolbar` and other commands (Upload, Clean,
Serial Monitor) below.

**Happy coding with PlatformIO!**


.. _ide_vscode_toolbar:

PlatformIO Toolbar
------------------

PlatformIO IDE Toolbar is located in VSCode Status Bar (left corner)
and contains quick access buttons for the popular commands.
Each button contains hint (delay mouse on it).

.. image:: ../_static/ide/vscode/platformio-ide-vscode-toolbar.png

* PlatformIO: Home (:ref:`pioaccount`, library and platform managers, board explorer,
  and many more...)
* PlatformIO: Build
* PlatformIO: Upload
* PlatformIO: Clean
* Run a task... (See "Task Runner" below)
* :ref:`Serial Port Monitor <cmd_device_monitor>`
* PIO Terminal

Key Bindings
------------

* ``ctrl+alt+i`` Initialize or Update Project
* ``ctrl+alt+b`` / ``cmd-shift-b`` / ``ctrl-shift-b`` Build Project
* ``cmd-shift-d`` / ``ctrl-shift-d`` Debug project
* ``ctrl+alt+u`` Upload Firmware
* ``ctrl+alt+s`` Open :ref:`Serial Port Monitor <cmd_device_monitor>`

Task Runner
-----------

PlatformIO IDE provides base tasks ``Menu > Tasks`` (Build, Upload, Clean,
Monitor, etc) and custom tasks per :ref:`projectconf` environment
(``[env:***]``). A default behavior is to use Terminal Panel for presentation.
Also, we use dedicated panel per unique task.

PlatformIO IDE provides own Problems Matcher named ``$platformio``.
You can use it later if decide to change base task settings.

You can override existing task with own presentation options. For example,
let configure PlatformIO Task Runner to use NEW Terminal panel per each "Build"
command:

1. Please click on "gear" icon near "Build" task in ``Menu > Tasks``
2. Replace template in ``tasks.json`` with this code

  .. code-block:: json

    {
        "version": "2.0.0",
        "tasks": [
            {
                "type": "PlatformIO",
                "args": [
                    "run"
                ],
                "problemMatcher": [
                    "$platformio"
                ],
                "presentation": {
                    "panel": "new"
                }
            }
        ]
    }

See more options in `official VSCode documentation <https://code.visualstudio.com/docs/editor/tasks#_output-behavior>`__.

Serial Port Monitor
-------------------

You can customize Serial Port Monitor using
:ref:`projectconf_section_env_monitor` in :ref:`projectconf`:

* :ref:`projectconf_monitor_port`
* :ref:`projectconf_monitor_baud`
* :ref:`projectconf_monitor_rts`
* :ref:`projectconf_monitor_dtr`

Example:

.. code-block:: ini

    [env:esp32dev]
    platform = espressif32
    framework = arduino
    board = esp32dev

    ; Custom Serial Monitor port
    monitor_port = /dev/ttyUSB1

    ; Custom Serial Monitor baud rate
    monitor_baud = 115200

Install Shell Commands
----------------------

Please navigate to FAQ :ref:`faq_install_shell_commands`.

Settings
--------

`How to configure VSCode settings? <https://code.visualstudio.com/docs/getstarted/settings>`_

``platformio-ide.useBuiltinPIOCore``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Use built-in :ref:`piocore`, default configuration is ``true``.

``platformio-ide.useDevelopmentPIOCore``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Use development version of :ref:`piocore`, default configuration is ``false``.

``platformio-ide.autoRebuildAutocompleteIndex``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Automatically rebuild C/C++ Project Index when :ref:`projectconf` is changed
or when new libraries are installed, default configuration is ``true``.

``platformio-ide.forceUploadAndMonitor``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Force "Upload and Monitor" task for Upload (``platformio-ide.upload``) command,
default configuration is ``false``.

``platformio-ide.customPATH``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Custom PATH for ``platformio`` command. Paste here the result of ``echo $PATH``
(Unix) / ``echo %PATH%`` (Windows) command by typing into your system terminal
if you prefer to use custom version of :ref:`piocore`, default configuration
is ``null``.


Changelog
---------

Please visit `releases page <https://github.com/platformio/platformio-vscode-ide/releases>`_.
