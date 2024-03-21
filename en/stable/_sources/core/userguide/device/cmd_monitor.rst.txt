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

.. _cmd_device_monitor:

pio device monitor
==================

.. contents::

Usage
-----

.. code-block:: bash

    pio device monitor [OPTIONS]

Description
-----------

This is a console application that provides a small terminal
application. It is based on `Miniterm <https://pythonhosted.org/pyserial/examples.html#miniterm>`_
and itself does not implement any terminal features such
as *VT102* compatibility. However it inherits these features from the terminal
it is run. For example on GNU/Linux running from an *xterm* it will support the
escape sequences of the *xterm*. On *Windows* the typical console window is dumb
and does not support any escapes. When *ANSI.sys* is loaded it supports some
escapes.

Miniterm supports `RFC 2217 <https://tools.ietf.org/html/rfc2217.html>`__
remote serial ports and raw sockets using `URL Handlers <https://pyserial.readthedocs.io/en/latest/url_handlers.html#urls>`__
such as ``rfc2217://<host>:<port>`` respectively ``socket://<host>:<port>``
as port argument when invoking.

To control *monitor* please use these "hot keys":

* ``Ctrl+C`` Quit
* ``Ctrl+T`` Menu
* ``Ctrl+T followed by Ctrl+H`` Help

Options
-------

.. program:: pio device monitor

.. option::
    -p, --port

The possible values are the same as documented for
:ref:`projectconf_monitor_port` option.

.. option::
    -b, --baud

Set baud rate, default ``9600``.

Can be customized in :ref:`projectconf`
using :ref:`projectconf_monitor_speed` option.

.. option::
    --parity

Set parity (*None, Even, Odd, Space, Mark*), one of
[``N``, ``E``, ``O``, ``S``, ``M``], default is ``N``.

Can be customized in :ref:`projectconf` using
:ref:`projectconf_monitor_parity` option.

.. option::
    --rtscts

Enable ``RTS/CTS`` flow control.

.. option::
    --xonxoff

Enable software flow control.

.. option::
    --rts

Set initial ``RTS`` line state (``0`` or ``1``).

Can be customized in :ref:`projectconf` using :ref:`projectconf_monitor_rts`
option.

.. option::
    --dtr

Set initial ``DTR`` line state (``0`` or ``1``).

Can be customized in :ref:`projectconf` using :ref:`projectconf_monitor_dtr`
option.

.. option::
    --echo

Enable local echo.

Can be customized in :ref:`projectconf`
using :ref:`projectconf_monitor_echo` option.

.. option::
    --encoding

Set the encoding for the serial port (e.g. ``hexlify``, ``Latin-1``, ``UTF-8``),
default ``UTF-8``. See the full list of `supported encodings <https://docs.python.org/3/library/codecs.html#standard-encodings>`_.

Can be customized in :ref:`projectconf`
using :ref:`projectconf_monitor_encoding` option.

.. option::
    -f, --filter

Add text transformation. See available filters at :ref:`cmd_device_monitor_filters`.

.. option::
    --eol

End of line mode (``CR``, ``LF`` or ``CRLF``), default ``CRLF``.

Can be customized in :ref:`projectconf`
using :ref:`projectconf_monitor_eol` option.

.. option::
    --raw

Do not apply any encodings/transformations.

Can be customized in :ref:`projectconf`
using :ref:`projectconf_monitor_raw` option.

.. option::
    --exit-char

ASCII code of special character that is used to exit the application,
default ``3`` (DEC, ``Ctrl+C``).

For example, to use ``Ctrl+]`` run
``pio device monitor --exit-char 29``.

.. option::
    --menu-char

ASCII code of special character that is used to control miniterm (menu),
default ``20`` (DEC)

.. option::
    ---quiet

Diagnostics: suppress non-error messages, default ``Off``.

.. option::
    --no-reconnect

Disable automatic reconnection if the established connection fails.

.. option::
    -d, --project-dir

Specify the path to project directory. By default, ``--project-dir`` is equal
to current working directory (``CWD``).

.. option::
    -e, --environment

Process specified environments.

You can also specify which environments should be processed by default using
:ref:`projectconf_pio_default_envs` option from :ref:`projectconf`.

.. _cmd_device_monitor_filters:

Filters
-------

PlatformIO allows you to apply multiple filters to the device monitor INPUT & OUTPUT
streams using the :option:`pio device monitor --filter` command or
:ref:`projectconf_monitor_filters` option.

Built-in Filters
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Description
    * - ``direct``
      - Do-nothing: forward all data unchanged. Useful if data already contains ANSI escape codes (colors)
    * - ``default``
      - Remove typical terminal control codes from input
    * - ``debug``
      - Print what is sent and received
    * - ``hexlify``
      - Show a hexadecimal representation of the data (code point of each character)
    * - ``log2file``
      - Log data to a file "platformio-device-monitor-%date%.log" located in the current working directory
    * - ``nocontrol``
      - Remove all control codes, incl. CR+LF
    * - ``printable``
      - Show decimal code for all non-ASCII characters and replace most control codes
    * - ``time``
      - Add timestamp with milliseconds for each new line
    * - ``send_on_enter``
      - Send a text to device on ENTER
    * - ``esp32_exception_decoder``
      - Custom filter for :ref:`platform_espressif32` which decodes crash exception
    * - ``esp8266_exception_decoder``
      - Custom filter for :ref:`platform_espressif8266` which decodes crash exception

Community Filters
~~~~~~~~~~~~~~~~~

The Community Filters are not a part of PlatformIO Core installation. You need to
install them manually. Please visit an official filter's documentation on how to use it.

.. list-table::
    :header-rows:  1

    * - Name
      - Description
    * - `arduplot <https://github.com/yhur/arduplot>`__
      - **Serial Plotter** compatible with Arduino syntax (output)

.. _cmd_device_monitor_custom_filters:

Custom Filters
~~~~~~~~~~~~~~

:ref:`piocore` provides an API to extend device monitor with custom filters.
Each filter is a Python-based file and its name should have the ``filter_`` prefix.
In a Python code, you need to extend ``DeviceMonitorFilterBase`` class to get access
to the ``rx()`` and ``tx()`` methods/callbacks.

:ref:`piocore` looks for the custom filters in the next locations:

- Project :ref:`projectconf_pio_monitor_dir`
- :ref:`projectconf_pio_platforms_dir`/<platform>/monitor
- :ref:`projectconf_pio_packages_dir`/<package>/monitor

See the base API below:

**filter_demo.py**

.. code-block:: python

  from platformio.public import DeviceMonitorFilterBase


  class Demo(DeviceMonitorFilterBase):
      NAME = "demo"

      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          print("Demo filter is loaded")

      def rx(self, text):
          return f"Received: {text}\n"

      def tx(self, text):
          print(f"Sent: {text}\n")
          return text

**Examples**

- https://github.com/platformio/platformio-core/tree/develop/platformio/device/monitor/filters
- https://github.com/platformio/platform-espressif32/tree/develop/monitor
- https://github.com/platformio/platform-espressif8266/tree/develop/monitor

Capture output to a file
~~~~~~~~~~~~~~~~~~~~~~~~

To capture the output of the device monitor in a file, you can use the
``log2file`` filter from :ref:`cmd_device_monitor_filters`.
By default, the log file will be saved in the ``logs`` folder located in the project root directory.

.. code-block:: bash

    > pio device monitor -f default -f log2file


Or using :ref:`projectconf` and :ref:`projectconf_monitor_filters`

.. code-block:: ini

    [env:log_output_to_file]
    ...
    platform = ...
    monitor_filters = default, log2file

Examples
--------

1. Show available options for *monitor*

.. code-block:: bash

    > pio device monitor --help
    Usage: pio device monitor [OPTIONS]

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
      -f, --filter TEXT     Add filters / text transformation
      --eol [CR|LF|CRLF]    End of line mode, default=CRLF
      --raw                 Do not apply any encodings/transformations
      --exit-char INTEGER   ASCII code of special character that is used to exit
                            the application, default=29 (DEC)
      --menu-char INTEGER   ASCII code of special character that is used to
                            control miniterm (menu), default=20 (DEC)
      --quiet               Diagnostics: suppress non-error messages, default=Off
      -h, --help            Show this message and exit.

2. Communicate with serial device and print help inside terminal

.. code-block:: bash

    > pio device monitor

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
