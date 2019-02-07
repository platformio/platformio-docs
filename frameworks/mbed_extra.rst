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

The configuration system
~~~~~~~~~~~~~~~~~~~~~~~~

PlatformIO allows you to customize mbed OS compile time configuration
parameters using ``mbed_app.json`` manifest. It should be placed into the root
of your project and located on the same level as :ref:`projectconf`.

Configuration is defined using `JSON <https://en.wikipedia.org/wiki/JSON>`_.
Some examples of configuration parameters:

* The sampling period for a data acquisition application.
* The default stack size for a newly created OS thread.
* The receive buffer size of a serial communication library.
* The flash and RAM memory size of a target board.

See more details in the official `ARM Mbed OS Configuration System <https://os.mbed.com/docs/mbed-os/v5.11/reference/configuration.html>`_.

A few PlatformIO-ready projects based on ARM mbed OS which use ``mbed_app.json``;

* `Freescale Kinetis: mbed-rtos-tls-client <https://github.com/platformio/platform-freescalekinetis/tree/develop/examples/mbed-rtos-tls-client>`_
* `ST STM32: mbed-rtos-mesh-minimal <https://github.com/platformio/platform-ststm32/tree/develop/examples/mbed-rtos-mesh-minimal>`_

Mbed lib and Mbed OS 5
~~~~~~~~~~~~~~~~~~~~~~

PlatformIO allows compiling projects with or without Mbed OS. By default, project 
is built without the OS feature. Most of the framework functionality requires the OS to be 
enabled. To add the OS feature you can use a special macro definition that needs be added to 
:ref:`projectconf_build_flags` of :ref:`projectconf`:

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - ``PIO_FRAMEWORK_MBED_RTOS_PRESENT``
      - Build the project with enabled ``rtos``

An example of :ref:`projectconf` with enabled ``rtos``

.. code-block:: ini

    [env:wizwiki_w7500p]
    platform = wiznet7500
    framework = mbed
    board = wizwiki_w7500p
    build_flags = -D PIO_FRAMEWORK_MBED_RTOS_PRESENT


Build profiles
~~~~~~~~~~~~~~

By default, PlatformIO builds your project using ``develop profile`` which provides optimized 
firmware size with full error information and allows MCU to go to sleep mode. In the case when
defalt build profile is not suitable for your project there two other profiles ``release`` and
``debug`` that can be enabled using special macro definitions. You can change build profile 
:ref:`projectconf_build_flags` of :ref:`projectconf`:

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - ``MBED_BUILD_PROFILE_RELEASE``
      - Release profile (smallest firmware, minimal error info)

    * - ``MBED_BUILD_PROFILE_DEBUG``
      - Debug profile (largest firmware, disabled sleep mode)

More information about differences between build profiles can be found on the 
official page `ARM Mbed OS Build Profiles <https://os.mbed.com/docs/mbed-os/v5.11/tools/build-profiles.html>`_.
