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

.. _cmd_remote_device:

pio remote device
=================

**Remote Device: monitor remote device or list existing.**

.. contents::

.. _cmd_remote_device_list:

pio remote device list
-----------------------------

Usage
~~~~~

.. code-block:: bash

    pio remote device list [OPTIONS]

    # List devices from the specified agents. Multiple agents are allowed.
    pio remote --agent NAME device list [OPTIONS]

Description
~~~~~~~~~~~

List `Serial Ports <http://en.wikipedia.org/wiki/Serial_port>`_ on remote
machines where :ref:`cmd_remote_agent` is started.

You can list devices from the specified remote machines using ``--agent NAME``
option between "remote" & "device" sub-commands. For example, you have run
:option:`pio remote agent start --name` command with "home" and "office"
options:

* ``pio remote agent start --name home``
* ``pio remote agent start --name office``

Now, to list devices from office machine please use
``pio remote --agent office device list``.

Multiple agents are allowed (
``pio remote --agent lab1 --agent lab3 device ...``).

Options
~~~~~~~

.. program:: pio remote device list

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`_ format


Example
~~~~~~~

.. code::

    > pio remote device list

    Agent innomac.local
    ===================
    /dev/cu.Bluetooth-Incoming-Port
    -------------------------------
    Hardware ID: n/a
    Description: n/a
    /dev/cu.obd2ecu-SPPDev
    ----------------------
    Hardware ID: n/a
    Description: n/a
    /dev/cu.usbmodemFA1431
    ----------------------
    Hardware ID: USB VID:PID=2A03:0043 SER=75435353038351015271 LOCATION=250-1.4.3
    Description: Arduino Uno
    /dev/cu.usbserial-A6004003
    --------------------------
    Hardware ID: USB VID:PID=0403:6001 SER=A6004003 LOCATION=253-1.3.1
    Description: FT232R USB UART - FT232R USB UART
    /dev/cu.SLAB_USBtoUART
    ----------------------
    Hardware ID: USB VID:PID=10C4:EA60 SER=0001 LOCATION=253-1.3.2
    Description: CP2102 USB to UART Bridge Controller - CP2102 USB to UART Bridge Controller
    /dev/cu.usbmodem589561
    ----------------------
    Hardware ID: USB VID:PID=16C0:0483 SER=589560 LOCATION=250-1.4.1
    Description: USB Serial


.. _cmd_remote_device_monitor:

pio remote device monitor
--------------------------------

**Remote Serial Port Monitor**

Usage
~~~~~

.. code-block:: bash

    pio remote device monitor [OPTIONS]

    # Connect to a specified agent
    pio remote --agent NAME device monitor [OPTIONS]
    pio remote -a NAME device monitor [OPTIONS]


Description
~~~~~~~~~~~

Connect to Serial Port of remote device and receive or send data in real time.
:ref:`cmd_remote_agent` should be started before on a remote machine.

To control *monitor* please use these "hot keys":

* ``Ctrl+C`` Quit
* ``Ctrl+T`` Menu
* ``Ctrl+T followed by Ctrl+H`` Help

Options
~~~~~~~

.. program:: pio remote device monitor

.. option::
    -p, --port

Port, a number or a device name

.. option::
    -b, --baud

Set baud rate, default ``9600``

.. option::
    --parity

Set parity (*None, Even, Odd, Space, Mark*), one of
[``N``, ``E``, ``O``, ``S``, ``M``], default ``N``

.. option::
    --rtscts

Enable ``RTS/CTS`` flow control, default ``Off``

.. option::
    --xonxoff

Enable software flow control, default ``Off``

.. option::
    --rts

Set initial ``RTS`` line state, default ``0``

.. option::
    --dtr

Set initial ``DTR`` line state, default ``0``

.. option::
    --echo

Enable local echo, default ``Off``

.. option::
    --encoding

Set the encoding for the serial port (e.g. ``hexlify``, ``Latin1``, ``UTF-8``),
default ``UTF-8``.

.. option::
    -f, --filter

Add text transformation. Available filters:

* ``colorize`` Apply different colors for received and echo
* ``debug`` Print what is sent and received
* ``default`` Remove typical terminal control codes from input
* ``direct`` Do-nothing: forward all data unchanged
* ``nocontrol`` Remove all control codes, incl. CR+LF
* ``printable`` Show decimal code for all non-ASCII characters and replace
  most control codes

.. option::
    --eol

End of line mode (``CR``, ``LF`` or ``CRLF``), default ``CRLF``

.. option::
    --raw

Do not apply any encodings/transformations

.. option::
    --exit-char

ASCII code of special character that is used to exit the application,
default ``3`` (DEC, ``Ctrl+C``).

For example, to use ``Ctrl+]`` run
``pio remote device monitor --exit-char 29``.

.. option::
    --menu-char

ASCII code of special character that is used to control miniterm (menu),
default ``20`` (DEC)

.. option::
    ---quiet

Diagnostics: suppress non-error messages, default ``Off``

.. option::
    -d, --project-dir

Specify the path to project directory. By default, ``--project-dir`` is equal
to current working directory (``CWD``).

.. option::
    -e, --environment

Process specified environments.

You can also specify which environments should be processed by default using
:ref:`projectconf_pio_default_envs` option from :ref:`projectconf`.

Examples
~~~~~~~~

1. Show available options for *monitor*

.. code::

    > pio remote device monitor --help

    Usage: pio remote device monitor [OPTIONS]

    Options:
      -p, --port TEXT       Port, a number or a device name
      -b, --baud INTEGER    Set baud rate, default=9600
      --parity [N|E|O|S|M]  Set parity, default=N
      --rtscts              Enable RTS/CTS flow control, default=Off
      --xonxoff             Enable software flow control, default=Off
      --rts [0|1]           Set initial RTS line state, default=0
      --dtr [0|1]           Set initial DTR line state, default=0
      --echo                Enable local echo, default=Off
      --encoding TEXT       Set the encoding for the serial port (e.g. hexlify,
                            Latin1, UTF-8), default: UTF-8
      -f, --filter TEXT     Add text transformation
      --eol [CR|LF|CRLF]    End of line mode, default=CRLF
      --raw                 Do not apply any encodings/transformations
      --exit-char INTEGER   ASCII code of special character that is used to exit
                            the application, default=29 (DEC)
      --menu-char INTEGER   ASCII code of special character that is used to
                            control miniterm (menu), default=20 (DEC)
      --quiet               Diagnostics: suppress non-error messages, default=Off
      -h, --help            Show this message and exit.

2. Communicate with serial device and print help inside terminal

.. code::

    > pio remote device monitor

    --- Available ports:
    --- /dev/cu.Bluetooth-Incoming-Port n/a
    --- /dev/cu.Bluetooth-Modem n/a
    --- /dev/cu.SLAB_USBtoUART CP2102 USB to UART Bridge Controller
    --- /dev/cu.obd2ecu-SPPDev n/a
    Enter port name:/dev/cu.SLAB_USBtoUART
    --- Miniterm on /dev/cu.SLAB_USBtoUART: 9600,8,N,1 ---
    --- Quit: Ctrl+C  |  Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---
    Hello PlatformIO!
    ---
    --- Ctrl+]   Exit program
    --- Ctrl+T   Menu escape key, followed by:
    --- Menu keys:
    ---    Ctrl+T  Send the menu character itself to remote
    ---    Ctrl+]  Send the exit character itself to remote
    ---    Ctrl+I  Show info
    ---    Ctrl+U  Upload file (prompt will be shown)
    --- Toggles:
    ---    Ctrl+R  RTS          Ctrl+E  local echo
    ---    Ctrl+D  DTR          Ctrl+B  BREAK
    ---    Ctrl+L  line feed    Ctrl+A  Cycle repr mode
    ---
    --- Port settings (Ctrl+T followed by the following):
    ---    p          change port
    ---    7 8        set data bits
    ---    n e o s m  change parity (None, Even, Odd, Space, Mark)
    ---    1 2 3      set stop bits (1, 2, 1.5)
    ---    b          change baud rate
    ---    x X        disable/enable software flow control
    ---    r R        disable/enable hardware flow control
    --- exit ---
