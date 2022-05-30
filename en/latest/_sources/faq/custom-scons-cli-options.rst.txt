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

Custom SCons command-line options
---------------------------------

PlatformIO is built on top of the open-source software construction tool called SCons.
SCons has many useful command-line options that control its behavior and may come in
handy to know the exact internal processes happening in SCons when it builds a target.
For example:

- ``--dry-run`` configures SCons to print the commands that would be executed to build
  any target, but do not execute the commands.
- ``--tree=all`` forces SCons to print file dependency tree including implicit and
  ignored dependencies
- ``--debug=explain`` will print an explanation of why SCons decides to (re-)build the
  targets it selects for building.

The list of available command-line options can be found in the
official `SCons documentation <https://scons.org/doc/production/HTML/scons-user/ch10.html#sect-command-line-options>`_.

The easiest way to pass extra command-line options to the SCons build system used in
PlatformIO is via the external ``SCONSFLAGS`` environment variable:

.. code-block::

    # POSIX shell
    export SCONSFLAGS="--tree=all"

    # Windows CMD
    C:\Users\foo> set SCONSFLAGS=--dry-run
