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

.. _faq:

Frequently Asked Questions
==========================

.. note::
   We have a big database with `Frequently Asked Questions in our Community Forums <https://community.platformio.org/c/faq>`_.
   Please have a look at it.

.. contents:: Contents
    :local:

General
-------

What is PlatformIO?
~~~~~~~~~~~~~~~~~~~

Please refer to :ref:`what_is_pio`

What is ``.pioenvs`` directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please refer to :ref:`projectconf_pio_build_dir`.

Command completion in Terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bash completion
'''''''''''''''

Bash completion support will complete subcommands and parameters. To enable
Bash completion for `platformio` subcommands you need to put into your `.bashrc`:

.. code-block:: bash

    eval "$(_PLATFORMIO_COMPLETE=source platformio)"
    eval "$(_PLATFORMIO_COMPLETE=source pio)"

ZSH completion
''''''''''''''

To enable ``zsh`` completion please run these commands:

.. code-block:: bash

    autoload bashcompinit && bashcompinit
    eval "$(_PLATFORMIO_COMPLETE=source platformio)"
    eval "$(_PLATFORMIO_COMPLETE=source pio)"

.. note::

    For permanent command completion you need to place commands above to
    ``~/.bashrc`` or ``~/.zshrc`` file.

Install Python Interpreter
--------------------------

:ref:`piocore` is written in `Python <https://www.python.org/downloads/>`_ that
is installed by default on the all popular OS except Windows.

**Windows Users**, please `Download the latest Python 2.7.x <https://www.python.org/downloads/>`_
and install it. **DON'T FORGET** to select ``Add python.exe to Path`` feature
on the "Customize" stage, otherwise ``python`` command will not be available.

.. image:: _static/python-installer-add-path.png


.. _faq_install_shell_commands:

Install PlatformIO Core Shell Commands
--------------------------------------

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

You can add PlatformIO executables' directory to the PATH environmental variable. This method will allow you to execute ``platformio`` commands from any terminal emulator as long as you're logged in as the user PlatformIO is installed and configured for.

If you use Bash as your default shell, you can do it by editing either ``~/.profile`` or ``~/.bash_profile`` and adding the following line:

.. code-block:: shell

    export PATH=$PATH:~/.platformio/penv/bin

If you use Zsh, you can either edit ``~/.zprofile`` and add the code above, or for supporting both, Bash and Zsh, you can first edit ``~/.profile`` and add the code above, then edit ``~/.zprofile`` and add the following line:

.. code-block:: shell

    emulate sh -c '. ~/.profile'

After everithing's done, just restart your session (log out and log back in) and you're good to go.

If you don't know the difference between the two, check out `this page <https://serverfault.com/questions/261802/what-are-the-functional-differences-between-profile-bash-profile-and-bashrc>`_.

Method 2
''''''''

Go to the *PlatformIO* menu → *Settings* → *PlatformIO IDE*, scroll down to the *Custom PATH for `platformio` command* and enter the following: ``~/.platformio/penv/bin``. After you've done that, you'll need to go to the *PlatformIO* menu → *Settings* → *PlatformIO IDE Terminal*, scroll down to the *Toggles* section and uncheck the *Login Shell* checkbox. Finally, restart Atom and check out the result.

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
``C:\Users\{username}\.platformio\penv\Scripts;`` path in the beginning of a
list (please replace ``{username}`` with your account name).

.. _faq_convert_ino_to_cpp:

Convert Arduino file to C++ manually
------------------------------------

Some :ref:`ide` doesn't support Arduino files (``*.ino`` and ``.pde``) because
they are not valid C/C++ based source files:

1. Missing includes such as ``#include <Arduino.h>``
2. Function declarations are omitted.

In this case, code completion and code linting does not work properly or
disabled. To avoid this issue you can manually convert your INO files to CPP.

For example, we have the next ``Demo.ino`` file:

.. code-block:: cpp

    void setup () {
        someFunction(13);
    }

    void loop() {
        delay(1000);
    }

    void someFunction(int num) {
    }

Let's convert it to  ``Demo.cpp``:

1. Add ``#include <Arduino.h>`` at the top of the source file
2. Declare each custom function (excluding built-in, such as ``setup`` and ``loop``)
   before it will be called.

The final ``Demo.cpp``:

.. code-block:: cpp

    #include <Arduino.h>

    void someFunction(int num);

    void setup () {
        someFunction(13);
    }

    void loop() {
        delay(1000);
    }

    void someFunction(int num) {
    }


.. _faq_troubleshooting:

Troubleshooting
---------------

Installation
~~~~~~~~~~~~

Multiple PIO Cores in a system
''''''''''''''''''''''''''''''

Multiple standalone :ref:`piocore` in a system could lead to a different
issues. We highly recommend to keep one instance of PIO Core or use built-in
PIO Core in :ref:`pioide`:

* :ref:`ide_atom` - ``Menu PlatformIO: Settings > PlatformIO IDE > Use built-in PlatformIO Core``

Finally, if you have a standalone :ref:`piocore` in a system, please open system
Terminal (not PlatformIO IDE Terminal) and uninstall obsolete PIO Core:

.. code-block:: bash

    pip uninstall platformio

    # if you used MacOS "brew"
    brew uninstall platformio

If you need to have :ref:`piocore` globally in a system, please
:ref:`faq_install_shell_commands`.

'platformio' is not recognized as an internal or external command
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

If you use :ref:`pioide`, please check in PlatformIO IDE Settings that
"Use built-in PIO Core" is enabled.

If you modify system environment variable ``PATH`` in your Bash/Fish/ZSH
profile, please do not override global ``PATH``. This line
``export PATH="/my/custom/path"`` is incorrect. Use ``export PATH="/my/custom/path":$PATH``
instead.

[Errno 1] Operation not permitted
'''''''''''''''''''''''''''''''''

