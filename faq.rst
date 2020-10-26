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

What is ``.pio`` directory
~~~~~~~~~~~~~~~~~~~~~~~~~~

Please refer to :ref:`projectconf_pio_workspace_dir`.

What is ``.pioenvs`` directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please refer to :ref:`projectconf_pio_build_dir`.

Command completion in Terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please refer to :ref:`cmd_system_completion`.

.. _faq_install_python:

Install Python Interpreter
--------------------------

:ref:`piocore` is written in `Python <https://www.python.org/downloads/>`_ that
is installed by default on the all popular OS except Windows.

Please navigate to official website and `Download the latest Python <https://www.python.org/downloads/>`_
and install it. Please **READ NOTES BELOW**.

:macOS:
  Please read the "Important Information" displayed during installation for information
  about SSL/TLS certificate validation and the running the **"Install Certificates.command"**.

  If you do not install SSL/TLS certificates, PlatformIO will not be able to download
  dependent packages, libraries, and toolchains.

:Windows:
  Please select ``Add Python to Path`` (see below), otherwise, ``python`` command will
  not be available.

  .. image:: _static/images/python-installer-add-path.png

.. _faq_convert_ino_to_cpp:

Convert Arduino file to C++ manually
------------------------------------

Some :ref:`ide` doesn't support Arduino files (``*.ino`` and ``.pde``) because
they are not valid C/C++ based source files:

1. Missing includes such as ``#include <Arduino.h>``
2. Function declarations are omitted.

In this case, code completion and code linting do not work properly or
are disabled. To avoid this issue you can manually convert your INO files to CPP.

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

Finish.

Program Memory Usage
--------------------

PlatformIO calculates firmware/program memory usage based on the next segments:

:``.text``:

    The code segment, also known as a text segment or simply as
    text, is where a portion of an object file or the corresponding section of
    the program's virtual address space that contains executable instructions
    is stored and is generally read-only and fixed size.

:``.data``:

    The .data segment contains any global or static variables which have a
    pre-defined value and can be modified. The values for these variables are
    initially stored within the read-only memory (typically within ``.text``)
    and are copied into the ``.data`` segment during the start-up routine of
    the program. Example,

    .. code-block:: cpp

         int val = 3;
         char string[] = "Hello World";

:``.bss``:

     Uninitialized data is usually adjacent to the data segment. The BSS
     segment contains all global variables and static variables that are
     initialized to zero or do not have explicit initialization in the source code.
     For instance, a variable defined as ``static int i;`` would be contained
     in the BSS segment.

The rough calculation could be done as:

* PROGRAM (Flash) = ``.text`` + ``.data``
* DATA (RAM) = ``.bss`` + ``.data``

If you need to print **all memory sections and addresses**, please use
:option:`pio run --verbose` command.

Recommended for reading:

* https://en.wikipedia.org/wiki/Data_segment
* `text, data and bss: Code and Data Size Explained <https://mcuoneclipse.com/2013/04/14/text-data-and-bss-code-and-data-size-explained/?utm_source=platformio&utm_medium=docs>`_

.. _faq_advanced_serial_monitor_ui:

Advanced Serial Monitor with UI
-------------------------------

PlatformIO Core provides CLI version (:ref:`cmd_device_monitor`) of Serial Monitor.
If you need advanced instrument with a rich UI, we recommend free and multi-platform
`CoolTerm <https://freeware.the-meiers.org/?utm_source=platformio&utm_medium=docs>`_
serial port terminal application.

.. warning::
  Please note that you need to **manually disconnect (close serial port connection)** in
  CoolTerm **before doing uploading** in PlatformIO. PlatformIO can not disconnect/connect
  to a target device automatically when CoolTerm is used.

.. _faq_troubleshooting:

Troubleshooting
---------------

Installation
~~~~~~~~~~~~

Multiple PlatformIO Cores in a system
'''''''''''''''''''''''''''''''''''''

Multiple standalone :ref:`piocore` in a system could lead to the different
issues. We highly recommend to keep one instance of PlatformIO Core or use built-in
PlatformIO Core in :ref:`pioide`:

