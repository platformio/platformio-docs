---
description: Declare, install and update library dependencies with the PlatformIO library manager.
---

<a id="librarymanager"></a>

# Library management {#library-management}

PlatformIO manages the libraries your project uses: you declare them in
`platformio.ini`, and PlatformIO installs the right versions for each project
environment, keeps them separate between projects, and finds the ones your
code actually includes.

Libraries can come from the [PlatformIO Registry](https://registry.platformio.org/),
Git, Mercurial or Subversion repositories, archives, or local folders.

| Guide | What it covers |
| --- | --- |
| [Dependency management](./dependencies.md) | Declaring, installing and updating libraries |
| [Library Dependency Finder](./ldf.md) | How PlatformIO finds the libraries your code includes |
| [Create a library](./creating.md) | Structure, manifest and publishing of your own library |

<a id="configuration"></a>

## Configuration {#library-configuration}

Configure library management per project environment with these
[`platformio.ini` options](../../reference/platformio-ini/env/library-options.md):

| Option | Purpose |
| --- | --- |
| [`lib_deps`](../../reference/platformio-ini/env/lib-deps.md) | The libraries the environment depends on |
| [`lib_ignore`](../../reference/platformio-ini/env/lib-ignore.md) | Libraries to leave out |
| [`lib_extra_dirs`](../../reference/platformio-ini/env/lib-extra-dirs.md) | Extra folders to search for libraries |
| [`lib_ldf_mode`](../../reference/platformio-ini/env/lib-ldf-mode.md) | How the [Library Dependency Finder](./ldf.md#ldf-mode) scans the code |
| [`lib_compat_mode`](../../reference/platformio-ini/env/lib-compat-mode.md) | How strictly libraries must match the framework and platform |
| [`lib_archive`](../../reference/platformio-ini/env/lib-archive.md) | Whether libraries are built as static archives |

A library describes itself with a [`library.json`](../../reference/library-json/index.md)
manifest.
