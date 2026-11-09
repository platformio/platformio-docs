---
description: How PlatformIO calculates the flash and RAM usage of a program from its .text, .data and .bss sections.
---

# Program memory usage

After a build, PlatformIO reports how much flash and RAM the program uses. By
default, it computes these from three sections of the program:

| Section | Contains | Stored in |
| --- | --- | --- |
| `.text` | The program code and constant data. Read-only. | Flash |
| `.data` | Global and static variables with an initial value. The initial values are stored in flash and copied to RAM at startup. | Flash and RAM |
| `.bss` | Global and static variables that are zero-initialized or have no initializer, such as `static int i;`. | RAM |

Example of variables in `.data`:

```cpp
int val = 3;
char string[] = "Hello World";
```

The reported sizes are:

- **Flash** = `.text` + `.data`
- **RAM** = `.data` + `.bss`

Some development platforms calculate the sizes their own way, for example to
account for additional memory regions.

The RAM figure covers only static data: the stack and heap are not included.

To print all memory sections and their addresses, build with
[`pio run --verbose`](../../reference/cli/pio-run.md#cmdoption-pio-run-v).

Further reading:

- [Data segment](https://en.wikipedia.org/wiki/Data_segment) (Wikipedia)
- [text, data and bss: code and data size explained](https://mcuoneclipse.com/2013/04/14/text-data-and-bss-code-and-data-size-explained/?utm_source=platformio&utm_medium=docs)