* :ref:`ide_atom` - ``Menu PlatformIO: Settings > PlatformIO IDE > Use built-in PlatformIO Core``
* :ref:`ide_vscode` - :ref:`ide_vscode_settings` > Set ``platformio-ide.useBuiltinPIOCore`` to ``true``.

Finally, if you have a standalone :ref:`piocore` in a system, please open system
Terminal (not PlatformIO IDE Terminal) and uninstall obsolete PlatformIO Core:

.. code-block:: bash

    pip uninstall platformio

    # if you used macOS "brew"
    brew uninstall platformio

If you need to have :ref:`piocore` globally in a system, please
:ref:`piocore_install_shell_commands`.

'platformio' is not recognized as an internal or external command
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

If you use :ref:`pioide`, please check in PlatformIO IDE Settings that
"Use built-in PlatformIO Core" is enabled.

If you modify system environment variable ``PATH`` in your Bash/Fish/ZSH
profile, please do not override global ``PATH``. This line
``export PATH="/my/custom/path"`` is incorrect. Use ``export PATH="/my/custom/path":$PATH``
instead.

.. _faq_udev_rules:

99-platformio-udev.rules
''''''''''''''''''''''''

Linux users have to install `udev <https://en.wikipedia.org/wiki/Udev>`_ rules
for PlatformIO supported boards/devices. The
latest version of rules may be found at https://raw.githubusercontent.com/platformio/platformio-core/master/scripts/99-platformio-udev.rules

.. note::
  Please check that your board's PID and VID  are listed in the rules.
  You can list connected devices and their PID/VID using :ref:`cmd_device_list`
  command.

This file must be placed at ``/etc/udev/rules.d/99-platformio-udev.rules``
(preferred location) or ``/lib/udev/rules.d/99-platformio-udev.rules``
(required on some broken systems).

Please open system Terminal and type

.. code-block:: bash

    # Recommended
    curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core/master/scripts/99-platformio-udev.rules | sudo tee /etc/udev/rules.d/99-platformio-udev.rules

    # OR, manually download and copy this file to destination folder
    sudo cp 99-platformio-udev.rules /etc/udev/rules.d/99-platformio-udev.rules


Restart "udev" management tool:

.. code-block:: bash

    sudo service udev restart

    # or

    sudo udevadm control --reload-rules
    sudo udevadm trigger


Ubuntu/Debian users may need to add own “username” to the “dialout” group if
they are not “root”, doing this issuing

.. code-block:: bash

    sudo usermod -a -G dialout $USER
    sudo usermod -a -G plugdev $USER

Similarly, Arch users may need to add their user to the “uucp” group

.. code-block:: bash

    sudo usermod -a -G uucp $USER
    sudo usermod -a -G lock $USER

.. note::
  You will need to log out and log back in again (or reboot) for the user
  group changes to take effect.

After this file is installed, physically unplug and reconnect your board.

ImportError: cannot import name _remove_dead_weakref
''''''''''''''''''''''''''''''''''''''''''''''''''''

Windows users can experience this issue when multiple Python interpreters are
installed in a system and conflict each other. The easy way to fix this
problem is uninstalling all Python interpreters using Windows Programs Manager
and installing them manually again.

1. "Windows > Start Menu > Settings > System > Apps & Features", select
   Python interpreters and uninstall them.
2. Install the latest Python interpreter, see :ref:`faq_install_python` guide
3. Remove ``C:\Users\YourUserName\.platformio`` and ``C:\.platformio`` folders
   if exist (do not forget to replace "YourUserName" with the real user name)
4. Restart :ref:`pioide`.

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

Solution 4: Manual
^^^^^^^^^^^^^^^^^^

If none of the solutions above do work for you, you can download and unpack
all packages manually to ":ref:`projectconf_pio_core_dir`/packages".

Please visit `PlatformIO Package Storage <https://bintray.com/platformio/dl-packages>`_
and download a package for your platform.
A correct package path is ":ref:`projectconf_pio_core_dir`/packages/{package_name}/package.json".

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
