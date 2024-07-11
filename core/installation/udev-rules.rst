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

.. _platformio_udev_rules:

99-platformio-udev.rules
------------------------

Linux users have to install `udev <https://en.wikipedia.org/wiki/Udev>`_ rules
for PlatformIO supported boards/devices. The latest version of the rules may be found at
https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/system/99-platformio-udev.rules

.. note::
  Please check that your board's PID and VID  are listed in the rules.
  You can list connected devices and their PID/VID using :ref:`cmd_device_list`
  command.

This file must be placed at ``/etc/udev/rules.d/99-platformio-udev.rules``
(preferred location) or ``/lib/udev/rules.d/99-platformio-udev.rules``
(required on some broken systems).

Please open the system Terminal and type

.. code-block:: bash

    curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/system/99-platformio-udev.rules | sudo tee /etc/udev/rules.d/99-platformio-udev.rules

Or you can manually download and copy the file to a destination folder

.. code-block:: bash

    sudo cp 99-platformio-udev.rules /etc/udev/rules.d/99-platformio-udev.rules


Restart the "udev" management tool:

.. code-block:: bash

    sudo service udev restart

    # or

    sudo udevadm control --reload-rules
    sudo udevadm trigger


After this file is installed, physically unplug and reconnect your board.

Alternative using group membership
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of using a udev rules file, Linux users can get write access to the boards
using system `groups <https://wiki.archlinux.org/title/Users_and_groups>`__.

First, you need to identify which group owns the file corresponding to the serial port communication to the board (the serial port name can be found with :ref:`cmd_device_list`
command). For example, the file permissions for the serial port ``/dev/ttyACM0`` can be queried by:

.. code-block:: bash

    ls -l /dev/ttyACM0
    
    # prints something like:
    # crw-rw---- 1 root dialout 166, 0 juil. 10 13:43 /dev/ttyACM0

In that case, the read/write permission (``rw``) is granted to both the “root” user and members of the “dialout” group. Now, it is possible to grant read/write access to all users (``$ sudo chmod a+rw /dev/ttyACM0``), but this would only last as long as the card remains connected (only the udev rules file mentioned above can make such change permanent).

The alternative permanent solution is to add its own “username” to the “dialout” group, or whichever group name was identified at the preceding step. Typical names are “dialout”, “plugdev” (Debian/Ubuntu, Fedora), or “uucp” (Arch Linux). Adding a user to a group is done by:

.. code-block:: bash

    sudo usermod -a -G dialout $USERNAME

.. note::
    You will need to log out and log back in again (or reboot) for the user
    group changes to take effect. The effectiveness of the change can be checked with the ``$ id`` shell command.
