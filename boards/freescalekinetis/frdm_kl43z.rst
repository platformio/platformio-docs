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

.. _board_freescalekinetis_frdm_kl43z:

Freescale Kinetis FRDM-KL43Z
============================

.. contents::

Hardware
--------

Platform :ref:`platform_freescalekinetis`: Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

.. list-table::

  * - **Microcontroller**
    - MKL43Z256VLH4
  * - **Frequency**
    - 48MHz
  * - **Flash**
    - 256KB
  * - **RAM**
    - 32KB
  * - **Vendor**
    - `Freescale <https://os.mbed.com/platforms/FRDM-KL43Z/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``frdm_kl43z`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:frdm_kl43z]
  platform = freescalekinetis
  board = frdm_kl43z

You can override default Freescale Kinetis FRDM-KL43Z settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `frdm_kl43z.json <https://github.com/platformio/platform-freescalekinetis/blob/master/boards/frdm_kl43z.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:frdm_kl43z]
  platform = freescalekinetis
  board = frdm_kl43z

  ; change microcontroller
  board_build.mcu = mkl43z256vlh4

  ; change MCU frequency
  board_build.f_cpu = 48000000L


Uploading
---------
Freescale Kinetis FRDM-KL43Z supports the following uploading protocols:

* ``cmsis-dap``
* ``jlink``
* ``mbed``

Default protocol is ``mbed``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:frdm_kl43z]
  platform = freescalekinetis
  board = frdm_kl43z

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

Freescale Kinetis FRDM-KL43Z has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_cmsis-dap`
    - Yes
    - Yes
  * - :ref:`debugging_tool_jlink`
    - 
    - 

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_mbed`
      - Arm Mbed OS is a platform operating system designed for the internet of things