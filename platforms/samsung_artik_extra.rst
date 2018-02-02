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

Configuration
-------------

.. contents::
    :local:

If you are using the Samsung ARTIK platform on macOS or Linux, you need to
perform the configuration steps detailed below to enable support for deployment
and debugging.

Windows
~~~~~~~

Usually Windows Update Service will automatically install FTDI driver.
You can choose an off-line installation and install
`FTDI driver <http://developer.artik.io/downloads/artik_ide/platformio/CDM_v2.12.26_WHQL_Certified.zip>`_
manually.

After installation, you will have two FTDI devices. Please use
`zadig <http://developer.artik.io/downloads/artik_ide/platformio/zadig-2.3.exe>`_
tool to change one FTDI device to a "libusb" compatible device.

macOS
~~~~~

First check that you have a FTDI compatible driver on your mac:

.. code::

    kextstat | grep FTDI

You should have ``com.apple.driver.AppleUSBFTDI``.

1. Install `ARTIK FTDI Driver <http://developer.artik.io/downloads/artik_ide/platformio/Artik053FTDIDriver.pkg>`_
2. Reboot your system.

Linux
~~~~~

Create a new file named ``/etc/udev/rules.d/51-artik053.rules`` and add the
following line:

.. code::

    SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6010", MODE="0660", GROUP="plugdev", SYMLINK+="artik053-%n"
