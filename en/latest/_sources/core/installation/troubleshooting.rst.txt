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

.. note::
    **Linux OS**: Don't forget to install :ref:`platformio_udev_rules`

    **Windows OS**: Please check that you have correctly installed the
    USB driver from the board manufacturer.

If you find any issues with PlatformIO Core Installer Script, please report to
https://github.com/platformio/platformio-core-installer/issues


.. _multiple_pio_cores_issue:

Multiple PlatformIO Cores in a system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multiple standalone :ref:`piocore` in a system could lead to the different
issues. We highly recommend to keep one instance of PlatformIO Core or use built-in
PlatformIO Core in :ref:`pioide`:

* :ref:`ide_vscode` - :ref:`ide_vscode_settings` > Set ``platformio-ide.useBuiltinPIOCore`` to ``true``.

Finally, if you have a standalone :ref:`piocore` in a system, please open system
Terminal (not PlatformIO IDE Terminal) and uninstall obsolete PlatformIO Core:

.. code-block:: bash

    pip uninstall platformio
    python -m pip uninstall platformio

    # if you used macOS "brew"
    brew uninstall platformio

If you need to have :ref:`piocore` globally in a system, please
:ref:`piocore_install_shell_commands`.

'platformio' is not recognized as an internal or external command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you use :ref:`pioide`, please check in PlatformIO IDE Settings that
"Use built-in PlatformIO Core" is enabled.

If you modify the system environment variable ``PATH`` in your Bash/Fish/ZSH
profile, please do not override global ``PATH``. This line
``export PATH="/my/custom/path"`` is incorrect. Use ``export PATH="/my/custom/path":$PATH``
instead.

ImportError: cannot import name _remove_dead_weakref
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Windows users can experience this issue when multiple Python interpreters are
installed in a system and conflict with each other. The easy way to fix this
problem is uninstalling all Python interpreters using Windows Programs Manager
and installing them manually again.

1. "Windows > Start Menu > Settings > System > Apps & Features", select
   Python interpreters and uninstall them.
2. Install the latest Python interpreter, see :ref:`faq_install_python` guide
3. Remove ``C:\Users\YourUserName\.platformio`` and ``C:\.platformio`` folders
   if exist (do not forget to replace "YourUserName" with the real user name)
4. Restart :ref:`pioide`.
