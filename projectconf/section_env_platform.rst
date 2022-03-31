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

.. |PIOREGISTRY| replace:: `PlatformIO Registry <https://registry.platformio.org>`__

.. _projectconf_section_env_platform:

Platform options
----------------

.. contents::
    :local:

.. _projectconf_env_platform:

``platform``
^^^^^^^^^^^^

Type: ``Package Specification`` | Multiple: ``No``

Specify a development platform that provides integration of vendor-specific
boards (development kits, MCUs), high-level frameworks, and SDKs.
See :ref:`cmd_pkg_install_specifications` for details.

|PIOREGISTRY| allows you to explore supported development platforms, boards, frameworks, and toolchains.

For the advanced platform configuration, please check the :ref:`platforms` documentation.

Example of using a `Espressif 32 development platform <https://registry.platformio.org/platforms/platformio/espressif32>`_:

.. code-block:: ini

    [env:recommended_specification]
    ; allow backwards-compatible new functionality and bug-fixes
    platform = espressif32@^3.5.0

    [env:allow_only_bug_fixes]
    platform = espressif32@~3.5.0

    [env:exact_version]
    platform = espressif32@3.5.0

    [env:latest_version]
    platform = espressif32

    [env:development_verion_by_git]
    platform = https://github.com/platformio/platform-espressif32.git

    [env:custom_git_branch]
    platform = https://github.com/platformio/platform-espressif32.git#master

    [env:specific_git_commit]
    platform = https://github.com/platformio/platform-espressif32.git#f8340a2081a31c2ac8ed2b16907f2a21dc8897d4

.. _projectconf_env_platform_packages:

``platform_packages``
^^^^^^^^^^^^^^^^^^^^^

Type: ``Package Specification`` | Multiple: ``Yes``

Configure custom packages per a build environment. You can also override
default packages by :ref:`platforms` using the same name.
See :ref:`cmd_pkg_install_specifications` for details.

Check the |PIOREGISTRY| for the available toolchains, frameworks, SDKs, etc.

Examples:

.. code-block:: ini

    [env:override_default_toolchain]
    platform = atmelavr
    platform_packages =
      ; use GCC AVR 5.0+
      toolchain-gccarmnoneeabi@>1.50000.0

    [env:override_framework]
    platform = espressif8266
    platform_packages =
      ; use upstream Git version
      framework-arduinoespressif8266 @ https://github.com/esp8266/Arduino.git

    [env:external_package]
    platform = ststm32
    platform_packages =
      ; latest openOCD from PlatformIO Package Registry
      tool-openocd

      ; source code of ST-Link
      tool-stlink-source @ https://github.com/texane/stlink.git

.. _projectconf_env_framework:

``framework``
^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``Yes``

:ref:`frameworks` name.


.. _projectconf_env_board:

``board``
^^^^^^^^^

Type: ``String (ID)`` | Multiple: ``No``

*PlatformIO* has pre-configured settings for the most popular boards:

- build configuration
- upload configuration
- debugging configuration
- connectivity information, etc.

You can find a valid  ``board`` ID in :ref:`boards` catalog,
`Boards Explorer <https://platformio.org/boards>`_ or
:ref:`cmd_boards` command.

``board_build.mcu``
^^^^^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``No``

``board_build.mcu`` is a microcontroller(MCU) type that is used by compiler to
recognize MCU architecture. The correct type of ``board_build.mcu`` depends on
platform library. For example, the list of ``board_build.mcu`` for "megaAVR Devices"
is described `here <http://www.nongnu.org/avr-libc/user-manual/>`_.

The full list of ``board_build.mcu`` for the popular embedded platforms you can find
in *Boards* section of :ref:`platforms`. See "Microcontroller" column.

.. _projectconf_board_build.f_cpu:

``board_build.f_cpu``
^^^^^^^^^^^^^^^^^^^^^

Type: ``Number`` | Multiple: ``No``

The option ``board_build.f_cpu`` is used to define MCU frequency (Hertz, Clock). A
format of this option is ``C-like long integer`` value with ``L`` suffix. The
1 Hertz is equal to ``1L``, then 16 MHz (Mega Hertz) is equal to ``16000000L``.

The full list of ``board_build.f_cpu`` for the popular embedded platforms you can
find in *Boards* section of :ref:`platforms`. See "Frequency" column.

.. note::
    This option doesn't make any changes to real clock settings on hardware. You should
    specify a ``board_build.f_cpu`` value  if you have changed a target's clock frequency
    so that the underlying software will be configured accordingly to match the change.

.. _projectconf_board_build.ldscript:

``board_build.ldscript``
^^^^^^^^^^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``No``

Path to the linker script to be used instead of the one defined by a framework. This
is useful for specifying a modified linker script, for example, when an application
requires a special memory section for a bootloader.

.. _projectconf_board_more_options:

More options
^^^^^^^^^^^^

You can override any board option declared in manifest file using the next
format ``board_{OBJECT.PATH}``, where ``{OBJECT.PATH}`` is an object path in
JSON manifest. Please navigate to "boards" folder of `PlatfomIO development platforms <https://github.com/topics/platformio-platform>`_
and open JSON file to list all available options.

For example, `Manifest: Espressif ESP32 Dev Module <https://github.com/platformio/platform-espressif32/blob/develop/boards/esp32dev.json>`_:

.. code-block:: ini

    [env:custom_board_options]
    ; Custom CPU Frequency
    board_build.f_cpu = 160000000L

    ; Custom FLASH Frequency
    board_build.f_flash = 80000000L

    ; Custom FLASH Mode
    board_build.flash_mode = qio

    ; Custom linker script
    board_build.ldscript = /path/to/ldscript.ld

    ; Custom maximum program size
    board_upload.maximum_size = 1310720
