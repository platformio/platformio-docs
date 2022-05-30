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

Troubleshooting
---------------

Package Manager
~~~~~~~~~~~~~~~

.. _faq_package_manager_error_5:

[Error 5] Access is denied
''''''''''''''''''''''''''

PlatformIO installs all packages to ":ref:`projectconf_pio_core_dir`/packages"
directory. You **MUST HAVE** write access to this folder.
Please note that **PlatformIO does not require** "sudo"/administrative privileges.

.. contents::
    :local:

Solution 1: Remove folder
^^^^^^^^^^^^^^^^^^^^^^^^^

A quick solution is to remove ":ref:`projectconf_pio_core_dir`/packages" folder
and repeat installation/building/uploading again.

Solution 2: Antivirus
^^^^^^^^^^^^^^^^^^^^^

Some antivirus tools forbid programs to create files in the background.
PlatformIO Package Manager does all work in the background: downloads package,
unpacks archive in temporary folder and moves final files to
":ref:`projectconf_pio_core_dir`/packages" folder.

Antivirus tool can block PlatformIO, that is why you see "[Error 5] Access is denied".
Try to **disable it for a while** or add :ref:`projectconf_pio_core_dir`
directory to exclusion/whitelist.

Solution 3: Run from Terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As we mentioned in "Solution 2", antivirus tools can block background file
system operations. Another solution is to run :ref:`piocore` from a system terminal.

1. Open **System Terminal**, on Windows ``cmd.exe`` (not :ref:`pioide` Terminal)
2. Build a project and upload firmware using :ref:`piocore` which will download
   and install all dependent packages:

   .. code-block:: bash

       # Change directory to PlatformIO Project where is located "platformio.ini"
       cd path/to/platformio/project

       # Force PlatformIO to install PlatformIO Home dependencies
       pio home

       # Force PlatformIO to install toolchains
       pio run --target upload

If "pio" command is not globally available in your environment and you
use :ref:`pioide`, please use built-in :ref:`piocore` which is located in:

* Windows: ``C:\Users\{username}\.platformio\penv\Scripts\platformio``
  Please replace ``{username}`` with a real user name
* Unix: ``~/.platformio/penv/bin/platformio``


.. note::
    You can add ``platformio`` and ``pio`` commands to your system environment.
    See :ref:`piocore_install_shell_commands`.

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

* Set :envvar:`PLATFORMIO_CORE_DIR` environment variable with own path
* Configure custom location per project using :ref:`projectconf_pio_core_dir`
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