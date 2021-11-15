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

Tutorials
---------

* :ref:`tutorial_stm32cube_debugging_unit_testing`


Configuration Options
---------------------

Custom Configuration Header
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Type: ``Bool (yes or no)`` | Multiple: ``No`` | Default: ``no``

STM32Cube-based projects require a special configuration header file that contains
several essential macros (oscillator adaptations, caching settings, etc.) and controls
what framework modules (ADC, DMA, etc.) are enabled.

By default, PlatformIO uses a template header file shipped with the framework package
``stm32YYxx_hal_conf_template.h`` and renames it to ``stm32YYxx_hal_conf.h`` expected by
the internal framework implementation. This behavior can be disabled via a special
option ``custom_config_header`` set in :ref:`projectconf`, for example:

.. code-block:: ini

    [env:nucleo_f401re]
    platform = ststm32
    framework = stm32cube
    board = nucleo_f401re
    board_build.stm32cube.custom_config_header = yes

Note that the location for the custom configuration header is not strictly limited as
long as the path to this file is visible to the build system.

Custom System Setup Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Type: ``Bool (yes or no)`` | Multiple: ``No`` | Default: ``no``

Besides project source files, STM32Cube requires additional code to properly startup
the MCU and prepare a runtime environment. By default, PlatformIO is capable of compiling
default implementations shipped with the framework according to the MCU field specified
in a board manifest. If this functionality is already implemented as part of your project,
you can force PlatformIO to skip adding default implementations via the ``custom_system_setup``
option, for example:

.. code-block:: ini

    [env:nucleo_f401re]
    platform = ststm32
    framework = stm32cube
    board = nucleo_f401re
    board_build.stm32cube.custom_system_setup = yes


Selecting System File
~~~~~~~~~~~~~~~~~~~~~

Type: ``String`` | Multiple: ``No`` | Default: ``Dynamically selected``

This file (e.g. ``system_stm32f0xx.c``) is responsible for basic system initialization
that is called after the reset routine and before jumping to the ``main`` function.
In most cases, this option won't be needed as the STM32Cube framework provides
only one default implementation. It's mostly used with dual-core targets (e.g. ``STM32H7``)
which can have several implementations for different boot settings of available CPU cores.
The desired implementation can be selected via a special option ``system_file``
in :ref:`projectconf`, for example:

.. code-block:: ini

    [env:disco_h747xi]
    platform = ststm32
    framework = stm32cube
    board = disco_h747xi
    board_build.stm32cube.system_file = system_stm32h7xx_dualcore_bootcm7_cm4gated.c


Custom Startup File
~~~~~~~~~~~~~~~~~~~

Type: ``String`` | Multiple: ``No`` | Default: ``Dynamically selected``

The Startup File (e.g. ``startup_stm32f205xx.s``) is responsible for preparing a proper
runtime environment before calling the ``main`` function. It contains a minimal
interrupt vector table (including ``ResetHanlder`` implementation), sets stack pointer
and program counter, initializes memory, etc. In most cases, PlatformIO is capable of
automatically selecting a proper startup file according to the MCU field specified in a
board manifest. In case this feature fails, it's possible to manually specify the desired
startup file, for example:

.. code-block:: ini

    [env:custom_board_name]
    platform = ststm32
    framework = stm32cube
    board = custom_board_name
    board_build.stm32cube.startup_file = startup_stm32l152xca.s


Disabling Bundled Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Type: ``Bool (yes or no)`` | Multiple: ``No`` | Default: ``no``

By default, PlatformIO adds dynamic library manifests to STM32Cube components (BSPs,
middleware, etc.), so :ref:`ldf` can be used to resolve project dependencies and
suitable components will be added to the build process as standalone libraries.
If your project doesn't require this feature, it can be disabled via the
``disable_embedded_libs`` option, for example:

.. code-block:: ini

    [env:disco_f303vc]
    platform = ststm32
    framework = stm32cube
    board = disco_f303vc
    board_build.stm32cube.disable_embedded_libs = yes


Custom Build Variant
~~~~~~~~~~~~~~~~~~~~

Type: ``String`` | Multiple: ``No`` | Default: ``None``

The STM32Cube framework for each MCU family may contain Board Support Packages (BSPs)
for various development kits. These BSPs mostly contain drivers for on-board hardware
modules (displays, sensors, etc.). The ``variant`` option is used to select what
target-specific macros should be used when compiling BSP components, for example:

.. code-block:: ini

    [env:nucleo_g474re]
    platform = ststm32
    framework = stm32cube
    board = nucleo_g474re
    board_build.stm32cube.variant = STM32G4xx_Nucleo

Custom DSP Library
~~~~~~~~~~~~~~~~~~

Type: ``Bool (yes or no)`` | Multiple: ``No`` | Default: ``no``

The STM32Cube contains header files and precompiled static archives for commonly used
DSP functions. By default, PlatformIO adds paths to these headers and archives to each
STM32Cube-based project. If a project already has its own implementation of the DSP
library and to avoid possible conflicts with the default DSP library shipped with the
framework, the ``custom_dsp_library`` can be used:

.. code-block:: ini

    [env:nucleo_f401re]
    platform = ststm32
    framework = stm32cube
    board = nucleo_f401re
    board_build.stm32cube.custom_dsp_library = yes

Using with STM32CubeMX
----------------------

At the moment there is no seamless integration with projects generated by *STM32CubeMX*
tool. Instead, a small cross-platform Python application called ``stm32pio``
can be used to create and update PlatformIO projects from *STM32CubeMX* ``.ioc`` files.
It uses *STM32CubeMX* to generate a HAL-framework-based code and alongside creates
PlatformIO project with compatible parameters to stick them both together.

More details about ``stm32pio`` tool can be found in `the official repository <https://github.com/ussserrr/stm32pio>`_. 

