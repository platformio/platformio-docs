..  Copyright (c) 2019-present PlatformIO <contact@platformio.org>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _check_tool_pvsstudio:

PVS-Studio
==========

**PVS-Studio** is a static code analysis tool for detecting bugs and security weaknesses
in the source code of programs, written in C, C++, C# and Java. It analyze source code
intended for 32-bit, 64-bit and embedded ARM platforms.
Official page can be found `here  <https://www.viva64.com/en/pvs-studio/>`__.

.. contents:: Contents
    :local:

Features
--------

**PVS-Studio** performs a wide range of code checks, and it is also useful in finding
misprints and Copy-Paste errors. These checks are static analysis checks that can be
performed at a source code level. Some of the defects that might be detected include:

- Arithmetic over/underflow
- Array index out of bounds
- Undefined/unspecified behavior
- Incorrect usage of exceptions
- Buffer overrun
- Null pointer/null reference dereference
- Improper understanding of function/class operation logic
- Illegal bitwise/shift operations

The full list of supported checks can be found on
`the official webpage  <https://www.viva64.com/en/w/>`__.

Configuration
-------------

To enable **PVS-Studio** tool simply add it to the :ref:`projectconf_check_tool`
option in :ref:`projectconf`:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    check_tool = pvs-studio

Useful options that can be used used for adjusting check process:

.. toctree::
  :maxdepth: 2

  ../../projectconf/section_env_check

Extra flags
-----------

Useful flags that can help more precisely configure **PVS-Studio** to satisfy
your project requirements:

  .. list-table::
    :header-rows:  1

    * - Flag
      - Meaning

    * - ``--analysis-mode <arg>``
      - Analysis mode (``0`` - full analysis (default), ``1`` - 64-bit. analysis, ``2`` - reserved, ``4`` - general analysis, ``8`` - optimization, ``16`` - customer's specific requests, ``32`` - MISRA)

    * - ``--analyzer-errors <arg>``
      - Errors activation (Default: all errors is on)

    * - ``--errors-off <arg>``
      - Errors OFF (Default: all errors is on)

    * - ``--exclude-path <arg>``
      - All code that is located under the path will be excluded from analysis

    * - ``--lic-file <arg>``
      - Path to custom license file. Default locations ``~/.config/PVS-Studio/PVS-Studio.lic`` on Unix and ``%APPDATA%\PVS-Studio\PVS-Studio.lic`` on Windows

    * - ``--rules-config <arg>``
      - Specifies the path to rules configuration file.

    * - ``--platform <arg>``
      - Platform name (Win32, x64, etc) (Default: ``ARM``)


An example with a special analysis mode, disabled errors and license file:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    check_tool = pvs-studio
    check_flags =
      pvs-studio: --analysis-mode=4 --errors-off=V532,V586 --lic-file=/path/to/file.lic


Obtaining license
-----------------

Since **PVS-Studio** is a paid B2B solution, `a license <https://www.viva64.com/en/order>`__
should be purchased. But PVS-Studio can be used for free of charge, for example for 
checking open source projects. More information about the cases when you can get a free 
**PVS-Studio** license can be found on `the official webpage <https://www.viva64.com/en/open-source-license/>`__. 

.. tip::
    If you're experiencing problems with the license file or see the following error message:
    ``License information is incorrect. Please check your registration data or contact
    Customer Support``, try saving the license file in ``UTF-8 + BOM`` format with the
    following contents:
    
    .. code-block:: none

        name@domain.com
        AAAA-BBBB-CCCC-DDDD
    
    
