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

VSCode
======

.. include:: pioide_features.rst

---------

**Visual Studio Code** is a lightweight but
powerful source code editor which runs on your desktop and is available for
Windows, macOS and Linux. It comes with built-in support for JavaScript,
TypeScript and Node.js and has a rich ecosystem of extensions for other
languages (such as C++, C#, Python, PHP, Go) and runtimes (such as .NET and Unity)

.. image:: ../../_static/images/ide/vscode/platformio-ide-vscode.png
    :target: ../../_images/platformio-ide-vscode.png

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
2. **Search** for the official ``platformio ide`` `extension <https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide>`_
3. **Install** PlatformIO IDE.

.. image:: ../../_static/images/ide/vscode/platformio-ide-vscode-pkg-installer.png

Quick Start
-----------

This tutorial introduces you to the basics of PlatformIO IDE workflow and shows
you a creation process of a simple "Blink" example. After finishing you will
have a general understanding of how to work with projects in the IDE.

Setting Up the Project
~~~~~~~~~~~~~~~~~~~~~~

1. Click on "PlatformIO Home" button on the bottom :ref:`ide_vscode_toolbar`

.. image:: ../../_static/images/ide/vscode/platformio-ide-vscode-welcome.png

2. Click on "New Project", select a board and create new PlatformIO Project

.. image:: ../../_static/images/ide/vscode/platformio-ide-vscode-new-project.png

3. Open ``main.cpp`` file form ``src`` folder and replace its contents with
   the next:

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

.. image:: ../../_static/images/ide/vscode/platformio-ide-vscode-blink-project.png

4. Build your project with ``ctrl+alt+b`` hotkey (see all Key Bindings in
   "User Guide" section below) or using "Build" button on the :ref:`ide_vscode_toolbar`

.. image:: ../../_static/images/ide/vscode/platformio-ide-vscode-build-project.png


---------------

Further for reading:

* :ref:`tutorials` (step-by-step tutorials with debugging and unit testing)
* Learn more about :ref:`ide_vscode_toolbar` and other commands (Upload,
  Clean, Serial Monitor) below.

**Happy coding with PlatformIO!**

.. _ide_vscode_toolbar:

PlatformIO Toolbar
------------------

PlatformIO IDE Toolbar is located in VSCode Status Bar (left corner)
and contains quick access buttons for the popular commands.
Each button contains hint (delay mouse on it).

.. image:: ../../_static/images/ide/vscode/platformio-ide-vscode-toolbar.png

1. :ref:`piohome`
2. PlatformIO: Build
3. PlatformIO: Upload
4. PlatformIO: Clean
5. :ref:`Serial Port Monitor <cmd_device_monitor>`
6. :ref:`piocore`
7. Project environment switcher (if more than one environment is available).
   See :ref:`projectconf_section_env` of :ref:`projectconf` .

PlatformIO Core (CLI)
---------------------

There are 2 ways how to access :ref:`piocore`:

1. "Terminal" icon on the :ref:`ide_vscode_toolbar`
2. Left Activity Bar > PlatformIO (ant icon) > Quick Access > Miscellaneous > PlatformIO Core CLI

.. image:: ../../_static/images/ide/vscode/platformio-ide-vscode-cli-access.png


Project Tasks
-------------

Task Explorer
~~~~~~~~~~~~~

PlatformIO provides access to "Project Task" where you can control
the build process of the environments declared in :ref:`projectconf`.
Project Task Explorer is located in the VSCode Activity Bar under the branded
PlatformIO icon. You can also access it via "VSCode Menu > Open View... >
PlatformIO".

.. hint::
  Please note that you can drag/move "Project Task" into to the another view within
  VSCode, such as "Explorer".

.. image:: ../../_static/images/ide/vscode/platformio-ide-vscode-task-explorer.png

Task Runner
~~~~~~~~~~~

PlatformIO IDE provides built-in tasks through the menu ``Terminal > Run Task...`` (Build,
Upload, Clean, Monitor, etc) and custom tasks per :ref:`projectconf` environment
(``[env:***]``). The default behavior is to use Terminal Panels for presentation,
one panel dedicated to each unique task.

The PlatformIO IDE provides its own Problems Matcher named ``$platformio``.
You can use it later if you decide to change base task settings.

You can override existing tasks with your own presentation options. For example,
let's configure PlatformIO Task Runner to use a NEW Terminal panel for each "Build"
command:

1. The menu item ``Terminal > Run Task...`` opens up a list of VSCode
   tasks for PlatformIO. In the line ``PlatformIO: Build``, press the
   gear icon on the far right side of the list. This creates or opens
   the file ``.vscode/tasks.json`` with some template code.

2. Replace the template in ``tasks.json`` with this code

  .. code-block:: json

    {
        "version": "2.0.0",
        "tasks": [
            {
                "type": "PlatformIO",
                "task": "Monitor",
                "problemMatcher": [
                    "$platformio"
                ],
                "presentation": {
                    "panel": "new"
                }
            }
        ]
    }

See more options in the `official VSCode documentation <https://code.visualstudio.com/docs/editor/tasks#_output-behavior>`__.

.. _ide_vscode_custom_task:

Custom Tasks
~~~~~~~~~~~~

Custom tasks can be added to ``tasks.json`` file located in the ``.vscode`` folder
in the root of project. Please read the official documentation `Tasks in VSCode <https://code.visualstudio.com/docs/editor/tasks#vscode>`_.

This simple example demonstrates a custom monitor task which echoes input locally.
There are a lot of other commands, please read more about :ref:`piocore` and
its commands (:ref:`piocore_userguide`).

.. code-block:: json

    {
        "version": "2.0.0",
        "tasks": [
            {
                "type": "shell",
                "command": "platformio",
                "args": [
                    "device",
                    "monitor",
                    "--echo"
                ],
                "problemMatcher": [
                    "$platformio"
                ],
                "label": "PlatformIO: Monitor (local echo)"
            }
        ]
    }

If the ``platformio`` executable file is not in your system environment "PATH", you
can provide the full path to the binary folder using the ``options`` field for the task. For example,
if the ``platformio`` binary is located in the home folder "~/.platformio/penv/bin":

.. code-block:: json

    {
        "version": "2.0.0",
        "tasks": [
            {
                "type": "shell",
                "command": "platformio",
                "args": [
                    "device",
                    "monitor",
                    "--echo"
                ],
                "problemMatcher": [
                    "$platformio"
                ],
                "label": "PlatformIO: Monitor (local echo)",
                "options": {
                    "env": {"PATH": "${env:HOME}/.platformio/penv/bin"}
                }
            }
        ]
    }

Multi-project Workspaces
------------------------

You can work with multiple project folders in Visual Studio Code with
multi-root workspaces. This can be very helpful when you are working on
several related projects at the same time. Read more in the documentation
`Multi-root Workspaces <https://code.visualstudio.com/docs/editor/multi-root-workspaces>`_.

Serial Port Monitor
-------------------

You can customize Serial Port Monitor using
:ref:`projectconf_section_env_monitor` in :ref:`projectconf`:

* :ref:`projectconf_monitor_port`
* :ref:`projectconf_monitor_speed`
* :ref:`projectconf_monitor_rts`
* :ref:`projectconf_monitor_dtr`
* :ref:`projectconf_monitor_flags`

Example:

.. code-block:: ini

    [env:esp32dev]
    platform = espressif32
    framework = arduino
    board = esp32dev

    ; Custom Serial Monitor port
    monitor_port = /dev/ttyUSB1

    ; Custom Serial Monitor speed (baud rate)
    monitor_speed = 115200

Debugging
---------

Debugging in VSCode works in combination with :ref:`piodebug`. You should
have :ref:`pioaccount` to work with it.

VSCode has a separate activity view named "Debug" (accessed by the bug icon on the left toolbar).
:ref:`piodebug` extends it with more advanced debugging instruments and features:

- Local, Global, and Static Variable Explorer
- Conditional Breakpoints
- Expressions and Watchpoints
- Generic Registers
- Peripheral Registers
- Memory Viewer
- Disassembly
- Multi-thread support
- A hot restart of an active debugging session.

There are two pre-configured debugging configurations:

:PIO Debug:
  **Default configuration**. PlatformIO runs the **Pre-Debug** task and builds
  the project using :ref:`Debug Configuration <build_configurations>`. Also, it
  checks for project changes.

:PIO Debug (skip Pre-Debug):
  PlatformIO skips the **Pre-Debug** stage and DOES NOT build or check the project for changes.
  If you do changes in project source files, they will not be reflected in
  debug sessions until you switch back to the "PIO Debug" configuration or
  manually run the "Pre-Debug" task.

  This configuration is very useful for quick debug session. It is super fast
  by skipping several checks, letting you control project changes manually.

.. note::
  Please note that :ref:`piodebug` will use the first declared build
  environment in :ref:`projectconf` if the :ref:`projectconf_pio_default_envs`
  option is not specified.

.. image:: ../../_static/images/ide/vscode/platformio-ide-vscode-debug.png

Variable Format
~~~~~~~~~~~~~~~

Currently, VSCode does not provide an UI or API to change the variable format. See the
related `VSCode Issue #28025 <https://github.com/Microsoft/vscode/issues/28025>`_.

A temporary solution is to set the default numerical base in which the
debugger displays numeric output in the Debug Console. (The Debug
Console is visible during active debugging sessions). For example, to
show variables in hexadecimal format, copy the code below and paste it
into "Debug Console":

.. code::

  set output-radix 16

Possible values, listed in decimal base, are: 8, 10, 16.

Watchpoints
~~~~~~~~~~~

Please read `GDB: Setting Watchpoints <https://sourceware.org/gdb/download/onlinedocs/gdb/Set-Watchpoints.html>`__
first.

Currently, VSCode does not provide an API to change the value format of watchpoints.
You can manually cast watchpoint expressions to display the value as specific pointer types:

* ``$pc``, default decimal integer format
* ``*0x10012000``, an address, default decimal integer format
* ``(void*)$pc``, $pc register, hexadecimal format
* ``*(void**)0x10012000``, an address, hexadecimal format

Install Shell Commands
----------------------

Please refer to PlatformIO Core :ref:`piocore_install_shell_commands`.

Proxy Server Support
--------------------

There are two options how to configure a proxy server:

1. Declare the ``HTTP_PROXY`` and ``HTTPS_PROXY`` system environment variables
   (for example ``HTTP_PROXY=http://user:pass@10.10.1.10:3128/``, etc.)
2. Open `VSCode Settings <https://code.visualstudio.com/docs/getstarted/settings>`__
   and search for "Proxy". Please set "Http: Proxy" and disable
   "Http: Proxy Strict SSL".

.. _ide_vscode_keybindings:

Key Bindings
------------

* ``ctrl+alt+b`` / ``cmd-shift-b`` / ``ctrl-shift-b`` Build Project
* ``cmd-shift-d`` / ``ctrl-shift-d`` Debug project
* ``ctrl+alt+u`` Upload Firmware
* ``ctrl+alt+s`` Open :ref:`Serial Port Monitor <cmd_device_monitor>`

You can override existing key bindings  or add a new in VSCode. See official
documentation `Key Bindings for Visual Studio Code <https://code.visualstudio.com/docs/getstarted/keybindings>`_.

.. _ide_vscode_settings:

Settings
--------

`How to configure VSCode settings? <https://code.visualstudio.com/docs/getstarted/settings>`__

``platformio-ide.activateOnlyOnPlatformIOProject``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If true, activate the ``platformio ide`` extension only when a
PlatformIO-based project (that has a :ref:`projectconf`) is open in the
workspace. The default value is ``false``.

``platformio-ide.autoCloseSerialMonitor``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If true, automatically close :ref:`cmd_device_monitor` before uploading/testing.
The default value is ``true``.

``platformio-ide.autoRebuildAutocompleteIndex``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If true, automatically rebuild the C/C++ Project Index when :ref:`projectconf`
is changed or when new libraries are installed. The default value is ``true``.

``platformio-ide.buildTask``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The build task (label) that is launched by the "Build" button in the
:ref:`ide_vscode_toolbar` and :ref:`ide_vscode_keybindings`. The default is ``PlatformIO: Build``.

You can create custom :ref:`ide_vscode_custom_task` and assign one of them to ``platformio-ide.buildTask``.

``platformio-ide.autoPreloadEnvTasks``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Automatically preload ALL project environment tasks. The default value is ``false``.

``platformio-ide.customPATH``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Custom PATH for the ``platformio`` command. Paste here the result of ``echo $PATH``
(Unix) / ``echo %PATH%`` (Windows) command by typing into your system terminal
if you prefer to use a custom version of :ref:`piocore`. The default value is ``null``, meaning PlatformIO looks for the ``platformio`` command in the system path.

``platformio-ide.disableToolbar``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Disable the PlatformIO toolbar. The default value is ``false``.

``platformio-ide.forceUploadAndMonitor``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If true, the Upload (``platformio-ide.upload``) command is changed to
use the "Upload and Monitor" task. The default value is ``false``.

``platformio-ide.reopenSerialMonitorDelay``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Configure the time in milliseconds before reopening the Serial Port Monitor.
The default value is ``0``, which means to reopen instantly.

``platformio-ide.useBuiltinPython``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Use a portable Python 3 Interpreter if available. The default value is ``true``.

``platformio-ide.useBuiltinPIOCore``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If true, use the built-in :ref:`piocore`. The default value is ``true``.

``platformio-ide.useDevelopmentPIOCore``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If true, use the development version of :ref:`piocore`. The default
value is ``false``.

``platformio-ide.disablePIOHomeStartup``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Disable showing PlatformIO Home at startup. The default value is ``false``.

``platformio-ide.pioHomeServerHttpPort``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PlatformIO Home server HTTP port. The default value ``0`` automatically assigns a free port in
the range [8010..8100]).

Known issues
------------

PackageManager is unable to install tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a known bug in VSCode Terminal
`issue #61 <https://github.com/platformio/platformio-vscode-ide/issues/61>`_.

A temporary solution is to install packages using a system terminal (not VSCode Terminal).
Please use "Solution 3: Run from Terminal" in FAQ > Package Manager >
:ref:`faq_package_manager_error_5`.
Afterwards, go back to using the VSCode Terminal.

Changelog
---------

Please visit the `releases page <https://github.com/platformio/platformio-vscode-ide/releases>`_.
