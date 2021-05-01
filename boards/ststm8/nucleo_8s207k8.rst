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

.. _board_ststm8_nucleo_8s207k8:

NUCLEO-8S207K8
==============

.. contents::

Hardware
--------

Platform :ref:`platform_ststm8`: The STM8 is an 8-bit microcontroller family by STMicroelectronics an extended variant of the ST7 microcontroller architecture. STM8 microcontrollers are particularly low cost for a full-featured 8-bit microcontroller.

.. list-table::

  * - **Microcontroller**
    - STM8S207K8T6
  * - **Frequency**
    - 16MHz
  * - **Flash**
    - 64KB
  * - **RAM**
    - 6KB
  * - **Vendor**
    - `STMicroelectronics <https://www.st.com/en/evaluation-tools/nucleo-8s207k8.html?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``nucleo_8s207k8`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:nucleo_8s207k8]
  platform = ststm8
  board = nucleo_8s207k8

You can override default NUCLEO-8S207K8 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `nucleo_8s207k8.json <https://github.com/platformio/platform-ststm8/blob/master/boards/nucleo_8s207k8.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:nucleo_8s207k8]
  platform = ststm8
  board = nucleo_8s207k8

  ; change microcontroller
  board_build.mcu = stm8s207k8t6

  ; change MCU frequency
  board_build.f_cpu = 16000000L


Uploading
---------
NUCLEO-8S207K8 supports the following uploading protocols:

* ``serial``
* ``stlinkv21``

Default protocol is ``stlinkv21``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:nucleo_8s207k8]
  platform = ststm8
  board = nucleo_8s207k8

  upload_protocol = stlinkv21

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

NUCLEO-8S207K8 has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_stlink`
    - Yes
    - Yes

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_spl`
      - The ST Standard Peripheral Library provides a set of functions for handling the peripherals on the STM32 family of microcontrollers.