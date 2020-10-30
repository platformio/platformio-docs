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

.. _cmd_project_config:

pio project config
==================

.. contents::

Usage
-----

.. code-block:: bash

    pio project config [OPTIONS]


Description
-----------

Show project computed configuration based on :ref:`projectconf`.
The extra configuration files and dynamic variables will be expanded.

This command is useful for developers to check how PlatformIO computes configuration
from :ref:`projectconf`.

Options
~~~~~~~

.. program:: pio project config

.. option::
    -d, --project-dir

Specify the path to project directory. By default, ``--project-dir`` is equal
to current working directory (``CWD``).

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`_ format.

Examples
--------

.. code::

    > pio project config
    Computed project configuration for Tasmota Project

    platformio
    ----------
    src_dir          =  tasmota
    build_dir        =  .pioenvs
    build_cache_dir  =  .cache
    extra_configs    =  platformio_tasmota_env.ini
                        platformio_override.ini
    default_envs     =  tasmota

    common
    ------
    framework               =  arduino
    board                   =  esp01_1m
    board_build.flash_mode  =  dout
    platform                =  espressif8266
    build_flags             =  -D NDEBUG
                               -mtarget-align
                               -Wl,-Map,firmware.map
                               -Wl,-Teagle.flash.1m.ld
                               -DBEARSSL_SSL_BASIC
                               -DPIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK22x_190703
                               -DPIO_FRAMEWORK_ARDUINO_LWIP2_HIGHER_BANDWIDTH_LOW_FLASH
                               -DVTABLES_IN_FLASH
                               -fno-exceptions
                               -lstdc++
    build_unflags           =  -Wall
    board_build.f_cpu       =  80000000L
    monitor_speed           =  115200
    upload_speed            =  115200
    upload_resetmethod      =  nodemcu
    upload_port             =  COM5
    extra_scripts           =  pio/strip-floats.py
                               pio/name-firmware.py

    scripts_defaults
    ----------------
    extra_scripts  =  pio/strip-floats.py
                      pio/name-firmware.py

    ...
