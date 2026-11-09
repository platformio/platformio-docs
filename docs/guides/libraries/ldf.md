<a id="ldf"></a>

# Library Dependency Finder (LDF) {#library-dependency-finder-ldf}

Library Dependency Finder is a core part of PlatformIO Build System that operates with the C/C++ source files and looks for `#include ...` directives to know what header directories to include for the compiler.

In spite of the fact that Library Dependency Finder is written in pure Python, it evaluates [C/C++ Preprocessor conditional syntax](#ldf-c-cond-syntax) (`#ifdef`, `if`, `defined`, `else`, and `elif`) without calling `gcc -E`. This approach allows to significantly reduce the total compilation time. See [Dependency Finder Mode](#ldf-mode) for more details.

## Configuration {#configuration}

Library Dependency Finder can be configured from ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md):

- [Library options](../../reference/platformio-ini/env/library-options.md)

  - [`lib_deps`](../../reference/platformio-ini/env/lib-deps.md)
  - [`lib_ignore`](../../reference/platformio-ini/env/lib-ignore.md)
  - [`lib_extra_dirs`](../../reference/platformio-ini/env/lib-extra-dirs.md)
  - [`lib_ldf_mode`](../../reference/platformio-ini/env/lib-ldf-mode.md)
  - [`lib_compat_mode`](../../reference/platformio-ini/env/lib-compat-mode.md)
  - [`lib_archive`](../../reference/platformio-ini/env/lib-archive.md)

<a id="ldf-storage"></a>

## Storage {#storage}

There are different storages where Library Dependency Finder looks for libraries. These storages (folders) have priority and LDF operates in the next order:

1. [lib_dir](../../reference/platformio-ini/platformio/lib-dir.md) - own/private library storage per project
2. [libdeps_dir](../../reference/platformio-ini/platformio/libdeps-dir.md) - project dependency storage used by [Library Management](./index.md)
3. "[core_dir](../../reference/platformio-ini/platformio/core-dir.md)/lib" - global storage per all projects.
4. Library storages built into frameworks, SDKs.

<a id="ldf-mode"></a>

## Dependency Finder Mode {#dependency-finder-mode}

Library Dependency Finder starts work from analyzing source files of the project ([src_dir](../../reference/platformio-ini/platformio/src-dir.md)) and can work in the next modes:

<dl>

<dt>

`off`

</dt>

<dd>

"Manual mode", does not process source files of a project and dependencies. Builds only the libraries that are specified in manifests ([library.json](../../reference/library-json/index.md), `module.json`) or using [lib_deps](../../reference/platformio-ini/env/lib-deps.md) option.

</dd>

<dt>

`chain`

</dt>

<dd>

