---
description: Library options of the platformio.ini [env] section.
---

<a id="projectconf-section-env-library"></a>

# Library options {#library-options}

Declare library dependencies and control how the Library Dependency Finder resolves them.

| Option | Description |
| --- | --- |
| [`lib_deps`](./lib-deps.md) | A list of project library dependencies which should be installed automatically before a build process |
| [`lib_ignore`](./lib-ignore.md) | A list of library names which should be ignored by Library Dependency Finder (LDF) |
| [`lib_extra_dirs`](./lib-extra-dirs.md) | A list of extra directories/storages where Library Dependency Finder (LDF) will look for dependencies |
| [`lib_ldf_mode`](./lib-ldf-mode.md) | Control how Library Dependency Finder (LDF) should analyze dependencies (`#include` directives) |
| [`lib_compat_mode`](./lib-compat-mode.md) | Configure a strictness (compatibility mode by frameworks, development platforms) of Library Dependency Finder (LDF) |
| [`lib_archive`](./lib-archive.md) | Create an archive (`*.a`, static library) from the object files and link it into a firmware (program) |
