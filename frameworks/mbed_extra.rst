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

mbed framework consists of several components, some of which should be explicitly added to the build process.
For this purpose PlatformIO has special macro definitions that should be added to :ref:`projectconf_build_flags` when one of the components is used in a project:

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

Articles
--------

* Dec 15, 2015 - **stastaka** - `PlatformIOでカスタムボードを使う (Use a custom board for PlatformIO, Japanese) <http://qiita.com/stastaka/items/a6a50dbbb2933bd78bdd>`_
* Nov 06, 2015 - **nocd5** - `PlatformIOでmbedをオフラインビルドしSTM32 Nucleoボードでmrubyを使う (Use mruby in the offline build for STM32 Nucleo board with mbed and PlatformIO, Japanese) <http://qiita.com/nocd5/items/d5fda776240f7e7c17eb>`_
* Oct 21, 2015 - **Vittorio Zaccaria** - `Using a cheap STM32 Nucleo to teach remote sensor monitoring <http://www.vittoriozaccaria.net/#/blog/2015/10/21/using-a-cheap-stm32-to-teach-remote-sensor-monitoring.html>`_
* Sep 01, 2015 - **Thomas P. Weldon, Ph.D.** - `Improvised MBED FRDM-K64F Eclipse/PlatformIO Setup and Software Installation <http://thomasweldon.com/tpw/courses/embeddsp/p00pcFrdmK64_eclipsePlatformioSetup.html>`_

See more :ref:`articles`.

Examples
--------

All project examples are located in PlatformIO repository
`Examples for MBED framework <https://github.com/platformio/platformio-examples/tree/develop/mbed>`_.

* `Blink <https://github.com/platformio/platformio-examples/tree/develop/mbed/mbed-blink>`_
* `DSP <https://github.com/platformio/platformio-examples/tree/develop/mbed/mbed-dsp>`_
* `Events <https://github.com/platformio/platformio-examples/tree/develop/mbed/mbed-events>`_
* `File System <https://github.com/platformio/platformio-examples/tree/develop/mbed/mbed-filesystem>`_
* `RTOS <https://github.com/platformio/platformio-examples/tree/develop/mbed/mbed-rtos>`_
* `RTOS Ethernet <https://github.com/platformio/platformio-examples/tree/develop/mbed/mbed-rtos-ethernet>`_
* `RTOS Ethernet TLS <https://github.com/platformio/platformio-examples/tree/develop/mbed/mbed-rtos-ethernet-tls>`_
* `Serial <https://github.com/platformio/platformio-examples/tree/develop/mbed/mbed-serial>`_
