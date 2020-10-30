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

.. contents:: Contents
    :local:

In a nutshell, avr-stub is a piece of software (stub) that is added to your
application and communicates with PlatformIO when a debug session is running. It
requires several additional configuration steps in order to use it as a debug tool. To
use avr-stub, the following settings in :ref:`projectconf`:

.. code-block:: ini

    [env:myenv]
    platform = atmelavr
    board = ...

    debug_tool = avr-stub
    debug_port = SERIAL_PORT

    ; GDB stub implementation
    lib_deps =
        jdolinay/avr-debugger @ ~1.1

Where the value in :ref:`projectconf_debug_port` is a serial port connected to your
board and ``jdolinay/avr-debugger`` is a special library that implements the GDB stub.

In order to enable the GDB stub in your application, a call to the special function
``debug_init`` must be added at the beginning of your application. For example, with
the Arduino framework it might look like this:

.. code-block:: cpp

    #include "Arduino.h"
    #include "avr8-stub.h"

    void setup()
    {
      // initialize GDB stub
      debug_init();
      pinMode(LED_BUILTIN, OUTPUT);
    }

    void loop()
    {
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
    }

.. warning::
    If your program doesn't stop on a breakpoint, try specifying an explicit breakpoint
    directly in the code using the ``breakpoint`` function:

    .. code-block:: cpp

        ...

        void loop()
        {
          breakpoint();
          digitalWrite(LED_BUILTIN, HIGH);
          delay(300);
          digitalWrite(LED_BUILTIN, LOW);
          delay(100);
        }

        ...

Breakpoint modes
----------------

The avr-stub tool supports the following three breakpoint modes:

.. list-table::
    :header-rows:  1
    :widths: 80 20

    * - Description
      - AVR8_BREAKPOINT_MODE

    * - FLASH breakpoint mode, which works only with atmega328 based boards and
        requires a special bootloader
      - ``0``

    * - RAM breakpoint mode, the default mode which works out of the box with all
        atmega328, atmega1280, and atmega2560 based boards
      - ``1``

    * - FLASH breakpoint mode through Optiboot, which works with all atmega328,
        atmega1280, and atmega2560 based boards and requires the version 8 of the
        bootloader.
      - ``2``

To switch between modes, specify a special macro definition ``AVR8_BREAKPOINT_MODE``
with the appropriate value from the table above, for example:

.. code-block:: ini

    [env:myenv]
    platform = atmelavr
    board = uno

    ; Set breakpoint mode
    build_flags =
      -DAVR8_BREAKPOINT_MODE=2

    debug_tool = avr-stub
    debug_port = SERIAL_PORT

    lib_deps =
        jdolinay/avr-debugger @ ~1.1


Debugger limitations
--------------------

- One external interrupt pin must be reserved for the debugger.
- Any part of your application that uses the UART module (e.g. Arduino Serial class)
  cannot be used in your program together with the debugger.
- When using flash breakpoints the watchdog cannot be used.

More detailed information can be found in the ``Important limitations of the debugger``
section in `the official documentation <https://github.com/jdolinay/avr_debug/blob/master/doc/avr_debug.pdf>`__.
