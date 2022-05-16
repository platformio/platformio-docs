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

.. _check:

Static Code Analysis
====================

**Automated code analysis without hassle!**

Static analysis became an important part of software development cycle. It can
identify potential bugs, vulnerabilities and security threats by doing an
analysis on the source code level without having to test it on hardware or
execute any code.

**Static Code Analysis** helps reduce development cost by enabling engineers to detect the
precise location of defects and eliminate issues more efficiently and earlier
in the development cycle. It can also ensure compliance with internal or
industry coding standards such as MISRA, CERT, etc.

**Key features**

- Fully integrated within the PlatformIO ecosystem and easy to execute on the entire project.
- Straightforward integration with :ref:`ci` services.
- Possibility to reuse the same setup on other projects.
- Easy and flexible rule configuration.
- Comprehensive and detailed error information
- Multiple architectures and development platforms.
- Cross-platform: Windows, MacOS, Linux.

**Static Code Analysis** can detect a wide range of known defects in C/C++ code, including:

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

.. toctree::
  :maxdepth: 2

  ui
  severity
  configuration
  tools/index
  cli