\[**DEFAULT**\] Parses ALL C/C++ source files of the project and follows only by nested includes (`#include ...`, chain...) from the libraries. It also parses C, CC, CPP files from libraries which have the same name as included header file. **Does not evaluate** [C/C++ Preprocessor conditional syntax](#ldf-c-cond-syntax).

</dd>

<dt>

`deep`

</dt>

<dd>

Parses ALL C/C++ source files of the project and parses ALL C/C++ source files of the each found dependency (recursively). **Does not evaluate** [C/C++ Preprocessor conditional syntax](#ldf-c-cond-syntax).

</dd>

<dt>

`chain+`

</dt>

<dd>

The same behavior as for the `chain` but **evaluates** [C/C++ Preprocessor conditional syntax](#ldf-c-cond-syntax).

</dd>

<dt>

`deep+`

</dt>

<dd>

The same behavior as for the `deep` but **evaluates** [C/C++ Preprocessor conditional syntax](#ldf-c-cond-syntax).

</dd>

</dl>

The mode can be changed using [lib_ldf_mode](../../reference/platformio-ini/env/lib-ldf-mode.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md). Default value is set to `chain`.

:::note

Once a library is picked by the LDF for the build process, all source files according to its manifest file will be built.

:::

:::note

Usually, when the LDF appears to fail to identify a dependency of a library, it is because the dependency is only referenced from a library source file, and not a library header file (see example below). In this case, it is necessary to either explicitly reference the dependency from the project source or ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) ([lib_deps](../../reference/platformio-ini/env/lib-deps.md) option), or change the LDF mode to "deep" (not generally recommended).

:::

A difference between `chain/chain+` and `deep/deep+` modes. For example, there are 2 libraries:

- Library `Foo` with files:

  - `Foo/foo.h`
  - `Foo/foo.cpp`
  - `Foo/extra.cpp`

- Library `Bar` with files:

  - `Bar/bar.h`
  - `Bar/bar.cpp`

<dl>

<dt>

Case 1

</dt>

<dd>

- `lib_ldf_mode = chain`
- `Foo/foo.h` depends on the `Bar` library (contains `#include <bar.h>`)
- `#include <foo.h>` is located in one of the project source files

Here the nested includes (`project file > foo.h > bar.h`) and LDF will find both libraries `Foo` and `Bar`.

</dd>

<dt>

Case 2

</dt>

<dd>

- `lib_ldf_mode = chain`
- `Foo/extra.cpp` depends on the `Bar` library (contains `#include <bar.h>`)
- `#include <foo.h>` is located in one of the project source files

In this case, LDF will not find the `Bar` library because it doesn't know about the CPP file (`Foo/extra.cpp`).

</dd>

<dt>

Case 3

</dt>

<dd>

- `lib_ldf_mode = deep`
- `Foo/extra.cpp` depends on `Bar` library (contains `#include <bar.h>`)
- `#include <foo.h>` is located in one of the project source files

Firstly, LDF finds the `Foo` library, then it parses all sources from the `Foo` library and finds `Foo/extra.cpp` that depends on `#include <bar.h>`.  Secondly, it will parse all sources from the `Bar` library. This operation continues until all dependencies will not be parsed.

</dd>

</dl>

<a id="ldf-compat-mode"></a>

## Compatibility Mode {#compatibility-mode}

Compatibility mode allows one to control strictness of Library Dependency Finder. If library contains one of manifest file ([library.json](../../reference/library-json/index.md), `library.properties`, `module.json`), then LDF check compatibility of this library with real build environment. Available compatibility modes:

<dl>

<dt>

`off`

</dt>

<dd>

Does not check for compatibility (is not recommended)

</dd>

<dt>

`soft`

</dt>

<dd>

\[**DEFAULT**\] Checks for the compatibility with [framework](../../reference/platformio-ini/env/framework.md) from build environment

</dd>

<dt>

`strict`

</dt>

<dd>

Checks for the compatibility with [framework](../../reference/platformio-ini/env/framework.md) and [platform](../../reference/platformio-ini/env/platform.md) from build environment.

</dd>

</dl>

This mode can be changed using [lib_compat_mode](../../reference/platformio-ini/env/lib-compat-mode.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md). Default value is set to `soft`.

<a id="ldf-c-cond-syntax"></a>

## C/C++ Preprocessor conditional syntax {#c-c-preprocessor-conditional-syntax}

In spite of the fact that Library Dependency Finder is written in pure Python, it evaluates [C/C++ Preprocessor conditional syntax](https://gcc.gnu.org/onlinedocs/cpp/Conditional-Syntax.html#Conditional-Syntax) (`#ifdef`, `if`, `defined`, `else`, and `elif`) without calling `gcc -E`. For example,

`platformio.ini`

```ini
[env:myenv]
lib_ldf_mode = chain+
build_flags = -D MY_PROJECT_VERSION=13
```

`mylib.h`

```c
#ifdef MY_PROJECT_VERSION
// include common file for the project
#include "my_common.h"
#endif

#if MY_PROJECT_VERSION < 10
// this include will be ignored because does not satisfy condition above
#include "my_old.h"
#endif
```
