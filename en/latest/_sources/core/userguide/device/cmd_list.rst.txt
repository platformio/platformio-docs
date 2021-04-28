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

.. _cmd_device_list:

pio device list
===============

.. contents::

Usage
-----

.. code-block:: bash

    pio device list [OPTIONS]


Description
-----------

List available devices.
Default is set to ``--serial`` and all available
`Serial Ports <http://en.wikipedia.org/wiki/Serial_port>`_ will be shown.

Options
-------

.. program:: pio device list

.. option::
    --serial

List available `Serial Ports <http://en.wikipedia.org/wiki/Serial_port>`_,
default.

.. option::
    --logical

List available logical devices.

.. option::
    --mdns

List multicast DNS services.

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`_ format.

Examples
--------

1. Unix OS

.. code-block:: bash

    > pio device list
    /dev/cu.SLAB_USBtoUART
    ----------
    Hardware ID: USB VID:PID=10c4:ea60 SNR=0001
    Description: CP2102 USB to UART Bridge Controller

    /dev/cu.uart-1CFF4676258F4543
    ----------
    Hardware ID: USB VID:PID=451:f432 SNR=1CFF4676258F4543
    Description: Texas Instruments MSP-FET430UIF


2. Windows OS

.. code-block:: bash

    > pio device list
    COM4
    ----------
    Hardware ID: USB VID:PID=0451:F432
    Description: MSP430 Application UART (COM4)

    COM3
    ----------
    Hardware ID: USB VID:PID=10C4:EA60 SNR=0001
    Description: Silicon Labs CP210x USB to UART Bridge (COM3)


3. List multicast DNS services and logical devices

.. code-block:: bash

    > pio device list --mdns --logical
    Multicast DNS Services
    ======================

    PlatformIO._bttremote._tcp.local.
    ------------------------------
    Type: _bttremote._tcp.local.
    IP: ...
    Port: 62941
    Properties: ...

    Time for PlatformIO._adisk._tcp.local.
    ---------------------------------
    Type: _adisk._tcp.local.
    IP: 192.168.0.1
    Port: 9
    Properties: ...

    PlatformIO._ssh._tcp.local.
    ------------------------
    Type: _ssh._tcp.local.
    IP: ...
    Port: 22

    PlatformIO._sftp-ssh._tcp.local.
    -----------------------------
    Type: _sftp-ssh._tcp.local.
    IP: ...
    Port: 22


    Logical Devices
    ===============
    /
    -
    Name:

    /Volumes/PIO
    -------------
    Name: PIO

    /Volumes/PLUS
    --------------
    Name: PLUS
