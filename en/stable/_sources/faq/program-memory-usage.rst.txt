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

Program Memory Usage
--------------------

PlatformIO calculates firmware/program memory usage based on the next segments:

:``.text``:

    The code segment, also known as a text segment or simply as
    text, is where a portion of an object file or the corresponding section of
    the program's virtual address space that contains executable instructions
    is stored and is generally read-only and fixed size.

:``.data``:

    The .data segment contains any global or static variables which have a
    pre-defined value and can be modified. The values for these variables are
    initially stored within the read-only memory (typically within ``.text``)
    and are copied into the ``.data`` segment during the start-up routine of
    the program. Example,

    .. code-block:: cpp

         int val = 3;
         char string[] = "Hello World";

:``.bss``:

     Uninitialized data is usually adjacent to the data segment. The BSS
     segment contains all global variables and static variables that are
     initialized to zero or do not have explicit initialization in the source code.
     For instance, a variable defined as ``static int i;`` would be contained
     in the BSS segment.

The rough calculation could be done as:

* PROGRAM (Flash) = ``.text`` + ``.data``
* DATA (RAM) = ``.bss`` + ``.data``

If you need to print **all memory sections and addresses**, please use
:option:`pio run --verbose` command.

Recommended for reading:

* https://en.wikipedia.org/wiki/Data_segment
* `text, data and bss: Code and Data Size Explained <https://mcuoneclipse.com/2013/04/14/text-data-and-bss-code-and-data-size-explained/?utm_source=platformio&utm_medium=docs>`_
