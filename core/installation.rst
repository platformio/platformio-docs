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

.. |PIOCore| replace:: **PlatformIO Core**

.. _core_installation:

Installation
============

.. note::

    Please note that you do not need to install :ref:`piocore` if you are going
    to use :ref:`pioide`. :ref:`piocore` is built into
    PlatformIO IDE and you will be able to use it within PlatformIO IDE Terminal.

    If you need :ref:`piocore` outside PlatformIO IDE, please :ref:`piocore_install_shell_commands`.

|PIOCore| is written in `Python <https://www.python.org/downloads/>`_
and works on Windows, macOS, Linux, FreeBSD and *ARM*-based credit-card sized
computers (`Raspberry Pi <http://www.raspberrypi.org>`_,
`BeagleBone <http://beagleboard.org>`_, `CubieBoard <http://cubieboard.org>`_,
`Samsung ARTIK <https://www.artik.io>`_, etc.).

.. contents::
    :local:

System requirements
-------------------

:Operating System: Windows, macOS, Linux, FreeBSD, Linux ARMv6+
:Python Interpreter:

    **Python 3.6+ or above**. See detailed instruction on how to :ref:`faq_install_python`.

:Terminal Application:

    All commands below should be executed in
    `Command-line <http://en.wikipedia.org/wiki/Command-line_interface>`_
    application (Terminal). For macOS and Linux OS - *Terminal* application,
    for Windows OS – ``cmd.exe`` application.


:Access to Serial Ports (USB/UART):

    **Windows Users:** Please check that you have correctly installed USB
    driver from board manufacturer

    **Linux Users**:

    * Please install :ref:`faq_udev_rules`
    * Raspberry Pi users, please read this article
      `Enable serial port on Raspberry Pi <https://hallard.me/enable-serial-port-on-raspberry-pi/>`__.


Installation Methods
--------------------

Please *choose ONE of* the following methods:

.. contents::
    :local:

.. _installation_installer_script:

Installer Script
~~~~~~~~~~~~~~~~

.. warning::
    PlatformIO **DOES NOT** require administrative/sudo permissions. Please install using
    default user account **WITHOUT EXTRA PERMISSIONS**.

Super-Quick (Mac / Linux)
'''''''''''''''''''''''''

To install or upgrade |PIOCore| paste that at a *Terminal* prompt:

.. code-block:: bash

    python3 -c "$(curl -fsSL https://raw.githubusercontent.com/platformio/platformio/master/scripts/get-platformio.py)"

    # or using `curl`

    curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py -o get-platformio.py
    python3 get-platformio.py

    # or using `wget`

    wget https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py -O get-platformio.py
    python3 get-platformio.py


Local Download (Mac / Linux / Windows)
''''''''''''''''''''''''''''''''''''''

To install or upgrade *PlatformIO Core*, download (save as...)
`get-platformio.py <https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py>`_
script. Then run the following:

.. code-block:: bash

    # change directory to folder where is located downloaded "get-platformio.py"
    cd /path/to/dir/where/is/located/get-platformio.py/script

    # run it
    python get-platformio.py


On *Windows OS* it may look like:

.. code-block:: bash

    # change directory to folder where is located downloaded "get-platformio.py"
    cd C:\path\to\dir\where\is\located\script\get-platformio.py

    # run it
    python.exe get-platformio.py

.. note::
    If you need to have access to ``platformio`` or ``platformio.exe`` commands from
    other applications or terminal in your OS, please :ref:`piocore_install_shell_commands`.

Python Package Manager
~~~~~~~~~~~~~~~~~~~~~~

.. warning::
    We recommend using this method **ONLY FOR** :ref:`ci` use cases or where your have
    full permissions to install PlatformIO Core into the global scope of your OS.

    For personal using, and avoiding maintenance and upgrade issues, we
    **HIGHLY RECOMMEND** using :ref:`installation_installer_script` which installs
    |PIOCore| into an isolated virtual environment and does not affect your OS.

The latest stable version of |PIOCore| may be installed or upgraded via
Python Package Manager (`pip <https://pip.pypa.io>`_) as follows:

.. code-block:: bash

    pip install -U platformio

macOS Homebrew
~~~~~~~~~~~~~~

The latest stable version of PlatformIO may be installed or upgraded via
macOS Homebrew Packages Manager (`brew <http://brew.sh/>`_) as follows:

.. code-block:: bash

    brew install platformio

.. _installation_develop:

Development Version
-------------------

