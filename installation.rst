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

.. _installation:

Installation
============

.. note::

    Please note that you do not need to install :ref:`piocore` if you are going
    to use :ref:`pioide`. :ref:`piocore` is built into
    PlatformIO IDE and you will be able to use it within PlatformIO IDE Terminal.

    If you need :ref:`piocore` outside PlatformIO IDE, please :ref:`piocore_install_shell_commands`.

**PlatformIO Core** is written in `Python <https://www.python.org/downloads/>`_
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

    Python 2.7 or Python 3.5+.
    See detailed instruction how to :ref:`faq_install_python` for Windows.

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

Python Package Manager
~~~~~~~~~~~~~~~~~~~~~~

The latest stable version of PlatformIO may be installed or upgraded via
Python Package Manager (`pip <https://pip.pypa.io>`_) as follows:

.. code-block:: bash

    pip install -U platformio

If ``pip`` command is not available run ``easy_install pip`` or use
:ref:`installation_installer_script` which will install ``pip`` and
``platformio`` automatically.

Note that you may run into permissions issues running these commands. You have
a few options here:

* Run with ``sudo`` to install PlatformIO and dependencies globally
* Specify the `pip install --user <https://pip.pypa.io/en/stable/user_guide.html#user-installs>`_
  option to install local to your user
* Run the command in a `virtualenv <https://virtualenv.pypa.io>`_ local to a
  specific project working set.

.. _installation_installer_script:

Installer Script
~~~~~~~~~~~~~~~~

Super-Quick (Mac / Linux)
'''''''''''''''''''''''''

To install or upgrade *PlatformIO* paste that at a *Terminal* prompt
(**MAY require** administrator access ``sudo``):

.. code-block:: bash

    python -c "$(curl -fsSL https://raw.githubusercontent.com/platformio/platformio/develop/scripts/get-platformio.py)"


Local Download (Mac / Linux / Windows)
''''''''''''''''''''''''''''''''''''''

To install or upgrade *PlatformIO*, download (save as...)
`get-platformio.py <https://raw.githubusercontent.com/platformio/platformio/develop/scripts/get-platformio.py>`_
script. Then run the following (**MAY require** administrator access ``sudo``):

.. code-block:: bash

    # change directory to folder where is located downloaded "get-platformio.py"
    cd /path/to/dir/where/is/located/get-platformio.py/script

    # run it
    python get-platformio.py


On *Windows OS* it may look like:

.. code-block:: bash

    # change directory to folder where is located downloaded "get-platformio.py"
    cd C:\path\to\dir\where\is\located\get-platformio.py\script

    # run it
    C:\Python27\python.exe get-platformio.py


macOS Homebrew
~~~~~~~~~~~~~~

The latest stable version of PlatformIO may be installed or upgraded via
macOS Homebrew Packages Manager (`brew <http://brew.sh/>`_) as follows:

.. code-block:: bash

    brew install platformio

Full Guide
~~~~~~~~~~

1. Check a ``python`` version:

.. code-block:: bash

    python --version

If Python is not installed (command not found), please :ref:`faq_install_python`.

2. Install a ``platformio`` and related packages:

.. code-block:: bash

    pip install -U platformio

If your computer does not recognize ``pip`` command, try to install it first
using `these instructions <https://pip.pypa.io/en/latest/installing.html>`_.

For upgrading ``platformio`` to the latest version:

.. code-block:: bash

    pip install -U platformio


Virtual Environment
~~~~~~~~~~~~~~~~~~~

PlatformIO Core may be installed into isolated Python environment. This
method is very good if you don't want to install PlatformIO Core Python's
dependencies (packages) into your global system scope. :ref:`pioide` uses this
method to install PlatformIO Core.

Default and recommended environment folder is ":ref:`projectconf_pio_core_dir`/penv".
You can print **environment folder path** using the next command in your
system terminal:

.. code-block:: bash

    python -c "import os; print(os.path.join(os.getenv('PLATFORMIO_CORE_DIR', os.path.join(os.path.expanduser('~'), '.platformio')), 'penv'))"

    ######################## Examples
    # Windows
    # C:\Users\UserName\.platformio\penv

    # Linux
    # ~/.platformio/penv
    # /home/username/.platformio/penv

    # macOS
    # ~/.platformio/penv
    # /Users/username/.platformio/penv

Prerequisites
'''''''''''''

