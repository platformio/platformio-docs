..  Copyright 2014-present PlatformIO <contact@platformio.org>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _framework_espidf:

Framework ``espidf``
====================
Espressif IoT Development Framework. Official development framework for ESP32.

For more detailed information please visit `vendor site <https://github.com/espressif/esp-idf>`_.

.. contents::

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_espressif32`
      - Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by horizontal.

Aiyarafun
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``node32s``
      - `Node32s <http://www.ayarafun.com>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - ESP32
      - 240 MHz
      - 1024 Kb
      - 112 Kb

April Brother
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``espea32``
      - `April Brother ESPea32 <https://blog.aprbrother.com/product/espea>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - ESP32
      - 240 MHz
      - 1024 Kb
      - 288 Kb

DFRobot
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``firebeetle32``
      - `FireBeetle-ESP32 <https://dfrobotblog.wordpress.com>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - ESP32
      - 240 MHz
      - 1024 Kb
      - 288 Kb

Electronic SweetPeas
~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``esp320``
      - `Electronic SweetPeas ESP320 <http://www.sweetpeas.se/controller-modules/10-esp210.html>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - ESP32
      - 240 MHz
      - 1024 Kb
      - 288 Kb

Espressif
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``esp32dev``
      - `Espressif ESP32 Dev Module <https://en.wikipedia.org/wiki/ESP32>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - ESP32
      - 240 MHz
      - 1024 Kb
      - 288 Kb

Hornbill
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``hornbill32dev``
      - `Hornbill ESP32 Dev <https://hackaday.io/project/18997-hornbill>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - ESP32
      - 240 MHz
      - 1024 Kb
      - 288 Kb

    * - ``hornbill32minima``
      - `Hornbill ESP32 Minima <https://hackaday.io/project/18997-hornbill>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - ESP32
      - 240 MHz
      - 1024 Kb
      - 288 Kb

IntoRobot
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``intorobot``
      - `IntoRobot Fig <http://docs.intorobot.com/zh/hardware/fig/hardware/>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - ESP32
      - 240 MHz
      - 1024 Kb
      - 288 Kb

MakerAsia
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``nano32``
      - `MakerAsia Nano32 <http://iot-bits.com/nano32-esp32-development-board>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - ESP32
      - 240 MHz
      - 1024 Kb
      - 288 Kb

Noduino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``quantum``
      - `Noduino Quantum <http://wiki.jackslab.org/Noduino>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - ESP32
      - 240 MHz
      - 1024 Kb
      - 288 Kb

SparkFun Electronics
~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``esp32thing``
      - `SparkFun ESP32 Thing <https://www.sparkfun.com/products/13907>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - ESP32
      - 240 MHz
      - 1024 Kb
      - 112 Kb

WEMOS
~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``lolin32``
      - `WEMOS LoLin32 <https://wemos.cc>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - ESP32
      - 240 MHz
      - 1024 Kb
      - 288 Kb
