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

.. _ide_clion:

CLion
=====

The `CLion <https://www.jetbrains.com/clion/>`_ is a cross-platform C/C++ IDE
for Linux, OS X, and Windows integrated with the CMake build system. The
initial version will support the GCC and Clang compilers and GDB debugger.
Clion includes such features as a smart editor, code quality assurance,
automated refactorings, project manager, integrated version control systems.

Refer to the `CLion Documentation <https://www.jetbrains.com/clion/documentation/>`_
page for more detailed information.

.. image:: ../_static/ide/clion/ide-platformio-clion.png
    :target: ../_images/ide-platformio-clion.png

.. contents:: Contents
    :local:

Integration
-----------

Integration process consists of these steps:

1. Open system Terminal and install :ref:`installation_develop` of :ref:`piocore`
2. Create new folder for your project and change directory (``cd``) to it
3. Generate a project using PIO Core Project Generator (:option:`platformio init --ide`)
4. Import project in IDE.

------------

Choose board ``ID`` using :ref:`cmd_boards` or `Embedded Boards Explorer <http://platformio.org/boards>`_
command and generate project via :option:`platformio init --ide` command:

.. code-block:: shell

    platformio init --ide clion --board <ID>

    # For example, generate project for Arduino UNO
    platformio init --ide clion --board uno

Then:

1. Place source files (``*.c, *.cpp, *.h, *.hpp``) to ``src`` directory and
   repeat :option:`platformio init --ide` command above (to refresh source files list)
2. Import this project via ``Menu: File > Import Project``
   and specify root directory where is located :ref:`projectconf`
3. Open source file from ``src`` directory
4. Build project (*DO NOT* use "Run" button, see marks on the screenshot above):
   ``Menu: Run > Build``.

.. warning::

    1. :ref:`piocore` **DOES NOT** depend on ``Cmake``, it has own cross-platform
       Build System. All data related to build flags and source code filtering
       should be specified using :ref:`projectconf_section_env_build` in
       :ref:`projectconf`.

    2. See know issue: :ref:`ide_clion_knownissues_inopde_not_supported` and how
    to resolve it.

There are 6 predefined targets for building (*NOT FOR RUNNING*, see marks on
the screenshot above):

* ``PLATFORMIO_BUILD`` - Build project without auto-uploading
* ``PLATFORMIO_UPLOAD`` - Build and upload (if no errors)
* ``PLATFORMIO_CLEAN`` - Clean compiled objects
* ``PLATFORMIO_TEST`` - :ref:`unit_testing`
* ``PLATFORMIO_PROGRAM`` - Build and upload using external programmer
  (if no errors), see :ref:`atmelavr_upload_via_programmer`
* ``PLATFORMIO_UPLOADFS`` - Upload files to file system SPIFFS,
  see :ref:`platform_espressif_uploadfs`
* ``PLATFORMIO_UPDATE`` - Update installed platforms and libraries via :ref:`cmd_update`
* ``PLATFORMIO_REBUILD_PROJECT_INDEX`` - Rebuild C/C++ Index for the Project.
  Allows to fix code completion and code linting issues.


PlatformIO Project Generator created "File Watchers" configuration to monitor
changes in ``platformio.ini`` and automatically rebuild C/C++ Project Index.
**You need to install extra plugin** named ``File Watchers`` via
"Clion: Preferences > Plugins" to enable this feature.

.. warning::
    The libraries which are added, installed or used in the project
    after generating process will not be reflected in IDE. To fix it please run
    ``PLATFORMIO_REBUILD_PROJECT_INDEX`` target.

Known issues
------------

.. _ide_clion_knownissues_inopde_not_supported:

Arduino ``.ino`` files are not supported
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CLion uses "CMake" tool for code completion and code linting. As result, it
doesn't support Arduino files (``*.ino`` and ``.pde``) because they are
not valid C/C++ based source files:

1. Missing includes such as ``#include <Arduino.h>``
2. Function declarations are omitted.

See how to :ref:`faq_convert_ino_to_cpp`.

Articles / Manuals
------------------

* Dec 01, 2015 - **JetBrains CLion Blog** - `C++ Annotated: Fall 2015. Arduino Support in CLion using PlatformIO <http://blog.jetbrains.com/clion/2015/12/cpp-annotated-fall-2015/>`_
* Nov 22, 2015 - **Michał Seroczyński** - `Using PlatformIO to get started with Arduino in CLion IDE <http://www.ches.pl/using-platformio-get-started-arduino-clion-ide/>`_
* Nov 09, 2015 - **ÁLvaro García Gómez** - `Programar con Arduino "The good way" (Programming with Arduino "The good way", Spanish) <http://congdegnu.es/2015/11/09/programar-con-arduino-the-good-way/>`_

See more :ref:`articles`.
