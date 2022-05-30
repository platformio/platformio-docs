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

System Requirements
-------------------

PlatformIO Core is written in `Python <https://www.python.org/downloads/>`_
and works on the most popular operating systems including ARM-based
credit-card-sized computers (`Raspberry Pi <http://www.raspberrypi.org>`_,
`BeagleBone <http://beagleboard.org>`_, etc.).

:Operating System:

    Windows, macOS, Linux, FreeBSD, Linux ARMv6+

:Python Interpreter:

    **Python 3.6+ or above**. See detailed instructions on how to
    :ref:`faq_install_python`.

:Terminal Application:

    All CLI commands below should be executed in the
    `Command-line <http://en.wikipedia.org/wiki/Command-line_interface>`_
    application (Terminal). For macOS and Linux OS - *Terminal* application,
    for Windows OS – ``cmd.exe`` application.

:Access to Serial Ports (USB/UART):

    **Windows Users:** Please check that you have correctly installed
    the USB driver from the board manufacturer.

    **Linux Users**:

    * Please install :ref:`platformio_udev_rules`
    * Raspberry Pi users, please read this article
      `Enable serial port on Raspberry Pi <https://hallard.me/enable-serial-port-on-raspberry-pi/>`__.
