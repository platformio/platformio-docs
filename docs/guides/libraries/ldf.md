---
description: How the Library Dependency Finder decides which libraries to build, its modes and its search order.
---

# Library Dependency Finder (LDF)

The Library Dependency Finder (LDF) is the part of the PlatformIO build system
that decides which libraries to build. It scans your source files for
`#include` directives, finds the libraries that provide those headers, and adds
them, and the libraries they include in turn, to the build.

The LDF can also evaluate [preprocessor conditionals](#ldf-c-cond-syntax)
(`#ifdef`, `#if`, `defined`, `#else`, `#elif`) without running the
preprocessor, which keeps it fast. See [Dependency Finder mode](#ldf-mode).

## Configuration {#configuration}

Configure the LDF with the [library options](../../reference/platformio-ini/env/library-options.md)
in `platformio.ini`, mainly [`lib_ldf_mode`](../../reference/platformio-ini/env/lib-ldf-mode.md),
[`lib_compat_mode`](../../reference/platformio-ini/env/lib-compat-mode.md),
[`lib_extra_dirs`](../../reference/platformio-ini/env/lib-extra-dirs.md) and
[`lib_ignore`](../../reference/platformio-ini/env/lib-ignore.md).

<a id="ldf-storage"></a>

## Storage {#storage}

The LDF looks for libraries in these folders, in this order of priority:

1. The folders in [`lib_extra_dirs`](../../reference/platformio-ini/env/lib-extra-dirs.md), if any.
2. [`lib_dir`](../../reference/platformio-ini/platformio/lib-dir.md): the project's private libraries (`lib/`).
3. [`libdeps_dir`](../../reference/platformio-ini/platformio/libdeps-dir.md)`/<environment>`:
   the dependencies installed from [`lib_deps`](../../reference/platformio-ini/env/lib-deps.md).
4. [`globallib_dir`](../../reference/platformio-ini/platformio/globallib-dir.md):
   libraries installed globally (deprecated).
5. Libraries bundled with the framework or SDK.

<a id="ldf-mode"></a>

## Dependency Finder mode {#dependency-finder-mode}

The LDF starts from the project's source files ([`src_dir`](../../reference/platformio-ini/platformio/src-dir.md)) and works in one of these modes:

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

Set the mode with [`lib_ldf_mode`](../../reference/platformio-ini/env/lib-ldf-mode.md). The default is `chain`.

:::note

Once the LDF selects a library, all its source files (as defined by its manifest) are built.

:::

:::note

When the LDF misses a library's dependency, it is usually because the dependency is included only from one of the library's source files, not from its headers (see case 2 below). Then either include the dependency from your own code, add it to [`lib_deps`](../../reference/platformio-ini/env/lib-deps.md), or switch to a `deep` mode (slower).

:::

The following cases show the difference between the `chain` and `deep` modes, with two libraries:

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

The LDF follows the chain of includes (project file > `foo.h` > `bar.h`) and finds both `Foo` and `Bar`.

</dd>

<dt>

Case 2

</dt>

<dd>

- `lib_ldf_mode = chain`
- `Foo/extra.cpp` depends on the `Bar` library (contains `#include <bar.h>`)
- `#include <foo.h>` is located in one of the project source files

The LDF does not find `Bar`, because in `chain` mode it does not scan `Foo/extra.cpp`.

</dd>

<dt>

Case 3

</dt>

<dd>

- `lib_ldf_mode = deep`
- `Foo/extra.cpp` depends on `Bar` library (contains `#include <bar.h>`)
- `#include <foo.h>` is located in one of the project source files

The LDF finds `Foo`, scans all its sources, finds `#include <bar.h>` in `Foo/extra.cpp`, and adds `Bar`. It then scans `Bar` the same way, until no new dependencies are found.

</dd>

</dl>

<a id="ldf-compat-mode"></a>

## Compatibility mode {#compatibility-mode}

The compatibility mode controls whether the LDF skips libraries that are not compatible with the environment. Compatibility is read from the library's manifest ([`library.json`](../../reference/library-json/index.md), `library.properties` or `module.json`). The modes:

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

Set the mode with [`lib_compat_mode`](../../reference/platformio-ini/env/lib-compat-mode.md). The default is `soft`.

<a id="ldf-c-cond-syntax"></a>

## C/C++ preprocessor conditional syntax {#c-c-preprocessor-conditional-syntax}

In the `chain+` and `deep+` modes, the LDF evaluates [preprocessor conditionals](https://gcc.gnu.org/onlinedocs/cpp/Conditional-Syntax.html) (`#ifdef`, `#if`, `defined`, `#else`, `#elif`) with the macros from your build flags, and ignores includes in branches that are not taken. For example:

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