.. warning::
    If you use :ref:`pioide`, please enable development version:

    * :ref:`ide_atom`: "Menu PlatformIO: Settings > PlatformIO IDE > Use development
      version of PlatformIO Core"
    * :ref:`ide_vscode`: Set ``platformio-ide.useDevelopmentPIOCore`` to ``true`` in
      :ref:`ide_vscode_settings`.

Install the latest PlatformIO from the ``develop`` branch:

.. code-block:: bash

    # uninstall existing version
    pip uninstall platformio

    # install the latest development version of PlatformIO
    pip install -U https://github.com/platformio/platformio-core/archive/develop.zip

If you want to be up-to-date with the latest ``develop`` version of PlatformIO,
then you need to re-install PlatformIO each time you see a new commits in
`PlatformIO GitHub repository (branch: develop) <https://github.com/platformio/platformio-core/commits/develop>`_ like so:

.. code-block:: bash

    pip install -U https://github.com/platformio/platformio-core/archive/develop.zip

Or:

.. code-block:: bash

    pio upgrade --dev

To revert to the latest stable version:

.. code-block:: bash

    pip uninstall platformio
    pip install -U platformio

.. _piocore_install_shell_commands:

Install Shell Commands
----------------------

:ref:`piocore` consists of 2 standalone tools in a system:

* ``platformio`` or ``pio`` (short alias) - :ref:`piocore_userguide`
* ``piodebuggdb`` - alias of :ref:`cmd_debug`

If you have :ref:`pioide` already installed, you do not need to install
:ref:`piocore` separately. Just link these tools with your shell:

.. contents::
    :local:

Unix and Unix-like
~~~~~~~~~~~~~~~~~~

In Unix and Unix-like systems, there are multiple ways to achieve this.

Method 1
''''''''

You can export PlatformIO executables' directory to the PATH environmental
variable. This method will allow you to execute ``platformio`` commands from
any terminal emulator as long as you're logged in as the user PlatformIO is
installed and configured for.

If you use Bash as your default shell, you can do it by editing either
``~/.profile`` or ``~/.bash_profile`` and adding the following line:

.. code-block:: shell

    export PATH=$PATH:~/.platformio/penv/bin

If you use Zsh, you can either edit ``~/.zprofile`` and add the code above, or
for supporting both, Bash and Zsh, you can first edit ``~/.profile`` and add
the code above, then edit ``~/.zprofile`` and add the following line:

.. code-block:: shell

    emulate sh -c '. ~/.profile'

After everything's done, just restart your session (log out and log back in) and you're good to go.

If you don't know the difference between the two, check out `this page <https://serverfault.com/questions/261802/what-are-the-functional-differences-between-profile-bash-profile-and-bashrc>`_.

Method 2
''''''''

You can create system-wide symlinks. This method is not recommended if you have
multiple users on your computer because the symlinks will be broken for other users
and they will get errors while executing PlatformIO commands. If that's not a problem,
open your system terminal app and paste these commands
(**MAY require** administrator access ``sudo``):

.. code-block:: shell

    ln -s ~/.platformio/penv/bin/platformio /usr/local/bin/platformio
    ln -s ~/.platformio/penv/bin/pio /usr/local/bin/pio
    ln -s ~/.platformio/penv/bin/piodebuggdb /usr/local/bin/piodebuggdb

After that, you should be able to run PlatformIO from terminal. No restart is required.

Windows
~~~~~~~

Please read one of these instructions `How do I set or change the PATH system variable? <https://www.google.com.ua/search?q=how+do+i+set+or+change+the+path+system+variable>`_

You need to edit system environment variable called ``Path`` and append
``C:\Users\UserName\.platformio\penv\Scripts;`` path in the beginning of a
list (please replace ``UserName`` with your account name).


.. _piocore_uninstall:

Uninstall PlatformIO Core and dependent packages
------------------------------------------------

* Uninstall PlatformIO Core tool

    .. code-block:: bash

        # uninstall standalone PlatformIO Core installed via `pip`
        pip uninstall platformio

        # uninstall Homebrew's PlatformIO Core (only macOS users if you installed it via Homebrew before)
        brew uninstall platformio

