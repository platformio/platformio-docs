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

``debug_server_ready_pattern``
------------------------------

Type: ``String`` | Multiple: ``No``

A pattern to determine when debugging server is ready for an incoming connection.
The pattern applies tool debugging server process's STDOUT and STDERR outputs.

A regular expression (RegExp) is allowed if the pattern starts with ``-`` character.
See `Python regular expression operations <https://docs.python.org/3/library/re.html>`_
for syntax and details.

Examples:

.. code-block:: ini

    [env:custom_debug_server_ready_pattern]
    ...

    ; match by string
    debug_server_ready_pattern = Waiting for GDB connection

    ; match by regular expression
    debug_server_ready_pattern = -.*Listening on port \d+ for gdb connections
