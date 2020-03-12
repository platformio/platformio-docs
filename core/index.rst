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

.. |PIOCORE| replace:: **PlatformIO Core**

.. _piocore:

PlatformIO Core (CLI)
=====================

|PIOCORE| (CLI tool) is a heart of whole PlatformIO ecosystem and consists of

* Multi-platform Build System
* Development platform and package managers
* :ref:`librarymanager`
* :ref:`ldf`
* :ref:`Serial Port Monitor <cmd_device_monitor>`
* Integration components (:ref:`ide` and :ref:`ci`).

|PIOCORE| is written in `Python <https://www.python.org/downloads/>`_
and works on Windows, macOS, Linux, FreeBSD and *ARM*-based credit-card sized
computers (`Raspberry Pi <http://www.raspberrypi.org>`_,
`BeagleBone <http://beagleboard.org>`_,
`CubieBoard <http://cubieboard.org>`_,
`Samsung ARTIK <https://www.artik.io>`_, etc.).


|PIOCORE| provides a rich and documented Command Line Interface (CLI).
The other PlatformIO-based software and IDEs are based on **PlatformIO Core CLI**,
such as :ref:`pioide`. In other words, they wrap |PIOCORE| with own GUI.

.. note::

    Please note that you do not need to install |PIOCORE| if you are going
    to use :ref:`pioide`. |PIOCORE| is built into
    PlatformIO IDE and you will be able to use it within PlatformIO IDE Terminal.

    If you need |PIOCORE| commands outside PlatformIO IDE, please :ref:`piocore_install_shell_commands`.

.. toctree::
    :maxdepth: 2

    userguide/demo
    installation
    quickstart
    userguide/index
