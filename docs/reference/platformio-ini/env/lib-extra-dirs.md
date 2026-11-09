<a id="projectconf-lib-extra-dirs"></a>

# `lib_extra_dirs` {#lib-extra-dirs}

:::info

Deprecated since version 6.0: The `lib_extra_dirs` option has been deprecated and will be removed in the next major release.

If you need to use an external local library that is not part of the project, please utilize the [Local Folder](../../cli/pio-pkg/install.md#cmd-pkg-install-local-folder) and "Symbolic Link" features.

```ini
[env:myenv]
lib_deps =
    FooLib=symlink://../../shared-libraries/FooLib
```

:::

---

Type: `DirPath` | Multiple: `Yes`

A list with extra directories/storages where [Library Dependency Finder (LDF)](../../../guides/libraries/ldf.md) will look for dependencies.

:::warning

This is a not direct path to a library with source code. It should be a path to storage that contains libraries grouped by folders. For example, `D:\PlatformIO\extra\libraries` but not `D:\PlatformIO\extra\libraries\FooLibrary`.

:::

Example:

```ini
[env:myenv]
lib_extra_dirs =
    /common/libraries
    /iot/libraries
```
