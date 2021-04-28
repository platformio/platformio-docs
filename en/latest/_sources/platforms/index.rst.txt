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

The PlatformIO ecosystem has a decentralized architecture, allowing
development for a range of *development platforms*. A development
platform (or just "platform" for short) is usually a particular
microcontroller or processor architecture that PlatformIO projects can
be compiled to run on. (A few platforms, for example Teensy, use
different target architectures for different boards.)

Each of the three supported host systems Mac OS X, Linux and Windows
support compiling for all platforms listed below. Some platforms are
also supported under ARM Linux hosts such as Raspberry Pi. For each
development platform, PlatformIO defines:

- The **PlatformIO Build System** build scripts for the supported frameworks
  and SDKs
- Pre-configured presets for embedded circuit boards
- Pre-compiled toolchains and related tools for the architechture(s)

Each project must specify the platform name using the
:ref:`projectconf_env_platform` option in :ref:`projectconf`. A
specific platform version can optionally be specified as well. As
embedded boards are equipped with a particular microcontroller, each
embedded board specifies what development platform it uses and this
can not be changed.

If a new board uses an architecture not in this list, a custom
development platform can be created; see :ref:`platform_creating`.


Embedded
--------

.. toctree::
    :maxdepth: 1

    aceinna_imu
    asrmicro650x
    atmelavr
    atmelmegaavr
    atmelsam
    chipsalliance
    espressif32
    espressif8266
    freescalekinetis
    gd32v
    infineonxmc
    intel_arc32
    intel_mcs51
    kendryte210
    lattice_ice40
    maxim32
    microchippic32
    nordicnrf51
    nordicnrf52
    nuclei
    nxpimxrt
    nxplpc
    riscv_gap
    shakti
    sifive
    siliconlabsefm32
    ststm32
    ststm8
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
