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

.. _check_tool_cppcheck:

Cppcheck
========

**Cppcheck** is a static analysis tool for C/C++ code. It provides a unique
code analysis to detect bugs and focuses on detecting undefined behavior and
dangerous coding constructs. The goal is to detect only real errors in the
code (i.e. have very few false positives). More information about this tool on
`the official webpage  <http://cppcheck.sourceforge.net>`__.

.. hint::
  Cppcheck is rarely wrong about reported errors. But there are many bugs that
  it doesn't detect. You will find more bugs in your software by testing your
  software carefully than by using Cppcheck.

.. contents:: Contents
    :local:

Features
--------

**Cppcheck** supports a wide variety of static checks that may not be covered
by the compiler itself. These checks are static analysis checks that can be
performed at a source code level. The program is directed towards static
analysis checks that are rigorous, rather than heuristic in nature.

Some of the defects that might be detected include:
  - Automatic variable checking
  - Bounds checking for array overruns
  - Classes checking (e.g. unused functions, variable initialization, and memory duplication)
  - Usage of deprecated or superseded functions
  - Exception safety checking, for example, usage of memory allocation and destructor checks
  - Memory leaks, e.g. due to lost scope without deallocation
  - Resource leaks, e.g. due to forgetting to close a file handle
  - Invalid usage of Standard Template Library functions and idioms
  - Miscellaneous stylistic and performance errors

Additional checks
-----------------

Be default **Cppcheck** is configured to check the next additional defects:

- ``warning``
- ``style``
- ``performance``
- ``portability``
- ``unusedFunction``

The full list of supported check with detailed description is located on
`the official webpage  <https://sourceforge.net/p/cppcheck/wiki/ListOfChecks/>`__.

Configuration
-------------

**Cppcheck** is implicitly used as the default check tool when :ref:`projectconf_check_tool`
option in :ref:`projectconf` is not set. To be explicit, you can specify it
in the configuration directly:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    check_tool = cppcheck
    check_flags = --enable=all

Useful options that can be used used for adjusting check process:

.. toctree::
  :maxdepth: 2

  ../../projectconf/section_env_check

Extra flags
-----------

Useful flags that can help more precisely configure **Cppcheck** to satisfy
your project requirements:

  .. list-table::
    :header-rows:  1

    * - Flag
      - Meaning

    * - ``--enable=<id>``
      - Enable additional checks. The available ids are: ``all``, ``warning``, ``style``, ``performance``, ``portability``, ``information``, ``unusedFunction``, ``missingInclude``

    * - ``--std=<id>``
      - Set standard. The available options are: ``c89``, ``c99``, ``c11``, ``c++03``, ``c++11``, ``c++14``, ``c++17``, ``c++20 (default)``

    * - ``--language=<language>``
      - Forces **Cppcheck** to check all files as the given language. Valid values are: ``c``, ``c++``

    * - ``--inline-suppr``
      - Enable inline suppressions. Use them by placing one or more comments, like: ``// cppcheck-suppress warningId`` on the lines before the warning to suppress (enabled by default if no extra flags specified).

    * - ``--suppress=<spec>``
      - Suppress warnings that match ``<spec>``. The format of ``<spec>`` is: ``[error id]:[filename]:[line]``

    * - ``--platform=<type>``
      - Specifies platform-specific types and sizes. The available built-in platforms are: ``unix32``, ``unix64``, ``win32A``, ``win32W``, ``win64``, ``avr8``, ``native``, ``unspecified (default)``

    * - ``--inconclusive``
      - Allow reporting defects even though the analysis is inconclusive.

    * - ``-D<ID>``
      - Define a preprocessor symbol. Example: ``-DDEBUG=1``

    * - ``-U<ID>``
      - Undefine preprocessor symbol. Use -U to explicitly hide certain #ifdef <ID> code paths from checking. Example: ``-UDEBUG``

    * - ``-I <dir>``
      - Give a path to search for include files. Give several -I parameters to give several paths.

    * - ``-j <jobs>``
      - Start ``<jobs>`` threads to do the checking simultaneously.

Suppressing warnings
--------------------
It might be useful to explicitly instruct **Cppcheck** to ignore some of the
known defects in project codebase. Since ``--inline-suppr`` is enabled by
default, it's possible to directly mark pieces of code that will be excluded
from **Cppcheck** report using ``// cppcheck-suppress warningId`` syntax.

.. note::
  Warning ID can be found in square brackets at the end of defect description, for example:
  ``src\Blink.cpp:17: [low:style] The function 'loop' is never used. [unusedFunction]``

By default, :ref:`piocheck` command doesn't scan framework sources and that's
why some functions from in your project might be reported as unused. For example,
you can ignore warnings about ``setup`` and ``loop`` functions from
Arduino-based projects:

.. code-block:: c

    // cppcheck-suppress unusedFunction
    void setup()
    {
      ...
    }

    // cppcheck-suppress unusedFunction
    void loop()
    {
      ...
    }

Addons (MISRA, CERT)
--------------------

**Cppcheck** provides several addon scripts that analyze dump files to check
compatibility with secure coding standards and to locate various issues.
Most useful addons for verifying compliance with popular guidelines are
**MISRA** and **CERT**.

MISRA
~~~~~

``MISRA`` is a proprietary set of software development guidelines for the
C/C++ programming languages developed by MISRA (Motor Industry Software
Reliability Association).  It aims to facilitate code safety, security,
portability, and reliability  in the context of embedded systems, specifically
those systems programmed in ISO C/C++.

.. note::
  Since this standard is proprietary, **Cppcheck** does not display error text
  by specifying only the number of violated rules (for example, [c2012-21.3]).
  If you want to display full texts for violated rules, you will need to
  create a text file containing MISRA rules, which you will have to pass when
  calling the script with ``--rule-texts`` flag.

In order to use ``MISRA`` addon you will need to provide a special file with
the description of ``MISRA`` rules. Usually, it has the next contents:

.. code-block:: ini

  Appendix A Summary of guidelines
  Rule 3.1 Required
  R3.1 Rule description
  Rule 4.1 Required
  ...
  Rule 21.3 Required
  R21.3 Rule description
  Rule 21.4
  R21.4 Rule description

Next, you need to instruct **Cppcheck** that you want to run an additional
addon script. Since this script requires an additional file with rules,
you can pass it via a special ``json`` file:

.. code-block:: json

    {
      "script": "addons/misra.py",
      "args": ["--rule-texts=misra-rules.txt"]
    }

Finally, add new flag to :ref:`projectconf_check_flags`:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    check_tool = cppcheck
    check_flags =
      cppcheck: --addon=misra.json

The full list of implemented ``MISRA`` checks can be found on
`the official webpage  <http://cppcheck.sourceforge.net/misra.php>`__.

CERT
~~~~

``SEI CERT`` coding standard provides rules for secure coding in the C
programming language. The goal of these rules and recommendations is to
develop safe, reliable, and secure systems, for example by eliminating
undefined behaviors that can lead to undefined program behaviors and
exploitable vulnerabilities.

In order to use the ``CERT`` addon, simply specify it as an additional flag in
:ref:`projectconf_check_flags` section:

.. code-block:: ini

    [env:myenv]
    platform = ...
    board = ...
    check_tool = cppcheck
    check_flags =
      cppcheck: --addon=cert.py