Answered in `issue #295 <https://github.com/platformio/platformio-core/issues/295#issuecomment-143772005>`_.

Windows AttributeError: 'module' object has no attribute 'packages'
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Answered in `issue #252 <https://github.com/platformio/platformio-core/issues/252#issuecomment-127072039>`_.

PlatformIO: command not found || An error "pkg_resources.DistributionNotFound"
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Please upgrade *SetupTools* package:

.. code-block:: bash

    [sudo] pip uninstall setuptools
    [sudo] pip install setuptools

    # Then re-install PlatformIO
    [sudo] pip uninstall platformio
    [sudo] pip install platformio


Package Manager
~~~~~~~~~~~~~~~

.. _faq_package_manager_error_5:

[Error 5] Access is denied
''''''''''''''''''''''''''

PlatformIO installs all packages to ":ref:`projectconf_pio_home_dir`/packages"
directory. You **MUST HAVE** write access for this folder.
Please note that **PlatformIO does not require** "sudo"/administrative privileges.

.. contents::
    :local:

Solution 1: Remove folder
^^^^^^^^^^^^^^^^^^^^^^^^^

A quick solution is to remove ":ref:`projectconf_pio_home_dir`/packages" folder
and repeat installation/building/uploading again.

Solution 2: Antivirus
^^^^^^^^^^^^^^^^^^^^^

Some antivirus tools forbid programs to create files in background.
PlatformIO Package Manager does all work in background: downloads package,
unpacks archive in temporary folder and moves final files to
":ref:`projectconf_pio_home_dir`/packages" folder.

Antivirus tool can block PlatformIO, that is why you see "[Error 5] Access is denied".
Try to **disable it for a while** or add :ref:`projectconf_pio_home_dir`
directory to exclusion/white list.

Solution 3: Run from Terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As we mentioned in "Solution 2", antivirus tools can block background file
system operations. Other solution is to run :ref:`piocore` from a system terminal.

1. Open **System Terminal**, on Windows ``cmd.exe`` (not :ref:`pioide` Terminal)
2. Build project and upload firmware using :ref:`piocore` which will download
   and install all dependent packages:

   .. code-block:: bash

       # Change directory to PlatformIO Project where is located "platformio.ini"
       cd path/to/platformio/project

       # Force PlatformIO to install all tools
       platformio run --target upload

If "platformio" command is not globally available in your environment and you
use :ref:`pioide`, please use built-in :ref:`piocore` which is located in:

* Windows: ``C:\Users\{username}\.platformio\penv\Scripts\platformio``
  Please replace ``{username}`` with a real user name
* Unix: ``~/.platformio/penv/bin/platformio``


.. note::
    You can add ``platformio`` and ``pio`` commands to your system environment.
    See :ref:`faq_install_shell_commands`.

Solution 4: Manual
^^^^^^^^^^^^^^^^^^

If none of solutions above does not work for you, you can download and unpack
all packages manually to ":ref:`projectconf_pio_home_dir`/packages".

Please visit `PlatformIO Package Storage <https://bintray.com/platformio/dl-packages>`_
and download a package for your platform.
A correct package path is ":ref:`projectconf_pio_home_dir`/packages/{package_name}/package.json".

Building
~~~~~~~~

UnicodeWarning: Unicode equal comparison failed
'''''''''''''''''''''''''''''''''''''''''''''''

Full warning message is "UnicodeWarning: Unicode equal comparison failed to
convert both arguments to Unicode - interpreting them as being unequal".

**KNOWN ISSUE**. Please move your project to a folder which full path does not
contain non-ASCII chars.

UnicodeDecodeError: Non-ASCII characters found in build environment
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

**KNOWN ISSUE**. :ref:`piocore` currently does not support projects which
contain non-ASCII characters (codes) in a full path or depend on the
libraries which use non-ASCII characters in their names.

**TEMPORARY SOLUTION**

1. Use :ref:`pioide`, it will automatically install :ref:`piocore` in a root
   of system disk (``%DISK%/.platformio``) and avoid an issue when system
   User contains non-ASCII characters
2. Do not use non-ASCII characters in project folder name or its parent folders.

Also, if you want to place :ref:`piocore` in own location, see:

* Set :envvar:`PLATFORMIO_HOME_DIR` environment variable with own path
* Configure custom location per project using :ref:`projectconf_pio_home_dir`
  option in :ref:`projectconf`.

ARM toolchain: cc1plus: error while loading shared libraries
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

See related answers for
`error while loading shared libraries <https://github.com/platformio/platformio-core/issues?utf8=✓&q=error+while+loading+shared+libraries>`_.

Archlinux: libncurses.so.5: cannot open shared object file
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Answered in `issue #291 <https://github.com/platformio/platformio-core/issues/291>`_.

Monitoring a serial port breaks upload
''''''''''''''''''''''''''''''''''''''

Answered in `issue #384 <https://github.com/platformio/platformio-core/issues/384>`_.
