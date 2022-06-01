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
https://raw.githubusercontent.com/platformio/platformio-core/master/scripts/99-platformio-udev.rules

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
