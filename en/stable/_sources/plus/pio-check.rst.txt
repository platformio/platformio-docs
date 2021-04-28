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

.. |PIOCheck| replace:: **Static Code Analysis**

.. _piocheck:

Static Code Analysis
====================

**Automated code analysis without hassle!**

.. contents:: Contents
    :local:
    :depth: 1

Static analysis became an important part of software development cycle. It can
identify potential bugs, vulnerabilities and security threats by doing an
analysis on the source code level without having to test it on hardware or
execute any code.

|PIOCheck| helps reduce development cost by enabling engineers to detect the
precise location of defects and eliminate issues more efficiently and earlier
in the development cycle. It can also ensure compliance with internal or
industry coding standards such as MISRA, CERT, etc.

Key features
------------

  - Fully integrated within the PlatformIO ecosystem and easy to execute on the entire project.
  - Straightforward integration with :ref:`ci` services.
  - Possibility to reuse the same setup on other projects.
  - Easy and flexible rule configuration.
  - Comprehensive and detailed error information
  - Multiple architectures and development platforms.
  - Cross-platform: Windows, MacOS, Linux.

|PIOCheck| can detect a wide range of known defects in C/C++ code, including:
  - Potential NULL pointer dereferences
  - Possible indexing beyond array bounds
  - Suspicious assignments
  - Reads of potentially uninitialized objects
  - Unused variables or functions
  - Out of scope memory usage

.. warning::
  Before performing a static analysis check, make sure your project builds
  without errors. For information about how to build a project, see the
  :ref:`cmd_run` command or :ref:`ide_vscode` guide.

User Interface
--------------

There is the rich and friendly interface for |PIOCheck| in :ref:`piohome`.
It allows you to filter messages or directly jump to an issue in a source code.

.. image:: ../_static/images/home/pio-home-inspect-stats-check.png

.. image:: ../_static/images/home/pio-home-inspect-code-defects.png

Configuration
-------------

|PIOCheck| allows selecting what tool is used for finding defects in
the project, what source files are checked. |PIOCheck| can be configured
from :ref:`projectconf` using the next options:

.. toctree::
  :maxdepth: 2

  ../projectconf/section_env_check

.. _check_tools:

Check tools
-----------

You can switch between or specify multiple tools used for finding defects
using :ref:`projectconf_check_tool` option:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    check_tool = cppcheck, clangtidy


Detailed information about supported check tools and their configuration
process can be found on these pages:

.. toctree::
  :maxdepth: 1

  check-tools/cppcheck
  check-tools/clang-tidy
  check-tools/pvs-studio

.. _check_severity:

Defect severity
---------------

Defect severity is a classification of software defect (bug,
vulnerability, etc) that indicates the degree of negative impact on the quality
of software. |PIOCheck| uses the next classification of possible defects:

.. list-table::
    :header-rows:  1

    * - Severity
      - Meaning

    * - ``high``
      - Issues that are possibly bugs

    * - ``medium``
      - Suggestions about defensive programming in order to prevent potential bugs

    * - ``low``
      - Issues related to code cleanup and performance (unused functions, redundant code, const-ness, etc)


CLI Guide
---------

|PIOCheck| can be configured using command line commands. Detailed description
of these commands can be found here:

.. toctree::
  :maxdepth: 3

  pio check <../core/userguide/cmd_check>
