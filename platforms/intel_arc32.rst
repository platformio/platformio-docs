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

.. _platform_intel_arc32:

Intel ARC32
===========

:Configuration:
  :ref:`projectconf_env_platform` = ``intel_arc32``

ARC embedded processors are a family of 32-bit CPUs that are widely used in SoC devices for storage, home, mobile, automotive, and Internet of Things applications.

For more detailed information please visit `vendor site <http://www.intel.com/content/www/us/en/wearables/wearable-soc.html?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Intel ARC32 development platform repository <https://github.com/platformio/platform-intel_arc32/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `arduino-curie-imu <https://github.com/platformio/platform-intel_arc32/tree/master/examples/arduino-curie-imu?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-blink <https://github.com/platformio/platform-intel_arc32/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-intel_arc32/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs>`_

Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-intel_arc32/releases>`__
of Intel ARC32 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = intel_arc32
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = intel_arc32@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-intel_arc32.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinointel <https://github.com/01org/corelibs-arduino101.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework Intel ARC32 processor

    * - `tool-arduino101load <https://github.com/01org/intel-arduino-tools.git?utm_source=platformio.org&utm_medium=docs>`__
      - Genuino101 uploader tool

    * - `toolchain-intelarc32 <https://embarc.org/toolchain/?utm_source=platformio.org&utm_medium=docs>`__
      - GCC for Intel ARC processor

.. warning::
    **Linux Users**:

        * Install "udev" rules :ref:`faq_udev_rules`
        * Raspberry Pi users, please read this article
          `Enable serial port on Raspberry Pi <https://hallard.me/enable-serial-port-on-raspberry-pi/>`__.


    **Windows Users:**

        Please check that you have a correctly installed USB driver from board
        manufacturer


Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

Intel
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_intel_arc32_genuino101`
      - No
      - ARCV2EM
      - 32MHz
      - 152KB
      - 80KB
