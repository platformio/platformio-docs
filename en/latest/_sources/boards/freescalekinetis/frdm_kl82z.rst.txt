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

.. _board_freescalekinetis_frdm_kl82z:

Freescale Kinetis FRDM-KL82Z
============================

.. contents::

Hardware
--------

Platform :ref:`platform_freescalekinetis`: Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

.. list-table::

  * - **Microcontroller**
    - MKL82Z128VLK7
  * - **Frequency**
    - 96MHz
  * - **Flash**
    - 128KB
  * - **RAM**
    - 96KB
  * - **Vendor**
    - `Freescale <https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/l-seriesultra-low-powerm0-plus/freedom-development-board-for-kinetis-ultra-low-power-kl82-mcus:FRDM-KL82Z?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``frdm_kl82z`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:frdm_kl82z]
  platform = freescalekinetis
  board = frdm_kl82z

You can override default Freescale Kinetis FRDM-KL82Z settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `frdm_kl82z.json <https://github.com/platformio/platform-freescalekinetis/blob/master/boards/frdm_kl82z.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:frdm_kl82z]
  platform = freescalekinetis
  board = frdm_kl82z

  ; change microcontroller
  board_build.mcu = mkl82z128vlk7

  ; change MCU frequency
  board_build.f_cpu = 96000000L


Uploading
---------
Freescale Kinetis FRDM-KL82Z supports the next uploading protocols:

* ``jlink``
* ``mbed``

Default protocol is ``mbed``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:frdm_kl82z]
  platform = freescalekinetis
  board = frdm_kl82z

  upload_protocol = mbed

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

Freescale Kinetis FRDM-KL82Z does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_jlink`
    - 
    - Yes

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_mbed`
      - Arm Mbed OS is an open source embedded operating system designed specifically for the 'things' in the Internet of Things. It includes all the features you need to develop a connected product based on an Arm Cortex-M microcontroller, including security, connectivity, an RTOS and drivers for sensors and I/O devices