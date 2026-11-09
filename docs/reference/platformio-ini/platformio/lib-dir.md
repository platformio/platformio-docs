---
description: "A storage for the custom/private project libraries (platformio.ini option lib_dir)."
---

<a id="projectconf-pio-lib-dir"></a>

# `lib_dir` {#lib-dir}

- **Type:** Path
- **Multiple values:** No
- **Default:** `${PROJECT_DIR}/lib`
- **Environment variable:** [`PLATFORMIO_LIB_DIR`](../../environment-variables.md#envvar-PLATFORMIO_LIB_DIR), overrides the value in `platformio.ini`

You can put your own/private libraries here. The source code of each library should be placed in separate directory, like `lib/private_lib/[here are source files]`. This directory has the highest priority for [Library Dependency Finder (LDF)](../../../guides/libraries/ldf.md).

The default value is `lib`, meaning a `lib` directory located in the root of the project.

For example, see how the `Foo` and `Bar` libraries are organized:

```text
|--lib
|  |--Bar
|  |  |--docs
|  |  |--examples
|  |  |--src
|  |     |- Bar.c
|  |     |- Bar.h
|  |--Foo
|  |  |- Foo.c
|  |  |- Foo.h
|- platformio.ini
|--src
   |- main.c
```

Then in `src/main.c` you should use:

```c
#include <Foo.h>
#include <Bar.h>

// rest of H/C/CPP code
```

PlatformIO will find your libraries automatically, configure the preprocessor's include paths and build them.
