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

.. _platforms:

Development Platforms
=====================

PlatformIO ecosystem has decentralized architecture. Build scripts, toolchains,
the pre-built tools for the popular OS (*Mac OS X, Linux (+ARM) and Windows*)
are organized into the multiple development platforms.

Each development platform contains:

- **PlatformIO Build System** based build scripts for the supported frameworks
  and SDKs
- Pre-configured presets for embedded boards
- Pre-compiled toolchains and relative tools for multiple architectures.

A platform name or its specific version could could be specified using
:ref:`projectconf_env_platform` option in :ref:`projectconf`.

Embedded
--------

.. toctree::
    :maxdepth: 1

    atmelavr
    atmelsam
    espressif32
    espressif8266
    freescalekinetis
    intel_arc32
    lattice_ice40
    maxim32
    microchippic32
    nordicnrf51
    nordicnrf52
    nxplpc
    siliconlabsefm32
    ststm32
    teensy
    timsp430
    titiva
    wiznet7500

Desktop
-------

.. toctree::
    :maxdepth: 1

    native
    linux_arm
    linux_i686
    linux_x86_64
    windows_x86
