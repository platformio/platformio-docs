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

RTOS, Events, FileSystem
~~~~~~~~~~~~~~~~~~~~~~~~

mbed framework consists of several components, some of which should be
explicitly added to the build process. For this purpose PlatformIO has special
macro definitions that should be added to :ref:`projectconf_build_flags` of
:ref:`projectconf` when one of the components is used in a project:

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - ``PIO_FRAMEWORK_MBED_RTOS_PRESENT``
      - Build the project with enabled ``rtos`` library

    * - ``PIO_FRAMEWORK_MBED_EVENTS_PRESENT``
      - Build the project with enabled ``events`` library

    * - ``PIO_FRAMEWORK_MBED_FILESYSTEM_PRESENT``
      - Build the project with enabled ``filesystem`` library

An example of :ref:`projectconf` with enabled ``events`` library

.. code-block:: ini

    [env:wizwiki_w7500p]
    platform = wiznet7500
    framework = mbed
    board = wizwiki_w7500p
    build_flags = -D PIO_FRAMEWORK_MBED_EVENTS_PRESENT


An example of :ref:`projectconf` with ``events`` and ``rtos`` libraries

.. code-block:: ini

    [env:nrf52_dk]
    platform = nordicnrf52
    framework = mbed
    board = nrf52_dk
    build_flags = -D PIO_FRAMEWORK_MBED_EVENTS_PRESENT -D PIO_FRAMEWORK_MBED_RTOS_PRESENT

An example of :ref:`projectconf` with ``filesystem`` library

.. code-block:: ini

    [env:nucleo_f767zi]
    platform = ststm32
    framework = mbed
    board = nucleo_f767zi
    build_flags = -D PIO_FRAMEWORK_MBED_FILESYSTEM_PRESENT

Ignore built-in libraries
~~~~~~~~~~~~~~~~~~~~~~~~~

See :ref:`projectconf_lib_ignore`.