1.  Please remove existing PlatformIO Core **environment folder** if exists.
    See above command how to get path to environment folder.

2.  Please check that you have a valid Python interpreter running a next
    command in system terminal. Python 2.7.9+ or Python 3.5+ is recommended.

    .. code-block:: bash

        python --version

        # or, for Unix (Linux, Mac), you can use `python2` or `python3` aliases
        python2 --version
        python3 --version

    .. warning::
        **Windows Users**: If you already tried to install :ref:`pioide` and did
        not get success, please open system's Control Panel > Installed Programs,
        and check if PlatformIO IDE tried to install an own isolated Python 2.7
        version. Please uninstall it. Also is good to uninstall all Python
        interpreters from a system and install manually the latest Python
        using :ref:`faq_install_python` guide.

3.  Make sure ``virtualenv --help`` command exists in a system, otherwise,
    please install it manually using ``pip install virtualenv`` or
    ``pip2 install virtualenv`` command.

    If ``pip`` (Python Package Manager) does not exists, you have to install it
    manually. See https://pip.pypa.io/en/stable/installing/

Creating
''''''''

1.  Create a folder which contains all the necessary executables to use the
    packages that PIO Core would need using ``virtualenv`` command:

    .. code-block:: bash

        virtualenv /path/to/.platformio/penv

        # If you want to use a custom Python interpreter
        virtualenv --python=/path/to/custom/python /path/to/.platformio/penv

        # EXAMPLES
        # Windows
        virtualenv C:\Users\UserName\.platformio\penv
        virtualenv --python=C:\Python27\python.exe  C:\Users\UserName\.platformio\penv

        # Unix (Linux, Mac)
        virtualenv ~/.platformio/penv
        virtualenv -p python3 ~/.platformio/penv

2.  Activate virtual environment

    .. code-block:: bash

        # Windows
        C:\Users\UserName\.platformio\penv

        # Unix (Linux, Mac)
        source /path/to/.platformio/penv/bin/activate
        # or
        . /path/to/.platformio/penv/bin/activate

3.  Install PIO Core into virtual environment

    .. code-block:: bash

        pip install -U platformio

If you plan to use PIO Core commands outside virtual environment, please
:ref:`piocore_install_shell_commands`.

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
then you need to re-install PlatformIO each time if you see the new commits in
`PlatformIO GitHub repository (branch: develop) <https://github.com/platformio/platformio-core/commits/develop>`_.

To revert to the latest stable version

.. code-block:: bash

    pip uninstall platformio
    pip install -U platformio


.. _piocore_install_shell_commands:

Install Shell Commands
----------------------

:ref:`piocore` consists of 2 standalone tools in a system:

* ``platformio`` or ``pio`` (short alias) - :ref:`userguide`
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

Go to the *PlatformIO* menu → *Settings* → *PlatformIO IDE*, scroll down to the *Custom PATH for `platformio` command* and enter the following: ``~/.platformio/penv/bin``. After you've done that, you'll need to go to the *PlatformIO* menu → *Settings* → *PlatformIO IDE Terminal*, scroll down to the *Toggles* section and uncheck the *Login Shell* checkbox. Finally, restart your editor/IDE and check out the result.

Method 3
''''''''

You can create system-wide symlinks. This method is not recommended if you have multiple users on your computer because the symlinks will be broken for other users and they will get errors while executing PlatformIO commands. If that's not a problem, open your system terminal app and paste these commands (**MAY require** administrator access ``sudo``):

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

Uninstall PIO Core and dependent packages
-----------------------------------------

* Uninstall PIO Core tool

    .. code-block:: bash

        # uninstall standalone PIO Core installed via `pip`
        pip uninstall platformio

        # uninstall Homebrew's PIO Core (only macOS users if you installed it via Homebrew before)
        brew uninstall platformio

* Dependent packages, global libraries are installed to :ref:`projectconf_pio_core_dir`
  folder (in user's HOME directory). Just remove it.

Troubleshooting
---------------

.. note::
    **Linux OS**: Don't forget to install "udev" rules file
    `99-platformio-udev.rules <https://github.com/platformio/platformio-core/blob/develop/scripts/99-platformio-udev.rules>`_ (an instruction is located in the file).

    **Windows OS**: Please check that you have correctly installed USB driver
    from board manufacturer

For further details, frequently questions, known issues, please
refer to :ref:`faq`.
