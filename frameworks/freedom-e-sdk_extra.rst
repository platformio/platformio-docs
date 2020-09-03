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

Using with FreeRTOS
~~~~~~~~~~~~~~~~~~~

In order to add FreeRTOS to your project, it must be explicitly specified as an
additional framework in the ``framework`` field of :ref:`projectconf`, for example:

.. code-block:: ini

    [env:freertos]
    platform = sifive
    framework = freedom-e-sdk, freertos
    board = ...

.. note::

    FreeRTOS RISC-V port for the :ref:`platform_sifive` development platform is
    distributed as part of ``Freedom E SDK`` and cannot be used as a standalone
    framework

Most of the application specific configuration is done in a special file called
``FreeRTOSConfig.h`` which must be present in each FreeRTOS-based project. Additional
settings for build configuration are set in :ref:`projectconf` using the following
syntax ``board_build.freertos.*`` where ``*`` is an option from the following list:

FreeRTOS settings
^^^^^^^^^^^^^^^^^

:heap_model:

Available values: ``heap_1, heap_2, heap_3, heap_4, heap_5`` | Default: ``heap_4``

FreeRTOS offers several heap management schemes that range in complexity and features:

- ``heap_1`` – the very simplest, does not permit memory to be freed.
- ``heap_2`` – permits memory to be freed, but does not coalescence adjacent free blocks.
- ``heap_3`` – simply wraps the standard ``malloc()`` and ``free()`` for thread safety.
- ``heap_4`` – coalescences adjacent free blocks to avoid fragmentation. Includes
  absolute address placement option.
- ``heap_5`` – as per ``heap_4``, with the ability to span the heap across multiple
  non-adjacent memory areas.

More information about FreeRTOS Memory Management can be found in
`the official documentation <https://www.freertos.org/a00111.html>`__.

:interrupt_handler:

Default: ``FreedomMetal_InterruptHandler``

The name of a function to be called to handle interrupts

:exception_handler:

Default: ``FreedomMetal_ExceptionHandler``

The name of a function to be called to handle exceptions

:mtime_ctrl_addr:

Default: ``0x2000000``

The address of Machine Timer Register ``mtime``

:mpu_wrappers:

Available values: ``enable | disable`` | Default: ``disable``

Use Memory Protection Unit wrappers

Segger SystemView settings
^^^^^^^^^^^^^^^^^^^^^^^^^^

SystemView is a real-time recording and visualization tool for embedded systems that
reveals the true runtime behavior of an application.

:systemview:

Available values: ``enable | disable`` | Default: ``disable``

Compile and link Segger SystemView library

:sysview_record_enter_isr:

Default: ``SEGGER_SYSVIEW_RecordEnterISR``

The name of a function to be called to record interrupt execution.

:sysview_record_enter_isr:

Default: ``SEGGER_SYSVIEW_RecordExitISR``

The name of a function to be called to record finish of interrupt execution.

:sysview_record_exit_isr_to_scheduler:

Default: ``SEGGER_SYSVIEW_RecordExitISRToScheduler``

The name of a function to be called to record finish of interrupt when it's caused by
a context switch.

An example of :ref:`projectconf` with modified heap settings and enabled SystemView
feature:

.. code-block:: ini

    [env:sifive-hifive1-revb]
    platform = sifive
    framework = freedom-e-sdk, freertos
    board = hifive1-revb
    monitor_speed = 115200
    ; Configure stack size
    board_build.freedom-e-sdk.heap_size = 0x400
    ; Configure heap model and enable SystemView
    board_build.freertos.heap_model = heap_1
    board_build.freertos.systemview = enable

More information about FreeRTOS package for :ref:`platform_sifive` development platform
can be found in `the official repository <https://github.com/sifive/FreeRTOS-metal>`__.
