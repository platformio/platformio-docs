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

You can export the PlatformIO executables' directory to the PATH environmental
variable. This method will allow you to execute ``platformio`` commands from
any terminal emulator as long as you're logged in as the user PlatformIO is
installed and configured for.

If you use Bash as your default shell, you can do it by editing either
``~/.profile`` or ``~/.bash_profile`` and adding the following line:

.. code-block:: shell

    export PATH=$PATH:$HOME/.platformio/penv/bin

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

You need to edit the system environment variable called ``Path`` and append
``C:\Users\UserName\.platformio\penv\Scripts;`` path in the beginning of a
list (please replace ``UserName`` with your account name).