* Dependent packages, global libraries are installed to :ref:`projectconf_pio_core_dir`
  folder (in user's HOME directory). Just remove it.

Integration with custom applications (extensions, plugins)
----------------------------------------------------------

We recommend using PlatformIO Core **Installer Script** when you integrate PlatformIO Core
into an application, such as extension or plugin for IDE. Examples that use this installer are:

- `platformio-node-helpers <https://github.com/platformio/platformio-node-helpers>`_,
  is used by `PlatformIO IDE for VSCode <https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide>`_
  and `PlatformIO IDE for Atom <https://atom.io/packages/platformio-ide>`_

Prerequisite
~~~~~~~~~~~~

Python Interpreter
''''''''''''''''''

PlatformIO Core Installer Script is written in Python and is compatible with Python 2.7+
and Python 3.5+. **We highly recommend using the latest Python 3**.

Python is installed by default on the most popular Unix OS (macOS, Linux, FreeBSD).
If there is no Python on a user machine (you can check running ``python --version``),
we have 2 options:

1. Ask the user to install Python 3 using our guide :ref:`faq_install_python`
2. You can automatically `Download Portable Python 3 <https://bintray.com/beta/#/platformio/dl-misc/python-portable?tab=files>`_
   and unpack it in a cache folder of your application. Later, you can use
   ``unpacked_protable_python_dir/python.exe``  for the installer script.

Installer Script
''''''''''''''''

There are 2 options on how to work with PlatformIO Core Installer Script:

1. Bundle `get-platformio.py <https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py>`_ file into your application
2. Download `get-platformio.py <https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py>`_ file on demand.

In both cases, you will need to have ``get-platformio.py`` script on the end-user machine.
You can copy or download it to a cache/temporary folder.

A list of arguments and options for the installer script is available via

.. code-block:: bash

    python get-platformio.py --help

Workflow
~~~~~~~~

We will describe a simple workflow on how to automatically install :ref:`piocore` for
end-user of your application/extension. We assume that ``get-platformio.py`` script
is already copied/downloaded and exists on the end-user machine. See above how to get it.

Step 1. Where is PlatformIO Core installed?
'''''''''''''''''''''''''''''''''''''''''''

You should check the PlatformIO Core installation state **each time** when the user
starts your application. You need to call the Installer Script with ``check core`` arguments:

.. code-block:: bash

    python get-platformio.py check core

This command returns ``0`` "exit code" when PlatformIO Core is already installed
and is ready for use, otherwise, the non-zero code of subprocess will be returned and
you need to install PlatformIO Core (see **Step #2** below).

If you need to have full information about PlatformIO Core installation state,
please run with ``--dump-state`` option and specify a folder or a full path where
to save data in JSON format:

.. code-block:: bash

    get-platformio.py check core --dump-state tmpdir/pioinstaller-state.json

Now, read JSON file and use ``platformio_exe`` binary to call PlatforIO Core using CLI
(see :ref:`piocore_userguide`). You can also export ``penv_bin_dir`` into system
environment ``PATH`` variable and ``platformio`` command will be available without
a full path.

Example of ``pioinstaller-state.json`` run on macOS:

.. code-block:: json

    {
      "cache_dir": "/Users/Freedom/.platformio/.cache",
      "core_dir": "/Users/Freedom/.platformio",
      "core_version": "4.3.1",
      "installer_version": "0.2.0",
      "is_develop_core": false,
      "penv_bin_dir": "/Users/Freedom/.platformio/penv/bin",
      "penv_dir": "/Users/Freedom/.platformio/penv",
      "platformio_exe": "/Users/Freedom/.platformio/penv/bin/platformio",
      "python_exe": "/Users/Freedom/.platformio/penv/bin/python",
      "system": "darwin_x86_64"
    }

Step 2. Install PlatformIO Core
'''''''''''''''''''''''''''''''

To install PlatformIO Core into the virtual environment in an automatic mode, please call
installer script without any arguments:

.. code-block:: bash

    python get-platformio.py

Available options:

- ``--verbose``, verbose output
- ``--dev``, install the latest development version of PlatformIO Core
- ``--ignore-python``, a path to Python to be ignored (multiple options and unix wildcards are allowed)

More options are available at ``python get-platformio.py --help``.

Installer Script will return exit code ``0`` on success, otherwise non-zero code and
error explanation.

Next time just use again ``python get-platformio.py check core`` as described in Step #1 (see above).

Troubleshooting
---------------

.. note::
    **Linux OS**: Don't forget to install "udev" rules file
    `99-platformio-udev.rules <https://github.com/platformio/platformio-core/blob/develop/scripts/99-platformio-udev.rules>`_ (an instruction is located in the file).

    **Windows OS**: Please check that you have correctly installed USB driver
    from board manufacturer

For further details, frequently questions, known issues, please
refer to :ref:`faq`.

If you find any issues with PlatformIO Core Installer Script, please report to
https://github.com/platformio/platformio-core-installer/issues
