# Program Memory Usage {#program-memory-usage}

PlatformIO calculates firmware/program memory usage based on the next segments:

<dl>

<dt>

`.text`

</dt>

<dd>

The code segment, also known as a text segment or simply as text, is where a portion of an object file or the corresponding section of the program's virtual address space that contains executable instructions is stored and is generally read-only and fixed size.

</dd>

<dt>

`.data`

</dt>

<dd>

The .data segment contains any global or static variables which have a pre-defined value and can be modified. The values for these variables are initially stored within the read-only memory (typically within `.text`) and are copied into the `.data` segment during the start-up routine of the program. Example,

```cpp
int val = 3;
char string[] = "Hello World";
```

</dd>

<dt>

`.bss`

</dt>

<dd>

Uninitialized data is usually adjacent to the data segment. The BSS segment contains all global variables and static variables that are initialized to zero or do not have explicit initialization in the source code. For instance, a variable defined as `static int i;` would be contained in the BSS segment.

</dd>

</dl>

The rough calculation could be done as:

- PROGRAM (Flash) = `.text` + `.data`
- DATA (RAM) = `.bss` + `.data`

If you need to print **all memory sections and addresses**, please use [`pio run --verbose`](../../reference/cli/pio-run.md#cmdoption-pio-run-v) command.

Recommended for reading:

- [https://en.wikipedia.org/wiki/Data_segment](https://en.wikipedia.org/wiki/Data_segment)
- [text, data and bss: Code and Data Size Explained](https://mcuoneclipse.com/2013/04/14/text-data-and-bss-code-and-data-size-explained/?utm_source=platformio&utm_medium=docs)
